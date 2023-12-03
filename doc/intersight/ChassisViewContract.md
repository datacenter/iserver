# Intersight Chassis

## contract view

```
# iserver get chassis -v contract

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 4
Collect chassis api objects...

Contract [#4]
-------------

+--------------------------+-------------+------------+----------+--------------------------+------------------------------------------------------+----------------+-------------+
| Chassis                  | Status      | Start Date | End Date | Last Updated             | Service Description                                  | Purchase Order | Sales Order |
+--------------------------+-------------+------------+----------+--------------------------+------------------------------------------------------+----------------+-------------+
| ynas-eu-spdc-FOX2034GCLV | Not Covered | --         | --       | 2023-12-03T00:18:56.117Z | Cisco UCS C3260 Base Chassis w/4x PSU, SSD, Railkit  | 6710005409     | 103763581   | 
| ucsx-eu-spdc-1           | Not Covered | --         | --       | 2023-12-03T11:49:16.393Z | UCS 9508 Chassis Configured                          | PR693977       | 114707998   | 
| FI-ucsb1-eu-spdc-1       | Not Covered | --         | --       | 2023-12-03T02:08:58.181Z | UCS 5108 Blade Server AC2 Chassis/0 PSU/8 fans/0 FEX | 6710008742     | 110341108   | 
| FI-ucsb1-eu-spdc-2       | Not Covered | --         | --       | 2023-12-03T02:08:58.181Z | UCS 5108 Blade Server AC2 Chassis/0 PSU/8 fans/0 FEX | 6710008742     | 110341108   | 
+--------------------------+-------------+------------+----------+--------------------------+------------------------------------------------------+----------------+-------------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer

```
# iserver get chassis -v contract

{
    "duration": 5774,
    "isctl": {
        "read": true,
        "calls": 2,
        "success": 2,
        "failed": 0,
        "total_time": 3724
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

2023-12-03 14:31:45.398845	True	1851	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:31:47.283928	True	1873	4	isctl get asset devicecontractinformation --filter "DeviceId in ('FOX2034GCLV', 'FOX2642P1SA', 'FOX2403P669', 'FOX2403P2Z9')"  -o json --top 100
```

[[Back]](./ChassisInventory.md)