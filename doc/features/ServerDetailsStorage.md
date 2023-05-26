# Server Details - Storage Information

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --storage

+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF (7d) | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | C2      | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+

Storage Summary
- Controllers            : 2
- Disks Count            : 10
- Capacity               : 11.03 [TB]
- HDD Count              : 6
- HDD Capacity           : 7.19 [TB]
- SSD Count              : 4
- SSD Capacity           : 3.84 [TB]
- Virtual Drive Count    : 1
- Virtual Drive Capacity : 1.2 [TB]


Storage Controller
- Model                : Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)
- Vendor               : LSI Logic
- Serial               : SK00188839
- Presence             : equipped
- Status               : 
- PCIe Address         : 
- PCI Slot             : MRAID
- Controller Id        : MRAID
- Name                 : storage-SAS-MRAID
- Dn                   : sys/rack-unit-1/board/storage-SAS-MRAID
- Raid Support         : yes
- Physical Disks Count : 10
- Virtual Drives Count : 1


Storage Controller
- Model                : 
- Vendor               : Cisco Systems Inc
- Serial               : 
- Presence             : equipped
- Status               : 
- PCIe Address         : 
- PCI Slot             : PCIe-Switch
- Controller Id        : PCIe-Switch
- Name                 : storage-NVMe-PCIe-Switch
- Dn                   : sys/rack-unit-1/board/storage-NVMe-PCIe-Switch
- Raid Support         : N/A
- Physical Disks Count : 0
- Virtual Drives Count : 0


+-------+---------+------------+------+----------+------------+-------------------+----------+----------------+---------+----------+----------------------+-------+----------+-----------------------------------------------+
| State | Disk Id | Size       | Type | Bootable | Link Speed | Controller        | Drive Id | Model          | Vendor  | Fw       | Serial               | State | Presence | Dn                                            |
+-------+---------+------------+------+----------+------------+-------------------+----------+----------------+---------+----------+----------------------+-------+----------+-----------------------------------------------+
| V     | 9       | 959.0 [GB] | SSD  | X        | 6.0 Gb/s   | storage-SAS-MRAID |          | SSDSC2KB960G7K | ATA     | SCV1CS08 | PHYS746002YU960CGN   | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-9  | 
| V     | 10      | 959.0 [GB] | SSD  | X        | 6.0 Gb/s   | storage-SAS-MRAID |          | SSDSC2KB960G7K | ATA     | SCV1CS08 | PHYS746002XE960CGN   | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-10 | 
| V     | 11      | 959.0 [GB] | SSD  | X        | 6.0 Gb/s   | storage-SAS-MRAID |          | SSDSC2KB960G7K | ATA     | SCV1CS08 | PHYS746002VN960CGN   | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-11 | 
| V     | 12      | 959.0 [GB] | SSD  | X        | 6.0 Gb/s   | storage-SAS-MRAID |          | SSDSC2KB960G7K | ATA     | SCV1CS08 | PHYS74610194960CGN   | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-12 | 
| V     | 13      | 1.2 [TB]   | HDD  | X        | 12.0 Gb/s  | storage-SAS-MRAID |          | ST1200MM0009   | SEAGATE | CN03     | WFK654680000C024C6NE | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-13 | 
| V     | 14      | 1.2 [TB]   | HDD  | X        | 12.0 Gb/s  | storage-SAS-MRAID |          | ST1200MM0009   | SEAGATE | CN03     | WFK65J9T0000C025976H | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-14 | 
| V     | 15      | 1.2 [TB]   | HDD  | X        | 12.0 Gb/s  | storage-SAS-MRAID |          | ST1200MM0009   | SEAGATE | CN03     | WFK65HVV0000C024KK59 | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-15 | 
| V     | 16      | 1.2 [TB]   | HDD  | X        | 12.0 Gb/s  | storage-SAS-MRAID |          | ST1200MM0009   | SEAGATE | CN03     | WFK65M390000C024KKSN | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-16 | 
| V     | 17      | 1.2 [TB]   | HDD  | X        | 12.0 Gb/s  | storage-SAS-MRAID | 0        | ST1200MM0009   | SEAGATE | CN03     | WFK654FJ0000C024KKCC | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-17 | 
| V     | 18      | 1.2 [TB]   | HDD  | X        | 12.0 Gb/s  | storage-SAS-MRAID | 0        | AL15SEB120N    | TOSHIBA | 5703     | Y9G0A06DFJMF         | Good  | equipped | sys/rack-unit-1/board/storage-SAS-MRAID/pd-18 | 
+-------+---------+------------+------+----------+------------+-------------------+----------+----------------+---------+----------+----------------------+-------+----------+-----------------------------------------------+

