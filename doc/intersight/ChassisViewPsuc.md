# Intersight Chassis

## psuc view

```
# iserver get chassis -v psuc

iaccount demo (cache: any)
Select chassis...
Selected chassis: 4
Collect chassis api objects...

PSU Control [#4]
----------------

+------------+--------------------+---------------------+-------------------+-----------------+
| Chassis    | Input Power Health | Output Power Health | Redundancy Health | Redundancy Mode |
+------------+--------------------+---------------------+-------------------+-----------------+
| Chassis405 | --                 | --                  | --                | --              |
| Chassis229 | V                  | V                   | V                 | Grid            |
| Chassis164 | V                  | V                   | V                 | n+1             |
| Chassis811 | V                  | V                   | V                 | n+1             |
+------------+--------------------+---------------------+-------------------+-----------------+

Power Control [#4]
------------------

+------------+-----------+--------------+-----------------+--------------+---------+---------+-----------------------------+----------------------+-----------------+-----------------+
| Chassis    | Save Mode | Ext Capacity | Dyn Rebalancing | Alloc Budget | Max Req | Min Req | Max Avail Non-Redundant (N) | Max Avail Grid (N+N) | Max Avail (N+1) | Max Avail (N+2) |
+------------+-----------+--------------+-----------------+--------------+---------+---------+-----------------------------+----------------------+-----------------+-----------------+
| Chassis405 | --        | --           | --              | --           | --      | --      | --                          | --                   | --              | --              |
| Chassis229 | Disabled  | Enabled      | Enabled         | --           | 6680 W  | 3773 W  | 15218 W                     | 10500 W              | 17500 W         | 14000 W         |
| Chassis164 | Disabled  | Enabled      | Enabled         | --           | 2812 W  | 2100 W  | 0 W                         | 0 W                  | 0 W             | 0 W             |
| Chassis811 | Disabled  | Enabled      | Enabled         | --           | 2900 W  | 2100 W  | 0 W                         | 0 W                  | 0 W             | 0 W             |
+------------+-----------+--------------+-----------------+--------------+---------+---------+-----------------------------+----------------------+-----------------+-----------------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ChassisInventory.md)