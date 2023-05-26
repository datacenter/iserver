# Get Blades with Environmental Information

Environmental = Power + Thermal

```
# iserver get ucsm blades --manager milan --chassis-id 1 --env

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
| chassis-1 | blade-1 | 138.0 | 138.0 | 139.71 | 144.0 | 11.47   | 11.47 | 11.61 | 11.96 | 12.04   | 12.04 | 12.04 | 12.04 | 
| chassis-1 | blade-2 | 138.0 | 138.0 | 138.0  | 138.0 | 11.52   | 11.52 | 11.52 | 11.52 | 11.98   | 11.98 | 11.98 | 11.98 | 
| chassis-1 | blade-3 | 126.0 | 126.0 | 126.0  | 126.0 | 10.52   | 10.52 | 10.52 | 10.52 | 11.98   | 11.98 | 11.98 | 11.98 | 
| chassis-1 | blade-4 | 126.0 | 126.0 | 126.6  | 132.0 | 10.52   | 10.52 | 10.57 | 11.02 | 11.98   | 11.98 | 11.98 | 11.98 | 
+-----------+---------+-------+-------+--------+-------+---------+-------+-------+-------+---------+-------+-------+-------+

+-----------+---------+---------------+---------------------+
| Chassis   | Name    | Sensor Health | Highest Temperature |
+-----------+---------+---------------+---------------------+
| chassis-1 | blade-1 | True          | 37.0                | 
| chassis-1 | blade-2 | True          | 38.0                | 
| chassis-1 | blade-3 | True          | 40.0                | 
| chassis-1 | blade-4 | True          | 41.0                | 
+-----------+---------+---------------+---------------------+
```

JSON Output

