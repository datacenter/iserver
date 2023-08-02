# Node Interface - VFC

## Event view

```
# iserver get aci intf vfc
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view event

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Vfc - Event Logs last 10y [#0]
----------------------------------------
None
```

Developer

```
# iserver get aci intf vfc
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view event

{
    "duration": 1249,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 390,
        "disconnect_time": 0,
        "mo_time": 636,
        "total_time": 1026
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

True	390	-	connect apic21o.emea-sp.cisco.com:443
True	343	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	293	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l2VfcIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceVfc.md)