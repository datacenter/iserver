# Node Protocol - IS-IS

## Show multicast tree for selected node

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view tree

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

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
    "duration": 2144,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 438,
        "disconnect_time": 0,
        "mo_time": 1386,
        "total_time": 1824
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

True	438	-	connect apic11o.emea-sp.cisco.com
True	370	13	apic11o.emea-sp.cisco.com class fabricNode
True	327	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis
True	335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	354	16	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisFmcastTree
```

[[Back]](./ProtocolIsis.md)