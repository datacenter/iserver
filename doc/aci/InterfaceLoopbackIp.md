# Node Interface - Loopback

## Filter by ip address

```
# iserver get aci intf lb --apic apic11 --node any --ip 10.3.0.32

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
| Node                | Interface | Admin State | Oper State | IPv4 Address       | Last Errors | Current Error Index |
+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
| pod-1/bl205-eu-spdc | lo0       | up          | up         | 10.3.192.64/32     | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo1       | up          | up         | 172.16.11.233/32   | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo2       | up          | up         | 10.3.48.64/32      | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo3       | up          | up         | 172.31.2.25/32     | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo4       | up          | up         | 115.115.115.115/32 | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo5       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo6       | up          | up         | 205.205.205.15/32  | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo7       | up          | up         | 205.205.205.25/32  | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo8       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo9       | up          | up         | 172.24.0.253/32    | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo10      | up          | up         | 172.24.0.15/32     | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32       | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo0       | up          | up         | 10.3.32.64/32      | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo1       | up          | up         | 172.16.11.237/32   | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo2       | up          | up         | 172.31.2.26/32     | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo3       | up          | up         | 10.3.48.64/32      | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo4       | up          | up         | 172.24.0.252/32    | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo5       | up          | up         | 116.116.116.116/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo6       | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo7       | up          | up         | 124.124.124.124/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo8       | up          | up         | 172.24.0.14/32     | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo9       | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo10      | up          | up         | 206.206.206.15/32  | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo11      | up          | up         | 118.118.118.118/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo12      | up          | up         | 122.122.122.122/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo13      | up          | up         | 206.206.206.25/32  | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo14      | up          | up         | 120.120.120.120/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32       | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo0       | up          | up         | 10.3.192.67/32     | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo1       | up          | up         | 172.16.11.232/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo2       | up          | up         | 10.3.40.67/32      | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo3       | up          | up         | 172.30.4.0/32      | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo4       | up          | up         | 201.201.201.201/32 | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo5       | up          | up         | 121.121.121.121/32 | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo6       | up          | up         | 15.254.101.8/32    | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo7       | up          | up         | 15.254.101.6/32    | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo8       | up          | up         | 15.254.101.0/32    | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo9       | up          | up         | 15.254.101.4/32    | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo10      | up          | up         | 15.254.101.99/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo11      | up          | up         | 201.201.201.201/32 | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo12      | up          | up         | 15.254.101.2/32    | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo13      | up          | up         | 121.121.121.121/32 | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32       | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo0       | up          | up         | 10.3.192.68/32     | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo1       | up          | up         | 172.16.11.231/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo2       | up          | up         | 10.3.40.67/32      | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo3       | up          | up         | 172.30.4.1/32      | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo4       | up          | up         | 15.254.101.9/32    | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo5       | up          | up         | 15.254.101.5/32    | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo6       | up          | up         | 15.254.101.100/32  | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo7       | up          | up         | 15.254.101.1/32    | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo8       | up          | up         | 202.202.202.202/32 | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo9       | up          | up         | 122.122.122.122/32 | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo10      | up          | up         | 122.122.122.122/32 | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo11      | up          | up         | 15.254.101.7/32    | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo12      | up          | up         | 15.254.101.3/32    | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo13      | up          | up         | 202.202.202.202/32 | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32       | 0           | 4294967295          | 
| pod-1/cl209-eu-spdc | lo0       | up          | up         | 10.3.136.64/32     | 0           | 4294967295          | 
| pod-1/cl209-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32       | 0           | 4294967295          | 
| pod-1/cl210-eu-spdc | lo0       | up          | up         | 10.3.136.65/32     | 0           | 4294967295          | 
| pod-1/cl210-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32       | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo0       | up          | up         | 172.16.30.160/32   | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo1       | up          | up         | 131.131.131.131/32 | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo2       | up          | up         | 172.16.30.161/32   | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo3       | up          | up         | 172.31.3.31/32     | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo4       | up          | up         | 172.16.30.88/32    | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo5       | up          | up         | 172.30.4.4/32      | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo6       | up          | up         |                    | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo7       | up          | up         | 131.131.131.131/32 | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo8       | up          | up         | 131.131.131.131/32 | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo9       | up          | up         | 172.24.3.15/32     | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo1023    | up          | up         | 172.16.30.32/32    | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo0       | up          | up         | 172.16.30.120/32   | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo1       | up          | up         | 132.132.132.132/32 | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo2       | up          | up         | 172.16.30.121/32   | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo3       | up          | up         | 172.31.3.32/32     | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo4       | up          | up         | 172.16.30.88/32    | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo5       | up          | up         | 172.30.4.5/32      | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo6       | up          | up         |                    | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo7       | up          | up         | 132.132.132.132/32 | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo8       | up          | up         | 172.24.3.14/32     | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo9       | up          | up         | 132.132.132.132/32 | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo1023    | up          | up         | 172.16.30.32/32    | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo0       | up          | up         | 10.3.192.65/32     | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo1       | up          | up         | 10.3.0.33/32       | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo2       | up          | up         | 10.3.0.34/32       | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo3       | up          | up         | 10.3.0.35/32       | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo4       | up          | up         | 172.16.11.236/32   | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo5       | up          | up         | 172.16.11.228/32   | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo6       | up          | up         | 172.16.11.225/32   | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo7       | up          | up         | 172.16.11.226/32   | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo8       | up          | up         | 172.16.10.1/32     | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo9       | up          | up         | 172.16.1.1/32      | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo10      | up          | up         | 172.16.11.227/32   | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo11      | up          | up         | 10.3.40.65/32      | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo12      | up          | up         | 10.3.192.101/32    | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo13      | up          | up         | 10.3.40.64/32      | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo14      | up          | up         | 10.3.192.102/32    | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo15      | up          | up         | 172.16.11.1/32     | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo16      | up          | up         | 172.16.12.1/32     | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo17      | up          | up         | 101.101.101.101/32 | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo18      | up          | up         | 10.3.40.66/32      | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo19      | up          | up         | 10.3.192.103/32    | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo20      | up          | up         | 10.58.28.181/32    | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo0       | up          | up         | 10.3.32.65/32      | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo1       | up          | up         | 10.3.0.33/32       | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo2       | up          | up         | 10.3.0.34/32       | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo3       | up          | up         | 10.3.0.35/32       | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo4       | up          | up         | 172.16.11.236/32   | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo5       | up          | up         | 172.16.11.1/32     | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo6       | up          | up         | 172.16.11.225/32   | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo7       | up          | up         | 172.16.11.226/32   | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo8       | up          | up         | 172.16.10.1/32     | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo9       | up          | up         | 172.16.1.1/32      | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo10      | up          | up         | 172.16.11.227/32   | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo11      | up          | up         | 10.3.40.65/32      | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo12      | up          | up         | 10.3.152.65/32     | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo13      | up          | up         | 10.3.40.64/32      | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo14      | up          | up         | 10.3.152.66/32     | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo15      | up          | up         | 172.16.12.1/32     | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo16      | up          | up         | 102.102.102.102/32 | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo17      | up          | up         | 10.3.40.66/32      | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo18      | up          | up         | 10.3.152.67/32     | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo19      | up          | up         | 10.58.28.182/32    | 0           | 4294967295          | 
+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
```

Developer

```
# iserver get aci intf lb --apic apic11 --node any --ip 10.3.0.32

{
    "duration": 7418,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 403,
        "disconnect_time": 0,
        "mo_time": 6358,
        "total_time": 6761
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	403	-	connect apic11o.emea-sp.cisco.com
True	303	13	apic11o.emea-sp.cisco.com class fabricNode
True	295	12	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	302	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
True	290	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	294	63	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4Addr
True	296	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	300	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	304	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	300	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
True	281	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	294	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ipv4Addr
True	291	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	309	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ipv4Addr
True	301	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	375	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4Addr
True	296	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	296	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4Addr
True	316	21	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	292	23	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4Addr
True	300	20	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	323	22	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4Addr
```

[[Back]](./InterfaceLoopback.md)