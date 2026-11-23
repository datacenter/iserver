# Intersight Chassis

## exp view

```
# iserver get chassis -v exp

iaccount demo (cache: any)
Select chassis...
Selected chassis: 4
Collect chassis api objects...

Expander Module [#2]
--------------------

+------------+-------------+----------+-----------+----------------+--------+-------+-------------------+------+
| Chassis    | I/O Module  | Presence | OperState | Model          | Serial | P/N   | Vendor            | Fans |
+------------+-------------+----------+-----------+----------------+--------+-------+-------------------+------+
| Chassis599 | X-Fabric #1 | equipped | V         | UCSX-9508-RBLK | SN-34  | PN-38 | Cisco Systems Inc | 3    |
| Chassis599 | X-Fabric #2 | equipped | V         | UCSX-9508-RBLK | SN-75  | PN-54 | Cisco Systems Inc | 3    |
+------------+-------------+----------+-----------+----------------+--------+-------+-------------------+------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ChassisInventory.md)