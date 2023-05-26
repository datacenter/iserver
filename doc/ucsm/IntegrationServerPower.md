# Get Intersight Server with Power Information

```
# iserver get server --ip 10.58.52.36 --power

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
```

JSON Output

```
# iserver get server --ip 10.58.52.36 --power

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
# iserver get server --ip 10.58.52.36 --power

Developer output

{
    "duration": 5962,
    "isctl": {
        "read": true,
        "calls": 4,
        "success": 4,
        "failed": 0,
        "total_time": 4111
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
        "connect_time": 983,
        "disconnect_time": 0,
        "mo_time": 570,
        "total_time": 1553
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

2022-12-13 17:07:20.070705	True	2000	93	isctl get compute rackunit   -o json --top 100
2022-12-13 17:07:20.647437	True	575	10	isctl get compute blade   -o json --top 100
2022-12-13 17:07:21.276441	True	494	1	isctl get asset deviceregistration  moid 618942976f72612d309dfbe1 -o json
2022-12-13 17:07:22.320723	True	1042	16	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-06T17:07:21.000Z"  -o json --top 100


Log: ucsm
----------

2022-12-13 17:07:23.145518	True	818	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:07:23.349639	True	203	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:07:23.547505	True	198	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:07:23.716216	True	169	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:07:23.883092	True	165	disconnect vip-ucsb1.emea-sp.cisco.com
```
