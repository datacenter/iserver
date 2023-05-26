# Server Details - Firmware Information

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --fw

+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+---------+
| SF   | MF  | WF (7d) | Name                           | Model              | Serial      | IP          | CPU        | Memory    | Fw      |
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+---------+
| P+ H | CRi | C2      | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 4.2(2a) | 
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+---------+

+--------------------+-------------+--------------------+----------------------------+----------------------------------------------------------+
| Name               | Component   | Type               | Version                    | Dn                                                       |
+--------------------+-------------+--------------------+----------------------------+----------------------------------------------------------+
| Adapter            | system      | adaptor            | 5.2(2b)                    | sys/rack-unit-1/adaptor-MLOM/mgmt/fw-system              | 
| Adapter            | system      | adaptor            | 0x8000B900-1.826.0         | sys/rack-unit-1/network-adapter-3/mgmt/fw-system         | 
| Adapter            | system      | adaptor            | 0x8000B900-1.826.0         | sys/rack-unit-1/network-adapter-6/mgmt/fw-system         | 
| Adapter            | system      | adaptor            | 0x800016F9-1.826.0         | sys/rack-unit-1/network-adapter-L/mgmt/fw-system         | 
| BIOS               | boot-loader | blade-bios         | C240M5.4.2.2b.0.0613220203 | sys/rack-unit-1/bios/fw-boot-loader                      | 
| Board Controller   | boot-loader | blade-controller   | 4.2(2a)                    | sys/rack-unit-1/mgmt/fw-boot-loader                      | 
| CIMC Controller    | system      | blade-controller   | 4.2(2a)                    | sys/rack-unit-1/mgmt/fw-system                           | 
| Storage Controller | system      | storage-controller | 1.8.0.58-24b3              | sys/rack-unit-1/board/storage-NVMe-PCIe-Switch/fw-system | 
| Storage Controller | boot-loader | storage-controller | 7.19.00.0_0x07130200       | sys/rack-unit-1/board/storage-SAS-MRAID/fw-boot-loader   | 
| Storage Controller | system      | storage-controller | 51.19.0-4296               | sys/rack-unit-1/board/storage-SAS-MRAID/fw-system        | 
+--------------------+-------------+--------------------+----------------------------+----------------------------------------------------------+
```

JSON output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --fw

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
    "NumCpus": 2,
    "NumCpuCores": 40,
    "NumThreads": 80,
    "Cpu": "2S 40C 80T",
    "FirmwarewComponents": [
        {
            "Component": "system",
            "Dn": "sys/rack-unit-1/adaptor-MLOM/mgmt/fw-system",
            "Type": "adaptor",
            "PackageVersion": "",
            "Version": "5.2(2b)",
            "Name": "Adapter"
        },
        {
            "Component": "system",
            "Dn": "sys/rack-unit-1/network-adapter-3/mgmt/fw-system",
            "Type": "adaptor",
            "PackageVersion": "",
            "Version": "0x8000B900-1.826.0",
            "Name": "Adapter"
        },
        {
            "Component": "system",
            "Dn": "sys/rack-unit-1/network-adapter-6/mgmt/fw-system",
            "Type": "adaptor",
            "PackageVersion": "",
            "Version": "0x8000B900-1.826.0",
            "Name": "Adapter"
        },
        {
            "Component": "system",
            "Dn": "sys/rack-unit-1/network-adapter-L/mgmt/fw-system",
            "Type": "adaptor",
            "PackageVersion": "",
            "Version": "0x800016F9-1.826.0",
            "Name": "Adapter"
        },
        {
            "Component": "boot-loader",
            "Dn": "sys/rack-unit-1/bios/fw-boot-loader",
            "Type": "blade-bios",
            "PackageVersion": "",
            "Version": "C240M5.4.2.2b.0.0613220203",
            "Name": "BIOS"
        },
        {
            "Component": "boot-loader",
            "Dn": "sys/rack-unit-1/mgmt/fw-boot-loader",
            "Type": "blade-controller",
            "PackageVersion": "",
            "Version": "4.2(2a)",
            "Name": "Board Controller"
        },
        {
            "Component": "system",
            "Dn": "sys/rack-unit-1/mgmt/fw-system",
            "Type": "blade-controller",
            "PackageVersion": "",
            "Version": "4.2(2a)",
            "Name": "CIMC Controller"
        },
        {
            "Component": "system",
            "Dn": "sys/rack-unit-1/board/storage-NVMe-PCIe-Switch/fw-system",
            "Type": "storage-controller",
            "PackageVersion": "",
            "Version": "1.8.0.58-24b3",
            "Name": "Storage Controller"
        },
        {
            "Component": "boot-loader",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-boot-loader",
            "Type": "storage-controller",
            "PackageVersion": "",
            "Version": "7.19.00.0_0x07130200",
            "Name": "Storage Controller"
        },
        {
            "Component": "system",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-system",
            "Type": "storage-controller",
            "PackageVersion": "",
            "Version": "51.19.0-4296",
            "Name": "Storage Controller"
        }
    ],
    "FirmwareVersion": "4.2(2a)",
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
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --fw

Developer output

{
    "duration": 17840,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 12968
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

2023-01-05 18:48:25.189522	True	3701	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:48:27.240081	True	2048	10	isctl get compute blade   -o json --top 100
2023-01-05 18:48:33.025879	True	1605	10	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:48:35.023311	True	1988	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:48:36.753300	True	1723	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2023-01-05 18:48:38.661206	True	1903	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:48:36.000Z"  -o json --top 100
```
