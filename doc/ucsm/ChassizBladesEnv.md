# Get Chassis' and Blades with Environmental Information

Environmental = Power + Thermal

```
# iserver get ucsm chassiz --manager milan --blade --env

+------------+-----------+---------------+-------------+-------------+-------------+---------------+
| Chassis Id | Name      | Model         | Serial      | Operability | Power State | Thermal State |
+------------+-----------+---------------+-------------+-------------+-------------+---------------+
| 1          | chassis-1 | UCSB-5108-AC2 | FOX2403P669 | operable    | ok          | ok            | 
| 2          | chassis-2 | UCSB-5108-AC2 | FOX2403P2Z9 | operable    | ok          | ok            | 
+------------+-----------+---------------+-------------+-------------+-------------+---------------+

+-----------+---------+--------------+-------------+---------------+-------------+-------------+-------------+
| Chassis   | Blade   | Model        | Serial      | Overal Status | Operability | Power State | Assoc State |
+-----------+---------+--------------+-------------+---------------+-------------+-------------+-------------+
| chassis-1 | blade-1 | UCSB-B200-M4 | FCH205371PZ | ok            | operable    | on          | associated  | 
| chassis-1 | blade-2 | UCSB-B200-M4 | FCH20527XXD | ok            | operable    | on          | associated  | 
| chassis-1 | blade-3 | UCSB-B200-M4 | FCH20437VXH | ok            | operable    | on          | associated  | 
| chassis-1 | blade-4 | UCSB-B200-M4 | FCH205371UU | ok            | operable    | on          | associated  | 
| chassis-2 | blade-1 | UCSB-B200-M5 | FLM241501FB | ok            | operable    | on          | associated  | 
| chassis-2 | blade-2 | UCSB-B200-M5 | FLM24140BJB | ok            | operable    | on          | associated  | 
| chassis-2 | blade-3 | UCSB-B200-M5 | FLM241501CT | ok            | operable    | on          | associated  | 
| chassis-2 | blade-4 | UCSB-B200-M5 | FLM24140B0B | ok            | operable    | on          | associated  | 
+-----------+---------+--------------+-------------+---------------+-------------+-------------+-------------+

+-----------+-----------------+--------+--------+--------+------------------+--------+---------+--------+
| Chassis   | Input Power Now | Min    | Avg    | Max    | Output Power Now | Min    | Avg     | Max    |
+-----------+-----------------+--------+--------+--------+------------------+--------+---------+--------+
| chassis-1 | 1128.0          | 1104.0 | 1122.0 | 1152.0 | 782.0            | 782.0  | 839.5   | 897.0  | 
| chassis-2 | 1416.0          | 1416.0 | 1440.0 | 1488.0 | 1196.0           | 1058.0 | 1199.29 | 1288.0 | 
+-----------+-----------------+--------+--------+--------+------------------+--------+---------+--------+

+-----------+-------+------------------+--------+--------+--------+--------------------+------+-------+------+
| Chassis   | PSU   | Output Power (W) | Min    | Avg    | Max    | Output Current (A) | Min  | Avg   | Max  |
+-----------+-------+------------------+--------+--------+--------+--------------------+------+-------+------+
| chassis-1 | PSU 1 | 348.23           | 348.23 | 355.74 | 360.24 | 29.0               | 29.0 | 29.62 | 30.0 | 
| chassis-1 | PSU 2 | 357.87           | 357.87 | 368.31 | 381.73 | 30.0               | 30.0 | 30.88 | 32.0 | 
| chassis-1 | PSU 3 | 0.0              | 0.0    | 0.0    | 0.0    | 0.0                | 0.0  | 0.0   | 0.0  | 
| chassis-1 | PSU 4 | 83.5             | 83.5   | 93.94  | 131.22 | 7.0                | 7.0  | 7.88  | 11.0 | 
| chassis-2 | PSU 1 | 226.65           | 226.65 | 258.38 | 324.22 | 19.0               | 19.0 | 21.57 | 27.0 | 
| chassis-2 | PSU 2 | 310.15           | 310.15 | 320.49 | 336.22 | 26.0               | 26.0 | 26.71 | 28.0 | 
| chassis-2 | PSU 3 | 429.44           | 248.85 | 394.84 | 462.15 | 36.0               | 21.0 | 33.29 | 39.0 | 
| chassis-2 | PSU 4 | 226.65           | 202.79 | 223.67 | 238.58 | 19.0               | 17.0 | 18.71 | 20.0 | 
+-----------+-------+------------------+--------+--------+--------+--------------------+------+-------+------+

+-----------+---------+-------+-------+--------+-------+---------+-------+-------+-------+---------+-------+-------+-------+
| Chassis   | Name    | Power | Min   | Avg    | Max   | Current | Min   | Avg   | Max   | Voltage | Min   | Avg   | Max   |
+-----------+---------+-------+-------+--------+-------+---------+-------+-------+-------+---------+-------+-------+-------+
| chassis-1 | blade-1 | 138.0 | 138.0 | 138.0  | 138.0 | 11.47   | 11.47 | 11.47 | 11.47 | 12.04   | 12.04 | 12.04 | 12.04 | 
| chassis-1 | blade-2 | 138.0 | 138.0 | 138.0  | 138.0 | 11.52   | 11.52 | 11.52 | 11.52 | 11.98   | 11.98 | 11.98 | 11.98 | 
| chassis-1 | blade-3 | 126.0 | 126.0 | 126.0  | 126.0 | 10.52   | 10.52 | 10.52 | 10.52 | 11.98   | 11.98 | 11.98 | 11.98 | 
| chassis-1 | blade-4 | 126.0 | 126.0 | 126.43 | 132.0 | 10.52   | 10.52 | 10.56 | 11.02 | 11.98   | 11.98 | 11.98 | 11.98 | 
| chassis-2 | blade-1 | 214.5 | 210.6 | 212.55 | 214.5 | 17.73   | 17.41 | 17.57 | 17.73 | 12.1    | 12.1  | 12.1  | 12.1  | 
| chassis-2 | blade-2 | 241.8 | 241.8 | 244.14 | 253.5 | 19.89   | 19.89 | 20.09 | 20.86 | 12.15   | 12.15 | 12.15 | 12.15 | 
| chassis-2 | blade-3 | 195.0 | 195.0 | 195.0  | 195.0 | 16.12   | 16.12 | 16.12 | 16.12 | 12.1    | 12.1  | 12.1  | 12.1  | 
| chassis-2 | blade-4 | 234.0 | 234.0 | 239.85 | 245.7 | 19.35   | 19.35 | 19.83 | 20.31 | 12.1    | 12.1  | 12.1  | 12.1  | 
+-----------+---------+-------+-------+--------+-------+---------+-------+-------+-------+---------+-------+-------+-------+

+-----------+----------------------+-------------+------+------+------+
| Chassis   | Fan                  | Speed (RPM) | Min  | Avg  | Max  |
+-----------+----------------------+-------------+------+------+------+
| chassis-1 | Fan Module 1 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| chassis-1 | Fan Module 1 - Fan 2 | 3476        | 3476 | 3475 | 3476 | 
| chassis-1 | Fan Module 2 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| chassis-1 | Fan Module 2 - Fan 2 | 3520        | 3476 | 3513 | 3520 | 
| chassis-1 | Fan Module 3 - Fan 1 | 3344        | 3344 | 3343 | 3344 | 
| chassis-1 | Fan Module 3 - Fan 2 | 3564        | 3564 | 3564 | 3564 | 
| chassis-1 | Fan Module 4 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| chassis-1 | Fan Module 4 - Fan 2 | 3520        | 3520 | 3520 | 3520 | 
| chassis-1 | Fan Module 5 - Fan 1 | 3300        | 3256 | 3293 | 3300 | 
| chassis-1 | Fan Module 5 - Fan 2 | 3520        | 3520 | 3520 | 3520 | 
| chassis-1 | Fan Module 6 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| chassis-1 | Fan Module 6 - Fan 2 | 3520        | 3476 | 3492 | 3520 | 
| chassis-1 | Fan Module 7 - Fan 1 | 3256        | 3256 | 3256 | 3256 | 
| chassis-1 | Fan Module 7 - Fan 2 | 3476        | 3476 | 3475 | 3476 | 
| chassis-1 | Fan Module 8 - Fan 1 | 3344        | 3300 | 3331 | 3344 | 
| chassis-1 | Fan Module 8 - Fan 2 | 3520        | 3520 | 3520 | 3520 | 
| chassis-2 | Fan Module 1 - Fan 1 | 4576        | 4576 | 4576 | 4576 | 
| chassis-2 | Fan Module 1 - Fan 2 | 4840        | 4840 | 4839 | 4840 | 
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
| chassis-2 | Fan Module 8 - Fan 1 | 4620        | 4576 | 4593 | 4620 | 
| chassis-2 | Fan Module 8 - Fan 2 | 4928        | 4928 | 4928 | 4928 | 
+-----------+----------------------+-------------+------+------+------+

+-----------+-----------------------+-----------------+------+-------+------+
| Chassis   | Sensor                | Temperature (C) | Min  | Avg   | Max  |
+-----------+-----------------------+-----------------+------+-------+------+
| chassis-1 | Fan Module 1          | 33.0            | 33.0 | 33.25 | 34.0 | 
| chassis-1 | Fan Module 2          | 33.0            | 33.0 | 33.0  | 33.0 | 
| chassis-1 | Fan Module 3          | 35.0            | 35.0 | 35.0  | 35.0 | 
| chassis-1 | Fan Module 4          | 32.0            | 32.0 | 32.0  | 32.0 | 
| chassis-1 | Fan Module 5          | 29.0            | 29.0 | 29.0  | 29.0 | 
| chassis-1 | Fan Module 6          | 29.0            | 28.0 | 28.12 | 29.0 | 
| chassis-1 | Fan Module 7          | 31.0            | 31.0 | 31.0  | 31.0 | 
| chassis-1 | Fan Module 8          | 29.0            | 29.0 | 29.0  | 29.0 | 
| chassis-1 | PSU 1                 | 24.0            | 24.0 | 24.25 | 25.0 | 
| chassis-1 | PSU 2                 | 25.0            | 25.0 | 25.0  | 25.0 | 
| chassis-1 | PSU 3                 | 25.0            | 24.0 | 24.75 | 25.0 | 
| chassis-1 | PSU 4                 | 23.0            | 23.0 | 23.0  | 23.0 | 
| chassis-1 | IO Module 1 - Ambient | 42.0            | 42.0 | 42.0  | 42.0 | 
| chassis-1 | IO Module 2 - Ambient | 45.0            | 45.0 | 45.0  | 45.0 | 
| chassis-1 | IO Module 1 - ASIC    | 64.0            | 64.0 | 64.0  | 64.0 | 
| chassis-1 | IO Module 2 - ASIC    | 66.0            | 66.0 | 66.0  | 66.0 | 
| chassis-2 | Fan Module 1          | 31.0            | 31.0 | 31.0  | 31.0 | 
| chassis-2 | Fan Module 2          | 32.0            | 32.0 | 32.0  | 32.0 | 
| chassis-2 | Fan Module 3          | 30.0            | 30.0 | 30.0  | 30.0 | 
| chassis-2 | Fan Module 4          | 29.0            | 29.0 | 29.0  | 29.0 | 
| chassis-2 | Fan Module 5          | 29.0            | 29.0 | 29.0  | 29.0 | 
| chassis-2 | Fan Module 6          | 29.0            | 29.0 | 29.0  | 29.0 | 
| chassis-2 | Fan Module 7          | 27.0            | 27.0 | 27.0  | 27.0 | 
| chassis-2 | Fan Module 8          | 27.0            | 26.0 | 26.43 | 27.0 | 
| chassis-2 | PSU 1                 | 20.0            | 20.0 | 20.0  | 20.0 | 
| chassis-2 | PSU 2                 | 19.0            | 19.0 | 19.14 | 20.0 | 
| chassis-2 | PSU 3                 | 20.0            | 20.0 | 20.0  | 20.0 | 
| chassis-2 | PSU 4                 | 21.0            | 21.0 | 21.14 | 22.0 | 
| chassis-2 | IO Module 1 - Ambient | 39.0            | 39.0 | 39.0  | 39.0 | 
| chassis-2 | IO Module 2 - Ambient | 37.0            | 37.0 | 37.0  | 37.0 | 
| chassis-2 | IO Module 1 - ASIC    | 54.0            | 53.0 | 53.8  | 54.0 | 
| chassis-2 | IO Module 2 - ASIC    | 50.0            | 50.0 | 50.13 | 51.0 | 
+-----------+-----------------------+-----------------+------+-------+------+

+-----------+---------+---------------+---------------------+
| Chassis   | Name    | Sensor Health | Highest Temperature |
+-----------+---------+---------------+---------------------+
| chassis-1 | blade-1 | True          | 37.5                | 
| chassis-1 | blade-2 | True          | 38.0                | 
| chassis-1 | blade-3 | True          | 41.0                | 
| chassis-1 | blade-4 | True          | 41.0                | 
| chassis-2 | blade-1 | True          | 39.5                | 
| chassis-2 | blade-2 | True          | 48.5                | 
| chassis-2 | blade-3 | True          | 37.0                | 
| chassis-2 | blade-4 | True          | 49.0                | 
+-----------+---------+---------------+---------------------+
```

