# Intersight Chassis

## Filter by serial

```
# iserver get chassis --serial FOX2403P669 --serial FOX2642P1SA

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 2
Collect chassis api objects...

Chassis State Summary [#2]
--------------------------

+--------------------+---------+-------+---------------+-------------+----------+------------+------+-----+----------+-----------+-----+
| Chassis            | Health  | State | Model         | Serial      | ConnPath | ConnStatus | Node | I/O | Expander | FanModule | PSU |
+--------------------+---------+-------+---------------+-------------+----------+------------+------+-----+----------+-----------+-----+
| ucsx-eu-spdc-1     | Healthy | V     | UCSX-9508     | FOX2642P1SA | A,B      | A,B        | 3    | 2   | 2        | 4         | 6   | 
| FI-ucsb1-eu-spdc-1 | Healthy | V     | UCSB-5108-AC2 | FOX2403P669 | A,B      | A,B        | 4    | 2   | 0        | 8         | 4   | 
+--------------------+---------+-------+---------------+-------------+----------+------------+------+-----+----------+-----------+-----+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer output

```
# iserver get chassis --serial FOX2403P669 --serial FOX2642P1SA

{
    "duration": 7956,
    "isctl": {
        "read": true,
        "calls": 2,
        "success": 2,
        "failed": 0,
        "total_time": 5634
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
        "lines": 4
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 14:30:38.670745	True	3019	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:30:41.304684	True	2615	1	isctl get chassis profile --filter "AssignedChassis/Moid in ('64be876876752d39013ea7f4', '6501db4b76752d3901eb37bf')" --expand "ConfigResult" -o json --top 100
```

[[Back]](./ServerInventory.md)