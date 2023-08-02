# Node Interface - Management

## Audit view

```
# iserver get aci intf mgmt
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view audit

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Management - Audit Logs last 10y [#0]
-----------------------------------------------
None
```

Developer

```
# iserver get aci intf mgmt
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view audit

{
    "duration": 1497,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 363,
        "disconnect_time": 0,
        "mo_time": 1041,
        "total_time": 1404
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

True	363	-	connect apic21o.emea-sp.cisco.com:443
True	277	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	274	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	490	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/mgmtMgmtIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceMgmt.md)