# Node Protocol - LACP

## Inst view

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc --view inst

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol LACP - Instance [#1]
-----------------------------

+---------------------+---------+-------------------+------------+-----------+---------+-----------+------------+
| Node                | Admin   | System MAC        | Admin Prio | Oper Prio | Intf Up | Intf Down | Intf Count |
+---------------------+---------+-------------------+------------+-----------+---------+-----------+------------+
| pod-1/bl205-eu-spdc | enabled | 4C:71:0D:7E:84:C0 | 32768      | 32768     | 5       | 0         | 5          | 
+---------------------+---------+-------------------+------------+-----------+---------+-----------+------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc --view inst

{
    "duration": 2167,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 394,
        "disconnect_time": 0,
        "mo_time": 1551,
        "total_time": 1945
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

True	394	-	connect apic11o.emea-sp.cisco.com:443
True	293	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	277	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lacp/inst
True	425	5	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	277	5	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	279	5	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp&rsp-subtree-include=fault-count
```

[[Back]](./ProtocolLacp.md)