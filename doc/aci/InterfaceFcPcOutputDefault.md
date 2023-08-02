# Node Interface - FcPc

## Default output

```
# iserver get aci intf fcpc --apic apic21 --node any

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

Interface FcPc - State [#0]
---------------------------
None
```

Developer

```
# iserver get aci intf fcpc --apic apic21 --node any

{
    "duration": 6706,
    "apic": {
        "read": true,
        "success": 14,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 13,
        "connect_time": 606,
        "disconnect_time": 0,
        "mo_time": 5815,
        "total_time": 6421
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

True	606	-	connect apic21o.emea-sp.cisco.com:443
True	467	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	390	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcFcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	428	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/pcFcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	567	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/pcFcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	480	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/pcFcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	491	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/pcFcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	439	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/pcFcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	407	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/pcFcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	406	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/pcFcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	498	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/pcFcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	380	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/pcFcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	447	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/pcFcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	415	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/pcFcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceFcPc.md)