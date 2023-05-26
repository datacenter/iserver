# VMM Domain

## Filter by name

```
# iserver get aci domain vmm --apic apic11 --name *r3dc*

Apic: apic11

+--------------+-----------------+-------------------+-----------------------+-----------+---------+
| Domain Name  | AAEP            | VLAN Pool         | Encapsulation Block   | EPG Usage | Uplinks |
+--------------+-----------------+-------------------+-----------------------+-----------+---------+
| EU-SPDC-R3DC | UCSB1-R3DC_AAEP | ESX-R3DC_VlanPool | [2300-2309] (static)  | 5/410     | 2       | 
|              | ESX-R3DC_AAEP   |                   | [2310-2310] (static)  |           |         | 
|              |                 |                   | [3001-3399] (inherit) |           |         | 
+--------------+-----------------+-------------------+-----------------------+-----------+---------+
```

[[Back]](./DomainVmm.md)