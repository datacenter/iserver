# Policy Group - Access Interface VPC

## Port specific output

```
# iserver get aci pg access intf vpc --apic apic11 --name HX* -o port

Apic: apic11

+-----------------+-------------------------+--------------------+---------------+
| Name            | Attached Entity Profile | Deployed Node Name | Deployed Port |
+-----------------+-------------------------+--------------------+---------------+
| HX1-FI-A_PolGrp | HX1_AAEP                | bl206-eu-spdc      | eth1/11       | 
|                 |                         | bl205-eu-spdc      | eth1/11       | 
+-----------------+-------------------------+--------------------+---------------+
| HX1-FI-B_PolGrp | HX1_AAEP                | bl205-eu-spdc      | eth1/12       | 
|                 |                         | bl206-eu-spdc      | eth1/12       | 
+-----------------+-------------------------+--------------------+---------------+
```

[[Back]](./PgAccessInterfaceVpc.md)