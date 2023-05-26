# Get Blades with Power Information

```
# iserver get ucsm blades --manager milan --chassis-id 1 --power

+-----------+---------+--------------+-------------+---------------+-------------+-------------+-------------+
| Chassis   | Blade   | Model        | Serial      | Overal Status | Operability | Power State | Assoc State |
+-----------+---------+--------------+-------------+---------------+-------------+-------------+-------------+
| chassis-1 | blade-1 | UCSB-B200-M4 | FCH205371PZ | ok            | operable    | on          | associated  | 
| chassis-1 | blade-2 | UCSB-B200-M4 | FCH20527XXD | ok            | operable    | on          | associated  | 
| chassis-1 | blade-3 | UCSB-B200-M4 | FCH20437VXH | ok            | operable    | on          | associated  | 
| chassis-1 | blade-4 | UCSB-B200-M4 | FCH205371UU | ok            | operable    | on          | associated  | 
+-----------+---------+--------------+-------------+---------------+-------------+-------------+-------------+

+-----------+---------+-------+-------+--------+-------+---------+-------+-------+-------+---------+-------+-------+-------+
| Chassis   | Name    | Power | Min   | Avg    | Max   | Current | Min   | Avg   | Max   | Voltage | Min   | Avg   | Max   |
+-----------+---------+-------+-------+--------+-------+---------+-------+-------+-------+---------+-------+-------+-------+
| chassis-1 | blade-1 | 138.0 | 138.0 | 139.85 | 144.0 | 11.47   | 11.47 | 11.62 | 11.96 | 12.04   | 12.04 | 12.04 | 12.04 | 
| chassis-1 | blade-2 | 138.0 | 138.0 | 138.0  | 138.0 | 11.52   | 11.52 | 11.52 | 11.52 | 11.98   | 11.98 | 11.98 | 11.98 | 
| chassis-1 | blade-3 | 126.0 | 126.0 | 126.0  | 126.0 | 10.52   | 10.52 | 10.52 | 10.52 | 11.98   | 11.98 | 11.98 | 11.98 | 
| chassis-1 | blade-4 | 126.0 | 126.0 | 126.67 | 132.0 | 10.52   | 10.52 | 10.58 | 11.02 | 11.98   | 11.98 | 11.98 | 11.98 | 
+-----------+---------+-------+-------+--------+-------+---------+-------+-------+-------+---------+-------+-------+-------+

+-----------+---------+---------------+---------------------+
| Chassis   | Name    | Sensor Health | Highest Temperature |
+-----------+---------+---------------+---------------------+
| chassis-1 | blade-1 | None          | None                | 
| chassis-1 | blade-2 | None          | None                | 
| chassis-1 | blade-3 | None          | None                | 
| chassis-1 | blade-4 | None          | None                | 
+-----------+---------+---------------+---------------------+
```

JSON Output

```
# iserver get ucsm blades --manager milan --chassis-id 1 --power

[
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
                "time_collected": "2022-12-08T10:59:23.591",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "consumed_power": 138.0,
                "input_current": 11.47,
                "input_voltage": 12.04,
                "consumed_power_avg": 139.85,
                "input_current_avg": 11.62,
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
                "PowerNow": 138.0,
                "PowerMin": 138.0,
                "PowerAvg": 139.85,
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
                "time_collected": "2022-12-08T10:59:56.574",
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
                "time_collected": "2022-12-08T10:59:58.765",
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
                "time_collected": "2022-12-08T10:59:17.465",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "consumed_power": 126.0,
                "input_current": 10.52,
                "input_voltage": 11.98,
                "consumed_power_avg": 126.67,
                "input_current_avg": 10.58,
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
                "PowerAvg": 126.67,
                "PowerMax": 132.0
            }
        }
    }
]
```

Developer Output

```
# iserver get ucsm blades --manager milan --chassis-id 1 --power

Developer output

{
    "duration": 5447,
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
        "connect_time": 2418,
        "disconnect_time": 0,
        "mo_time": 2332,
        "total_time": 4750
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

2022-12-08 11:00:01.785636	True	1875	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 11:00:02.681802	True	889	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 11:00:03.502220	True	788	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 11:00:04.179161	True	655	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 11:00:05.239109	True	543	disconnect vip-ucsb1.emea-sp.cisco.com
```
