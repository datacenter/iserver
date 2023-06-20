# Node Protocol - LLDP

## Show instance summary for selected nodes

```
# iserver get aci proto lldp --apic apic11 --node bl --view summary

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc

+---------------------+-------------+-----------+-----------------+------------------------+-----------+--------+
| Node                | Admin State | Hold Time | Init Delay Time | Transmission Frequency | Neighbors | Errors |
+---------------------+-------------+-----------+-----------------+------------------------+-----------+--------+
| pod-1/bl205-eu-spdc | enabled     | 120       | 2               | 30                     | 13        | X      | 
| pod-1/bl206-eu-spdc | enabled     | 120       | 2               | 30                     | 10        | X      | 
+---------------------+-------------+-----------+-----------------+------------------------+-----------+--------+
Interface context: lldp
```

Developer

```
# iserver get aci proto lldp --apic apic11 --node bl --view summary

{
    "duration": 2982,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 2445,
        "total_time": 2840
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

True	395	-	connect apic11o.emea-sp.cisco.com:443
True	442	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	291	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst
True	277	1	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/lldpInstStats
True	284	13	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	272	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/lldp/inst
True	277	1	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-206/lldpInstStats
True	602	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
```

[[Back]](./ProtocolLldp.md)