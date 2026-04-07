# Intersight Fabric Interconnect - Filter by model

[[Back]](./FiInventory.md)

```
# iserver get fi --model *6454*

+----+-----------------------+----+-------------+-------------+------------+------+--------------+----------------+---------------+----------+--------+-----+---------+
| ID | Fabric Interconnect   | Id | Model       | Serial      | Management | Oper | Health       | IP             | Version       | Ports    | FanMod | Psu | Storage |
+----+-----------------------+----+-------------+-------------+------------+------+--------------+----------------+---------------+----------+--------+-----+---------+
| 1  | fi1 FI-A              | A  | UCS-FI-6454 | Serial11111 | UCSM       | V    | Healthy      | 10.10.10.10/24 | 1.1(1a)       | 8/8/54   | 4      | 2   | 8       |
| 2  | fi1 FI-B              | B  | UCS-FI-6454 | Serial22222 | UCSM       | V    | Healthy      | 10.10.10.11/24 | 1.1(1a)       | 7/8/54   | 4      | 2   | 8       |
+----+-----------------------+----+-------------+-------------+------------+------+--------------+----------------+---------------+----------+--------+-----+---------+

Filter: name, serial, model
View:   state (def), eth, pc, fc, fpc, fanm, fan, psu, storage, inv, all
```

[[Back]](./FiInventory.md)