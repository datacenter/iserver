# Intersight Chassis

## exp view

```
# iserver get chassis -v exp

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 4
Collect chassis api objects...

Expander Module [#2]
--------------------

+----------------+-------------+----------+-----------+----------------+-------------+-------------+-------------------+------+
| Chassis        | I/O Module  | Presence | OperState | Model          | Serial      | P/N         | Vendor            | Fans |
+----------------+-------------+----------+-----------+----------------+-------------+-------------+-------------------+------+
| ucsx-eu-spdc-1 | X-Fabric #1 | equipped | V         | UCSX-9508-RBLK | FCH2631760N | 73-19787-04 | Cisco Systems Inc | 3    | 
| ucsx-eu-spdc-1 | X-Fabric #2 | equipped | V         | UCSX-9508-RBLK | FCH263176WA | 73-19787-04 | Cisco Systems Inc | 3    | 
+----------------+-------------+----------+-----------+----------------+-------------+-------------+-------------------+------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer

```
# iserver get chassis -v exp

{
    "duration": 7457,
    "isctl": {
        "read": true,
        "calls": 2,
        "success": 2,
        "failed": 0,
        "total_time": 5404
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

2023-12-03 14:32:01.753470	True	2868	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:32:04.312024	True	2536	2	isctl get equipment expandermodule --filter "EquipmentChassis/Moid in ('61bb973576752d3139b05c2e', '64be876876752d39013ea7f4', '6501db4b76752d3901eb37bf', '6501db4b76752d3901eb37c1')"  -o json --top 100
```

[[Back]](./ChassisInventory.md)