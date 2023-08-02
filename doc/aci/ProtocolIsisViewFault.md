# Node Protocol - IS-IS

## Fault view

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view fault

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol ISIS - Faults [#0]
---------------------------
None
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view fault

{
    "duration": 1346,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 416,
        "disconnect_time": 0,
        "mo_time": 834,
        "total_time": 1250
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

True	416	-	connect apic11o.emea-sp.cisco.com:443
True	377	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	457	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./ProtocolIsis.md)