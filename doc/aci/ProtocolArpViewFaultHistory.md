# Node Protocol - ARP

## Fault history view

```
# iserver get aci proto arp
    --apic apic21
    --node bl2205-eu-spdc
    --when any
    --view hfault

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Protocol ARP - Fault Records last 10y [#0]
------------------------------------------
None
```

Developer

```
# iserver get aci proto arp
    --apic apic21
    --node bl2205-eu-spdc
    --when any
    --view hfault

{
    "duration": 1150,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 407,
        "disconnect_time": 0,
        "mo_time": 563,
        "total_time": 970
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

True	407	-	connect apic21o.emea-sp.cisco.com:443
True	293	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	270	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/arp query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolArp.md)