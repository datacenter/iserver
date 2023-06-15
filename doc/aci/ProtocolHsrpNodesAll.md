# Node Protocol - HSRP

## Show HSRP state summary for all nodes

```
# iserver get aci proto hsrp --apic apic11 --node any

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
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+-------------+------------+
| Node                | Admin State | Oper State |
+---------------------+-------------+------------+
| pod-1/bl205-eu-spdc | enabled     | enabled    | 
| pod-1/bl206-eu-spdc | enabled     | enabled    | 
| pod-1/cl201-eu-spdc | enabled     | enabled    | 
| pod-1/cl202-eu-spdc | enabled     | enabled    | 
| pod-1/rl301-eu-spdc | enabled     | enabled    | 
| pod-1/rl302-eu-spdc | enabled     | enabled    | 
+---------------------+-------------+------------+
```

Developer

```
# iserver get aci proto hsrp --apic apic11 --node any

{
    "duration": 9017,
    "apic": {
        "read": true,
        "success": 24,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 23,
        "connect_time": 487,
        "disconnect_time": 0,
        "mo_time": 7888,
        "total_time": 8375
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

True	487	-	connect apic11o.emea-sp.cisco.com
True	356	13	apic11o.emea-sp.cisco.com class fabricNode
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205 query query-target=subtree&target-subtree-class=hsrpEntity
True	336	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/hsrpDom
True	344	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206 query query-target=subtree&target-subtree-class=hsrpEntity
True	353	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/hsrpDom
True	310	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	362	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201 query query-target=subtree&target-subtree-class=hsrpEntity
True	316	10	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/hsrpDom
True	353	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	324	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202 query query-target=subtree&target-subtree-class=hsrpEntity
True	315	10	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/hsrpDom
True	312	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	357	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209 query query-target=subtree&target-subtree-class=hsrpEntity
True	354	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210 query query-target=subtree&target-subtree-class=hsrpEntity
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301 query query-target=subtree&target-subtree-class=hsrpEntity
True	336	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/hsrpDom
True	359	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	329	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302 query query-target=subtree&target-subtree-class=hsrpEntity
True	330	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/hsrpDom
True	339	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	398	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101 query query-target=subtree&target-subtree-class=hsrpEntity
True	382	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102 query query-target=subtree&target-subtree-class=hsrpEntity
```

[[Back]](./ProtocolHsrp.md)