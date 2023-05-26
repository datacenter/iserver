# Get Intersight Servers with Thermal Information

```
# iserver get servers --group power -c thermal

+---------+-----+----+--------------------------------+--------------------+-------------+-------------+------+---------+-------------+-------------+----------------+
| SF      | MF  | WF | Name                           | Model              | Serial      | IP          | Fans | Sensors | Highest (C) | Min Gap (C) | Over Threshold |
+---------+-----+----+--------------------------------+--------------------+-------------+-------------+------+---------+-------------+-------------+----------------+
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-1           | (B) UCSB-B200-M4   | FCH205371PZ | 10.58.52.33 | N/A  | True    | 37.5        | N/A         | N/A            | 
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-2           | (B) UCSB-B200-M4   | FCH20527XXD | 10.58.52.34 | N/A  | True    | 38.5        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-1-3           | (B) UCSB-B200-M4   | FCH20437VXH | 10.58.52.35 | N/A  | True    | 41.0        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-1-4           | (B) UCSB-B200-M4   | FCH205371UU | 10.58.52.36 | N/A  | True    | 42.0        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-1           | (B) UCSB-B200-M5   | FLM241501FB | 10.58.52.41 | N/A  | True    | 46.5        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-2           | (B) UCSB-B200-M5   | FLM24140BJB | 10.58.52.42 | N/A  | True    | 40.5        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-3           | (B) UCSB-B200-M5   | FLM241501CT | 10.58.52.43 | N/A  | True    | 37.5        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-4           | (B) UCSB-B200-M5   | FLM24140B0B | 10.58.52.44 | N/A  | True    | 48.5        | N/A         | N/A            | 
| P+ H    | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 |      |         |             |             |                | 
| P+ H    | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 |      |         |             |             |                | 
| P+ H    | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 |      |         |             |             |                | 
| P- H    | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 |      |         |             |             |                | 
| P- H    | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 |      |         |             |             |                | 
| P- H    | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 |      |         |             |             |                | 
| P+ H    | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 |      |         |             |             |                | 
+---------+-----+----+--------------------------------+--------------------+-------------+-------------+------+---------+-------------+-------------+----------------+
```

JSON Output

