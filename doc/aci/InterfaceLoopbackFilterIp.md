# Node Interface - Loopback

## Filter by ip address

```
# iserver get aci intf lb --apic apic21 --node any --ip 10.5.216.66

Apic: apic21 (mode:online, cache:off)
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: cl2209-eu-spdc
- node: cl2210-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

+----------------------+--------+---------+-----------+-------------+------------+--------------------+-------------+---------------------+
| Node                 | Health | Faults  | Interface | Admin State | Oper State | IPv4 Address       | Last Errors | Current Error Index |
+----------------------+--------+---------+-----------+-------------+------------+--------------------+-------------+---------------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.216.66/32     | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.65/32     | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo2       | up          | up         | 172.16.21.232/32   | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo3       | up          | up         | 125.125.125.125/32 | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo4       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo5       | up          | up         | 45.23.1.4/32       | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo6       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo7       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo8       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.216.64/32     | 0           | 4294967295          | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.65/32     | 0           | 4294967295          | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | lo2       | up          | up         | 172.16.21.233/32   | 0           | 4294967295          | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | lo3       | up          | up         | 33.223.33.2/32     | 0           | 4294967295          | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | lo4       | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | lo5       | up          | up         | 126.126.126.126/32 | 0           | 4294967295          | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | lo6       | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | lo7       | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | lo8       | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.80.96/32      | 0           | 4294967295          | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.64/32     | 0           | 4294967295          | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | lo2       | up          | up         | 172.16.21.231/32   | 0           | 4294967295          | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | lo3       | up          | up         | 172.24.2.251/32    | 0           | 4294967295          | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | lo4       | up          | up         | 172.24.2.253/32    | 0           | 4294967295          | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | lo5       | up          | up         | 203.203.203.203/32 | 0           | 4294967295          | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | lo6       | up          | up         | 201.201.201.201/32 | 0           | 4294967295          | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.216.67/32     | 0           | 4294967295          | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.64/32     | 0           | 4294967295          | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | lo2       | up          | up         | 172.16.21.234/32   | 0           | 4294967295          | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | lo3       | up          | up         | 172.24.2.250/32    | 0           | 4294967295          | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | lo4       | up          | up         | 172.24.2.252/32    | 0           | 4294967295          | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | lo5       | up          | up         | 204.204.204.204/32 | 0           | 4294967295          | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | lo6       | up          | up         | 202.202.202.202/32 | 0           | 4294967295          | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.240.34/32     | 0           | 4294967295          | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.66/32     | 0           | 4294967295          | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | lo2       | up          | up         | 172.16.21.237/32   | 0           | 4294967295          | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | lo3       | up          | up         | 207.207.207.207/32 | 0           | 4294967295          | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | lo4       | up          | up         | 207.207.207.207/32 | 0           | 4294967295          | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.240.35/32     | 0           | 4294967295          | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.66/32     | 0           | 4294967295          | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | lo2       | up          | up         | 172.16.21.235/32   | 0           | 4294967295          | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | lo3       | up          | up         | 208.208.208.208/32 | 0           | 4294967295          | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | lo4       | up          | up         | 208.208.208.208/32 | 0           | 4294967295          | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
| pod-1/cl2209-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.216.65/32     | 0           | 4294967295          | 
| pod-1/cl2209-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.67/32     | 0           | 4294967295          | 
| pod-1/cl2209-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
| pod-1/cl2210-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.216.68/32     | 0           | 4294967295          | 
| pod-1/cl2210-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.67/32     | 0           | 4294967295          | 
| pod-1/cl2210-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
| pod-1/rl2701-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 172.16.70.208/32   | 0           | 4294967295          | 
| pod-1/rl2701-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 171.171.171.171/32 | 0           | 4294967295          | 
| pod-1/rl2701-eu-spdc | 100    | 0 0 0 0 | lo2       | up          | up         | 172.16.70.209/32   | 0           | 4294967295          | 
| pod-1/rl2701-eu-spdc | 100    | 0 0 0 0 | lo3       | up          | up         | 172.16.70.232/32   | 0           | 4294967295          | 
| pod-1/rl2701-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 172.16.70.32/32    | 0           | 4294967295          | 
| pod-1/rl2702-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 172.16.70.24/32    | 0           | 4294967295          | 
| pod-1/rl2702-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 172.172.172.172/32 | 0           | 4294967295          | 
| pod-1/rl2702-eu-spdc | 100    | 0 0 0 0 | lo2       | up          | up         | 172.16.70.25/32    | 0           | 4294967295          | 
| pod-1/rl2702-eu-spdc | 100    | 0 0 0 0 | lo3       | up          | up         | 172.16.70.232/32   | 0           | 4294967295          | 
| pod-1/rl2702-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 172.16.70.32/32    | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.80.97/32      | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.80.65/32      | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo2       | up          | up         | 10.5.160.71/32     | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo3       | up          | up         | 10.5.80.66/32      | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo4       | up          | up         | 10.5.160.70/32     | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo5       | up          | up         | 10.5.80.64/32      | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo6       | up          | up         | 10.5.160.69/32     | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo7       | up          | up         | 10.5.0.33/32       | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo8       | up          | up         | 10.5.0.34/32       | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo9       | up          | up         | 10.5.0.35/32       | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo10      | up          | up         | 172.16.21.238/32   | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo11      | up          | up         | 172.16.21.2/32     | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo12      | up          | up         | 172.16.21.239/32   | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo13      | up          | up         | 172.16.21.240/32   | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo14      | up          | up         | 172.16.21.230/32   | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo15      | up          | up         | 172.16.21.1/32     | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo16      | up          | up         | 172.16.22.1/32     | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo17      | up          | up         | 111.111.111.111/32 | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo18      | up          | up         | 10.58.50.181/32    | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.80.98/32      | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.80.65/32      | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo2       | up          | up         | 10.5.80.66/32      | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo3       | up          | up         | 10.5.160.66/32     | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo4       | up          | up         | 10.5.80.64/32      | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo5       | up          | up         | 10.5.160.65/32     | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo6       | up          | up         | 10.5.160.67/32     | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo7       | up          | up         | 10.5.0.33/32       | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo8       | up          | up         | 10.5.0.34/32       | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo9       | up          | up         | 10.5.0.35/32       | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo10      | up          | up         | 172.16.21.236/32   | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo11      | up          | up         | 172.16.21.2/32     | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo12      | up          | up         | 172.16.21.239/32   | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo13      | up          | up         | 172.16.21.240/32   | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo14      | up          | up         | 172.16.21.230/32   | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo15      | up          | up         | 172.16.21.1/32     | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo16      | up          | up         | 172.16.22.1/32     | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo17      | up          | up         | 112.112.112.112/32 | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo18      | up          | up         | 10.58.50.182/32    | 0           | 4294967295          | 
+----------------------+--------+---------+-----------+-------------+------------+--------------------+-------------+---------------------+
```

Developer

```
# iserver get aci intf lb --apic apic21 --node any --ip 10.5.216.66

{
    "duration": 12004,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 557,
        "disconnect_time": 0,
        "mo_time": 10209,
        "total_time": 10766
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

True	557	-	connect apic21o.emea-sp.cisco.com:443
True	431	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	383	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	447	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4Addr
True	388	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	385	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ipv4Addr
True	398	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	386	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ipv4Addr
True	387	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	390	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ipv4Addr
True	396	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	419	30	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ipv4Addr
True	535	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	425	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	385	3	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	393	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/ipv4Addr
True	384	3	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	387	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/ipv4Addr
True	416	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	401	13	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ipv4Addr
True	422	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	433	14	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ipv4Addr
True	403	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	385	21	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/ipv4Addr
True	449	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	381	21	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/ipv4Addr
```

[[Back]](./InterfaceLoopback.md)