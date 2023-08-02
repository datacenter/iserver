# Node Protocol - IS-IS

## Intf view

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view intf

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol ISIS - Interface [#5]
------------------------------

+---------------------+---------+------------+-------------+--------------+--------------------+----------------+
| Node                | Domain  | Id         | Admin State | Circuit Type | Control            | Protocol State |
+---------------------+---------+------------+-------------+--------------+--------------------+----------------+
| pod-1/cl201-eu-spdc | overlay | eth1/107.7 | enabled     | l1           |                    | Ready          | 
| pod-1/cl201-eu-spdc | overlay | eth1/108.8 | enabled     | l1           |                    | Ready          | 
| pod-1/cl201-eu-spdc | overlay | lo0        | enabled     | l1           | advert-tep,passive | Ready          | 
| pod-1/cl201-eu-spdc | overlay | lo1        | enabled     | l1           | passive            | Ready          | 
| pod-1/cl201-eu-spdc | overlay | lo2        | enabled     | l1           | advert-tep,passive | Ready          | 
+---------------------+---------+------------+-------------+--------------+--------------------+----------------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view intf

{
    "duration": 1699,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 402,
        "disconnect_time": 0,
        "mo_time": 1148,
        "total_time": 1550
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

True	402	-	connect apic11o.emea-sp.cisco.com:443
True	303	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	288	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis query query-target=children&rsp-subtree-include=health,fault-count
True	278	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	279	5	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisIf
```

[[Back]](./ProtocolIsis.md)