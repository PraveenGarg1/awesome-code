###
# pip install redis==2.10.6
# pip install redis-py-cluster==1.3.4

# python clean.py <ip_of_any_redis_node> <redis_port>
# python clean.py 192.168.134.213 6379

from rediscluster import StrictRedisCluster
import sys
startup_nodes = [{"host": sys.argv[1], "port": sys.argv[2]}]
rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)

rc.flushdb()
print("DB cleaned")
print(rc.dbsize())