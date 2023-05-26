# Get Chassis with Environmental Information

Environmental = Power + Thermal

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --env

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

+----------------------+-------------+------+------+------+
| Fan                  | Speed (RPM) | Min  | Avg  | Max  |
+----------------------+-------------+------+------+------+
| Fan Module 1 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| Fan Module 1 - Fan 2 | 3476        | 3476 | 3476 | 3476 | 
| Fan Module 2 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| Fan Module 2 - Fan 2 | 3520        | 3476 | 3510 | 3520 | 
| Fan Module 3 - Fan 1 | 3344        | 3344 | 3344 | 3344 | 
| Fan Module 3 - Fan 2 | 3564        | 3564 | 3564 | 3564 | 
| Fan Module 4 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| Fan Module 4 - Fan 2 | 3520        | 3520 | 3520 | 3520 | 
| Fan Module 5 - Fan 1 | 3300        | 3300 | 3300 | 3300 | 
| Fan Module 5 - Fan 2 | 3520        | 3520 | 3520 | 3520 | 
| Fan Module 6 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| Fan Module 6 - Fan 2 | 3520        | 3476 | 3484 | 3520 | 
| Fan Module 7 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| Fan Module 7 - Fan 2 | 3476        | 3476 | 3476 | 3476 | 
| Fan Module 8 - Fan 1 | 3344        | 3300 | 3325 | 3344 | 
| Fan Module 8 - Fan 2 | 3520        | 3520 | 3520 | 3520 | 
+----------------------+-------------+------+------+------+

