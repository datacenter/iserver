# Extra server information - PSU State

```
# iserver get servers --column psu --group p2b

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+-----+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    | Psu |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+-----+
| P+ H | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 2/2 | 
| P+ H | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 2S 40C 80T | 384 [GiB] | 2/2 | 
| P+ H | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | 2S 40C 80T | 384 [GiB] | 2/2 | 
| P- H | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 2S 40C 80T | 384 [GiB] | 2/2 | 
| P- H | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | 2S 40C 80T | 384 [GiB] | 2/2 | 
| P- H | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | 2S 40C 80T | 384 [GiB] | 2/2 | 
| P+ H | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 | 2S 40C 80T | 384 [GiB] | 2/2 | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+-----+
```

JSON output

```
# iserver get servers --column psu --group p2b

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
        "PsuInfo": [
            {
                "Moid": "5fdf9c0d6176752d35e44cf7",
                "Name": "",
                "Model": "PS-2112-9S-LF",
                "Serial": "LIT241244MU",
                "Vendor": "Cisco Systems Inc",
                "Dn": "sys/rack-unit-1/psu-1",
                "On": true,
                "Voltage": "ok"
            },
            {
                "Moid": "5fdf9c0d6176752d35e44cf9",
                "Name": "",
                "Model": "PS-2112-9S-LF",
                "Serial": "LIT241244Z5",
                "Vendor": "Cisco Systems Inc",
                "Dn": "sys/rack-unit-1/psu-2",
                "On": true,
                "Voltage": "ok"
            }
        ],
        "PsuOn": 2,
        "PsuCount": 2,
        "PsuSummary": "2/2",
        "PsuHealthy": true,
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
        "PsuInfo": [
            {
                "Moid": "5fdf9c856176752d35e476b8",
                "Name": "",
                "Model": "PS-2112-9S-LF",
                "Serial": "LIT241244RQ",
                "Vendor": "Cisco Systems Inc",
                "Dn": "sys/rack-unit-1/psu-1",
                "On": true,
                "Voltage": "ok"
            },
            {
                "Moid": "5fdf9c856176752d35e476ba",
                "Name": "",
                "Model": "PS-2112-9S-LF",
                "Serial": "LIT241242TS",
                "Vendor": "Cisco Systems Inc",
                "Dn": "sys/rack-unit-1/psu-2",
                "On": true,
                "Voltage": "ok"
            }
        ],
        "PsuOn": 2,
        "PsuCount": 2,
        "PsuSummary": "2/2",
        "PsuHealthy": true,
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
        "PsuInfo": [
            {
                "Moid": "5fdf9d0f6176752d35e4b2a3",
                "Name": "",
                "Model": "PS-2112-9S-LF",
                "Serial": "LIT241244NV",
                "Vendor": "Cisco Systems Inc",
                "Dn": "sys/rack-unit-1/psu-1",
                "On": true,
                "Voltage": "ok"
            },
            {
                "Moid": "5fdf9d0f6176752d35e4b2a5",
                "Name": "",
                "Model": "PS-2112-9S-LF",
                "Serial": "LIT241244UN",
                "Vendor": "Cisco Systems Inc",
                "Dn": "sys/rack-unit-1/psu-2",
                "On": true,
                "Voltage": "ok"
            }
        ],
        "PsuOn": 2,
        "PsuCount": 2,
        "PsuSummary": "2/2",
        "PsuHealthy": true,
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
        "PsuInfo": [
            {
                "Moid": "62a7eebf76752d313928bfbc",
                "Name": "",
                "Model": "700-014550-0000",
                "Serial": "APS240201EL",
                "Vendor": "Cisco Systems Inc",
                "Dn": "sys/rack-unit-1/psu-1",
                "On": true,
                "Voltage": "ok"
            },
            {
                "Moid": "62a7eebf76752d313928bfbe",
                "Name": "",
                "Model": "700-014550-0000",
                "Serial": "ART2601F4S6",
                "Vendor": "Cisco Systems Inc",
                "Dn": "sys/rack-unit-1/psu-2",
                "On": true,
                "Voltage": "ok"
            }
        ],
        "PsuOn": 2,
        "PsuCount": 2,
        "PsuSummary": "2/2",
        "PsuHealthy": true,
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
        "PsuInfo": [
            {
                "Moid": "5fdfdc456176752d35fce61b",
                "Name": "",
                "Model": "700-014550-0000",
                "Serial": "APS240201ES",
                "Vendor": "Cisco Systems Inc",
                "Dn": "sys/rack-unit-1/psu-1",
                "On": true,
                "Voltage": "ok"
            },
            {
                "Moid": "5fdfdc456176752d35fce620",
                "Name": "",
                "Model": "700-014550-0000",
                "Serial": "ART2601F4S2",
                "Vendor": "Cisco Systems Inc",
                "Dn": "sys/rack-unit-1/psu-2",
                "On": true,
                "Voltage": "ok"
            }
        ],
        "PsuOn": 2,
        "PsuCount": 2,
        "PsuSummary": "2/2",
        "PsuHealthy": true,
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
        "PsuInfo": [
            {
                "Moid": "61dc832c76752d3139cba4f4",
                "Name": "",
                "Model": "700-014550-0000",
                "Serial": "APS240201EX",
                "Vendor": "Cisco Systems Inc",
                "Dn": "sys/rack-unit-1/psu-1",
                "On": true,
                "Voltage": "ok"
            },
            {
                "Moid": "61dc832c76752d3139cba4fa",
                "Name": "",
                "Model": "700-014550-0000",
                "Serial": "ART2601F4SS",
                "Vendor": "Cisco Systems Inc",
                "Dn": "sys/rack-unit-1/psu-2",
                "On": true,
                "Voltage": "ok"
            }
        ],
        "PsuOn": 2,
        "PsuCount": 2,
        "PsuSummary": "2/2",
        "PsuHealthy": true,
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
        "PsuInfo": [
            {
                "Moid": "5fdfe80e6176752d3502b0f2",
                "Name": "",
                "Model": "700-014550-0000",
                "Serial": "APS240201ER",
                "Vendor": "Cisco Systems Inc",
                "Dn": "sys/rack-unit-1/psu-1",
                "On": true,
                "Voltage": "ok"
            },
            {
                "Moid": "5fdfe80e6176752d3502b0f5",
                "Name": "",
                "Model": "700-014550-0000",
                "Serial": "ART2601F4LL",
                "Vendor": "Cisco Systems Inc",
                "Dn": "sys/rack-unit-1/psu-2",
                "On": true,
                "Voltage": "ok"
            }
        ],
        "PsuOn": 2,
        "PsuCount": 2,
        "PsuSummary": "2/2",
        "PsuHealthy": true,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    }
]
```

Developer output

```
# iserver get servers --column psu --group p2b

Developer output

{
    "duration": 3585,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 4718
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

2022-12-13 16:58:16.064434	True	1804	93	isctl get compute rackunit   -o json --top 100
2022-12-13 16:58:16.731456	True	666	10	isctl get compute blade   -o json --top 100
2022-12-13 16:58:17.154682	True	374	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 16:58:17.232184	True	456	7	isctl get asset deviceregistration --filter "Moid in ('5fdf9be76f72612d300a8d81', '5fdf9c676f72612d300a9c8d', '5fdf9cf26f72612d300aaca0', '5fdfa1686f72612d300b383f', '5fdfdc206f72612d30120ab4', '5fdfe4666f72612d30130510', '5fdfe7d86f72612d30136fed')"  -o json --top 100
2022-12-13 16:58:17.438520	True	657	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T16:58:16.000Z"  -o json --top 100
2022-12-13 16:58:17.609808	True	761	14	isctl get equipment psu --filter "Parent/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '5fdfa1806176752d35e678c2', '5fdfdc3b6176752d35fce0a9', '5fdfe47f6176752d35001995', '5fdfe80d6176752d3502b008')"  -o json --top 100
```
