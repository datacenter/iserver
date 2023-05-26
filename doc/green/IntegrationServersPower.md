# Get Intersight Servers with Power Information

```
# iserver get servers --group power -c power

+---------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+
| SF      | MF  | WF | Name                           | Model              | Serial      | IP          | Consumed [W] | Min [W] | Avg [W] | Max [W] |
+---------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-1           | (B) UCSB-B200-M4   | FCH205371PZ | 10.58.52.33 | 138.0        | 138.0   | 142.36  | 144.0   | 
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-2           | (B) UCSB-B200-M4   | FCH20527XXD | 10.58.52.34 | 138.0        | 138.0   | 138.0   | 138.0   | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-1-3           | (B) UCSB-B200-M4   | FCH20437VXH | 10.58.52.35 | 126.0        | 126.0   | 126.0   | 126.0   | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-1-4           | (B) UCSB-B200-M4   | FCH205371UU | 10.58.52.36 | 126.0        | 126.0   | 126.0   | 126.0   | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-1           | (B) UCSB-B200-M5   | FLM241501FB | 10.58.52.41 | 241.8        | 237.9   | 242.36  | 249.6   | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-2           | (B) UCSB-B200-M5   | FLM24140BJB | 10.58.52.42 | 202.8        | 202.8   | 202.8   | 202.8   | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-3           | (B) UCSB-B200-M5   | FLM241501CT | 10.58.52.43 | 195.0        | 195.0   | 195.97  | 198.9   | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-4           | (B) UCSB-B200-M5   | FLM24140B0B | 10.58.52.44 | 230.1        | 230.1   | 234.0   | 237.9   | 
| P+ H    | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 |              |         |         |         | 
| P+ H    | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 |              |         |         |         | 
| P+ H    | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 |              |         |         |         | 
| P- H    | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 0            | 0       | 0       | 0       | 
| P- H    | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | 0            | 0       | 0       | 0       | 
| P- H    | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 |              |         |         |         | 
| P+ H    | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 |              |         |         |         | 
+---------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+
```

JSON Output

