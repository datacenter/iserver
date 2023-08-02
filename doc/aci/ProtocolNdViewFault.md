# Node Protocol - ND

## Fault view

```
# iserver get aci proto nd --apic apic11 --node bl205-eu-spdc --view fault

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol ND - Faults [#0]
-------------------------
None
```

Developer

```
# iserver get aci proto nd --apic apic11 --node bl205-eu-spdc --view fault

{
    "duration": 1075,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 377,
        "disconnect_time": 0,
        "mo_time": 591,
        "total_time": 968
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

True	377	-	connect apic11o.emea-sp.cisco.com:443
True	296	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	295	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./ProtocolNd.md)