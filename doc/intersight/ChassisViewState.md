# Intersight Chassis

## state view

```
# iserver get chassis

iaccount demo (cache: any)
Select chassis...
Selected chassis: 4
Collect chassis api objects...

Chassis State Summary [#4]
--------------------------

+------------+---------------+-------+-----------------+--------+----------+------------+------+-----+----------+-----------+-----+
| Chassis    | Health        | State | Model           | Serial | ConnPath | ConnStatus | Node | I/O | Expander | FanModule | PSU |
+------------+---------------+-------+-----------------+--------+----------+------------+------+-----+----------+-----------+-----+
| Chassis754 | Healthy       | --    | UCSS-S3260-BASE | SN-84  |          |            | 1    | 0   | 0        | 4         | 4   |
| Chassis643 | Healthy       | V     | UCSX-9508       | SN-20  | A,B      | A,B        | 3    | 2   | 2        | 4         | 6   |
| Chassis871 | Critical (12) | X     | UCSB-5108-AC2   | SN-53  | A,B      |            | 4    | 2   | 0        | 8         | 4   |
| Chassis364 | Healthy       | V     | UCSB-5108-AC2   | SN-35  | A,B      | A,B        | 4    | 2   | 0        | 8         | 4   |
+------------+---------------+-------+-----------------+--------+----------+------------+------+-----+----------+-----------+-----+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ChassisInventory.md)