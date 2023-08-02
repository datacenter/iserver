# Node Interface - Loopback

## Audit view

```
# iserver get aci intf lb
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view audit

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Loopback - Audit Logs last 10y [#0]
---------------------------------------------
None
```

Developer

```
# iserver get aci intf lb
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view audit

{
    "duration": 2733,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 627,
        "disconnect_time": 0,
        "mo_time": 1858,
        "total_time": 2485
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

True	627	-	connect apic21o.emea-sp.cisco.com:443
True	497	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	411	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required
True	427	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4Addr
True	523	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3LbRtdIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceLoopback.md)