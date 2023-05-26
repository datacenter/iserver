# Get Chassis' with Environmental Information

Environmental = Power + Thermal

```
# iserver get ucsm chassiz --manager milan --env

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

+-----------+----------------------+-------------+------+------+------+
| Chassis   | Fan                  | Speed (RPM) | Min  | Avg  | Max  |
+-----------+----------------------+-------------+------+------+------+
| chassis-1 | Fan Module 1 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| chassis-1 | Fan Module 1 - Fan 2 | 3476        | 3476 | 3475 | 3476 | 
| chassis-1 | Fan Module 2 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| chassis-1 | Fan Module 2 - Fan 2 | 3520        | 3476 | 3512 | 3520 | 
| chassis-1 | Fan Module 3 - Fan 1 | 3344        | 3344 | 3343 | 3344 | 
| chassis-1 | Fan Module 3 - Fan 2 | 3564        | 3564 | 3564 | 3564 | 
| chassis-1 | Fan Module 4 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| chassis-1 | Fan Module 4 - Fan 2 | 3520        | 3520 | 3520 | 3520 | 
| chassis-1 | Fan Module 5 - Fan 1 | 3300        | 3256 | 3293 | 3300 | 
| chassis-1 | Fan Module 5 - Fan 2 | 3520        | 3520 | 3520 | 3520 | 
| chassis-1 | Fan Module 6 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| chassis-1 | Fan Module 6 - Fan 2 | 3476        | 3476 | 3488 | 3520 | 
| chassis-1 | Fan Module 7 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| chassis-1 | Fan Module 7 - Fan 2 | 3476        | 3476 | 3475 | 3476 | 
| chassis-1 | Fan Module 8 - Fan 1 | 3344        | 3300 | 3330 | 3344 | 
| chassis-1 | Fan Module 8 - Fan 2 | 3520        | 3520 | 3520 | 3520 | 
| chassis-2 | Fan Module 1 - Fan 1 | 4576        | 4576 | 4576 | 4576 | 
| chassis-2 | Fan Module 1 - Fan 2 | 4840        | 4840 | 4840 | 4840 | 
| chassis-2 | Fan Module 2 - Fan 1 | 4620        | 4620 | 4620 | 4620 | 
| chassis-2 | Fan Module 2 - Fan 2 | 4928        | 4928 | 4928 | 4928 | 
| chassis-2 | Fan Module 3 - Fan 1 | 4576        | 4576 | 4576 | 4576 | 
| chassis-2 | Fan Module 3 - Fan 2 | 4884        | 4884 | 4884 | 4884 | 
| chassis-2 | Fan Module 4 - Fan 1 | 4620        | 4620 | 4620 | 4620 | 
| chassis-2 | Fan Module 4 - Fan 2 | 4884        | 4884 | 4884 | 4884 | 
| chassis-2 | Fan Module 5 - Fan 1 | 4664        | 4664 | 4664 | 4664 | 
| chassis-2 | Fan Module 5 - Fan 2 | 4928        | 4928 | 4928 | 4928 | 
| chassis-2 | Fan Module 6 - Fan 1 | 4708        | 4708 | 4708 | 4708 | 
| chassis-2 | Fan Module 6 - Fan 2 | 5016        | 5016 | 5016 | 5016 | 
| chassis-2 | Fan Module 7 - Fan 1 | 4664        | 4664 | 4664 | 4664 | 
| chassis-2 | Fan Module 7 - Fan 2 | 4928        | 4928 | 4928 | 4928 | 
| chassis-2 | Fan Module 8 - Fan 1 | 4576        | 4576 | 4589 | 4620 | 
| chassis-2 | Fan Module 8 - Fan 2 | 4928        | 4928 | 4928 | 4928 | 
+-----------+----------------------+-------------+------+------+------+

+-----------+-----------------------+-----------------+------+-------+------+
| Chassis   | Sensor                | Temperature (C) | Min  | Avg   | Max  |
+-----------+-----------------------+-----------------+------+-------+------+
| chassis-1 | Fan Module 1          | 34.0            | 33.0 | 33.29 | 34.0 | 
| chassis-1 | Fan Module 2          | 33.0            | 33.0 | 33.0  | 33.0 | 
| chassis-1 | Fan Module 3          | 35.0            | 35.0 | 35.0  | 35.0 | 
| chassis-1 | Fan Module 4          | 32.0            | 32.0 | 32.0  | 32.0 | 
| chassis-1 | Fan Module 5          | 29.0            | 29.0 | 29.0  | 29.0 | 
| chassis-1 | Fan Module 6          | 28.0            | 28.0 | 28.0  | 28.0 | 
| chassis-1 | Fan Module 7          | 31.0            | 31.0 | 31.0  | 31.0 | 
| chassis-1 | Fan Module 8          | 29.0            | 29.0 | 29.0  | 29.0 | 
| chassis-1 | PSU 1                 | 25.0            | 24.0 | 24.29 | 25.0 | 
| chassis-1 | PSU 2                 | 25.0            | 25.0 | 25.0  | 25.0 | 
| chassis-1 | PSU 3                 | 24.0            | 24.0 | 24.71 | 25.0 | 
| chassis-1 | PSU 4                 | 23.0            | 23.0 | 23.0  | 23.0 | 
| chassis-1 | IO Module 1 - Ambient | 42.0            | 42.0 | 42.0  | 42.0 | 
| chassis-1 | IO Module 2 - Ambient | 45.0            | 45.0 | 45.0  | 45.0 | 
| chassis-1 | IO Module 1 - ASIC    | 64.0            | 64.0 | 64.0  | 64.0 | 
| chassis-1 | IO Module 2 - ASIC    | 66.0            | 65.0 | 65.47 | 66.0 | 
| chassis-2 | Fan Module 1          | 31.0            | 31.0 | 31.0  | 31.0 | 
| chassis-2 | Fan Module 2          | 32.0            | 32.0 | 32.0  | 32.0 | 
| chassis-2 | Fan Module 3          | 30.0            | 30.0 | 30.0  | 30.0 | 
| chassis-2 | Fan Module 4          | 29.0            | 29.0 | 29.0  | 29.0 | 
| chassis-2 | Fan Module 5          | 29.0            | 29.0 | 29.0  | 29.0 | 
| chassis-2 | Fan Module 6          | 29.0            | 29.0 | 29.0  | 29.0 | 
| chassis-2 | Fan Module 7          | 27.0            | 27.0 | 27.0  | 27.0 | 
| chassis-2 | Fan Module 8          | 26.0            | 26.0 | 26.33 | 27.0 | 
| chassis-2 | PSU 1                 | 20.0            | 20.0 | 20.0  | 20.0 | 
| chassis-2 | PSU 2                 | 20.0            | 19.0 | 19.17 | 20.0 | 
| chassis-2 | PSU 3                 | 20.0            | 20.0 | 20.0  | 20.0 | 
| chassis-2 | PSU 4                 | 22.0            | 21.0 | 21.17 | 22.0 | 
| chassis-2 | IO Module 1 - Ambient | 39.0            | 39.0 | 39.0  | 39.0 | 
| chassis-2 | IO Module 2 - Ambient | 37.0            | 37.0 | 37.0  | 37.0 | 
| chassis-2 | IO Module 1 - ASIC    | 54.0            | 53.0 | 53.8  | 54.0 | 
| chassis-2 | IO Module 2 - ASIC    | 50.0            | 50.0 | 50.15 | 51.0 | 
+-----------+-----------------------+-----------------+------+-------+------+
```

