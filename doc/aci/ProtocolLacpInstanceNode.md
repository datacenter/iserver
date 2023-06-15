# Node Protocol - LACP

## Show instance summary for selected node

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc

Apic: apic11 (mode:online, cache:off)
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
    "duration": 2486,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 434,
        "disconnect_time": 0,
        "mo_time": 1705,
        "total_time": 2139
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

True	434	-	connect apic11o.emea-sp.cisco.com
True	306	13	apic11o.emea-sp.cisco.com class fabricNode
True	318	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst
True	367	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	345	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	369	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
```

[[Back]](./ProtocolLacp.md)