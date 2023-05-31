# Node Protocol - HSRP

## Show HSRP state summary for selected nodes

```
# iserver get aci proto hsrp --apic apic11 --node rl

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-------------+------------+
| Node                | Admin State | Oper State |
+---------------------+-------------+------------+
| pod-1/rl301-eu-spdc | enabled     | enabled    | 
| pod-1/rl302-eu-spdc | enabled     | enabled    | 
+---------------------+-------------+------------+
```

Developer

```
# iserver get aci proto hsrp --apic apic11 --node rl

{
    "duration": 2818,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 488,
        "disconnect_time": 0,
        "mo_time": 2204,
        "total_time": 2692
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

True	488	-	connect apic11o.emea-sp.cisco.com
True	314	11	apic11o.emea-sp.cisco.com class fabricNode
True	302	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301 query query-target=subtree&target-subtree-class=hsrpEntity
True	290	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/hsrpDom
True	287	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302 query query-target=subtree&target-subtree-class=hsrpEntity
True	358	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/hsrpDom
True	320	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolHsrp.md)