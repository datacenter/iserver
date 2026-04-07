# Intersight Fabric Interconnect - Ethernet port channel view

[[Back]](./FiInventory.md)

```
# iserver get fi -v pc

+----+-----------------+-------+---------------+------------+---------+--------+---------+---------+
| ID | FI              | PC ID | Name          | Role       | Admin   | State  | Speed   | Members |
+----+-----------------+-------+---------------+------------+---------+--------+---------+---------+
| 1  | fi1 FI-A [ID:A] | 15    | UCSB1-ACI-1   | FcoeUplink | enabled | up     | 40gbps  | 2/2     |
| 2  | fi1 FI-A [ID:A] | 17    | UCSB1-ACI-2   | FcoeUplink | enabled | failed | 10gbps  | 2/2     |
| 3  | fi1 FI-A [ID:A] | 25    | UCSB1-IPN-1   | FcoeUplink | enabled | up     | 100gbps | 2/2     | 
| 4  | fi1 FI-A [ID:A] | 27    | UCSB1-IPN-2   | FcoeUplink | enabled | up     | 10gbps  | 2/2     |
...

Filter: name, serial, model
View:   state (def), eth, pc, fc, fpc, fanm, fan, psu, storage, inv, all
```

[[Back]](./FiInventory.md)