# Node Interface - Encapsulated Routed

## Audit view

```
# iserver get aci intf l3e
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view audit

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Encapsulated Routed - Audit Logs last 10y [#0]
--------------------------------------------------------
None
```

Developer

```
# iserver get aci intf l3e
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view audit

{
    "duration": 2480,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 544,
        "disconnect_time": 0,
        "mo_time": 1689,
        "total_time": 2233
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

True	544	-	connect apic21o.emea-sp.cisco.com:443
True	424	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	384	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	372	33	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4If
True	509	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceL3e.md)