# Node Protocol - IS-IS

## Show instance summary for selected nodes

```
# iserver get aci proto isis --apic apic11 --node rl

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-------------+------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
| Node                | Admin State | Oper State | Domain Name | Oper State | System ID         | Area | Protocol | Mode   | Max ECMP | Metric Style | MTU  |
+---------------------+-------------+------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
| pod-1/rl301-eu-spdc | enabled     | enabled    | overlay-1   | ok         | A0:1E:10:AC:00:00 | 1    | ip       | fabric | 18       | wide         | 1492 | 
| pod-1/rl302-eu-spdc | enabled     | enabled    | overlay-1   | ok         | 78:1E:10:AC:00:00 | 1    | ip       | fabric | 18       | wide         | 1492 | 
+---------------------+-------------+------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node rl

{
    "duration": 2796,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 382,
        "disconnect_time": 0,
        "mo_time": 2148,
        "total_time": 2530
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

True	382	-	connect apic11o.emea-sp.cisco.com
True	295	13	apic11o.emea-sp.cisco.com class fabricNode
True	953	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis
True	312	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	283	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis query query-target=subtree&target-subtree-class=isisDom
```

[[Back]](./ProtocolIsis.md)