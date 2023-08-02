# Node Interface - Loopback

## Fault view

```
# iserver get aci intf lb --apic apic21 --node any --view fault

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

Interface Loopback - Faults [#0]
--------------------------------
None
```

Developer

```
# iserver get aci intf lb --apic apic21 --node any --view fault

{
    "duration": 17654,
    "apic": {
        "read": true,
        "success": 38,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 37,
        "connect_time": 552,
        "disconnect_time": 0,
        "mo_time": 15956,
        "total_time": 16508
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

True	552	-	connect apic21o.emea-sp.cisco.com:443
True	419	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	397	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	411	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4Addr
True	426	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	371	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	456	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ipv4Addr
True	532	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l3LbRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	386	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	417	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ipv4Addr
True	419	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l3LbRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	452	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	443	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ipv4Addr
True	495	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l3LbRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	378	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	383	30	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ipv4Addr
True	436	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l3LbRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	389	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	371	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	508	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l3LbRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	452	3	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	382	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/ipv4Addr
True	461	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l3LbRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	433	3	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	413	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/ipv4Addr
True	379	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l3LbRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	402	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	415	13	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ipv4Addr
True	472	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l3LbRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	413	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	470	14	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ipv4Addr
True	500	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l3LbRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	416	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	504	21	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/ipv4Addr
True	515	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l3LbRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	399	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	392	21	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/ipv4Addr
True	449	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l3LbRtdIf query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./InterfaceLoopback.md)