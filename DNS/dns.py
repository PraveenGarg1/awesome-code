#!/usr/bin/python

###########################################
#    author : Praveen Garg                #
#    email  : praveengarg1405@gmail.com   #
###########################################

"""
This is a dummy dns server. For every DNS query, the DNS Server returns a
valid response v4/v6 based on the request type.
"""

import socket
import sys

import ipaddress
import yaml


class DNSQuery:
    def __init__(self, data):
        self.data = data
        self.domain = ''

        tipo = (ord(data[2]) >> 3) & 15  # Opcode bits
        if tipo == 0:  # Standard query
            ini = 12
            lon = ord(data[ini])
            while lon != 0:
                self.domain += data[ini + 1:ini + lon + 1] + '.'
                ini += lon + 1
                lon = ord(data[ini])

    def create_packet(self, ips_list, packet, proto, domain_pointer='\xc0\x0c'):
        for ip in ips_list:
            packet += domain_pointer  # Pointer to domain name
            if proto == "v4":
                packet += '\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04'  # Response type, ttl and resource data length -> 4 bytes
                packet += str.join('', map(lambda x: chr(int(x)), ip.split('.')))  # 4bytes of IP
            elif proto == "v6":
                v6addr = ipaddress.ip_address(unicode(ip))
                ipv6 = v6addr.exploded
                packet += '\x00\x1c\x00\x01\x00\x00\x00\x3c\x00\x10'  # Response type, ttl and resource data length -> 16 bytes
                packet += str.join('', map(lambda x: chr(int(x[:2], 16)) + chr(int(x[2:], 16)),
                                           ipv6.split(':')))  # 16bytes of IP
        return packet

    def reply(self, ips_list, proto):
        packet = ''
        if not ips_list:
            packet += self.data[:2] + "\x81\x83"
            packet += '\x00\x00\x00\x00\x00\x00\x00\x00'
            return packet
        if self.domain:
            packet += self.data[:2] + "\x81\x80"
            packet += self.data[4:6] + '\x00' + chr(len(ips_list)) + '\x00\x00\x00\x00'  # Questions and Answers Counts
            packet += self.data[12:]  # Original Domain Name Question
            packet = self.create_packet(ips_list, packet, proto)
        return packet

    def get_ip(self, proto, lists):
        ip = ""
        if proto:
            host = str(self.domain).rstrip('.')
            if host in lists[proto].keys():
                ip = str(lists[proto][host])
        return ip


def read_conffile(filename):
    conf = {}
    try:
        with open(filename, 'r') as fh:
            conf = yaml.load(fh)
    except:
        print >> sys.stderr, "Error reading config file: %s" % (filename)
    print conf
    return conf


if __name__ == '__main__':
    valueHash = {
        'port': 5055
    }

    lists = read_conffile('dns.yml')
    for key in valueHash.keys():
        if key not in lists:
            lists[key] = valueHash[key]

    udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udps.bind(('', int(lists['port'])))

    try:
        while 1:
            data, addr = udps.recvfrom(1024)
            p = DNSQuery(data)
            proto = ""
            if int(ord(data[-3])) == 1:
                proto = "v4"
            elif int(ord(data[-3])) == 28:
                proto = "v6"
            else:
                print 'Invalid Q-type'

            ips = p.get_ip(proto, lists)
            ips_list = ips if ips == "" else ips.split(',')
            udps.sendto(p.reply(ips_list, proto), addr)

            if ips == "" or proto == "":
                print "Can't resolve domain : %s" % (p.domain)
            else:
                print 'Resolving host : %s -> %s' % (p.domain, str(ips_list))

    except KeyboardInterrupt:
        print '\n^C Received, Shutting down the web server'
        udps.close()
        sys.exit(0)

