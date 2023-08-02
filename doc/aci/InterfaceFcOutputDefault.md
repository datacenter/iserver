# Node Interface - Fc

## Default output

```
# iserver get aci intf fc --apic apic21 --node any

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

Interface Fc - State [#0]
-------------------------
None
```

Developer

```
# iserver get aci intf fc --apic apic21 --node any

{
    "duration": 6279,
    "apic": {
        "read": true,
        "success": 14,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 13,
        "connect_time": 656,
        "disconnect_time": 0,
        "mo_time": 5315,
        "total_time": 5971
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

True	656	-	connect apic21o.emea-sp.cisco.com:443
True	450	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	383	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1FcPhysIf query query-target=children&target-subtree-class=l1RtFcBrConf&rsp-subtree-include=health,fault-count,required
True	445	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l1FcPhysIf query query-target=children&target-subtree-class=l1RtFcBrConf&rsp-subtree-include=health,fault-count,required
True	358	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l1FcPhysIf query query-target=children&target-subtree-class=l1RtFcBrConf&rsp-subtree-include=health,fault-count,required
True	398	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l1FcPhysIf query query-target=children&target-subtree-class=l1RtFcBrConf&rsp-subtree-include=health,fault-count,required
True	384	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l1FcPhysIf query query-target=children&target-subtree-class=l1RtFcBrConf&rsp-subtree-include=health,fault-count,required
True	378	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l1FcPhysIf query query-target=children&target-subtree-class=l1RtFcBrConf&rsp-subtree-include=health,fault-count,required
True	391	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l1FcPhysIf query query-target=children&target-subtree-class=l1RtFcBrConf&rsp-subtree-include=health,fault-count,required
True	425	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l1FcPhysIf query query-target=children&target-subtree-class=l1RtFcBrConf&rsp-subtree-include=health,fault-count,required
True	474	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l1FcPhysIf query query-target=children&target-subtree-class=l1RtFcBrConf&rsp-subtree-include=health,fault-count,required
True	399	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l1FcPhysIf query query-target=children&target-subtree-class=l1RtFcBrConf&rsp-subtree-include=health,fault-count,required
True	434	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l1FcPhysIf query query-target=children&target-subtree-class=l1RtFcBrConf&rsp-subtree-include=health,fault-count,required
True	396	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l1FcPhysIf query query-target=children&target-subtree-class=l1RtFcBrConf&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceFc.md)