# Node Protocol - HSRP

## Show HSRP state summary for all nodes

```
# iserver get aci proto hsrp --apic apic11 --node any

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+-------------+------------+
| Node                | Admin State | Oper State |
+---------------------+-------------+------------+
| pod-1/bl205-eu-spdc | enabled     | enabled    | 
| pod-1/bl206-eu-spdc | enabled     | enabled    | 
| pod-1/cl201-eu-spdc | enabled     | enabled    | 
| pod-1/cl202-eu-spdc | enabled     | enabled    | 
| pod-1/rl301-eu-spdc | enabled     | enabled    | 
| pod-1/rl302-eu-spdc | enabled     | enabled    | 
|                     |             |            | 
|                     |             |            | 
+---------------------+-------------+------------+
```

[[Back]](./ProtocolHsrp.md)