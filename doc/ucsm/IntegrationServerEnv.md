# Get Intersight Server with Environmental Information

Environmental = Power + Thermal

```
# iserver get server --ip 10.58.52.36 --env

+------+----+----+----------------------+------------------+-------------+-------------+------------+-----------+
| SF   | MF | WF | Name                 | Model            | Serial      | IP          | CPU        | Memory    |
+------+----+----+----------------------+------------------+-------------+-------------+------------+-----------+
| P+ H | CU |    | FI-ucsb1-eu-spdc-1-4 | (B) UCSB-B200-M4 | FCH205371UU | 10.58.52.36 | 2S 24C 48T | 256 [GiB] | 
+------+----+----+----------------------+------------------+-------------+-------------+------------+-----------+

+--------------------+-------+-------+-------+-------+
| Power Statistics   | Value | Min   | Avg   | Max   |
+--------------------+-------+-------+-------+-------+
| Consumed Power (W) | 126.0 | 126.0 | 126.5 | 132.0 | 
| Input Current (A)  | 10.52 | 10.52 | 10.56 | 11.02 | 
| Input Voltage (V)  | 11.98 | 11.98 | 11.98 | 11.98 | 
+--------------------+-------+-------+-------+-------+

+--------------------+-------+------+-------+------+
| Thermal Statistics | Value | Min  | Avg   | Max  |
+--------------------+-------+------+-------+------+
| Motherboard Front  | 25.0  | 25.0 | 25.08 | 26.0 | 
| Motherboard Rear   | 36.0  | 36.0 | 36.0  | 36.0 | 
| CPU-1              | 39.5  | 39.0 | 39.36 | 39.5 | 
| CPU-2              | 41.0  | 41.0 | 41.57 | 42.0 | 
| MEM-1              | 29.0  | 29.0 | 29.0  | 29.0 | 
| MEM-10             | 29.0  | 29.0 | 29.0  | 29.0 | 
| MEM-13             | 30.0  | 30.0 | 30.0  | 30.0 | 
| MEM-16             | 32.0  | 31.0 | 31.17 | 32.0 | 
| MEM-19             | 28.0  | 28.0 | 28.0  | 28.0 | 
| MEM-22             | 30.0  | 30.0 | 30.0  | 30.0 | 
| MEM-4              | 28.0  | 28.0 | 28.0  | 28.0 | 
| MEM-7              | 31.0  | 31.0 | 31.0  | 31.0 | 
+--------------------+-------+------+-------+------+
```

JSON Output

