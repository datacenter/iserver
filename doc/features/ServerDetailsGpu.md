# Server Details - GPU

```
# iserver get server --name comp2-p4b-eu-spdc-WZP26360D3D --gpu

+------+-----+---------+-------------------------------+--------------------+-------------+-------------+--------------+-----------+
| SF   | MF  | WF (7d) | Name                          | Model              | Serial      | IP          | CPU          | Memory    |
+------+-----+---------+-------------------------------+--------------------+-------------+-------------+--------------+-----------+
| P+ H | Cri |         | comp2-p4b-eu-spdc-WZP26360D3D | (R) UCSC-C245-M6SX | WZP26360D3D | 10.58.53.34 | 2S 128C 256T | 512 [GiB] | 
+------+-----+---------+-------------------------------+--------------------+-------------+-------------+--------------+-----------+

+------------------------------+--------------+--------+--------+----------+---------------------------------+
| GPU Device Model             | Pid          | SlotId | Vendor | Firmware | Dn                              |
+------------------------------+--------------+--------+--------+----------+---------------------------------+
| NVIDIA A16 PCIe FHFL DS 250W | UCSC-GPU-A16 | 7      | 0x10de | N/A      | sys/rack-unit-1/equipped-slot-7 | 
+------------------------------+--------------+--------+--------+----------+---------------------------------+
```

JSON output

```
# iserver get server --name comp2-p4b-eu-spdc-WZP26360D3D --gpu

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
    "PciModels": [
        "UCS-NVMEI4-I1920",
        "UCS-NVMEI4-I1920",
        "UCS-NVMEI4-I1920",
        "UCSC-M-V100-04",
        "UCS-M2-HWRAID",
        "UCSC-PCIE-C25Q-04",
        "UCSC-GPU-A16",
        "UCSC-RAID-M6SD",
        "UCS-NVMEI4-I1920"
    ],
    "GpuInfo": [
        {
            "Model": "NVIDIA A16 PCIe FHFL DS 250W",
            "Pid": "UCSC-GPU-A16",
            "SlotId": "7",
            "Vendor": "0x10de",
            "FirmwareVersion": "N/A",
            "Dn": "sys/rack-unit-1/equipped-slot-7",
            "Serial": ""
        }
    ],
    "Connected": true,
    "Workflow": {
        "Days": 7,
        "Running": null,
        "LatestMoid": null,
        "Last": []
    },
    "FlagState": "P+ H",
    "FlagManagement": "Cri",
    "FlagWorkflow": ""
}
```

Developer output

```
# iserver get server --name comp2-p4b-eu-spdc-WZP26360D3D --gpu

Developer output

{
    "duration": 14866,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 11294
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

2023-01-05 18:48:46.288403	True	3552	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:48:47.805597	True	1512	10	isctl get compute blade   -o json --top 100
2023-01-05 18:48:52.507360	True	1524	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '6384d44a6f72612d317bfc51'"  -o json --top 100
2023-01-05 18:48:54.077399	True	1568	9	isctl get pci device --filter "Parent/Moid eq '6384d45476752d31395c7874'"  -o json --top 100
2023-01-05 18:48:55.529793	True	1447	1	isctl get asset deviceregistration  moid 6384d44a6f72612d317bfc51 -o json
2023-01-05 18:48:57.224513	True	1691	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:48:55.000Z"  -o json --top 100
```
