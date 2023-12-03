# Intersight Chassis

## psu view

```
# iserver get chassis --name ucsx -v psu

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 1
Collect chassis api objects...

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
# iserver get chassis --name ucsx -v psu

{
    "duration": 6548,
    "isctl": {
        "read": true,
        "calls": 2,
        "success": 2,
        "failed": 0,
        "total_time": 4412
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

2023-12-03 14:35:26.478795	True	2215	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:35:28.686919	True	2197	6	isctl get equipment psu --filter "Parent/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
```

[[Back]](./ChassisInventory.md)