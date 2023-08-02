# Node Interface - MacSec

## Fault view

```
# iserver get aci intf macsec --apic apic21 --node any --view fault

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

Interface MacSec - Faults [#0]
------------------------------
None
```

Developer

```
# iserver get aci intf macsec --apic apic21 --node any --view fault

{
    "duration": 39550,
    "apic": {
        "read": true,
        "success": 50,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 49,
        "connect_time": 526,
        "disconnect_time": 0,
        "mo_time": 36401,
        "total_time": 36927
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

True	526	-	connect apic21o.emea-sp.cisco.com:443
True	447	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	473	28	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1060	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	413	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	503	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree-include=faults,no-scoped,subtree
True	405	28	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1216	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	518	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ethpmPhysIf
True	533	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/macsecIf query rsp-subtree-include=faults,no-scoped,subtree
True	544	102	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	2253	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	422	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ethpmPhysIf
True	990	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/macsecIf query rsp-subtree-include=faults,no-scoped,subtree
True	543	102	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	2272	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	521	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ethpmPhysIf
True	1222	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/macsecIf query rsp-subtree-include=faults,no-scoped,subtree
True	584	48	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1479	60	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	458	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ethpmPhysIf
True	651	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/macsecIf query rsp-subtree-include=faults,no-scoped,subtree
True	509	48	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1353	60	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	492	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ethpmPhysIf
True	790	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/macsecIf query rsp-subtree-include=faults,no-scoped,subtree
True	441	28	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1366	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	395	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/ethpmPhysIf
True	488	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/macsecIf query rsp-subtree-include=faults,no-scoped,subtree
True	418	28	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1121	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	514	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/ethpmPhysIf
True	463	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/macsecIf query rsp-subtree-include=faults,no-scoped,subtree
True	506	51	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1520	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	435	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ethpmPhysIf
True	648	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/macsecIf query rsp-subtree-include=faults,no-scoped,subtree
True	502	51	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1868	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	463	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ethpmPhysIf
True	683	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/macsecIf query rsp-subtree-include=faults,no-scoped,subtree
True	395	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	825	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	365	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/ethpmPhysIf
True	374	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/macsecIf query rsp-subtree-include=faults,no-scoped,subtree
True	351	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	762	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	486	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/ethpmPhysIf
True	361	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/macsecIf query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./InterfaceMacSec.md)