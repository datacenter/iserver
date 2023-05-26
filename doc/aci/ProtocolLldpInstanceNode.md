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

[[Back]](./ProtocolLldp.md)