# Intersight Fabric Interconnect - Power supply view

[[Back]](./FiInventory.md)

```
# iserver get fi --name fi1* -v psu

+----+---------------------+--------+----------+---------+-------------+-------------+-------------+---------------------+
| ID | Fabric Interconnect | PSU    | Presence | Voltage | Model       | Pid         | Serial      | Vendor              |
+----+---------------------+--------+----------+---------+-------------+-------------+-------------+---------------------+
| 1  | fi1 FI-A [ID:A]     | PSU #1 | equipped | ---     | UCS-PSU-XYZ | UCS-PSU-XYZ | PSU123      | Cisco Systems, Inc. |
| 2  | fi1 FI-A [ID:A]     | PSU #2 | equipped | ---     | UCS-PSU-XYZ | UCS-PSU-XYZ | PSU456      | Cisco Systems, Inc. |
+----+---------------------+--------+----------+---------+-------------+-------------+-------------+---------------------+

Filter: name, serial, model
View:   state (def), eth, pc, fc, fpc, fanm, fan, psu, storage, inv, all
```

[[Back]](./FiInventory.md)