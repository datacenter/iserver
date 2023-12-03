# Intersight Chassis

## hw view

```
# iserver get chassis --name ucsx -v hw

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 1
Collect chassis api objects...

Node [#3]
---------

+----------------+------+------------------+---------+-------+--------------+-------------+-------------+-------------+
| Chassis        | Slot | Name             | Health  | Power | Model        | Serial      | CPU         | Memory      |
+----------------+------+------------------+---------+-------+--------------+-------------+-------------+-------------+
| ucsx-eu-spdc-1 | 1    | ucsx-eu-spdc-1-1 | Healthy | on    | UCSX-210C-M6 | FCH26447781 | 2S 64C 128T | 512.0 [GiB] | 
| ucsx-eu-spdc-1 | 2    | ucsx-eu-spdc-1-2 | Healthy | on    | UCSX-210C-M6 | FCH2644774P | 2S 64C 128T | 512.0 [GiB] | 
| ucsx-eu-spdc-1 | 3    | ucsx-eu-spdc-1-3 | Healthy | on    | UCSX-210C-M6 | FCH264477DW | 2S 64C 128T | 512.0 [GiB] | 
+----------------+------+------------------+---------+-------+--------------+-------------+-------------+-------------+

I/O Module [#2]
---------------

+----------------+-----------------+------+----------+-----------+------------------+-------------+-------------+---------+-------------------+------------+---------------+------+
| Chassis        | I/O Module      | Path | Presence | OperState | Model            | Serial      | P/N         | Version | Vendor            | Host Ports | Network Ports | Fans |
+----------------+-----------------+------+----------+-----------+------------------+-------------+-------------+---------+-------------------+------------+---------------+------+
| ucsx-eu-spdc-1 | I/O #1 (top)    | B    | equipped | V         | UCSX-I-9108-100G | FCH26417CDN | 73-20854-02 | 4.2(3c) | Cisco Systems Inc | 29         | 3             | 3    | 
| ucsx-eu-spdc-1 | I/O #2 (bottom) | A    | equipped | V         | UCSX-I-9108-100G | FCH26417CF0 | 73-20854-02 | 4.3(2a) | Cisco Systems Inc | 3          | 3             | 3    | 
+----------------+-----------------+------+----------+-----------+------------------+-------------+-------------+---------+-------------------+------------+---------------+------+

Expander Module [#2]
--------------------

+----------------+-------------+----------+-----------+----------------+-------------+-------------+-------------------+------+
| Chassis        | I/O Module  | Presence | OperState | Model          | Serial      | P/N         | Vendor            | Fans |
+----------------+-------------+----------+-----------+----------------+-------------+-------------+-------------------+------+
| ucsx-eu-spdc-1 | X-Fabric #1 | equipped | V         | UCSX-9508-RBLK | FCH2631760N | 73-19787-04 | Cisco Systems Inc | 3    | 
| ucsx-eu-spdc-1 | X-Fabric #2 | equipped | V         | UCSX-9508-RBLK | FCH263176WA | 73-19787-04 | Cisco Systems Inc | 3    | 
+----------------+-------------+----------+-----------+----------------+-------------+-------------+-------------------+------+

Fan [#8]
--------

+----------------+----------------------+----------+----------+-------+---------------+-------------+-------------+
| Chassis        | Fan                  | Control  | Presence | State | Model         | Serial      | Part Number |
+----------------+----------------------+----------+----------+-------+---------------+-------------+-------------+
| ucsx-eu-spdc-1 | Fan Module 1 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH26387AGB | 73-19422-04 | 
| ucsx-eu-spdc-1 | Fan Module 1 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH26387AGB | 73-19422-04 | 
| ucsx-eu-spdc-1 | Fan Module 2 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH263471C2 | 73-19422-04 | 
| ucsx-eu-spdc-1 | Fan Module 2 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH263471C2 | 73-19422-04 | 
| ucsx-eu-spdc-1 | Fan Module 3 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH2634719M | 73-19422-04 | 
| ucsx-eu-spdc-1 | Fan Module 3 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH2634719M | 73-19422-04 | 
| ucsx-eu-spdc-1 | Fan Module 4 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH2634705K | 73-19422-04 | 
| ucsx-eu-spdc-1 | Fan Module 4 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH2634705K | 73-19422-04 | 
+----------------+----------------------+----------+----------+-------+---------------+-------------+-------------+

PSU [#6]
--------

+----------------+--------+-------+---------+-----------------+-------------+
| Chassis        | PSU    | State | Voltage | Model           | Serial      |
+----------------+--------+-------+---------+-----------------+-------------+
| ucsx-eu-spdc-1 | PSU #1 | X     | 0       | UCSX-PSU-2800AC | DTM26460266 | 
+----------------+--------+-------+---------+-----------------+-------------+
| ucsx-eu-spdc-1 | PSU #2 | X     | 0       | UCSX-PSU-2800AC | DTM2646028Y | 
+----------------+--------+-------+---------+-----------------+-------------+
| ucsx-eu-spdc-1 | PSU #3 | X     | 0       | UCSX-PSU-2800AC | DTM2646028Z | 
+----------------+--------+-------+---------+-----------------+-------------+
| ucsx-eu-spdc-1 | PSU #4 | X     | 0       | UCSX-PSU-2800AC | DTM264602JB | 
+----------------+--------+-------+---------+-----------------+-------------+
| ucsx-eu-spdc-1 | PSU #5 | X     | 0       | UCSX-PSU-2800AC | DTM2646028N | 
+----------------+--------+-------+---------+-----------------+-------------+
| ucsx-eu-spdc-1 | PSU #6 | X     | 0       | UCSX-PSU-2800AC | DTM264602J9 | 
+----------------+--------+-------+---------+-----------------+-------------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer

```
# iserver get chassis --name ucsx -v hw

{
    "duration": 17388,
    "isctl": {
        "read": true,
        "calls": 8,
        "success": 8,
        "failed": 0,
        "total_time": 15425
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": true,
        "lines": 10
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 14:33:10.760318	True	1828	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:33:12.525925	True	1756	3	isctl get compute blade --filter "EquipmentChassis/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
2023-12-03 14:33:14.429595	True	1890	2	isctl get equipment iocard --filter "EquipmentChassis/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
2023-12-03 14:33:16.972102	True	2528	2	isctl get equipment expandermodule --filter "EquipmentChassis/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
2023-12-03 14:33:19.240836	True	2260	1	isctl get equipment fancontrol --filter "Parent/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
2023-12-03 14:33:21.103036	True	1831	4	isctl get equipment fanmodule --filter "EquipmentChassis/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
2023-12-03 14:33:22.743409	True	1622	8	isctl get equipment fan --filter "Parent/Moid in ('64be89ab76752d39013f54fc', '64be89ab76752d39013f550b', '64be89ac76752d39013f552c', '64be89ac76752d39013f5544')"  -o json --top 100
2023-12-03 14:33:24.465335	True	1710	6	isctl get equipment psu --filter "Parent/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
```

[[Back]](./ChassisInventory.md)