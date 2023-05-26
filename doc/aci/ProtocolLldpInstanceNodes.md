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

[[Back]](./ProtocolLldp.md)