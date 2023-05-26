# Get Chassis and Blades with Power Information

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --blade --power

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

+-------+------------------+--------+--------+--------+--------------------+------+-------+------+
| PSU   | Output Power (W) | Min    | Avg    | Max    | Output Current (A) | Min  | Avg   | Max  |
+-------+------------------+--------+--------+--------+--------------------+------+-------+------+
| PSU 1 | 360.24           | 348.23 | 356.24 | 360.24 | 30.0               | 29.0 | 29.67 | 30.0 | 
| PSU 2 | 381.73           | 357.87 | 367.81 | 381.73 | 32.0               | 30.0 | 30.83 | 32.0 | 
| PSU 3 | 0.0              | 0.0    | 0.0    | 0.0    | 0.0                | 0.0  | 0.0   | 0.0  | 
| PSU 4 | 95.43            | 83.5   | 89.47  | 95.43  | 8.0                | 7.0  | 7.5   | 8.0  | 
+-------+------------------+--------+--------+--------+--------------------+------+-------+------+

+---------+--------------+-------------+---------------+-------------+-------------+-------------+
| Blade   | Model        | Serial      | Overal Status | Operability | Power State | Assoc State |
+---------+--------------+-------------+---------------+-------------+-------------+-------------+
| blade-1 | UCSB-B200-M4 | FCH205371PZ | ok            | operable    | on          | associated  | 
| blade-2 | UCSB-B200-M4 | FCH20527XXD | ok            | operable    | on          | associated  | 
| blade-3 | UCSB-B200-M4 | FCH20437VXH | ok            | operable    | on          | associated  | 
| blade-4 | UCSB-B200-M4 | FCH205371UU | ok            | operable    | on          | associated  | 
+---------+--------------+-------------+---------------+-------------+-------------+-------------+

+-----------+---------+-------+-------+--------+-------+---------+-------+-------+-------+---------+-------+-------+-------+
| Chassis   | Name    | Power | Min   | Avg    | Max   | Current | Min   | Avg   | Max   | Voltage | Min   | Avg   | Max   |
+-----------+---------+-------+-------+--------+-------+---------+-------+-------+-------+---------+-------+-------+-------+
| chassis-1 | blade-1 | 144.0 | 138.0 | 140.0  | 144.0 | 11.96   | 11.47 | 11.63 | 11.96 | 12.04   | 12.04 | 12.04 | 12.04 | 
| chassis-1 | blade-2 | 138.0 | 138.0 | 138.0  | 138.0 | 11.52   | 11.52 | 11.52 | 11.52 | 11.98   | 11.98 | 11.98 | 11.98 | 
| chassis-1 | blade-3 | 126.0 | 126.0 | 126.0  | 126.0 | 10.52   | 10.52 | 10.52 | 10.52 | 11.98   | 11.98 | 11.98 | 11.98 | 
| chassis-1 | blade-4 | 126.0 | 126.0 | 126.55 | 132.0 | 10.52   | 10.52 | 10.57 | 11.02 | 11.98   | 11.98 | 11.98 | 11.98 | 
+-----------+---------+-------+-------+--------+-------+---------+-------+-------+-------+---------+-------+-------+-------+
```

JSON Output

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --blade --power

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
                    "time_collected": "2022-12-08T11:01:22.888",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "consumed_power": 144.0,
                    "input_current": 11.96,
                    "input_voltage": 12.04,
                    "consumed_power_avg": 140.0,
                    "input_current_avg": 11.63,
                    "input_voltage_avg": 12.04,
                    "consumed_power_min": 138.0,
                    "input_current_min": 11.47,
                    "input_voltage_min": 12.04,
                    "consumed_power_max": 144.0,
                    "input_current_max": 11.96,
                    "input_voltage_max": 12.04
                },
                "Summary": {
                    "Source": "UCSM",
                    "PowerNow": 144.0,
                    "PowerMin": 138.0,
                    "PowerAvg": 140.0,
                    "PowerMax": 144.0
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
                    "time_collected": "2022-12-08T11:01:17.586",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "consumed_power": 126.0,
                    "input_current": 10.52,
                    "input_voltage": 11.98,
                    "consumed_power_avg": 126.55,
                    "input_current_avg": 10.57,
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
                    "PowerAvg": 126.55,
                    "PowerMax": 132.0
                }
            }
        }
    ]
}
```

Developer Output

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --blade --power

Developer output

{
    "duration": 6636,
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
        "connect_time": 2473,
        "disconnect_time": 0,
        "mo_time": 3367,
        "total_time": 5840
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

2022-12-08 11:02:10.136103	True	1932	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 11:02:10.926624	True	765	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 11:02:11.497280	True	547	vip-ucsb1.emea-sp.cisco.com:equipmentChassisStats
2022-12-08 11:02:12.154179	True	631	vip-ucsb1.emea-sp.cisco.com:EquipmentPsuStats
2022-12-08 11:02:12.942864	True	784	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 11:02:13.659862	True	640	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 11:02:14.735060	True	541	disconnect vip-ucsb1.emea-sp.cisco.com
```
