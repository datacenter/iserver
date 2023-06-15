# Node Protocol - ND

## Leaf nodes adjacencies

```
# iserver get aci proto nd --apic apic11 --role leaf

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

+---------------------+-------------+----------------+----------------+------------------------+
| Node                | Admin State | Aging Interval | Neighbor Count | Active Interface Count |
+---------------------+-------------+----------------+----------------+------------------------+
| pod-1/bl205-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/bl206-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/cl201-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/cl202-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/cl209-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/cl210-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/rl301-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/rl302-eu-spdc | enabled     | 1380           | 0              | 0                      | 
+---------------------+-------------+----------------+----------------+------------------------+
```

Developer

```
# iserver get aci proto nd --apic apic11 --role leaf

{
    "duration": 12242,
    "apic": {
        "read": true,
        "success": 34,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 33,
        "connect_time": 446,
        "disconnect_time": 0,
        "mo_time": 10962,
        "total_time": 11408
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

True	446	-	connect apic11o.emea-sp.cisco.com
True	358	13	apic11o.emea-sp.cisco.com class fabricNode
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/nd/inst
True	342	26	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ndDom
True	323	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	311	35	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/nd/inst
True	323	25	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ndDom
True	326	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	322	33	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
True	324	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/nd/inst
True	333	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ndDom
True	304	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	349	37	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/nd/inst
True	317	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ndDom
True	342	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	341	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/nd/inst
True	328	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ndDom
True	329	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	339	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
True	311	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/nd/inst
True	294	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ndDom
True	331	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	333	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
True	370	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/nd/inst
True	350	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ndDom
True	333	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	354	24	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/nd/inst
True	358	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ndDom
True	351	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	366	24	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolNd.md)