JSON Output

```
# iserver get ucsm chassiz --manager milan --env

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
        },
        "thermal_stats": {
            "Data": {
                "Fan": [
                    {
                        "dn": "sys/chassis-1/fan-module-1-1/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:10.938",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-1",
                        "fan_module_id": "1",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 1 - Fan 1",
                        "speed": "3256",
                        "speed_avg": "3256",
                        "speed_min": "3256",
                        "speed_max": "3256"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-1/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:10.938",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-1",
                        "fan_module_id": "1",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 1 - Fan 2",
                        "speed": "3476",
                        "speed_avg": "3475",
                        "speed_min": "3476",
                        "speed_max": "3476"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-2/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:10.938",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-2",
                        "fan_module_id": "2",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 2 - Fan 1",
                        "speed": "3256",
                        "speed_avg": "3256",
                        "speed_min": "3256",
                        "speed_max": "3256"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-2/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:10.938",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-2",
                        "fan_module_id": "2",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 2 - Fan 2",
                        "speed": "3520",
                        "speed_avg": "3512",
                        "speed_min": "3476",
                        "speed_max": "3520"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-3/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:10.938",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-3",
                        "fan_module_id": "3",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 3 - Fan 1",
                        "speed": "3344",
                        "speed_avg": "3343",
                        "speed_min": "3344",
                        "speed_max": "3344"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-3/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:10.938",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-3",
                        "fan_module_id": "3",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 3 - Fan 2",
                        "speed": "3564",
                        "speed_avg": "3564",
                        "speed_min": "3564",
                        "speed_max": "3564"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-4/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:10.938",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-4",
                        "fan_module_id": "4",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 4 - Fan 1",
                        "speed": "3256",
                        "speed_avg": "3256",
                        "speed_min": "3256",
                        "speed_max": "3256"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-4/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:10.939",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-4",
                        "fan_module_id": "4",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 4 - Fan 2",
                        "speed": "3520",
                        "speed_avg": "3520",
                        "speed_min": "3520",
                        "speed_max": "3520"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-5/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:10.939",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-5",
                        "fan_module_id": "5",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 5 - Fan 1",
                        "speed": "3300",
                        "speed_avg": "3293",
                        "speed_min": "3256",
                        "speed_max": "3300"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-5/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:10.939",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-5",
                        "fan_module_id": "5",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 5 - Fan 2",
                        "speed": "3520",
                        "speed_avg": "3520",
                        "speed_min": "3520",
                        "speed_max": "3520"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-6/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:10.939",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-6",
                        "fan_module_id": "6",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 6 - Fan 1",
                        "speed": "3256",
                        "speed_avg": "3256",
                        "speed_min": "3256",
                        "speed_max": "3256"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-6/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:10.939",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-6",
                        "fan_module_id": "6",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 6 - Fan 2",
                        "speed": "3476",
                        "speed_avg": "3488",
                        "speed_min": "3476",
                        "speed_max": "3520"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-7/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:10.939",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-7",
                        "fan_module_id": "7",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 7 - Fan 1",
                        "speed": "3256",
                        "speed_avg": "3256",
                        "speed_min": "3256",
                        "speed_max": "3256"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-7/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:10.939",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-7",
                        "fan_module_id": "7",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 7 - Fan 2",
                        "speed": "3476",
                        "speed_avg": "3475",
                        "speed_min": "3476",
                        "speed_max": "3476"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-8/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:10.939",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-8",
                        "fan_module_id": "8",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 8 - Fan 1",
                        "speed": "3344",
                        "speed_avg": "3330",
                        "speed_min": "3300",
                        "speed_max": "3344"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-8/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:10.939",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-8",
                        "fan_module_id": "8",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 8 - Fan 2",
                        "speed": "3520",
                        "speed_avg": "3520",
                        "speed_min": "3520",
                        "speed_max": "3520"
                    }
                ],
                "Temperature": [
                    {
                        "dn": "sys/chassis-1/fan-module-1-1/stats",
                        "time_collected": "2022-12-08T11:03:10.936",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-1",
                        "fan_module_id": "1",
                        "name": "Fan Module 1",
                        "temperature": 34.0,
                        "temperature_avg": 33.29,
                        "temperature_min": 33.0,
                        "temperature_max": 34.0
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-2/stats",
                        "time_collected": "2022-12-08T11:03:10.936",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-2",
                        "fan_module_id": "2",
                        "name": "Fan Module 2",
                        "temperature": 33.0,
                        "temperature_avg": 33.0,
                        "temperature_min": 33.0,
                        "temperature_max": 33.0
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-3/stats",
                        "time_collected": "2022-12-08T11:03:10.936",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-3",
                        "fan_module_id": "3",
                        "name": "Fan Module 3",
                        "temperature": 35.0,
                        "temperature_avg": 35.0,
                        "temperature_min": 35.0,
                        "temperature_max": 35.0
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-4/stats",
                        "time_collected": "2022-12-08T11:03:10.936",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-4",
                        "fan_module_id": "4",
                        "name": "Fan Module 4",
                        "temperature": 32.0,
                        "temperature_avg": 32.0,
                        "temperature_min": 32.0,
                        "temperature_max": 32.0
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-5/stats",
                        "time_collected": "2022-12-08T11:03:10.936",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-5",
                        "fan_module_id": "5",
                        "name": "Fan Module 5",
                        "temperature": 29.0,
                        "temperature_avg": 29.0,
                        "temperature_min": 29.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-6/stats",
                        "time_collected": "2022-12-08T11:03:10.936",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-6",
                        "fan_module_id": "6",
                        "name": "Fan Module 6",
                        "temperature": 28.0,
                        "temperature_avg": 28.0,
                        "temperature_min": 28.0,
                        "temperature_max": 28.0
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-7/stats",
                        "time_collected": "2022-12-08T11:03:10.936",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-7",
                        "fan_module_id": "7",
                        "name": "Fan Module 7",
                        "temperature": 31.0,
                        "temperature_avg": 31.0,
                        "temperature_min": 31.0,
                        "temperature_max": 31.0
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-8/stats",
                        "time_collected": "2022-12-08T11:03:10.936",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-8",
                        "fan_module_id": "8",
                        "name": "Fan Module 8",
                        "temperature": 29.0,
                        "temperature_avg": 29.0,
                        "temperature_min": 29.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-1/psu-1/stats",
                        "time_collected": "2022-12-08T11:03:10.937",
                        "chassis_rn": "chassis-1",
                        "psu_rn": "psu-1",
                        "psu_id": "1",
                        "name": "PSU 1",
                        "temperature": 25.0,
                        "temperature_avg": 24.29,
                        "temperature_min": 24.0,
                        "temperature_max": 25.0
                    },
                    {
                        "dn": "sys/chassis-1/psu-2/stats",
                        "time_collected": "2022-12-08T11:03:10.937",
                        "chassis_rn": "chassis-1",
                        "psu_rn": "psu-2",
                        "psu_id": "2",
                        "name": "PSU 2",
                        "temperature": 25.0,
                        "temperature_avg": 25.0,
                        "temperature_min": 25.0,
                        "temperature_max": 25.0
                    },
                    {
                        "dn": "sys/chassis-1/psu-3/stats",
                        "time_collected": "2022-12-08T11:03:10.937",
                        "chassis_rn": "chassis-1",
                        "psu_rn": "psu-3",
                        "psu_id": "3",
                        "name": "PSU 3",
                        "temperature": 24.0,
                        "temperature_avg": 24.71,
                        "temperature_min": 24.0,
                        "temperature_max": 25.0
                    },
                    {
                        "dn": "sys/chassis-1/psu-4/stats",
                        "time_collected": "2022-12-08T11:03:10.937",
                        "chassis_rn": "chassis-1",
                        "psu_rn": "psu-4",
                        "psu_id": "4",
                        "name": "PSU 4",
                        "temperature": 23.0,
                        "temperature_avg": 23.0,
                        "temperature_min": 23.0,
                        "temperature_max": 23.0
                    },
                    {
                        "dn": "sys/chassis-1/slot-1/stats",
                        "time_collected": "2022-12-08T11:03:03.186",
                        "chassis_rn": "chassis-1",
                        "slot_rn": "slot-1",
                        "slot_id": "1",
                        "name": "IO Module 1 - Ambient",
                        "temperature": 42.0,
                        "temperature_avg": 42.0,
                        "temperature_min": 42.0,
                        "temperature_max": 42.0
                    },
                    {
                        "dn": "sys/chassis-1/slot-2/stats",
                        "time_collected": "2022-12-08T11:03:10.937",
                        "chassis_rn": "chassis-1",
                        "slot_rn": "slot-2",
                        "slot_id": "2",
                        "name": "IO Module 2 - Ambient",
                        "temperature": 45.0,
                        "temperature_avg": 45.0,
                        "temperature_min": 45.0,
                        "temperature_max": 45.0
                    },
                    {
                        "dn": "sys/chassis-1/slot-1/stats",
                        "time_collected": "2022-12-08T11:03:03.186",
                        "chassis_rn": "chassis-1",
                        "slot_rn": "slot-1",
                        "slot_id": "1",
                        "name": "IO Module 1 - ASIC",
                        "temperature": 64.0,
                        "temperature_avg": 64.0,
                        "temperature_min": 64.0,
                        "temperature_max": 64.0
                    },
                    {
                        "dn": "sys/chassis-1/slot-2/stats",
                        "time_collected": "2022-12-08T11:03:10.937",
                        "chassis_rn": "chassis-1",
                        "slot_rn": "slot-2",
                        "slot_id": "2",
                        "name": "IO Module 2 - ASIC",
                        "temperature": 66.0,
                        "temperature_avg": 65.47,
                        "temperature_min": 65.0,
                        "temperature_max": 66.0
                    }
                ]
            },
            "Summary": {
                "Source": "UCSM",
                "HighestTemperature": 66.0
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
        },
        "thermal_stats": {
            "Data": {
                "Fan": [
                    {
                        "dn": "sys/chassis-2/fan-module-1-1/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-1",
                        "fan_module_id": "1",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 1 - Fan 1",
                        "speed": "4576",
                        "speed_avg": "4576",
                        "speed_min": "4576",
                        "speed_max": "4576"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-1/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-1",
                        "fan_module_id": "1",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 1 - Fan 2",
                        "speed": "4840",
                        "speed_avg": "4840",
                        "speed_min": "4840",
                        "speed_max": "4840"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-2/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-2",
                        "fan_module_id": "2",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 2 - Fan 1",
                        "speed": "4620",
                        "speed_avg": "4620",
                        "speed_min": "4620",
                        "speed_max": "4620"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-2/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-2",
                        "fan_module_id": "2",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 2 - Fan 2",
                        "speed": "4928",
                        "speed_avg": "4928",
                        "speed_min": "4928",
                        "speed_max": "4928"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-3/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-3",
                        "fan_module_id": "3",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 3 - Fan 1",
                        "speed": "4576",
                        "speed_avg": "4576",
                        "speed_min": "4576",
                        "speed_max": "4576"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-3/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-3",
                        "fan_module_id": "3",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 3 - Fan 2",
                        "speed": "4884",
                        "speed_avg": "4884",
                        "speed_min": "4884",
                        "speed_max": "4884"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-4/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-4",
                        "fan_module_id": "4",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 4 - Fan 1",
                        "speed": "4620",
                        "speed_avg": "4620",
                        "speed_min": "4620",
                        "speed_max": "4620"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-4/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-4",
                        "fan_module_id": "4",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 4 - Fan 2",
                        "speed": "4884",
                        "speed_avg": "4884",
                        "speed_min": "4884",
                        "speed_max": "4884"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-5/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-5",
                        "fan_module_id": "5",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 5 - Fan 1",
                        "speed": "4664",
                        "speed_avg": "4664",
                        "speed_min": "4664",
                        "speed_max": "4664"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-5/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-5",
                        "fan_module_id": "5",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 5 - Fan 2",
                        "speed": "4928",
                        "speed_avg": "4928",
                        "speed_min": "4928",
                        "speed_max": "4928"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-6/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-6",
                        "fan_module_id": "6",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 6 - Fan 1",
                        "speed": "4708",
                        "speed_avg": "4708",
                        "speed_min": "4708",
                        "speed_max": "4708"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-6/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-6",
                        "fan_module_id": "6",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 6 - Fan 2",
                        "speed": "5016",
                        "speed_avg": "5016",
                        "speed_min": "5016",
                        "speed_max": "5016"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-7/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-7",
                        "fan_module_id": "7",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 7 - Fan 1",
                        "speed": "4664",
                        "speed_avg": "4664",
                        "speed_min": "4664",
                        "speed_max": "4664"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-7/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-7",
                        "fan_module_id": "7",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 7 - Fan 2",
                        "speed": "4928",
                        "speed_avg": "4928",
                        "speed_min": "4928",
                        "speed_max": "4928"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-8/fan-1/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-8",
                        "fan_module_id": "8",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 8 - Fan 1",
                        "speed": "4576",
                        "speed_avg": "4589",
                        "speed_min": "4576",
                        "speed_max": "4620"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-8/fan-2/stats",
                        "time_collected": "2022-12-08T11:03:16.347",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-8",
                        "fan_module_id": "8",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 8 - Fan 2",
                        "speed": "4928",
                        "speed_avg": "4928",
                        "speed_min": "4928",
                        "speed_max": "4928"
                    }
                ],
                "Temperature": [
                    {
                        "dn": "sys/chassis-2/fan-module-1-1/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-1",
                        "fan_module_id": "1",
                        "name": "Fan Module 1",
                        "temperature": 31.0,
                        "temperature_avg": 31.0,
                        "temperature_min": 31.0,
                        "temperature_max": 31.0
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-2/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-2",
                        "fan_module_id": "2",
                        "name": "Fan Module 2",
                        "temperature": 32.0,
                        "temperature_avg": 32.0,
                        "temperature_min": 32.0,
                        "temperature_max": 32.0
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-3/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-3",
                        "fan_module_id": "3",
                        "name": "Fan Module 3",
                        "temperature": 30.0,
                        "temperature_avg": 30.0,
                        "temperature_min": 30.0,
                        "temperature_max": 30.0
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-4/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-4",
                        "fan_module_id": "4",
                        "name": "Fan Module 4",
                        "temperature": 29.0,
                        "temperature_avg": 29.0,
                        "temperature_min": 29.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-5/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-5",
                        "fan_module_id": "5",
                        "name": "Fan Module 5",
                        "temperature": 29.0,
                        "temperature_avg": 29.0,
                        "temperature_min": 29.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-6/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-6",
                        "fan_module_id": "6",
                        "name": "Fan Module 6",
                        "temperature": 29.0,
                        "temperature_avg": 29.0,
                        "temperature_min": 29.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-7/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-7",
                        "fan_module_id": "7",
                        "name": "Fan Module 7",
                        "temperature": 27.0,
                        "temperature_avg": 27.0,
                        "temperature_min": 27.0,
                        "temperature_max": 27.0
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-8/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-8",
                        "fan_module_id": "8",
                        "name": "Fan Module 8",
                        "temperature": 26.0,
                        "temperature_avg": 26.33,
                        "temperature_min": 26.0,
                        "temperature_max": 27.0
                    },
                    {
                        "dn": "sys/chassis-2/psu-1/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "psu_rn": "psu-1",
                        "psu_id": "1",
                        "name": "PSU 1",
                        "temperature": 20.0,
                        "temperature_avg": 20.0,
                        "temperature_min": 20.0,
                        "temperature_max": 20.0
                    },
                    {
                        "dn": "sys/chassis-2/psu-2/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "psu_rn": "psu-2",
                        "psu_id": "2",
                        "name": "PSU 2",
                        "temperature": 20.0,
                        "temperature_avg": 19.17,
                        "temperature_min": 19.0,
                        "temperature_max": 20.0
                    },
                    {
                        "dn": "sys/chassis-2/psu-3/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "psu_rn": "psu-3",
                        "psu_id": "3",
                        "name": "PSU 3",
                        "temperature": 20.0,
                        "temperature_avg": 20.0,
                        "temperature_min": 20.0,
                        "temperature_max": 20.0
                    },
                    {
                        "dn": "sys/chassis-2/psu-4/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "psu_rn": "psu-4",
                        "psu_id": "4",
                        "name": "PSU 4",
                        "temperature": 22.0,
                        "temperature_avg": 21.17,
                        "temperature_min": 21.0,
                        "temperature_max": 22.0
                    },
                    {
                        "dn": "sys/chassis-2/slot-1/stats",
                        "time_collected": "2022-12-08T11:03:52.254",
                        "chassis_rn": "chassis-2",
                        "slot_rn": "slot-1",
                        "slot_id": "1",
                        "name": "IO Module 1 - Ambient",
                        "temperature": 39.0,
                        "temperature_avg": 39.0,
                        "temperature_min": 39.0,
                        "temperature_max": 39.0
                    },
                    {
                        "dn": "sys/chassis-2/slot-2/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "slot_rn": "slot-2",
                        "slot_id": "2",
                        "name": "IO Module 2 - Ambient",
                        "temperature": 37.0,
                        "temperature_avg": 37.0,
                        "temperature_min": 37.0,
                        "temperature_max": 37.0
                    },
                    {
                        "dn": "sys/chassis-2/slot-1/stats",
                        "time_collected": "2022-12-08T11:03:52.254",
                        "chassis_rn": "chassis-2",
                        "slot_rn": "slot-1",
                        "slot_id": "1",
                        "name": "IO Module 1 - ASIC",
                        "temperature": 54.0,
                        "temperature_avg": 53.8,
                        "temperature_min": 53.0,
                        "temperature_max": 54.0
                    },
                    {
                        "dn": "sys/chassis-2/slot-2/stats",
                        "time_collected": "2022-12-08T11:03:16.346",
                        "chassis_rn": "chassis-2",
                        "slot_rn": "slot-2",
                        "slot_id": "2",
                        "name": "IO Module 2 - ASIC",
                        "temperature": 50.0,
                        "temperature_avg": 50.15,
                        "temperature_min": 50.0,
                        "temperature_max": 51.0
                    }
                ]
            },
            "Summary": {
                "Source": "UCSM",
                "HighestTemperature": 54.0
            }
        }
    }
]
```

Developer Output

```
# iserver get ucsm chassiz --manager milan --env

Developer output

{
    "duration": 5100,
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
        "success": 8,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 2030,
        "disconnect_time": 0,
        "mo_time": 2772,
        "total_time": 4802
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

2022-12-08 11:03:50.248008	True	1587	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 11:03:50.739047	True	490	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 11:03:51.174259	True	433	vip-ucsb1.emea-sp.cisco.com:equipmentChassisStats
2022-12-08 11:03:51.645803	True	469	vip-ucsb1.emea-sp.cisco.com:EquipmentPsuStats
2022-12-08 11:03:52.136145	True	489	vip-ucsb1.emea-sp.cisco.com:EquipmentFanStats
2022-12-08 11:03:52.578411	True	440	vip-ucsb1.emea-sp.cisco.com:EquipmentFanModuleStats
2022-12-08 11:03:53.031266	True	451	vip-ucsb1.emea-sp.cisco.com:EquipmentIOCardStats
2022-12-08 11:03:53.722537	True	443	disconnect vip-ucsb1.emea-sp.cisco.com
```
