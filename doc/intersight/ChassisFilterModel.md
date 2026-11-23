# Intersight Chassis

## Filter by model

```
# iserver get chassis --model 5108

iaccount demo (cache: any)
Select chassis...
Selected chassis: 2
Collect chassis api objects...

Chassis State Summary [#2]
--------------------------

+------------+---------------+-------+---------------+--------+----------+------------+------+-----+----------+-----------+-----+
| Chassis    | Health        | State | Model         | Serial | ConnPath | ConnStatus | Node | I/O | Expander | FanModule | PSU |
+------------+---------------+-------+---------------+--------+----------+------------+------+-----+----------+-----------+-----+
| Chassis261 | Critical (12) | X     | UCSB-5108-AC2 | SN-98  | A,B      |            | 4    | 2   | 0        | 8         | 4   |
| Chassis979 | Healthy       | V     | UCSB-5108-AC2 | SN-63  | A,B      | A,B        | 4    | 2   | 0        | 8         | 4   |
+------------+---------------+-------+---------------+--------+----------+------------+------+-----+----------+-----------+-----+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ServerInventory.md)