# Intersight Chassis

## Default output

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
| Chassis328 | Healthy       | --    | UCSS-S3260-BASE | SN-25  |          |            | 1    | 0   | 0        | 4         | 4   |
| Chassis324 | Healthy       | V     | UCSX-9508       | SN-78  | A,B      | A,B        | 3    | 2   | 2        | 4         | 6   |
| Chassis515 | Critical (12) | X     | UCSB-5108-AC2   | SN-36  | A,B      |            | 4    | 2   | 0        | 8         | 4   |
| Chassis612 | Healthy       | V     | UCSB-5108-AC2   | SN-25  | A,B      | A,B        | 4    | 2   | 0        | 8         | 4   |
+------------+---------------+-------+-----------------+--------+----------+------------+------+-----+----------+-----------+-----+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ChassisInventory.md)