```
# iserver get servers --group power -c thermal

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
        "Thermal": null,
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
        "Thermal": null,
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
        "Thermal": null,
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
        "Thermal": null,
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
        "Thermal": null,
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
        "Thermal": null,
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
        "Thermal": null,
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6335c26e76752d3139b9694c",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-2-1",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM241501FB",
        "ManagementMode": "UCSM",
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
        "ManagementIp": "10.58.52.41",
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
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-2/blade-1/board/temp-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 20.0,
                    "fm_temp_sen_rear": 36.0,
                    "temperature_avg": 20.33,
                    "fm_temp_sen_rear_avg": 36.0,
                    "temperature_min": 20.0,
                    "fm_temp_sen_rear_min": 36.0,
                    "temperature_max": 21.0,
                    "fm_temp_sen_rear_max": 36.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/temp-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 36.0,
                    "temperature_avg": 36.0,
                    "temperature_min": 36.0,
                    "temperature_max": 36.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/cpu-1/env-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 41.5,
                    "temperature_avg": 41.25,
                    "temperature_min": 41.0,
                    "temperature_max": 41.5
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/cpu-2/env-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 46.5,
                    "temperature_avg": 45.75,
                    "temperature_min": 45.0,
                    "temperature_max": 46.5
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-11/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-11",
                    "name": "MEM-11",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.2,
                    "temperature_min": 29.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.27,
                    "temperature_min": 31.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-15/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-15",
                    "name": "MEM-15",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-17/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-17",
                    "name": "MEM-17",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.07,
                    "temperature_min": 31.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-21/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-21",
                    "name": "MEM-21",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-23/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-23",
                    "name": "MEM-23",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-3/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-3",
                    "name": "MEM-3",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.4,
                    "temperature_min": 27.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-5/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-5",
                    "name": "MEM-5",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-7/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-7",
                    "name": "MEM-7",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-9/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:43.799",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-9",
                    "name": "MEM-9",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                }
            ],
            "Summary": {
                "Source": "UCSM",
                "FanHealth": "N/A",
                "SensorHealth": true,
                "HighestTemperature": 46.5,
                "SmallestGap": "N/A",
                "OverThreshold": "N/A"
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6335c45976752d3139b9bf94",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-2-2",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM24140BJB",
        "ManagementMode": "UCSM",
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
        "ManagementIp": "10.58.52.42",
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
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-2/blade-2/board/temp-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 21.0,
                    "fm_temp_sen_rear": 35.0,
                    "temperature_avg": 21.0,
                    "fm_temp_sen_rear_avg": 35.0,
                    "temperature_min": 21.0,
                    "fm_temp_sen_rear_min": 35.0,
                    "temperature_max": 21.0,
                    "fm_temp_sen_rear_max": 35.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/temp-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 35.0,
                    "temperature_avg": 35.0,
                    "temperature_min": 35.0,
                    "temperature_max": 35.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/cpu-1/env-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 38.5,
                    "temperature_avg": 38.5,
                    "temperature_min": 38.5,
                    "temperature_max": 38.5
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/cpu-2/env-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 40.5,
                    "temperature_avg": 40.5,
                    "temperature_min": 40.5,
                    "temperature_max": 40.5
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-11/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-11",
                    "name": "MEM-11",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 28.78,
                    "temperature_min": 28.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 32.0,
                    "temperature_avg": 31.78,
                    "temperature_min": 31.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-15/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-15",
                    "name": "MEM-15",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-17/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-17",
                    "name": "MEM-17",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 33.0,
                    "temperature_avg": 33.0,
                    "temperature_min": 33.0,
                    "temperature_max": 33.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-21/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-21",
                    "name": "MEM-21",
                    "type": "memory",
                    "temperature": 32.0,
                    "temperature_avg": 31.33,
                    "temperature_min": 31.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-23/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-23",
                    "name": "MEM-23",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 30.22,
                    "temperature_min": 30.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-3/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-3",
                    "name": "MEM-3",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-5/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-5",
                    "name": "MEM-5",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.0,
                    "temperature_min": 31.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-7/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-7",
                    "name": "MEM-7",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-9/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:59.355",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-9",
                    "name": "MEM-9",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                }
            ],
            "Summary": {
                "Source": "UCSM",
                "FanHealth": "N/A",
                "SensorHealth": true,
                "HighestTemperature": 40.5,
                "SmallestGap": "N/A",
                "OverThreshold": "N/A"
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.RRRR"
        },
        "Moid": "6335e1f376752d3139bf12b8",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-1-1",
        "Model": "UCSB-B200-M4",
        "Serial": "FCH205371PZ",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
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
        "ManagementIp": "10.58.52.33",
        "AlarmSummary": {
            "Critical": 9,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Critical (9)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-1/board/temp-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 23.0,
                    "fm_temp_sen_rear": 36.0,
                    "temperature_avg": 23.0,
                    "fm_temp_sen_rear_avg": 36.0,
                    "temperature_min": 23.0,
                    "fm_temp_sen_rear_min": 36.0,
                    "temperature_max": 23.0,
                    "fm_temp_sen_rear_max": 36.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/temp-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 36.0,
                    "temperature_avg": 36.0,
                    "temperature_min": 36.0,
                    "temperature_max": 36.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/cpu-1/env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 34.5,
                    "temperature_avg": 34.4,
                    "temperature_min": 34.0,
                    "temperature_max": 34.5
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/cpu-2/env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 37.5,
                    "temperature_avg": 37.67,
                    "temperature_min": 37.0,
                    "temperature_max": 38.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-10/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-10",
                    "name": "MEM-10",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-11/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-11",
                    "name": "MEM-11",
                    "type": "memory",
                    "temperature": 25.0,
                    "temperature_avg": 25.0,
                    "temperature_min": 25.0,
                    "temperature_max": 25.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.54,
                    "temperature_min": 29.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-14/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-14",
                    "name": "MEM-14",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.23,
                    "temperature_min": 28.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-16/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-16",
                    "name": "MEM-16",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.46,
                    "temperature_min": 31.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-17/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-17",
                    "name": "MEM-17",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-2/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-2",
                    "name": "MEM-2",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 26.92,
                    "temperature_min": 26.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-20/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-20",
                    "name": "MEM-20",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-22",
                    "name": "MEM-22",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-23/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-23",
                    "name": "MEM-23",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.0,
                    "temperature_min": 31.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-4/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-4",
                    "name": "MEM-4",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-5/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-5",
                    "name": "MEM-5",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-7/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-7",
                    "name": "MEM-7",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-8/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:56.154",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-8",
                    "name": "MEM-8",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                }
            ],
            "Summary": {
                "Source": "UCSM",
                "FanHealth": "N/A",
                "SensorHealth": true,
                "HighestTemperature": 37.5,
                "SmallestGap": "N/A",
                "OverThreshold": "N/A"
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M4",
        "LocatorLedOn": false,
        "FlagState": "P+ C(9)",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.RRRR"
        },
        "Moid": "6337014c76752d3139f2f459",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-1-2",
        "Model": "UCSB-B200-M4",
        "Serial": "FCH20527XXD",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
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
        "ManagementIp": "10.58.52.34",
        "AlarmSummary": {
            "Critical": 9,
            "Warning": 0,
            "Info": 1
        },
        "Health": "Critical (9)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-2/board/temp-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 24.0,
                    "fm_temp_sen_rear": 37.0,
                    "temperature_avg": 24.0,
                    "fm_temp_sen_rear_avg": 37.0,
                    "temperature_min": 24.0,
                    "fm_temp_sen_rear_min": 37.0,
                    "temperature_max": 24.0,
                    "fm_temp_sen_rear_max": 37.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/temp-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 37.0,
                    "temperature_avg": 37.0,
                    "temperature_min": 37.0,
                    "temperature_max": 37.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/cpu-1/env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 36.0,
                    "temperature_avg": 35.83,
                    "temperature_min": 35.5,
                    "temperature_max": 36.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/cpu-2/env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 38.5,
                    "temperature_avg": 38.33,
                    "temperature_min": 38.0,
                    "temperature_max": 38.5
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-10/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-10",
                    "name": "MEM-10",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-11/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-11",
                    "name": "MEM-11",
                    "type": "memory",
                    "temperature": 26.0,
                    "temperature_avg": 26.0,
                    "temperature_min": 26.0,
                    "temperature_max": 26.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 33.0,
                    "temperature_avg": 33.0,
                    "temperature_min": 33.0,
                    "temperature_max": 33.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-14/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-14",
                    "name": "MEM-14",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.0,
                    "temperature_min": 31.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-16/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-16",
                    "name": "MEM-16",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-17/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-17",
                    "name": "MEM-17",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 33.0,
                    "temperature_avg": 33.0,
                    "temperature_min": 33.0,
                    "temperature_max": 33.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-2/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-2",
                    "name": "MEM-2",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-20/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-20",
                    "name": "MEM-20",
                    "type": "memory",
                    "temperature": 33.0,
                    "temperature_avg": 33.0,
                    "temperature_min": 33.0,
                    "temperature_max": 33.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-22",
                    "name": "MEM-22",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-23/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-23",
                    "name": "MEM-23",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-4/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-4",
                    "name": "MEM-4",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-5/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-5",
                    "name": "MEM-5",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-7/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-7",
                    "name": "MEM-7",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-8/dimm-env-stats",
                    "time_collected": "2022-12-13T18:01:57.019",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-8",
                    "name": "MEM-8",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                }
            ],
            "Summary": {
                "Source": "UCSM",
                "FanHealth": "N/A",
                "SensorHealth": true,
                "HighestTemperature": 38.5,
                "SmallestGap": "N/A",
                "OverThreshold": "N/A"
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M4",
        "LocatorLedOn": false,
        "FlagState": "P+ C(9)",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6337063276752d3139f3cc83",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-1-3",
        "Model": "UCSB-B200-M4",
        "Serial": "FCH20437VXH",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
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
        "ManagementIp": "10.58.52.35",
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
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-3/board/temp-stats",
                    "time_collected": "2022-12-13T18:02:21.966",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 26.0,
                    "fm_temp_sen_rear": 36.0,
                    "temperature_avg": 25.09,
                    "fm_temp_sen_rear_avg": 36.09,
                    "temperature_min": 25.0,
                    "fm_temp_sen_rear_min": 36.0,
                    "temperature_max": 26.0,
                    "fm_temp_sen_rear_max": 37.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/temp-stats",
                    "time_collected": "2022-12-13T18:02:21.966",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 36.0,
                    "temperature_avg": 36.09,
                    "temperature_min": 36.0,
                    "temperature_max": 37.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/cpu-1/env-stats",
                    "time_collected": "2022-12-13T18:02:21.966",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 38.0,
                    "temperature_avg": 37.59,
                    "temperature_min": 36.5,
                    "temperature_max": 38.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/cpu-2/env-stats",
                    "time_collected": "2022-12-13T18:02:21.966",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 41.0,
                    "temperature_avg": 41.0,
                    "temperature_min": 40.5,
                    "temperature_max": 41.5
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:21.966",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.09,
                    "temperature_min": 28.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-10/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:21.966",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-10",
                    "name": "MEM-10",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:21.966",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 30.27,
                    "temperature_min": 27.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-16/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:21.966",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-16",
                    "name": "MEM-16",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 26.64,
                    "temperature_min": 26.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:21.966",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 26.0,
                    "temperature_avg": 28.73,
                    "temperature_min": 26.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:21.966",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-22",
                    "name": "MEM-22",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 26.36,
                    "temperature_min": 25.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-4/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:21.966",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-4",
                    "name": "MEM-4",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-7/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:21.966",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-7",
                    "name": "MEM-7",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                }
            ],
            "Summary": {
                "Source": "UCSM",
                "FanHealth": "N/A",
                "SensorHealth": true,
                "HighestTemperature": 41.0,
                "SmallestGap": "N/A",
                "OverThreshold": "N/A"
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M4",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "63371c9176752d3139f7da74",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-1-4",
        "Model": "UCSB-B200-M4",
        "Serial": "FCH205371UU",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
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
        "ManagementIp": "10.58.52.36",
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
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-4/board/temp-stats",
                    "time_collected": "2022-12-13T18:02:01.350",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 26.0,
                    "fm_temp_sen_rear": 36.0,
                    "temperature_avg": 25.14,
                    "fm_temp_sen_rear_avg": 36.0,
                    "temperature_min": 25.0,
                    "fm_temp_sen_rear_min": 36.0,
                    "temperature_max": 26.0,
                    "fm_temp_sen_rear_max": 36.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/temp-stats",
                    "time_collected": "2022-12-13T18:02:01.350",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 36.0,
                    "temperature_avg": 36.0,
                    "temperature_min": 36.0,
                    "temperature_max": 36.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/cpu-1/env-stats",
                    "time_collected": "2022-12-13T18:02:01.349",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 39.5,
                    "temperature_avg": 39.25,
                    "temperature_min": 39.0,
                    "temperature_max": 39.5
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/cpu-2/env-stats",
                    "time_collected": "2022-12-13T18:02:01.349",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 42.0,
                    "temperature_avg": 41.75,
                    "temperature_min": 41.5,
                    "temperature_max": 42.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:01.350",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-10/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:01.350",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-10",
                    "name": "MEM-10",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:01.350",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-16/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:01.350",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-16",
                    "name": "MEM-16",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.0,
                    "temperature_min": 31.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:01.350",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:01.350",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-22",
                    "name": "MEM-22",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-4/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:01.350",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-4",
                    "name": "MEM-4",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-7/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:01.350",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-7",
                    "name": "MEM-7",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.0,
                    "temperature_min": 31.0,
                    "temperature_max": 31.0
                }
            ],
            "Summary": {
                "Source": "UCSM",
                "FanHealth": "N/A",
                "SensorHealth": true,
                "HighestTemperature": 42.0,
                "SmallestGap": "N/A",
                "OverThreshold": "N/A"
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M4",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "63371c9176752d3139f7da78",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-2-4",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM24140B0B",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
        "AvailableMemory": 196608,
        "TotalMemory": 196608,
        "UsedMemory": 0,
        "TotalMemoryUnit": "192 [GiB]",
        "TotalMemoryGB": 192,
        "AvailableMemoryUnit": "192 [GiB]",
        "AvailableMemoryGB": 192,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.52.44",
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
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-2/blade-4/board/temp-stats",
                    "time_collected": "2022-12-13T18:02:51.812",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 22.0,
                    "fm_temp_sen_rear": 38.0,
                    "temperature_avg": 21.6,
                    "fm_temp_sen_rear_avg": 38.0,
                    "temperature_min": 21.0,
                    "fm_temp_sen_rear_min": 38.0,
                    "temperature_max": 22.0,
                    "fm_temp_sen_rear_max": 38.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/temp-stats",
                    "time_collected": "2022-12-13T18:02:51.812",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 38.0,
                    "temperature_avg": 38.0,
                    "temperature_min": 38.0,
                    "temperature_max": 38.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/cpu-2/env-stats",
                    "time_collected": "2022-12-13T18:02:51.812",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 48.5,
                    "temperature_avg": 48.4,
                    "temperature_min": 48.0,
                    "temperature_max": 49.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/cpu-1/env-stats",
                    "time_collected": "2022-12-13T18:02:51.812",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 41.0,
                    "temperature_avg": 40.7,
                    "temperature_min": 40.5,
                    "temperature_max": 41.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:51.812",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:51.812",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 32.0,
                    "temperature_avg": 32.0,
                    "temperature_min": 32.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-15/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:51.812",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-15",
                    "name": "MEM-15",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-17/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:51.812",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-17",
                    "name": "MEM-17",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-3/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:51.812",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-3",
                    "name": "MEM-3",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-5/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:51.812",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-5",
                    "name": "MEM-5",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                }
            ],
            "Summary": {
                "Source": "UCSM",
                "FanHealth": "N/A",
                "SensorHealth": true,
                "HighestTemperature": 48.5,
                "SmallestGap": "N/A",
                "OverThreshold": "N/A"
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "63371c9176752d3139f7da82",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-2-3",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM241501CT",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
        "AvailableMemory": 196608,
        "TotalMemory": 196608,
        "UsedMemory": 0,
        "TotalMemoryUnit": "192 [GiB]",
        "TotalMemoryGB": 192,
        "AvailableMemoryUnit": "192 [GiB]",
        "AvailableMemoryGB": 192,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.52.43",
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
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-2/blade-3/board/temp-stats",
                    "time_collected": "2022-12-13T18:02:54.846",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 20.0,
                    "fm_temp_sen_rear": 32.0,
                    "temperature_avg": 20.0,
                    "fm_temp_sen_rear_avg": 32.0,
                    "temperature_min": 20.0,
                    "fm_temp_sen_rear_min": 32.0,
                    "temperature_max": 20.0,
                    "fm_temp_sen_rear_max": 32.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/temp-stats",
                    "time_collected": "2022-12-13T18:02:54.846",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 32.0,
                    "temperature_avg": 32.0,
                    "temperature_min": 32.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/cpu-2/env-stats",
                    "time_collected": "2022-12-13T18:02:54.846",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 36.5,
                    "temperature_avg": 36.5,
                    "temperature_min": 36.5,
                    "temperature_max": 36.5
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/cpu-1/env-stats",
                    "time_collected": "2022-12-13T18:02:54.846",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 37.5,
                    "temperature_avg": 37.67,
                    "temperature_min": 37.5,
                    "temperature_max": 38.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:54.846",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:54.846",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-15/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:54.846",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-15",
                    "name": "MEM-15",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-17/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:54.846",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-17",
                    "name": "MEM-17",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-3/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:54.846",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-3",
                    "name": "MEM-3",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-5/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:54.846",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-5",
                    "name": "MEM-5",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                }
            ],
            "Summary": {
                "Source": "UCSM",
                "FanHealth": "N/A",
                "SensorHealth": true,
                "HighestTemperature": 37.5,
                "SmallestGap": "N/A",
                "OverThreshold": "N/A"
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    }
]
```

