# Node Protocol - IS-IS

## Show neighbor details for selected node

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view neighbor

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+---------+------------+-------------------+-------+--------------+-------------+-------+
| Node                | Domain  | Interface  | System Id         | Level | Circuit Type | Peer IP     | State |
+---------------------+---------+------------+-------------------+-------+--------------+-------------+-------+
| pod-1/cl201-eu-spdc | overlay | eth1/108.8 | 41:20:03:0A:00:00 | l1    | bcast        | 10.3.32.65  | up    | 
| pod-1/cl201-eu-spdc | overlay | eth1/107.7 | 41:C0:03:0A:00:00 | l1    | bcast        | 10.3.192.65 | up    | 
+---------------------+---------+------------+-------------------+-------+--------------+-------------+-------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view neighbor

{
    "duration": 1931,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 424,
        "disconnect_time": 0,
        "mo_time": 1307,
        "total_time": 1731
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

True	424	-	connect apic11o.emea-sp.cisco.com
True	318	13	apic11o.emea-sp.cisco.com class fabricNode
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	317	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisAdjEp&rsp-subtree=children&rsp-subtree-class=isisPeerIpAddr
```

[[Back]](./ProtocolIsis.md)