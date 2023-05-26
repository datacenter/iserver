# Get Chassis and Blades with Environmental Information

Environmental = Power + Thermal

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --blade --env

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
| Input Power  | 1128.0 | 1104.0 | 1116.0 | 1128.0 | 
| Output Power | 874.0  | 828.0  | 839.5  | 874.0  | 
+--------------+--------+--------+--------+--------+

+-------+------------------+--------+--------+--------+--------------------+------+-------+------+
| PSU   | Output Power (W) | Min    | Avg    | Max    | Output Current (A) | Min  | Avg   | Max  |
+-------+------------------+--------+--------+--------+--------------------+------+-------+------+
| PSU 1 | 360.24           | 348.23 | 356.24 | 360.24 | 30.0               | 29.0 | 29.67 | 30.0 | 
| PSU 2 | 381.73           | 357.87 | 367.81 | 381.73 | 32.0               | 30.0 | 30.83 | 32.0 | 
| PSU 3 | 0.0              | 0.0    | 0.0    | 0.0    | 0.0                | 0.0  | 0.0   | 0.0  | 
| PSU 4 | 95.43            | 83.5   | 89.47  | 95.43  | 8.0                | 7.0  | 7.5   | 8.0  | 
+-------+------------------+--------+--------+--------+--------------------+------+-------+------+

+----------------------+-------------+------+------+------+
| Fan                  | Speed (RPM) | Min  | Avg  | Max  |
+----------------------+-------------+------+------+------+
| Fan Module 1 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| Fan Module 1 - Fan 2 | 3476        | 3476 | 3475 | 3476 | 
| Fan Module 2 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| Fan Module 2 - Fan 2 | 3520        | 3476 | 3511 | 3520 | 
| Fan Module 3 - Fan 1 | 3344        | 3344 | 3343 | 3344 | 
| Fan Module 3 - Fan 2 | 3564        | 3564 | 3564 | 3564 | 
| Fan Module 4 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| Fan Module 4 - Fan 2 | 3520        | 3520 | 3520 | 3520 | 
| Fan Module 5 - Fan 1 | 3256        | 3256 | 3292 | 3300 | 
| Fan Module 5 - Fan 2 | 3520        | 3520 | 3520 | 3520 | 
| Fan Module 6 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| Fan Module 6 - Fan 2 | 3520        | 3476 | 3490 | 3520 | 
| Fan Module 7 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| Fan Module 7 - Fan 2 | 3476        | 3476 | 3475 | 3476 | 
| Fan Module 8 - Fan 1 | 3344        | 3300 | 3328 | 3344 | 
| Fan Module 8 - Fan 2 | 3520        | 3520 | 3520 | 3520 | 
+----------------------+-------------+------+------+------+

+-----------------------+-----------------+------+-------+------+
| Sensor                | Temperature (C) | Min  | Avg   | Max  |
+-----------------------+-----------------+------+-------+------+
| Fan Module 1          | 33.0            | 33.0 | 33.17 | 34.0 | 
| Fan Module 2          | 33.0            | 33.0 | 33.0  | 33.0 | 
| Fan Module 3          | 35.0            | 35.0 | 35.0  | 35.0 | 
| Fan Module 4          | 32.0            | 32.0 | 32.0  | 32.0 | 
| Fan Module 5          | 29.0            | 29.0 | 29.0  | 29.0 | 
| Fan Module 6          | 28.0            | 28.0 | 28.0  | 28.0 | 
| Fan Module 7          | 31.0            | 31.0 | 31.0  | 31.0 | 
| Fan Module 8          | 29.0            | 29.0 | 29.0  | 29.0 | 
| PSU 1                 | 25.0            | 24.0 | 24.17 | 25.0 | 
| PSU 2                 | 25.0            | 25.0 | 25.0  | 25.0 | 
| PSU 3                 | 24.0            | 24.0 | 24.83 | 25.0 | 
| PSU 4                 | 23.0            | 23.0 | 23.0  | 23.0 | 
| IO Module 1 - Ambient | 42.0            | 42.0 | 42.0  | 42.0 | 
| IO Module 2 - Ambient | 45.0            | 45.0 | 45.0  | 45.0 | 
| IO Module 1 - ASIC    | 64.0            | 64.0 | 64.0  | 64.0 | 
| IO Module 2 - ASIC    | 65.0            | 65.0 | 65.38 | 66.0 | 
+-----------------------+-----------------+------+-------+------+

+---------+--------------+-------------+---------------+-------------+-------------+-------------+
| Blade   | Model        | Serial      | Overal Status | Operability | Power State | Assoc State |
+---------+--------------+-------------+---------------+-------------+-------------+-------------+
| blade-1 | UCSB-B200-M4 | FCH205371PZ | ok            | operable    | on          | associated  | 
| blade-2 | UCSB-B200-M4 | FCH20527XXD | ok            | operable    | on          | associated  | 
| blade-3 | UCSB-B200-M4 | FCH20437VXH | ok            | operable    | on          | associated  | 
| blade-4 | UCSB-B200-M4 | FCH205371UU | ok            | operable    | on          | associated  | 
+---------+--------------+-------------+---------------+-------------+-------------+-------------+

