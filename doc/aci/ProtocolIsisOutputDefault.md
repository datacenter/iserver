# Node Protocol - IS-IS

## Default output

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view inst

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol ISIS - Instance [#1]
-----------------------------

+---------------------+--------+---------+-------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
| Node                | Health | Faults  | Admin State | Domain Name | Oper State | System ID         | Area | Protocol | Mode   | Max ECMP | Metric Style | MTU  |
+---------------------+--------+---------+-------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | enabled     | overlay-1   | ok         | 43:C0:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
+---------------------+--------+---------+-------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view inst

{
    "duration": 1494,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 411,
        "disconnect_time": 0,
        "mo_time": 907,
        "total_time": 1318
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

True	411	-	connect apic11o.emea-sp.cisco.com:443
True	313	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	298	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis query query-target=children&rsp-subtree-include=health,fault-count
True	296	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
```

[[Back]](./ProtocolIsis.md)