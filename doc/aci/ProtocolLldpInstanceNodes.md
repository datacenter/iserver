# Node Protocol - LLDP

## Show instance summary for selected nodes

```
# iserver get aci proto lldp --apic apic11 --node bl --view summary

Apic: apic11 (mode:online, cache:on)
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
    "duration": 202,
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
    "cache_hits": 8
}
```

[[Back]](./ProtocolLldp.md)