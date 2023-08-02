# Node Protocol - IS-IS

## Fault history view

```
# iserver get aci proto isis
    --apic apic11
    --node cl201-eu-spdc
    --view hfault
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol ISIS - Fault Records [#0]
----------------------------------
None
```

Developer

```
# iserver get aci proto isis
    --apic apic11
    --node cl201-eu-spdc
    --view hfault
    --when 90d

{
    "duration": 1151,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 388,
        "disconnect_time": 0,
        "mo_time": 669,
        "total_time": 1057
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

True	388	-	connect apic11o.emea-sp.cisco.com:443
True	292	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	377	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolIsis.md)