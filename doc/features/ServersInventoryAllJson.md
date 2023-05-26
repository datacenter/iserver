# Servers inventory in JSON format

Use JSON (-o json) output format.

```
# iserver get servers -o json

[
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5e8c4ed26176752d32d51c40",
        "DeviceMoId": "5e8c4ecd6f72612d302b11a6",
        "Name": "esx2-eu-spdc-FCH2004V1PV",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2004V1PV",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 16,
        "NumThreads": 32,
        "Cpu": "2S 16C 32T",
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
        "ManagementIp": "10.58.28.34",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5ecf828a6176752d35b7eb9a",
        "DeviceMoId": "5ecf82676f72612d30687409",
        "Name": "mgmt-p4a-eu-spdc-WZP22520Y9D",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP22520Y9D",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 96,
        "Cpu": "2S 48C 96T",
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
        "ManagementIp": "10.58.29.60",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.RRRR"
        },
        "Moid": "5ecf86f16176752d35b94401",
        "DeviceMoId": "5ecf86d86f72612d3068b4bc",
        "Name": "comp1-p2a-eu-spdc-WZP22511E6V",
        "Model": "UCSC-C240-M5SX",
        "Serial": "WZP22511E6V",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
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
        "ManagementIp": "10.58.28.51",
        "AlarmSummary": {
            "Critical": 1,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Critical (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P- C(1)",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5ecf87c56176752d35b97fa4",
        "DeviceMoId": "5ecf87bc6f72612d3068c346",
        "Name": "znas-eu-spdc-WZP22511E3P",
        "Model": "UCSC-C240-M5SX",
        "Serial": "WZP22511E3P",
        "ManagementMode": "IntersightStandalone",
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
        "ManagementIp": "10.58.28.56",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "Connected": false,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fa045ce6176752d35c9d2f5",
        "DeviceMoId": "5fa045b46f72612d3086c548",
        "Name": "esx3-eu-spdc-FCH2004V0RW",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2004V0RW",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 16,
        "NumThreads": 32,
        "Cpu": "2S 16C 32T",
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
        "ManagementIp": "10.58.28.35",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fa048b06176752d35cae964",
        "DeviceMoId": "5fa0489f6f72612d30878741",
        "Name": "esx5-eu-spdc-FCH2017V024",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2017V024",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 36,
        "NumThreads": 72,
        "Cpu": "2S 36C 72T",
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
        "ManagementIp": "10.58.28.50",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fa04aa26176752d35cba3c9",
        "DeviceMoId": "5fa04a9e6f72612d30880e03",
        "Name": "mgmt-p1-eu-spdc-WZP2252176Z",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP2252176Z",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 96,
        "Cpu": "2S 48C 96T",
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
        "ManagementIp": "10.58.28.40",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fa04baa6176752d35cc0518",
        "DeviceMoId": "5fa04b536f72612d30883fd0",
        "Name": "aio-1-p1-eu-spdc-WZP22490ZCU",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP22490ZCU",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 44,
        "NumThreads": 88,
        "Cpu": "2S 44C 88T",
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
        "ManagementIp": "10.58.28.41",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fa04c3a6176752d35cc3569",
        "DeviceMoId": "5fa04be16f72612d30886344",
        "Name": "aio-2-p1-eu-spdc-WZP22520Y69",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP22520Y69",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.28.42",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fa04cc16176752d35cc60ce",
        "DeviceMoId": "5fa04cb86f72612d30889bc8",
        "Name": "aio-3-p1-eu-spdc-WZP22520Y54",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP22520Y54",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 44,
        "NumThreads": 88,
        "Cpu": "2S 44C 88T",
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
        "ManagementIp": "10.58.28.43",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fa04e266176752d35cce224",
        "DeviceMoId": "5fa04dd16f72612d3088e6b1",
        "Name": "comp1-p1-eu-spdc-WZP22520Y9J",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP22520Y9J",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 96,
        "Cpu": "2S 48C 96T",
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
        "ManagementIp": "10.58.28.44",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fa04e8e6176752d35cd0c4e",
        "DeviceMoId": "5fa04e6c6f72612d30890d70",
        "Name": "comp2-p1-spdc-WZP22520Y95",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP22520Y95",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 96,
        "Cpu": "2S 48C 96T",
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
        "ManagementIp": "10.58.28.45",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fa051816176752d35ce095c",
        "DeviceMoId": "5fa051776f72612d3089d7e9",
        "Name": "comp4-p1-eu-spdc-FCH2016V23J",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2016V23J",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.28.47",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "Connected": false,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fa052a26176752d35ce6572",
        "DeviceMoId": "5fa052926f72612d308a2325",
        "Name": "comp5-p1-eu-spdc-FCH2017V0TN",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2017V0TN",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.28.48",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "Connected": false,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fa1a79b6176752d35486b5c",
        "DeviceMoId": "5fa1a78b6f72612d30e49bd3",
        "Name": "tnas-eu-spdc-WZP22511E68",
        "Model": "UCSC-C240-M5SX",
        "Serial": "WZP22511E68",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.25.52",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
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
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fe295aa6176752d35119a62",
        "DeviceMoId": "5fe295916f72612d306438ac",
        "Name": "esx6-eu-spdc-FCH2006V04E",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2006V04E",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 16,
        "NumThreads": 32,
        "Cpu": "2S 16C 32T",
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
        "ManagementIp": "10.58.28.57",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.RRRR"
        },
        "Moid": "5fe32f176176752d354c125a",
        "DeviceMoId": "5fe32eb66f72612d3075c96a",
        "Name": "esx7-eu-spdc-FCH2004V0M6",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2004V0M6",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 16,
        "NumThreads": 32,
        "Cpu": "2S 16C 32T",
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
        "ManagementIp": "10.58.28.58",
        "AlarmSummary": {
            "Critical": 1,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Critical (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ C(1)",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "5fe32f536176752d354c2ade",
        "DeviceMoId": "5fe32f4d6f72612d3075db4b",
        "Name": "esx8-eu-spdc-FCH2017V0T1",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2017V0T1",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.28.59",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6026a92e6176752d350ac89a",
        "DeviceMoId": "6026a9096f72612d305e7b8b",
        "Name": "POD-4A-AIO-1-WZP23400AK9",
        "Model": "UCSC-C240-M5SN",
        "Serial": "WZP23400AK9",
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
        "ManagementIp": "10.58.29.55",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6026a9ba6176752d350b0bc2",
        "DeviceMoId": "6026a9976f72612d305e8e4c",
        "Name": "POD-4A-AIO-2-WZP23400AK7",
        "Model": "UCSC-C240-M5SN",
        "Serial": "WZP23400AK7",
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
        "ManagementIp": "10.58.29.56",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6026aa596176752d350b5bd5",
        "DeviceMoId": "6026aa376f72612d305ea314",
        "Name": "POD-4A-AIO-3-WZP23400AM2",
        "Model": "UCSC-C240-M5SN",
        "Serial": "WZP23400AM2",
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
        "ManagementIp": "10.58.29.57",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6026ab006176752d350bb5b4",
        "DeviceMoId": "6026aade6f72612d305eb7fd",
        "Name": "comp1-p4A-eu-spdc",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WMP24040045",
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
        "ManagementIp": "10.58.29.54",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6026ab926176752d350bfa1f",
        "DeviceMoId": "6026ab6f6f72612d305ec984",
        "Name": "comp2-p4a-eu-spdc-WZP22520B04",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP22520B04",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 96,
        "Cpu": "2S 48C 96T",
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
        "ManagementIp": "10.58.29.58",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.RRRR"
        },
        "Moid": "6026ae316176752d350d1cf6",
        "DeviceMoId": "6026ae116f72612d305f1e80",
        "Name": "comp3-p2a-eu-spdc-WZP2335149W",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP2335149W",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 16,
        "NumThreads": 32,
        "Cpu": "2S 16C 32T",
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
        "ManagementIp": "10.58.28.53",
        "AlarmSummary": {
            "Critical": 1,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Critical (1)",
        "Connected": false,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P- C(1)",
        "FlagManagement": "cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "6026af226176752d350d8b38",
        "DeviceMoId": "6026aefd6f72612d305f3c94",
        "Name": "comp4-p2a-eu-spdc-WZP22520Y8W",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP22520Y8W",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
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
        "ManagementIp": "10.58.28.54",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6026b0086176752d350dec89",
        "DeviceMoId": "6026afe76f72612d305f5af6",
        "Name": "esx01-eu-spdc-WZP22520Y99",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP22520Y99",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
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
        "ManagementIp": "10.58.29.37",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6026b0c56176752d350e3741",
        "DeviceMoId": "6026b0a16f72612d305f7116",
        "Name": "esx00-eu-spdc-WZP22520AXQ",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP22520AXQ",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 96,
        "Cpu": "2S 48C 96T",
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
        "ManagementIp": "10.58.29.36",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6026b2946176752d350ef654",
        "DeviceMoId": "6026b2376f72612d305fa447",
        "Name": "comp3-p4a-eu-spdc-WZP22520Y8X",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP22520Y8X",
        "ManagementMode": "IntersightStandalone",
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
        "ManagementIp": "10.58.29.59",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "6026b5ab6176752d35104d78",
        "DeviceMoId": "6026b5846f72612d30b98bb0",
        "Name": "aio1-p5g-eu-spdc-WZP23450C7D",
        "Model": "UCSC-C240-M5SX",
        "Serial": "WZP23450C7D",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 96,
        "Cpu": "2S 48C 96T",
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
        "ManagementIp": "10.58.25.41",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "Connected": false,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "6026b65f6176752d35109d55",
        "DeviceMoId": "6026b6346f72612d30b997b6",
        "Name": "aio2-p5g-eu-spdc-WZP23450C8M",
        "Model": "UCSC-C240-M5SX",
        "Serial": "WZP23450C8M",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 96,
        "Cpu": "2S 48C 96T",
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
        "ManagementIp": "10.58.25.42",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "Connected": false,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6026b9a26176752d3537f191",
        "DeviceMoId": "6026b8a26f72612d30b9b627",
        "Name": "aio3-p5g-eu-spdc-WZP23450C8K",
        "Model": "UCSC-C240-M5SX",
        "Serial": "WZP23450C8K",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 96,
        "Cpu": "2S 48C 96T",
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
        "ManagementIp": "10.58.50.51",
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
        "Groups": "",
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
        "TypeModel": "(R) UCSC-C240-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6026bb9c6176752d353915f2",
        "DeviceMoId": "6026b9416f72612d30b9be8a",
        "Name": "cu-p5g-eu-spdc-WZP23440N11",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP23440N11",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 96,
        "Cpu": "2S 48C 96T",
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
        "ManagementIp": "10.58.29.49",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G.."
        },
        "Moid": "6026bc4e6176752d3539ad8b",
        "DeviceMoId": "6026bbb86f72612d30b9e10d",
        "Name": "core-p5g-eu-spdc-WZP23440N02",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP23440N02",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 96,
        "Cpu": "2S 48C 96T",
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
        "ManagementIp": "10.58.29.50",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "Connected": false,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": true,
        "FlagState": "P+ H L",
        "FlagManagement": "cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "6026c0526176752d353b8b29",
        "DeviceMoId": "6026c0336f72612d30ba2932",
        "Name": "esx22-eu-spdc-WZP2343171Y",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP2343171Y",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 96,
        "Cpu": "2S 48C 96T",
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
        "ManagementIp": "10.58.50.39",
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
        "Groups": "",
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
        "FlagState": "P- H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6061d6c06176752d357360aa",
        "DeviceMoId": "6061d69a6f72612d30c09961",
        "Name": " C220-WZP23360FH9",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP23360FH9",
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
        "ManagementIp": "10.58.244.70",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "606323a46176752d350804cb",
        "DeviceMoId": "606323916f72612d30e34f36",
        "Name": " C220-WZP23350ZAQ",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP23350ZAQ",
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
        "ManagementIp": "10.58.244.186",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "60632bda6176752d350b9fc0",
        "DeviceMoId": "60632bb46f72612d30e4222e",
        "Name": "C240-WZP232102PH",
        "Model": "UCSC-C240-M5SX",
        "Serial": "WZP232102PH",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 56,
        "NumThreads": 112,
        "Cpu": "2S 56C 112T",
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
        "ManagementIp": "10.58.244.236",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.RRRR"
        },
        "Moid": "60632dcf6176752d350c72bc",
        "DeviceMoId": "60632d896f72612d30e45356",
        "Name": "C220-231",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP23240NNZ",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
        "AvailableMemory": 327680,
        "TotalMemory": 393216,
        "UsedMemory": 65536,
        "TotalMemoryUnit": "384 [GiB]",
        "TotalMemoryGB": 384,
        "AvailableMemoryUnit": "320 [GiB]",
        "AvailableMemoryGB": 320,
        "UsedMemoryUnit": "64 [GiB]",
        "UsedMemoryGB": 64,
        "UsedMemoryPct": 16,
        "UsedMemoryPctUnit": "16%",
        "ManagementIp": "10.58.250.241",
        "AlarmSummary": {
            "Critical": 1,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Critical (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ C(1)",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6098fe686176752d35a6dbc8",
        "DeviceMoId": "6098fe506f72612d30e78ffb",
        "Name": "esx91-eu-spdc-WZP234411LW",
        "Model": "UCSC-C240-M5SX",
        "Serial": "WZP234411LW",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.25.33",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "61260a8076752d3131235d3a",
        "DeviceMoId": "5ecf87256f72612d3068b971",
        "Name": "comp2-p2a-eu-spdc-WZP22511E6G",
        "Model": "UCSC-C240-M5SX",
        "Serial": "WZP22511E6G",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
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
        "ManagementIp": "10.58.28.52",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "61324fa676752d3131fd5d08",
        "DeviceMoId": "61320ad96f72612d300340e7",
        "Name": "esx20-eu-spdc-WMP24040053",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WMP24040053",
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
        "ManagementIp": "10.58.50.40",
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
        "Groups": "pod2b",
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
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6139bd4e76752d3137136802",
        "DeviceMoId": "6139bd1a6f72612d30db6982",
        "Name": "du-p5g-eu-spdc-WZP2526088F",
        "Model": "UCSC-C240-M5SX",
        "Serial": "WZP2526088F",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 48,
        "Cpu": "2S 48C 48T",
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
        "ManagementIp": "10.58.29.48",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "6141c1f676752d313775876f",
        "DeviceMoId": "6141c1e76f72612d30d2b35f",
        "Name": "esx95-eu-spdc-FCH2017V241",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2017V241",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 16,
        "NumThreads": 32,
        "Cpu": "2S 16C 32T",
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
        "ManagementIp": "10.58.25.37",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6141c32376752d313775f536",
        "DeviceMoId": "6141c3186f72612d30d2d8f8",
        "Name": "esx93-eu-spdc-FCH2108V1HE",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2108V1HE",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.25.35",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.YYYY"
        },
        "Moid": "6141c3ad76752d31377629ad",
        "DeviceMoId": "6141c37c6f72612d30d2e54d",
        "Name": "esx92-eu-spdc-FCH2017V2AF",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2017V2AF",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.25.34",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 1,
            "Info": 1
        },
        "Health": "Warnings (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ W(1)",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.YYYY"
        },
        "Moid": "6141c3b676752d3137762cf2",
        "DeviceMoId": "6141c3976f72612d30d2e7d0",
        "Name": "esx94-eu-spdc-FCH2017V2AH",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2017V2AH",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.25.36",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 2,
            "Info": 1
        },
        "Health": "Warnings (2)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P- W(2)",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6169b3bd76752d313972fba0",
        "DeviceMoId": "6169b3926f72612d30589b53",
        "Name": "esx9-eu-spdc-FCH2016V23J",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2016V23J",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.28.60",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6169b76576752d313973e815",
        "DeviceMoId": "6169b7086f72612d3058fe9b",
        "Name": "esx10-eu-spdc-FCH2017V0TN",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2017V0TN",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.28.61",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "616ea34876752d3139b2261f",
        "DeviceMoId": "616ea3296f72612d30e81fe9",
        "Name": "esx11-eu-spdc-FCH2050V125",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2050V125",
        "ManagementMode": "IntersightStandalone",
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
        "ManagementIp": "10.58.29.51",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.YYYY"
        },
        "Moid": "61c35fad76752d3139f50e2d",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "Name": "berlin-ucsm-2",
        "Model": "UCSC-C240-M4S",
        "Serial": "FCH1930V0PH",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
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
        "ManagementIp": "10.49.234.198",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 1,
            "Info": 0
        },
        "Health": "Warnings (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ W(1)",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.YYYY"
        },
        "Moid": "61c35fad76752d3139f50e3e",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "Name": "berlin-ucsm-6",
        "Model": "UCSC-C240-M4S",
        "Serial": "FCH1930V0KM",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
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
        "ManagementIp": "10.49.234.195",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 1,
            "Info": 0
        },
        "Health": "Warnings (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ W(1)",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "61c35fad76752d3139f50e50",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "Name": "berlin-ucsm-1",
        "Model": "UCSC-C240-M5SX",
        "Serial": "WZP21490417",
        "ManagementMode": "UCSM",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
        "AvailableMemory": 720896,
        "TotalMemory": 720896,
        "UsedMemory": 0,
        "TotalMemoryUnit": "704 [GiB]",
        "TotalMemoryGB": 704,
        "AvailableMemoryUnit": "704 [GiB]",
        "AvailableMemoryGB": 704,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.49.234.199",
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
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.YYYY"
        },
        "Moid": "61c35fad76752d3139f50e78",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "Name": "berlin-ucsm-4",
        "Model": "UCSC-C240-M4SX",
        "Serial": "FCH1916V1CT",
        "ManagementMode": "UCSM",
        "OperPowerState": "off",
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
        "ManagementIp": "10.49.234.197",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 1,
            "Info": 0
        },
        "Health": "Warnings (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M4SX",
        "LocatorLedOn": false,
        "FlagState": "P- W(1)",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.YYYY"
        },
        "Moid": "61c35fad76752d3139f50e88",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "Name": "berlin-ucsm-5",
        "Model": "UCSC-C240-M4SX",
        "Serial": "FCH1916V0UY",
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
        "ManagementIp": "10.49.234.206",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 2,
            "Info": 1
        },
        "Health": "Warnings (2)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M4SX",
        "LocatorLedOn": false,
        "FlagState": "P+ W(2)",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.YYYY"
        },
        "Moid": "61c35fad76752d3139f50eae",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "Name": "berlin-ucsm-8",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH1849V26H",
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
        "ManagementIp": "10.49.234.194",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 1,
            "Info": 0
        },
        "Health": "Warnings (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ W(1)",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.YYYY"
        },
        "Moid": "61c35fad76752d3139f50efa",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "Name": "berlin-ucsm-7",
        "Model": "UCSC-C240-M4S",
        "Serial": "FCH1930V1LA",
        "ManagementMode": "UCSM",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
        "AvailableMemory": 786432,
        "TotalMemory": 786432,
        "UsedMemory": 0,
        "TotalMemoryUnit": "768 [GiB]",
        "TotalMemoryGB": 768,
        "AvailableMemoryUnit": "768 [GiB]",
        "AvailableMemoryGB": 768,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.49.234.205",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 1,
            "Info": 0
        },
        "Health": "Warnings (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M4S",
        "LocatorLedOn": false,
        "FlagState": "P- W(1)",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "61df0d5676752d3139507e9e",
        "DeviceMoId": "61df0d3c6f72612d307e5a50",
        "Name": "sn12-eu-spdc-WZP23430C4D",
        "Model": "SE-NODE-G2",
        "Serial": "WZP23430C4D",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 20,
        "NumThreads": 40,
        "Cpu": "2S 20C 40T",
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
        "ManagementIp": "10.58.29.34",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) SE-NODE-G2",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.RRRR"
        },
        "Moid": "61df0e1476752d313950b310",
        "DeviceMoId": "61df0df76f72612d307e6ad3",
        "Name": "sn13-eu-spdc-WZP234301R9",
        "Model": "SE-NODE-G2",
        "Serial": "WZP234301R9",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 20,
        "NumThreads": 40,
        "Cpu": "2S 20C 40T",
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
        "ManagementIp": "10.58.29.35",
        "AlarmSummary": {
            "Critical": 1,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Critical (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) SE-NODE-G2",
        "LocatorLedOn": false,
        "FlagState": "P+ C(1)",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "61df120b76752d3139518492",
        "DeviceMoId": "61df11db6f72612d307ebf0f",
        "Name": "sn11-eu-spdc-WZP23430C4N",
        "Model": "SE-NODE-G2",
        "Serial": "WZP23430C4N",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 20,
        "NumThreads": 40,
        "Cpu": "2S 20C 40T",
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
        "ManagementIp": "10.58.29.33",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) SE-NODE-G2",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "61e9985676752d3139e59f59",
        "DeviceMoId": "61e998396f72612d305682d9",
        "Name": "comp2-p3b-eu-spdc-FCH2017V1J8",
        "Model": "UCSC-C240-M4SX",
        "Serial": "FCH2017V1J8",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 16,
        "NumThreads": 32,
        "Cpu": "2S 16C 32T",
        "AvailableMemory": 131072,
        "TotalMemory": 131072,
        "UsedMemory": 0,
        "TotalMemoryUnit": "128 [GiB]",
        "TotalMemoryGB": 128,
        "AvailableMemoryUnit": "128 [GiB]",
        "AvailableMemoryGB": 128,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.50.49",
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
        "Groups": "p3b",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M4SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "61e99b6176752d3139e62d14",
        "DeviceMoId": "61e99b2d6f72612d3056bb7d",
        "Name": "comp3-p3b-eu-spdc-FCH2017V1J5",
        "Model": "UCSC-C240-M4SX",
        "Serial": "FCH2017V1J5",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 16,
        "NumThreads": 32,
        "Cpu": "2S 16C 32T",
        "AvailableMemory": 131072,
        "TotalMemory": 131072,
        "UsedMemory": 0,
        "TotalMemoryUnit": "128 [GiB]",
        "TotalMemoryGB": 128,
        "AvailableMemoryUnit": "128 [GiB]",
        "AvailableMemoryGB": 128,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.50.50",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 1
        },
        "Health": "Healthy (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "p3b",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M4SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "61e99fb976752d3139e71340",
        "DeviceMoId": "61e99f9c6f72612d3057152d",
        "Name": "comp4-p3b-eu-spdc-FCH2108V1FC",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2108V1FC",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.50.57",
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
        "Groups": "p3b",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "61e9a1ba76752d3139e778f3",
        "DeviceMoId": "61e9a19a6f72612d30573d28",
        "Name": "comp5-p3b-eu-spdc-FCH2017V1Y6",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2017V1Y6",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.50.58",
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
        "Groups": "p3b",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "61e9a43176752d3139e7f79a",
        "DeviceMoId": "61e9a40d6f72612d30576dcc",
        "Name": "comp6-p3b-eu-spdc-FCH2017V24J",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2017V24J",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.50.59",
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
        "Groups": "p3b",
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
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "61fa65c276752d3139491f4a",
        "DeviceMoId": "61fa65ab6f72612d300ab92a",
        "Name": "comp1-p3b-eu-spdc-FCH2017V1J7",
        "Model": "UCSC-C240-M4SX",
        "Serial": "FCH2017V1J7",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 16,
        "NumThreads": 32,
        "Cpu": "2S 16C 32T",
        "AvailableMemory": 131072,
        "TotalMemory": 131072,
        "UsedMemory": 0,
        "TotalMemoryUnit": "128 [GiB]",
        "TotalMemoryGB": 128,
        "AvailableMemoryUnit": "128 [GiB]",
        "AvailableMemoryGB": 128,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.50.48",
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
        "Groups": "p3b",
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
        "TypeModel": "(R) UCSC-C240-M4SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "62d157fd76752d313915f4f6",
        "DeviceMoId": "62d157f56f72612d31c554a7",
        "Name": "HX1-eu-spdc-2",
        "Model": "HXAF220C-M5SN",
        "Serial": "WZP24100SN0",
        "ManagementMode": "UCSM",
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
        "ManagementIp": "10.58.24.55",
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
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) HXAF220C-M5SN",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "62d157fe76752d313915f512",
        "DeviceMoId": "62d157f56f72612d31c554a7",
        "Name": "HX1-eu-spdc-6",
        "Model": "HXAF240C-M5SX",
        "Serial": "WMP250901AY",
        "ManagementMode": "UCSM",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 52,
        "NumThreads": 104,
        "Cpu": "2S 52C 104T",
        "AvailableMemory": 786432,
        "TotalMemory": 786432,
        "UsedMemory": 0,
        "TotalMemoryUnit": "768 [GiB]",
        "TotalMemoryGB": 768,
        "AvailableMemoryUnit": "768 [GiB]",
        "AvailableMemoryGB": 768,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.24.59",
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
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) HXAF240C-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.RRRR"
        },
        "Moid": "62d157fe76752d313915f529",
        "DeviceMoId": "62d157f56f72612d31c554a7",
        "Name": "HX1-eu-spdc-4",
        "Model": "HXAF220C-M5SN",
        "Serial": "WZP24100SMP",
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
        "ManagementIp": "10.58.24.57",
        "AlarmSummary": {
            "Critical": 3,
            "Warning": 4,
            "Info": 3
        },
        "Health": "Critical (3)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) HXAF220C-M5SN",
        "LocatorLedOn": false,
        "FlagState": "P+ C(3)",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "62d157fe76752d313915f549",
        "DeviceMoId": "62d157f56f72612d31c554a7",
        "Name": "HX1-eu-spdc-5",
        "Model": "HXAF240C-M5SX",
        "Serial": "WMP250901B0",
        "ManagementMode": "UCSM",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 52,
        "NumThreads": 104,
        "Cpu": "2S 52C 104T",
        "AvailableMemory": 786432,
        "TotalMemory": 786432,
        "UsedMemory": 0,
        "TotalMemoryUnit": "768 [GiB]",
        "TotalMemoryGB": 768,
        "AvailableMemoryUnit": "768 [GiB]",
        "AvailableMemoryGB": 768,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.24.58",
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
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) HXAF240C-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "62d157fe76752d313915f563",
        "DeviceMoId": "62d157f56f72612d31c554a7",
        "Name": "HX1-eu-spdc-7",
        "Model": "HXAF240C-M5SX",
        "Serial": "WMP2509019D",
        "ManagementMode": "UCSM",
        "OperPowerState": "off",
        "NumCpus": 2,
        "NumCpuCores": 52,
        "NumThreads": 104,
        "Cpu": "2S 52C 104T",
        "AvailableMemory": 786432,
        "TotalMemory": 786432,
        "UsedMemory": 0,
        "TotalMemoryUnit": "768 [GiB]",
        "TotalMemoryGB": 768,
        "AvailableMemoryUnit": "768 [GiB]",
        "AvailableMemoryGB": 768,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.24.54",
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
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) HXAF240C-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "62e2b54b76752d3139eab326",
        "DeviceMoId": "62d157f56f72612d31c554a7",
        "Name": "HX1-eu-spdc-3",
        "Model": "HXAF220C-M5SN",
        "Serial": "WZP24100SML",
        "ManagementMode": "UCSM",
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
        "ManagementIp": "10.58.24.53",
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
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) HXAF220C-M5SN",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.RRRR"
        },
        "Moid": "62ebeb3876752d3139464b1f",
        "DeviceMoId": "62d157f56f72612d31c554a7",
        "Name": "HX1-eu-spdc-1",
        "Model": "HXAF220C-M5SN",
        "Serial": "WZP24100SMV",
        "ManagementMode": "UCSM",
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
        "ManagementIp": "10.58.24.56",
        "AlarmSummary": {
            "Critical": 2,
            "Warning": 6,
            "Info": 2
        },
        "Health": "Critical (2)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) HXAF220C-M5SN",
        "LocatorLedOn": false,
        "FlagState": "P- C(2)",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.YYYY"
        },
        "Moid": "6311aae876752d31398e1a50",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "Name": "berlin-ucsm-3",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2031V0YM",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
        "AvailableMemory": 688128,
        "TotalMemory": 688128,
        "UsedMemory": 0,
        "TotalMemoryUnit": "672 [GiB]",
        "TotalMemoryGB": 672,
        "AvailableMemoryUnit": "672 [GiB]",
        "AvailableMemoryGB": 672,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.49.234.196",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 1,
            "Info": 1
        },
        "Health": "Warnings (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": false
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ W(1)",
        "FlagManagement": "Cu",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6336f19576752d3139f05a4b",
        "DeviceMoId": "6336f14d6f72612d31d41b72",
        "Name": "esx21-eu-spdc-WZP23440N1P",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WZP23440N1P",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 96,
        "Cpu": "2S 48C 96T",
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
        "ManagementIp": "10.58.50.38",
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
        "Groups": "",
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
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "637b898f76752d3139ba61cc",
        "DeviceMoId": "637b897f6f72612d39f8b9e9",
        "Name": "HPE-ProLiant DL360 Gen10 Plus-VYRBX9UJ4S",
        "Model": "ProLiant DL360 Gen10 Plus",
        "Serial": "VYRBX9UJ4S",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 56,
        "NumThreads": 112,
        "Cpu": "2S 56C 112T",
        "AvailableMemory": 32768,
        "TotalMemory": 32768,
        "UsedMemory": 0,
        "TotalMemoryUnit": "32 [GiB]",
        "TotalMemoryGB": 32,
        "AvailableMemoryUnit": "32 [GiB]",
        "AvailableMemoryGB": 32,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.242.29.174",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) ProLiant DL360 Gen10 Plus",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "637b8a1276752d3139ba7805",
        "DeviceMoId": "637b8a016f72612d39f8bfa7",
        "Name": "Dell-PowerEdge R650-YGFCBTJSO8WOMR",
        "Model": "PowerEdge R650",
        "Serial": "YGFCBTJSO8WOMR",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 56,
        "NumThreads": 112,
        "Cpu": "2S 56C 112T",
        "AvailableMemory": 131072,
        "TotalMemory": 131072,
        "UsedMemory": 0,
        "TotalMemoryUnit": "128 [GiB]",
        "TotalMemoryGB": 128,
        "AvailableMemoryUnit": "128 [GiB]",
        "AvailableMemoryGB": 128,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.44.182.90",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) PowerEdge R650",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "637ca9b576752d3139eea04f",
        "DeviceMoId": "637ca8cd6f72612d3130bddc",
        "Name": "esx12-eu-spdc-FCH2049V1WU",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2049V1WU",
        "ManagementMode": "IntersightStandalone",
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
        "ManagementIp": "10.58.29.52",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.YYYY"
        },
        "Moid": "637caeb676752d3139ef7b01",
        "DeviceMoId": "637cadbb6f72612d3130e87a",
        "Name": "esx13-eu-spdc-FCH2018V027",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2018V027",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 16,
        "NumThreads": 32,
        "Cpu": "2S 16C 32T",
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
        "ManagementIp": "10.58.29.53",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 1,
            "Info": 1
        },
        "Health": "Warnings (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ W(1)",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "637ce9a576752d3139f994e1",
        "DeviceMoId": "637ce9916f72612d3132dcb3",
        "Name": "esx4-eu-spdc-FCH2016V2BE",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2016V2BE",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 36,
        "NumThreads": 72,
        "Cpu": "2S 36C 72T",
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
        "ManagementIp": "10.58.28.36",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "637d61fd76752d31390ef488",
        "DeviceMoId": "637d60986f72612d31377620",
        "Name": "esx1-eu-spdc-FCH2017V0T3",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2017V0T3",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.28.33",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "637d65ac76752d3139102834",
        "DeviceMoId": "637d63196f72612d313788d7",
        "Name": "esx14-eu-spdc-FCH2017V0TE",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2017V0TE",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.29.42",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 1
        },
        "Health": "Healthy (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.RRRR"
        },
        "Moid": "637f588776752d313966cb9d",
        "DeviceMoId": "637f58116f72612d31490de7",
        "Name": "comp7-p3b-eu-spdc-FCH2023V2A4",
        "Model": "UCSC-C220-M4S",
        "Serial": "FCH2023V2A4",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 28,
        "NumThreads": 56,
        "Cpu": "2S 28C 56T",
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
        "ManagementIp": "10.58.50.60",
        "AlarmSummary": {
            "Critical": 1,
            "Warning": 1,
            "Info": 1
        },
        "Health": "Critical (1)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "TypeModel": "(R) UCSC-C220-M4S",
        "LocatorLedOn": false,
        "FlagState": "P+ C(1)",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6384d45476752d31395c7874",
        "DeviceMoId": "6384d44a6f72612d317bfc51",
        "Name": "comp2-p4b-eu-spdc-WZP26360D3D",
        "Model": "UCSC-C245-M6SX",
        "Serial": "WZP26360D3D",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 128,
        "NumThreads": 256,
        "Cpu": "2S 128C 256T",
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
        "ManagementIp": "10.58.53.34",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C245-M6SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6385018e76752d313964b3b5",
        "DeviceMoId": "638501816f72612d317dabd7",
        "Name": "comp3-p4b-eu-spdc-WZP262207UM",
        "Model": "UCSC-C225-M6S",
        "Serial": "WZP262207UM",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 1,
        "NumCpuCores": 64,
        "NumThreads": 128,
        "Cpu": "1S 64C 128T",
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
        "ManagementIp": "10.58.53.35",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C225-M6S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6385028e76752d313964e821",
        "DeviceMoId": "638502356f72612d317db208",
        "Name": "comp4-p4b-eu-spdc-WZP262207VP",
        "Model": "UCSC-C225-M6S",
        "Serial": "WZP262207VP",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 1,
        "NumCpuCores": 32,
        "NumThreads": 64,
        "Cpu": "1S 32C 64T",
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
        "ManagementIp": "10.58.53.36",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C225-M6S",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6388e77876752d313919a95d",
        "DeviceMoId": "6388e7616f72612d31a41c5c",
        "Name": "comp1-p4b-eu-spdc-WZP26360D36",
        "Model": "UCSC-C245-M6SX",
        "Serial": "WZP26360D36",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 48,
        "NumThreads": 96,
        "Cpu": "2S 48C 96T",
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
        "ManagementIp": "10.58.53.33",
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
        "Groups": "",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C245-M6SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":RR.G"
        },
        "Moid": "5efdfb996176752d3559b9d5",
        "DeviceMoId": "5efdfb7e6f72612d30e4501e",
        "Name": "C3X60M4-FCH21067808",
        "Model": "UCSC-C3K-M4SRB",
        "Serial": "FCH21067808",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
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
        "ManagementIp": "",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "Connected": false,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "",
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
        "Type": "Blade",
        "TypeModel": "(B) UCSC-C3K-M4SRB",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "cri",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "61bb973176752d3139b05b78",
        "DeviceMoId": "61bb97146f72612d301e5946",
        "Name": "ynas-eu-spdc-FCH21067808",
        "Model": "UCSC-C3K-M4SRB",
        "Serial": "FCH21067808",
        "ManagementMode": "IntersightStandalone",
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
        "ManagementIp": "",
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
        "Groups": "",
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
        "Type": "Blade",
        "TypeModel": "(B) UCSC-C3K-M4SRB",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "Cri",
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
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    }
]
```

Developer output

```
# iserver get servers -o json

Developer output

{
    "duration": 6062,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 5972
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
        "lines": 48
    }
}

Log: isctl
-----------

2022-12-13 16:57:34.098538	True	2152	93	isctl get compute rackunit   -o json --top 100
2022-12-13 16:57:34.924605	True	825	10	isctl get compute blade   -o json --top 100
2022-12-13 16:57:35.542383	True	572	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T16:57:34.000Z"  -o json --top 100
2022-12-13 16:57:35.584451	True	616	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 16:57:36.325197	True	1360	100	isctl get asset deviceregistration   -o json --top 100
2022-12-13 16:57:36.772693	True	447	9	isctl get asset deviceregistration   -o json --top 100 --skip 100
```
