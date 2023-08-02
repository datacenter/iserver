# Node Protocol - ND

## Event view

```
# iserver get aci proto nd
    --apic apic11
    --node bl205-eu-spdc
    --view event
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol ND - Event Logs [#0]
-----------------------------
None
```

Developer

```
# iserver get aci proto nd
    --apic apic11
    --node bl205-eu-spdc
    --view event
    --when 90d

{
    "duration": 1191,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 404,
        "disconnect_time": 0,
        "mo_time": 681,
        "total_time": 1085
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

True	404	-	connect apic11o.emea-sp.cisco.com:443
True	340	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	341	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolNd.md)