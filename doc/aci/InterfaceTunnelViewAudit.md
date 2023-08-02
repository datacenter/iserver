# Node Interface - Tunnel

## Audit view

```
# iserver get aci intf tun
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view audit

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Tunnel - Audit Logs last 10y [#0]
-------------------------------------------
None
```

Developer

```
# iserver get aci intf tun
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view audit

{
    "duration": 1529,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 404,
        "disconnect_time": 0,
        "mo_time": 1003,
        "total_time": 1407
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

True	404	-	connect apic21o.emea-sp.cisco.com:443
True	277	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	330	22	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/tunnelIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	396	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/tunnelIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceTunnel.md)