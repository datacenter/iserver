# Node Protocol - ND

## Diag view

```
# iserver get aci proto nd
    --apic apic11
    --node bl205-eu-spdc
    --view diag
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol ND - Faults [#0]
-------------------------
None

Protocol ND - Fault Records [#0]
--------------------------------
None

Protocol ND - Event Logs [#0]
-----------------------------
None
```

Developer

```
# iserver get aci proto nd
    --apic apic11
    --node bl205-eu-spdc
    --view diag
    --when 90d

{
    "duration": 1774,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 398,
        "disconnect_time": 0,
        "mo_time": 1259,
        "total_time": 1657
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

True	398	-	connect apic11o.emea-sp.cisco.com:443
True	296	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	284	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd query rsp-subtree-include=faults,no-scoped,subtree
True	337	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	342	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolNd.md)