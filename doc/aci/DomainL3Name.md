# L3 Domain

## Filter by name

```
# iserver get aci domain l3 --apic apic11 --name UCSB*

Apic: apic11

+-------------+------------+----------------+-----------------------+-----------+
| Domain Name | AAEP       | VLAN Pool      | Encapsulation Block   | EPG Usage |
+-------------+------------+----------------+-----------------------+-----------+
| UCSB1_L3Dom | UCSB1_AAEP | UCSB1_VlanPool | [2-100] (static)      | 0/1999    | 
|             |            |                | [101-1000] (inherit)  |           | 
|             |            |                | [2001-2500] (inherit) |           | 
|             |            |                | [3001-3500] (inherit) |           | 
+-------------+------------+----------------+-----------------------+-----------+
```

[[Back]](./DomainL3.md)