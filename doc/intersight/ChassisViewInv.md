# Intersight Chassis

## inv view

```
# iserver get chassis --name ucsx -v inv

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 1
Collect chassis api objects...

Chassis Inventory: ucsx-eu-spdc-1
---------------------------------

+----------+----------------------+------------------+-------------------+-------------+------------------+
| Type     | Name                 | Model            | Vendor            | Serial      | Pid              |
+----------+----------------------+------------------+-------------------+-------------+------------------+
| Chassis  | ucsx-eu-spdc-1       | UCSX-9508        | Cisco Systems Inc | FOX2642P1SA | UCSX-9508        | 
| Node     | Server #1            | UCSX-210C-M6     | Cisco Systems Inc | FCH26447781 | UCSX-210C-M6     | 
| Node     | Server #2            | UCSX-210C-M6     | Cisco Systems Inc | FCH2644774P | UCSX-210C-M6     | 
| Node     | Server #3            | UCSX-210C-M6     | Cisco Systems Inc | FCH264477DW | UCSX-210C-M6     | 
| IO       | I/O #1 (top)         | UCSX-I-9108-100G | Cisco Systems Inc | FCH26417CDN | UCSX-I-9108-100G | 
| IO       | I/O #2 (bottom)      | UCSX-I-9108-100G | Cisco Systems Inc | FCH26417CF0 | UCSX-I-9108-100G | 
| Expander | X-Fabric #1          | UCSX-9508-RBLK   | Cisco Systems Inc | FCH2631760N | UCSX-9508-RBLK   | 
| Expander | X-Fabric #2          | UCSX-9508-RBLK   | Cisco Systems Inc | FCH263176WA | UCSX-9508-RBLK   | 
| Fan      | Fan Module 1 - Fan 1 | UCSX-9508-FAN    | Cisco Systems Inc | FCH26387AGB | UCSX-9508-FAN    | 
| Fan      | Fan Module 1 - Fan 2 | UCSX-9508-FAN    | Cisco Systems Inc | FCH26387AGB | UCSX-9508-FAN    | 
| Fan      | Fan Module 2 - Fan 1 | UCSX-9508-FAN    | Cisco Systems Inc | FCH263471C2 | UCSX-9508-FAN    | 
| Fan      | Fan Module 2 - Fan 2 | UCSX-9508-FAN    | Cisco Systems Inc | FCH263471C2 | UCSX-9508-FAN    | 
| Fan      | Fan Module 3 - Fan 1 | UCSX-9508-FAN    | Cisco Systems Inc | FCH2634719M | UCSX-9508-FAN    | 
| Fan      | Fan Module 3 - Fan 2 | UCSX-9508-FAN    | Cisco Systems Inc | FCH2634719M | UCSX-9508-FAN    | 
| Fan      | Fan Module 4 - Fan 1 | UCSX-9508-FAN    | Cisco Systems Inc | FCH2634705K | UCSX-9508-FAN    | 
| Fan      | Fan Module 4 - Fan 2 | UCSX-9508-FAN    | Cisco Systems Inc | FCH2634705K | UCSX-9508-FAN    | 
| PSU      | PSU #1               | UCSX-PSU-2800AC  | Cisco Systems Inc | DTM26460266 | UCSX-PSU-2800AC  | 
| PSU      | PSU #2               | UCSX-PSU-2800AC  | Cisco Systems Inc | DTM2646028Y | UCSX-PSU-2800AC  | 
| PSU      | PSU #3               | UCSX-PSU-2800AC  | Cisco Systems Inc | DTM2646028Z | UCSX-PSU-2800AC  | 
| PSU      | PSU #4               | UCSX-PSU-2800AC  | Cisco Systems Inc | DTM264602JB | UCSX-PSU-2800AC  | 
| PSU      | PSU #5               | UCSX-PSU-2800AC  | Cisco Systems Inc | DTM2646028N | UCSX-PSU-2800AC  | 
| PSU      | PSU #6               | UCSX-PSU-2800AC  | Cisco Systems Inc | DTM264602J9 | UCSX-PSU-2800AC  | 
+----------+----------------------+------------------+-------------------+-------------+------------------+
```

Developer

```
# iserver get chassis --name ucsx -v inv

{
    "duration": 18390,
    "isctl": {
        "read": true,
        "calls": 8,
        "success": 8,
        "failed": 0,
        "total_time": 16172
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
        "lines": 10
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 14:33:37.062692	True	2384	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:33:38.982328	True	1910	3	isctl get compute blade --filter "EquipmentChassis/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
2023-12-03 14:33:40.601534	True	1610	2	isctl get equipment iocard --filter "EquipmentChassis/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
2023-12-03 14:33:42.575046	True	1963	2	isctl get equipment expandermodule --filter "EquipmentChassis/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
2023-12-03 14:33:44.926269	True	2340	1	isctl get equipment fancontrol --filter "Parent/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
2023-12-03 14:33:46.980639	True	2035	4	isctl get equipment fanmodule --filter "EquipmentChassis/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
2023-12-03 14:33:48.883594	True	1891	8	isctl get equipment fan --filter "Parent/Moid in ('64be89ab76752d39013f54fc', '64be89ab76752d39013f550b', '64be89ac76752d39013f552c', '64be89ac76752d39013f5544')"  -o json --top 100
2023-12-03 14:33:50.935645	True	2039	6	isctl get equipment psu --filter "Parent/Moid in ('64be876876752d39013ea7f4')"  -o json --top 100
```

[[Back]](./ChassisInventory.md)