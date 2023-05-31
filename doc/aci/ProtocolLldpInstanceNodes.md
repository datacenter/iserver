# Node Protocol - LLDP

## Show instance summary for selected nodes

```
# iserver get aci proto lldp --apic apic11 --node bl

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc

+---------------------+-------------+-----------+-----------------+------------------------+-----------+
| Node                | Admin State | Hold Time | Init Delay Time | Transmission Frequency | Neighbors |
+---------------------+-------------+-----------+-----------------+------------------------+-----------+
| pod-1/bl205-eu-spdc | enabled     | 120       | 2               | 30                     | 13        | 
| pod-1/bl206-eu-spdc | enabled     | 120       | 2               | 30                     | 10        | 
+---------------------+-------------+-----------+-----------------+------------------------+-----------+
```

Developer

```
# iserver get aci proto lldp --apic apic11 --node bl

{
    "duration": 3902,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 414,
        "disconnect_time": 0,
        "mo_time": 3279,
        "total_time": 3693
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

True	414	-	connect apic11o.emea-sp.cisco.com
True	1362	11	apic11o.emea-sp.cisco.com class fabricNode
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lldp/inst
True	316	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lldpInstStats
True	340	13	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lldp/inst
True	321	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/lldpInstStats
True	301	10	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
```

[[Back]](./ProtocolLldp.md)