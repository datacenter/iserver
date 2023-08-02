# Node Protocol - ND

## Fault history view

```
# iserver get aci proto nd
    --apic apic11
    --node bl205-eu-spdc
    --view hfault
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol ND - Fault Records [#0]
--------------------------------
None
```

Developer

```
# iserver get aci proto nd
    --apic apic11
    --node bl205-eu-spdc
    --view hfault
    --when 90d

{
    "duration": 1318,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 394,
        "disconnect_time": 0,
        "mo_time": 821,
        "total_time": 1215
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

True	394	-	connect apic11o.emea-sp.cisco.com:443
True	297	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	524	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolNd.md)