# Node Protocol - HSRP

## Show HSRP state summary for selected node

```
# iserver get aci proto hsrp --apic apic11 --node cl201-eu-spdc

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+-------------+------------+
| Node                | Admin State | Oper State |
+---------------------+-------------+------------+
| pod-1/cl201-eu-spdc | enabled     | enabled    | 
+---------------------+-------------+------------+
```

Developer

```
# iserver get aci proto hsrp --apic apic11 --node cl201-eu-spdc

{
    "duration": 2056,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 463,
        "disconnect_time": 0,
        "mo_time": 1350,
        "total_time": 1813
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

True	463	-	connect apic11o.emea-sp.cisco.com
True	372	13	apic11o.emea-sp.cisco.com class fabricNode
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201 query query-target=subtree&target-subtree-class=hsrpEntity
True	337	10	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/hsrpDom
True	341	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolHsrp.md)