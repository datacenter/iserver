# Node Protocol - IS-IS

## Show instance summary for all nodes

```
# iserver get aci proto isis --apic apic11 --node any

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
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
    "duration": 6586,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 490,
        "disconnect_time": 0,
        "mo_time": 5782,
        "total_time": 6272
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
    }
}

Log: apic
----------

True	490	-	connect apic11o.emea-sp.cisco.com
True	298	11	apic11o.emea-sp.cisco.com class fabricNode
True	312	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/isis
True	347	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	331	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/isis
True	391	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	329	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis
True	355	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/isis
True	348	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	443	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	343	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/isis
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	314	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/isis
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/isis query query-target=subtree&target-subtree-class=isisDom
```

[[Back]](./ProtocolIsis.md)