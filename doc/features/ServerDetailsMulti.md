# Server Details - Multiple Selected Information

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --cpu --memory --pci

+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF (7d) | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | C2      | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+

+-------+--------+--------+----------------------+------+------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+
| State | CPU Id | Socket | Vendor               | Arch | Model                                    | Cores | Enabled | Threads | Speed [GHz] | Stepping | Presence | OperState |
+-------+--------+--------+----------------------+------+------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+
| V     | 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | 
| V     | 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | 20    | 20      | 40      | 2.5         | 7        | equipped | operable  | 
+-------+--------+--------+----------------------+------+------------------------------------------+-------+---------+---------+-------------+----------+----------+-----------+

+-------+-----------+-------+------+----------+----------+-------------+---------+--------------+--------------+----------------------+----------+------------+----------+---------+
| State | Memory Id | Array | Bank | Location | Capacity | Clock       | Latency | Form Factor  | Type         | Model                | Serial   | Oper State | Presence | Thermal |
+-------+-----------+-------+------+----------+----------+-------------+---------+--------------+--------------+----------------------+----------+------------+----------+---------+
| V     | 1         | 1     | 0    | DIMM_A1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73490 | operable   | equipped |         | 
| X     | 2         | 1     | 0    | DIMM_A2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 3         | 1     | 0    | DIMM_B1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72CD9 | operable   | equipped |         | 
| X     | 4         | 1     | 0    | DIMM_B2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 5         | 1     | 0    | DIMM_C1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F7348D | operable   | equipped |         | 
| X     | 6         | 1     | 0    | DIMM_C2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 7         | 1     | 0    | DIMM_D1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F734A7 | operable   | equipped |         | 
| X     | 8         | 1     | 0    | DIMM_D2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 9         | 1     | 0    | DIMM_E1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73492 | operable   | equipped |         | 
| X     | 10        | 1     | 0    | DIMM_E2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 11        | 1     | 0    | DIMM_F1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73498 | operable   | equipped |         | 
| X     | 12        | 1     | 0    | DIMM_F2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 13        | 1     | 0    | DIMM_G1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F7348E | operable   | equipped |         | 
| X     | 14        | 1     | 0    | DIMM_G2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 15        | 1     | 0    | DIMM_H1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73495 | operable   | equipped |         | 
| X     | 16        | 1     | 0    | DIMM_H2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 17        | 1     | 0    | DIMM_J1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72CCC | operable   | equipped |         | 
| X     | 18        | 1     | 0    | DIMM_J2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 19        | 1     | 0    | DIMM_K1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73493 | operable   | equipped |         | 
| X     | 20        | 1     | 0    | DIMM_K2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 21        | 1     | 0    | DIMM_L1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73494 | operable   | equipped |         | 
| X     | 22        | 1     | 0    | DIMM_L2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
| V     | 23        | 1     | 0    | DIMM_M1  | 32 [GiB] | 2933        |         | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F734AD | operable   | equipped |         | 
| X     | 24        | 1     | 0    | DIMM_M2  |          | unspecified |         | undiscovered | undiscovered |                      |          | removed    | missing  |         | 
+-------+-----------+-------+------+----------+----------+-------------+---------+--------------+--------------+----------------------+----------+------------+----------+---------+

