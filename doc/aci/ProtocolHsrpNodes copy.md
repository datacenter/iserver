# Node Protocol - HSRP

## Show HSRP state summary for selected nodes

```
# iserver get aci proto hsrp --apic apic11 --node rl

Apic: apic11
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-------------+------------+
| Node                | Admin State | Oper State |
+---------------------+-------------+------------+
| pod-1/rl301-eu-spdc | enabled     | enabled    | 
| pod-1/rl302-eu-spdc | enabled     | enabled    | 
+---------------------+-------------+------------+
```

[[Back]](./ProtocolHsrp.md)