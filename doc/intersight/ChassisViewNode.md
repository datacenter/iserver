# Intersight Chassis

## node view

```
# iserver get chassis --name ucsx -v node

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

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer

```
# iserver get chassis --name ucsx -v node

{
    "duration": 7179,
    "isctl": {
        "read": true,
        "calls": 2,
        "success": 2,
        "failed": 0,
        "total_time": 5203
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

2023-12-03 14:34:46.307752	True	2607	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:34:48.921961	True	2596	3	isctl get compute blade --filter "EquipmentChassis/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
```

[[Back]](./ChassisInventory.md)