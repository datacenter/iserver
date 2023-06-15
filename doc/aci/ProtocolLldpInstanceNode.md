# Node Protocol - LLDP

## Show instance summary for selected node

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc --view summary

Apic: apic11 (mode:online, cache:on)
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
    "duration": 128,
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
    "cache_hits": 5
}
```

[[Back]](./ProtocolLldp.md)