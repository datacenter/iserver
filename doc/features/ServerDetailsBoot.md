# Server Details - Boot

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --boot

+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF (7d) | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | C2      | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+

Boot Settings
-------------
- Configured Boot Mode : Legacy
- Actual Boot Mode     : Legacy
- Secure Boot          : disabled


+-------+----------+----------+----------+
| Order | Name     | Type     | State    |
+-------+----------+----------+----------+
| 1     | localhdd | LOCALHDD | Disabled | 
| 2     | pxeboot  | PXE      | Disabled | 
| 3     | vmedia   | VMEDIA   | Disabled | 
+-------+----------+----------+----------+
```

JSON output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --boot

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
    "BootInfo": {
        "ConfiguredBootMode": "Legacy",
        "ActualBootMode": "Legacy",
        "SecureBoot": "disabled",
        "Order": [
            {
                "Moid": "60000c0b6176752d35b76e3e",
                "Name": "localhdd",
                "Order": 1,
                "State": "Disabled",
                "Type": "LOCALHDD"
            },
            {
                "Moid": "60000c046176752d35b76bb3",
                "Name": "pxeboot",
                "Order": 2,
                "State": "Disabled",
                "Type": "PXE"
            },
            {
                "Moid": "6013f1496176752d35458e49",
                "Name": "vmedia",
                "Order": 3,
                "State": "Disabled",
                "Type": "VMEDIA"
            }
        ]
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
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --boot

Developer output

{
    "duration": 23896,
    "isctl": {
        "read": true,
        "calls": 11,
        "success": 11,
        "failed": 0,
        "total_time": 19451
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

2023-01-05 18:45:55.922849	True	3437	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:45:57.790452	True	1865	10	isctl get compute blade   -o json --top 100
2023-01-05 18:46:03.361011	True	1664	1	isctl get boot devicebootmode --filter "ComputeRackUnit/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:46:04.836840	True	1473	1	isctl get bios bootmode --filter "ComputeRackUnit/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:46:06.340087	True	1501	1	isctl get boot devicebootsecurity --filter "ComputePhysical/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:46:07.957372	True	1613	1	isctl get boot hdddevice --filter "ComputePhysical/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:46:09.289406	True	1329	1	isctl get boot pxedevice --filter "ComputePhysical/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:46:10.826554	True	1535	1	isctl get boot vmediadevice --filter "ComputePhysical/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:46:12.784893	True	1953	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:46:14.164219	True	1373	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2023-01-05 18:46:15.875210	True	1708	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:46:14.000Z"  -o json --top 100
```
