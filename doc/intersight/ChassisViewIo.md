# Intersight Chassis

## io view

```
# iserver get chassis -v io

iaccount demo (cache: any)
Select chassis...
Selected chassis: 4
Collect chassis api objects...

I/O Module [#6]
---------------

+------------+-----------------+------+----------+-----------+------------------+--------+-------+---------+-------------------+------------+---------------+------+
| Chassis    | I/O Module      | Path | Presence | OperState | Model            | Serial | P/N   | Version | Vendor            | Host Ports | Network Ports | Fans |
+------------+-----------------+------+----------+-----------+------------------+--------+-------+---------+-------------------+------------+---------------+------+
| Chassis561 | I/O #1 (top)    | B    | equipped | V         | UCSX-I-9108-100G | SN-48  | PN-80 | 1.0(1a) | Cisco Systems Inc | 29         | 3             | 3    |
| Chassis561 | I/O #2 (bottom) | A    | equipped | V         | UCSX-I-9108-100G | SN-29  | PN-82 | 1.0(1a) | Cisco Systems Inc | 3          | 3             | 3    |
| Chassis493 | I/O #1 (left)   | A    | equipped | V         | UCS-IOM-2408     | SN-40  | PN-96 | 1.0(1a) | Cisco Systems Inc | 0          | 0             | 0    |
| Chassis493 | I/O #2 (right)  | B    | equipped | V         | UCS-IOM-2408     | SN-79  | PN-57 | 1.0(1a) | Cisco Systems Inc | 0          | 0             | 0    |
| Chassis815 | I/O #1 (left)   | A    | equipped | V         | UCS-IOM-2408     | SN-79  | PN-61 | 1.0(1a) | Cisco Systems Inc | 0          | 0             | 0    |
| Chassis815 | I/O #2 (right)  | B    | equipped | V         | UCS-IOM-2408     | SN-58  | PN-73 | 1.0(1a) | Cisco Systems Inc | 0          | 0             | 0    |
+------------+-----------------+------+----------+-----------+------------------+--------+-------+---------+-------------------+------------+---------------+------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ChassisInventory.md)