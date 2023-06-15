# Node Protocol - ND

## Multiple node adjacencies

```
# iserver get aci proto nd --apic apic11 --node bl

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc

+---------------------+-------------+----------------+----------------+------------------------+
| Node                | Admin State | Aging Interval | Neighbor Count | Active Interface Count |
+---------------------+-------------+----------------+----------------+------------------------+
| pod-1/bl205-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/bl206-eu-spdc | enabled     | 1380           | 0              | 0                      | 
+---------------------+-------------+----------------+----------------+------------------------+
```

Developer

```
# iserver get aci proto nd --apic apic11 --node bl

{
    "duration": 3902,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 451,
        "disconnect_time": 0,
        "mo_time": 3093,
        "total_time": 3544
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

True	451	-	connect apic11o.emea-sp.cisco.com
True	341	13	apic11o.emea-sp.cisco.com class fabricNode
True	326	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/nd/inst
True	347	26	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ndDom
True	360	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	380	35	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
True	346	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/nd/inst
True	330	25	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ndDom
True	348	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	315	33	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolNd.md)