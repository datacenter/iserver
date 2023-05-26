# Get Chassis' with Power Information

```
# iserver get ucsm chassiz --manager milan --power

+------------+-----------+---------------+-------------+-------------+-------------+---------------+
| Chassis Id | Name      | Model         | Serial      | Operability | Power State | Thermal State |
+------------+-----------+---------------+-------------+-------------+-------------+---------------+
| 1          | chassis-1 | UCSB-5108-AC2 | FOX2403P669 | operable    | ok          | ok            | 
| 2          | chassis-2 | UCSB-5108-AC2 | FOX2403P2Z9 | operable    | ok          | ok            | 
+------------+-----------+---------------+-------------+-------------+-------------+---------------+

+-----------+-----------------+--------+---------+--------+------------------+--------+---------+--------+
| Chassis   | Input Power Now | Min    | Avg     | Max    | Output Power Now | Min    | Avg     | Max    |
+-----------+-----------------+--------+---------+--------+------------------+--------+---------+--------+
| chassis-1 | 1152.0          | 1104.0 | 1121.14 | 1152.0 | 897.0            | 828.0  | 847.71  | 897.0  | 
| chassis-2 | 1440.0          | 1416.0 | 1444.0  | 1488.0 | 1150.0           | 1058.0 | 1199.83 | 1288.0 | 
+-----------+-----------------+--------+---------+--------+------------------+--------+---------+--------+

+-----------+-------+------------------+--------+--------+--------+--------------------+------+-------+------+
| Chassis   | PSU   | Output Power (W) | Min    | Avg    | Max    | Output Current (A) | Min  | Avg   | Max  |
+-----------+-------+------------------+--------+--------+--------+--------------------+------+-------+------+
| chassis-1 | PSU 1 | 360.24           | 348.23 | 356.81 | 360.24 | 30.0               | 29.0 | 29.71 | 30.0 | 
| chassis-1 | PSU 2 | 381.73           | 357.87 | 369.8  | 381.73 | 32.0               | 30.0 | 31.0  | 32.0 | 
| chassis-1 | PSU 3 | 0.0              | 0.0    | 0.0    | 0.0    | 0.0                | 0.0  | 0.0   | 0.0  | 
| chassis-1 | PSU 4 | 131.22           | 83.5   | 95.43  | 131.22 | 11.0               | 7.0  | 8.0   | 11.0 | 
| chassis-2 | PSU 1 | 264.18           | 226.65 | 263.66 | 324.22 | 22.0               | 19.0 | 22.0  | 27.0 | 
| chassis-2 | PSU 2 | 312.21           | 312.21 | 322.21 | 336.22 | 26.0               | 26.0 | 26.83 | 28.0 | 
| chassis-2 | PSU 3 | 343.65           | 248.85 | 389.08 | 462.15 | 29.0               | 21.0 | 32.83 | 39.0 | 
| chassis-2 | PSU 4 | 228.15           | 202.79 | 223.18 | 238.58 | 19.0               | 17.0 | 18.67 | 20.0 | 
+-----------+-------+------------------+--------+--------+--------+--------------------+------+-------+------+
```

JSON Output

