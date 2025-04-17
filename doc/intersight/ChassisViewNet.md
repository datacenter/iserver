# Intersight Chassis

## net view

```
# iserver get chassis --name ucsx -v net

iaccount demo (cache: any)
Select chassis...
Selected chassis: 1
Collect chassis api objects...

I/O Module [#2]
---------------

+------------+-----------------+------+----------+-----------+------------------+--------+-------+---------+-------------------+------------+---------------+------+
| Chassis    | I/O Module      | Path | Presence | OperState | Model            | Serial | P/N   | Version | Vendor            | Host Ports | Network Ports | Fans |
+------------+-----------------+------+----------+-----------+------------------+--------+-------+---------+-------------------+------------+---------------+------+
| Chassis779 | I/O #1 (top)    | B    | equipped | V         | UCSX-I-9108-100G | SN-89  | PN-28 | 1.0(1a) | Cisco Systems Inc | 29         | 3             | 3    |
| Chassis779 | I/O #2 (bottom) | A    | equipped | V         | UCSX-I-9108-100G | SN-21  | PN-26 | 1.0(1a) | Cisco Systems Inc | 3          | 3             | 3    |
+------------+-----------------+------+----------+-----------+------------------+--------+-------+---------+-------------------+------------+---------------+------+

Network Port [#6]
-----------------

+------------+-----------------+--------------+-------+-----------+-------------+---------------------+--------------------+-------------------+
| Chassis    | I/O Module      | Network Port | Speed | Switch ID | Switch Port | Switch Port Channel | Switch Transceiver | Switch Port Speed |
+------------+-----------------+--------------+-------+-----------+-------------+---------------------+--------------------+-------------------+
| Chassis779 | I/O #1 (top)    | 1/1          | auto  | B         | 1/1         | 1153                | QSFP-100G-AOC3M    | 100G              |
| Chassis779 | I/O #1 (top)    | 1/2          | 100G  | B         | 1/1         | 1153                | QSFP-100G-AOC3M    | 100G              |
| Chassis779 | I/O #1 (top)    | 1/5          | 100G  | A         | 1/1         | 1025                | QSFP-100G-AOC1M    | 100G              |
| Chassis779 | I/O #2 (bottom) | 2/1          | 100G  | A         | 1/2         | 1025                | QSFP-100G-AOC1M    | 100G              |
| Chassis779 | I/O #2 (bottom) | 2/2          | auto  | A         | 1/2         | 1025                | QSFP-100G-AOC1M    | 100G              |
| Chassis779 | I/O #2 (bottom) | 2/5          | auto  | A         | 1/2         | 1025                | QSFP-100G-AOC1M    | 100G              |
+------------+-----------------+--------------+-------+-----------+-------------+---------------------+--------------------+-------------------+

Host Port [#32]
---------------

+------------+-----------------+------+-----------+--------+-------+-------+--------------+--------------+
| Chassis    | I/O Module      | Path | Host Port | Mode   | Speed | State | State Qual   | Port Channel |
+------------+-----------------+------+-----------+--------+-------+-------+--------------+--------------+
| Chassis779 | I/O #1 (top)    | B    | 1/1/1     | vntag  | 100G  | up    | link-failure | 1282         |
| Chassis779 | I/O #1 (top)    | A    | 1/1/3     | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/4     | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | B    | 1/1/5     | vntag  | 100G  | up    | link-failure | 1280         |
| Chassis779 | I/O #1 (top)    | A    | 1/1/7     | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/8     | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | B    | 1/1/9     | vntag  | 100G  | up    | link-failure | 1281         |
| Chassis779 | I/O #1 (top)    | A    | 1/1/11    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/12    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/13    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/14    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/15    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/16    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/17    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/18    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/19    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/20    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/21    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/22    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/23    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/24    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/25    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/26    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/27    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/28    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/29    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/30    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/31    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #1 (top)    | A    | 1/1/32    | access | auto  | down  | admin-down   | 0            |
| Chassis779 | I/O #2 (bottom) | A    | 1/1/1     | vntag  |       | up    |              | 1281         |
| Chassis779 | I/O #2 (bottom) | A    | 1/1/5     | vntag  |       | up    |              | 1282         |
| Chassis779 | I/O #2 (bottom) | A    | 1/1/9     | vntag  |       | up    |              | 1280         |
+------------+-----------------+------+-----------+--------+-------+-------+--------------+--------------+

UCS Domain Switch [#2]
----------------------

+------------+-----------+----------+--------------+----+-------------+--------+---------------+--------+---------+
| Chassis    | Domain    | Switch   | Health       | Id | Model       | Serial | Management IP | Ports  | Version |
+------------+-----------+----------+--------------+----+-------------+--------+---------------+--------+---------+
| Chassis779 | Domain-32 | Switch A | Warnings (1) | A  | UCS-FI-6536 | SN-71  | 10.156.3.189  | 6/6/32 | 1.0(1a) |
| Chassis779 | Domain-32 | Switch B | Warnings (1) | B  | UCS-FI-6536 | SN-37  | 10.111.48.108 | 6/6/32 | 1.0(1a) |
+------------+-----------+----------+--------------+----+-------------+--------+---------------+--------+---------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ChassisInventory.md)