+-----------+---------+-------+-------+-------+-------+---------+-------+-------+-------+---------+-------+-------+-------+
| Chassis   | Name    | Power | Min   | Avg   | Max   | Current | Min   | Avg   | Max   | Voltage | Min   | Avg   | Max   |
+-----------+---------+-------+-------+-------+-------+---------+-------+-------+-------+---------+-------+-------+-------+
| chassis-1 | blade-1 | 138.0 | 138.0 | 138.0 | 138.0 | 11.47   | 11.47 | 11.47 | 11.47 | 12.04   | 12.04 | 12.04 | 12.04 | 
| chassis-1 | blade-2 | 138.0 | 138.0 | 138.0 | 138.0 | 11.52   | 11.52 | 11.52 | 11.52 | 11.98   | 11.98 | 11.98 | 11.98 | 
| chassis-1 | blade-3 | 126.0 | 126.0 | 126.0 | 126.0 | 10.52   | 10.52 | 10.52 | 10.52 | 11.98   | 11.98 | 11.98 | 11.98 | 
| chassis-1 | blade-4 | 126.0 | 126.0 | 126.5 | 132.0 | 10.52   | 10.52 | 10.56 | 11.02 | 11.98   | 11.98 | 11.98 | 11.98 | 
+-----------+---------+-------+-------+-------+-------+---------+-------+-------+-------+---------+-------+-------+-------+

