# Node Interface - Encapsulated Routed

## Fault view

```
# iserver get aci intf l3e --apic apic21 --node any --view fault

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

Interface Encapsulated Routed - Faults [#0]
-------------------------------------------
None
```

Developer

```
# iserver get aci intf l3e --apic apic21 --node any --view fault

{
    "duration": 18586,
    "apic": {
        "read": true,
        "success": 38,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 37,
        "connect_time": 618,
        "disconnect_time": 0,
        "mo_time": 16955,
        "total_time": 17573
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

True	618	-	connect apic21o.emea-sp.cisco.com:443
True	469	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	389	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	361	33	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4If
True	599	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	594	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	414	33	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ipv4If
True	478	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l3EncRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	459	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	486	35	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ipv4If
True	471	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l3EncRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	410	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	423	35	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ipv4If
True	484	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l3EncRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	399	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	385	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ipv4If
True	404	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l3EncRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	418	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	479	33	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4If
True	515	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l3EncRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	460	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	501	14	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/ipv4If
True	408	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l3EncRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	423	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	454	14	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/ipv4If
True	422	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l3EncRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	448	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	459	18	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ipv4If
True	435	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l3EncRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	401	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	428	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ipv4If
True	461	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l3EncRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	530	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	404	62	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/ipv4If
True	540	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l3EncRtdIf query rsp-subtree-include=faults,no-scoped,subtree
True	544	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	434	62	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/ipv4If
True	566	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l3EncRtdIf query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./InterfaceL3e.md)