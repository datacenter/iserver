# Policy Group - Access Interface VPC

## Filter by aaep

```
# iserver get aci pg access intf vpc --apic apic11 --aaep Infra_AAEP -o aaep

Apic: apic11

+--------------------+-------------------------+-------------+----------------+
| Name               | Attached Entity Profile | Domain Type | Domain Name    |
+--------------------+-------------------------+-------------+----------------+
| Infra_PolGrp       | Infra_AAEP              | L3          | Infra_L3Dom    | 
|                    |                         | Physical    | Infra_PhysDom  | 
|                    |                         | L2          | VNF-mgmt_L2Dom | 
+--------------------+-------------------------+-------------+----------------+
| NXOS_FABRIC_PolGrp | Infra_AAEP              | L3          | Infra_L3Dom    | 
|                    |                         | Physical    | Infra_PhysDom  | 
|                    |                         | L2          | VNF-mgmt_L2Dom | 
+--------------------+-------------------------+-------------+----------------+
```

[[Back]](./PgAccessInterfaceVpc.md)