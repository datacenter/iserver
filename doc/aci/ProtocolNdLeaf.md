# Node Protocol - ND

## Leaf nodes adjacencies

```
# iserver get aci proto nd --apic apic11 --role leaf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-------------+----------------+----------------+------------------------+
| Node                | Admin State | Aging Interval | Neighbor Count | Active Interface Count |
+---------------------+-------------+----------------+----------------+------------------------+
| pod-1/bl205-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/bl206-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/cl201-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/cl202-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/rl301-eu-spdc | enabled     | 1380           | 0              | 0                      | 
| pod-1/rl302-eu-spdc | enabled     | 1380           | 0              | 0                      | 
+---------------------+-------------+----------------+----------------+------------------------+
```

Developer

```
# iserver get aci proto nd --apic apic11 --role leaf

{
    "duration": 8761,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 391,
        "disconnect_time": 0,
        "mo_time": 8134,
        "total_time": 8525
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

True	391	-	connect apic11o.emea-sp.cisco.com
True	299	11	apic11o.emea-sp.cisco.com class fabricNode
True	318	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/nd/inst
True	309	26	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ndDom
True	283	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	318	35	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
True	348	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/nd/inst
True	311	25	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ndDom
True	289	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	347	33	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
True	369	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/nd/inst
True	288	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ndDom
True	315	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	315	37	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
True	336	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/nd/inst
True	362	30	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ndDom
True	316	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	332	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/nd/inst
True	336	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ndDom
True	330	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	349	24	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
True	361	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/nd/inst
True	323	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ndDom
True	305	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	323	24	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolNd.md)