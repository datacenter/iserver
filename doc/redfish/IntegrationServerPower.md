# Get Intersight Server with Power Information

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --power

+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF (7d) | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | C2      | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+

Power Consumption (Watt)
------------------------
- Current      : 324
- Min          : 177
- Average      : 335
- Max          : 490
- Limit action : NoAction


+----------------+---------+--------+--------+-----------------+
| Sensor Name    | State   | Health | Volts  | Upper Threshold |
+----------------+---------+--------+--------+-----------------+
| PSU1_VOUT      | Enabled | OK     | 12     | 14              | 
| PSU2_VOUT      | Enabled | OK     | 12.1   | 14              | 
| P12V           | Enabled | OK     | 11.832 | 13.166          | 
| P3V_BAT_SCALED | Enabled | OK     | 3.011  | 3.588           | 
+----------------+---------+--------+--------+-----------------+

+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
| PSU Name | State   | Health | Serial      | Firmware | Output (Watt) | Input (Watt) | Max (V) | Min (V) | Max (Hz) | Min (Hz) |
+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
| PSU1     | Enabled | OK     | LIT241244MU | 10062019 | 144           | 166          | 264     | 180     | 63       | 47       | 
| PSU2     | Enabled | OK     | LIT241244Z5 | 10062019 | 147           | 165          | 264     | 180     | 63       | 47       | 
+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
```

JSON Output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --power

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
    "Power": {
        "Data": {
            "PowerControl": {
                "PowerConsumedWatts": 324,
                "LimitException": "NoAction",
                "MinConsumedWatts": 177,
                "AverageConsumedWatts": 335,
                "MaxConsumedWatts": 490
            },
            "Voltage": [
                {
                    "Name": "PSU1_VOUT",
                    "ReadingVolts": 12,
                    "UpperThresholdCritical": 14,
                    "PhysicalContext": "PowerSupply",
                    "State": "Enabled",
                    "Health": "OK"
                },
                {
                    "Name": "PSU2_VOUT",
                    "ReadingVolts": 12.1,
                    "UpperThresholdCritical": 14,
                    "PhysicalContext": "PowerSupply",
                    "State": "Enabled",
                    "Health": "OK"
                },
                {
                    "Name": "P12V",
                    "ReadingVolts": 11.832,
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
                    "PowerInputWatts": 166,
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
                    "PowerOutputWatts": 147,
                    "LastPowerOutputWatts": 147,
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
            "PowerAvg": 335,
            "PowerMax": 490
        }
    },
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