```
# iserver get ucsm blades --manager milan --chassis-id 1 --env

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
                "time_collected": "2022-12-08T11:00:23.430",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "consumed_power": 138.0,
                "input_current": 11.47,
                "input_voltage": 12.04,
                "consumed_power_avg": 139.71,
                "input_current_avg": 11.61,
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
                "PowerAvg": 139.71,
                "PowerMax": 144.0
            }
        },
        "thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-1/board/temp-stats",
                    "time_collected": "2022-12-08T11:00:23.431",
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
                    "time_collected": "2022-12-08T11:00:23.431",
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
                    "time_collected": "2022-12-08T11:00:23.430",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 34.5,
                    "temperature_avg": 34.25,
                    "temperature_min": 34.0,
                    "temperature_max": 34.5
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T11:00:23.430",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 37.0,
                    "temperature_avg": 37.0,
                    "temperature_min": 37.0,
                    "temperature_max": 37.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T11:00:23.431",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 27.6,
                    "temperature_min": 27.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-10/dimm-env-stats",
                    "time_collected": "2022-12-08T11:00:23.431",
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
                    "time_collected": "2022-12-08T11:00:23.431",
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
                    "time_collected": "2022-12-08T11:00:23.431",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.87,
                    "temperature_min": 31.0,
                    "temperature_max": 33.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-14/dimm-env-stats",
                    "time_collected": "2022-12-08T11:00:23.431",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-14",
                    "name": "MEM-14",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.07,
                    "temperature_min": 30.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-16/dimm-env-stats",
                    "time_collected": "2022-12-08T11:00:23.431",
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
                    "time_collected": "2022-12-08T11:00:23.431",
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
                    "time_collected": "2022-12-08T11:00:23.431",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.2,
                    "temperature_min": 30.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-2/dimm-env-stats",
                    "time_collected": "2022-12-08T11:00:23.431",
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
                    "time_collected": "2022-12-08T11:00:23.431",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-20",
                    "name": "MEM-20",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.67,
                    "temperature_min": 28.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-08T11:00:23.431",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-22",
                    "name": "MEM-22",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 26.93,
                    "temperature_min": 26.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-23/dimm-env-stats",
                    "time_collected": "2022-12-08T11:00:23.431",
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
                    "time_collected": "2022-12-08T11:00:23.431",
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
                    "time_collected": "2022-12-08T11:00:23.431",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-5",
                    "name": "MEM-5",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 26.93,
                    "temperature_min": 26.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-7/dimm-env-stats",
                    "time_collected": "2022-12-08T11:00:23.431",
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
                    "time_collected": "2022-12-08T11:00:23.431",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-8",
                    "name": "MEM-8",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.27,
                    "temperature_min": 27.0,
                    "temperature_max": 28.0
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
        },
        "thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-2/board/temp-stats",
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 38.0,
                    "temperature_avg": 37.92,
                    "temperature_min": 37.5,
                    "temperature_max": 38.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.75,
                    "temperature_min": 29.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-14/dimm-env-stats",
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-23",
                    "name": "MEM-23",
                    "type": "memory",
                    "temperature": 32.0,
                    "temperature_avg": 32.0,
                    "temperature_min": 32.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-4/dimm-env-stats",
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
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
                    "time_collected": "2022-12-08T10:59:56.574",
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
        },
        "thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-3/board/temp-stats",
                    "time_collected": "2022-12-08T10:59:58.765",
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
                    "time_collected": "2022-12-08T10:59:58.765",
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
                    "time_collected": "2022-12-08T10:59:58.764",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 37.0,
                    "temperature_avg": 37.0,
                    "temperature_min": 36.5,
                    "temperature_max": 37.5
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T10:59:58.764",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 40.0,
                    "temperature_avg": 40.62,
                    "temperature_min": 40.0,
                    "temperature_max": 41.5
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T10:59:58.765",
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
                    "time_collected": "2022-12-08T10:59:58.765",
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
                    "time_collected": "2022-12-08T10:59:58.765",
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
                    "time_collected": "2022-12-08T10:59:58.765",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-16",
                    "name": "MEM-16",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.38,
                    "temperature_min": 28.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-08T10:59:58.765",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 25.0,
                    "temperature_avg": 25.0,
                    "temperature_min": 25.0,
                    "temperature_max": 25.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-08T10:59:58.765",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-22",
                    "name": "MEM-22",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.54,
                    "temperature_min": 27.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-4/dimm-env-stats",
                    "time_collected": "2022-12-08T10:59:58.765",
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
                    "time_collected": "2022-12-08T10:59:58.765",
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
                "HighestTemperature": 40.0,
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
                "time_collected": "2022-12-08T11:00:17.356",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "consumed_power": 126.0,
                "input_current": 10.52,
                "input_voltage": 11.98,
                "consumed_power_avg": 126.6,
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
                "PowerAvg": 126.6,
                "PowerMax": 132.0
            }
        },
        "thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-4/board/temp-stats",
                    "time_collected": "2022-12-08T11:00:17.356",
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
                    "time_collected": "2022-12-08T11:00:17.356",
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
                    "time_collected": "2022-12-08T11:00:17.356",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 39.0,
                    "temperature_avg": 38.2,
                    "temperature_min": 38.0,
                    "temperature_max": 39.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T11:00:17.356",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 41.0,
                    "temperature_avg": 41.1,
                    "temperature_min": 41.0,
                    "temperature_max": 41.5
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T11:00:17.356",
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
                    "time_collected": "2022-12-08T11:00:17.356",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
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
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-08T11:00:17.356",
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
                    "time_collected": "2022-12-08T11:00:17.356",
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
                    "time_collected": "2022-12-08T11:00:17.356",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 30.5,
                    "temperature_min": 30.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-08T11:00:17.356",
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
                    "time_collected": "2022-12-08T11:00:17.356",
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
                    "time_collected": "2022-12-08T11:00:17.356",
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
```

Developer Output

```
# iserver get ucsm blades --manager milan --chassis-id 1 --env

Developer output

{
    "duration": 5850,
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
        "connect_time": 2261,
        "disconnect_time": 0,
        "mo_time": 3341,
        "total_time": 5602
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

2022-12-08 11:00:47.987529	True	1754	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 11:00:48.571921	True	580	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 11:00:49.185421	True	610	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 11:00:49.724032	True	519	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 11:00:50.197623	True	470	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 11:00:50.680282	True	480	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 11:00:51.364928	True	682	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 11:00:52.001731	True	507	disconnect vip-ucsb1.emea-sp.cisco.com
```
