# Node Protocol - HSRP

## Fault view

```
# iserver get aci proto hsrp --apic apic11 --node cl201-eu-spdc --view fault

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol HSRP - Event Logs [#0]
-------------------------------
None
```

Developer

```
# iserver get aci proto hsrp --apic apic11 --node cl201-eu-spdc --view fault

{
    "duration": 1109,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 391,
        "disconnect_time": 0,
        "mo_time": 604,
        "total_time": 995
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

True	391	-	connect apic11o.emea-sp.cisco.com:443
True	296	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	308	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/hsrp query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./ProtocolHsrp.md)