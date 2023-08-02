# Node Interface - Physical

## Audit view

```
# iserver get aci intf phy
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view audit

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Phy - Audit Logs last 10y [#0]
----------------------------------------
None
Interface context: phy
```

Developer

```
# iserver get aci intf phy
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view audit

{
    "duration": 3129,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 412,
        "disconnect_time": 0,
        "mo_time": 2338,
        "total_time": 2750
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

True	412	-	connect apic21o.emea-sp.cisco.com:443
True	304	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1148	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	329	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	557	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfacePhy.md)