# Intersight Chassis

## adv view

```
# iserver get chassis -v adv

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 4
Collect chassis api objects...

Advisory Summary [#0]
---------------------
None

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer

```
# iserver get chassis -v adv

{
    "duration": 6466,
    "isctl": {
        "read": true,
        "calls": 2,
        "success": 2,
        "failed": 0,
        "total_time": 4253
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

2023-12-03 14:31:14.707635	True	2604	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:31:16.369477	True	1649	0	isctl get tam advisoryinstance --filter "RegisteredDevice/Moid in ('61bb97146f72612d301e5946', '64be6ab66f726131018165d8', '6501db456f726131016b7aea', '6501db456f726131016b7aea')"  -o json --top 100
```

[[Back]](./ChassisInventory.md)