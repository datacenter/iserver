# Node Protocol - IS-IS

## Show instance summary for all nodes

```
# iserver get aci proto isis --apic apic11 --node any

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+-------------+------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
| Node                | Admin State | Oper State | Domain Name | Oper State | System ID         | Area | Protocol | Mode   | Max ECMP | Metric Style | MTU  |
+---------------------+-------------+------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
| pod-1/bl205-eu-spdc | enabled     | enabled    | overlay-1   | ok         | 40:C0:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
| pod-1/bl206-eu-spdc | enabled     | enabled    | overlay-1   | ok         | 40:20:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
| pod-1/cl201-eu-spdc | enabled     | enabled    | overlay-1   | ok         | 43:C0:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
| pod-1/cl202-eu-spdc | enabled     | enabled    | overlay-1   | ok         | 44:C0:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
| pod-1/cl209-eu-spdc | enabled     | enabled    | overlay-1   | ok         | 40:88:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
| pod-1/cl210-eu-spdc | enabled     | enabled    | overlay-1   | ok         | 41:88:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
| pod-1/rl301-eu-spdc | enabled     | enabled    | overlay-1   | ok         | A0:1E:10:AC:00:00 | 1    | ip       | fabric | 18       | wide         | 1492 | 
| pod-1/rl302-eu-spdc | enabled     | enabled    | overlay-1   | ok         | 78:1E:10:AC:00:00 | 1    | ip       | fabric | 18       | wide         | 1492 | 
| pod-1/s101-eu-spdc  | enabled     | enabled    | overlay-1   | ok         | 41:C0:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
| pod-1/s102-eu-spdc  | enabled     | enabled    | overlay-1   | ok         | 41:20:03:0A:00:00 | 1    | ip       | fabric | 18       | narrow       | 1492 | 
+---------------------+-------------+------------+-------------+------------+-------------------+------+----------+--------+----------+--------------+------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node any

{
    "duration": 7789,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 6837,
        "total_time": 7259
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

True	422	-	connect apic11o.emea-sp.cisco.com
True	299	13	apic11o.emea-sp.cisco.com class fabricNode
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/isis
True	311	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	328	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/isis
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	282	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/isis
True	326	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/isis
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	355	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/isis
True	335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	368	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	326	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis
True	328	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	329	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/isis
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/isis
True	295	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/isis query query-target=subtree&target-subtree-class=isisDom
```

[[Back]](./ProtocolIsis.md)