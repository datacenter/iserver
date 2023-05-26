# Node Protocol - LLDP

## Show instance summary for all leaf nodes

```
# iserver get aci proto lldp --apic apic11 --role leaf

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-------------+-----------+-----------------+------------------------+-----------+
| Node                | Admin State | Hold Time | Init Delay Time | Transmission Frequency | Neighbors |
+---------------------+-------------+-----------+-----------------+------------------------+-----------+
| pod-1/bl205-eu-spdc | enabled     | 120       | 2               | 30                     | 13        | 
| pod-1/bl206-eu-spdc | enabled     | 120       | 2               | 30                     | 10        | 
| pod-1/cl201-eu-spdc | enabled     | 120       | 2               | 30                     | 43        | 
| pod-1/cl202-eu-spdc | enabled     | 120       | 2               | 30                     | 43        | 
| pod-1/rl301-eu-spdc | enabled     | 120       | 2               | 30                     | 21        | 
| pod-1/rl302-eu-spdc | enabled     | 120       | 2               | 30                     | 21        | 
+---------------------+-------------+-----------+-----------------+------------------------+-----------+
```

[[Back]](./ProtocolLldp.md)