# Intersight Chassis

## Default output

```
# iserver get chassis

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 4
Collect chassis api objects...

Chassis State Summary [#4]
--------------------------

+--------------------------+---------+-------+-----------------+-------------+----------+------------+------+-----+----------+-----------+-----+
| Chassis                  | Health  | State | Model           | Serial      | ConnPath | ConnStatus | Node | I/O | Expander | FanModule | PSU |
+--------------------------+---------+-------+-----------------+-------------+----------+------------+------+-----+----------+-----------+-----+
| ynas-eu-spdc-FOX2034GCLV | Healthy | --    | UCSS-S3260-BASE | FOX2034GCLV |          |            | 1    | 0   | 0        | 4         | 4   | 
| ucsx-eu-spdc-1           | Healthy | V     | UCSX-9508       | FOX2642P1SA | A,B      | A,B        | 3    | 2   | 2        | 4         | 6   | 
| FI-ucsb1-eu-spdc-1       | Healthy | V     | UCSB-5108-AC2   | FOX2403P669 | A,B      | A,B        | 4    | 2   | 0        | 8         | 4   | 
| FI-ucsb1-eu-spdc-2       | Healthy | V     | UCSB-5108-AC2   | FOX2403P2Z9 | A,B      | A,B        | 4    | 2   | 0        | 8         | 4   | 
+--------------------------+---------+-------+-----------------+-------------+----------+------------+------+-----+----------+-----------+-----+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer output

```
# iserver get chassis

{
    "duration": 6513,
    "isctl": {
        "read": true,
        "calls": 2,
        "success": 2,
        "failed": 0,
        "total_time": 4579
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

2023-12-03 14:36:17.159314	True	2640	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:36:19.116491	True	1939	1	isctl get chassis profile --filter "AssignedChassis/Moid in ('61bb973576752d3139b05c2e', '64be876876752d39013ea7f4', '6501db4b76752d3901eb37bf', '6501db4b76752d3901eb37c1')" --expand "ConfigResult" -o json --top 100
```

[[Back]](./ChassisInventory.md)