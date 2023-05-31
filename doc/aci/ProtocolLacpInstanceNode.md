# Node Protocol - LACP

## Show instance summary for selected node

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
| Node                | Admin State | System MAC        | Admin Priority | Oper Priority | Port Channel Interfaces |
+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
| pod-1/bl205-eu-spdc | enabled     | 4C:71:0D:7E:84:C0 | 32768          | 32768         | 5/0/5                   | 
+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc

{
    "duration": 4174,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 578,
        "disconnect_time": 0,
        "mo_time": 3056,
        "total_time": 3634
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

True	578	-	connect apic11o.emea-sp.cisco.com
True	356	11	apic11o.emea-sp.cisco.com class fabricNode
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst
True	387	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	308	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	320	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/2] query query-target=children&target-subtree-class=lacpAdjEp
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/27] query query-target=children&target-subtree-class=lacpAdjEp
True	369	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/12] query query-target=children&target-subtree-class=lacpAdjEp
True	363	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/11] query query-target=children&target-subtree-class=lacpAdjEp
True	311	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/1] query query-target=children&target-subtree-class=lacpAdjEp
```

[[Back]](./ProtocolLacp.md)