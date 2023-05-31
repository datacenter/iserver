# Node Protocol - LACP

## Show instance summary for selected nodes

```
# iserver get aci proto lacp --apic apic11 --node rl

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
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
    "duration": 4347,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 501,
        "disconnect_time": 0,
        "mo_time": 3385,
        "total_time": 3886
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

True	501	-	connect apic11o.emea-sp.cisco.com
True	340	11	apic11o.emea-sp.cisco.com class fabricNode
True	288	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst
True	300	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	288	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	292	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst/if-[eth1/4] query query-target=children&target-subtree-class=lacpAdjEp
True	278	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst/if-[eth1/3] query query-target=children&target-subtree-class=lacpAdjEp
True	303	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst
True	287	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	431	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst/if-[eth1/4] query query-target=children&target-subtree-class=lacpAdjEp
True	284	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst/if-[eth1/3] query query-target=children&target-subtree-class=lacpAdjEp
```

[[Back]](./ProtocolLacp.md)