# Server Details - Chassis

```
# iserver get server --name FI-ucsb1-eu-spdc-2-4 --chassis

+------+----+---------+----------------------+------------------+-------------+-------------+------------+-----------+
| SF   | MF | WF (7d) | Name                 | Model            | Serial      | IP          | CPU        | Memory    |
+------+----+---------+----------------------+------------------+-------------+-------------+------------+-----------+
| P+ H | CU |         | FI-ucsb1-eu-spdc-2-4 | (B) UCSB-B200-M5 | FLM24140B0B | 10.58.52.44 | 2S 40C 80T | 192 [GiB] | 
+------+----+---------+----------------------+------------------+-------------+-------------+------------+-----------+

Chassis
-------
- Name   : FI-ucsb1-eu-spdc-2
- Model  : UCSB-5108-AC2
- Serial : FOX2403P2Z9
- Blades : 4
- Health : Healthy
```

JSON output

```
# iserver get server --name FI-ucsb1-eu-spdc-2-4 --chassis

{
    "__Output": {
        "FlagState": ":GG.G",
        "FlagManagement": ":GG",
        "FlagWorkflow": ":"
    },
    "Moid": "63371c9176752d3139f7da78",
    "DeviceMoId": "618942976f72612d309dfbe1",
    "Name": "FI-ucsb1-eu-spdc-2-4",
    "Model": "UCSB-B200-M5",
    "Serial": "FLM24140B0B",
    "ManagementMode": "UCSM",
    "OperPowerState": "on",
    "Type": "Blade",
    "TypeModel": "(B) UCSB-B200-M5",
    "ChassisInfo": {
        "__Output": {
            "Health": "Green"
        },
        "Moid": "619d05ae76752d313994a00a",
        "Dn": "sys/chassis-2",
        "Blades": 4,
        "Name": "FI-ucsb1-eu-spdc-2",
        "Model": "UCSB-5108-AC2",
        "Serial": "FOX2403P2Z9",
        "Health": "Healthy",
        "HealthSummary": "Healthy",
        "UcsDomain": ""
    },
    "NumCpus": 2,
    "NumCpuCores": 40,
    "NumThreads": 80,
    "Cpu": "2S 40C 80T",
    "Groups": "power,ucsm",
    "AlarmSummary": {
        "__Output": {
            "Critical": "Red",
            "Warning": "Yellow",
            "Info": "Blue",
            "Cleared": "Green"
        },
        "Critical": 0,
        "Warning": 0,
        "Info": 0
    },
    "Health": "Healthy",
    "LocatorLedOn": false,
    "ManagementIp": "10.58.52.44",
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
    "AvailableMemory": 196608,
    "TotalMemory": 196608,
    "UsedMemory": 0,
    "TotalMemoryUnit": "192 [GiB]",
    "TotalMemoryGB": 192,
    "AvailableMemoryUnit": "192 [GiB]",
    "AvailableMemoryGB": 192,
    "UsedMemoryUnit": "0 [KiB]",
    "UsedMemoryGB": 0,
    "UsedMemoryPct": 0,
    "UsedMemoryPctUnit": "0%",
    "Connected": true,
    "Workflow": {
        "Days": 7,
        "Running": null,
        "LatestMoid": null,
        "Last": []
    },
    "FlagState": "P+ H",
    "FlagManagement": "CU",
    "FlagWorkflow": ""
}
```

Developer output

```
# iserver get server --name FI-ucsb1-eu-spdc-2-4 --chassis

Developer output

{
    "duration": 13601,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 9591
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
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "mo": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "mo_time": 0,
        "total_time": 0
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
        "lines": 369
    }
}

Log: isctl
-----------

2023-01-05 18:46:22.863540	True	3201	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:46:24.567622	True	1699	10	isctl get compute blade   -o json --top 100
2023-01-05 18:46:29.776546	True	1601	1	isctl get equipment chassis  moid 619d05ae76752d313994a00a -o json
2023-01-05 18:46:31.151835	True	1372	1	isctl get asset deviceregistration  moid 618942976f72612d309dfbe1 -o json
2023-01-05 18:46:32.872833	True	1718	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:46:31.000Z"  -o json --top 100
```
