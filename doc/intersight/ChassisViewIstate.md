# Intersight Chassis

## istate view

```
# iserver get chassis --name ucsx -v istate

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

Advisory Summary [#0]
---------------------
None

Alarm [#0]
----------
None

Contract [#1]
-------------

+----------------+-------------+------------+----------+--------------------------+-----------------------------+----------------+-------------+
| Chassis        | Status      | Start Date | End Date | Last Updated             | Service Description         | Purchase Order | Sales Order |
+----------------+-------------+------------+----------+--------------------------+-----------------------------+----------------+-------------+
| ucsx-eu-spdc-1 | Not Covered | --         | --       | 2023-12-03T11:49:16.393Z | UCS 9508 Chassis Configured | PR693977       | 114707998   | 
+----------------+-------------+------------+----------+--------------------------+-----------------------------+----------------+-------------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer

```
# iserver get chassis --name ucsx -v istate

{
    "duration": 11743,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 9606
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
        "lines": 7
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 14:34:03.683216	True	1975	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:34:06.022182	True	2321	0	isctl get tam advisoryinstance --filter "RegisteredDevice/Moid in ('64be6ab66f726131018165d8')"  -o json --top 100
2023-12-03 14:34:07.682852	True	1654	2	isctl get cond alarm --filter "RegisteredDevice/Moid in ('64be6ab66f726131018165d8')"  -o json --top 100
2023-12-03 14:34:09.542367	True	1852	1	isctl get asset devicecontractinformation --filter "DeviceId in ('FOX2642P1SA')"  -o json --top 100
2023-12-03 14:34:11.356840	True	1804	1	isctl get chassis profile --filter "AssignedChassis/Moid in ('64be876876752d39013ea7f4')" --expand "ConfigResult" -o json --top 100
```

[[Back]](./ChassisInventory.md)