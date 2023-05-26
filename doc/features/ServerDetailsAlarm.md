# Server Details - Alarm

```
# iserver get server --name comp7-p3b-eu-spdc-FCH2023V2A4 --alarm

+---------+-----+---------+-------------------------------+-------------------+-------------+-------------+------------+-----------+
| SF      | MF  | WF (7d) | Name                          | Model             | Serial      | IP          | CPU        | Memory    |
+---------+-----+---------+-------------------------------+-------------------+-------------+-------------+------------+-----------+
| P+ C(1) | CRi |         | comp7-p3b-eu-spdc-FCH2023V2A4 | (R) UCSC-C220-M4S | FCH2023V2A4 | 10.58.50.60 | 2S 28C 56T | 256 [GiB] | 
+---------+-----+---------+-------------------------------+-------------------+-------------+-------------+------------+-----------+

Alarm Summary
-------------
- Critical : 1
- Warning  : 1
- Info     : 1


Alarm UCS-F0999
---------------
- Severity      : Critical
- Description   : Storage Raid Battery SLOT-HBA relearn failed: Learn cycle failed
- Create Time   : 2022-11-24T11:40:33.895Z
- Affected Type : storage.Controller
- Affected Name : comp7-p3b-eu-spdc-FCH2023V2A4/sys/rack-unit-1/board/storage-SAS-SLOT-HBA/raid-battery


Alarm UCS-F1258
---------------
- Severity      : Info
- Description   : Flex Flash Local disk 2 is inoperable: reseat or replace the local disk 2
- Create Time   : 2022-11-24T11:40:33.912Z
- Affected Type : storage.FlexFlashPhysicalDrive
- Affected Name : comp7-p3b-eu-spdc-FCH2023V2A4/sys/rack-unit-1/board/storage-flexflash-FlexFlash-0/card-2


Alarm UCS-F1260
---------------
- Severity      : Warning
- Description   : Flex Flash Virtual Drive 1 (Hypervisor) Degraded: please check the flash device or the controller
- Create Time   : 2022-11-24T11:40:33.929Z
- Affected Type : storage.FlexFlashVirtualDrive
- Affected Name : comp7-p3b-eu-spdc-FCH2023V2A4/sys/rack-unit-1/board/storage-flexflash-FlexFlash-0/vd-1
```

JSON output

```
# iserver get server --name comp7-p3b-eu-spdc-FCH2023V2A4 --alarm

{
    "__Output": {
        "FlagState": ":GG.RRRR",
        "FlagManagement": ":GGY",
        "FlagWorkflow": ":"
    },
    "Moid": "637f588776752d313966cb9d",
    "DeviceMoId": "637f58116f72612d31490de7",
    "Name": "comp7-p3b-eu-spdc-FCH2023V2A4",
    "Model": "UCSC-C220-M4S",
    "Serial": "FCH2023V2A4",
    "ManagementMode": "IntersightStandalone",
    "OperPowerState": "on",
    "Type": "Rack",
    "TypeModel": "(R) UCSC-C220-M4S",
    "AlarmInfo": [
        {
            "__Output": {
                "Severity": "Red"
            },
            "AffectedType": "storage.Controller",
            "AffectedMoid": "637f5aea76752d3139673975",
            "AffectedName": "comp7-p3b-eu-spdc-FCH2023V2A4/sys/rack-unit-1/board/storage-SAS-SLOT-HBA/raid-battery",
            "AncestorMoId": "637f588776752d313966cb9d",
            "AncestorMoType": "compute.RackUnit",
            "CreateTime": "2022-11-24T11:40:33.895Z",
            "Description": "Storage Raid Battery SLOT-HBA relearn failed: Learn cycle failed",
            "Moid": "637f583165696e2d3252ce2e",
            "Name": "UCS-F0999",
            "Code": "F0999",
            "Severity": "Critical"
        },
        {
            "__Output": {
                "Severity": "Blue"
            },
            "AffectedType": "storage.FlexFlashPhysicalDrive",
            "AffectedMoid": "637f5aea76752d3139673991",
            "AffectedName": "comp7-p3b-eu-spdc-FCH2023V2A4/sys/rack-unit-1/board/storage-flexflash-FlexFlash-0/card-2",
            "AncestorMoId": "637f588776752d313966cb9d",
            "AncestorMoType": "compute.RackUnit",
            "CreateTime": "2022-11-24T11:40:33.912Z",
            "Description": "Flex Flash Local disk 2 is inoperable: reseat or replace the local disk 2",
            "Moid": "637f583165696e2d3252ce34",
            "Name": "UCS-F1258",
            "Code": "F1258",
            "Severity": "Info"
        },
        {
            "__Output": {
                "Severity": "Yellow"
            },
            "AffectedType": "storage.FlexFlashVirtualDrive",
            "AffectedMoid": "637f5aeb76752d31396739c0",
            "AffectedName": "comp7-p3b-eu-spdc-FCH2023V2A4/sys/rack-unit-1/board/storage-flexflash-FlexFlash-0/vd-1",
            "AncestorMoId": "637f588776752d313966cb9d",
            "AncestorMoType": "compute.RackUnit",
            "CreateTime": "2022-11-24T11:40:33.929Z",
            "Description": "Flex Flash Virtual Drive 1 (Hypervisor) Degraded: please check the flash device or the controller",
            "Moid": "637f583165696e2d3252ce37",
            "Name": "UCS-F1260",
            "Code": "F1260",
            "Severity": "Warning"
        }
    ],
    "NumCpus": 2,
    "NumCpuCores": 28,
    "NumThreads": 56,
    "Cpu": "2S 28C 56T",
    "Groups": "",
    "AlarmSummary": {
        "__Output": {
            "Critical": "Red",
            "Warning": "Yellow",
            "Info": "Blue",
            "Cleared": "Green"
        },
        "Critical": 1,
        "Warning": 1,
        "Info": 1
    },
    "Health": "Critical (1)",
    "LocatorLedOn": false,
    "ManagementIp": "10.58.50.60",
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
    "Connected": true,
    "Workflow": {
        "Days": 7,
        "Running": null,
        "LatestMoid": null,
        "Last": []
    },
    "FlagState": "P+ C(1)",
    "FlagManagement": "CRi",
    "FlagWorkflow": ""
}
```

Developer output

```
# iserver get server --name comp7-p3b-eu-spdc-FCH2023V2A4 --alarm

Developer output

{
    "duration": 14287,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 10049
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
        "lines": 439
    }
}

Log: isctl
-----------

2023-01-05 18:45:16.811544	True	2560	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:45:18.406716	True	1591	10	isctl get compute blade   -o json --top 100
2023-01-05 18:45:23.406271	True	1505	3	isctl get cond alarm --filter "RegisteredDevice/Moid eq '637f58116f72612d31490de7'"  -o json --top 100
2023-01-05 18:45:24.948193	True	1539	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '637f58116f72612d31490de7'"  -o json --top 100
2023-01-05 18:45:26.329259	True	1377	1	isctl get asset deviceregistration  moid 637f58116f72612d31490de7 -o json
2023-01-05 18:45:27.811293	True	1477	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:45:26.000Z"  -o json --top 100
```
