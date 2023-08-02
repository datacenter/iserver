# Node Interface - Fc

## Fault view

```
# iserver get aci intf fc --apic apic21 --view fault

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Fc - Faults [#0]
--------------------------
None
```

Developer

```
# iserver get aci intf fc --apic apic21 --view fault

{
    "duration": 2142,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 586,
        "disconnect_time": 0,
        "mo_time": 1375,
        "total_time": 1961
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

True	586	-	connect apic21o.emea-sp.cisco.com:443
True	538	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	837	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1FcPhysIf query query-target=children&target-subtree-class=l1RtFcBrConf&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceFc.md)