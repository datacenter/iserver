# Node Interface - Loopback

## Filter by ip subnet

```
# iserver get aci intf lb --apic apic21 --node any --subnet 10.5.0.0/16

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

+----------------------+--------+---------+-----------+-------------+------------+----------------+-------------+---------------------+
| Node                 | Health | Faults  | Interface | Admin State | Oper State | IPv4 Address   | Last Errors | Current Error Index |
+----------------------+--------+---------+-----------+-------------+------------+----------------+-------------+---------------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.216.66/32 | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.65/32 | 0           | 4294967295          | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32   | 0           | 4294967295          | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.216.64/32 | 0           | 4294967295          | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.65/32 | 0           | 4294967295          | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32   | 0           | 4294967295          | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.80.96/32  | 0           | 4294967295          | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.64/32 | 0           | 4294967295          | 
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32   | 0           | 4294967295          | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.216.67/32 | 0           | 4294967295          | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.64/32 | 0           | 4294967295          | 
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32   | 0           | 4294967295          | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.240.34/32 | 0           | 4294967295          | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.66/32 | 0           | 4294967295          | 
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32   | 0           | 4294967295          | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.240.35/32 | 0           | 4294967295          | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.66/32 | 0           | 4294967295          | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32   | 0           | 4294967295          | 
| pod-1/cl2209-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.216.65/32 | 0           | 4294967295          | 
| pod-1/cl2209-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.67/32 | 0           | 4294967295          | 
| pod-1/cl2209-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32   | 0           | 4294967295          | 
| pod-1/cl2210-eu-spdc | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.216.68/32 | 0           | 4294967295          | 
| pod-1/cl2210-eu-spdc | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.192.67/32 | 0           | 4294967295          | 
| pod-1/cl2210-eu-spdc | 100    | 0 0 0 0 | lo1023    | up          | up         | 10.5.0.32/32   | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.80.97/32  | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.80.65/32  | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo2       | up          | up         | 10.5.160.71/32 | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo3       | up          | up         | 10.5.80.66/32  | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo4       | up          | up         | 10.5.160.70/32 | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo5       | up          | up         | 10.5.80.64/32  | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo6       | up          | up         | 10.5.160.69/32 | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo7       | up          | up         | 10.5.0.33/32   | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo8       | up          | up         | 10.5.0.34/32   | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo9       | up          | up         | 10.5.0.35/32   | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo0       | up          | up         | 10.5.80.98/32  | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo1       | up          | up         | 10.5.80.65/32  | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo2       | up          | up         | 10.5.80.66/32  | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo3       | up          | up         | 10.5.160.66/32 | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo4       | up          | up         | 10.5.80.64/32  | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo5       | up          | up         | 10.5.160.65/32 | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo6       | up          | up         | 10.5.160.67/32 | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo7       | up          | up         | 10.5.0.33/32   | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo8       | up          | up         | 10.5.0.34/32   | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo9       | up          | up         | 10.5.0.35/32   | 0           | 4294967295          | 
+----------------------+--------+---------+-----------+-------------+------------+----------------+-------------+---------------------+
```

Developer

```
# iserver get aci intf lb --apic apic21 --node any --subnet 10.5.0.0/16

{
    "duration": 11196,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 654,
        "disconnect_time": 0,
        "mo_time": 9841,
        "total_time": 10495
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

True	654	-	connect apic21o.emea-sp.cisco.com:443
True	405	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	394	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	377	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4Addr
True	390	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	382	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ipv4Addr
True	380	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	395	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ipv4Addr
True	384	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	416	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ipv4Addr
True	398	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	432	30	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ipv4Addr
True	385	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	372	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	382	3	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	372	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/ipv4Addr
True	412	3	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	422	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/ipv4Addr
True	373	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	375	13	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ipv4Addr
True	394	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	368	14	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ipv4Addr
True	414	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	373	21	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/ipv4Addr
True	466	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	380	21	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/ipv4Addr
```

[[Back]](./InterfaceLoopback.md)