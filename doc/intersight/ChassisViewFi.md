# Intersight Chassis

## fi view

```
# iserver get chassis -v fi

iaccount demo (cache: any)
Select chassis...
Selected chassis: 4
Collect chassis api objects...

UCS Domain Switch [#6]
----------------------

+------------+-----------+----------+--------------+----+-------------+--------+----------------+----------+---------+
| Chassis    | Domain    | Switch   | Health       | Id | Model       | Serial | Management IP  | Ports    | Version |
+------------+-----------+----------+--------------+----+-------------+--------+----------------+----------+---------+
| Chassis721 | Domain-98 | Switch A | Warnings (1) | A  | UCS-FI-6536 | SN-51  | 10.48.121.179  | 6/6/32   | 1.0(1a) |
| Chassis721 | Domain-98 | Switch B | Warnings (1) | B  | UCS-FI-6536 | SN-96  | 10.120.114.64  | 6/6/32   | 1.0(1a) |
| Chassis206 | Domain-31 | Switch A | Healthy      | A  | UCS-FI-6454 | SN-70  | 10.20.34.203   | 19/19/54 | 1.0(1a) |
| Chassis206 | Domain-31 | Switch B | Healthy      | B  | UCS-FI-6454 | SN-96  | 10.46.169.158  | 19/19/54 | 1.0(1a) |
| Chassis433 | Domain-81 | Switch A | Healthy      | A  | UCS-FI-6454 | SN-92  | 10.162.247.13  | 19/19/54 | 1.0(1a) |
| Chassis433 | Domain-81 | Switch B | Healthy      | B  | UCS-FI-6454 | SN-97  | 10.139.101.107 | 19/19/54 | 1.0(1a) |
+------------+-----------+----------+--------------+----+-------------+--------+----------------+----------+---------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ChassisInventory.md)