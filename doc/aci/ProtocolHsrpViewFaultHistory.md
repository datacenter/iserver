# Node Protocol - HSRP

## Fault history view

```
# iserver get aci proto hsrp
    --apic apic11
    --node cl201-eu-spdc
    --view hfault
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol HSRP - Event Logs [#0]
-------------------------------
None
```

Developer

```
# iserver get aci proto hsrp
    --apic apic11
    --node cl201-eu-spdc
    --view hfault
    --when 90d

{
    "duration": 2427,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 510,
        "disconnect_time": 0,
        "mo_time": 1701,
        "total_time": 2211
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

True	510	-	connect apic11o.emea-sp.cisco.com:443
True	1319	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	382	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/hsrp query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolHsrp.md)