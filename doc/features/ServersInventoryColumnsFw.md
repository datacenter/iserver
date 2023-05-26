# Extra server information - Firware Version

```
# iserver get servers --column fw --group p2b

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+---------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    | Fw      |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+---------+
| P+ H | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 4.2(2a) | 
| P+ H | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 2S 40C 80T | 384 [GiB] | 4.2(2a) | 
| P+ H | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | 2S 40C 80T | 384 [GiB] | 4.1(3d) | 
| P- H | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 2S 40C 80T | 384 [GiB] | 4.2(2a) | 
| P- H | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | 2S 40C 80T | 384 [GiB] | 4.2(2a) | 
| P- H | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | 2S 40C 80T | 384 [GiB] | 4.2(2a) | 
| P+ H | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 | 2S 40C 80T | 384 [GiB] | 4.2(2a) | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+---------+
```

JSON output

```
# iserver get servers --column fw --group p2b

[
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fdf9c016176752d35e44795",
        "DeviceMoId": "5fdf9be76f72612d300a8d81",
        "Name": "comp-1-p2b-eu-spdc-WZP23400AJW",
        "Model": "UCSC-C240-M5SN",
        "Serial": "WZP23400AJW",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
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
        "ManagementIp": "10.58.50.41",
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
        "Groups": "p2b,pod2b,power",
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
        "FirmwarewComponents": [
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/adaptor-MLOM/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "5.2(2b)"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/bios/fw-boot-loader",
                "Type": "blade-bios",
                "PackageVersion": "",
                "Version": "C240M5.4.2.2b.0.0613220203\n"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/board/storage-NVMe-PCIe-Switch/fw-system",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "1.8.0.58-24b3"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-boot-loader",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "7.19.00.0_0x07130200"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-system",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "51.19.0-4296"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/mgmt/fw-boot-loader",
                "Type": "blade-controller",
                "PackageVersion": "",
                "Version": "4.2(2a)"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/mgmt/fw-system",
                "Type": "blade-controller",
                "PackageVersion": "",
                "Version": "4.2(2a)"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-3/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x8000B900-1.826.0"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-6/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x8000B900-1.826.0"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-L/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x800016F9-1.826.0"
            }
        ],
        "FirmwareVersion": "4.2(2a)",
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fdf9c786176752d35e47110",
        "DeviceMoId": "5fdf9c676f72612d300a9c8d",
        "Name": "comp-2-p2b-eu-spdc-WZP23400AK4",
        "Model": "UCSC-C240-M5SN",
        "Serial": "WZP23400AK4",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
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
        "ManagementIp": "10.58.50.42",
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
        "Groups": "p2b,pod2b,power",
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
        "FirmwarewComponents": [
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/adaptor-MLOM/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "5.2(2b)"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/bios/fw-boot-loader",
                "Type": "blade-bios",
                "PackageVersion": "",
                "Version": "C240M5.4.2.2b.0.0613220203\n"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/board/storage-NVMe-PCIe-Switch/fw-system",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "1.8.0.58-24b3"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-boot-loader",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "7.19.00.0_0x07130200"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-system",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "51.19.0-4296"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/mgmt/fw-boot-loader",
                "Type": "blade-controller",
                "PackageVersion": "",
                "Version": "4.2(2a)"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/mgmt/fw-system",
                "Type": "blade-controller",
                "PackageVersion": "",
                "Version": "4.2(2a)"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-3/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x8000B900-1.826.0"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-6/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x8000B900-1.826.0"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-L/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x800016F9-1.826.0"
            }
        ],
        "FirmwareVersion": "4.2(2a)",
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fdf9d026176752d35e4ac4e",
        "DeviceMoId": "5fdf9cf26f72612d300aaca0",
        "Name": "comp-3-p2b-eu-spdc-WZP23400AKL",
        "Model": "UCSC-C240-M5SN",
        "Serial": "WZP23400AKL",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
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
        "ManagementIp": "10.58.50.43",
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
        "Groups": "p2b,pod2b,power",
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
        "FirmwarewComponents": [
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/adaptor-MLOM/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "5.1(3d)"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/bios/fw-boot-loader",
                "Type": "blade-bios",
                "PackageVersion": "",
                "Version": "C240M5.4.1.3i.0.0713210713\n"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/board/storage-NVMe-PCIe-Switch/fw-system",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "1.8.0.58-24b3"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-boot-loader",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "7.10.03.1_0x070A0402"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-system",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "51.10.0-3612"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/mgmt/fw-boot-loader",
                "Type": "blade-controller",
                "PackageVersion": "",
                "Version": "4.1(3d)"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/mgmt/fw-system",
                "Type": "blade-controller",
                "PackageVersion": "",
                "Version": "4.1(3d)"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-3/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x80009E5D-1.823.2"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-6/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x80009E5D-1.823.2"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-L/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x80001516-1.823.2"
            }
        ],
        "FirmwareVersion": "4.1(3d)",
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "5fdfa1806176752d35e678c2",
        "DeviceMoId": "5fdfa1686f72612d300b383f",
        "Name": "comp-4-p2b-eu-spdc-WMP240400FM",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WMP240400FM",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
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
        "ManagementIp": "10.58.50.44",
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
        "Groups": "p2b,pod2b,test,self-test-power,power",
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
        "FirmwarewComponents": [
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/bios/fw-boot-loader",
                "Type": "blade-bios",
                "PackageVersion": "",
                "Version": "C220M5.4.2.2b.0.0613220203\n"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-boot-loader",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "7.19.00.0_0x07130200"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-system",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "51.19.0-4296"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/mgmt/fw-boot-loader",
                "Type": "blade-controller",
                "PackageVersion": "",
                "Version": "4.2(2a)"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/mgmt/fw-system",
                "Type": "blade-controller",
                "PackageVersion": "",
                "Version": "4.2(2a)"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-1/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x8000B900-1.826.0"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-2/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x8000B900-1.826.0"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-L/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x800016F7-1.826.0"
            }
        ],
        "FirmwareVersion": "4.2(2a)",
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "5fdfdc3b6176752d35fce0a9",
        "DeviceMoId": "5fdfdc206f72612d30120ab4",
        "Name": "comp-5-p2b-eu-spdc-WMP2404000R",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WMP2404000R",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
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
        "ManagementIp": "10.58.50.45",
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
        "Groups": "p2b,pod2b,power",
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
        "FirmwarewComponents": [
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/bios/fw-boot-loader",
                "Type": "blade-bios",
                "PackageVersion": "",
                "Version": "C220M5.4.2.2b.0.0613220203\n"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-boot-loader",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "7.19.00.0_0x07130200"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-system",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "51.19.0-4296"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/mgmt/fw-boot-loader",
                "Type": "blade-controller",
                "PackageVersion": "",
                "Version": "4.2(2a)"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/mgmt/fw-system",
                "Type": "blade-controller",
                "PackageVersion": "",
                "Version": "4.2(2a)"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-1/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x8000B900-1.826.0"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-2/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x8000B900-1.826.0"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-L/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x800016F7-1.826.0"
            }
        ],
        "FirmwareVersion": "4.2(2a)",
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "5fdfe47f6176752d35001995",
        "DeviceMoId": "5fdfe4666f72612d30130510",
        "Name": "comp-6-p2b-eu-spdc-WMP24040059",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WMP24040059",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
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
        "ManagementIp": "10.58.50.46",
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
        "Groups": "p2b,pod2b,test,self-test-power,self-test-locator,power",
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
        "FirmwarewComponents": [
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/bios/fw-boot-loader",
                "Type": "blade-bios",
                "PackageVersion": "",
                "Version": "C220M5.4.2.2b.0.0613220203\n"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-boot-loader",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "7.19.00.0_0x07130200"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-system",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "51.19.0-4296"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/mgmt/fw-boot-loader",
                "Type": "blade-controller",
                "PackageVersion": "",
                "Version": "4.2(2a)"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/mgmt/fw-system",
                "Type": "blade-controller",
                "PackageVersion": "",
                "Version": "4.2(2a)"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-1/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x8000B900-1.826.0"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-2/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x8000B900-1.826.0"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-L/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x800016F7-1.826.0"
            }
        ],
        "FirmwareVersion": "4.2(2a)",
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fdfe80d6176752d3502b008",
        "DeviceMoId": "5fdfe7d86f72612d30136fed",
        "Name": "comp-7-p2b-eu-spdc-WMP24040061",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WMP24040061",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
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
        "ManagementIp": "10.58.50.47",
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
        "Groups": "p2b,pod2b,power",
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
        "FirmwarewComponents": [
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/adaptor-MLOM/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "5.2(2b)"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/bios/fw-boot-loader",
                "Type": "blade-bios",
                "PackageVersion": "",
                "Version": "C220M5.4.2.2b.0.0613220203\n"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-boot-loader",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "7.19.00.0_0x07130200"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/fw-system",
                "Type": "storage-controller",
                "PackageVersion": "",
                "Version": "51.19.0-4296"
            },
            {
                "Component": "boot-loader",
                "Dn": "sys/rack-unit-1/mgmt/fw-boot-loader",
                "Type": "blade-controller",
                "PackageVersion": "",
                "Version": "4.2(2a)"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/mgmt/fw-system",
                "Type": "blade-controller",
                "PackageVersion": "",
                "Version": "4.2(2a)"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-1/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x8000B900-1.826.0"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-2/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x8000B900-1.826.0"
            },
            {
                "Component": "system",
                "Dn": "sys/rack-unit-1/network-adapter-L/mgmt/fw-system",
                "Type": "adaptor",
                "PackageVersion": "",
                "Version": "0x800016F7-1.826.0"
            }
        ],
        "FirmwareVersion": "4.2(2a)",
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    }
]
```

