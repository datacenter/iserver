# Node Protocol - LLDP

## Show instance summary for selected node

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-------------+-----------+-----------------+------------------------+-----------+
| Node                | Admin State | Hold Time | Init Delay Time | Transmission Frequency | Neighbors |
+---------------------+-------------+-----------+-----------------+------------------------+-----------+
| pod-1/bl205-eu-spdc | enabled     | 120       | 2               | 30                     | 13        | 
+---------------------+-------------+-----------+-----------------+------------------------+-----------+
```

Developer

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc

{
    "duration": 1912,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 432,
        "disconnect_time": 0,
        "mo_time": 1361,
        "total_time": 1793
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

True	432	-	connect apic11o.emea-sp.cisco.com
True	325	11	apic11o.emea-sp.cisco.com class fabricNode
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lldp/inst
True	350	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lldpInstStats
True	337	13	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
```

[[Back]](./ProtocolLldp.md)