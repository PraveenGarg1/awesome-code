#!/bin/sh
set -e

# Supports Redis-Server: v=3.2.8
# Supports Redis-Cli: v=3.2.8

# Check if redis is present or not
type redis-cli >/dev/null 2>&1 || { echo >&2 "Please run the script on a redis node"; exit 1; }

# Cluster topology defines the cluster info on (master, slave, hash_slot, etc)
cluster_topology=$(redis-cli -c cluster nodes)

# Master nodes from the cluster topology
masters=$(echo "${cluster_topology}" | grep "master" | cut -d ' ' -f 2,9 | tr ' ' ',')

# Directory to store backups
rm -rf /opt/redis-backup
mkdir -p /opt/redis-backup/readable-dump

# https://redis.io/commands/cluster-nodes
for master in ${masters}
do
    # Master IP
    master_ip=$(echo "${master}" | cut -d ',' -f 1 | cut -d ':' -f 1)

    # Master Port
    master_port=$(echo "${master}" | cut -d ',' -f 1 | cut -d ':' -f 2)

    # Fetch the slots from the cluster topology for the master nodes
    slots=$(echo "${master}" | cut -d ',' -f 2 | awk '{print "["$0"]"}')

    printf "START BACKUP FOR %s\n" ${master_ip}:${master_port}

    # If master nodes and slots aren't available (0-16383 slots) in topology
    if [ -z "$master_ip" ] && [ -z "$slots" ]
    then
        printf "Can't find redis master or slots in topology\n%s\n" $cluster_topology
        exit 1
    fi

    # Synchronous (blocking) save of the dataset (Ensuring redis save all in-memory data)
    rdb_save=$(redis-cli -c -h ${master_ip} -p ${master_port} save)
    echo "Redis save status: " ${rdb_save}

    # Get recent dump.rdb from the replica nodes
    redis-cli --rdb dump.rdb -h ${master_ip} -p ${master_port} > /dev/null 2>&1

    # Check rdb file for consistency (redis-check-rdb)
    rdb_check=$(redis-check-rdb dump.rdb)

    echo ${rdb_check} > /dev/null 2>&1

    # If rdb is consistent, compress it and move to backup directory. Fail otherwise.
    if [ $? -eq 0 ]
    then
        backup_file_prefix=dump-${slots}-$(date '+%Y-%m-%d-%H:%M:%S')
        rdb --command diff dump.rdb > ${backup_file_prefix}.rdb-txt 2> /dev/null
        mv ${backup_file_prefix}.rdb-txt /opt/redis-backup/readable-dump
        gzip dump.rdb
        mv dump.rdb.gz /opt/redis-backup/${backup_file_prefix}.rdb.gz
    else
        failed_dump=dump-failed-${slots}-$(date '+%Y-%m-%d-%H:%M:%S').rdb
        printf "RDB check failed!"
        mv dump.rdb /opt/redis-backup/${failed_dump}
    fi
    printf "END BACKUP FOR %s\n\n" ${master_ip}:${master_port}
done

# Navigate to the directory containing readable dumps
cd /opt/redis-backup/readable-dump

# Concatenate and sort the whole file
cat *.rdb-txt | sort | grep -v "heartbeat" > redis-dump.txt

echo "Backup location: /opt/redis-backup"
