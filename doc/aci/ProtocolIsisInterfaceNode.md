# Node Protocol - IS-IS

## Show interface details for selected node

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view intf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+---------+--------------+-------------+--------------+--------------------+----------------+
| Node                | Domain  | Id           | Admin State | Circuit Type | Control            | Protocol State |
+---------------------+---------+--------------+-------------+--------------+--------------------+----------------+
| pod-1/cl201-eu-spdc | overlay | eth1/107.7   | enabled     | l1           |                    | Ready          | 
| pod-1/cl201-eu-spdc | overlay | eth1/108.504 | enabled     | l1           |                    | Ready          | 
| pod-1/cl201-eu-spdc | overlay | lo0          | enabled     | l1           | advert-tep,passive | Ready          | 
| pod-1/cl201-eu-spdc | overlay | lo1          | enabled     | l1           | advert-tep,passive | Ready          | 
| pod-1/cl201-eu-spdc | overlay | lo2          | enabled     | l1           | passive            | Ready          | 
+---------------------+---------+--------------+-------------+--------------+--------------------+----------------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view intf

{
    "duration": 1980,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 404,
        "disconnect_time": 0,
        "mo_time": 1396,
        "total_time": 1800
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

True	404	-	connect apic11o.emea-sp.cisco.com
True	319	11	apic11o.emea-sp.cisco.com class fabricNode
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis
True	324	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	413	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisIf
```

[[Back]](./ProtocolIsis.md)