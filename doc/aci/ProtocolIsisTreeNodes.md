# Node Protocol - IS-IS

## Show multicast tree for selected nodes

```
# iserver get aci proto isis --apic apic11 --node rl --view tree

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+---------+----+--------------+-------------+----------+--------+----------------+------------+
| Node                | Domain  | Id | Root Address | Root Port   | Diameter | Origin | Diameter Alert | Oper State |
+---------------------+---------+----+--------------+-------------+----------+--------+----------------+------------+
| pod-1/rl301-eu-spdc | overlay | 0  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 1  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 2  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 3  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 4  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 5  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 6  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 7  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 8  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 9  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 10 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 11 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 12 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 13 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 14 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl301-eu-spdc | overlay | 15 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 0  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 1  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 2  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 3  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 4  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 5  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 6  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 7  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 8  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 9  | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 10 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 11 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 12 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 13 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 14 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
| pod-1/rl302-eu-spdc | overlay | 15 | 0.0.0.0      | unspecified | 0        | static | inactive       | active     | 
+---------------------+---------+----+--------------+-------------+----------+--------+----------------+------------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node rl --view tree

{
    "duration": 3124,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 425,
        "disconnect_time": 0,
        "mo_time": 2396,
        "total_time": 2821
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

True	425	-	connect apic11o.emea-sp.cisco.com
True	336	13	apic11o.emea-sp.cisco.com class fabricNode
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	318	16	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisFmcastTree
True	354	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis
True	390	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	331	16	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisFmcastTree
```

[[Back]](./ProtocolIsis.md)