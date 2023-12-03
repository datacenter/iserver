# Intersight Chassis

## Filter by name

```
# iserver get chassis --name ucsx

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 1
Collect chassis api objects...

Chassis State Summary [#1]
--------------------------

+----------------+---------+-------+-----------+-------------+----------+------------+------+-----+----------+-----------+-----+
| Chassis        | Health  | State | Model     | Serial      | ConnPath | ConnStatus | Node | I/O | Expander | FanModule | PSU |
+----------------+---------+-------+-----------+-------------+----------+------------+------+-----+----------+-----------+-----+
| ucsx-eu-spdc-1 | Healthy | V     | UCSX-9508 | FOX2642P1SA | A,B      | A,B        | 3    | 2   | 2        | 4         | 6   | 
+----------------+---------+-------+-----------+-------------+----------+------------+------+-----+----------+-----------+-----+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer output

```
# iserver get chassis --name ucsx

{
    "duration": 7124,
    "isctl": {
        "read": true,
        "calls": 2,
        "success": 2,
        "failed": 0,
        "total_time": 5006
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

2023-12-03 14:30:19.668284	True	2520	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:30:22.171704	True	2486	1	isctl get chassis profile --filter "AssignedChassis/Moid in ('64be876876752d39013ea7f4')" --expand "ConfigResult" -o json --top 100
```

[[Back]](./ServerInventory.md)