```
# iserver get server --ip 10.58.52.36 --env

{
    "__Output": {
        "FlagState": ":GG.G"
    },
    "Moid": "63371c9176752d3139f7da74",
    "DeviceMoId": "618942976f72612d309dfbe1",
    "Name": "FI-ucsb1-eu-spdc-1-4",
    "Model": "UCSB-B200-M4",
    "Serial": "FCH205371UU",
    "ManagementMode": "UCSM",
    "OperPowerState": "on",
    "NumCpus": 2,
    "NumCpuCores": 24,
    "NumThreads": 48,
    "Cpu": "2S 24C 48T",
    "AvailableMemory": 262144,
    "TotalMemory": 262144,
    "UsedMemory": 0,
    "TotalMemoryUnit": "256 [GiB]",
    "TotalMemoryGB": 256,
    "AvailableMemoryUnit": "256 [GiB]",
    "AvailableMemoryGB": 256,
    "UsedMemoryUnit": "0 [KiB]",
    "UsedMemoryGB": 0,
    "UsedMemoryPct": 0,
    "UsedMemoryPctUnit": "0%",
    "ManagementIp": "10.58.52.36",
    "AlarmSummary": {
        "Critical": 0,
        "Warning": 0,
        "Info": 0
    },
    "Health": "Healthy",
    "Connected": true,
    "Workflow": {
        "Running": null,
        "LatestMoid": null,
        "Last": []
    },
    "Groups": "power,ucsm",
    "Redfish": {
        "Capable": false,
        "Enabled": false
    },
    "UCSM": {
        "Capable": true,
        "Enabled": true
    },
    "IMC": {
        "Capable": false,
        "Enabled": false
    },
    "Power": {
        "Data": {
            "dn": "sys/chassis-1/blade-4/board/power-stats",
            "time_collected": "2022-12-13T18:07:02.240",
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
    "Thermal": {
        "Data": [
            {
                "dn": "sys/chassis-1/blade-4/board/temp-stats",
                "time_collected": "2022-12-13T18:07:02.240",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "name": "Motherboard Front",
                "type": "motherboard",
                "temperature": 25.0,
                "fm_temp_sen_rear": 36.0,
                "temperature_avg": 25.08,
                "fm_temp_sen_rear_avg": 36.0,
                "temperature_min": 25.0,
                "fm_temp_sen_rear_min": 36.0,
                "temperature_max": 26.0,
                "fm_temp_sen_rear_max": 36.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/temp-stats",
                "time_collected": "2022-12-13T18:07:02.240",
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
                "time_collected": "2022-12-13T18:07:02.240",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "cpu_rn": "cpu-1",
                "name": "CPU-1",
                "type": "cpu",
                "temperature": 39.5,
                "temperature_avg": 39.36,
                "temperature_min": 39.0,
                "temperature_max": 39.5
            },
            {
                "dn": "sys/chassis-1/blade-4/board/cpu-2/env-stats",
                "time_collected": "2022-12-13T18:07:02.240",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "cpu_rn": "cpu-2",
                "name": "CPU-2",
                "type": "cpu",
                "temperature": 41.0,
                "temperature_avg": 41.57,
                "temperature_min": 41.0,
                "temperature_max": 42.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-1/dimm-env-stats",
                "time_collected": "2022-12-13T18:07:02.240",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
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
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-10/dimm-env-stats",
                "time_collected": "2022-12-13T18:07:02.240",
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
                "time_collected": "2022-12-13T18:07:02.240",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
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
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-16/dimm-env-stats",
                "time_collected": "2022-12-13T18:07:02.240",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-16",
                "name": "MEM-16",
                "type": "memory",
                "temperature": 32.0,
                "temperature_avg": 31.17,
                "temperature_min": 31.0,
                "temperature_max": 32.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-19/dimm-env-stats",
                "time_collected": "2022-12-13T18:07:02.240",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-19",
                "name": "MEM-19",
                "type": "memory",
                "temperature": 28.0,
                "temperature_avg": 28.0,
                "temperature_min": 28.0,
                "temperature_max": 28.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-22/dimm-env-stats",
                "time_collected": "2022-12-13T18:07:02.240",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-22",
                "name": "MEM-22",
                "type": "memory",
                "temperature": 30.0,
                "temperature_avg": 30.0,
                "temperature_min": 30.0,
                "temperature_max": 30.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-4/dimm-env-stats",
                "time_collected": "2022-12-13T18:07:02.240",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-4",
                "name": "MEM-4",
                "type": "memory",
                "temperature": 28.0,
                "temperature_avg": 28.0,
                "temperature_min": 28.0,
                "temperature_max": 28.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-7/dimm-env-stats",
                "time_collected": "2022-12-13T18:07:02.240",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-7",
                "name": "MEM-7",
                "type": "memory",
                "temperature": 31.0,
                "temperature_avg": 31.0,
                "temperature_min": 31.0,
                "temperature_max": 31.0
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
    },
    "Type": "Blade",
    "TypeModel": "(B) UCSB-B200-M4",
    "LocatorLedOn": false,
    "FlagState": "P+ H",
    "FlagManagement": "CU",
    "FlagWorkflow": ""
}
```

Developer Output

```
# iserver get server --ip 10.58.52.36 --env

Developer output

{
    "duration": 7957,
    "isctl": {
        "read": true,
        "calls": 4,
        "success": 4,
        "failed": 0,
        "total_time": 4267
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
        "success": 12,
        "failed": 0,
        "connect": 4,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 1766,
        "disconnect_time": 0,
        "mo_time": 1591,
        "total_time": 3357
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
        "read": true,
        "lines": 52
    }
}

Log: isctl
-----------

2022-12-13 17:07:34.198795	True	2199	93	isctl get compute rackunit   -o json --top 100
2022-12-13 17:07:35.035788	True	835	10	isctl get compute blade   -o json --top 100
2022-12-13 17:07:35.722375	True	545	1	isctl get asset deviceregistration  moid 618942976f72612d309dfbe1 -o json
2022-12-13 17:07:36.412649	True	688	16	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-06T17:07:35.000Z"  -o json --top 100


Log: ucsm
----------

2022-12-13 17:07:37.145012	True	726	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:07:37.341767	True	196	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:07:37.629383	True	287	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:07:37.796819	True	167	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:07:37.963018	True	165	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:07:38.685425	True	720	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:07:38.848838	True	163	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:07:39.043439	True	194	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:07:39.221982	True	178	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:07:39.399366	True	177	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:07:39.628691	True	229	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:07:39.792659	True	155	disconnect vip-ucsb1.emea-sp.cisco.com
```
