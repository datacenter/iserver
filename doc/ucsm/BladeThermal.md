# Get Blade with Thermal Information

```
# iserver get ucsm blade --manager milan --chassis-id 1 --blade-id 1 --thermal

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


+--------------------+-------+------+-------+------+
| Thermal Statistics | Value | Min  | Avg   | Max  |
+--------------------+-------+------+-------+------+
| Motherboard Front  | 23.0  | 23.0 | 23.0  | 23.0 | 
| Motherboard Rear   | 36.0  | 36.0 | 36.0  | 36.0 | 
| CPU-1              | 35.0  | 33.5 | 34.27 | 35.0 | 
| CPU-2              | 37.5  | 36.5 | 37.03 | 37.5 | 
| MEM-1              | 28.0  | 27.0 | 27.54 | 28.0 | 
| MEM-10             | 29.0  | 29.0 | 29.0  | 29.0 | 
| MEM-11             | 25.0  | 25.0 | 25.0  | 25.0 | 
| MEM-13             | 32.0  | 31.0 | 32.0  | 33.0 | 
| MEM-14             | 30.0  | 30.0 | 30.08 | 31.0 | 
| MEM-16             | 28.0  | 28.0 | 28.0  | 28.0 | 
| MEM-17             | 25.0  | 25.0 | 25.0  | 25.0 | 
| MEM-19             | 30.0  | 30.0 | 30.23 | 31.0 | 
| MEM-2              | 26.0  | 26.0 | 26.0  | 26.0 | 
| MEM-20             | 28.0  | 28.0 | 28.77 | 29.0 | 
| MEM-22             | 27.0  | 26.0 | 26.92 | 27.0 | 
| MEM-23             | 27.0  | 27.0 | 27.0  | 27.0 | 
| MEM-4              | 27.0  | 27.0 | 27.0  | 27.0 | 
| MEM-5              | 27.0  | 26.0 | 26.92 | 27.0 | 
| MEM-7              | 29.0  | 29.0 | 29.0  | 29.0 | 
| MEM-8              | 27.0  | 27.0 | 27.31 | 28.0 | 
+--------------------+-------+------+-------+------+
```

JSON Output

```
# iserver get ucsm blade --manager milan --chassis-id 1 --blade-id 1 --thermal

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
    "thermal": {
        "Data": [
            {
                "dn": "sys/chassis-1/blade-1/board/temp-stats",
                "time_collected": "2022-12-08T10:58:22.884",
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
                "time_collected": "2022-12-08T10:58:22.884",
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
                "time_collected": "2022-12-08T10:58:22.884",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "cpu_rn": "cpu-1",
                "name": "CPU-1",
                "type": "cpu",
                "temperature": 35.0,
                "temperature_avg": 34.27,
                "temperature_min": 33.5,
                "temperature_max": 35.0
            },
            {
                "dn": "sys/chassis-1/blade-1/board/cpu-2/env-stats",
                "time_collected": "2022-12-08T10:58:22.884",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "cpu_rn": "cpu-2",
                "name": "CPU-2",
                "type": "cpu",
                "temperature": 37.5,
                "temperature_avg": 37.03,
                "temperature_min": 36.5,
                "temperature_max": 37.5
            },
            {
                "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-1/dimm-env-stats",
                "time_collected": "2022-12-08T10:58:22.884",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-1",
                "name": "MEM-1",
                "type": "memory",
                "temperature": 28.0,
                "temperature_avg": 27.54,
                "temperature_min": 27.0,
                "temperature_max": 28.0
            },
            {
                "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-10/dimm-env-stats",
                "time_collected": "2022-12-08T10:58:22.884",
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
                "time_collected": "2022-12-08T10:58:22.884",
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
                "time_collected": "2022-12-08T10:58:22.884",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-13",
                "name": "MEM-13",
                "type": "memory",
                "temperature": 32.0,
                "temperature_avg": 32.0,
                "temperature_min": 31.0,
                "temperature_max": 33.0
            },
            {
                "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-14/dimm-env-stats",
                "time_collected": "2022-12-08T10:58:22.884",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-14",
                "name": "MEM-14",
                "type": "memory",
                "temperature": 30.0,
                "temperature_avg": 30.08,
                "temperature_min": 30.0,
                "temperature_max": 31.0
            },
            {
                "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-16/dimm-env-stats",
                "time_collected": "2022-12-08T10:58:22.884",
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
                "time_collected": "2022-12-08T10:58:22.884",
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
                "time_collected": "2022-12-08T10:58:22.884",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-19",
                "name": "MEM-19",
                "type": "memory",
                "temperature": 30.0,
                "temperature_avg": 30.23,
                "temperature_min": 30.0,
                "temperature_max": 31.0
            },
            {
                "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-2/dimm-env-stats",
                "time_collected": "2022-12-08T10:58:22.884",
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
                "time_collected": "2022-12-08T10:58:22.884",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-20",
                "name": "MEM-20",
                "type": "memory",
                "temperature": 28.0,
                "temperature_avg": 28.77,
                "temperature_min": 28.0,
                "temperature_max": 29.0
            },
            {
                "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-22/dimm-env-stats",
                "time_collected": "2022-12-08T10:58:22.884",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-22",
                "name": "MEM-22",
                "type": "memory",
                "temperature": 27.0,
                "temperature_avg": 26.92,
                "temperature_min": 26.0,
                "temperature_max": 27.0
            },
            {
                "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-23/dimm-env-stats",
                "time_collected": "2022-12-08T10:58:22.884",
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
                "time_collected": "2022-12-08T10:58:22.884",
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
                "time_collected": "2022-12-08T10:58:22.884",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-5",
                "name": "MEM-5",
                "type": "memory",
                "temperature": 27.0,
                "temperature_avg": 26.92,
                "temperature_min": 26.0,
                "temperature_max": 27.0
            },
            {
                "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-7/dimm-env-stats",
                "time_collected": "2022-12-08T10:58:22.884",
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
                "time_collected": "2022-12-08T10:58:22.884",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-8",
                "name": "MEM-8",
                "type": "memory",
                "temperature": 27.0,
                "temperature_avg": 27.31,
                "temperature_min": 27.0,
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
}
```

Developer Output

```
# iserver get ucsm blade --manager milan --chassis-id 1 --blade-id 1 --thermal

Developer output

{
    "duration": 5301,
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
        "connect_time": 2188,
        "disconnect_time": 0,
        "mo_time": 2894,
        "total_time": 5082
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

2022-12-08 10:59:15.396959	True	1725	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 10:59:15.996855	True	596	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 10:59:16.538580	True	538	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 10:59:17.116740	True	576	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 10:59:17.575318	True	456	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 10:59:18.307004	True	728	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 10:59:18.935772	True	463	disconnect vip-ucsb1.emea-sp.cisco.com
```
