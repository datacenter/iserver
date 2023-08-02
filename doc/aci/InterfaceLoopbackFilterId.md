# Node Interface - Loopback

## Filter by interface id

```
# iserver get aci intf lb --apic apic21 --node any --id lo8

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
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | lo8       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | lo8       | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| pod-1/s2101-eu-spdc  | 100    | 0 0 0 0 | lo8       | up          | up         | 10.5.0.34/32       | 0           | 4294967295          | 
| pod-1/s2102-eu-spdc  | 100    | 0 0 0 0 | lo8       | up          | up         | 10.5.0.34/32       | 0           | 4294967295          | 
+----------------------+--------+---------+-----------+-------------+------------+--------------------+-------------+---------------------+
```

Developer

```
# iserver get aci intf lb --apic apic21 --node any --id lo8

{
    "duration": 11869,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 511,
        "disconnect_time": 0,
        "mo_time": 10438,
        "total_time": 10949
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

True	511	-	connect apic21o.emea-sp.cisco.com:443
True	463	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	387	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	411	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4Addr
True	401	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	384	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ipv4Addr
True	394	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	423	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ipv4Addr
True	443	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	374	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ipv4Addr
True	473	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	427	30	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ipv4Addr
True	450	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	409	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	384	3	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	414	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/ipv4Addr
True	423	3	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	387	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/ipv4Addr
True	479	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	417	13	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ipv4Addr
True	414	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	449	14	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ipv4Addr
True	398	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	411	21	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/ipv4Addr
True	424	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	399	21	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/ipv4Addr
```

[[Back]](./InterfaceLoopback.md)