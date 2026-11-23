# Intersight Chassis

## istate view

```
# iserver get chassis --name ucsx -v istate

iaccount demo (cache: any)
Select chassis...
Selected chassis: 1
Collect chassis api objects...

Chassis State Summary [#1]
--------------------------

+------------+---------+-------+-----------+--------+----------+------------+------+-----+----------+-----------+-----+
| Chassis    | Health  | State | Model     | Serial | ConnPath | ConnStatus | Node | I/O | Expander | FanModule | PSU |
+------------+---------+-------+-----------+--------+----------+------------+------+-----+----------+-----------+-----+
| Chassis953 | Healthy | V     | UCSX-9508 | SN-70  | A,B      | A,B        | 3    | 2   | 2        | 4         | 6   |
+------------+---------+-------+-----------+--------+----------+------------+------+-----+----------+-----------+-----+

Advisory Summary [#0]
---------------------
None

Alarm [#0]
----------
None

Contract [#1]
-------------

+------------+-------------+------------+----------+--------------------------+-----------------------------+----------------+-------------+
| Chassis    | Status      | Start Date | End Date | Last Updated             | Service Description         | Purchase Order | Sales Order |
+------------+-------------+------------+----------+--------------------------+-----------------------------+----------------+-------------+
| Chassis953 | Not Covered | --         | --       | 2025-01-01T00:00:00.000Z | UCS 9508 Chassis Configured | PO244          | SO169       |
+------------+-------------+------------+----------+--------------------------+-----------------------------+----------------+-------------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ChassisInventory.md)