```
# iserver get servers --group power -c power

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
        "Power": null,
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
        "Power": null,
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
        "Power": null,
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
        "Power": {
            "Data": {
                "PowerControl": {
                    "PowerConsumedWatts": 0,
                    "LimitException": "NoAction",
                    "MinConsumedWatts": 0,
                    "AverageConsumedWatts": 0,
                    "MaxConsumedWatts": 0
                },
                "Voltage": [
                    {
                        "Name": "PSU1_VOUT",
                        "ReadingVolts": 0,
                        "UpperThresholdCritical": 14,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    },
                    {
                        "Name": "PSU2_VOUT",
                        "ReadingVolts": 0,
                        "UpperThresholdCritical": 14,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    },
                    {
                        "Name": "P3V_BAT_SCALED",
                        "ReadingVolts": 3.042,
                        "UpperThresholdCritical": 3.588,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    }
                ],
                "PowerSupply": [
                    {
                        "Name": "PSU1",
                        "Model": "700-014550-0000",
                        "SerialNumber": "APS240201EL",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10252046",
                        "PowerOutputWatts": 0,
                        "LastPowerOutputWatts": 0,
                        "PowerInputWatts": 7,
                        "PowerSupplyType": "AC",
                        "State": "Enabled",
                        "Health": "OK",
                        "MinimumVoltage": 180,
                        "OutputWattage": 1050,
                        "MaximumFrequencyHz": 63,
                        "MaximumVoltage": 264,
                        "MinimumFrequencyHz": 47
                    },
                    {
                        "Name": "PSU2",
                        "Model": "700-014550-0000",
                        "SerialNumber": "ART2601F4S6",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10252046",
                        "PowerOutputWatts": 0,
                        "LastPowerOutputWatts": 0,
                        "PowerInputWatts": 8,
                        "PowerSupplyType": "AC",
                        "State": "Enabled",
                        "Health": "OK",
                        "MinimumVoltage": 180,
                        "OutputWattage": 1050,
                        "MaximumFrequencyHz": 63,
                        "MaximumVoltage": 264,
                        "MinimumFrequencyHz": 47
                    }
                ]
            },
            "Summary": {
                "Source": "Redfish",
                "PowerNow": 0,
                "PowerMin": 0,
                "PowerAvg": 0,
                "PowerMax": 0
            }
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
        "Power": {
            "Data": {
                "PowerControl": {
                    "PowerConsumedWatts": 0,
                    "LimitException": "NoAction",
                    "MinConsumedWatts": 0,
                    "AverageConsumedWatts": 0,
                    "MaxConsumedWatts": 0
                },
                "Voltage": [
                    {
                        "Name": "PSU1_VOUT",
                        "ReadingVolts": 0,
                        "UpperThresholdCritical": 14,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    },
                    {
                        "Name": "PSU2_VOUT",
                        "ReadingVolts": 0,
                        "UpperThresholdCritical": 14,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    },
                    {
                        "Name": "P3V_BAT_SCALED",
                        "ReadingVolts": 3.026,
                        "UpperThresholdCritical": 3.588,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    }
                ],
                "PowerSupply": [
                    {
                        "Name": "PSU1",
                        "Model": "700-014550-0000",
                        "SerialNumber": "APS240201ES",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10252046",
                        "PowerOutputWatts": 0,
                        "LastPowerOutputWatts": 0,
                        "PowerInputWatts": 8,
                        "PowerSupplyType": "AC",
                        "State": "Enabled",
                        "Health": "OK",
                        "MinimumVoltage": 180,
                        "OutputWattage": 1050,
                        "MaximumFrequencyHz": 63,
                        "MaximumVoltage": 264,
                        "MinimumFrequencyHz": 47
                    },
                    {
                        "Name": "PSU2",
                        "Model": "700-014550-0000",
                        "SerialNumber": "ART2601F4S2",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10252046",
                        "PowerOutputWatts": 0,
                        "LastPowerOutputWatts": 0,
                        "PowerInputWatts": 8,
                        "PowerSupplyType": "AC",
                        "State": "Enabled",
                        "Health": "OK",
                        "MinimumVoltage": 180,
                        "OutputWattage": 1050,
                        "MaximumFrequencyHz": 63,
                        "MaximumVoltage": 264,
                        "MinimumFrequencyHz": 47
                    }
                ]
            },
            "Summary": {
                "Source": "Redfish",
                "PowerNow": 0,
                "PowerMin": 0,
                "PowerAvg": 0,
                "PowerMax": 0
            }
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
        "Power": null,
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
        "Power": null,
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
        "Power": {
            "Data": {
                "dn": "sys/chassis-2/blade-1/board/power-stats",
                "time_collected": "2022-12-13T18:02:43.799",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-1",
                "consumed_power": 241.8,
                "input_current": 19.99,
                "input_voltage": 12.1,
                "consumed_power_avg": 242.36,
                "input_current_avg": 20.09,
                "input_voltage_avg": 12.06,
                "consumed_power_min": 237.9,
                "input_current_min": 19.77,
                "input_voltage_min": 12.04,
                "consumed_power_max": 249.6,
                "input_current_max": 20.64,
                "input_voltage_max": 12.1
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 241.8,
                "PowerMin": 237.9,
                "PowerAvg": 242.36,
                "PowerMax": 249.6
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
        "Power": {
            "Data": {
                "dn": "sys/chassis-2/blade-2/board/power-stats",
                "time_collected": "2022-12-13T18:01:59.355",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-2",
                "consumed_power": 202.8,
                "input_current": 16.69,
                "input_voltage": 12.15,
                "consumed_power_avg": 202.8,
                "input_current_avg": 16.69,
                "input_voltage_avg": 12.15,
                "consumed_power_min": 202.8,
                "input_current_min": 16.69,
                "input_voltage_min": 12.15,
                "consumed_power_max": 202.8,
                "input_current_max": 16.69,
                "input_voltage_max": 12.15
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 202.8,
                "PowerMin": 202.8,
                "PowerAvg": 202.8,
                "PowerMax": 202.8
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
        "Power": {
            "Data": {
                "dn": "sys/chassis-1/blade-1/board/power-stats",
                "time_collected": "2022-12-13T18:01:56.154",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "consumed_power": 138.0,
                "input_current": 11.47,
                "input_voltage": 12.04,
                "consumed_power_avg": 142.36,
                "input_current_avg": 11.83,
                "input_voltage_avg": 12.04,
                "consumed_power_min": 138.0,
                "input_current_min": 11.47,
                "input_voltage_min": 12.04,
                "consumed_power_max": 144.0,
                "input_current_max": 11.96,
                "input_voltage_max": 12.04
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 138.0,
                "PowerMin": 138.0,
                "PowerAvg": 142.36,
                "PowerMax": 144.0
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
        "Power": {
            "Data": {
                "dn": "sys/chassis-1/blade-2/board/power-stats",
                "time_collected": "2022-12-13T18:01:57.019",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-2",
                "consumed_power": 138.0,
                "input_current": 11.52,
                "input_voltage": 11.98,
                "consumed_power_avg": 138.0,
                "input_current_avg": 11.52,
                "input_voltage_avg": 11.98,
                "consumed_power_min": 138.0,
                "input_current_min": 11.52,
                "input_voltage_min": 11.98,
                "consumed_power_max": 138.0,
                "input_current_max": 11.52,
                "input_voltage_max": 11.98
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 138.0,
                "PowerMin": 138.0,
                "PowerAvg": 138.0,
                "PowerMax": 138.0
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
        "Power": {
            "Data": {
                "dn": "sys/chassis-1/blade-3/board/power-stats",
                "time_collected": "2022-12-13T18:02:21.966",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-3",
                "consumed_power": 126.0,
                "input_current": 10.52,
                "input_voltage": 11.98,
                "consumed_power_avg": 126.0,
                "input_current_avg": 10.52,
                "input_voltage_avg": 11.98,
                "consumed_power_min": 126.0,
                "input_current_min": 10.52,
                "input_voltage_min": 11.98,
                "consumed_power_max": 126.0,
                "input_current_max": 10.52,
                "input_voltage_max": 11.98
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 126.0,
                "PowerMin": 126.0,
                "PowerAvg": 126.0,
                "PowerMax": 126.0
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
        "Power": {
            "Data": {
                "dn": "sys/chassis-1/blade-4/board/power-stats",
                "time_collected": "2022-12-13T18:02:01.350",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "consumed_power": 126.0,
                "input_current": 10.52,
                "input_voltage": 11.98,
                "consumed_power_avg": 126.0,
                "input_current_avg": 10.52,
                "input_voltage_avg": 11.98,
                "consumed_power_min": 126.0,
                "input_current_min": 10.52,
                "input_voltage_min": 11.98,
                "consumed_power_max": 126.0,
                "input_current_max": 10.52,
                "input_voltage_max": 11.98
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 126.0,
                "PowerMin": 126.0,
                "PowerAvg": 126.0,
                "PowerMax": 126.0
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
        "Power": {
            "Data": {
                "dn": "sys/chassis-2/blade-4/board/power-stats",
                "time_collected": "2022-12-13T18:01:52.294",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-4",
                "consumed_power": 230.1,
                "input_current": 19.02,
                "input_voltage": 12.1,
                "consumed_power_avg": 234.0,
                "input_current_avg": 19.35,
                "input_voltage_avg": 12.1,
                "consumed_power_min": 230.1,
                "input_current_min": 19.02,
                "input_voltage_min": 12.1,
                "consumed_power_max": 237.9,
                "input_current_max": 19.67,
                "input_voltage_max": 12.1
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 230.1,
                "PowerMin": 230.1,
                "PowerAvg": 234.0,
                "PowerMax": 237.9
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
        "Power": {
            "Data": {
                "dn": "sys/chassis-2/blade-3/board/power-stats",
                "time_collected": "2022-12-13T18:01:55.349",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-3",
                "consumed_power": 195.0,
                "input_current": 16.04,
                "input_voltage": 12.15,
                "consumed_power_avg": 195.97,
                "input_current_avg": 16.16,
                "input_voltage_avg": 12.12,
                "consumed_power_min": 195.0,
                "input_current_min": 16.04,
                "input_voltage_min": 12.1,
                "consumed_power_max": 198.9,
                "input_current_max": 16.44,
                "input_voltage_max": 12.15
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 195.0,
                "PowerMin": 195.0,
                "PowerAvg": 195.97,
                "PowerMax": 198.9
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
# iserver get servers --group power -c power

Developer output

{
    "duration": 10669,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 4987
    },
    "redfish": {
        "read": true,
        "success": 12,
        "failed": 10,
        "connect": 14,
        "disconnect": 0,
        "path": 8,
        "connect_time": 9658,
        "disconnect_time": 0,
        "path_time": 1217,
        "total_time": 10875
    },
    "ucsm": {
        "read": true,
        "success": 40,
        "failed": 0,
        "connect": 16,
        "disconnect": 0,
        "mo": 24,
        "connect_time": 7837,
        "disconnect_time": 0,
        "mo_time": 4676,
        "total_time": 12513
    },
    "ssh": {
        "read": false,
        "calls": 0,
        "total_time": 0
    },
    "error": {
        "read": true,
        "lines": 11
    },
    "info": {
        "read": true,
        "lines": 11
    },
    "debug": {
        "read": true,
        "lines": 74
    }
}

Log: info
----------

[2022-12-13 17:02:34.679457]	[connect]	Redfish authentication failed: 10.58.50.43 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:34.688049]	[disconnect]	Redfish session close failed: 10.58.50.43 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:34.725306]	[connect]	Redfish authentication failed: 10.58.50.42 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:34.730244]	[connect]	Redfish authentication failed: 10.58.50.41 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:34.737068]	[disconnect]	Redfish session close failed: 10.58.50.42 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:34.741453]	[disconnect]	Redfish session close failed: 10.58.50.41 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:36.062023]	[connect]	Redfish authentication failed: 10.58.50.46 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:36.067330]	[disconnect]	Redfish session close failed: 10.58.50.46 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:36.101714]	[connect]	Redfish authentication failed: 10.58.50.47 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:36.108459]	[disconnect]	Redfish session close failed: 10.58.50.47 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'


Log: error
-----------

[2022-12-13 17:02:34.679180]	[connect]	Redfish authentication failed: 10.58.50.43 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:34.687886]	[disconnect]	Redfish session close failed: 10.58.50.43 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:34.724884]	[connect]	Redfish authentication failed: 10.58.50.42 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:34.729997]	[connect]	Redfish authentication failed: 10.58.50.41 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:34.736818]	[disconnect]	Redfish session close failed: 10.58.50.42 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:34.741250]	[disconnect]	Redfish session close failed: 10.58.50.41 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:36.061767]	[connect]	Redfish authentication failed: 10.58.50.46 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:36.067083]	[disconnect]	Redfish session close failed: 10.58.50.46 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:36.101521]	[connect]	Redfish authentication failed: 10.58.50.47 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:36.108268]	[disconnect]	Redfish session close failed: 10.58.50.47 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'


Log: isctl
-----------

2022-12-13 17:02:31.720828	True	2223	93	isctl get compute rackunit   -o json --top 100
2022-12-13 17:02:32.544372	True	822	10	isctl get compute blade   -o json --top 100
2022-12-13 17:02:33.147222	True	561	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 17:02:33.224383	True	632	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T17:02:32.000Z"  -o json --top 100
2022-12-13 17:02:33.328570	True	749	8	isctl get asset deviceregistration --filter "Moid in ('5fdf9be76f72612d300a8d81', '5fdf9c676f72612d300a9c8d', '5fdf9cf26f72612d300aaca0', '5fdfa1686f72612d300b383f', '5fdfdc206f72612d30120ab4', '5fdfe4666f72612d30130510', '5fdfe7d86f72612d30136fed', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1')"  -o json --top 100


Log: redfish
-------------

2022-12-13 17:02:34.679791	False	1292	connect 10.58.50.43
2022-12-13 17:02:34.688327	False	5	disconnect 10.58.50.43
2022-12-13 17:02:34.725783	False	1340	connect 10.58.50.42
2022-12-13 17:02:34.730531	False	1348	connect 10.58.50.41
2022-12-13 17:02:34.737463	False	7	disconnect 10.58.50.42
2022-12-13 17:02:34.741773	False	5	disconnect 10.58.50.41
2022-12-13 17:02:34.768933	True	1371	connect 10.58.50.44
2022-12-13 17:02:34.775235	True	6	10.58.50.44:/redfish/v1/Systems
2022-12-13 17:02:34.781269	True	6	10.58.50.44:/redfish/v1/Chassis
2022-12-13 17:02:34.841295	True	60	10.58.50.44:/redfish/v1/Chassis/1
2022-12-13 17:02:35.308158	True	466	10.58.50.44:/redfish/v1/Chassis/1/Power
2022-12-13 17:02:35.433381	True	121	disconnect 10.58.50.44
2022-12-13 17:02:36.008254	True	1309	connect 10.58.50.45
2022-12-13 17:02:36.013553	True	5	10.58.50.45:/redfish/v1/Systems
2022-12-13 17:02:36.020566	True	6	10.58.50.45:/redfish/v1/Chassis
2022-12-13 17:02:36.062296	False	1312	connect 10.58.50.46
2022-12-13 17:02:36.067752	False	5	disconnect 10.58.50.46
2022-12-13 17:02:36.085344	True	64	10.58.50.45:/redfish/v1/Chassis/1
2022-12-13 17:02:36.101958	False	1348	connect 10.58.50.47
2022-12-13 17:02:36.108695	False	6	disconnect 10.58.50.47
2022-12-13 17:02:36.692951	True	604	10.58.50.45:/redfish/v1/Chassis/1/Power
2022-12-13 17:02:36.888038	True	189	disconnect 10.58.50.45


Log: ucsm
----------

2022-12-13 17:02:36.181808	True	736	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:36.378011	True	196	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:36.597340	True	219	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:36.765486	True	168	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:02:36.813091	True	731	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:36.950493	True	184	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:37.018503	True	205	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:37.156350	True	1033	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:37.207407	True	189	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:37.406047	True	250	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:37.409479	True	202	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:02:37.560233	True	149	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:37.589291	True	183	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:37.724208	True	825	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:37.744830	True	155	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:02:37.900406	True	154	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:37.952737	True	228	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:37.955757	True	988	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:38.176944	True	221	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:38.214894	True	262	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:38.406738	True	827	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:38.416543	True	201	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:02:38.433963	True	256	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:38.563883	True	145	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:38.610650	True	204	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:38.614186	True	180	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:02:38.634713	True	716	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:38.753483	True	138	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:38.778169	True	168	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:38.801155	True	167	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:38.942763	True	164	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:02:38.984453	True	183	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:39.097003	True	152	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:39.147521	True	163	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:02:39.297020	True	147	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:39.340201	True	752	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:39.509304	True	169	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:39.693433	True	184	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:02:39.852297	True	159	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:02:40.013992	True	160	disconnect vip-ucsb1.emea-sp.cisco.com
```
