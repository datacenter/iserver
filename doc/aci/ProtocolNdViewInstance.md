# Node Protocol - ND

## Inst view

```
# iserver get aci proto nd --apic apic11 --node bl205-eu-spdc --view inst

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol ND - Instance [#1]
---------------------------

+---------------------+--------+---------+-------------+----------------+----------------+------------------------+
| Node                | Health | Faults  | Admin State | Aging Interval | Neighbor Count | Active Interface Count |
+---------------------+--------+---------+-------------+----------------+----------------+------------------------+
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | enabled     | 1380           |                |                        | 
+---------------------+--------+---------+-------------+----------------+----------------+------------------------+
```

Developer

```
# iserver get aci proto nd --apic apic11 --node bl205-eu-spdc --view inst

{
    "duration": 1075,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 392,
        "disconnect_time": 0,
        "mo_time": 576,
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

True	392	-	connect apic11o.emea-sp.cisco.com:443
True	289	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	287	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd query query-target=children&rsp-subtree-include=health,fault-count
```

[[Back]](./ProtocolNd.md)