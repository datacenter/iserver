# Intersight Chassis

## net view

```
# iserver get chassis --name ucsx -v net

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 1
Collect chassis api objects...

I/O Module [#2]
---------------

+----------------+-----------------+------+----------+-----------+------------------+-------------+-------------+---------+-------------------+------------+---------------+------+
| Chassis        | I/O Module      | Path | Presence | OperState | Model            | Serial      | P/N         | Version | Vendor            | Host Ports | Network Ports | Fans |
+----------------+-----------------+------+----------+-----------+------------------+-------------+-------------+---------+-------------------+------------+---------------+------+
| ucsx-eu-spdc-1 | I/O #1 (top)    | B    | equipped | V         | UCSX-I-9108-100G | FCH26417CDN | 73-20854-02 | 4.2(3c) | Cisco Systems Inc | 29         | 3             | 3    | 
| ucsx-eu-spdc-1 | I/O #2 (bottom) | A    | equipped | V         | UCSX-I-9108-100G | FCH26417CF0 | 73-20854-02 | 4.3(2a) | Cisco Systems Inc | 3          | 3             | 3    | 
+----------------+-----------------+------+----------+-----------+------------------+-------------+-------------+---------+-------------------+------------+---------------+------+

Network Port [#6]
-----------------

+----------------+-----------------+--------------+-------+-----------+-------------+---------------------+--------------------+-------------------+
| Chassis        | I/O Module      | Network Port | Speed | Switch ID | Switch Port | Switch Port Channel | Switch Transceiver | Switch Port Speed |
+----------------+-----------------+--------------+-------+-----------+-------------+---------------------+--------------------+-------------------+
| ucsx-eu-spdc-1 | I/O #1 (top)    | 1/1          | auto  | B         | 1/1         | 1153                | QSFP-100G-AOC3M    | 100G              | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | 1/2          | 100G  | B         | 1/1         | 1153                | QSFP-100G-AOC3M    | 100G              | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | 1/5          | 100G  | A         | 1/1         | 1025                | QSFP-100G-AOC1M    | 100G              | 
| ucsx-eu-spdc-1 | I/O #2 (bottom) | 2/1          | 100G  | A         | 1/2         | 1025                | QSFP-100G-AOC1M    | 100G              | 
| ucsx-eu-spdc-1 | I/O #2 (bottom) | 2/2          | auto  | A         | 1/2         | 1025                | QSFP-100G-AOC1M    | 100G              | 
| ucsx-eu-spdc-1 | I/O #2 (bottom) | 2/5          | auto  | A         | 1/2         | 1025                | QSFP-100G-AOC1M    | 100G              | 
+----------------+-----------------+--------------+-------+-----------+-------------+---------------------+--------------------+-------------------+

Host Port [#32]
---------------

+----------------+-----------------+------+-----------+--------+-------+-------+--------------+--------------+
| Chassis        | I/O Module      | Path | Host Port | Mode   | Speed | State | State Qual   | Port Channel |
+----------------+-----------------+------+-----------+--------+-------+-------+--------------+--------------+
| ucsx-eu-spdc-1 | I/O #1 (top)    | B    | 1/1/1     | vntag  | 100G  | up    | link-failure | 1282         | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/3     | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/4     | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | B    | 1/1/5     | vntag  | 100G  | up    | link-failure | 1280         | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/7     | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/8     | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | B    | 1/1/9     | vntag  | 100G  | up    | link-failure | 1281         | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/11    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/12    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/13    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/14    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/15    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/16    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/17    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/18    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/19    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/20    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/21    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/22    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/23    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/24    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/25    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/26    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/27    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/28    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/29    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/30    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/31    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #1 (top)    | A    | 1/1/32    | access | auto  | down  | admin-down   | 0            | 
| ucsx-eu-spdc-1 | I/O #2 (bottom) | A    | 1/1/1     | vntag  |       | up    |              | 1281         | 
| ucsx-eu-spdc-1 | I/O #2 (bottom) | A    | 1/1/5     | vntag  |       | up    |              | 1282         | 
| ucsx-eu-spdc-1 | I/O #2 (bottom) | A    | 1/1/9     | vntag  |       | up    |              | 1280         | 
+----------------+-----------------+------+-----------+--------+-------+-------+--------------+--------------+

UCS Domain Switch [#2]
----------------------

+----------------+--------------+-------------------+--------------+----+-------------+-------------+---------------+--------+---------------+
| Chassis        | Domain       | Switch            | Health       | Id | Model       | Serial      | Management IP | Ports  | Version       |
+----------------+--------------+-------------------+--------------+----+-------------+-------------+---------------+--------+---------------+
| ucsx-eu-spdc-1 | ucsx-eu-spdc | ucsx-eu-spdc FI-A | Warnings (1) | A  | UCS-FI-6536 | FDO2713139D | 10.58.28.22   | 6/6/32 | 9.3(5)I42(3c) | 
| ucsx-eu-spdc-1 | ucsx-eu-spdc | ucsx-eu-spdc FI-B | Warnings (1) | B  | UCS-FI-6536 | FDO2713137X | 10.58.28.23   | 6/6/32 | 9.3(5)I42(3c) | 
+----------------+--------------+-------------------+--------------+----+-------------+-------------+---------------+--------+---------------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer

```
# iserver get chassis --name ucsx -v net

{
    "duration": 13394,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 11561
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
        "lines": 8
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 14:34:23.420212	True	2203	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:34:25.349536	True	1915	3	isctl get compute blade --filter "EquipmentChassis/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
2023-12-03 14:34:27.056812	True	1697	2	isctl get equipment iocard --filter "EquipmentChassis/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
2023-12-03 14:34:28.830907	True	1762	32	isctl get ether hostport --filter "RegisteredDevice/Moid in ('64be6ab66f726131018165d8')"  -o json --top 100
2023-12-03 14:34:30.814974	True	1967	6	isctl get ether networkport --filter "RegisteredDevice/Moid in ('64be6ab66f726131018165d8')"  -o json --top 100
2023-12-03 14:34:32.859468	True	2017	2	isctl get network elementsummary --filter "RegisteredDevice/Moid in ('64be6ab66f726131018165d8')"  -o json --top 100
```

[[Back]](./ChassisInventory.md)