# Extra server information - Fan state

```
# iserver get servers --column fan --group p2b

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+-----+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    | Fan |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+-----+
| P+ H | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 6/7 | 
| P+ H | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 2S 40C 80T | 384 [GiB] | 6/7 | 
| P+ H | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | 2S 40C 80T | 384 [GiB] | 6/7 | 
| P- H | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 2S 40C 80T | 384 [GiB] | 0/7 | 
| P- H | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | 2S 40C 80T | 384 [GiB] | 0/7 | 
| P- H | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | 2S 40C 80T | 384 [GiB] | 0/7 | 
| P+ H | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 | 2S 40C 80T | 384 [GiB] | 7/7 | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+-----+
```

JSON output

```
# iserver get servers --column fan --group p2b

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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "LocatorLedOn": false,
        "FanInfo": [
            {
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
                ]
            },
            {
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
                ]
            },
            {
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
                ]
            },
            {
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
                ]
            },
            {
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
                ]
            },
            {
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
                ]
            },
            {
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
                ]
            }
        ],
        "FanOn": 6,
        "FanCount": 7,
        "FanSummary": "6/7",
        "FanHealthy": false,
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "LocatorLedOn": false,
        "FanInfo": [
            {
                "Moid": "5fdf9c876176752d35e4777c",
                "ModuleId": 1,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-1",
                "On": true,
                "Name": "Fan Module 1",
                "FanCount": 2,
                "FanMoids": [
                    "5fdf9c8a6176752d35e478a4",
                    "5fdf9c8a6176752d35e478b2"
                ]
            },
            {
                "Moid": "5fdf9c876176752d35e4777e",
                "ModuleId": 2,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-2",
                "On": true,
                "Name": "Fan Module 2",
                "FanCount": 2,
                "FanMoids": [
                    "5fdf9c8a6176752d35e478a0",
                    "5fdf9c8a6176752d35e478ac"
                ]
            },
            {
                "Moid": "5fdf9c876176752d35e47780",
                "ModuleId": 3,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-3",
                "On": true,
                "Name": "Fan Module 3",
                "FanCount": 2,
                "FanMoids": [
                    "5fdf9c8a6176752d35e478a8",
                    "5fdf9c8a6176752d35e478ae"
                ]
            },
            {
                "Moid": "5fdf9c876176752d35e47782",
                "ModuleId": 4,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-4",
                "On": true,
                "Name": "Fan Module 4",
                "FanCount": 2,
                "FanMoids": [
                    "5fdf9c8a6176752d35e478aa",
                    "5fdf9c8a6176752d35e478b4"
                ]
            },
            {
                "Moid": "5fdf9c876176752d35e47784",
                "ModuleId": 5,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-5",
                "On": true,
                "Name": "Fan Module 5",
                "FanCount": 2,
                "FanMoids": [
                    "5fdf9c8a6176752d35e4789a",
                    "5fdf9c8a6176752d35e478a2"
                ]
            },
            {
                "Moid": "5fdf9c876176752d35e47786",
                "ModuleId": 6,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-6",
                "On": true,
                "Name": "Fan Module 6",
                "FanCount": 2,
                "FanMoids": [
                    "5fdf9c8a6176752d35e4789c",
                    "5fdf9c8a6176752d35e478a6"
                ]
            },
            {
                "Moid": "5fdf9c876176752d35e47788",
                "ModuleId": 7,
                "OperState": "unknown",
                "Presence": "missing",
                "Dn": "sys/rack-unit-1/fan-module-1-7",
                "On": false,
                "Name": "Fan Module 7",
                "FanCount": 2,
                "FanMoids": [
                    "5fdf9c8a6176752d35e4789e",
                    "5fdf9c8a6176752d35e478b0"
                ]
            }
        ],
        "FanOn": 6,
        "FanCount": 7,
        "FanSummary": "6/7",
        "FanHealthy": false,
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "LocatorLedOn": false,
        "FanInfo": [
            {
                "Moid": "5fdf9d116176752d35e4b357",
                "ModuleId": 1,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-1",
                "On": true,
                "Name": "Fan Module 1",
                "FanCount": 2,
                "FanMoids": [
                    "5fdf9d136176752d35e4b41c",
                    "5fdf9d136176752d35e4b431"
                ]
            },
            {
                "Moid": "5fdf9d116176752d35e4b359",
                "ModuleId": 2,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-2",
                "On": true,
                "Name": "Fan Module 2",
                "FanCount": 2,
                "FanMoids": [
                    "5fdf9d136176752d35e4b418",
                    "5fdf9d136176752d35e4b41f"
                ]
            },
            {
                "Moid": "5fdf9d116176752d35e4b35b",
                "ModuleId": 3,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-3",
                "On": true,
                "Name": "Fan Module 3",
                "FanCount": 2,
                "FanMoids": [
                    "5fdf9d136176752d35e4b421",
                    "5fdf9d136176752d35e4b423"
                ]
            },
            {
                "Moid": "5fdf9d116176752d35e4b35d",
                "ModuleId": 4,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-4",
                "On": true,
                "Name": "Fan Module 4",
                "FanCount": 2,
                "FanMoids": [
                    "5fdf9d136176752d35e4b425",
                    "5fdf9d136176752d35e4b42b"
                ]
            },
            {
                "Moid": "5fdf9d116176752d35e4b35f",
                "ModuleId": 5,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-5",
                "On": true,
                "Name": "Fan Module 5",
                "FanCount": 2,
                "FanMoids": [
                    "5fdf9d136176752d35e4b41a",
                    "5fdf9d136176752d35e4b433"
                ]
            },
            {
                "Moid": "5fdf9d116176752d35e4b361",
                "ModuleId": 6,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-6",
                "On": true,
                "Name": "Fan Module 6",
                "FanCount": 2,
                "FanMoids": [
                    "5fdf9d136176752d35e4b427",
                    "5fdf9d136176752d35e4b42d"
                ]
            },
            {
                "Moid": "5fdf9d116176752d35e4b355",
                "ModuleId": 7,
                "OperState": "unknown",
                "Presence": "missing",
                "Dn": "sys/rack-unit-1/fan-module-1-7",
                "On": false,
                "Name": "Fan Module 7",
                "FanCount": 2,
                "FanMoids": [
                    "5fdf9d136176752d35e4b42f",
                    "5fdf9d136176752d35e4b435"
                ]
            }
        ],
        "FanOn": 6,
        "FanCount": 7,
        "FanSummary": "6/7",
        "FanHealthy": false,
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FanInfo": [
            {
                "Moid": "5fdfa18f6176752d35e67e6a",
                "ModuleId": 1,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-1",
                "On": false,
                "Name": "Fan Module 1",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfa1916176752d35e67f75",
                    "5fdfa1916176752d35e67f77"
                ]
            },
            {
                "Moid": "5fdfa18f6176752d35e67e70",
                "ModuleId": 2,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-2",
                "On": false,
                "Name": "Fan Module 2",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfa1916176752d35e67f67",
                    "5fdfa1916176752d35e67f6f"
                ]
            },
            {
                "Moid": "5fdfa18f6176752d35e67e72",
                "ModuleId": 3,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-3",
                "On": false,
                "Name": "Fan Module 3",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfa1916176752d35e67f69",
                    "5fdfa1916176752d35e67f79"
                ]
            },
            {
                "Moid": "5fdfa18f6176752d35e67e74",
                "ModuleId": 4,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-4",
                "On": false,
                "Name": "Fan Module 4",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfa1916176752d35e67f71",
                    "5fdfa1916176752d35e67f7b"
                ]
            },
            {
                "Moid": "5fdfa18f6176752d35e67e76",
                "ModuleId": 5,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-5",
                "On": false,
                "Name": "Fan Module 5",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfa1916176752d35e67f63",
                    "5fdfa1916176752d35e67f7d"
                ]
            },
            {
                "Moid": "5fdfa18f6176752d35e67e78",
                "ModuleId": 6,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-6",
                "On": false,
                "Name": "Fan Module 6",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfa1916176752d35e67f6b",
                    "5fdfa1916176752d35e67f73"
                ]
            },
            {
                "Moid": "5fdfa18f6176752d35e67e7a",
                "ModuleId": 7,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-7",
                "On": false,
                "Name": "Fan Module 7",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfa1916176752d35e67f65",
                    "5fdfa1916176752d35e67f6d"
                ]
            }
        ],
        "FanOn": 0,
        "FanCount": 7,
        "FanSummary": "0/7",
        "FanHealthy": false,
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FanInfo": [
            {
                "Moid": "5fdfdc476176752d35fce72a",
                "ModuleId": 1,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-1",
                "On": false,
                "Name": "Fan Module 1",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfdc4a6176752d35fce8b2",
                    "5fdfdc4a6176752d35fce8b6"
                ]
            },
            {
                "Moid": "5fdfdc476176752d35fce72c",
                "ModuleId": 2,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-2",
                "On": false,
                "Name": "Fan Module 2",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfdc4a6176752d35fce8a8",
                    "5fdfdc4a6176752d35fce8b4"
                ]
            },
            {
                "Moid": "5fdfdc476176752d35fce72e",
                "ModuleId": 3,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-3",
                "On": false,
                "Name": "Fan Module 3",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfdc4a6176752d35fce897",
                    "5fdfdc4a6176752d35fce8ac"
                ]
            },
            {
                "Moid": "5fdfdc476176752d35fce730",
                "ModuleId": 4,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-4",
                "On": false,
                "Name": "Fan Module 4",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfdc4a6176752d35fce899",
                    "5fdfdc4a6176752d35fce8b0"
                ]
            },
            {
                "Moid": "5fdfdc476176752d35fce724",
                "ModuleId": 5,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-5",
                "On": false,
                "Name": "Fan Module 5",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfdc4a6176752d35fce89c",
                    "5fdfdc4a6176752d35fce8aa"
                ]
            },
            {
                "Moid": "5fdfdc476176752d35fce726",
                "ModuleId": 6,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-6",
                "On": false,
                "Name": "Fan Module 6",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfdc4a6176752d35fce89e",
                    "5fdfdc4a6176752d35fce8ae"
                ]
            },
            {
                "Moid": "5fdfdc476176752d35fce728",
                "ModuleId": 7,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-7",
                "On": false,
                "Name": "Fan Module 7",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfdc4a6176752d35fce8a0",
                    "5fdfdc4a6176752d35fce8a6"
                ]
            }
        ],
        "FanOn": 0,
        "FanCount": 7,
        "FanSummary": "0/7",
        "FanHealthy": false,
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FanInfo": [
            {
                "Moid": "61dc837876752d3139cbb2ea",
                "ModuleId": 1,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-1",
                "On": false,
                "Name": "Fan Module 1",
                "FanCount": 2,
                "FanMoids": [
                    "61dc833c76752d3139cba825",
                    "61dc833c76752d3139cba82b"
                ]
            },
            {
                "Moid": "61dc837876752d3139cbb2ec",
                "ModuleId": 2,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-2",
                "On": false,
                "Name": "Fan Module 2",
                "FanCount": 2,
                "FanMoids": [
                    "61dc833c76752d3139cba82d",
                    "61dc833c76752d3139cba82f"
                ]
            },
            {
                "Moid": "61dc837876752d3139cbb2ee",
                "ModuleId": 3,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-3",
                "On": false,
                "Name": "Fan Module 3",
                "FanCount": 2,
                "FanMoids": [
                    "61dc833c76752d3139cba831",
                    "61dc833c76752d3139cba833"
                ]
            },
            {
                "Moid": "61dc837776752d3139cbb2de",
                "ModuleId": 4,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-4",
                "On": false,
                "Name": "Fan Module 4",
                "FanCount": 2,
                "FanMoids": [
                    "61dc833c76752d3139cba83b",
                    "61dc833c76752d3139cba83d"
                ]
            },
            {
                "Moid": "61dc837776752d3139cbb2e0",
                "ModuleId": 5,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-5",
                "On": false,
                "Name": "Fan Module 5",
                "FanCount": 2,
                "FanMoids": [
                    "61dc833c76752d3139cba835",
                    "61dc833c76752d3139cba837"
                ]
            },
            {
                "Moid": "61dc837776752d3139cbb2e2",
                "ModuleId": 6,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-6",
                "On": false,
                "Name": "Fan Module 6",
                "FanCount": 2,
                "FanMoids": [
                    "61dc833c76752d3139cba827",
                    "61dc833c76752d3139cba83f"
                ]
            },
            {
                "Moid": "61dc837876752d3139cbb2e4",
                "ModuleId": 7,
                "OperState": "unknown",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-7",
                "On": false,
                "Name": "Fan Module 7",
                "FanCount": 2,
                "FanMoids": [
                    "61dc833c76752d3139cba829",
                    "61dc833c76752d3139cba839"
                ]
            }
        ],
        "FanOn": 0,
        "FanCount": 7,
        "FanSummary": "0/7",
        "FanHealthy": false,
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FanInfo": [
            {
                "Moid": "5fdfe80e6176752d3502b139",
                "ModuleId": 1,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-1",
                "On": true,
                "Name": "Fan Module 1",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfe80f6176752d3502b17d",
                    "5fdfe80f6176752d3502b17f"
                ]
            },
            {
                "Moid": "5fdfe80e6176752d3502b13b",
                "ModuleId": 2,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-2",
                "On": true,
                "Name": "Fan Module 2",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfe80f6176752d3502b16b",
                    "5fdfe80f6176752d3502b187"
                ]
            },
            {
                "Moid": "5fdfe80e6176752d3502b13d",
                "ModuleId": 3,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-3",
                "On": true,
                "Name": "Fan Module 3",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfe80f6176752d3502b16e",
                    "5fdfe80f6176752d3502b181"
                ]
            },
            {
                "Moid": "5fdfe80e6176752d3502b13f",
                "ModuleId": 4,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-4",
                "On": true,
                "Name": "Fan Module 4",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfe80f6176752d3502b170",
                    "5fdfe80f6176752d3502b183"
                ]
            },
            {
                "Moid": "5fdfe80e6176752d3502b141",
                "ModuleId": 5,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-5",
                "On": true,
                "Name": "Fan Module 5",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfe80f6176752d3502b174",
                    "5fdfe80f6176752d3502b176"
                ]
            },
            {
                "Moid": "5fdfe80e6176752d3502b143",
                "ModuleId": 6,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-6",
                "On": true,
                "Name": "Fan Module 6",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfe80f6176752d3502b17b",
                    "5fdfe80f6176752d3502b185"
                ]
            },
            {
                "Moid": "5fdfe80e6176752d3502b145",
                "ModuleId": 7,
                "OperState": "operable",
                "Presence": "equipped",
                "Dn": "sys/rack-unit-1/fan-module-1-7",
                "On": true,
                "Name": "Fan Module 7",
                "FanCount": 2,
                "FanMoids": [
                    "5fdfe80f6176752d3502b189",
                    "5fdfe80f6176752d3502b18b"
                ]
            }
        ],
        "FanOn": 7,
        "FanCount": 7,
        "FanSummary": "7/7",
        "FanHealthy": true,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    }
]
```

Developer output

```
# iserver get servers --column fan --group p2b

Developer output

{
    "duration": 3939,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 5233
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

2022-12-13 16:58:11.474919	True	2113	93	isctl get compute rackunit   -o json --top 100
2022-12-13 16:58:12.272387	True	796	10	isctl get compute blade   -o json --top 100
2022-12-13 16:58:12.740154	True	415	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T16:58:12.000Z"  -o json --top 100
2022-12-13 16:58:12.884542	True	553	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 16:58:12.970239	True	632	49	isctl get equipment fanmodule --filter "Parent/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '5fdfa1806176752d35e678c2', '5fdfdc3b6176752d35fce0a9', '5fdfe47f6176752d35001995', '5fdfe80d6176752d3502b008')"  -o json --top 100
2022-12-13 16:58:13.037031	True	724	7	isctl get asset deviceregistration --filter "Moid in ('5fdf9be76f72612d300a8d81', '5fdf9c676f72612d300a9c8d', '5fdf9cf26f72612d300aaca0', '5fdfa1686f72612d300b383f', '5fdfdc206f72612d30120ab4', '5fdfe4666f72612d30130510', '5fdfe7d86f72612d30136fed')"  -o json --top 100
```
