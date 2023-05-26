# Server Details - Memory Information

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --memory

+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF (7d) | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | C2      | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+

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
```

JSON output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --memory

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
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --memory

Developer output

{
    "duration": 17617,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 11639
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

2023-01-05 18:49:56.177599	True	3262	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:49:57.748453	True	1567	10	isctl get compute blade   -o json --top 100
2023-01-05 18:50:03.271218	True	1819	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:50:05.051492	True	1777	24	isctl get memory unit --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:50:06.582294	True	1524	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2023-01-05 18:50:08.279602	True	1690	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:50:06.000Z"  -o json --top 100
```
