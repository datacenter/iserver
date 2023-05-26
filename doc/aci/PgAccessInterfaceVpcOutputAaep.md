# Policy Group - Access Interface VPC

## AAEP specific output

```
# iserver get aci pg access intf vpc --apic apic11 --name HX* -o aaep

Apic: apic11

+-----------------+-------------------------+-------------+-------------+
| Name            | Attached Entity Profile | Domain Type | Domain Name |
+-----------------+-------------------------+-------------+-------------+
| HX1-FI-A_PolGrp | HX1_AAEP                | Physical    | HX1_PhysDom | 
+-----------------+-------------------------+-------------+-------------+
| HX1-FI-B_PolGrp | HX1_AAEP                | Physical    | HX1_PhysDom | 
+-----------------+-------------------------+-------------+-------------+
```

[[Back]](./PgAccessInterfaceVpc.md)