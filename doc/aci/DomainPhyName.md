# Phy Domain

## Filter by name

```
# iserver get aci domain phy --apic apic11 --name UCSB*

Apic: apic11

+--------------------+-----------------+---------------------+-----------------------+-----------+
| Domain Name        | AAEP            | VLAN Pool           | Encapsulation Block   | EPG Usage |
+--------------------+-----------------+---------------------+-----------------------+-----------+
| UCSB1-R3DC_PhysDom | UCSB1-R3DC_AAEP | UCSB1-R3DC_VlanPool | [2901-3000] (inherit) | 0/100     | 
+--------------------+-----------------+---------------------+-----------------------+-----------+
| UCSB1_PhysDom      | UCSB1_AAEP      | UCSB1_VlanPool      | [2-100] (static)      | 0/1999    | 
|                    |                 |                     | [101-1000] (inherit)  |           | 
|                    |                 |                     | [2001-2500] (inherit) |           | 
|                    |                 |                     | [3001-3500] (inherit) |           | 
+--------------------+-----------------+---------------------+-----------------------+-----------+
```

[[Back]](./DomainPhy.md)