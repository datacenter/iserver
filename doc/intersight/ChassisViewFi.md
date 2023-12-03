# Intersight Chassis

## fi view

```
# iserver get chassis -v fi

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 4
Collect chassis api objects...

UCS Domain Switch [#6]
----------------------

+--------------------+------------------+-----------------------+--------------+----+-------------+-------------+---------------+----------+---------------+
| Chassis            | Domain           | Switch                | Health       | Id | Model       | Serial      | Management IP | Ports    | Version       |
+--------------------+------------------+-----------------------+--------------+----+-------------+-------------+---------------+----------+---------------+
| ucsx-eu-spdc-1     | ucsx-eu-spdc     | ucsx-eu-spdc FI-A     | Warnings (1) | A  | UCS-FI-6536 | FDO2713139D | 10.58.28.22   | 6/6/32   | 9.3(5)I42(3c) | 
| ucsx-eu-spdc-1     | ucsx-eu-spdc     | ucsx-eu-spdc FI-B     | Warnings (1) | B  | UCS-FI-6536 | FDO2713137X | 10.58.28.23   | 6/6/32   | 9.3(5)I42(3c) | 
| FI-ucsb1-eu-spdc-1 | FI-ucsb1-eu-spdc | FI-ucsb1-eu-spdc FI-A | Healthy      | A  | UCS-FI-6454 | FDO241604GJ | 10.58.24.17   | 19/19/54 | 4.2(3d)       | 
| FI-ucsb1-eu-spdc-1 | FI-ucsb1-eu-spdc | FI-ucsb1-eu-spdc FI-B | Healthy      | B  | UCS-FI-6454 | FDO241604KU | 10.58.24.18   | 19/19/54 | 4.2(3d)       | 
| FI-ucsb1-eu-spdc-2 | FI-ucsb1-eu-spdc | FI-ucsb1-eu-spdc FI-A | Healthy      | A  | UCS-FI-6454 | FDO241604GJ | 10.58.24.17   | 19/19/54 | 4.2(3d)       | 
| FI-ucsb1-eu-spdc-2 | FI-ucsb1-eu-spdc | FI-ucsb1-eu-spdc FI-B | Healthy      | B  | UCS-FI-6454 | FDO241604KU | 10.58.24.18   | 19/19/54 | 4.2(3d)       | 
+--------------------+------------------+-----------------------+--------------+----+-------------+-------------+---------------+----------+---------------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer

```
# iserver get chassis -v fi

{
    "duration": 6721,
    "isctl": {
        "read": true,
        "calls": 2,
        "success": 2,
        "failed": 0,
        "total_time": 4685
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

2023-12-03 14:32:40.640316	True	2429	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:32:42.908739	True	2256	4	isctl get network elementsummary --filter "RegisteredDevice/Moid in ('61bb97146f72612d301e5946', '64be6ab66f726131018165d8', '6501db456f726131016b7aea', '6501db456f726131016b7aea')"  -o json --top 100
```

[[Back]](./ChassisInventory.md)