+------------------------------------------------------------------+-------------------+--------+--------+--------------------+-------------------------------------+
| PCI Device Model                                                 | Pid               | SlotId | Vendor | Firmware           | Dn                                  |
+------------------------------------------------------------------+-------------------+--------+--------+--------------------+-------------------------------------+
| Cisco(R) Ethernet Converged NIC XXV710-DA2                       | UCSC-PCIE-ID25GF  | 3      | 0x8086 | 0x8000B900-1.826.0 | sys/rack-unit-1/equipped-slot-3     | 
| Cisco(R) Ethernet Converged NIC XXV710-DA2                       | UCSC-PCIE-ID25GF  | 6      | 0x8086 | 0x8000B900-1.826.0 | sys/rack-unit-1/equipped-slot-6     | 
| Intel X550 LOM                                                   | UNKNOWN           | L      | 0x8086 | 0x800016F9-1.826.0 | sys/rack-unit-1/equipped-slot-L     | 
| Cisco UCS VIC 1457 MLOM                                          | UCSC-MLOM-C25Q-04 | MLOM   | 0x1137 | 5.2(2b)            | sys/rack-unit-1/equipped-slot-MLOM  | 
| Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | UCSC-RAID-M5      | MRAID  | 0x1000 | N/A                | sys/rack-unit-1/equipped-slot-MRAID | 
+------------------------------------------------------------------+-------------------+--------+--------+--------------------+-------------------------------------+
```

JSON output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --cpu --memory --pci

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
    "CpuInfo": [
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "Architecture": "Xeon",
            "Model": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
            "NumCores": 20,
            "NumCoresEnabled": "20",
            "NumThreads": "40",
            "OperState": "operable",
            "Presence": "equipped",
            "ProcessorId": 1,
            "SocketDesignation": "CPU1",
            "Speed": 2.5,
            "Stepping": "7",
            "Vendor": "Intel(R) Corporation",
            "Thermal": "",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "Architecture": "Xeon",
            "Model": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
            "NumCores": 20,
            "NumCoresEnabled": "20",
            "NumThreads": "40",
            "OperState": "operable",
            "Presence": "equipped",
            "ProcessorId": 2,
            "SocketDesignation": "CPU2",
            "Speed": 2.5,
            "Stepping": "7",
            "Vendor": "Intel(R) Corporation",
            "Thermal": "",
            "StateTick": "\u2713"
        }
    ],
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
    "MemoryInfo": [
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-1",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_A1",
            "MemoryId": 1,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73490",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-2",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_A2",
            "MemoryId": 2,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-3",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_B1",
            "MemoryId": 3,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F72CD9",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-4",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_B2",
            "MemoryId": 4,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-5",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_C1",
            "MemoryId": 5,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F7348D",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-6",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_C2",
            "MemoryId": 6,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-7",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_D1",
            "MemoryId": 7,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F734A7",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-8",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_D2",
            "MemoryId": 8,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-9",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_E1",
            "MemoryId": 9,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73492",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-10",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_E2",
            "MemoryId": 10,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-11",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_F1",
            "MemoryId": 11,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73498",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-12",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_F2",
            "MemoryId": 12,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-13",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_G1",
            "MemoryId": 13,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F7348E",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-14",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_G2",
            "MemoryId": 14,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-15",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_H1",
            "MemoryId": 15,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73495",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-16",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_H2",
            "MemoryId": 16,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-17",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_J1",
            "MemoryId": 17,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F72CCC",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-18",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_J2",
            "MemoryId": 18,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-19",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_K1",
            "MemoryId": 19,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73493",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-20",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_K2",
            "MemoryId": 20,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-21",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_L1",
            "MemoryId": 21,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73494",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-22",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_L2",
            "MemoryId": 22,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "StateTick": "Green"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-23",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_M1",
            "MemoryId": 23,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F734AD",
            "Speed": "",
            "Thermal": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "LatencyUnit": "",
            "CapacityUnit": "32 [GiB]",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "StateTick": "Red"
            },
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-24",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_M2",
            "MemoryId": 24,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Thermal": "",
            "Type": "undiscovered",
            "Vendor": "",
            "LatencyUnit": "",
            "CapacityUnit": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930",
            "StateTick": "\u2717"
        }
    ],
    "PciDevicesInfo": [
        {
            "Model": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
            "Pid": "UCSC-PCIE-ID25GF",
            "SlotId": "3",
            "Vendor": "0x8086",
            "FirmwareVersion": "0x8000B900-1.826.0",
            "Dn": "sys/rack-unit-1/equipped-slot-3",
            "Serial": ""
        },
        {
            "Model": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
            "Pid": "UCSC-PCIE-ID25GF",
            "SlotId": "6",
            "Vendor": "0x8086",
            "FirmwareVersion": "0x8000B900-1.826.0",
            "Dn": "sys/rack-unit-1/equipped-slot-6",
            "Serial": ""
        },
        {
            "Model": "Intel X550 LOM",
            "Pid": "UNKNOWN",
            "SlotId": "L",
            "Vendor": "0x8086",
            "FirmwareVersion": "0x800016F9-1.826.0",
            "Dn": "sys/rack-unit-1/equipped-slot-L",
            "Serial": ""
        },
        {
            "Model": "Cisco UCS VIC 1457 MLOM",
            "Pid": "UCSC-MLOM-C25Q-04",
            "SlotId": "MLOM",
            "Vendor": "0x1137",
            "FirmwareVersion": "5.2(2b)",
            "Dn": "sys/rack-unit-1/equipped-slot-MLOM",
            "Serial": ""
        },
        {
            "Model": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
            "Pid": "UCSC-RAID-M5",
            "SlotId": "MRAID",
            "Vendor": "0x1000",
            "FirmwareVersion": "N/A",
            "Dn": "sys/rack-unit-1/equipped-slot-MRAID",
            "Serial": ""
        }
    ],
    "PciModels": [
        "UCSC-MLOM-C25Q-04",
        "UCSC-RAID-M5",
        "Intel X550 LOM",
        "UCSC-PCIE-ID25GF",
        "UCSC-PCIE-ID25GF"
    ],
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
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --cpu --memory --pci

Developer output

{
    "duration": 18579,
    "isctl": {
        "read": true,
        "calls": 8,
        "success": 8,
        "failed": 0,
        "total_time": 13558
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

2023-01-05 18:56:42.818344	True	2954	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:56:44.606931	True	1786	10	isctl get compute blade   -o json --top 100
2023-01-05 18:56:48.988842	True	1485	2	isctl get processor unit --filter "ComputeBoard/Moid eq '5fdf9c056176752d35e44930'"  -o json --top 100
2023-01-05 18:56:50.505017	True	1514	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:56:52.119118	True	1612	24	isctl get memory unit --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:56:53.445253	True	1320	5	isctl get pci device --filter "Parent/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:56:54.832241	True	1376	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2023-01-05 18:56:56.350192	True	1511	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:56:54.000Z"  -o json --top 100
```
