# Test DNS Server

This is a test DNS server. For every DNS query (Qtype=A/AAAA) the DNS server returns a valid Ipv4 or v6 addresses based 
on the request type. The DNS reads config from a yml file named `dns.yml`, which should be present in the same directory
that was used to launch the DNS.

The config file contains three params: `port`, `v4` and `v6`.

```
## port on which dns server listen DNS query
port: 5055

## host-ip mapping for Ipv4 addresses
v4:
  example.com: 10.123.10.1,10.123.10.4,10.10.1.2
  auth.com: 10.123.10.2,10.123.10.5
  test.com: 10.10.1.1

## host-ip mapping for Ipv6 addresses
v6:
  example.com: 2001:1234:a23b:ffff:21ac:1256:ced1:1123,2001::2222
  auth.com: 2001::1111
```

The dns server's command-line has the following structure:
```
python dns.py
```

It start the dns-server that will response for both type of request i.e A (ipv4) and AAAA (ipv6).

It is recommended to run the dns server in a terminal multiplexer like
`screen` or `tmux`. Send a DNS query to the DNS server (let's assume that dns server is running on 192.168.160.10)

for example:


DNS query for ipv4 i.e qtype=A:
```
nslookup -q=A example.com -port=5055 192.168.160.10
```

Sample Output:
```
Server:192.168.160.10
Address:192.168.160.10#5055

Non-authoritative answer:
Name:example.com
Address: 10.123.10.1
Name:example.com
Address: 10.123.10.4
Name:example.com
Address: 10.10.1.2
```

DNS query for ipv6 i.e qtype=AAAA:
```
nslookup -q=AAAA example.com -port=5055 192.168.160.10
```

Sample output:
```
Server:192.168.160.10
Address:192.168.160.10#5055

Non-authoritative answer:
example.comhas AAAA address 2001:1234:a23b:ffff:21ac:1256:ced1:1123
example.comhas AAAA address 2001::2222
```

DNS query for un-available domain:
```
nslookup -q=A dns.com -port=5055 192.168.160.10
```

Sample Output:
```
Server:192.168.160.10
Address:192.168.160.10#5055

** server can't find dns.com: NXDOMAIN
```
