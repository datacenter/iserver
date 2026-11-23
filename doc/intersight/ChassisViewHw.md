# Intersight Chassis

## hw view

```
# iserver get chassis --name ucsx -v hw

iaccount demo (cache: any)
Select chassis...
Selected chassis: 1
Collect chassis api objects...

Node [#3]
---------

+------------+------+--------------+---------+-------+--------------+--------+-------------+-------------+
| Chassis    | Slot | Name         | Health  | Power | Model        | Serial | CPU         | Memory      |
+------------+------+--------------+---------+-------+--------------+--------+-------------+-------------+
| Chassis333 | 1    | Chassis333-1 | Healthy | on    | UCSX-210C-M6 | SN-64  | 2S 64C 128T | 512.0 [GiB] |
| Chassis333 | 2    | Chassis333-2 | Healthy | on    | UCSX-210C-M6 | SN-52  | 2S 64C 128T | 512.0 [GiB] |
| Chassis333 | 3    | Chassis333-3 | Healthy | on    | UCSX-210C-M6 | SN-18  | 2S 64C 128T | 512.0 [GiB] |
+------------+------+--------------+---------+-------+--------------+--------+-------------+-------------+

I/O Module [#2]
---------------

+------------+-----------------+------+----------+-----------+------------------+--------+-------+---------+-------------------+------------+---------------+------+
| Chassis    | I/O Module      | Path | Presence | OperState | Model            | Serial | P/N   | Version | Vendor            | Host Ports | Network Ports | Fans |
+------------+-----------------+------+----------+-----------+------------------+--------+-------+---------+-------------------+------------+---------------+------+
| Chassis333 | I/O #1 (top)    | B    | equipped | V         | UCSX-I-9108-100G | SN-86  | PN-39 | 1.0(1a) | Cisco Systems Inc | 29         | 3             | 3    |
| Chassis333 | I/O #2 (bottom) | A    | equipped | V         | UCSX-I-9108-100G | SN-12  | PN-26 | 1.0(1a) | Cisco Systems Inc | 3          | 3             | 3    |
+------------+-----------------+------+----------+-----------+------------------+--------+-------+---------+-------------------+------------+---------------+------+

Expander Module [#2]
--------------------

+------------+-------------+----------+-----------+----------------+--------+-------+-------------------+------+
| Chassis    | I/O Module  | Presence | OperState | Model          | Serial | P/N   | Vendor            | Fans |
+------------+-------------+----------+-----------+----------------+--------+-------+-------------------+------+
| Chassis333 | X-Fabric #1 | equipped | V         | UCSX-9508-RBLK | SN-18  | PN-84 | Cisco Systems Inc | 3    |
| Chassis333 | X-Fabric #2 | equipped | V         | UCSX-9508-RBLK | SN-58  | PN-11 | Cisco Systems Inc | 3    |
+------------+-------------+----------+-----------+----------------+--------+-------+-------------------+------+

Fan [#8]
--------

+------------+----------------------+----------+----------+-------+---------------+--------+-------------+
| Chassis    | Fan                  | Control  | Presence | State | Model         | Serial | Part Number |
+------------+----------------------+----------+----------+-------+---------------+--------+-------------+
| Chassis333 | Fan Module 1 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-69  | PN-55       |
| Chassis333 | Fan Module 1 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-40  | PN-97       |
| Chassis333 | Fan Module 2 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-72  | PN-78       |
| Chassis333 | Fan Module 2 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-33  | PN-15       |
| Chassis333 | Fan Module 3 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-91  | PN-65       |
| Chassis333 | Fan Module 3 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-83  | PN-38       |
| Chassis333 | Fan Module 4 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-36  | PN-93       |
| Chassis333 | Fan Module 4 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-19  | PN-65       |
+------------+----------------------+----------+----------+-------+---------------+--------+-------------+

PSU [#6]
--------

+------------+--------+-------+---------+-----------------+--------+
| Chassis    | PSU    | State | Voltage | Model           | Serial |
+------------+--------+-------+---------+-----------------+--------+
| Chassis333 | PSU #1 | X     | 0       | UCSX-PSU-2800AC | SN-19  |
+------------+--------+-------+---------+-----------------+--------+
| Chassis333 | PSU #2 | X     | 0       | UCSX-PSU-2800AC | SN-15  |
+------------+--------+-------+---------+-----------------+--------+
| Chassis333 | PSU #3 | X     | 0       | UCSX-PSU-2800AC | SN-93  |
+------------+--------+-------+---------+-----------------+--------+
| Chassis333 | PSU #4 | X     | 0       | UCSX-PSU-2800AC | SN-78  |
+------------+--------+-------+---------+-----------------+--------+
| Chassis333 | PSU #5 | X     | 0       | UCSX-PSU-2800AC | SN-35  |
+------------+--------+-------+---------+-----------------+--------+
| Chassis333 | PSU #6 | X     | 0       | UCSX-PSU-2800AC | SN-46  |
+------------+--------+-------+---------+-----------------+--------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ChassisInventory.md)