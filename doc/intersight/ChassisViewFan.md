# Intersight Chassis

## fan view

```
# iserver get chassis --name ucsx -v fan

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 1
Collect chassis api objects...

Fan [#8]
--------

+----------------+----------------------+----------+----------+-------+---------------+-------------+-------------+
| Chassis        | Fan                  | Control  | Presence | State | Model         | Serial      | Part Number |
+----------------+----------------------+----------+----------+-------+---------------+-------------+-------------+
| ucsx-eu-spdc-1 | Fan Module 1 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH26387AGB | 73-19422-04 | 
| ucsx-eu-spdc-1 | Fan Module 1 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH26387AGB | 73-19422-04 | 
| ucsx-eu-spdc-1 | Fan Module 2 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH263471C2 | 73-19422-04 | 
| ucsx-eu-spdc-1 | Fan Module 2 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH263471C2 | 73-19422-04 | 
| ucsx-eu-spdc-1 | Fan Module 3 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH2634719M | 73-19422-04 | 
| ucsx-eu-spdc-1 | Fan Module 3 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH2634719M | 73-19422-04 | 
| ucsx-eu-spdc-1 | Fan Module 4 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH2634705K | 73-19422-04 | 
| ucsx-eu-spdc-1 | Fan Module 4 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | FCH2634705K | 73-19422-04 | 
+----------------+----------------------+----------+----------+-------+---------------+-------------+-------------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer

```
# iserver get chassis --name ucsx -v fan

{
    "duration": 12597,
    "isctl": {
        "read": true,
        "calls": 4,
        "success": 4,
        "failed": 0,
        "total_time": 10682
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
        "lines": 6
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 14:32:20.080476	True	2375	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:32:22.903158	True	2810	1	isctl get equipment fancontrol --filter "Parent/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
2023-12-03 14:32:25.944499	True	3026	4	isctl get equipment fanmodule --filter "EquipmentChassis/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
2023-12-03 14:32:28.440854	True	2471	8	isctl get equipment fan --filter "Parent/Moid in ('64be89ab76752d39013f54fc', '64be89ab76752d39013f550b', '64be89ac76752d39013f552c', '64be89ac76752d39013f5544')"  -o json --top 100
```

[[Back]](./ChassisInventory.md)