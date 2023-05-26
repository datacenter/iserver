# Server Details - Board

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --board

+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF (7d) | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | C2      | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+

Motherboard Hardware Summary
----------------------------
- Board Id                     : 0
- Model                        : UCSC-C240-M5SN
- Serial                       : WZP23400AJW
- Vendor                       : Cisco Systems Inc
- Processors                   : 2
- Memory Arrays                : 1
- Storage Controller           : 2
- Storage Flex Util Controller : 1
- TPM                          : 1
```

JSON output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --board

{
    "__Output": {
        "FlagState": ":GG.G",
        "FlagManagement": ":GGY",
        "FlagWorkflow": ":GG"
    },
    "Moid": "5fdf9c016176752d35e44795",
    "DeviceMoId": "5fdf9be76f72612d300a8d81",
    "Name": "comp-1-p2b-eu-spdc-WZP23400AJW",
    "Model": "UCSC-C240-M5SN",
    "Serial": "WZP23400AJW",
    "ManagementMode": "IntersightStandalone",
    "OperPowerState": "on",
    "Type": "Rack",
    "TypeModel": "(R) UCSC-C240-M5SN",
    "BoardInfo": {
        "BoardId": 0,
        "CpuTypeController": "",
        "Dn": "sys/rack-unit-1/board",
        "Model": "UCSC-C240-M5SN",
        "Moid": "5fdf9c056176752d35e44930",
        "OperPowerState": "not-supported",
        "Serial": "WZP23400AJW",
        "Vendor": "Cisco Systems Inc",
        "EquipmentTpmsIds": [
            "5fdf9c186176752d35e4503a"
        ],
        "EquipmentTpmsCount": 1,
        "GraphicsCardsIds": [],
        "GraphicsCardsCount": 0,
        "MemoryArraysIds": [
            "5fdf9c416176752d35e45e6f"
        ],
        "MemoryArraysCount": 1,
        "PciCoprocessorCardsIds": [],
        "PciCoprocessorCardsCount": 0,
        "PciSwitchIds": [],
        "PciSwitchCount": 0,
        "ProcessorsIds": [
            "5fdf9c5a6176752d35e467d7",
            "5fdf9c5a6176752d35e467db"
        ],
        "ProcessorsCount": 2,
        "SecurityUnitsIds": [],
        "SecurityUnitsCount": 0,
        "StorageControllersIds": [
            "635840e076752d31399d9215",
            "636ddf1876752d3139c8d4f5"
        ],
        "StorageControllersCount": 2,
        "StorageFlexFlashControllersIds": [],
        "StorageFlexFlashControllersCount": 0,
        "StorageFlexUtilControllersIds": [
            "5fdf9c726176752d35e46f0c"
        ],
        "StorageFlexUtilControllersCount": 1
    },
    "NumCpus": 2,
    "NumCpuCores": 40,
    "NumThreads": 80,
    "Cpu": "2S 40C 80T",
    "Groups": "p2b,pod2b,power",
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
    "ManagementIp": "10.58.50.41",
    "Redfish": {
        "Capable": true,
        "Enabled": true
    },
    "UCSM": {
        "Capable": false,
        "Enabled": false
    },
    "IMC": {
        "Capable": true,
        "Enabled": false
    },
    "AvailableMemory": 393216,
    "TotalMemory": 393216,
    "UsedMemory": 0,
    "TotalMemoryUnit": "384 [GiB]",
    "TotalMemoryGB": 384,
    "AvailableMemoryUnit": "384 [GiB]",
    "AvailableMemoryGB": 384,
    "UsedMemoryUnit": "0 [KiB]",
    "UsedMemoryGB": 0,
    "UsedMemoryPct": 0,
    "UsedMemoryPctUnit": "0%",
    "Connected": true,
    "Workflow": {
        "Days": 7,
        "Running": null,
        "LatestMoid": "63b5c955696f6e2d30bd0bfb",
        "Last": [
            {
                "__Output": {
                    "Status": "Green"
                },
                "Moid": "63b5c955696f6e2d30bd0bfb",
                "Name": "Turn Off Locator",
                "Progress": 100,
                "CreateTime": "2023-01-04T18:45:41.509Z",
                "StartTime": "2023-01-04T18:45:41.741Z",
                "EndTime": "2023-01-04T18:45:45.353Z",
                "Status": "COMPLETED",
                "Type": "UserDefined",
                "CreateTimeEpoch": 1672854341509,
                "StartTimeEpoch": 1672854341741,
                "EndTimeEpoch": 1672854345353,
                "Running": false,
                "Completed": true,
                "Duration": "00:00:04"
            },
            {
                "__Output": {
                    "Status": "Green"
                },
                "Moid": "63b5c923696f6e2d30bd0b5d",
                "Name": "Turn On Locator",
                "Progress": 100,
                "CreateTime": "2023-01-04T18:44:51.803Z",
                "StartTime": "2023-01-04T18:44:52.467Z",
                "EndTime": "2023-01-04T18:44:57.964Z",
                "Status": "COMPLETED",
                "Type": "UserDefined",
                "CreateTimeEpoch": 1672854291803,
                "StartTimeEpoch": 1672854292467,
                "EndTimeEpoch": 1672854297964,
                "Running": false,
                "Completed": true,
                "Duration": "00:00:05"
            }
        ]
    },
    "FlagState": "P+ H",
    "FlagManagement": "CRi",
    "FlagWorkflow": "C2"
}
```

Developer output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --board

Developer output

{
    "duration": 15795,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 11604
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
        "lines": 466
    }
}

Log: isctl
-----------

2023-01-05 18:45:35.995483	True	3225	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:45:37.781437	True	1783	10	isctl get compute blade   -o json --top 100
2023-01-05 18:45:42.959471	True	1573	1	isctl get compute board --filter "ComputeRackUnit/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:45:44.542746	True	1580	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:45:46.184599	True	1639	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2023-01-05 18:45:47.994764	True	1804	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:45:46.000Z"  -o json --top 100
```
