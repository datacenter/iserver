# Get Chassis' and Blades with Power Information

```
# iserver get ucsm chassiz --manager milan --blade --power

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
| chassis-2 | 1440.0          | 1416.0 | 1444.0 | 1488.0 | 1150.0           | 1058.0 | 1199.83 | 1288.0 | 
+-----------+-----------------+--------+--------+--------+------------------+--------+---------+--------+

+-----------+-------+------------------+--------+--------+--------+--------------------+------+-------+------+
| Chassis   | PSU   | Output Power (W) | Min    | Avg    | Max    | Output Current (A) | Min  | Avg   | Max  |
+-----------+-------+------------------+--------+--------+--------+--------------------+------+-------+------+
| chassis-1 | PSU 1 | 348.23           | 348.23 | 355.74 | 360.24 | 29.0               | 29.0 | 29.62 | 30.0 | 
| chassis-1 | PSU 2 | 357.87           | 357.87 | 368.31 | 381.73 | 30.0               | 30.0 | 30.88 | 32.0 | 
| chassis-1 | PSU 3 | 0.0              | 0.0    | 0.0    | 0.0    | 0.0                | 0.0  | 0.0   | 0.0  | 
| chassis-1 | PSU 4 | 83.5             | 83.5   | 93.94  | 131.22 | 7.0                | 7.0  | 7.88  | 11.0 | 
| chassis-2 | PSU 1 | 264.18           | 226.65 | 263.66 | 324.22 | 22.0               | 19.0 | 22.0  | 27.0 | 
| chassis-2 | PSU 2 | 312.21           | 312.21 | 322.21 | 336.22 | 26.0               | 26.0 | 26.83 | 28.0 | 
| chassis-2 | PSU 3 | 343.65           | 248.85 | 389.08 | 462.15 | 29.0               | 21.0 | 32.83 | 39.0 | 
| chassis-2 | PSU 4 | 228.15           | 202.79 | 223.18 | 238.58 | 19.0               | 17.0 | 18.67 | 20.0 | 
+-----------+-------+------------------+--------+--------+--------+--------------------+------+-------+------+

+-----------+---------+-------+-------+--------+-------+---------+-------+-------+-------+---------+-------+-------+-------+
| Chassis   | Name    | Power | Min   | Avg    | Max   | Current | Min   | Avg   | Max   | Voltage | Min   | Avg   | Max   |
+-----------+---------+-------+-------+--------+-------+---------+-------+-------+-------+---------+-------+-------+-------+
| chassis-1 | blade-1 | 138.0 | 138.0 | 138.0  | 138.0 | 11.47   | 11.47 | 11.47 | 11.47 | 12.04   | 12.04 | 12.04 | 12.04 | 
| chassis-1 | blade-2 | 138.0 | 138.0 | 138.0  | 138.0 | 11.52   | 11.52 | 11.52 | 11.52 | 11.98   | 11.98 | 11.98 | 11.98 | 
| chassis-1 | blade-3 | 126.0 | 126.0 | 126.0  | 126.0 | 10.52   | 10.52 | 10.52 | 10.52 | 11.98   | 11.98 | 11.98 | 11.98 | 
| chassis-1 | blade-4 | 126.0 | 126.0 | 126.46 | 132.0 | 10.52   | 10.52 | 10.56 | 11.02 | 11.98   | 11.98 | 11.98 | 11.98 | 
| chassis-2 | blade-1 | 214.5 | 210.6 | 212.55 | 214.5 | 17.73   | 17.41 | 17.57 | 17.73 | 12.1    | 12.1  | 12.1  | 12.1  | 
| chassis-2 | blade-2 | 241.8 | 241.8 | 244.14 | 253.5 | 19.89   | 19.89 | 20.09 | 20.86 | 12.15   | 12.15 | 12.15 | 12.15 | 
| chassis-2 | blade-3 | 195.0 | 195.0 | 195.0  | 195.0 | 16.12   | 16.12 | 16.12 | 16.12 | 12.1    | 12.1  | 12.1  | 12.1  | 
| chassis-2 | blade-4 | 234.0 | 234.0 | 239.85 | 245.7 | 19.35   | 19.35 | 19.83 | 20.31 | 12.1    | 12.1  | 12.1  | 12.1  | 
+-----------+---------+-------+-------+--------+-------+---------+-------+-------+-------+---------+-------+-------+-------+
```

JSON Output

```
# iserver get ucsm chassiz --manager milan --blade --power

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
                        "time_collected": "2022-12-08T11:03:23.663",
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
                        "time_collected": "2022-12-08T11:03:17.395",
                        "chassis_rn": "chassis-1",
                        "blade_rn": "blade-4",
                        "consumed_power": 126.0,
                        "input_current": 10.52,
                        "input_voltage": 11.98,
                        "consumed_power_avg": 126.46,
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
                        "PowerAvg": 126.46,
                        "PowerMax": 132.0
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
                }
            }
        ],
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
# iserver get ucsm chassiz --manager milan --blade --power

Developer output

{
    "duration": 4975,
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
        "success": 7,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 2212,
        "disconnect_time": 0,
        "mo_time": 2608,
        "total_time": 4820
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

2022-12-08 11:04:12.256413	True	1761	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 11:04:13.028382	True	769	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 11:04:13.563085	True	530	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 11:04:14.013052	True	447	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 11:04:14.438040	True	421	vip-ucsb1.emea-sp.cisco.com:equipmentChassisStats
2022-12-08 11:04:14.881105	True	441	vip-ucsb1.emea-sp.cisco.com:EquipmentPsuStats
2022-12-08 11:04:15.434226	True	451	disconnect vip-ucsb1.emea-sp.cisco.com
```
