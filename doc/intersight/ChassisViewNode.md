# Intersight Chassis

## node view

```
# iserver get chassis --name ucsx -v node

iaccount demo (cache: any)
Select chassis...
Selected chassis: 1
Collect chassis api objects...

Node [#3]
---------

+------------+------+--------------+---------+-------+--------------+--------+-------------+-------------+
| Chassis    | Slot | Name         | Health  | Power | Model        | Serial | CPU         | Memory      |
+------------+------+--------------+---------+-------+--------------+--------+-------------+-------------+
| Chassis285 | 1    | Chassis285-1 | Healthy | on    | UCSX-210C-M6 | SN-61  | 2S 64C 128T | 512.0 [GiB] |
| Chassis285 | 2    | Chassis285-2 | Healthy | on    | UCSX-210C-M6 | SN-16  | 2S 64C 128T | 512.0 [GiB] |
| Chassis285 | 3    | Chassis285-3 | Healthy | on    | UCSX-210C-M6 | SN-43  | 2S 64C 128T | 512.0 [GiB] |
+------------+------+--------------+---------+-------+--------------+--------+-------------+-------------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ChassisInventory.md)