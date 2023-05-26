# Get Chassis with Power Information

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --power

Chassis
-------
- Chassis Id    : 1
- Name          : chassis-1
- Model         : UCSB-5108-AC2
- Serial        : FOX2403P669
- Operability   : operable
- Power State   : ok
- Thermal State : ok


+--------------+--------+--------+--------+--------+
| Type         | Now    | Min    | Avg    | Max    |
+--------------+--------+--------+--------+--------+
| Input Power  | 1128.0 | 1104.0 | 1113.6 | 1128.0 | 
| Output Power | 828.0  | 828.0  | 832.6  | 851.0  | 
+--------------+--------+--------+--------+--------+

+-------+------------------+--------+--------+--------+--------------------+------+------+------+
| PSU   | Output Power (W) | Min    | Avg    | Max    | Output Current (A) | Min  | Avg  | Max  |
+-------+------------------+--------+--------+--------+--------------------+------+------+------+
| PSU 1 | 348.23           | 348.23 | 355.44 | 360.24 | 29.0               | 29.0 | 29.6 | 30.0 | 
| PSU 2 | 369.8            | 357.87 | 365.03 | 369.8  | 31.0               | 30.0 | 30.6 | 31.0 | 
| PSU 3 | 0.0              | 0.0    | 0.0    | 0.0    | 0.0                | 0.0  | 0.0  | 0.0  | 
| PSU 4 | 95.43            | 83.5   | 88.27  | 95.43  | 8.0                | 7.0  | 7.4  | 8.0  | 
+-------+------------------+--------+--------+--------+--------------------+------+------+------+
```

JSON Output

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --power

{
    "mo_type": "chassis",
    "dn": "sys/chassis-1",
    "rn": "chassis-1",
    "id": "1",
    "model": "UCSB-5108-AC2",
    "oper_state": "operable",
    "part_number": "68-5091-06",
    "power": "ok",
    "serial": "FOX2403P669",
    "service_state": "in-service",
    "thermal": "ok",
    "vendor": "Cisco Systems Inc",
    "power_stats": {
        "Data": {
            "Chassis": {
                "dn": "sys/chassis-1/stats",
                "time_collected": "2022-12-08T11:01:10.787",
                "chassis_rn": "chassis-1",
                "input_power": 1128.0,
                "output_power": 828.0,
                "input_power_avg": 1113.6,
                "output_power_avg": 832.6,
                "input_power_min": 1104.0,
                "output_power_min": 828.0,
                "input_power_max": 1128.0,
                "output_power_max": 851.0
            },
            "PSU": [
                {
                    "dn": "sys/chassis-1/psu-1/stats",
                    "time_collected": "2022-12-08T11:01:10.786",
                    "chassis_rn": "chassis-1",
                    "psu_rn": "psu-1",
                    "psu_id": "1",
                    "name": "PSU 1",
                    "output_power": 348.23,
                    "output_power_avg": 355.44,
                    "output_power_min": 348.23,
                    "output_power_max": 360.24,
                    "output_current": 29.0,
                    "output_current_avg": 29.6,
                    "output_current_min": 29.0,
                    "output_current_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/psu-2/stats",
                    "time_collected": "2022-12-08T11:01:10.786",
                    "chassis_rn": "chassis-1",
                    "psu_rn": "psu-2",
                    "psu_id": "2",
                    "name": "PSU 2",
                    "output_power": 369.8,
                    "output_power_avg": 365.03,
                    "output_power_min": 357.87,
                    "output_power_max": 369.8,
                    "output_current": 31.0,
                    "output_current_avg": 30.6,
                    "output_current_min": 30.0,
                    "output_current_max": 31.0
                },
                {
                    "dn": "sys/chassis-1/psu-3/stats",
                    "time_collected": "2022-12-08T11:01:10.786",
                    "chassis_rn": "chassis-1",
                    "psu_rn": "psu-3",
                    "psu_id": "3",
                    "name": "PSU 3",
                    "output_power": 0.0,
                    "output_power_avg": 0.0,
                    "output_power_min": 0.0,
                    "output_power_max": 0.0,
                    "output_current": 0.0,
                    "output_current_avg": 0.0,
                    "output_current_min": 0.0,
                    "output_current_max": 0.0
                },
                {
                    "dn": "sys/chassis-1/psu-4/stats",
                    "time_collected": "2022-12-08T11:01:10.786",
                    "chassis_rn": "chassis-1",
                    "psu_rn": "psu-4",
                    "psu_id": "4",
                    "name": "PSU 4",
                    "output_power": 95.43,
                    "output_power_avg": 88.27,
                    "output_power_min": 83.5,
                    "output_power_max": 95.43,
                    "output_current": 8.0,
                    "output_current_avg": 7.4,
                    "output_current_min": 7.0,
                    "output_current_max": 8.0
                }
            ]
        }
    }
}
```

Developer Output

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --power

Developer output

{
    "duration": 3684,
    "isctl": {
        "read": false,
        "calls": 0,
        "success": 0,
        "failed": 0,
        "total_time": 0
    },
    "redfish": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "path": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "path_time": 0,
        "total_time": 0
    },
    "ucsm": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 2146,
        "disconnect_time": 0,
        "mo_time": 1424,
        "total_time": 3570
    },
    "ssh": {
        "read": false,
        "calls": 0,
        "total_time": 0
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
        "read": false,
        "lines": 0
    }
}

Log: ucsm
----------

2022-12-08 11:01:11.780368	True	1685	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 11:01:12.282386	True	499	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 11:01:12.742484	True	457	vip-ucsb1.emea-sp.cisco.com:equipmentChassisStats
2022-12-08 11:01:13.212989	True	468	vip-ucsb1.emea-sp.cisco.com:EquipmentPsuStats
2022-12-08 11:01:13.732901	True	461	disconnect vip-ucsb1.emea-sp.cisco.com
```
