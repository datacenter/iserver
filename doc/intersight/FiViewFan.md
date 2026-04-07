# Intersight Fabric Interconnect - Fan view

[[Back]](./FiInventory.md)

```
# iserver get fi --name fi1* -v fan

+----+---------------------+------------+-----+----------+-----------+-----------+--------+-----+----+-----------+---------------------+
| ID | Fabric Interconnect | Fan Module | Fan | Presence | OperState | Model     | Serial | Sku | PN | Pid       | Vendor              |
+----+---------------------+------------+-----+----------+-----------+-----------+--------+-----+----+-----------+---------------------+
| 1  | fi1 FI-A [ID:A]     | 1          | 1   | equipped | operable  | FAN-ABC-F | N/A    |     |    | FAN-ABC-F | Cisco Systems, Inc. |
| 2  | fi1 FI-A [ID:A]     | 1          | 2   | equipped | operable  | FAN-ABC-F | N/A    |     |    | FAN-ABC-F | Cisco Systems, Inc. |
| 3  | fi1 FI-A [ID:A]     | 2          | 1   | equipped | operable  | FAN-ABC-F | N/A    |     |    | FAN-ABC-F | Cisco Systems, Inc. |
| 4  | fi1 FI-A [ID:A]     | 2          | 2   | equipped | operable  | FAN-ABC-F | N/A    |     |    | FAN-ABC-F | Cisco Systems, Inc. |
| 5  | fi1 FI-A [ID:A]     | 3          | 1   | equipped | operable  | FAN-ABC-F | N/A    |     |    | FAN-ABC-F | Cisco Systems, Inc. |
| 6  | fi1 FI-A [ID:A]     | 3          | 2   | equipped | operable  | FAN-ABC-F | N/A    |     |    | FAN-ABC-F | Cisco Systems, Inc. |
| 7  | fi1 FI-A [ID:A]     | 4          | 1   | equipped | operable  | FAN-ABC-F | N/A    |     |    | FAN-ABC-F | Cisco Systems, Inc. |
| 8  | fi1 FI-A [ID:A]     | 4          | 2   | equipped | operable  | FAN-ABC-F | N/A    |     |    | FAN-ABC-F | Cisco Systems, Inc. | 
+----+---------------------+------------+-----+----------+-----------+-----------+--------+-----+----+-----------+---------------------+

Filter: name, serial, model
View:   state (def), eth, pc, fc, fpc, fanm, fan, psu, storage, inv, all
```

[[Back]](./FiInventory.md)