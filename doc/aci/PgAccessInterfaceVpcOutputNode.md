# Policy Group - Access Interface VPC

## Node specific output

```
# iserver get aci pg access intf vpc --apic apic11 --name HX* -o node

Apic: apic11

+-----------------+-------------------------+--------------------+
| Name            | Attached Entity Profile | Deployed Node Name |
+-----------------+-------------------------+--------------------+
| HX1-FI-A_PolGrp | HX1_AAEP                | bl206-eu-spdc      | 
|                 |                         | bl205-eu-spdc      | 
+-----------------+-------------------------+--------------------+
| HX1-FI-B_PolGrp | HX1_AAEP                | bl205-eu-spdc      | 
|                 |                         | bl206-eu-spdc      | 
+-----------------+-------------------------+--------------------+
```

[[Back]](./PgAccessInterfaceVpc.md)