# Get Intersight Servers with Environmental Information

Environmental = Power + Thermal

```
# iserver get servers --group power -c env

+---------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+------+---------+-------------+-------------+----------------+
| SF      | MF  | WF | Name                           | Model              | Serial      | IP          | Consumed [W] | Min [W] | Avg [W] | Max [W] | Fans | Sensors | Highest (C) | Min Gap (C) | Over Threshold |
+---------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+------+---------+-------------+-------------+----------------+
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-1           | (B) UCSB-B200-M4   | FCH205371PZ | 10.58.52.33 | 144.0        | 138.0   | 142.5   | 144.0   | N/A  | True    | 38.0        | N/A         | N/A            | 
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-2           | (B) UCSB-B200-M4   | FCH20527XXD | 10.58.52.34 | 138.0        | 138.0   | 138.0   | 138.0   | N/A  | True    | 38.5        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-1-3           | (B) UCSB-B200-M4   | FCH20437VXH | 10.58.52.35 | 126.0        | 126.0   | 126.0   | 126.0   | N/A  | True    | 41.0        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-1-4           | (B) UCSB-B200-M4   | FCH205371UU | 10.58.52.36 | 132.0        | 126.0   | 126.75  | 132.0   | N/A  | True    | 42.0        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-1           | (B) UCSB-B200-M5   | FLM241501FB | 10.58.52.41 | 241.8        | 237.9   | 242.36  | 249.6   | N/A  | True    | 46.5        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-2           | (B) UCSB-B200-M5   | FLM24140BJB | 10.58.52.42 | 206.7        | 202.8   | 203.77  | 206.7   | N/A  | True    | 40.5        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-3           | (B) UCSB-B200-M5   | FLM241501CT | 10.58.52.43 | 198.9        | 195.0   | 196.2   | 198.9   | N/A  | True    | 37.5        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-4           | (B) UCSB-B200-M5   | FLM24140B0B | 10.58.52.44 | 241.8        | 230.1   | 235.56  | 241.8   | N/A  | True    | 48.5        | N/A         | N/A            | 
| P+ H    | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 |              |         |         |         |      |         |             |             |                | 
| P+ H    | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 |              |         |         |         |      |         |             |             |                | 
| P+ H    | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 |              |         |         |         |      |         |             |             |                | 
| P- H    | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 0            | 0       | 0       | 0       |      |         |             |             |                | 
| P- H    | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | 0            | 0       | 0       | 0       |      |         |             |             |                | 
| P- H    | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 |              |         |         |         |      |         |             |             |                | 
| P+ H    | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 |              |         |         |         |      |         |             |             |                | 
+---------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+------+---------+-------------+-------------+----------------+
```

JSON Output

