# Intersight Chassis

## Filter by model

```
# iserver get chassis --model 5108

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 2
Collect chassis api objects...

Chassis State Summary [#2]
--------------------------

+--------------------+---------+-------+---------------+-------------+----------+------------+------+-----+----------+-----------+-----+
| Chassis            | Health  | State | Model         | Serial      | ConnPath | ConnStatus | Node | I/O | Expander | FanModule | PSU |
+--------------------+---------+-------+---------------+-------------+----------+------------+------+-----+----------+-----------+-----+
| FI-ucsb1-eu-spdc-1 | Healthy | V     | UCSB-5108-AC2 | FOX2403P669 | A,B      | A,B        | 4    | 2   | 0        | 8         | 4   | 
| FI-ucsb1-eu-spdc-2 | Healthy | V     | UCSB-5108-AC2 | FOX2403P2Z9 | A,B      | A,B        | 4    | 2   | 0        | 8         | 4   | 
+--------------------+---------+-------+---------------+-------------+----------+------------+------+-----+----------+-----------+-----+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer output

```
# iserver get chassis --model 5108

{
    "duration": 7313,
    "isctl": {
        "read": true,
        "calls": 2,
        "success": 2,
        "failed": 0,
        "total_time": 5310
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

2023-12-03 14:30:56.864083	True	2405	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:30:59.782367	True	2905	0	isctl get chassis profile --filter "AssignedChassis/Moid in ('6501db4b76752d3901eb37bf', '6501db4b76752d3901eb37c1')" --expand "ConfigResult" -o json --top 100
```

[[Back]](./ServerInventory.md)