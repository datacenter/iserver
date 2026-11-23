# Intersight Chassis

## contract view

```
# iserver get chassis -v contract

iaccount demo (cache: any)
Select chassis...
Selected chassis: 4
Collect chassis api objects...

Contract [#4]
-------------

+------------+-------------+------------+----------+--------------------------+------------------------------------------------------+----------------+-------------+
| Chassis    | Status      | Start Date | End Date | Last Updated             | Service Description                                  | Purchase Order | Sales Order |
+------------+-------------+------------+----------+--------------------------+------------------------------------------------------+----------------+-------------+
| Chassis118 | Not Covered | --         | --       | 2025-01-01T00:00:00.000Z | Cisco UCS C3260 Base Chassis w/4x PSU, SSD, Railkit  | PO145          | SO37        |
| Chassis547 | Not Covered | --         | --       | 2025-01-01T00:00:00.000Z | UCS 9508 Chassis Configured                          | PO238          | SO185       |
| Chassis743 | Not Covered | --         | --       | 2025-01-01T00:00:00.000Z | UCS 5108 Blade Server AC2 Chassis/0 PSU/8 fans/0 FEX | PO238          | SO158       |
| Chassis309 | Not Covered | --         | --       | 2025-01-01T00:00:00.000Z | UCS 5108 Blade Server AC2 Chassis/0 PSU/8 fans/0 FEX | PO83           | SO129       |
+------------+-------------+------------+----------+--------------------------+------------------------------------------------------+----------------+-------------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ChassisInventory.md)