Developer Output

```
# iserver get servers --group power -c thermal

Developer output

{
    "duration": 9661,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 4156
    },
    "redfish": {
        "read": true,
        "success": 0,
        "failed": 8,
        "connect": 8,
        "disconnect": 0,
        "path": 0,
        "connect_time": 5311,
        "disconnect_time": 0,
        "path_time": 0,
        "total_time": 5311
    },
    "ucsm": {
        "read": true,
        "success": 56,
        "failed": 0,
        "connect": 16,
        "disconnect": 0,
        "mo": 40,
        "connect_time": 9008,
        "disconnect_time": 0,
        "mo_time": 7758,
        "total_time": 16766
    },
    "ssh": {
        "read": false,
        "calls": 0,
        "total_time": 0
    },
    "error": {
        "read": true,
        "lines": 9
    },
    "info": {
        "read": true,
        "lines": 9
    },
    "debug": {
        "read": true,
        "lines": 72
    }
}

Log: info
----------

[2022-12-13 17:02:45.879301]	[connect]	Redfish authentication failed: 10.58.50.42 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:45.891151]	[connect]	Redfish authentication failed: 10.58.50.43 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:45.895896]	[disconnect]	Redfish session close failed: 10.58.50.42 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:45.900213]	[disconnect]	Redfish session close failed: 10.58.50.43 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:45.903479]	[connect]	Redfish authentication failed: 10.58.50.41 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:45.921388]	[disconnect]	Redfish session close failed: 10.58.50.41 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:45.967114]	[connect]	Redfish authentication failed: 10.58.50.47 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:45.979434]	[disconnect]	Redfish session close failed: 10.58.50.47 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'


Log: error
-----------

[2022-12-13 17:02:45.879001]	[connect]	Redfish authentication failed: 10.58.50.42 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:45.890915]	[connect]	Redfish authentication failed: 10.58.50.43 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:45.895703]	[disconnect]	Redfish session close failed: 10.58.50.42 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:45.900029]	[disconnect]	Redfish session close failed: 10.58.50.43 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:45.903101]	[connect]	Redfish authentication failed: 10.58.50.41 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:45.921187]	[disconnect]	Redfish session close failed: 10.58.50.41 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:45.966862]	[connect]	Redfish authentication failed: 10.58.50.47 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:45.979257]	[disconnect]	Redfish session close failed: 10.58.50.47 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'


Log: isctl
-----------

2022-12-13 17:02:43.321226	True	2180	93	isctl get compute rackunit   -o json --top 100
2022-12-13 17:02:43.958941	True	636	10	isctl get compute blade   -o json --top 100
2022-12-13 17:02:44.427550	True	419	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 17:02:44.428127	True	401	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T17:02:44.000Z"  -o json --top 100
2022-12-13 17:02:44.521776	True	520	8	isctl get asset deviceregistration --filter "Moid in ('5fdf9be76f72612d300a8d81', '5fdf9c676f72612d300a9c8d', '5fdf9cf26f72612d300aaca0', '5fdfa1686f72612d300b383f', '5fdfdc206f72612d30120ab4', '5fdfe4666f72612d30130510', '5fdfe7d86f72612d30136fed', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1')"  -o json --top 100


Log: redfish
-------------

2022-12-13 17:02:45.879635	False	1305	connect 10.58.50.42
2022-12-13 17:02:45.891435	False	1313	connect 10.58.50.43
2022-12-13 17:02:45.896185	False	8	disconnect 10.58.50.42
2022-12-13 17:02:45.900519	False	5	disconnect 10.58.50.43
2022-12-13 17:02:45.904077	False	1327	connect 10.58.50.41
2022-12-13 17:02:45.921677	False	5	disconnect 10.58.50.41
2022-12-13 17:02:45.967415	False	1342	connect 10.58.50.47
2022-12-13 17:02:45.979720	False	6	disconnect 10.58.50.47


Log: ucsm
----------

2022-12-13 17:02:46.632795	True	720	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:46.843013	True	209	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:46.959041	True	1052	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:47.086767	True	243	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:47.170626	True	211	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:47.256514	True	169	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:02:47.285609	True	1352	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:47.407361	True	237	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:47.431986	True	175	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:02:47.489925	True	204	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:47.581393	True	174	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:02:47.585440	True	1593	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:47.658094	True	226	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:02:47.677776	True	187	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:47.750377	True	169	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:02:47.789907	True	204	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:47.820081	True	155	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:47.875705	True	198	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:02:47.986780	True	196	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:48.007417	True	257	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:02:48.049334	True	174	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:02:48.153468	True	137	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:48.212791	True	225	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:02:48.277086	True	228	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:02:48.389161	True	176	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:02:48.460454	True	175	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:48.623887	True	234	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:02:48.667975	True	831	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:48.790219	True	158	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:48.837550	True	169	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:48.884794	True	715	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:49.017918	True	180	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:49.059546	True	175	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:49.180339	True	162	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:02:49.205241	True	721	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:49.233100	True	174	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:49.348654	True	168	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:02:49.369119	True	164	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:49.397683	True	164	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:02:49.544402	True	735	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:49.556064	True	186	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:49.563886	True	215	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:02:49.564673	True	167	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:02:49.705316	True	161	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:49.713368	True	157	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:02:49.716700	True	145	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:49.821217	True	257	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:02:49.874870	True	161	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:02:49.900269	True	195	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:50.040306	True	212	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:50.091925	True	191	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:02:50.105579	True	230	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:02:50.263282	True	171	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:02:50.266596	True	153	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:50.478705	True	215	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:02:50.640413	True	154	disconnect vip-ucsb1.emea-sp.cisco.com
```
