# Node Protocol - LACP

## Show instance summary for selected nodes

```
# iserver get aci proto lacp --apic apic11 --node rl

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
| Node                | Admin State | System MAC        | Admin Priority | Oper Priority | Port Channel Interfaces |
+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
| pod-1/rl301-eu-spdc | enabled     | A0:B4:39:4A:2B:DF | 32768          | 32768         | 2/0/2                   | 
| pod-1/rl302-eu-spdc | enabled     | A0:B4:39:4A:2D:B3 | 32768          | 32768         | 2/0/2                   | 
+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --node rl

{
    "duration": 3451,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 419,
        "disconnect_time": 0,
        "mo_time": 2752,
        "total_time": 3171
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

True	419	-	connect apic11o.emea-sp.cisco.com
True	307	13	apic11o.emea-sp.cisco.com class fabricNode
True	295	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst
True	287	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	304	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	309	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
True	315	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst
True	321	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	327	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	287	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
```

[[Back]](./ProtocolLacp.md)