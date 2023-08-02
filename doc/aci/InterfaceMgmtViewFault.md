# Node Interface - Management

## Fault view

```
# iserver get aci intf mgmt --apic apic21 --node any --view fault

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

Interface Management - Faults [#0]
----------------------------------
None
```

Developer

```
# iserver get aci intf mgmt --apic apic21 --node any --view fault

{
    "duration": 7685,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 378,
        "disconnect_time": 0,
        "mo_time": 6943,
        "total_time": 7321
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

True	378	-	connect apic21o.emea-sp.cisco.com:443
True	286	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	276	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	269	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/mgmtMgmtIf query rsp-subtree-include=faults,no-scoped,subtree
True	271	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	261	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/mgmtMgmtIf query rsp-subtree-include=faults,no-scoped,subtree
True	275	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	279	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/mgmtMgmtIf query rsp-subtree-include=faults,no-scoped,subtree
True	266	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	277	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/mgmtMgmtIf query rsp-subtree-include=faults,no-scoped,subtree
True	276	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	333	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/mgmtMgmtIf query rsp-subtree-include=faults,no-scoped,subtree
True	288	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	280	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/mgmtMgmtIf query rsp-subtree-include=faults,no-scoped,subtree
True	261	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	268	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/mgmtMgmtIf query rsp-subtree-include=faults,no-scoped,subtree
True	280	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	301	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/mgmtMgmtIf query rsp-subtree-include=faults,no-scoped,subtree
True	279	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	268	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/mgmtMgmtIf query rsp-subtree-include=faults,no-scoped,subtree
True	272	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	266	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/mgmtMgmtIf query rsp-subtree-include=faults,no-scoped,subtree
True	273	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	288	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/mgmtMgmtIf query rsp-subtree-include=faults,no-scoped,subtree
True	278	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	272	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/mgmtMgmtIf query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./InterfaceMgmt.md)