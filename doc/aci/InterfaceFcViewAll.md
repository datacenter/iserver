# Node Interface - Fc

## All view

```
# iserver get aci intf fc
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view all

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Fc - State [#0]
-------------------------
None

Interface Fc - Faults [#0]
--------------------------
None

Interface Fc - Fault Records last 10y [#0]
------------------------------------------
None

Interface Fc - Event Logs last 10y [#0]
---------------------------------------
None

Interface Fc - Audit Logs last 10y [#0]
---------------------------------------
None
```

Developer

```
# iserver get aci intf fc
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view all

{
    "duration": 1688,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 681,
        "disconnect_time": 0,
        "mo_time": 815,
        "total_time": 1496
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

True	681	-	connect apic21o.emea-sp.cisco.com:443
True	430	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	385	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1FcPhysIf query query-target=children&target-subtree-class=l1RtFcBrConf&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceFc.md)