+-------+----------+----------+-------+--------+------+----------+---------------+-------------------+---------+----------------------------------------------+
| State | Drive Id | Size     | Disks | Type   | Name | Bootable | Write Cache   | Controller        | State   | Dn                                           |
+-------+----------+----------+-------+--------+------+----------+---------------+-------------------+---------+----------------------------------------------+
| V     | 0        | 1.2 [TB] | 2     | RAID 1 | vd-0 | V        | write-through | storage-SAS-MRAID | Optimal | sys/rack-unit-1/board/storage-SAS-MRAID/vd-0 | 
+-------+----------+----------+-------+--------+------+----------+---------------+-------------------+---------+----------------------------------------------+
```

JSON output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --storage

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
    "StorageControllersInfo": [
        {
            "__Output": {
                "Presence": "Green"
            },
            "Model": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
            "Moid": "635840e076752d31399d9215",
            "Vendor": "LSI Logic",
            "Serial": "SK00188839",
            "Presence": "equipped",
            "ControllerStatus": "",
            "PciAddr": "",
            "PciSlot": "MRAID",
            "ControllerId": "MRAID",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID",
            "RaidSupport": "yes",
            "Name": "storage-SAS-MRAID",
            "PhysicalDiskCount": 10,
            "PhysicalDiskIds": [
                "635840e576752d31399d9373",
                "635840e576752d31399d9375",
                "635840e576752d31399d9377",
                "635840e576752d31399d9379",
                "635840e576752d31399d937b",
                "635840e676752d31399d937d",
                "635840e676752d31399d937f",
                "635840e676752d31399d9381",
                "635840e676752d31399d9383",
                "635840e676752d31399d9385"
            ],
            "VirtualDriveCount": 1,
            "VirtualDriveIds": [
                "638f666f76752d3139f6cc14"
            ]
        },
        {
            "__Output": {
                "Presence": "Green"
            },
            "Model": "",
            "Moid": "636ddf1876752d3139c8d4f5",
            "Vendor": "Cisco Systems Inc",
            "Serial": "",
            "Presence": "equipped",
            "ControllerStatus": "",
            "PciAddr": "",
            "PciSlot": "PCIe-Switch",
            "ControllerId": "PCIe-Switch",
            "Dn": "sys/rack-unit-1/board/storage-NVMe-PCIe-Switch",
            "RaidSupport": "N/A",
            "Name": "storage-NVMe-PCIe-Switch",
            "PhysicalDiskCount": 0,
            "PhysicalDiskIds": [],
            "VirtualDriveCount": 0,
            "VirtualDriveIds": []
        }
    ],
    "StorageControllersCount": 2,
    "VirtualDisks": [
        {
            "__Output": {
                "Presence": "Red",
                "Operability": "Red",
                "DriveState": "Green",
                "BootableTick": "Green",
                "StateTick": "Green"
            },
            "Moid": "638f666f76752d3139f6cc14",
            "Name": "vd-0",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/vd-0",
            "Size": "1143455 MB",
            "Type": "RAID 1",
            "VirtualDriveId": "0",
            "Bootable": "true",
            "DriveState": "Optimal",
            "Operability": "",
            "Presence": "",
            "ActualWriteCachePolicy": "write-through",
            "ConfiguredWriteCachePolicy": "write-through",
            "IoPolicy": "",
            "_VirtualDriveId": 0,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "PhysicalDiskCount": 2,
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2713",
            "StateTick": "\u2713",
            "PhysicalDiskIds": [
                "17",
                "18"
            ]
        }
    ],
    "VirtualDiskCount": 1,
    "VirtualDiskCapacity": 1198999470080,
    "VirtualDiskCapacityUnit": "1.2 [TB]",
    "HddDisks": [
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d937b",
            "Bootable": "",
            "DiskId": "13",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-13",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK654680000C024C6NE",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 13,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d937d",
            "Bootable": "",
            "DiskId": "14",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-14",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK65J9T0000C025976H",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 14,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d937f",
            "Bootable": "",
            "DiskId": "15",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-15",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK65HVV0000C024KK59",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 15,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d9381",
            "Bootable": "",
            "DiskId": "16",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-16",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK65M390000C024KKSN",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 16,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d9383",
            "Bootable": "",
            "DiskId": "17",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-17",
            "DriveFirmware": "CN03",
            "DriveState": "Online",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK654FJ0000C024KKCC",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 17,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": "638f666f76752d3139f6cc14",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d9385",
            "Bootable": "",
            "DiskId": "18",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-18",
            "DriveFirmware": "5703",
            "DriveState": "Online",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "AL15SEB120N",
            "Pid": "AL15SEB120N",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "Y9G0A06DFJMF",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "TOSHIBA",
            "_DiskId": 18,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": "638f666f76752d3139f6cc14",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        }
    ],
    "HddDiskCount": 6,
    "HddDiskCapacity": 7193996820480,
    "HddDiskCapacityUnit": "7.19 [TB]",
    "SsdDisks": [
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9373",
            "Bootable": "",
            "DiskId": "9",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-9",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS746002YU960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 9,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9375",
            "Bootable": "",
            "DiskId": "10",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-10",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS746002XE960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 10,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9377",
            "Bootable": "",
            "DiskId": "11",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-11",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS746002VN960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 11,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9379",
            "Bootable": "",
            "DiskId": "12",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-12",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS74610194960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 12,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        }
    ],
    "SsdDiskCount": 4,
    "SsdDiskCapacity": 3835997192192,
    "SsdDiskCapacityUnit": "3.84 [TB]",
    "PhysicalDisks": [
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9373",
            "Bootable": "",
            "DiskId": "9",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-9",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS746002YU960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 9,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9375",
            "Bootable": "",
            "DiskId": "10",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-10",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS746002XE960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 10,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9377",
            "Bootable": "",
            "DiskId": "11",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-11",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS746002VN960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 11,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d9379",
            "Bootable": "",
            "DiskId": "12",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-12",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "PHYS74610194960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "_DiskId": 12,
            "SizeBytes": 958999298048,
            "SizeUnit": "959.0 [GB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e576752d31399d937b",
            "Bootable": "",
            "DiskId": "13",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-13",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK654680000C024C6NE",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 13,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d937d",
            "Bootable": "",
            "DiskId": "14",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-14",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK65J9T0000C025976H",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 14,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d937f",
            "Bootable": "",
            "DiskId": "15",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-15",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK65HVV0000C024KK59",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 15,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d9381",
            "Bootable": "",
            "DiskId": "16",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-16",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK65M390000C024KKSN",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 16,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d9383",
            "Bootable": "",
            "DiskId": "17",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-17",
            "DriveFirmware": "CN03",
            "DriveState": "Online",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "WFK654FJ0000C024KKCC",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "_DiskId": 17,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": "638f666f76752d3139f6cc14",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "Operability": "Red",
                "DiskState": "Green",
                "BootableTick": "Red",
                "StateTick": "Green"
            },
            "Moid": "635840e676752d31399d9385",
            "Bootable": "",
            "DiskId": "18",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-18",
            "DriveFirmware": "5703",
            "DriveState": "Online",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "AL15SEB120N",
            "Pid": "AL15SEB120N",
            "OperPowerState": "",
            "Operability": "",
            "Presence": "equipped",
            "Serial": "Y9G0A06DFJMF",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "TOSHIBA",
            "_DiskId": 18,
            "SizeBytes": 1198999470080,
            "SizeUnit": "1.2 [TB]",
            "VirtualDriveMoid": "638f666f76752d3139f6cc14",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID",
            "StorageControllerName": "storage-SAS-MRAID",
            "BootableTick": "\u2717",
            "StateTick": "\u2713"
        }
    ],
    "PhysicalDiskCount": 10,
    "PhysicalDiskCapacity": 11029994012672,
    "PhysicalDiskCapacityUnit": "11.03 [TB]",
    "StorageDrives": "2C 6H 4S 1VD",
    "StorageCapacity": "R 11.03 [TB] , VD 1.2 [TB]",
    "StorageSummary": "2C 6H 4S 1VD R11.03 [TB] L1.2 [TB]",
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
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --storage

Developer output

{
    "duration": 21844,
    "isctl": {
        "read": true,
        "calls": 8,
        "success": 8,
        "failed": 0,
        "total_time": 15168
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

2023-01-05 18:51:57.430677	True	3119	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:51:59.209638	True	1776	10	isctl get compute blade   -o json --top 100
2023-01-05 18:52:04.817333	True	2205	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:52:06.352188	True	1533	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2023-01-05 18:52:07.914551	True	1559	2	isctl get storage controller --filter "Parent/Moid eq '5fdf9c056176752d35e44930'"  -o json --top 100
2023-01-05 18:52:09.428328	True	1510	1	isctl get storage virtualdrive --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:52:12.949590	True	1914	10	isctl get storage physicaldisk --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:52:14.507872	True	1552	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:52:12.000Z"  -o json --top 100
```
