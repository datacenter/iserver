# Node Protocol - LLDP

## Show instance summary for selected node

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc --view summary

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-------------+-----------+-----------------+------------------------+-----------+--------+
| Node                | Admin State | Hold Time | Init Delay Time | Transmission Frequency | Neighbors | Errors |
+---------------------+-------------+-----------+-----------------+------------------------+-----------+--------+
| pod-1/bl205-eu-spdc | enabled     | 120       | 2               | 30                     | 13        | X      | 
+---------------------+-------------+-----------+-----------------+------------------------+-----------+--------+
Interface context: lldp
```

Developer

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc --view summary

{
    "duration": 4374,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 741,
        "disconnect_time": 0,
        "mo_time": 3525,
        "total_time": 4266
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

True	741	-	connect apic11o.emea-sp.cisco.com:443
True	2461	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	284	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst
True	282	1	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/lldpInstStats
True	498	13	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
```

[[Back]](./ProtocolLldp.md)