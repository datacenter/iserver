# Get Intersight Servers with Power Information

```
# iserver get servers --group p2b -c power

+------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | Consumed [W] | Min [W] | Avg [W] | Max [W] |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+
| P+ H | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 324          | 177     | 334     | 490     | 
| P+ H | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 306          | 52      | 315     | 798     | 
| P+ H | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 |              |         |         |         | 
| P- H | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 0            | 0       | 0       | 0       | 
| P- H | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | 0            | 0       | 0       | 0       | 
| P- H | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | 0            | 0       | 0       | 0       | 
| P+ H | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 |              |         |         |         | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+
```

JSON Output

```
# iserver get servers --group p2b -c power

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
        "Power": {
            "Data": {
                "PowerControl": {
                    "PowerConsumedWatts": 324,
                    "LimitException": "NoAction",
                    "MinConsumedWatts": 177,
                    "AverageConsumedWatts": 334,
                    "MaxConsumedWatts": 490
                },
                "Voltage": [
                    {
                        "Name": "PSU1_VOUT",
                        "ReadingVolts": 12.1,
                        "UpperThresholdCritical": 14,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    },
                    {
                        "Name": "PSU2_VOUT",
                        "ReadingVolts": 12.2,
                        "UpperThresholdCritical": 14,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    },
                    {
                        "Name": "P12V",
                        "ReadingVolts": 11.89,
                        "UpperThresholdCritical": 13.166,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    },
                    {
                        "Name": "P3V_BAT_SCALED",
                        "ReadingVolts": 3.011,
                        "UpperThresholdCritical": 3.588,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    }
                ],
                "PowerSupply": [
                    {
                        "Name": "PSU1",
                        "Model": "PS-2112-9S-LF",
                        "SerialNumber": "LIT241244MU",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10062019",
                        "PowerOutputWatts": 144,
                        "LastPowerOutputWatts": 144,
                        "PowerInputWatts": 164,
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
                        "Model": "PS-2112-9S-LF",
                        "SerialNumber": "LIT241244Z5",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10062019",
                        "PowerOutputWatts": 144,
                        "LastPowerOutputWatts": 144,
                        "PowerInputWatts": 165,
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
                "PowerNow": 324,
                "PowerMin": 177,
                "PowerAvg": 334,
                "PowerMax": 490
            }
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
        "Power": {
            "Data": {
                "PowerControl": {
                    "PowerConsumedWatts": 306,
                    "LimitException": "NoAction",
                    "MinConsumedWatts": 52,
                    "AverageConsumedWatts": 315,
                    "MaxConsumedWatts": 798
                },
                "Voltage": [
                    {
                        "Name": "PSU1_VOUT",
                        "ReadingVolts": 12.2,
                        "UpperThresholdCritical": 14,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    },
                    {
                        "Name": "PSU2_VOUT",
                        "ReadingVolts": 12.2,
                        "UpperThresholdCritical": 14,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    },
                    {
                        "Name": "P12V",
                        "ReadingVolts": 11.89,
                        "UpperThresholdCritical": 13.166,
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
                        "Model": "PS-2112-9S-LF",
                        "SerialNumber": "LIT241244RQ",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10062019",
                        "PowerOutputWatts": 148,
                        "LastPowerOutputWatts": 148,
                        "PowerInputWatts": 162,
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
                        "Model": "PS-2112-9S-LF",
                        "SerialNumber": "LIT241242TS",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10062019",
                        "PowerOutputWatts": 136,
                        "LastPowerOutputWatts": 136,
                        "PowerInputWatts": 153,
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
                "PowerNow": 306,
                "PowerMin": 52,
                "PowerAvg": 315,
                "PowerMax": 798
            }
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
                        "SerialNumber": "APS240201EX",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10252041",
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
                        "SerialNumber": "ART2601F4SS",
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
    }
]
```