+-----------------------+-----------------+------+-------+------+
| Sensor                | Temperature (C) | Min  | Avg   | Max  |
+-----------------------+-----------------+------+-------+------+
| Fan Module 1          | 33.0            | 33.0 | 33.2  | 34.0 | 
| Fan Module 2          | 33.0            | 33.0 | 33.0  | 33.0 | 
| Fan Module 3          | 35.0            | 35.0 | 35.0  | 35.0 | 
| Fan Module 4          | 32.0            | 32.0 | 32.0  | 32.0 | 
| Fan Module 5          | 29.0            | 29.0 | 29.0  | 29.0 | 
| Fan Module 6          | 28.0            | 28.0 | 28.0  | 28.0 | 
| Fan Module 7          | 31.0            | 31.0 | 31.0  | 31.0 | 
| Fan Module 8          | 29.0            | 29.0 | 29.0  | 29.0 | 
| PSU 1                 | 24.0            | 24.0 | 24.0  | 24.0 | 
| PSU 2                 | 25.0            | 25.0 | 25.0  | 25.0 | 
| PSU 3                 | 25.0            | 25.0 | 25.0  | 25.0 | 
| PSU 4                 | 23.0            | 23.0 | 23.0  | 23.0 | 
| IO Module 1 - Ambient | 42.0            | 42.0 | 42.0  | 42.0 | 
| IO Module 2 - Ambient | 45.0            | 45.0 | 45.0  | 45.0 | 
| IO Module 1 - ASIC    | 64.0            | 64.0 | 64.0  | 64.0 | 
| IO Module 2 - ASIC    | 65.0            | 65.0 | 65.45 | 66.0 | 
+-----------------------+-----------------+------+-------+------+
```

JSON Output

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --env

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
    },
    "thermal_stats": {
        "Data": {
            "Fan": [
                {
                    "dn": "sys/chassis-1/fan-module-1-1/fan-1/stats",
                    "time_collected": "2022-12-08T11:01:10.787",
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
                    "time_collected": "2022-12-08T11:01:10.787",
                    "chassis_rn": "chassis-1",
                    "fan_module_rn": "fan-module-1-1",
                    "fan_module_id": "1",
                    "fan_rn": "fan-2",
                    "fan_id": "2",
                    "name": "Fan Module 1 - Fan 2",
                    "speed": "3476",
                    "speed_avg": "3476",
                    "speed_min": "3476",
                    "speed_max": "3476"
                },
                {
                    "dn": "sys/chassis-1/fan-module-1-2/fan-1/stats",
                    "time_collected": "2022-12-08T11:01:10.787",
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
                    "time_collected": "2022-12-08T11:01:10.787",
                    "chassis_rn": "chassis-1",
                    "fan_module_rn": "fan-module-1-2",
                    "fan_module_id": "2",
                    "fan_rn": "fan-2",
                    "fan_id": "2",
                    "name": "Fan Module 2 - Fan 2",
                    "speed": "3520",
                    "speed_avg": "3510",
                    "speed_min": "3476",
                    "speed_max": "3520"
                },
                {
                    "dn": "sys/chassis-1/fan-module-1-3/fan-1/stats",
                    "time_collected": "2022-12-08T11:01:10.787",
                    "chassis_rn": "chassis-1",
                    "fan_module_rn": "fan-module-1-3",
                    "fan_module_id": "3",
                    "fan_rn": "fan-1",
                    "fan_id": "1",
                    "name": "Fan Module 3 - Fan 1",
                    "speed": "3344",
                    "speed_avg": "3344",
                    "speed_min": "3344",
                    "speed_max": "3344"
                },
                {
                    "dn": "sys/chassis-1/fan-module-1-3/fan-2/stats",
                    "time_collected": "2022-12-08T11:01:10.787",
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
                    "time_collected": "2022-12-08T11:01:10.787",
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
                    "time_collected": "2022-12-08T11:01:10.787",
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
                    "time_collected": "2022-12-08T11:01:10.787",
                    "chassis_rn": "chassis-1",
                    "fan_module_rn": "fan-module-1-5",
                    "fan_module_id": "5",
                    "fan_rn": "fan-1",
                    "fan_id": "1",
                    "name": "Fan Module 5 - Fan 1",
                    "speed": "3300",
                    "speed_avg": "3300",
                    "speed_min": "3300",
                    "speed_max": "3300"
                },
                {
                    "dn": "sys/chassis-1/fan-module-1-5/fan-2/stats",
                    "time_collected": "2022-12-08T11:01:10.787",
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
                    "time_collected": "2022-12-08T11:01:10.787",
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
                    "time_collected": "2022-12-08T11:01:10.787",
                    "chassis_rn": "chassis-1",
                    "fan_module_rn": "fan-module-1-6",
                    "fan_module_id": "6",
                    "fan_rn": "fan-2",
                    "fan_id": "2",
                    "name": "Fan Module 6 - Fan 2",
                    "speed": "3520",
                    "speed_avg": "3484",
                    "speed_min": "3476",
                    "speed_max": "3520"
                },
                {
                    "dn": "sys/chassis-1/fan-module-1-7/fan-1/stats",
                    "time_collected": "2022-12-08T11:01:10.787",
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
                    "time_collected": "2022-12-08T11:01:10.787",
                    "chassis_rn": "chassis-1",
                    "fan_module_rn": "fan-module-1-7",
                    "fan_module_id": "7",
                    "fan_rn": "fan-2",
                    "fan_id": "2",
                    "name": "Fan Module 7 - Fan 2",
                    "speed": "3476",
                    "speed_avg": "3476",
                    "speed_min": "3476",
                    "speed_max": "3476"
                },
                {
                    "dn": "sys/chassis-1/fan-module-1-8/fan-1/stats",
                    "time_collected": "2022-12-08T11:01:10.787",
                    "chassis_rn": "chassis-1",
                    "fan_module_rn": "fan-module-1-8",
                    "fan_module_id": "8",
                    "fan_rn": "fan-1",
                    "fan_id": "1",
                    "name": "Fan Module 8 - Fan 1",
                    "speed": "3344",
                    "speed_avg": "3325",
                    "speed_min": "3300",
                    "speed_max": "3344"
                },
                {
                    "dn": "sys/chassis-1/fan-module-1-8/fan-2/stats",
                    "time_collected": "2022-12-08T11:01:10.787",
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
                    "time_collected": "2022-12-08T11:01:10.786",
                    "chassis_rn": "chassis-1",
                    "fan_module_rn": "fan-module-1-1",
                    "fan_module_id": "1",
                    "name": "Fan Module 1",
                    "temperature": 33.0,
                    "temperature_avg": 33.2,
                    "temperature_min": 33.0,
                    "temperature_max": 34.0
                },
                {
                    "dn": "sys/chassis-1/fan-module-1-2/stats",
                    "time_collected": "2022-12-08T11:01:10.786",
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
                    "time_collected": "2022-12-08T11:01:10.786",
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
                    "time_collected": "2022-12-08T11:01:10.786",
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
                    "time_collected": "2022-12-08T11:01:10.786",
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
                    "time_collected": "2022-12-08T11:01:10.786",
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
                    "time_collected": "2022-12-08T11:01:10.786",
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
                    "time_collected": "2022-12-08T11:01:10.786",
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
                    "time_collected": "2022-12-08T11:01:10.786",
                    "chassis_rn": "chassis-1",
                    "psu_rn": "psu-1",
                    "psu_id": "1",
                    "name": "PSU 1",
                    "temperature": 24.0,
                    "temperature_avg": 24.0,
                    "temperature_min": 24.0,
                    "temperature_max": 24.0
                },
                {
                    "dn": "sys/chassis-1/psu-2/stats",
                    "time_collected": "2022-12-08T11:01:10.786",
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
                    "time_collected": "2022-12-08T11:01:10.786",
                    "chassis_rn": "chassis-1",
                    "psu_rn": "psu-3",
                    "psu_id": "3",
                    "name": "PSU 3",
                    "temperature": 25.0,
                    "temperature_avg": 25.0,
                    "temperature_min": 25.0,
                    "temperature_max": 25.0
                },
                {
                    "dn": "sys/chassis-1/psu-4/stats",
                    "time_collected": "2022-12-08T11:01:10.786",
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
                    "time_collected": "2022-12-08T11:01:03.030",
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
                    "time_collected": "2022-12-08T11:01:10.786",
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
                    "time_collected": "2022-12-08T11:01:03.030",
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
                    "time_collected": "2022-12-08T11:01:10.786",
                    "chassis_rn": "chassis-1",
                    "slot_rn": "slot-2",
                    "slot_id": "2",
                    "name": "IO Module 2 - ASIC",
                    "temperature": 65.0,
                    "temperature_avg": 65.45,
                    "temperature_min": 65.0,
                    "temperature_max": 66.0
                }
            ]
        },
        "Summary": {
            "Source": "UCSM",
            "HighestTemperature": 65.0
        }
    }
}
```

Developer Output

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --env

Developer output

{
    "duration": 6594,
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
        "connect_time": 2170,
        "disconnect_time": 0,
        "mo_time": 2974,
        "total_time": 5144
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

2022-12-08 11:01:35.001137	True	1604	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 11:01:35.525712	True	521	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 11:01:35.983393	True	455	vip-ucsb1.emea-sp.cisco.com:equipmentChassisStats
2022-12-08 11:01:36.443921	True	458	vip-ucsb1.emea-sp.cisco.com:EquipmentPsuStats
2022-12-08 11:01:36.941102	True	492	vip-ucsb1.emea-sp.cisco.com:EquipmentFanStats
2022-12-08 11:01:37.496597	True	553	vip-ucsb1.emea-sp.cisco.com:EquipmentFanModuleStats
2022-12-08 11:01:37.993242	True	495	vip-ucsb1.emea-sp.cisco.com:EquipmentIOCardStats
2022-12-08 11:01:39.954165	True	566	disconnect vip-ucsb1.emea-sp.cisco.com
```