```
# iserver get ucsm chassiz --manager milan --power

[
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
                    "time_collected": "2022-12-08T11:03:10.938",
                    "chassis_rn": "chassis-1",
                    "input_power": 1152.0,
                    "output_power": 897.0,
                    "input_power_avg": 1121.14,
                    "output_power_avg": 847.71,
                    "input_power_min": 1104.0,
                    "output_power_min": 828.0,
                    "input_power_max": 1152.0,
                    "output_power_max": 897.0
                },
                "PSU": [
                    {
                        "dn": "sys/chassis-1/psu-1/stats",
                        "time_collected": "2022-12-08T11:03:10.937",
                        "chassis_rn": "chassis-1",
                        "psu_rn": "psu-1",
                        "psu_id": "1",
                        "name": "PSU 1",
                        "output_power": 360.24,
                        "output_power_avg": 356.81,
                        "output_power_min": 348.23,
                        "output_power_max": 360.24,
                        "output_current": 30.0,
                        "output_current_avg": 29.71,
                        "output_current_min": 29.0,
                        "output_current_max": 30.0
                    },
                    {
                        "dn": "sys/chassis-1/psu-2/stats",
                        "time_collected": "2022-12-08T11:03:10.937",
                        "chassis_rn": "chassis-1",
                        "psu_rn": "psu-2",
                        "psu_id": "2",
                        "name": "PSU 2",
                        "output_power": 381.73,
                        "output_power_avg": 369.8,
                        "output_power_min": 357.87,
                        "output_power_max": 381.73,
                        "output_current": 32.0,
                        "output_current_avg": 31.0,
                        "output_current_min": 30.0,
                        "output_current_max": 32.0
                    },
                    {
                        "dn": "sys/chassis-1/psu-3/stats",
                        "time_collected": "2022-12-08T11:03:10.937",
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
                        "time_collected": "2022-12-08T11:03:10.937",
                        "chassis_rn": "chassis-1",
                        "psu_rn": "psu-4",
                        "psu_id": "4",
                        "name": "PSU 4",
                        "output_power": 131.22,
                        "output_power_avg": 95.43,
                        "output_power_min": 83.5,
                        "output_power_max": 131.22,
                        "output_current": 11.0,
                        "output_current_avg": 8.0,
                        "output_current_min": 7.0,
                        "output_current_max": 11.0
                    }
                ]
            }
        }
    },
    {
        "mo_type": "chassis",
        "dn": "sys/chassis-2",
        "rn": "chassis-2",
        "id": "2",
        "model": "UCSB-5108-AC2",
        "oper_state": "operable",
        "part_number": "68-5091-06",
        "power": "ok",
        "serial": "FOX2403P2Z9",
        "service_state": "in-service",
        "thermal": "ok",
        "vendor": "Cisco Systems Inc",
        "power_stats": {
            "Data": {
                "Chassis": {
                    "dn": "sys/chassis-2/stats",
                    "time_collected": "2022-12-08T11:03:16.347",
                    "chassis_rn": "chassis-2",
                    "input_power": 1440.0,
                    "output_power": 1150.0,
                    "input_power_avg": 1444.0,
                    "output_power_avg": 1199.83,
                    "input_power_min": 1416.0,
                    "output_power_min": 1058.0,
                    "input_power_max": 1488.0,
                    "output_power_max": 1288.0
                },
                "PSU": [
                    {
                        "dn": "sys/chassis-2/psu-1/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "psu_rn": "psu-1",
                        "psu_id": "1",
                        "name": "PSU 1",
                        "output_power": 264.18,
                        "output_power_avg": 263.66,
                        "output_power_min": 226.65,
                        "output_power_max": 324.22,
                        "output_current": 22.0,
                        "output_current_avg": 22.0,
                        "output_current_min": 19.0,
                        "output_current_max": 27.0
                    },
                    {
                        "dn": "sys/chassis-2/psu-2/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "psu_rn": "psu-2",
                        "psu_id": "2",
                        "name": "PSU 2",
                        "output_power": 312.21,
                        "output_power_avg": 322.21,
                        "output_power_min": 312.21,
                        "output_power_max": 336.22,
                        "output_current": 26.0,
                        "output_current_avg": 26.83,
                        "output_current_min": 26.0,
                        "output_current_max": 28.0
                    },
                    {
                        "dn": "sys/chassis-2/psu-3/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "psu_rn": "psu-3",
                        "psu_id": "3",
                        "name": "PSU 3",
                        "output_power": 343.65,
                        "output_power_avg": 389.08,
                        "output_power_min": 248.85,
                        "output_power_max": 462.15,
                        "output_current": 29.0,
                        "output_current_avg": 32.83,
                        "output_current_min": 21.0,
                        "output_current_max": 39.0
                    },
                    {
                        "dn": "sys/chassis-2/psu-4/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "psu_rn": "psu-4",
                        "psu_id": "4",
                        "name": "PSU 4",
                        "output_power": 228.15,
                        "output_power_avg": 223.18,
                        "output_power_min": 202.79,
                        "output_power_max": 238.58,
                        "output_current": 19.0,
                        "output_current_avg": 18.67,
                        "output_current_min": 17.0,
                        "output_current_max": 20.0
                    }
                ]
            }
        }
    }
]
```

Developer Output

```
# iserver get ucsm chassiz --manager milan --power

Developer output

{
    "duration": 4165,
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
        "connect_time": 2242,
        "disconnect_time": 0,
        "mo_time": 1678,
        "total_time": 3920
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

2022-12-08 11:03:17.358919	True	1764	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 11:03:18.086939	True	719	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 11:03:18.544892	True	453	vip-ucsb1.emea-sp.cisco.com:equipmentChassisStats
2022-12-08 11:03:19.053470	True	506	vip-ucsb1.emea-sp.cisco.com:EquipmentPsuStats
2022-12-08 11:03:19.642776	True	478	disconnect vip-ucsb1.emea-sp.cisco.com
```