JSON Output

```
# iserver get ucsm chassiz --manager milan --blade --env

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
                        "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-1",
                            "cpu_rn": "cpu-1",
                            "name": "CPU-1",
                            "type": "cpu",
                            "temperature": 34.0,
                            "temperature_avg": 34.25,
                            "temperature_min": 34.0,
                            "temperature_max": 35.0
                        },
                        {
                            "dn": "sys/chassis-1/blade-1/board/cpu-2/env-stats",
                            "time_collected": "2022-12-08T11:04:22.939",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-1",
                            "cpu_rn": "cpu-2",
                            "name": "CPU-2",
                            "type": "cpu",
                            "temperature": 37.5,
                            "temperature_avg": 37.42,
                            "temperature_min": 37.0,
                            "temperature_max": 38.5
                        },
                        {
                            "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-1/dimm-env-stats",
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-1",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-13",
                            "name": "MEM-13",
                            "type": "memory",
                            "temperature": 31.0,
                            "temperature_avg": 31.75,
                            "temperature_min": 31.0,
                            "temperature_max": 32.0
                        },
                        {
                            "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-14/dimm-env-stats",
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-1",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-20",
                            "name": "MEM-20",
                            "type": "memory",
                            "temperature": 28.0,
                            "temperature_avg": 28.25,
                            "temperature_min": 28.0,
                            "temperature_max": 29.0
                        },
                        {
                            "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-22/dimm-env-stats",
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
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
                            "time_collected": "2022-12-08T11:04:22.939",
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
                        "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-2",
                            "cpu_rn": "cpu-2",
                            "name": "CPU-2",
                            "type": "cpu",
                            "temperature": 38.0,
                            "temperature_avg": 37.95,
                            "temperature_min": 37.5,
                            "temperature_max": 38.0
                        },
                        {
                            "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-1/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-2",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-13",
                            "name": "MEM-13",
                            "type": "memory",
                            "temperature": 30.0,
                            "temperature_avg": 29.87,
                            "temperature_min": 29.0,
                            "temperature_max": 30.0
                        },
                        {
                            "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-14/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-2",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-2",
                            "name": "MEM-2",
                            "type": "memory",
                            "temperature": 28.0,
                            "temperature_avg": 28.12,
                            "temperature_min": 28.0,
                            "temperature_max": 29.0
                        },
                        {
                            "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-20/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-2",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-23",
                            "name": "MEM-23",
                            "type": "memory",
                            "temperature": 32.0,
                            "temperature_avg": 31.75,
                            "temperature_min": 31.0,
                            "temperature_max": 32.0
                        },
                        {
                            "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-4/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
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
                            "time_collected": "2022-12-08T11:03:56.545",
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
                        "time_collected": "2022-12-08T11:03:58.817",
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
                            "time_collected": "2022-12-08T11:03:58.817",
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
                            "time_collected": "2022-12-08T11:03:58.817",
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
                            "time_collected": "2022-12-08T11:03:58.817",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-3",
                            "cpu_rn": "cpu-1",
                            "name": "CPU-1",
                            "type": "cpu",
                            "temperature": 37.5,
                            "temperature_avg": 37.5,
                            "temperature_min": 37.5,
                            "temperature_max": 37.5
                        },
                        {
                            "dn": "sys/chassis-1/blade-3/board/cpu-2/env-stats",
                            "time_collected": "2022-12-08T11:03:58.817",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-3",
                            "cpu_rn": "cpu-2",
                            "name": "CPU-2",
                            "type": "cpu",
                            "temperature": 41.0,
                            "temperature_avg": 40.75,
                            "temperature_min": 40.5,
                            "temperature_max": 41.0
                        },
                        {
                            "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-1/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:58.817",
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
                            "time_collected": "2022-12-08T11:03:58.817",
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
                            "time_collected": "2022-12-08T11:03:58.817",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-3",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-13",
                            "name": "MEM-13",
                            "type": "memory",
                            "temperature": 27.0,
                            "temperature_avg": 26.5,
                            "temperature_min": 26.0,
                            "temperature_max": 27.0
                        },
                        {
                            "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-16/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:58.817",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-3",
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
                            "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-19/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:58.817",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-3",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-19",
                            "name": "MEM-19",
                            "type": "memory",
                            "temperature": 25.0,
                            "temperature_avg": 24.5,
                            "temperature_min": 24.0,
                            "temperature_max": 25.0
                        },
                        {
                            "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-22/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:58.817",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-3",
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
                            "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-4/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:58.817",
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
                            "time_collected": "2022-12-08T11:03:58.817",
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
                        "HighestTemperature": 41.0,
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
                        "time_collected": "2022-12-08T11:04:17.553",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-4",
                        "consumed_power": 126.0,
                        "input_current": 10.52,
                        "input_voltage": 11.98,
                        "consumed_power_avg": 126.43,
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
                        "PowerAvg": 126.43,
                        "PowerMax": 132.0
                    }
                },
                "thermal": {
                    "Data": [
                        {
                            "dn": "sys/chassis-1/blade-4/board/temp-stats",
                            "time_collected": "2022-12-08T11:04:17.553",
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
                            "time_collected": "2022-12-08T11:04:17.553",
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
                            "time_collected": "2022-12-08T11:04:17.553",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-4",
                            "cpu_rn": "cpu-1",
                            "name": "CPU-1",
                            "type": "cpu",
                            "temperature": 38.0,
                            "temperature_avg": 38.22,
                            "temperature_min": 38.0,
                            "temperature_max": 39.0
                        },
                        {
                            "dn": "sys/chassis-1/blade-4/board/cpu-2/env-stats",
                            "time_collected": "2022-12-08T11:04:17.553",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-4",
                            "cpu_rn": "cpu-2",
                            "name": "CPU-2",
                            "type": "cpu",
                            "temperature": 41.0,
                            "temperature_avg": 41.17,
                            "temperature_min": 41.0,
                            "temperature_max": 42.0
                        },
                        {
                            "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-1/dimm-env-stats",
                            "time_collected": "2022-12-08T11:04:17.553",
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
                            "time_collected": "2022-12-08T11:04:17.553",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-4",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-10",
                            "name": "MEM-10",
                            "type": "memory",
                            "temperature": 29.0,
                            "temperature_avg": 28.87,
                            "temperature_min": 28.0,
                            "temperature_max": 29.0
                        },
                        {
                            "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-13/dimm-env-stats",
                            "time_collected": "2022-12-08T11:04:17.553",
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
                            "time_collected": "2022-12-08T11:04:17.553",
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
                            "time_collected": "2022-12-08T11:04:17.553",
                            "chassis_rn": "chassis-1",
                            "blade_rn": "blade-4",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-19",
                            "name": "MEM-19",
                            "type": "memory",
                            "temperature": 31.0,
                            "temperature_avg": 30.75,
                            "temperature_min": 30.0,
                            "temperature_max": 31.0
                        },
                        {
                            "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-22/dimm-env-stats",
                            "time_collected": "2022-12-08T11:04:17.553",
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
                            "time_collected": "2022-12-08T11:04:17.553",
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
                            "time_collected": "2022-12-08T11:04:17.553",
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
        ],
        "power_stats": {
            "Data": {
                "Chassis": {
                    "dn": "sys/chassis-1/stats",
                    "time_collected": "2022-12-08T11:04:11.015",
                    "chassis_rn": "chassis-1",
                    "input_power": 1128.0,
                    "output_power": 782.0,
                    "input_power_avg": 1122.0,
                    "output_power_avg": 839.5,
                    "input_power_min": 1104.0,
                    "output_power_min": 782.0,
                    "input_power_max": 1152.0,
                    "output_power_max": 897.0
                },
                "PSU": [
                    {
                        "dn": "sys/chassis-1/psu-1/stats",
                        "time_collected": "2022-12-08T11:04:11.014",
                        "chassis_rn": "chassis-1",
                        "psu_rn": "psu-1",
                        "psu_id": "1",
                        "name": "PSU 1",
                        "output_power": 348.23,
                        "output_power_avg": 355.74,
                        "output_power_min": 348.23,
                        "output_power_max": 360.24,
                        "output_current": 29.0,
                        "output_current_avg": 29.62,
                        "output_current_min": 29.0,
                        "output_current_max": 30.0
                    },
                    {
                        "dn": "sys/chassis-1/psu-2/stats",
                        "time_collected": "2022-12-08T11:04:11.015",
                        "chassis_rn": "chassis-1",
                        "psu_rn": "psu-2",
                        "psu_id": "2",
                        "name": "PSU 2",
                        "output_power": 357.87,
                        "output_power_avg": 368.31,
                        "output_power_min": 357.87,
                        "output_power_max": 381.73,
                        "output_current": 30.0,
                        "output_current_avg": 30.88,
                        "output_current_min": 30.0,
                        "output_current_max": 32.0
                    },
                    {
                        "dn": "sys/chassis-1/psu-3/stats",
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.015",
                        "chassis_rn": "chassis-1",
                        "psu_rn": "psu-4",
                        "psu_id": "4",
                        "name": "PSU 4",
                        "output_power": 83.5,
                        "output_power_avg": 93.94,
                        "output_power_min": 83.5,
                        "output_power_max": 131.22,
                        "output_current": 7.0,
                        "output_current_avg": 7.88,
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
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.015",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-2",
                        "fan_module_id": "2",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 2 - Fan 2",
                        "speed": "3520",
                        "speed_avg": "3513",
                        "speed_min": "3476",
                        "speed_max": "3520"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-3/fan-1/stats",
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.015",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-6",
                        "fan_module_id": "6",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 6 - Fan 2",
                        "speed": "3520",
                        "speed_avg": "3492",
                        "speed_min": "3476",
                        "speed_max": "3520"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-7/fan-1/stats",
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.015",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-8",
                        "fan_module_id": "8",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 8 - Fan 1",
                        "speed": "3344",
                        "speed_avg": "3331",
                        "speed_min": "3300",
                        "speed_max": "3344"
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-8/fan-2/stats",
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.014",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-1",
                        "fan_module_id": "1",
                        "name": "Fan Module 1",
                        "temperature": 33.0,
                        "temperature_avg": 33.25,
                        "temperature_min": 33.0,
                        "temperature_max": 34.0
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-2/stats",
                        "time_collected": "2022-12-08T11:04:11.014",
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
                        "time_collected": "2022-12-08T11:04:11.014",
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
                        "time_collected": "2022-12-08T11:04:11.014",
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
                        "time_collected": "2022-12-08T11:04:11.014",
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
                        "time_collected": "2022-12-08T11:04:11.014",
                        "chassis_rn": "chassis-1",
                        "fan_module_rn": "fan-module-1-6",
                        "fan_module_id": "6",
                        "name": "Fan Module 6",
                        "temperature": 29.0,
                        "temperature_avg": 28.12,
                        "temperature_min": 28.0,
                        "temperature_max": 29.0
                    },
                    {
                        "dn": "sys/chassis-1/fan-module-1-7/stats",
                        "time_collected": "2022-12-08T11:04:11.014",
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
                        "time_collected": "2022-12-08T11:04:11.014",
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
                        "time_collected": "2022-12-08T11:04:11.014",
                        "chassis_rn": "chassis-1",
                        "psu_rn": "psu-1",
                        "psu_id": "1",
                        "name": "PSU 1",
                        "temperature": 24.0,
                        "temperature_avg": 24.25,
                        "temperature_min": 24.0,
                        "temperature_max": 25.0
                    },
                    {
                        "dn": "sys/chassis-1/psu-2/stats",
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:11.015",
                        "chassis_rn": "chassis-1",
                        "psu_rn": "psu-3",
                        "psu_id": "3",
                        "name": "PSU 3",
                        "temperature": 25.0,
                        "temperature_avg": 24.75,
                        "temperature_min": 24.0,
                        "temperature_max": 25.0
                    },
                    {
                        "dn": "sys/chassis-1/psu-4/stats",
                        "time_collected": "2022-12-08T11:04:11.015",
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
                        "time_collected": "2022-12-08T11:04:03.264",
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
                        "time_collected": "2022-12-08T11:04:11.014",
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
                        "time_collected": "2022-12-08T11:04:03.264",
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
                        "time_collected": "2022-12-08T11:04:11.014",
                        "chassis_rn": "chassis-1",
                        "slot_rn": "slot-2",
                        "slot_id": "2",
                        "name": "IO Module 2 - ASIC",
                        "temperature": 66.0,
                        "temperature_avg": 66.0,
                        "temperature_min": 66.0,
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
        "blade": [
            {
                "mo_type": "blade",
                "association": "associated",
                "chassis_id": "2",
                "available_memory": "393216",
                "assigned_to_dn": "org-root/org-EU-SPN/ls-esx51-eu-spdc",
                "admin_state": "in-service",
                "dn": "sys/chassis-2/blade-1",
                "model": "UCSB-B200-M5",
                "num_of_adaptors": "2",
                "num_of_cores": "40",
                "num_of_cores_enabled": "40",
                "num_of_cpus": "2",
                "num_of_eth_host_ifs": "8",
                "num_of_fc_host_ifs": "0",
                "num_of_threads": "80",
                "oper_power": "on",
                "oper_state": "ok",
                "operability": "operable",
                "part_number": "68-5800-07",
                "rn": "blade-1",
                "serial": "FLM241501FB",
                "server_id": "2/1",
                "slot_id": "1",
                "total_memory": "393216",
                "uuid": "315220a5-2121-4e5b-0101-e1dc0000010f",
                "vendor": "Cisco Systems Inc",
                "id": "1",
                "chassis_rn": "chassis-2",
                "power": {
                    "Data": {
                        "dn": "sys/chassis-2/blade-1/board/power-stats",
                        "time_collected": "2022-12-08T11:03:44.269",
                        "chassis_rn": "chassis-2",
                        "blade_rn": "blade-1",
                        "consumed_power": 214.5,
                        "input_current": 17.73,
                        "input_voltage": 12.1,
                        "consumed_power_avg": 212.55,
                        "input_current_avg": 17.57,
                        "input_voltage_avg": 12.1,
                        "consumed_power_min": 210.6,
                        "input_current_min": 17.41,
                        "input_voltage_min": 12.1,
                        "consumed_power_max": 214.5,
                        "input_current_max": 17.73,
                        "input_voltage_max": 12.1
                    },
                    "Summary": {
                        "Source": "UCSM",
                        "PowerNow": 214.5,
                        "PowerMin": 210.6,
                        "PowerAvg": 212.55,
                        "PowerMax": 214.5
                    }
                },
                "thermal": {
                    "Data": [
                        {
                            "dn": "sys/chassis-2/blade-1/board/temp-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
                            "name": "Motherboard Front",
                            "type": "motherboard",
                            "temperature": 20.0,
                            "fm_temp_sen_rear": 33.0,
                            "temperature_avg": 20.0,
                            "fm_temp_sen_rear_avg": 33.0,
                            "temperature_min": 20.0,
                            "fm_temp_sen_rear_min": 33.0,
                            "temperature_max": 20.0,
                            "fm_temp_sen_rear_max": 33.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-1/board/temp-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
                            "name": "Motherboard Rear",
                            "type": "motherboard",
                            "temperature": 33.0,
                            "temperature_avg": 33.0,
                            "temperature_min": 33.0,
                            "temperature_max": 33.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-1/board/cpu-1/env-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
                            "cpu_rn": "cpu-1",
                            "name": "CPU-1",
                            "type": "cpu",
                            "temperature": 36.0,
                            "temperature_avg": 36.0,
                            "temperature_min": 36.0,
                            "temperature_max": 36.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-1/board/cpu-2/env-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
                            "cpu_rn": "cpu-2",
                            "name": "CPU-2",
                            "type": "cpu",
                            "temperature": 39.5,
                            "temperature_avg": 39.5,
                            "temperature_min": 39.5,
                            "temperature_max": 39.5
                        },
                        {
                            "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-1/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-1",
                            "name": "MEM-1",
                            "type": "memory",
                            "temperature": 27.0,
                            "temperature_avg": 27.0,
                            "temperature_min": 27.0,
                            "temperature_max": 27.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-11/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-11",
                            "name": "MEM-11",
                            "type": "memory",
                            "temperature": 29.0,
                            "temperature_avg": 29.0,
                            "temperature_min": 29.0,
                            "temperature_max": 29.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-13/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-13",
                            "name": "MEM-13",
                            "type": "memory",
                            "temperature": 30.0,
                            "temperature_avg": 30.0,
                            "temperature_min": 30.0,
                            "temperature_max": 30.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-15/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-15",
                            "name": "MEM-15",
                            "type": "memory",
                            "temperature": 28.0,
                            "temperature_avg": 28.0,
                            "temperature_min": 28.0,
                            "temperature_max": 28.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-17/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-17",
                            "name": "MEM-17",
                            "type": "memory",
                            "temperature": 29.0,
                            "temperature_avg": 29.0,
                            "temperature_min": 29.0,
                            "temperature_max": 29.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-19/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
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
                            "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-21/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-21",
                            "name": "MEM-21",
                            "type": "memory",
                            "temperature": 28.0,
                            "temperature_avg": 28.0,
                            "temperature_min": 28.0,
                            "temperature_max": 28.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-23/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-23",
                            "name": "MEM-23",
                            "type": "memory",
                            "temperature": 28.0,
                            "temperature_avg": 28.0,
                            "temperature_min": 28.0,
                            "temperature_max": 28.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-3/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-3",
                            "name": "MEM-3",
                            "type": "memory",
                            "temperature": 27.0,
                            "temperature_avg": 27.0,
                            "temperature_min": 27.0,
                            "temperature_max": 27.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-5/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
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
                            "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-7/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-7",
                            "name": "MEM-7",
                            "type": "memory",
                            "temperature": 26.0,
                            "temperature_avg": 26.0,
                            "temperature_min": 26.0,
                            "temperature_max": 26.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-9/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:44.269",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-1",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-9",
                            "name": "MEM-9",
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
                        "HighestTemperature": 39.5,
                        "SmallestGap": "N/A",
                        "OverThreshold": "N/A"
                    }
                }
            },
            {
                "mo_type": "blade",
                "association": "associated",
                "chassis_id": "2",
                "available_memory": "393216",
                "assigned_to_dn": "org-root/org-EU-SPN/ls-esx52-eu-spdc",
                "admin_state": "in-service",
                "dn": "sys/chassis-2/blade-2",
                "model": "UCSB-B200-M5",
                "num_of_adaptors": "2",
                "num_of_cores": "40",
                "num_of_cores_enabled": "40",
                "num_of_cpus": "2",
                "num_of_eth_host_ifs": "8",
                "num_of_fc_host_ifs": "0",
                "num_of_threads": "80",
                "oper_power": "on",
                "oper_state": "ok",
                "operability": "operable",
                "part_number": "68-5800-07",
                "rn": "blade-2",
                "serial": "FLM24140BJB",
                "server_id": "2/2",
                "slot_id": "2",
                "total_memory": "393216",
                "uuid": "315220a5-2121-4e5b-0101-e1dc0000011f",
                "vendor": "Cisco Systems Inc",
                "id": "2",
                "chassis_rn": "chassis-2",
                "power": {
                    "Data": {
                        "dn": "sys/chassis-2/blade-2/board/power-stats",
                        "time_collected": "2022-12-08T11:03:59.354",
                        "chassis_rn": "chassis-2",
                        "blade_rn": "blade-2",
                        "consumed_power": 241.8,
                        "input_current": 19.89,
                        "input_voltage": 12.15,
                        "consumed_power_avg": 244.14,
                        "input_current_avg": 20.09,
                        "input_voltage_avg": 12.15,
                        "consumed_power_min": 241.8,
                        "input_current_min": 19.89,
                        "input_voltage_min": 12.15,
                        "consumed_power_max": 253.5,
                        "input_current_max": 20.86,
                        "input_voltage_max": 12.15
                    },
                    "Summary": {
                        "Source": "UCSM",
                        "PowerNow": 241.8,
                        "PowerMin": 241.8,
                        "PowerAvg": 244.14,
                        "PowerMax": 253.5
                    }
                },
                "thermal": {
                    "Data": [
                        {
                            "dn": "sys/chassis-2/blade-2/board/temp-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "name": "Motherboard Front",
                            "type": "motherboard",
                            "temperature": 21.0,
                            "fm_temp_sen_rear": 37.0,
                            "temperature_avg": 21.0,
                            "fm_temp_sen_rear_avg": 37.33,
                            "temperature_min": 21.0,
                            "fm_temp_sen_rear_min": 37.0,
                            "temperature_max": 21.0,
                            "fm_temp_sen_rear_max": 38.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-2/board/temp-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "name": "Motherboard Rear",
                            "type": "motherboard",
                            "temperature": 37.0,
                            "temperature_avg": 37.33,
                            "temperature_min": 37.0,
                            "temperature_max": 38.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-2/board/cpu-1/env-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "cpu_rn": "cpu-1",
                            "name": "CPU-1",
                            "type": "cpu",
                            "temperature": 42.5,
                            "temperature_avg": 42.5,
                            "temperature_min": 42.5,
                            "temperature_max": 42.5
                        },
                        {
                            "dn": "sys/chassis-2/blade-2/board/cpu-2/env-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "cpu_rn": "cpu-2",
                            "name": "CPU-2",
                            "type": "cpu",
                            "temperature": 48.5,
                            "temperature_avg": 48.62,
                            "temperature_min": 48.5,
                            "temperature_max": 49.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-1/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-1",
                            "name": "MEM-1",
                            "type": "memory",
                            "temperature": 30.0,
                            "temperature_avg": 30.0,
                            "temperature_min": 30.0,
                            "temperature_max": 30.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-11/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-11",
                            "name": "MEM-11",
                            "type": "memory",
                            "temperature": 29.0,
                            "temperature_avg": 29.0,
                            "temperature_min": 29.0,
                            "temperature_max": 29.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-13/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-13",
                            "name": "MEM-13",
                            "type": "memory",
                            "temperature": 33.0,
                            "temperature_avg": 33.0,
                            "temperature_min": 33.0,
                            "temperature_max": 33.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-15/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-15",
                            "name": "MEM-15",
                            "type": "memory",
                            "temperature": 31.0,
                            "temperature_avg": 31.0,
                            "temperature_min": 31.0,
                            "temperature_max": 31.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-17/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-17",
                            "name": "MEM-17",
                            "type": "memory",
                            "temperature": 30.0,
                            "temperature_avg": 30.0,
                            "temperature_min": 30.0,
                            "temperature_max": 30.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-19/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-19",
                            "name": "MEM-19",
                            "type": "memory",
                            "temperature": 34.0,
                            "temperature_avg": 34.0,
                            "temperature_min": 34.0,
                            "temperature_max": 34.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-21/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-21",
                            "name": "MEM-21",
                            "type": "memory",
                            "temperature": 32.0,
                            "temperature_avg": 32.0,
                            "temperature_min": 32.0,
                            "temperature_max": 32.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-23/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-23",
                            "name": "MEM-23",
                            "type": "memory",
                            "temperature": 31.0,
                            "temperature_avg": 31.0,
                            "temperature_min": 31.0,
                            "temperature_max": 31.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-3/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-3",
                            "name": "MEM-3",
                            "type": "memory",
                            "temperature": 30.0,
                            "temperature_avg": 30.0,
                            "temperature_min": 30.0,
                            "temperature_max": 30.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-5/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-5",
                            "name": "MEM-5",
                            "type": "memory",
                            "temperature": 31.0,
                            "temperature_avg": 31.0,
                            "temperature_min": 31.0,
                            "temperature_max": 31.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-7/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
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
                            "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-9/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:59.354",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-2",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-9",
                            "name": "MEM-9",
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
                        "HighestTemperature": 48.5,
                        "SmallestGap": "N/A",
                        "OverThreshold": "N/A"
                    }
                }
            },
            {
                "mo_type": "blade",
                "association": "associated",
                "chassis_id": "2",
                "available_memory": "196608",
                "assigned_to_dn": "org-root/org-EU-SPN/ls-esx53-eu-spdc",
                "admin_state": "in-service",
                "dn": "sys/chassis-2/blade-3",
                "model": "UCSB-B200-M5",
                "num_of_adaptors": "2",
                "num_of_cores": "40",
                "num_of_cores_enabled": "40",
                "num_of_cpus": "2",
                "num_of_eth_host_ifs": "8",
                "num_of_fc_host_ifs": "0",
                "num_of_threads": "80",
                "oper_power": "on",
                "oper_state": "ok",
                "operability": "operable",
                "part_number": "68-5800-07",
                "rn": "blade-3",
                "serial": "FLM241501CT",
                "server_id": "2/3",
                "slot_id": "3",
                "total_memory": "196608",
                "uuid": "315220a5-2121-4e5b-0101-e1dc0000014e",
                "vendor": "Cisco Systems Inc",
                "id": "3",
                "chassis_rn": "chassis-2",
                "power": {
                    "Data": {
                        "dn": "sys/chassis-2/blade-3/board/power-stats",
                        "time_collected": "2022-12-08T11:03:55.370",
                        "chassis_rn": "chassis-2",
                        "blade_rn": "blade-3",
                        "consumed_power": 195.0,
                        "input_current": 16.12,
                        "input_voltage": 12.1,
                        "consumed_power_avg": 195.0,
                        "input_current_avg": 16.12,
                        "input_voltage_avg": 12.1,
                        "consumed_power_min": 195.0,
                        "input_current_min": 16.12,
                        "input_voltage_min": 12.1,
                        "consumed_power_max": 195.0,
                        "input_current_max": 16.12,
                        "input_voltage_max": 12.1
                    },
                    "Summary": {
                        "Source": "UCSM",
                        "PowerNow": 195.0,
                        "PowerMin": 195.0,
                        "PowerAvg": 195.0,
                        "PowerMax": 195.0
                    }
                },
                "thermal": {
                    "Data": [
                        {
                            "dn": "sys/chassis-2/blade-3/board/temp-stats",
                            "time_collected": "2022-12-08T11:03:55.370",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-3",
                            "name": "Motherboard Front",
                            "type": "motherboard",
                            "temperature": 20.0,
                            "fm_temp_sen_rear": 32.0,
                            "temperature_avg": 20.0,
                            "fm_temp_sen_rear_avg": 32.0,
                            "temperature_min": 20.0,
                            "fm_temp_sen_rear_min": 32.0,
                            "temperature_max": 20.0,
                            "fm_temp_sen_rear_max": 32.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-3/board/temp-stats",
                            "time_collected": "2022-12-08T11:03:55.370",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-3",
                            "name": "Motherboard Rear",
                            "type": "motherboard",
                            "temperature": 32.0,
                            "temperature_avg": 32.0,
                            "temperature_min": 32.0,
                            "temperature_max": 32.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-3/board/cpu-2/env-stats",
                            "time_collected": "2022-12-08T11:03:55.370",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-3",
                            "cpu_rn": "cpu-2",
                            "name": "CPU-2",
                            "type": "cpu",
                            "temperature": 36.5,
                            "temperature_avg": 36.38,
                            "temperature_min": 36.0,
                            "temperature_max": 36.5
                        },
                        {
                            "dn": "sys/chassis-2/blade-3/board/cpu-1/env-stats",
                            "time_collected": "2022-12-08T11:03:55.370",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-3",
                            "cpu_rn": "cpu-1",
                            "name": "CPU-1",
                            "type": "cpu",
                            "temperature": 37.0,
                            "temperature_avg": 37.12,
                            "temperature_min": 37.0,
                            "temperature_max": 37.5
                        },
                        {
                            "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-1/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:55.370",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-3",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-1",
                            "name": "MEM-1",
                            "type": "memory",
                            "temperature": 27.0,
                            "temperature_avg": 27.0,
                            "temperature_min": 27.0,
                            "temperature_max": 27.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-13/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:55.370",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-3",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-13",
                            "name": "MEM-13",
                            "type": "memory",
                            "temperature": 29.0,
                            "temperature_avg": 29.0,
                            "temperature_min": 29.0,
                            "temperature_max": 29.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-15/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:55.370",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-3",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-15",
                            "name": "MEM-15",
                            "type": "memory",
                            "temperature": 28.0,
                            "temperature_avg": 28.0,
                            "temperature_min": 28.0,
                            "temperature_max": 28.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-17/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:55.370",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-3",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-17",
                            "name": "MEM-17",
                            "type": "memory",
                            "temperature": 27.0,
                            "temperature_avg": 27.0,
                            "temperature_min": 27.0,
                            "temperature_max": 27.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-3/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:55.370",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-3",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-3",
                            "name": "MEM-3",
                            "type": "memory",
                            "temperature": 27.0,
                            "temperature_avg": 27.0,
                            "temperature_min": 27.0,
                            "temperature_max": 27.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-5/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:55.370",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-3",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-5",
                            "name": "MEM-5",
                            "type": "memory",
                            "temperature": 27.0,
                            "temperature_avg": 27.0,
                            "temperature_min": 27.0,
                            "temperature_max": 27.0
                        }
                    ],
                    "Summary": {
                        "Source": "UCSM",
                        "FanHealth": "N/A",
                        "SensorHealth": true,
                        "HighestTemperature": 37.0,
                        "SmallestGap": "N/A",
                        "OverThreshold": "N/A"
                    }
                }
            },
            {
                "mo_type": "blade",
                "association": "associated",
                "chassis_id": "2",
                "available_memory": "196608",
                "assigned_to_dn": "org-root/org-EU-SPN/ls-esx54-eu-spdc",
                "admin_state": "in-service",
                "dn": "sys/chassis-2/blade-4",
                "model": "UCSB-B200-M5",
                "num_of_adaptors": "2",
                "num_of_cores": "40",
                "num_of_cores_enabled": "40",
                "num_of_cpus": "2",
                "num_of_eth_host_ifs": "8",
                "num_of_fc_host_ifs": "0",
                "num_of_threads": "80",
                "oper_power": "on",
                "oper_state": "ok",
                "operability": "operable",
                "part_number": "68-5800-07",
                "rn": "blade-4",
                "serial": "FLM24140B0B",
                "server_id": "2/4",
                "slot_id": "4",
                "total_memory": "196608",
                "uuid": "315220a5-2121-4e5b-0101-e1dc0000015e",
                "vendor": "Cisco Systems Inc",
                "id": "4",
                "chassis_rn": "chassis-2",
                "power": {
                    "Data": {
                        "dn": "sys/chassis-2/blade-4/board/power-stats",
                        "time_collected": "2022-12-08T11:03:52.268",
                        "chassis_rn": "chassis-2",
                        "blade_rn": "blade-4",
                        "consumed_power": 234.0,
                        "input_current": 19.35,
                        "input_voltage": 12.1,
                        "consumed_power_avg": 239.85,
                        "input_current_avg": 19.83,
                        "input_voltage_avg": 12.1,
                        "consumed_power_min": 234.0,
                        "input_current_min": 19.35,
                        "input_voltage_min": 12.1,
                        "consumed_power_max": 245.7,
                        "input_current_max": 20.31,
                        "input_voltage_max": 12.1
                    },
                    "Summary": {
                        "Source": "UCSM",
                        "PowerNow": 234.0,
                        "PowerMin": 234.0,
                        "PowerAvg": 239.85,
                        "PowerMax": 245.7
                    }
                },
                "thermal": {
                    "Data": [
                        {
                            "dn": "sys/chassis-2/blade-4/board/temp-stats",
                            "time_collected": "2022-12-08T11:03:52.268",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-4",
                            "name": "Motherboard Front",
                            "type": "motherboard",
                            "temperature": 21.0,
                            "fm_temp_sen_rear": 38.0,
                            "temperature_avg": 21.67,
                            "fm_temp_sen_rear_avg": 38.0,
                            "temperature_min": 21.0,
                            "fm_temp_sen_rear_min": 38.0,
                            "temperature_max": 22.0,
                            "fm_temp_sen_rear_max": 38.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-4/board/temp-stats",
                            "time_collected": "2022-12-08T11:03:52.268",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-4",
                            "name": "Motherboard Rear",
                            "type": "motherboard",
                            "temperature": 38.0,
                            "temperature_avg": 38.0,
                            "temperature_min": 38.0,
                            "temperature_max": 38.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-4/board/cpu-2/env-stats",
                            "time_collected": "2022-12-08T11:03:52.268",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-4",
                            "cpu_rn": "cpu-2",
                            "name": "CPU-2",
                            "type": "cpu",
                            "temperature": 49.0,
                            "temperature_avg": 49.17,
                            "temperature_min": 48.5,
                            "temperature_max": 50.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-4/board/cpu-1/env-stats",
                            "time_collected": "2022-12-08T11:03:52.268",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-4",
                            "cpu_rn": "cpu-1",
                            "name": "CPU-1",
                            "type": "cpu",
                            "temperature": 42.5,
                            "temperature_avg": 41.58,
                            "temperature_min": 40.5,
                            "temperature_max": 42.5
                        },
                        {
                            "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-1/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:52.268",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-4",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-1",
                            "name": "MEM-1",
                            "type": "memory",
                            "temperature": 31.0,
                            "temperature_avg": 30.33,
                            "temperature_min": 30.0,
                            "temperature_max": 31.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-13/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:52.268",
                            "chassis_rn": "chassis-2",
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
                            "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-15/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:52.268",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-4",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-15",
                            "name": "MEM-15",
                            "type": "memory",
                            "temperature": 30.0,
                            "temperature_avg": 30.0,
                            "temperature_min": 30.0,
                            "temperature_max": 30.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-17/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:52.268",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-4",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-17",
                            "name": "MEM-17",
                            "type": "memory",
                            "temperature": 29.0,
                            "temperature_avg": 29.0,
                            "temperature_min": 29.0,
                            "temperature_max": 29.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-3/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:52.268",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-4",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-3",
                            "name": "MEM-3",
                            "type": "memory",
                            "temperature": 30.0,
                            "temperature_avg": 30.0,
                            "temperature_min": 30.0,
                            "temperature_max": 30.0
                        },
                        {
                            "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-5/dimm-env-stats",
                            "time_collected": "2022-12-08T11:03:52.268",
                            "chassis_rn": "chassis-2",
                            "blade_rn": "blade-4",
                            "array_rn": "memarray-1",
                            "dimm_rn": "mem-5",
                            "name": "MEM-5",
                            "type": "memory",
                            "temperature": 31.0,
                            "temperature_avg": 30.33,
                            "temperature_min": 30.0,
                            "temperature_max": 31.0
                        }
                    ],
                    "Summary": {
                        "Source": "UCSM",
                        "FanHealth": "N/A",
                        "SensorHealth": true,
                        "HighestTemperature": 49.0,
                        "SmallestGap": "N/A",
                        "OverThreshold": "N/A"
                    }
                }
            }
        ],
        "power_stats": {
            "Data": {
                "Chassis": {
                    "dn": "sys/chassis-2/stats",
                    "time_collected": "2022-12-08T11:04:16.423",
                    "chassis_rn": "chassis-2",
                    "input_power": 1416.0,
                    "output_power": 1196.0,
                    "input_power_avg": 1440.0,
                    "output_power_avg": 1199.29,
                    "input_power_min": 1416.0,
                    "output_power_min": 1058.0,
                    "input_power_max": 1488.0,
                    "output_power_max": 1288.0
                },
                "PSU": [
                    {
                        "dn": "sys/chassis-2/psu-1/stats",
                        "time_collected": "2022-12-08T11:04:16.422",
                        "chassis_rn": "chassis-2",
                        "psu_rn": "psu-1",
                        "psu_id": "1",
                        "name": "PSU 1",
                        "output_power": 226.65,
                        "output_power_avg": 258.38,
                        "output_power_min": 226.65,
                        "output_power_max": 324.22,
                        "output_current": 19.0,
                        "output_current_avg": 21.57,
                        "output_current_min": 19.0,
                        "output_current_max": 27.0
                    },
                    {
                        "dn": "sys/chassis-2/psu-2/stats",
                        "time_collected": "2022-12-08T11:04:16.422",
                        "chassis_rn": "chassis-2",
                        "psu_rn": "psu-2",
                        "psu_id": "2",
                        "name": "PSU 2",
                        "output_power": 310.15,
                        "output_power_avg": 320.49,
                        "output_power_min": 310.15,
                        "output_power_max": 336.22,
                        "output_current": 26.0,
                        "output_current_avg": 26.71,
                        "output_current_min": 26.0,
                        "output_current_max": 28.0
                    },
                    {
                        "dn": "sys/chassis-2/psu-3/stats",
                        "time_collected": "2022-12-08T11:04:16.422",
                        "chassis_rn": "chassis-2",
                        "psu_rn": "psu-3",
                        "psu_id": "3",
                        "name": "PSU 3",
                        "output_power": 429.44,
                        "output_power_avg": 394.84,
                        "output_power_min": 248.85,
                        "output_power_max": 462.15,
                        "output_current": 36.0,
                        "output_current_avg": 33.29,
                        "output_current_min": 21.0,
                        "output_current_max": 39.0
                    },
                    {
                        "dn": "sys/chassis-2/psu-4/stats",
                        "time_collected": "2022-12-08T11:04:16.422",
                        "chassis_rn": "chassis-2",
                        "psu_rn": "psu-4",
                        "psu_id": "4",
                        "name": "PSU 4",
                        "output_power": 226.65,
                        "output_power_avg": 223.67,
                        "output_power_min": 202.79,
                        "output_power_max": 238.58,
                        "output_current": 19.0,
                        "output_current_avg": 18.71,
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
                        "time_collected": "2022-12-08T11:04:16.423",
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
                        "time_collected": "2022-12-08T11:04:16.423",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-1",
                        "fan_module_id": "1",
                        "fan_rn": "fan-2",
                        "fan_id": "2",
                        "name": "Fan Module 1 - Fan 2",
                        "speed": "4840",
                        "speed_avg": "4839",
                        "speed_min": "4840",
                        "speed_max": "4840"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-2/fan-1/stats",
                        "time_collected": "2022-12-08T11:04:16.423",
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
                        "time_collected": "2022-12-08T11:04:16.423",
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
                        "time_collected": "2022-12-08T11:04:16.423",
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
                        "time_collected": "2022-12-08T11:04:16.423",
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
                        "time_collected": "2022-12-08T11:04:16.423",
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
                        "time_collected": "2022-12-08T11:04:16.423",
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
                        "time_collected": "2022-12-08T11:04:16.423",
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
                        "time_collected": "2022-12-08T11:04:16.423",
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
                        "time_collected": "2022-12-08T11:04:16.423",
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
                        "time_collected": "2022-12-08T11:04:16.423",
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
                        "time_collected": "2022-12-08T11:04:16.423",
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
                        "time_collected": "2022-12-08T11:04:16.423",
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
                        "time_collected": "2022-12-08T11:04:16.423",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-8",
                        "fan_module_id": "8",
                        "fan_rn": "fan-1",
                        "fan_id": "1",
                        "name": "Fan Module 8 - Fan 1",
                        "speed": "4620",
                        "speed_avg": "4593",
                        "speed_min": "4576",
                        "speed_max": "4620"
                    },
                    {
                        "dn": "sys/chassis-2/fan-module-1-8/fan-2/stats",
                        "time_collected": "2022-12-08T11:04:16.423",
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
                        "time_collected": "2022-12-08T11:04:16.422",
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
                        "time_collected": "2022-12-08T11:04:16.422",
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
                        "time_collected": "2022-12-08T11:04:16.422",
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
                        "time_collected": "2022-12-08T11:04:16.422",
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
                        "time_collected": "2022-12-08T11:04:16.422",
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
                        "time_collected": "2022-12-08T11:04:16.422",
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
                        "time_collected": "2022-12-08T11:04:16.422",
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
                        "time_collected": "2022-12-08T11:04:16.422",
                        "chassis_rn": "chassis-2",
                        "fan_module_rn": "fan-module-1-8",
                        "fan_module_id": "8",
                        "name": "Fan Module 8",
                        "temperature": 27.0,
                        "temperature_avg": 26.43,
                        "temperature_min": 26.0,
                        "temperature_max": 27.0
                    },
                    {
                        "dn": "sys/chassis-2/psu-1/stats",
                        "time_collected": "2022-12-08T11:04:16.422",
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
                        "time_collected": "2022-12-08T11:04:16.422",
                        "chassis_rn": "chassis-2",
                        "psu_rn": "psu-2",
                        "psu_id": "2",
                        "name": "PSU 2",
                        "temperature": 19.0,
                        "temperature_avg": 19.14,
                        "temperature_min": 19.0,
                        "temperature_max": 20.0
                    },
                    {
                        "dn": "sys/chassis-2/psu-3/stats",
                        "time_collected": "2022-12-08T11:04:16.422",
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
                        "time_collected": "2022-12-08T11:04:16.422",
                        "chassis_rn": "chassis-2",
                        "psu_rn": "psu-4",
                        "psu_id": "4",
                        "name": "PSU 4",
                        "temperature": 21.0,
                        "temperature_avg": 21.14,
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
                        "time_collected": "2022-12-08T11:04:16.422",
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
                        "time_collected": "2022-12-08T11:04:16.422",
                        "chassis_rn": "chassis-2",
                        "slot_rn": "slot-2",
                        "slot_id": "2",
                        "name": "IO Module 2 - ASIC",
                        "temperature": 50.0,
                        "temperature_avg": 50.13,
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
# iserver get ucsm chassiz --manager milan --blade --env

Developer output

{
    "duration": 7929,
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
        "connect_time": 2065,
        "disconnect_time": 0,
        "mo_time": 5388,
        "total_time": 7453
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

2022-12-08 11:04:36.610684	True	1594	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 11:04:37.257339	True	644	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 11:04:37.781185	True	522	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 11:04:38.206596	True	423	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 11:04:38.669506	True	461	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 11:04:39.171804	True	501	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 11:04:39.741088	True	568	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 11:04:40.232736	True	478	vip-ucsb1.emea-sp.cisco.com:equipmentChassisStats
2022-12-08 11:04:40.705823	True	472	vip-ucsb1.emea-sp.cisco.com:EquipmentPsuStats
2022-12-08 11:04:41.158269	True	450	vip-ucsb1.emea-sp.cisco.com:EquipmentFanStats
2022-12-08 11:04:41.596235	True	436	vip-ucsb1.emea-sp.cisco.com:EquipmentFanModuleStats
2022-12-08 11:04:42.030126	True	433	vip-ucsb1.emea-sp.cisco.com:EquipmentIOCardStats
2022-12-08 11:04:42.890998	True	471	disconnect vip-ucsb1.emea-sp.cisco.com
```
