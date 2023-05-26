# Server Details - Fan Information

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --fan

+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF (7d) | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | C2      | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+

+-------+---------------+-----------+----------+--------------------------------+
| State | Fan Module Id | OperState | Presence | Dn                             |
+-------+---------------+-----------+----------+--------------------------------+
| V     | 1             | operable  | equipped | sys/rack-unit-1/fan-module-1-1 | 
| V     | 2             | operable  | equipped | sys/rack-unit-1/fan-module-1-2 | 
| V     | 3             | operable  | equipped | sys/rack-unit-1/fan-module-1-3 | 
| V     | 4             | operable  | equipped | sys/rack-unit-1/fan-module-1-4 | 
| V     | 5             | operable  | equipped | sys/rack-unit-1/fan-module-1-5 | 
| V     | 6             | operable  | equipped | sys/rack-unit-1/fan-module-1-6 | 
| X     | 7             | unknown   | missing  | sys/rack-unit-1/fan-module-1-7 | 
+-------+---------------+-----------+----------+--------------------------------+
```

JSON output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --fan

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
    "FanInfo": [
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "On": "Green",
                "StateTick": "Green"
            },
            "Moid": "5fdf9c106176752d35e44d77",
            "ModuleId": 1,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-1",
            "On": true,
            "Name": "Fan Module 1",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e57",
                "5fdf9c126176752d35e44e6d"
            ],
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "On": "Green",
                "StateTick": "Green"
            },
            "Moid": "5fdf9c106176752d35e44d79",
            "ModuleId": 2,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-2",
            "On": true,
            "Name": "Fan Module 2",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e59",
                "5fdf9c126176752d35e44e65"
            ],
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "On": "Green",
                "StateTick": "Green"
            },
            "Moid": "5fdf9c106176752d35e44d7b",
            "ModuleId": 3,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-3",
            "On": true,
            "Name": "Fan Module 3",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e5f",
                "5fdf9c126176752d35e44e6f"
            ],
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "On": "Green",
                "StateTick": "Green"
            },
            "Moid": "5fdf9c106176752d35e44d7d",
            "ModuleId": 4,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-4",
            "On": true,
            "Name": "Fan Module 4",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e5b",
                "5fdf9c126176752d35e44e67"
            ],
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "On": "Green",
                "StateTick": "Green"
            },
            "Moid": "5fdf9c106176752d35e44d71",
            "ModuleId": 5,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-5",
            "On": true,
            "Name": "Fan Module 5",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e61",
                "5fdf9c126176752d35e44e69"
            ],
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Green",
                "OperState": "Green",
                "On": "Green",
                "StateTick": "Green"
            },
            "Moid": "5fdf9c106176752d35e44d73",
            "ModuleId": 6,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-6",
            "On": true,
            "Name": "Fan Module 6",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e5d",
                "5fdf9c126176752d35e44e63"
            ],
            "StateTick": "\u2713"
        },
        {
            "__Output": {
                "Presence": "Red",
                "OperState": "Red",
                "On": "Red",
                "StateTick": "Red"
            },
            "Moid": "5fdf9c106176752d35e44d75",
            "ModuleId": 7,
            "OperState": "unknown",
            "Presence": "missing",
            "Dn": "sys/rack-unit-1/fan-module-1-7",
            "On": false,
            "Name": "Fan Module 7",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e6b",
                "5fdf9c126176752d35e44e71"
            ],
            "StateTick": "\u2717"
        }
    ],
    "FanOn": 6,
    "FanCount": 7,
    "FanSummary": "6/7",
    "FanHealthy": false,
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
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --fan

Developer output

{
    "duration": 16911,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 11946
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

2023-01-05 18:48:03.779182	True	3242	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:48:05.601064	True	1819	10	isctl get compute blade   -o json --top 100
2023-01-05 18:48:11.261337	True	1701	7	isctl get equipment fanmodule --filter "Parent/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2023-01-05 18:48:12.833458	True	1568	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 18:48:14.632105	True	1778	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2023-01-05 18:48:16.475364	True	1838	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:48:14.000Z"  -o json --top 100
```
