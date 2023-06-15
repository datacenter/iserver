# Node Protocol - HSRP

## Show HSRP VRF domains for selected nodes

```
# iserver get aci proto hsrp --apic apic11 --node rl

Apic: apic11 (mode:online, cache:off)
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
    "duration": 3023,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 457,
        "disconnect_time": 0,
        "mo_time": 2324,
        "total_time": 2781
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

True	457	-	connect apic11o.emea-sp.cisco.com
True	360	13	apic11o.emea-sp.cisco.com class fabricNode
True	364	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301 query query-target=subtree&target-subtree-class=hsrpEntity
True	334	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/hsrpDom
True	307	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
True	315	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302 query query-target=subtree&target-subtree-class=hsrpEntity
True	332	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/hsrpDom
True	312	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/hsrpIf query rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolHsrp.md)