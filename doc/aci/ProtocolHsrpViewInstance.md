# Node Protocol - HSRP

## Inst view

```
# iserver get aci proto hsrp --apic apic11 --node cl201-eu-spdc --view inst

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol HSRP - Instance [#1]
-----------------------------

+---------------------+-------------+--------+---------+
| Node                | Admin State | Health | Faults  |
+---------------------+-------------+--------+---------+
| pod-1/cl201-eu-spdc | enabled     | 100    | 0 0 0 0 | 
+---------------------+-------------+--------+---------+
```

Developer

```
# iserver get aci proto hsrp --apic apic11 --node cl201-eu-spdc --view inst

{
    "duration": 1692,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 387,
        "disconnect_time": 0,
        "mo_time": 1140,
        "total_time": 1527
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

True	387	-	connect apic11o.emea-sp.cisco.com:443
True	282	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	277	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/hsrp query query-target=children&rsp-subtree-include=health,fault-count
True	285	10	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-201/hsrpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	296	0	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-201/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolHsrp.md)