```
# iserver get servers --group power -c env

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
        "Power": null,
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
        "Power": null,
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
        "Power": null,
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
        "Power": null,
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
        "Power": {
            "Data": {
                "dn": "sys/chassis-2/blade-2/board/power-stats",
                "time_collected": "2022-12-13T18:02:59.879",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-2",
                "consumed_power": 206.7,
                "input_current": 17.01,
                "input_voltage": 12.15,
                "consumed_power_avg": 203.77,
                "input_current_avg": 16.77,
                "input_voltage_avg": 12.15,
                "consumed_power_min": 202.8,
                "input_current_min": 16.69,
                "input_voltage_min": 12.15,
                "consumed_power_max": 206.7,
                "input_current_max": 17.01,
                "input_voltage_max": 12.15
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 206.7,
                "PowerMin": 202.8,
                "PowerAvg": 203.77,
                "PowerMax": 206.7
            }
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-2/blade-2/board/temp-stats",
                    "time_collected": "2022-12-13T18:02:59.879",
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
                    "time_collected": "2022-12-13T18:02:59.879",
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
                    "time_collected": "2022-12-13T18:02:59.879",
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
                    "time_collected": "2022-12-13T18:02:59.879",
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
                    "time_collected": "2022-12-13T18:02:59.879",
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
                    "time_collected": "2022-12-13T18:02:59.879",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-11",
                    "name": "MEM-11",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 28.8,
                    "temperature_min": 28.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:59.879",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 32.0,
                    "temperature_avg": 31.8,
                    "temperature_min": 31.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-15/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:59.879",
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
                    "time_collected": "2022-12-13T18:02:59.879",
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
                    "time_collected": "2022-12-13T18:02:59.879",
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
                    "time_collected": "2022-12-13T18:02:59.879",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-21",
                    "name": "MEM-21",
                    "type": "memory",
                    "temperature": 32.0,
                    "temperature_avg": 31.4,
                    "temperature_min": 31.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-23/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:59.879",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-23",
                    "name": "MEM-23",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 30.3,
                    "temperature_min": 30.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-3/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:59.879",
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
                    "time_collected": "2022-12-13T18:02:59.879",
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
                    "time_collected": "2022-12-13T18:02:59.879",
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
                    "time_collected": "2022-12-13T18:02:59.879",
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
        "Power": {
            "Data": {
                "dn": "sys/chassis-1/blade-1/board/power-stats",
                "time_collected": "2022-12-13T18:02:56.717",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "consumed_power": 144.0,
                "input_current": 11.96,
                "input_voltage": 12.04,
                "consumed_power_avg": 142.5,
                "input_current_avg": 11.84,
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
                "PowerNow": 144.0,
                "PowerMin": 138.0,
                "PowerAvg": 142.5,
                "PowerMax": 144.0
            }
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-1/board/temp-stats",
                    "time_collected": "2022-12-13T18:02:56.717",
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
                    "time_collected": "2022-12-13T18:02:56.717",
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
                    "time_collected": "2022-12-13T18:02:56.717",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 35.0,
                    "temperature_avg": 35.0,
                    "temperature_min": 35.0,
                    "temperature_max": 35.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/cpu-2/env-stats",
                    "time_collected": "2022-12-13T18:02:56.717",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 38.0,
                    "temperature_avg": 38.0,
                    "temperature_min": 38.0,
                    "temperature_max": 38.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:56.717",
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
                    "time_collected": "2022-12-13T18:02:56.718",
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
                    "time_collected": "2022-12-13T18:02:56.718",
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
                    "time_collected": "2022-12-13T18:02:56.718",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.5,
                    "temperature_min": 29.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-14/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:56.718",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-14",
                    "name": "MEM-14",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.21,
                    "temperature_min": 28.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-16/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:56.718",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-16",
                    "name": "MEM-16",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.43,
                    "temperature_min": 31.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-17/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:56.718",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-17",
                    "name": "MEM-17",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.93,
                    "temperature_min": 28.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:56.718",
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
                    "time_collected": "2022-12-13T18:02:56.717",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-2",
                    "name": "MEM-2",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 26.93,
                    "temperature_min": 26.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-20/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:56.718",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-20",
                    "name": "MEM-20",
                    "type": "memory",
                    "temperature": 26.0,
                    "temperature_avg": 26.93,
                    "temperature_min": 26.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:56.718",
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
                    "time_collected": "2022-12-13T18:02:56.718",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-23",
                    "name": "MEM-23",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.93,
                    "temperature_min": 30.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-4/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:56.717",
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
                    "time_collected": "2022-12-13T18:02:56.717",
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
                    "time_collected": "2022-12-13T18:02:56.717",
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
                    "time_collected": "2022-12-13T18:02:56.717",
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
                "HighestTemperature": 38.0,
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
        "Power": {
            "Data": {
                "dn": "sys/chassis-1/blade-2/board/power-stats",
                "time_collected": "2022-12-13T18:02:56.405",
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
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-2/board/temp-stats",
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 36.0,
                    "temperature_avg": 35.88,
                    "temperature_min": 35.5,
                    "temperature_max": 36.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/cpu-2/env-stats",
                    "time_collected": "2022-12-13T18:02:56.405",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 38.5,
                    "temperature_avg": 38.38,
                    "temperature_min": 38.0,
                    "temperature_max": 38.5
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 34.0,
                    "temperature_avg": 33.5,
                    "temperature_min": 33.0,
                    "temperature_max": 34.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-14/dimm-env-stats",
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
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
                    "time_collected": "2022-12-13T18:02:56.405",
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
        "Power": {
            "Data": {
                "dn": "sys/chassis-1/blade-4/board/power-stats",
                "time_collected": "2022-12-13T18:03:01.267",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "consumed_power": 132.0,
                "input_current": 11.02,
                "input_voltage": 11.98,
                "consumed_power_avg": 126.75,
                "input_current_avg": 10.58,
                "input_voltage_avg": 11.98,
                "consumed_power_min": 126.0,
                "input_current_min": 10.52,
                "input_voltage_min": 11.98,
                "consumed_power_max": 132.0,
                "input_current_max": 11.02,
                "input_voltage_max": 11.98
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 132.0,
                "PowerMin": 126.0,
                "PowerAvg": 126.75,
                "PowerMax": 132.0
            }
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-4/board/temp-stats",
                    "time_collected": "2022-12-13T18:03:01.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 25.0,
                    "fm_temp_sen_rear": 36.0,
                    "temperature_avg": 25.12,
                    "fm_temp_sen_rear_avg": 36.0,
                    "temperature_min": 25.0,
                    "fm_temp_sen_rear_min": 36.0,
                    "temperature_max": 26.0,
                    "fm_temp_sen_rear_max": 36.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/temp-stats",
                    "time_collected": "2022-12-13T18:03:01.267",
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
                    "time_collected": "2022-12-13T18:03:01.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 39.5,
                    "temperature_avg": 39.33,
                    "temperature_min": 39.0,
                    "temperature_max": 39.5
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/cpu-2/env-stats",
                    "time_collected": "2022-12-13T18:03:01.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 42.0,
                    "temperature_avg": 41.83,
                    "temperature_min": 41.5,
                    "temperature_max": 42.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-13T18:03:01.267",
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
                    "time_collected": "2022-12-13T18:03:01.267",
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
                    "time_collected": "2022-12-13T18:03:01.267",
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
                    "time_collected": "2022-12-13T18:03:01.267",
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
                    "time_collected": "2022-12-13T18:03:01.267",
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
                    "time_collected": "2022-12-13T18:03:01.267",
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
                    "time_collected": "2022-12-13T18:03:01.267",
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
                    "time_collected": "2022-12-13T18:03:01.267",
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
        "Power": {
            "Data": {
                "dn": "sys/chassis-2/blade-4/board/power-stats",
                "time_collected": "2022-12-13T18:02:51.812",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-4",
                "consumed_power": 241.8,
                "input_current": 19.99,
                "input_voltage": 12.1,
                "consumed_power_avg": 235.56,
                "input_current_avg": 19.48,
                "input_voltage_avg": 12.1,
                "consumed_power_min": 230.1,
                "input_current_min": 19.02,
                "input_voltage_min": 12.1,
                "consumed_power_max": 241.8,
                "input_current_max": 19.99,
                "input_voltage_max": 12.1
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 241.8,
                "PowerMin": 230.1,
                "PowerAvg": 235.56,
                "PowerMax": 241.8
            }
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
        "Power": {
            "Data": {
                "dn": "sys/chassis-2/blade-3/board/power-stats",
                "time_collected": "2022-12-13T18:02:54.846",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-3",
                "consumed_power": 198.9,
                "input_current": 16.36,
                "input_voltage": 12.15,
                "consumed_power_avg": 196.2,
                "input_current_avg": 16.18,
                "input_voltage_avg": 12.13,
                "consumed_power_min": 195.0,
                "input_current_min": 16.04,
                "input_voltage_min": 12.1,
                "consumed_power_max": 198.9,
                "input_current_max": 16.44,
                "input_voltage_max": 12.15
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 198.9,
                "PowerMin": 195.0,
                "PowerAvg": 196.2,
                "PowerMax": 198.9
            }
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
# iserver get servers --group power -c env

Developer output

{
    "duration": 17231,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 4792
    },
    "redfish": {
        "read": true,
        "success": 12,
        "failed": 18,
        "connect": 22,
        "disconnect": 0,
        "path": 8,
        "connect_time": 15979,
        "disconnect_time": 0,
        "path_time": 1232,
        "total_time": 17211
    },
    "ucsm": {
        "read": true,
        "success": 96,
        "failed": 0,
        "connect": 32,
        "disconnect": 0,
        "mo": 64,
        "connect_time": 16385,
        "disconnect_time": 0,
        "mo_time": 12279,
        "total_time": 28664
    },
    "ssh": {
        "read": false,
        "calls": 0,
        "total_time": 0
    },
    "error": {
        "read": true,
        "lines": 19
    },
    "info": {
        "read": true,
        "lines": 19
    },
    "debug": {
        "read": true,
        "lines": 82
    }
}

Log: info
----------

[2022-12-13 17:02:56.996093]	[connect]	Redfish authentication failed: 10.58.50.43 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:57.006687]	[connect]	Redfish authentication failed: 10.58.50.42 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:57.090861]	[connect]	Redfish authentication failed: 10.58.50.41 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.311474]	[connect]	Redfish authentication failed: 10.58.50.43 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.320661]	[disconnect]	Redfish session close failed: 10.58.50.43 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.326608]	[disconnect]	Redfish session close failed: 10.58.50.43 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.655092]	[connect]	Redfish authentication failed: 10.58.50.41 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.663784]	[disconnect]	Redfish session close failed: 10.58.50.41 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.669589]	[disconnect]	Redfish session close failed: 10.58.50.41 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.730874]	[connect]	Redfish authentication failed: 10.58.50.42 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.740160]	[disconnect]	Redfish session close failed: 10.58.50.42 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.745767]	[disconnect]	Redfish session close failed: 10.58.50.42 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:59.768333]	[connect]	Redfish authentication failed: 10.58.50.46 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:59.782501]	[disconnect]	Redfish session close failed: 10.58.50.46 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:03:00.129894]	[connect]	Redfish authentication failed: 10.58.50.47 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:03:00.137292]	[disconnect]	Redfish session close failed: 10.58.50.47 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:03:01.460906]	[connect]	Redfish authentication failed: 10.58.50.47 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:03:01.469825]	[disconnect]	Redfish session close failed: 10.58.50.47 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'


Log: error
-----------

[2022-12-13 17:02:56.995546]	[connect]	Redfish authentication failed: 10.58.50.43 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:57.006459]	[connect]	Redfish authentication failed: 10.58.50.42 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:57.090470]	[connect]	Redfish authentication failed: 10.58.50.41 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.311179]	[connect]	Redfish authentication failed: 10.58.50.43 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.320450]	[disconnect]	Redfish session close failed: 10.58.50.43 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.326389]	[disconnect]	Redfish session close failed: 10.58.50.43 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"Message.v1_0_6.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.654802]	[connect]	Redfish authentication failed: 10.58.50.41 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.663554]	[disconnect]	Redfish session close failed: 10.58.50.41 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.669391]	[disconnect]	Redfish session close failed: 10.58.50.41 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.730647]	[connect]	Redfish authentication failed: 10.58.50.42 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.739963]	[disconnect]	Redfish session close failed: 10.58.50.42 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:58.745570]	[disconnect]	Redfish session close failed: 10.58.50.42 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:59.768138]	[connect]	Redfish authentication failed: 10.58.50.46 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:02:59.782292]	[disconnect]	Redfish session close failed: 10.58.50.46 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:03:00.129674]	[connect]	Redfish authentication failed: 10.58.50.47 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:03:00.137127]	[disconnect]	Redfish session close failed: 10.58.50.47 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:03:01.460722]	[connect]	Redfish authentication failed: 10.58.50.47 400 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.SessionLimitExceeded",\n\t\t\t\t"Message":\t"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation.",\n\t\t\t\t"MessageArgs":\t[],\n\t\t\t\t"Severity":\t"Warning",\n\t\t\t\t"Resolution":\t"Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported)."\n\t\t\t}]\n\t}\n}'
[2022-12-13 17:03:01.469653]	[disconnect]	Redfish session close failed: 10.58.50.47 401 b'{\n\t"error":\t{\n\t\t"code":\t"Base.1.4.0.GeneralError",\n\t\t"message":\t"See ExtendedInfo for more information.",\n\t\t"@Message.ExtendedInfo":\t[{\n\t\t\t\t"@odata.type":\t"#Message.v1_1_1.Message",\n\t\t\t\t"MessageId":\t"Base.1.4.0.InsufficientPrivilege",\n\t\t\t\t"Message":\t"Missing Authentication Parameters",\n\t\t\t\t"MessageArgs":\t["Missing Authentication Parameters"],\n\t\t\t\t"Severity":\t"Critical",\n\t\t\t\t"Resolution":\t"Either abandon the operation or change the associated access rights and resubmit the request if the operation failed."\n\t\t\t}]\n\t}\n}'


Log: isctl
-----------

2022-12-13 17:02:53.957329	True	2230	93	isctl get compute rackunit   -o json --top 100
2022-12-13 17:02:54.814363	True	856	10	isctl get compute blade   -o json --top 100
2022-12-13 17:02:55.260551	True	383	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 17:02:55.439894	True	565	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T17:02:54.000Z"  -o json --top 100
2022-12-13 17:02:55.615228	True	758	8	isctl get asset deviceregistration --filter "Moid in ('5fdf9be76f72612d300a8d81', '5fdf9c676f72612d300a9c8d', '5fdf9cf26f72612d300aaca0', '5fdfa1686f72612d300b383f', '5fdfdc206f72612d30120ab4', '5fdfe4666f72612d30130510', '5fdfe7d86f72612d30136fed', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1')"  -o json --top 100


Log: redfish
-------------

2022-12-13 17:02:56.996630	False	1326	connect 10.58.50.43
2022-12-13 17:02:57.006985	False	1340	connect 10.58.50.42
2022-12-13 17:02:57.037280	True	1350	connect 10.58.50.44
2022-12-13 17:02:57.044864	True	7	10.58.50.44:/redfish/v1/Systems
2022-12-13 17:02:57.056766	True	11	10.58.50.44:/redfish/v1/Chassis
2022-12-13 17:02:57.091408	False	1431	connect 10.58.50.41
2022-12-13 17:02:57.105662	True	47	10.58.50.44:/redfish/v1/Chassis/1
2022-12-13 17:02:57.664181	True	557	10.58.50.44:/redfish/v1/Chassis/1/Power
2022-12-13 17:02:57.832544	True	163	disconnect 10.58.50.44
2022-12-13 17:02:58.311859	False	1314	connect 10.58.50.43
2022-12-13 17:02:58.321125	False	6	disconnect 10.58.50.43
2022-12-13 17:02:58.326925	False	4	disconnect 10.58.50.43
2022-12-13 17:02:58.655392	False	1562	connect 10.58.50.41
2022-12-13 17:02:58.664113	False	5	disconnect 10.58.50.41
2022-12-13 17:02:58.669878	False	4	disconnect 10.58.50.41
2022-12-13 17:02:58.731189	False	1723	connect 10.58.50.42
2022-12-13 17:02:58.740440	False	6	disconnect 10.58.50.42
2022-12-13 17:02:58.746082	False	5	disconnect 10.58.50.42
2022-12-13 17:02:59.152866	True	1309	connect 10.58.50.45
2022-12-13 17:02:59.158192	True	5	10.58.50.45:/redfish/v1/Systems
2022-12-13 17:02:59.165541	True	6	10.58.50.45:/redfish/v1/Chassis
2022-12-13 17:02:59.214113	True	48	10.58.50.45:/redfish/v1/Chassis/1
2022-12-13 17:02:59.767170	True	551	10.58.50.45:/redfish/v1/Chassis/1/Power
2022-12-13 17:02:59.768599	False	1429	connect 10.58.50.46
2022-12-13 17:02:59.782748	False	4	disconnect 10.58.50.46
2022-12-13 17:02:59.981308	True	210	disconnect 10.58.50.45
2022-12-13 17:03:00.130143	False	1448	connect 10.58.50.47
2022-12-13 17:03:00.137557	False	5	disconnect 10.58.50.47
2022-12-13 17:03:01.461149	False	1330	connect 10.58.50.47
2022-12-13 17:03:01.470081	False	5	disconnect 10.58.50.47


Log: ucsm
----------

2022-12-13 17:02:59.485630	True	728	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:02:59.684623	True	198	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:02:59.875607	True	189	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:00.042303	True	167	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:03:00.196563	True	153	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:00.575398	True	780	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:00.779999	True	204	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:00.904514	True	911	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:01.030839	True	250	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:01.089574	True	185	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:01.212137	True	181	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:03:01.239186	True	1041	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:01.269326	True	180	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:01.369940	True	156	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:01.420841	True	181	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:01.443359	True	174	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:03:01.599758	True	155	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:01.611757	True	190	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:01.773279	True	162	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:03:01.956472	True	183	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:03:02.084452	True	712	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:02.191080	True	235	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:03:02.247958	True	163	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:02.363539	True	164	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:02.437699	True	189	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:02.526784	True	1045	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:02.615553	True	178	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:03:02.724754	True	197	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:02.862504	True	1261	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:02.881306	True	266	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:03:02.921147	True	197	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:03.022546	True	160	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:03.083283	True	162	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:03:03.085041	True	704	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:03.099435	True	218	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:03:03.211871	True	189	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:03.239684	True	152	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:03.263400	True	155	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:03.326967	True	241	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:03.379024	True	167	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:03:03.522962	True	195	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:03.557753	True	178	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:03:03.740914	True	217	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:03:03.799089	True	242	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:03:03.903126	True	161	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:03.959667	True	152	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:04.002848	True	761	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:04.177998	True	174	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:04.318586	True	1034	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:04.349507	True	171	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:04.489304	True	171	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:04.513657	True	164	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:03:04.672300	True	766	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:04.682222	True	193	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:04.688217	True	175	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:03:04.836375	True	164	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:04.847233	True	165	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:03:04.902048	True	213	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:03:04.989925	True	141	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:05.032832	True	1054	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:05.066208	True	157	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:05.066636	True	230	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:05.202285	True	169	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:05.231676	True	165	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:03:05.384803	True	182	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:05.404151	True	173	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:03:05.550612	True	165	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:03:05.638943	True	234	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:03:05.702315	True	706	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:05.705554	True	153	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:05.806650	True	159	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:05.874008	True	171	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:06.064089	True	190	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:06.071014	True	987	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:06.226541	True	162	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:03:06.259698	True	188	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:06.400062	True	174	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:03:06.413980	True	704	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:06.542552	True	283	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:06.558412	True	144	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:06.615026	True	215	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:03:06.724243	True	166	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:06.728310	True	186	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:03:06.779973	True	157	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:06.879769	True	150	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:06.934914	True	210	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:03:07.109344	True	174	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:03:07.339332	True	230	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:03:07.503282	True	156	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:07.597320	True	715	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:03:07.755204	True	158	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:03:07.943686	True	188	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:03:08.253764	True	310	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-13 17:03:08.422839	True	168	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-13 17:03:08.639994	True	216	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-13 17:03:08.802972	True	155	disconnect vip-ucsb1.emea-sp.cisco.com
```
