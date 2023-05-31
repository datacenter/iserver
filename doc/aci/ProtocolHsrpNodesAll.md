# Node Protocol - HSRP

## Show HSRP state summary for all nodes

```
# iserver get aci proto hsrp --apic apic11 --node any

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
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
    "duration": 7591,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 404,
        "disconnect_time": 0,
        "mo_time": 6792,
        "total_time": 7196
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
True	307	11	apic11o.emea-sp.cisco.com class fabricNode
True	327	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205 query query-target=subtree&target-subtree-class=hsrpEntity
True	329	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/hsrpDom
True	323	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206 query query-target=subtree&target-subtree-class=hsrpEntity
True	300	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/hsrpDom
True	344	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	331	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201 query query-target=subtree&target-subtree-class=hsrpEntity
True	325	10	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/hsrpDom
True	341	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202 query query-target=subtree&target-subtree-class=hsrpEntity
True	303	10	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/hsrpDom
True	358	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	324	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301 query query-target=subtree&target-subtree-class=hsrpEntity
True	304	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/hsrpDom
True	282	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	296	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302 query query-target=subtree&target-subtree-class=hsrpEntity
True	328	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/hsrpDom
True	368	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	293	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101 query query-target=subtree&target-subtree-class=hsrpEntity
True	365	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102 query query-target=subtree&target-subtree-class=hsrpEntity
```

[[Back]](./ProtocolHsrp.md)