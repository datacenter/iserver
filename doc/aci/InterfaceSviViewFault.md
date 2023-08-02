# Node Interface - SVI

## Fault view

```
# iserver get aci intf svi --apic apic21 --node any --view fault

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

Interface SVI - Faults [#0]
---------------------------
None
```

Developer

```
# iserver get aci intf svi --apic apic21 --node any --view fault

{
    "duration": 11937,
    "apic": {
        "read": true,
        "success": 36,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 35,
        "connect_time": 368,
        "disconnect_time": 0,
        "mo_time": 10887,
        "total_time": 11255
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

True	368	-	connect apic21o.emea-sp.cisco.com:443
True	272	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	323	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	262	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4Addr
True	302	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l2BD query rsp-subtree-include=faults,no-scoped,subtree
True	319	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	269	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ipv4Addr
True	331	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l2BD query rsp-subtree-include=faults,no-scoped,subtree
True	373	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	287	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ipv4Addr
True	366	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l2BD query rsp-subtree-include=faults,no-scoped,subtree
True	410	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	324	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ipv4Addr
True	388	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l2BD query rsp-subtree-include=faults,no-scoped,subtree
True	402	20	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	311	30	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ipv4Addr
True	370	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l2BD query rsp-subtree-include=faults,no-scoped,subtree
True	378	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	308	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	391	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree-include=faults,no-scoped,subtree
True	312	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	273	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/ipv4Addr
True	274	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l2BD query rsp-subtree-include=faults,no-scoped,subtree
True	277	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	267	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/ipv4Addr
True	294	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l2BD query rsp-subtree-include=faults,no-scoped,subtree
True	301	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	257	13	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ipv4Addr
True	281	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l2BD query rsp-subtree-include=faults,no-scoped,subtree
True	312	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	298	14	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ipv4Addr
True	296	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l2BD query rsp-subtree-include=faults,no-scoped,subtree
True	270	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	262	21	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/ipv4Addr
True	266	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	261	21	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/ipv4Addr
```

[[Back]](./InterfaceSvi.md)