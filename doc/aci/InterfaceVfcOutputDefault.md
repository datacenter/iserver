# Node Interface - VFC

## Default output

```
# iserver get aci intf vfc --apic apic21 --node any

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

Interface Vfc - State [#0]
--------------------------
None
```

Developer

```
# iserver get aci intf vfc --apic apic21 --node any

{
    "duration": 4958,
    "apic": {
        "read": true,
        "success": 14,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 13,
        "connect_time": 458,
        "disconnect_time": 0,
        "mo_time": 3950,
        "total_time": 4408
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

True	458	-	connect apic21o.emea-sp.cisco.com:443
True	328	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	304	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l2VfcIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	301	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l2VfcIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	266	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l2VfcIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	286	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l2VfcIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	279	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l2VfcIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	331	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2VfcIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	286	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l2VfcIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	295	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l2VfcIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	337	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l2VfcIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	366	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l2VfcIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	274	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l2VfcIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	297	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l2VfcIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceVfc.md)