# Intersight Fabric Interconnect - Local storage view

[[Back]](./FiInventory.md)

```
# iserver get fi --name fi1* -v storage

+----+---------------------+-------------------+------------+------+
| ID | Fabric Interconnect | Storage Partition | Size [MiB] | Used |
+----+---------------------+-------------------+------------+------+
| 1  | fi1 FI-A [ID:A]     | bootflash         | 84926      | 39%  |
| 2  | fi1 FI-A [ID:A]     | opt               | 9928       | 3%   |
| 3  | fi1 FI-A [ID:A]     | spare             | 7918       | 1%   |
| 4  | fi1 FI-A [ID:A]     | usbdrive          | ---        | ---  |
| 5  | fi1 FI-A [ID:A]     | var_sysmgr        | 9648       | 6%   |
| 6  | fi1 FI-A [ID:A]     | var_tmp           | 600        | 4%   |
| 7  | fi1 FI-A [ID:A]     | volatile          | 2048       | 1%   |
| 8  | fi1 FI-A [ID:A]     | workspace         | 7917       | 9%   |
+----+---------------------+-------------------+------------+------+

Filter: name, serial, model
View:   state (def), eth, pc, fc, fpc, fanm, fan, psu, storage, inv, all
```

[[Back]](./FiInventory.md)