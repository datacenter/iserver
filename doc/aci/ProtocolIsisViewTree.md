# Node Protocol - IS-IS

## Tree view

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view tree

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol ISIS - Tree [#16]
--------------------------

+---------------------+---------+----+--------------+-------------+----------+--------+----------------+------------+
| Node                | Domain  | Id | Root Address | Root Port   | Diameter | Origin | Diameter Alert | Oper State |
+---------------------+---------+----+--------------+-------------+----------+--------+----------------+------------+
| pod-1/cl201-eu-spdc | overlay | 0  | 10.3.32.65   | eth1/108.8  | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 1  | 10.3.32.65   | eth1/108.8  | 6        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 2  | 10.3.32.65   | eth1/108.8  | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 3  | 10.3.32.65   | eth1/108.8  | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 4  | 10.3.32.65   | eth1/108.8  | 6        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 5  | 10.3.192.65  | eth1/107.7  | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 6  | 10.3.192.65  | eth1/107.7  | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 7  | 10.3.192.65  | eth1/107.7  | 6        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 8  | 10.3.192.65  | eth1/107.7  | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 9  | 10.3.192.65  | eth1/107.7  | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 10 | 10.3.192.65  | eth1/107.7  | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 11 | 10.3.32.65   | eth1/108.8  | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 12 | 10.3.32.65   | eth1/108.8  | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 13 | 0.0.0.0      | unspecified | 0        | static | inactive       | inactive   | 
| pod-1/cl201-eu-spdc | overlay | 14 | 0.0.0.0      | unspecified | 0        | static | inactive       | inactive   | 
| pod-1/cl201-eu-spdc | overlay | 15 | 0.0.0.0      | unspecified | 0        | static | inactive       | inactive   | 
+---------------------+---------+----+--------------+-------------+----------+--------+----------------+------------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view tree

{
    "duration": 1715,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 412,
        "disconnect_time": 0,
        "mo_time": 1174,
        "total_time": 1586
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

True	412	-	connect apic11o.emea-sp.cisco.com:443
True	297	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	290	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis query query-target=children&rsp-subtree-include=health,fault-count
True	290	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	297	16	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisFmcastTree
```

[[Back]](./ProtocolIsis.md)