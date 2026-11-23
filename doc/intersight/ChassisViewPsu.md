# Intersight Chassis

## psu view

```
# iserver get chassis --name ucsx -v psu

iaccount demo (cache: any)
Select chassis...
Selected chassis: 1
Collect chassis api objects...

PSU [#6]
--------

+------------+--------+-------+---------+-----------------+--------+
| Chassis    | PSU    | State | Voltage | Model           | Serial |
+------------+--------+-------+---------+-----------------+--------+
| Chassis745 | PSU #1 | X     | 0       | UCSX-PSU-2800AC | SN-31  |
+------------+--------+-------+---------+-----------------+--------+
| Chassis745 | PSU #2 | X     | 0       | UCSX-PSU-2800AC | SN-80  |
+------------+--------+-------+---------+-----------------+--------+
| Chassis745 | PSU #3 | X     | 0       | UCSX-PSU-2800AC | SN-82  |
+------------+--------+-------+---------+-----------------+--------+
| Chassis745 | PSU #4 | X     | 0       | UCSX-PSU-2800AC | SN-16  |
+------------+--------+-------+---------+-----------------+--------+
| Chassis745 | PSU #5 | X     | 0       | UCSX-PSU-2800AC | SN-15  |
+------------+--------+-------+---------+-----------------+--------+
| Chassis745 | PSU #6 | X     | 0       | UCSX-PSU-2800AC | SN-76  |
+------------+--------+-------+---------+-----------------+--------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ChassisInventory.md)