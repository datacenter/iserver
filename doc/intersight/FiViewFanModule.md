# Intersight Fabric Interconnect - Fan module view

[[Back]](./FiInventory.md)

```
# iserver get fi --name fi1* -v fanm

+----+---------------------+------------+--------+----------+-----------+-----------+-----------+---------------------+
| ID | Fabric Interconnect | Fan Module | # Fans | Presence | OperState | Model     | PN        | Vendor              |
+----+---------------------+------------+--------+----------+-----------+-----------+-----------+---------------------+
| 1  | fi1 FI-A [ID:A]     | 1          | 2      | equipped | operable  | FAN-ABC-F | FAN-ABC-F | Cisco Systems, Inc. |
| 2  | fi1 FI-A [ID:A]     | 2          | 2      | equipped | operable  | FAN-ABC-F | FAN-ABC-F | Cisco Systems, Inc. |
| 3  | fi1 FI-A [ID:A]     | 3          | 2      | equipped | operable  | FAN-ABC-F | FAN-ABC-F | Cisco Systems, Inc. |
| 4  | fi1 FI-A [ID:A]     | 4          | 2      | equipped | operable  | FAN-ABC-F | FAN-ABC-F | Cisco Systems, Inc. | 
+----+---------------------+------------+--------+----------+-----------+-----------+-----------+---------------------+

Filter: name, serial, model
View:   state (def), eth, pc, fc, fpc, fanm, fan, psu, storage, inv, all
```

[[Back]](./FiInventory.md)