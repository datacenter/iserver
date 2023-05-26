# Node Protocol - HSRP

## Show HSRP VRF domains for selected node

```
# iserver get aci proto hsrp --apic apic11 --node cl201-eu-spdc

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+-------------+------------+
| Node                | Admin State | Oper State |
+---------------------+-------------+------------+
| pod-1/cl201-eu-spdc | enabled     | enabled    | 
+---------------------+-------------+------------+
```

[[Back]](./ProtocolHsrp.md)