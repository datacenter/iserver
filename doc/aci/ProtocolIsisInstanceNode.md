# Node Protocol - IS-IS

## Show instance summary for selected node

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+-------------+------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
| Node                | Admin State | Oper State | Domain Name | Oper State | System ID         | Area | Protocol | Mode   | Max ECMP | Metric Style | MTU  |
+---------------------+-------------+------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
| pod-1/cl201-eu-spdc | enabled     | enabled    | overlay-1   | ok         | 43:C0:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
+---------------------+-------------+------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc

{
    "duration": 1528,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 430,
        "disconnect_time": 0,
        "mo_time": 934,
        "total_time": 1364
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

True	430	-	connect apic11o.emea-sp.cisco.com
True	316	13	apic11o.emea-sp.cisco.com class fabricNode
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis
True	311	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
```

[[Back]](./ProtocolIsis.md)