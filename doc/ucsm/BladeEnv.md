# Get Blade with Environmental Information

Environmental = Power + Thermal

```
# iserver get ucsm blade --manager milan --chassis-id 1 --blade-id 1 --env

Blade
-----
- Chassis       : chassis-1
- Blade         : blade-1
- Model         : UCSB-B200-M4
- Serial        : FCH205371PZ
- Overal Status : ok
- Operability   : operable
- Power State   : on
- Assoc State   : associated


+--------------------+-------+-------+--------+-------+
| Power Statistics   | Value | Min   | Avg    | Max   |
+--------------------+-------+-------+--------+-------+
| Consumed Power (W) | 138.0 | 138.0 | 139.85 | 144.0 | 
| Input Current (A)  | 11.47 | 11.47 | 11.62  | 11.96 | 
| Input Voltage (V)  | 12.04 | 12.04 | 12.04  | 12.04 | 
+--------------------+-------+-------+--------+-------+

+--------------------+-------+------+-------+------+
| Thermal Statistics | Value | Min  | Avg   | Max  |
+--------------------+-------+------+-------+------+
| Motherboard Front  | 23.0  | 23.0 | 23.0  | 23.0 | 
| Motherboard Rear   | 36.0  | 36.0 | 36.0  | 36.0 | 
| CPU-1              | 34.0  | 34.0 | 34.0  | 34.0 | 
| CPU-2              | 37.0  | 37.0 | 37.0  | 37.0 | 
| MEM-1              | 28.0  | 27.0 | 27.57 | 28.0 | 
| MEM-10             | 29.0  | 29.0 | 29.0  | 29.0 | 
| MEM-11             | 25.0  | 25.0 | 25.0  | 25.0 | 
| MEM-13             | 31.0  | 31.0 | 31.93 | 33.0 | 
| MEM-14             | 30.0  | 30.0 | 30.07 | 31.0 | 
| MEM-16             | 28.0  | 28.0 | 28.0  | 28.0 | 
| MEM-17             | 25.0  | 25.0 | 25.0  | 25.0 | 
| MEM-19             | 30.0  | 30.0 | 30.21 | 31.0 | 
| MEM-2              | 26.0  | 26.0 | 26.0  | 26.0 | 
| MEM-20             | 28.0  | 28.0 | 28.71 | 29.0 | 
| MEM-22             | 27.0  | 26.0 | 26.93 | 27.0 | 
| MEM-23             | 27.0  | 27.0 | 27.0  | 27.0 | 
| MEM-4              | 27.0  | 27.0 | 27.0  | 27.0 | 
| MEM-5              | 27.0  | 26.0 | 26.93 | 27.0 | 
| MEM-7              | 29.0  | 29.0 | 29.0  | 29.0 | 
| MEM-8              | 27.0  | 27.0 | 27.29 | 28.0 | 
+--------------------+-------+------+-------+------+
```

JSON Output

```
# iserver get ucsm blade --manager milan --chassis-id 1 --blade-id 1 --env

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
    },
    "thermal": {
        "Data": [
            {
                "dn": "sys/chassis-1/blade-1/board/temp-stats",
                "time_collected": "2022-12-08T10:59:23.591",
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
                "time_collected": "2022-12-08T10:59:23.591",
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
                "time_collected": "2022-12-08T10:59:23.591",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "cpu_rn": "cpu-1",
                "name": "CPU-1",
                "type": "cpu",
                "temperature": 34.0,
                "temperature_avg": 34.0,
                "temperature_min": 34.0,
                "temperature_max": 34.0
            },
            {
                "dn": "sys/chassis-1/blade-1/board/cpu-2/env-stats",
                "time_collected": "2022-12-08T10:59:23.591",
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
                "time_collected": "2022-12-08T10:59:23.591",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-1",
                "name": "MEM-1",
                "type": "memory",
                "temperature": 28.0,
                "temperature_avg": 27.57,
                "temperature_min": 27.0,
                "temperature_max": 28.0
            },
            {
                "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-10/dimm-env-stats",
                "time_collected": "2022-12-08T10:59:23.591",
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
                "time_collected": "2022-12-08T10:59:23.591",
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
                "time_collected": "2022-12-08T10:59:23.591",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-13",
                "name": "MEM-13",
                "type": "memory",
                "temperature": 31.0,
                "temperature_avg": 31.93,
                "temperature_min": 31.0,
                "temperature_max": 33.0
            },
            {
                "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-14/dimm-env-stats",
                "time_collected": "2022-12-08T10:59:23.591",
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
                "time_collected": "2022-12-08T10:59:23.591",
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
                "time_collected": "2022-12-08T10:59:23.591",
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
                "time_collected": "2022-12-08T10:59:23.591",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-19",
                "name": "MEM-19",
                "type": "memory",
                "temperature": 30.0,
                "temperature_avg": 30.21,
                "temperature_min": 30.0,
                "temperature_max": 31.0
            },
            {
                "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-2/dimm-env-stats",
                "time_collected": "2022-12-08T10:59:23.591",
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
                "time_collected": "2022-12-08T10:59:23.591",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-20",
                "name": "MEM-20",
                "type": "memory",
                "temperature": 28.0,
                "temperature_avg": 28.71,
                "temperature_min": 28.0,
                "temperature_max": 29.0
            },
            {
                "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-22/dimm-env-stats",
                "time_collected": "2022-12-08T10:59:23.591",
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
                "time_collected": "2022-12-08T10:59:23.591",
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
                "time_collected": "2022-12-08T10:59:23.591",
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
                "time_collected": "2022-12-08T10:59:23.591",
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
                "time_collected": "2022-12-08T10:59:23.591",
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
                "time_collected": "2022-12-08T10:59:23.591",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-8",
                "name": "MEM-8",
                "type": "memory",
                "temperature": 27.0,
                "temperature_avg": 27.29,
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
}
```

Developer Output

```
# iserver get ucsm blade --manager milan --chassis-id 1 --blade-id 1 --env

Developer output

{
    "duration": 5594,
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
        "connect_time": 2376,
        "disconnect_time": 0,
        "mo_time": 2948,
        "total_time": 5324
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

2022-12-08 10:59:28.779218	True	1761	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 10:59:29.318279	True	536	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 10:59:29.847644	True	527	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 10:59:30.315593	True	466	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 10:59:30.740108	True	423	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 10:59:31.196006	True	455	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 10:59:31.739181	True	541	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 10:59:32.519872	True	615	disconnect vip-ucsb1.emea-sp.cisco.com
```
