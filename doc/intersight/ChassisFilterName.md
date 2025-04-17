# Intersight Chassis

## Filter by name

```
# iserver get chassis --name ucsx

iaccount demo (cache: any)
Select chassis...
Selected chassis: 1
Collect chassis api objects...

Chassis State Summary [#1]
--------------------------

+------------+---------+-------+-----------+--------+----------+------------+------+-----+----------+-----------+-----+
| Chassis    | Health  | State | Model     | Serial | ConnPath | ConnStatus | Node | I/O | Expander | FanModule | PSU |
+------------+---------+-------+-----------+--------+----------+------------+------+-----+----------+-----------+-----+
| Chassis967 | Healthy | V     | UCSX-9508 | SN-11  | A,B      | A,B        | 3    | 2   | 2        | 4         | 6   |
+------------+---------+-------+-----------+--------+----------+------------+------+-----+----------+-----------+-----+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ServerInventory.md)