+-----------+---------+---------------+---------------------+
| Chassis   | Name    | Sensor Health | Highest Temperature |
+-----------+---------+---------------+---------------------+
| chassis-1 | blade-1 | True          | 37.5                | 
| chassis-1 | blade-2 | True          | 38.0                | 
| chassis-1 | blade-3 | True          | 40.5                | 
| chassis-1 | blade-4 | True          | 41.0                | 
+-----------+---------+---------------+---------------------+
```

JSON Output

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --blade --env

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
                "time_collected": "2022-12-08T11:02:10.857",
                "chassis_rn": "chassis-1",
                "input_power": 1128.0,
                "output_power": 874.0,
                "input_power_avg": 1116.0,
                "output_power_avg": 839.5,
                "input_power_min": 1104.0,
                "output_power_min": 828.0,
                "input_power_max": 1128.0,
                "output_power_max": 874.0
            },
            "PSU": [
                {
                    "dn": "sys/chassis-1/psu-1/stats",
                    "time_collected": "2022-12-08T11:02:10.856",
                    "chassis_rn": "chassis-1",
                    "psu_rn": "psu-1",
                    "psu_id": "1",
                    "name": "PSU 1",
                    "output_power": 360.24,
                    "output_power_avg": 356.24,
                    "output_power_min": 348.23,
                    "output_power_max": 360.24,
                    "output_current": 30.0,
                    "output_current_avg": 29.67,
                    "output_current_min": 29.0,
                    "output_current_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/psu-2/stats",
                    "time_collected": "2022-12-08T11:02:10.856",
                    "chassis_rn": "chassis-1",
                    "psu_rn": "psu-2",
                    "psu_id": "2",
                    "name": "PSU 2",
                    "output_power": 381.73,
                    "output_power_avg": 367.81,
                    "output_power_min": 357.87,
                    "output_power_max": 381.73,
                    "output_current": 32.0,
                    "output_current_avg": 30.83,
                    "output_current_min": 30.0,
                    "output_current_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/psu-3/stats",
                    "time_collected": "2022-12-08T11:02:10.856",
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
                    "time_collected": "2022-12-08T11:02:10.856",
                    "chassis_rn": "chassis-1",
                    "psu_rn": "psu-4",
                    "psu_id": "4",
                    "name": "PSU 4",
                    "output_power": 95.43,
                    "output_power_avg": 89.47,
                    "output_power_min": 83.5,
                    "output_power_max": 95.43,
                    "output_current": 8.0,
                    "output_current_avg": 7.5,
                    "output_current_min": 7.0,
                    "output_current_max": 8.0
                }
            ]
        }
    },
    "thermal_stats": {
        "Data": {
            "Fan": [
                {
                    "dn": "sys/chassis-1/fan-module-1-1/fan-1/stats",
                    "time_collected": "2022-12-08T11:02:10.857",
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
                    "time_collected": "2022-12-08T11:02:10.857",
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
                    "time_collected": "2022-12-08T11:02:10.857",
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
                    "time_collected": "2022-12-08T11:02:10.857",
                    "chassis_rn": "chassis-1",
                    "fan_module_rn": "fan-module-1-2",
                    "fan_module_id": "2",
                    "fan_rn": "fan-2",
                    "fan_id": "2",
                    "name": "Fan Module 2 - Fan 2",
                    "speed": "3520",
                    "speed_avg": "3511",
                    "speed_min": "3476",
                    "speed_max": "3520"
                },
                {
                    "dn": "sys/chassis-1/fan-module-1-3/fan-1/stats",
                    "time_collected": "2022-12-08T11:02:10.857",
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
                    "time_collected": "2022-12-08T11:02:10.857",
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
                    "time_collected": "2022-12-08T11:02:10.857",
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
                    "time_collected": "2022-12-08T11:02:10.857",
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
                    "time_collected": "2022-12-08T11:02:10.857",
                    "chassis_rn": "chassis-1",
                    "fan_module_rn": "fan-module-1-5",
                    "fan_module_id": "5",
                    "fan_rn": "fan-1",
                    "fan_id": "1",
                    "name": "Fan Module 5 - Fan 1",
                    "speed": "3256",
                    "speed_avg": "3292",
                    "speed_min": "3256",
                    "speed_max": "3300"
                },
                {
                    "dn": "sys/chassis-1/fan-module-1-5/fan-2/stats",
                    "time_collected": "2022-12-08T11:02:10.857",
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
                    "time_collected": "2022-12-08T11:02:10.857",
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
                    "time_collected": "2022-12-08T11:02:10.857",
                    "chassis_rn": "chassis-1",
                    "fan_module_rn": "fan-module-1-6",
                    "fan_module_id": "6",
                    "fan_rn": "fan-2",
                    "fan_id": "2",
                    "name": "Fan Module 6 - Fan 2",
                    "speed": "3520",
                    "speed_avg": "3490",
                    "speed_min": "3476",
                    "speed_max": "3520"
                },
                {
                    "dn": "sys/chassis-1/fan-module-1-7/fan-1/stats",
                    "time_collected": "2022-12-08T11:02:10.857",
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
                    "time_collected": "2022-12-08T11:02:10.857",
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
                    "time_collected": "2022-12-08T11:02:10.857",
                    "chassis_rn": "chassis-1",
                    "fan_module_rn": "fan-module-1-8",
                    "fan_module_id": "8",
                    "fan_rn": "fan-1",
                    "fan_id": "1",
                    "name": "Fan Module 8 - Fan 1",
                    "speed": "3344",
                    "speed_avg": "3328",
                    "speed_min": "3300",
                    "speed_max": "3344"
                },
                {
                    "dn": "sys/chassis-1/fan-module-1-8/fan-2/stats",
                    "time_collected": "2022-12-08T11:02:10.857",
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
                    "time_collected": "2022-12-08T11:02:10.856",
                    "chassis_rn": "chassis-1",
                    "fan_module_rn": "fan-module-1-1",
                    "fan_module_id": "1",
                    "name": "Fan Module 1",
                    "temperature": 33.0,
                    "temperature_avg": 33.17,
                    "temperature_min": 33.0,
                    "temperature_max": 34.0
                },
                {
                    "dn": "sys/chassis-1/fan-module-1-2/stats",
                    "time_collected": "2022-12-08T11:02:10.856",
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
                    "time_collected": "2022-12-08T11:02:10.856",
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
                    "time_collected": "2022-12-08T11:02:10.856",
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
                    "time_collected": "2022-12-08T11:02:10.856",
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
                    "time_collected": "2022-12-08T11:02:10.856",
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
                    "time_collected": "2022-12-08T11:02:10.856",
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
                    "time_collected": "2022-12-08T11:02:10.856",
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
                    "time_collected": "2022-12-08T11:02:10.856",
                    "chassis_rn": "chassis-1",
                    "psu_rn": "psu-1",
                    "psu_id": "1",
                    "name": "PSU 1",
                    "temperature": 25.0,
                    "temperature_avg": 24.17,
                    "temperature_min": 24.0,
                    "temperature_max": 25.0
                },
                {
                    "dn": "sys/chassis-1/psu-2/stats",
                    "time_collected": "2022-12-08T11:02:10.856",
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
                    "time_collected": "2022-12-08T11:02:10.856",
                    "chassis_rn": "chassis-1",
                    "psu_rn": "psu-3",
                    "psu_id": "3",
                    "name": "PSU 3",
                    "temperature": 24.0,
                    "temperature_avg": 24.83,
                    "temperature_min": 24.0,
                    "temperature_max": 25.0
                },
                {
                    "dn": "sys/chassis-1/psu-4/stats",
                    "time_collected": "2022-12-08T11:02:10.856",
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
                    "time_collected": "2022-12-08T11:02:03.105",
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
                    "time_collected": "2022-12-08T11:02:10.856",
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
                    "time_collected": "2022-12-08T11:02:03.105",
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
                    "time_collected": "2022-12-08T11:02:10.856",
                    "chassis_rn": "chassis-1",
                    "slot_rn": "slot-2",
                    "slot_id": "2",
                    "name": "IO Module 2 - ASIC",
                    "temperature": 65.0,
                    "temperature_avg": 65.38,
                    "temperature_min": 65.0,
                    "temperature_max": 66.0
                }
            ]
        },
        "Summary": {
            "Source": "UCSM",
            "HighestTemperature": 65.0
        }
    },
    "blade": [
        {
            "mo_type": "blade",
            "association": "associated",
            "chassis_id": "1",
            "available_memory": "524288",
            "assigned_to_dn": "org-root/org-EU-SPN/ls-esx41-eu-spdc",
            "admin_state": "in-service",
            "dn": "sys/chassis-1/blade-1",
            "model": "UCSB-B200-M4",
            "num_of_adaptors": "1",
            "num_of_cores": "24",
            "num_of_cores_enabled": "24",
            "num_of_cpus": "2",
            "num_of_eth_host_ifs": "8",
            "num_of_fc_host_ifs": "0",
            "num_of_threads": "48",
            "oper_power": "on",
            "oper_state": "ok",
            "operability": "operable",
            "part_number": "73-15862-04",
            "rn": "blade-1",
            "serial": "FCH205371PZ",
            "server_id": "1/1",
            "slot_id": "1",
            "total_memory": "524288",
            "uuid": "315220a5-2121-4e5b-0101-e1dc0000014f",
            "vendor": "Cisco Systems Inc",
            "id": "1",
            "chassis_rn": "chassis-1",
            "power": {
                "Data": {
                    "dn": "sys/chassis-1/blade-1/board/power-stats",
                    "time_collected": "2022-12-08T11:02:22.894",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "consumed_power": 138.0,
                    "input_current": 11.47,
                    "input_voltage": 12.04,
                    "consumed_power_avg": 138.0,
                    "input_current_avg": 11.47,
                    "input_voltage_avg": 12.04,
                    "consumed_power_min": 138.0,
                    "input_current_min": 11.47,
                    "input_voltage_min": 12.04,
                    "consumed_power_max": 138.0,
                    "input_current_max": 11.47,
                    "input_voltage_max": 12.04
                },
                "Summary": {
                    "Source": "UCSM",
                    "PowerNow": 138.0,
                    "PowerMin": 138.0,
                    "PowerAvg": 138.0,
                    "PowerMax": 138.0
                }
            },
            "thermal": {
                "Data": [
                    {
                        "dn": "sys/chassis-1/blade-1/board/temp-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "name": "Motherboard Front",
                        "type": "motherboard",
                        "temperature": 23.0,
                        "fm_temp_sen_rear": 36.0,
                        "temperature_avg": 23.0,
                        "fm_temp_sen_rear_avg": 36.0,
                        "temperature_min": 23.0,
                        "fm_temp_sen_rear_min": 36.0,
                        "temperature_max": 23.0,
                        "fm_temp_sen_rear_max": 36.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/temp-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "name": "Motherboard Rear",
                        "type": "motherboard",
                        "temperature": 36.0,
                        "temperature_avg": 36.0,
                        "temperature_min": 36.0,
                        "temperature_max": 36.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/cpu-1/env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "cpu_rn": "cpu-1",
                        "name": "CPU-1",
                        "type": "cpu",
                        "temperature": 34.0,
                        "temperature_avg": 34.38,
                        "temperature_min": 34.0,
                        "temperature_max": 35.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/cpu-2/env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "cpu_rn": "cpu-2",
                        "name": "CPU-2",
                        "type": "cpu",
                        "temperature": 37.5,
                        "temperature_avg": 37.5,
                        "temperature_min": 37.0,
                        "temperature_max": 38.5
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-1/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-1",
                        "name": "MEM-1",
                        "type": "memory",
                        "temperature": 28.0,
                        "temperature_avg": 28.0,
                        "temperature_min": 28.0,
                        "temperature_max": 28.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-10/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-10",
                        "name": "MEM-10",
                        "type": "memory",
                        "temperature": 29.0,
                        "temperature_avg": 29.0,
                        "temperature_min": 29.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-11/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-11",
                        "name": "MEM-11",
                        "type": "memory",
                        "temperature": 25.0,
                        "temperature_avg": 25.0,
                        "temperature_min": 25.0,
                        "temperature_max": 25.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-13/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-13",
                        "name": "MEM-13",
                        "type": "memory",
                        "temperature": 32.0,
                        "temperature_avg": 32.0,
                        "temperature_min": 32.0,
                        "temperature_max": 32.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-14/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-14",
                        "name": "MEM-14",
                        "type": "memory",
                        "temperature": 30.0,
                        "temperature_avg": 30.0,
                        "temperature_min": 30.0,
                        "temperature_max": 30.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-16/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-16",
                        "name": "MEM-16",
                        "type": "memory",
                        "temperature": 28.0,
                        "temperature_avg": 28.0,
                        "temperature_min": 28.0,
                        "temperature_max": 28.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-17/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-17",
                        "name": "MEM-17",
                        "type": "memory",
                        "temperature": 25.0,
                        "temperature_avg": 25.0,
                        "temperature_min": 25.0,
                        "temperature_max": 25.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-19/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-19",
                        "name": "MEM-19",
                        "type": "memory",
                        "temperature": 30.0,
                        "temperature_avg": 30.0,
                        "temperature_min": 30.0,
                        "temperature_max": 30.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-2/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-2",
                        "name": "MEM-2",
                        "type": "memory",
                        "temperature": 26.0,
                        "temperature_avg": 26.0,
                        "temperature_min": 26.0,
                        "temperature_max": 26.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-20/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-20",
                        "name": "MEM-20",
                        "type": "memory",
                        "temperature": 29.0,
                        "temperature_avg": 28.5,
                        "temperature_min": 28.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-22/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-22",
                        "name": "MEM-22",
                        "type": "memory",
                        "temperature": 27.0,
                        "temperature_avg": 27.0,
                        "temperature_min": 27.0,
                        "temperature_max": 27.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-23/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-23",
                        "name": "MEM-23",
                        "type": "memory",
                        "temperature": 27.0,
                        "temperature_avg": 27.0,
                        "temperature_min": 27.0,
                        "temperature_max": 27.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-4/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-4",
                        "name": "MEM-4",
                        "type": "memory",
                        "temperature": 27.0,
                        "temperature_avg": 27.0,
                        "temperature_min": 27.0,
                        "temperature_max": 27.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-5/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-5",
                        "name": "MEM-5",
                        "type": "memory",
                        "temperature": 27.0,
                        "temperature_avg": 27.0,
                        "temperature_min": 27.0,
                        "temperature_max": 27.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-7/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-7",
                        "name": "MEM-7",
                        "type": "memory",
                        "temperature": 29.0,
                        "temperature_avg": 29.0,
                        "temperature_min": 29.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-8/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:22.894",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-1",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-8",
                        "name": "MEM-8",
                        "type": "memory",
                        "temperature": 28.0,
                        "temperature_avg": 28.0,
                        "temperature_min": 28.0,
                        "temperature_max": 28.0
                    }
                ],
                "Summary": {
                    "Source": "UCSM",
                    "FanHealth": "N/A",
                    "SensorHealth": true,
                    "HighestTemperature": 37.5,
                    "SmallestGap": "N/A",
                    "OverThreshold": "N/A"
                }
            }
        },
        {
            "mo_type": "blade",
            "association": "associated",
            "chassis_id": "1",
            "available_memory": "524288",
            "assigned_to_dn": "org-root/org-EU-SPN/ls-esx42-eu-spdc",
            "admin_state": "in-service",
            "dn": "sys/chassis-1/blade-2",
            "model": "UCSB-B200-M4",
            "num_of_adaptors": "1",
            "num_of_cores": "24",
            "num_of_cores_enabled": "24",
            "num_of_cpus": "2",
            "num_of_eth_host_ifs": "8",
            "num_of_fc_host_ifs": "0",
            "num_of_threads": "48",
            "oper_power": "on",
            "oper_state": "ok",
            "operability": "operable",
            "part_number": "73-15862-04",
            "rn": "blade-2",
            "serial": "FCH20527XXD",
            "server_id": "1/2",
            "slot_id": "2",
            "total_memory": "524288",
            "uuid": "315220a5-2121-4e5b-0101-e1dc0000015f",
            "vendor": "Cisco Systems Inc",
            "id": "2",
            "chassis_rn": "chassis-1",
            "power": {
                "Data": {
                    "dn": "sys/chassis-1/blade-2/board/power-stats",
                    "time_collected": "2022-12-08T11:01:56.607",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "consumed_power": 138.0,
                    "input_current": 11.52,
                    "input_voltage": 11.98,
                    "consumed_power_avg": 138.0,
                    "input_current_avg": 11.52,
                    "input_voltage_avg": 11.98,
                    "consumed_power_min": 138.0,
                    "input_current_min": 11.52,
                    "input_voltage_min": 11.98,
                    "consumed_power_max": 138.0,
                    "input_current_max": 11.52,
                    "input_voltage_max": 11.98
                },
                "Summary": {
                    "Source": "UCSM",
                    "PowerNow": 138.0,
                    "PowerMin": 138.0,
                    "PowerAvg": 138.0,
                    "PowerMax": 138.0
                }
            },
            "thermal": {
                "Data": [
                    {
                        "dn": "sys/chassis-1/blade-2/board/temp-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "name": "Motherboard Front",
                        "type": "motherboard",
                        "temperature": 24.0,
                        "fm_temp_sen_rear": 36.0,
                        "temperature_avg": 24.0,
                        "fm_temp_sen_rear_avg": 36.0,
                        "temperature_min": 24.0,
                        "fm_temp_sen_rear_min": 36.0,
                        "temperature_max": 24.0,
                        "fm_temp_sen_rear_max": 36.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/temp-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "name": "Motherboard Rear",
                        "type": "motherboard",
                        "temperature": 36.0,
                        "temperature_avg": 36.0,
                        "temperature_min": 36.0,
                        "temperature_max": 36.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/cpu-1/env-stats",
                        "time_collected": "2022-12-08T11:01:56.606",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "cpu_rn": "cpu-1",
                        "name": "CPU-1",
                        "type": "cpu",
                        "temperature": 35.5,
                        "temperature_avg": 35.25,
                        "temperature_min": 35.0,
                        "temperature_max": 35.5
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/cpu-2/env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "cpu_rn": "cpu-2",
                        "name": "CPU-2",
                        "type": "cpu",
                        "temperature": 38.0,
                        "temperature_avg": 37.94,
                        "temperature_min": 37.5,
                        "temperature_max": 38.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-1/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-1",
                        "name": "MEM-1",
                        "type": "memory",
                        "temperature": 29.0,
                        "temperature_avg": 29.0,
                        "temperature_min": 29.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-10/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-10",
                        "name": "MEM-10",
                        "type": "memory",
                        "temperature": 29.0,
                        "temperature_avg": 29.0,
                        "temperature_min": 29.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-11/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-11",
                        "name": "MEM-11",
                        "type": "memory",
                        "temperature": 26.0,
                        "temperature_avg": 26.0,
                        "temperature_min": 26.0,
                        "temperature_max": 26.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-13/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-13",
                        "name": "MEM-13",
                        "type": "memory",
                        "temperature": 30.0,
                        "temperature_avg": 29.83,
                        "temperature_min": 29.0,
                        "temperature_max": 30.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-14/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-14",
                        "name": "MEM-14",
                        "type": "memory",
                        "temperature": 28.0,
                        "temperature_avg": 28.0,
                        "temperature_min": 28.0,
                        "temperature_max": 28.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-16/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-16",
                        "name": "MEM-16",
                        "type": "memory",
                        "temperature": 32.0,
                        "temperature_avg": 32.0,
                        "temperature_min": 32.0,
                        "temperature_max": 32.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-17/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-17",
                        "name": "MEM-17",
                        "type": "memory",
                        "temperature": 31.0,
                        "temperature_avg": 31.0,
                        "temperature_min": 31.0,
                        "temperature_max": 31.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-19/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-19",
                        "name": "MEM-19",
                        "type": "memory",
                        "temperature": 30.0,
                        "temperature_avg": 30.0,
                        "temperature_min": 30.0,
                        "temperature_max": 30.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-2/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-2",
                        "name": "MEM-2",
                        "type": "memory",
                        "temperature": 28.0,
                        "temperature_avg": 28.0,
                        "temperature_min": 28.0,
                        "temperature_max": 28.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-20/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-20",
                        "name": "MEM-20",
                        "type": "memory",
                        "temperature": 30.0,
                        "temperature_avg": 30.0,
                        "temperature_min": 30.0,
                        "temperature_max": 30.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-22/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-22",
                        "name": "MEM-22",
                        "type": "memory",
                        "temperature": 32.0,
                        "temperature_avg": 32.0,
                        "temperature_min": 32.0,
                        "temperature_max": 32.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-23/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-23",
                        "name": "MEM-23",
                        "type": "memory",
                        "temperature": 31.0,
                        "temperature_avg": 31.67,
                        "temperature_min": 31.0,
                        "temperature_max": 32.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-4/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-4",
                        "name": "MEM-4",
                        "type": "memory",
                        "temperature": 29.0,
                        "temperature_avg": 29.0,
                        "temperature_min": 29.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-5/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-5",
                        "name": "MEM-5",
                        "type": "memory",
                        "temperature": 28.0,
                        "temperature_avg": 28.0,
                        "temperature_min": 28.0,
                        "temperature_max": 28.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-7/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-7",
                        "name": "MEM-7",
                        "type": "memory",
                        "temperature": 29.0,
                        "temperature_avg": 29.0,
                        "temperature_min": 29.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-8/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:56.607",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-2",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-8",
                        "name": "MEM-8",
                        "type": "memory",
                        "temperature": 28.0,
                        "temperature_avg": 28.0,
                        "temperature_min": 28.0,
                        "temperature_max": 28.0
                    }
                ],
                "Summary": {
                    "Source": "UCSM",
                    "FanHealth": "N/A",
                    "SensorHealth": true,
                    "HighestTemperature": 38.0,
                    "SmallestGap": "N/A",
                    "OverThreshold": "N/A"
                }
            }
        },
        {
            "mo_type": "blade",
            "association": "associated",
            "chassis_id": "1",
            "available_memory": "262144",
            "assigned_to_dn": "org-root/org-EU-SPN/ls-esx43-eu-spdc",
            "admin_state": "in-service",
            "dn": "sys/chassis-1/blade-3",
            "model": "UCSB-B200-M4",
            "num_of_adaptors": "1",
            "num_of_cores": "24",
            "num_of_cores_enabled": "24",
            "num_of_cpus": "2",
            "num_of_eth_host_ifs": "8",
            "num_of_fc_host_ifs": "0",
            "num_of_threads": "48",
            "oper_power": "on",
            "oper_state": "ok",
            "operability": "operable",
            "part_number": "73-15862-04",
            "rn": "blade-3",
            "serial": "FCH20437VXH",
            "server_id": "1/3",
            "slot_id": "3",
            "total_memory": "262144",
            "uuid": "315220a5-2121-4e5b-0101-e1dc0000012f",
            "vendor": "Cisco Systems Inc",
            "id": "3",
            "chassis_rn": "chassis-1",
            "power": {
                "Data": {
                    "dn": "sys/chassis-1/blade-3/board/power-stats",
                    "time_collected": "2022-12-08T11:01:59.135",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "consumed_power": 126.0,
                    "input_current": 10.52,
                    "input_voltage": 11.98,
                    "consumed_power_avg": 126.0,
                    "input_current_avg": 10.52,
                    "input_voltage_avg": 11.98,
                    "consumed_power_min": 126.0,
                    "input_current_min": 10.52,
                    "input_voltage_min": 11.98,
                    "consumed_power_max": 126.0,
                    "input_current_max": 10.52,
                    "input_voltage_max": 11.98
                },
                "Summary": {
                    "Source": "UCSM",
                    "PowerNow": 126.0,
                    "PowerMin": 126.0,
                    "PowerAvg": 126.0,
                    "PowerMax": 126.0
                }
            },
            "thermal": {
                "Data": [
                    {
                        "dn": "sys/chassis-1/blade-3/board/temp-stats",
                        "time_collected": "2022-12-08T11:01:59.135",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-3",
                        "name": "Motherboard Front",
                        "type": "motherboard",
                        "temperature": 25.0,
                        "fm_temp_sen_rear": 36.0,
                        "temperature_avg": 25.0,
                        "fm_temp_sen_rear_avg": 36.0,
                        "temperature_min": 25.0,
                        "fm_temp_sen_rear_min": 36.0,
                        "temperature_max": 25.0,
                        "fm_temp_sen_rear_max": 36.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-3/board/temp-stats",
                        "time_collected": "2022-12-08T11:01:59.135",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-3",
                        "name": "Motherboard Rear",
                        "type": "motherboard",
                        "temperature": 36.0,
                        "temperature_avg": 36.0,
                        "temperature_min": 36.0,
                        "temperature_max": 36.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-3/board/cpu-1/env-stats",
                        "time_collected": "2022-12-08T11:01:59.135",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-3",
                        "cpu_rn": "cpu-1",
                        "name": "CPU-1",
                        "type": "cpu",
                        "temperature": 37.5,
                        "temperature_avg": 37.03,
                        "temperature_min": 36.5,
                        "temperature_max": 37.5
                    },
                    {
                        "dn": "sys/chassis-1/blade-3/board/cpu-2/env-stats",
                        "time_collected": "2022-12-08T11:01:59.135",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-3",
                        "cpu_rn": "cpu-2",
                        "name": "CPU-2",
                        "type": "cpu",
                        "temperature": 40.5,
                        "temperature_avg": 40.57,
                        "temperature_min": 40.0,
                        "temperature_max": 41.5
                    },
                    {
                        "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-1/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:59.135",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-3",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-1",
                        "name": "MEM-1",
                        "type": "memory",
                        "temperature": 28.0,
                        "temperature_avg": 28.0,
                        "temperature_min": 28.0,
                        "temperature_max": 28.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-10/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:59.135",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-3",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-10",
                        "name": "MEM-10",
                        "type": "memory",
                        "temperature": 28.0,
                        "temperature_avg": 28.0,
                        "temperature_min": 28.0,
                        "temperature_max": 28.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-13/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:59.135",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-3",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-13",
                        "name": "MEM-13",
                        "type": "memory",
                        "temperature": 27.0,
                        "temperature_avg": 27.0,
                        "temperature_min": 27.0,
                        "temperature_max": 27.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-16/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:59.135",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-3",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-16",
                        "name": "MEM-16",
                        "type": "memory",
                        "temperature": 28.0,
                        "temperature_avg": 28.33,
                        "temperature_min": 28.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-19/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:59.135",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-3",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-19",
                        "name": "MEM-19",
                        "type": "memory",
                        "temperature": 25.0,
                        "temperature_avg": 24.93,
                        "temperature_min": 24.0,
                        "temperature_max": 25.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-22/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:59.135",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-3",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-22",
                        "name": "MEM-22",
                        "type": "memory",
                        "temperature": 27.0,
                        "temperature_avg": 27.47,
                        "temperature_min": 27.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-4/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:59.135",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-3",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-4",
                        "name": "MEM-4",
                        "type": "memory",
                        "temperature": 27.0,
                        "temperature_avg": 27.0,
                        "temperature_min": 27.0,
                        "temperature_max": 27.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-7/dimm-env-stats",
                        "time_collected": "2022-12-08T11:01:59.135",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-3",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-7",
                        "name": "MEM-7",
                        "type": "memory",
                        "temperature": 29.0,
                        "temperature_avg": 29.0,
                        "temperature_min": 29.0,
                        "temperature_max": 29.0
                    }
                ],
                "Summary": {
                    "Source": "UCSM",
                    "FanHealth": "N/A",
                    "SensorHealth": true,
                    "HighestTemperature": 40.5,
                    "SmallestGap": "N/A",
                    "OverThreshold": "N/A"
                }
            }
        },
        {
            "mo_type": "blade",
            "association": "associated",
            "chassis_id": "1",
            "available_memory": "262144",
            "assigned_to_dn": "org-root/org-EU-SPN/ls-esx44-eu-spdc",
            "admin_state": "in-service",
            "dn": "sys/chassis-1/blade-4",
            "model": "UCSB-B200-M4",
            "num_of_adaptors": "1",
            "num_of_cores": "24",
            "num_of_cores_enabled": "24",
            "num_of_cpus": "2",
            "num_of_eth_host_ifs": "8",
            "num_of_fc_host_ifs": "0",
            "num_of_threads": "48",
            "oper_power": "on",
            "oper_state": "ok",
            "operability": "operable",
            "part_number": "73-15862-04",
            "rn": "blade-4",
            "serial": "FCH205371UU",
            "server_id": "1/4",
            "slot_id": "4",
            "total_memory": "262144",
            "uuid": "315220a5-2121-4e5b-0101-e1dc0000013f",
            "vendor": "Cisco Systems Inc",
            "id": "4",
            "chassis_rn": "chassis-1",
            "power": {
                "Data": {
                    "dn": "sys/chassis-1/blade-4/board/power-stats",
                    "time_collected": "2022-12-08T11:02:18.061",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "consumed_power": 126.0,
                    "input_current": 10.52,
                    "input_voltage": 11.98,
                    "consumed_power_avg": 126.5,
                    "input_current_avg": 10.56,
                    "input_voltage_avg": 11.98,
                    "consumed_power_min": 126.0,
                    "input_current_min": 10.52,
                    "input_voltage_min": 11.98,
                    "consumed_power_max": 132.0,
                    "input_current_max": 11.02,
                    "input_voltage_max": 11.98
                },
                "Summary": {
                    "Source": "UCSM",
                    "PowerNow": 126.0,
                    "PowerMin": 126.0,
                    "PowerAvg": 126.5,
                    "PowerMax": 132.0
                }
            },
            "thermal": {
                "Data": [
                    {
                        "dn": "sys/chassis-1/blade-4/board/temp-stats",
                        "time_collected": "2022-12-08T11:02:18.061",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-4",
                        "name": "Motherboard Front",
                        "type": "motherboard",
                        "temperature": 25.0,
                        "fm_temp_sen_rear": 36.0,
                        "temperature_avg": 25.0,
                        "fm_temp_sen_rear_avg": 36.0,
                        "temperature_min": 25.0,
                        "fm_temp_sen_rear_min": 36.0,
                        "temperature_max": 25.0,
                        "fm_temp_sen_rear_max": 36.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-4/board/temp-stats",
                        "time_collected": "2022-12-08T11:02:18.061",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-4",
                        "name": "Motherboard Rear",
                        "type": "motherboard",
                        "temperature": 36.0,
                        "temperature_avg": 36.0,
                        "temperature_min": 36.0,
                        "temperature_max": 36.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-4/board/cpu-1/env-stats",
                        "time_collected": "2022-12-08T11:02:18.061",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-4",
                        "cpu_rn": "cpu-1",
                        "name": "CPU-1",
                        "type": "cpu",
                        "temperature": 38.5,
                        "temperature_avg": 38.29,
                        "temperature_min": 38.0,
                        "temperature_max": 39.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-4/board/cpu-2/env-stats",
                        "time_collected": "2022-12-08T11:02:18.061",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-4",
                        "cpu_rn": "cpu-2",
                        "name": "CPU-2",
                        "type": "cpu",
                        "temperature": 41.0,
                        "temperature_avg": 41.21,
                        "temperature_min": 41.0,
                        "temperature_max": 42.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-1/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:18.061",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-4",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-1",
                        "name": "MEM-1",
                        "type": "memory",
                        "temperature": 28.0,
                        "temperature_avg": 28.0,
                        "temperature_min": 28.0,
                        "temperature_max": 28.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-10/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:18.061",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-4",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-10",
                        "name": "MEM-10",
                        "type": "memory",
                        "temperature": 29.0,
                        "temperature_avg": 28.83,
                        "temperature_min": 28.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-13/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:18.061",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-4",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-13",
                        "name": "MEM-13",
                        "type": "memory",
                        "temperature": 32.0,
                        "temperature_avg": 32.0,
                        "temperature_min": 32.0,
                        "temperature_max": 32.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-16/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:18.061",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-4",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-16",
                        "name": "MEM-16",
                        "type": "memory",
                        "temperature": 28.0,
                        "temperature_avg": 28.0,
                        "temperature_min": 28.0,
                        "temperature_max": 28.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-19/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:18.061",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-4",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-19",
                        "name": "MEM-19",
                        "type": "memory",
                        "temperature": 31.0,
                        "temperature_avg": 30.67,
                        "temperature_min": 30.0,
                        "temperature_max": 31.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-22/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:18.061",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-4",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-22",
                        "name": "MEM-22",
                        "type": "memory",
                        "temperature": 28.0,
                        "temperature_avg": 28.0,
                        "temperature_min": 28.0,
                        "temperature_max": 28.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-4/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:18.061",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-4",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-4",
                        "name": "MEM-4",
                        "type": "memory",
                        "temperature": 27.0,
                        "temperature_avg": 27.0,
                        "temperature_min": 27.0,
                        "temperature_max": 27.0
                    },
                    {
                        "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-7/dimm-env-stats",
                        "time_collected": "2022-12-08T11:02:18.061",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-4",
                        "array_rn": "memarray-1",
                        "dimm_rn": "mem-7",
                        "name": "MEM-7",
                        "type": "memory",
                        "temperature": 30.0,
                        "temperature_avg": 30.0,
                        "temperature_min": 30.0,
                        "temperature_max": 30.0
                    }
                ],
                "Summary": {
                    "Source": "UCSM",
                    "FanHealth": "N/A",
                    "SensorHealth": true,
                    "HighestTemperature": 41.0,
                    "SmallestGap": "N/A",
                    "OverThreshold": "N/A"
                }
            }
        }
    ]
}
```

Developer Output

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --blade --env

Developer output

{
    "duration": 7825,
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
        "success": 13,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 2047,
        "disconnect_time": 0,
        "mo_time": 5360,
        "total_time": 7407
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

2022-12-08 11:02:42.428495	True	1594	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 11:02:42.896116	True	465	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 11:02:43.337995	True	434	vip-ucsb1.emea-sp.cisco.com:equipmentChassisStats
2022-12-08 11:02:43.778166	True	439	vip-ucsb1.emea-sp.cisco.com:EquipmentPsuStats
2022-12-08 11:02:44.226149	True	446	vip-ucsb1.emea-sp.cisco.com:EquipmentFanStats
2022-12-08 11:02:44.670182	True	442	vip-ucsb1.emea-sp.cisco.com:EquipmentFanModuleStats
2022-12-08 11:02:45.113372	True	440	vip-ucsb1.emea-sp.cisco.com:EquipmentIOCardStats
2022-12-08 11:02:45.631951	True	515	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 11:02:46.074287	True	429	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 11:02:46.573133	True	497	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 11:02:47.131230	True	557	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 11:02:47.836444	True	696	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 11:02:48.620077	True	453	disconnect vip-ucsb1.emea-sp.cisco.com
```