Developer output

```
# iserver get servers --column fw --group p2b

Developer output

{
    "duration": 6261,
    "isctl": {
        "read": true,
        "calls": 13,
        "success": 13,
        "failed": 0,
        "total_time": 10294
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
        "lines": 56
    }
}

Log: isctl
-----------

2022-12-13 16:57:59.926586	True	2561	93	isctl get compute rackunit   -o json --top 100
2022-12-13 16:58:00.749837	True	822	10	isctl get compute blade   -o json --top 100
2022-12-13 16:58:01.261216	True	471	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 16:58:01.439195	True	637	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T16:58:00.000Z"  -o json --top 100
2022-12-13 16:58:01.583569	True	799	7	isctl get asset deviceregistration --filter "Moid in ('5fdf9be76f72612d300a8d81', '5fdf9c676f72612d300a9c8d', '5fdf9cf26f72612d300aaca0', '5fdfa1686f72612d300b383f', '5fdfdc206f72612d30120ab4', '5fdfe4666f72612d30130510', '5fdfe7d86f72612d30136fed')"  -o json --top 100
2022-12-13 16:58:01.966306	True	1084	63	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid in ('5fdf9be76f72612d300a8d81', '5fdf9c676f72612d300a9c8d', '5fdf9cf26f72612d300aaca0', '5fdfa1686f72612d300b383f', '5fdfdc206f72612d30120ab4', '5fdfe4666f72612d30130510', '5fdfe7d86f72612d30136fed')"  -o json --top 100
2022-12-13 16:58:02.486551	True	447	10	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdf9cf26f72612d300aaca0'"  -o json --top 100
2022-12-13 16:58:02.546315	True	517	10	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdf9c676f72612d300a9c8d'"  -o json --top 100
2022-12-13 16:58:02.752394	True	729	10	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2022-12-13 16:58:02.768915	True	735	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdfa1686f72612d300b383f'"  -o json --top 100
2022-12-13 16:58:02.939770	True	423	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdfdc206f72612d30120ab4'"  -o json --top 100
2022-12-13 16:58:02.970163	True	398	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdfe4666f72612d30130510'"  -o json --top 100
2022-12-13 16:58:03.459936	True	671	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdfe7d86f72612d30136fed'"  -o json --top 100
```
