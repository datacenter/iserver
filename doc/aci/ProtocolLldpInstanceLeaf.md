# Node Protocol - LLDP

## Show instance summary for all leaf nodes

```
# iserver get aci proto lldp --apic apic11 --role leaf --view summary

Apic: apic11 (mode:online, cache:on)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-------------+-----------+-----------------+------------------------+-----------+--------+
| Node                | Admin State | Hold Time | Init Delay Time | Transmission Frequency | Neighbors | Errors |
+---------------------+-------------+-----------+-----------------+------------------------+-----------+--------+
| pod-1/bl205-eu-spdc | enabled     | 120       | 2               | 30                     | 13        | X      | 
| pod-1/bl206-eu-spdc | enabled     | 120       | 2               | 30                     | 10        | X      | 
| pod-1/cl201-eu-spdc | enabled     | 120       | 2               | 30                     | 43        | V      | 
| pod-1/cl202-eu-spdc | enabled     | 120       | 2               | 30                     | 43        | X      | 
| pod-1/cl209-eu-spdc | enabled     | 120       | 2               | 30                     | 1         | X      | 
| pod-1/cl210-eu-spdc | enabled     | 120       | 2               | 30                     | 1         | X      | 
| pod-1/rl301-eu-spdc | enabled     | 120       | 2               | 30                     | 21        | V      | 
| pod-1/rl302-eu-spdc | enabled     | 120       | 2               | 30                     | 21        | V      | 
+---------------------+-------------+-----------+-----------------+------------------------+-----------+--------+
Interface context: lldp
```

Developer

```
# iserver get aci proto lldp --apic apic11 --role leaf --view summary

{
    "duration": 394,
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
    "cache_hits": 26
}
```

[[Back]](./ProtocolLldp.md)