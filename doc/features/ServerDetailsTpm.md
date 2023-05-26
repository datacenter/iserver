# Server Details - TPM

```
# iserver get server --name comp2-p4b-eu-spdc-WZP26360D3D --tpm

+------+-----+---------+-------------------------------+--------------------+-------------+-------------+--------------+-----------+
| SF   | MF  | WF (7d) | Name                          | Model              | Serial      | IP          | CPU          | Memory    |
+------+-----+---------+-------------------------------+--------------------+-------------+-------------+--------------+-----------+
| P+ H | Cri |         | comp2-p4b-eu-spdc-WZP26360D3D | (R) UCSC-C245-M6SX | WZP26360D3D | 10.58.53.34 | 2S 128C 256T | 512 [GiB] | 
+------+-----+---------+-------------------------------+--------------------+-------------+-------------+--------------+-----------+

+----------+-------------------+-------------+---------+------------------+-------------------+-------------+
| TPM      | Activation Status | Admin State | Version | Model            | Vendor            | Serial      |
+----------+-------------------+-------------+---------+------------------+-------------------+-------------+
| equipped | activated         | enabled     | 2.0     | UCSX-TPM2-002B-C | Cisco Systems Inc | FCH262076Q7 | 
+----------+-------------------+-------------+---------+------------------+-------------------+-------------+
```

JSON output

```
# iserver get server --name comp2-p4b-eu-spdc-WZP26360D3D --tpm

{
    "__Output": {
        "FlagState": ":GG.G",
        "FlagManagement": ":GYY",
        "FlagWorkflow": ":"
    },
    "Moid": "6384d45476752d31395c7874",
    "DeviceMoId": "6384d44a6f72612d317bfc51",
    "Name": "comp2-p4b-eu-spdc-WZP26360D3D",
    "Model": "UCSC-C245-M6SX",
    "Serial": "WZP26360D3D",
    "ManagementMode": "IntersightStandalone",
    "OperPowerState": "on",
    "Type": "Rack",
    "TypeModel": "(R) UCSC-C245-M6SX",
    "NumCpus": 2,
    "NumCpuCores": 128,
    "NumThreads": 256,
    "Cpu": "2S 128C 256T",
    "Groups": "",
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
    "ManagementIp": "10.58.53.34",
    "Redfish": {
        "Capable": true,
        "Enabled": false
    },
    "UCSM": {
        "Capable": false,
        "Enabled": false
    },
    "IMC": {
        "Capable": true,
        "Enabled": false
    },
    "AvailableMemory": 524288,
    "TotalMemory": 524288,
    "UsedMemory": 0,
    "TotalMemoryUnit": "512 [GiB]",
    "TotalMemoryGB": 512,
    "AvailableMemoryUnit": "512 [GiB]",
    "AvailableMemoryGB": 512,
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
    "TpmInfo": [
        {
            "__Output": {
                "ActivationStatus": "Green",
                "AdminState": "Green",
                "Presence": "Green"
            },
            "ActivationStatus": "activated",
            "AdminState": "enabled",
            "FirmwareVersion": "",
            "Model": "UCSX-TPM2-002B-C",
            "Moid": "6384d46676752d31395c7c85",
            "Presence": "equipped",
            "Serial": "FCH262076Q7",
            "TpmId": 0,
            "Vendor": "Cisco Systems Inc",
            "Version": "2.0"
        }
    ],
    "FlagState": "P+ H",
    "FlagManagement": "Cri",
    "FlagWorkflow": ""
}
```

Developer output

```
# iserver get server --name comp2-p4b-eu-spdc-WZP26360D3D --tpm

Developer output

{
    "duration": 16532,
    "isctl": {
        "read": true,
        "calls": 7,
        "success": 7,
        "failed": 0,
        "total_time": 12652
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
        "lines": 453
    }
}

Log: isctl
-----------

2023-01-05 18:52:44.084941	True	3101	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:52:45.737216	True	1650	10	isctl get compute blade   -o json --top 100
2023-01-05 18:52:50.793116	True	1614	1	isctl get compute board --filter "ComputeRackUnit/Moid eq '6384d45476752d31395c7874'"  -o json --top 100
2023-01-05 18:52:52.326867	True	1530	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '6384d44a6f72612d317bfc51'"  -o json --top 100
2023-01-05 18:52:53.967119	True	1638	1	isctl get asset deviceregistration  moid 6384d44a6f72612d317bfc51 -o json
2023-01-05 18:52:55.584709	True	1614	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:52:53.000Z"  -o json --top 100
2023-01-05 18:52:57.103572	True	1505	1	isctl get equipment tpm --filter "Moid in ('6384d46676752d31395c7c85')"  -o json --top 100
```
