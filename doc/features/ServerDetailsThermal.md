# Server Details - Thermal Information

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --thermal

+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF (7d) | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | C2      | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+

Thermal Summary
---------------
- Sensors Health   : True
- Highest (C)      : 54
- Smallest Gap (C) : 20
- Over Threshold   : 0
- Fans Health      : True


+------------------+---------+--------+------------------+-----------------+---------------------------+
| Sensor Name      | State   | Health | Location         | Value (Celcius) | Upper Threshold (Celcius) |
+------------------+---------+--------+------------------+-----------------+---------------------------+
| DDR4_P1_A1_TMP   | Enabled | OK     | Memory           | 29              | 85                        | 
| DDR4_P1_B1_TMP   | Enabled | OK     | Memory           | 28              | 85                        | 
| DDR4_P1_C1_TMP   | Enabled | OK     | Memory           | 28              | 85                        | 
| DDR4_P1_D1_TMP   | Enabled | OK     | Memory           | 29              | 85                        | 
| DDR4_P1_E1_TMP   | Enabled | OK     | Memory           | 29              | 85                        | 
| DDR4_P1_F1_TMP   | Enabled | OK     | Memory           | 28              | 85                        | 
| DDR4_P2_G1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| DDR4_P2_H1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| DDR4_P2_J1_TMP   | Enabled | OK     | Memory           | 28              | 85                        | 
| DDR4_P2_K1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| DDR4_P2_L1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| DDR4_P2_M1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| MLOM_TEMP        | Enabled | OK     | NetworkingDevice | 54              | 90                        | 
| P1_TEMP_SENS     | Enabled | OK     | CPU              | 39.5            | 100                       | 
| P2_TEMP_SENS     | Enabled | OK     | CPU              | 39.5            | 100                       | 
| PCH_TEMP_SENS    | Enabled | OK     | SystemBoard      | 33              | 85                        | 
| PCIE_SWITCH_TMP  | Enabled | OK     | SystemBoard      | 39              | 100                       | 
| PSU1_TEMP        | Enabled | OK     | PowerSupply      | 21              | 65                        | 
| PSU2_TEMP        | Enabled | OK     | PowerSupply      | 19              | 65                        | 
| RISER1_INLET_TMP | Enabled | OK     | SystemBoard      | 32              | 70                        | 
| RISER1_TEMP      | Enabled | OK     | SystemBoard      | 24              | 70                        | 
| RISER2_INLET_TMP | Enabled | OK     | SystemBoard      | 31              | 70                        | 
| RISER2_TEMP      | Enabled | OK     | SystemBoard      | 27              | 70                        | 
| TEMP_SENS_FRONT  | Enabled | OK     | SystemBoard      | 25              | 45                        | 
+------------------+---------+--------+------------------+-----------------+---------------------------+

+-----------------+---------+--------+----------+
| Fan Name        | State   | Health | Value    |
+-----------------+---------+--------+----------+
| MOD1_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD1_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD2_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD2_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD3_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD3_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD4_FAN1_SPEED | Enabled | OK     | 7070 RPM | 
| MOD4_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD5_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD5_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD6_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD6_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD7_FAN1_SPEED | Absent  |        |          | 
+-----------------+---------+--------+----------+
```

JSON Output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --thermal

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
    "Connected": true,
    "Thermal": {
        "Data": {
            "Temperature": [
                {
                    "Name": "DDR4_P1_A1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 114,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 29,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_B1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 120,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 28,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_C1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 126,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 28,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_D1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 132,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 29,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_E1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 138,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 29,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_F1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 144,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 28,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_G1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 150,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_H1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 156,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_J1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 162,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 28,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_K1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 168,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_L1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 174,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_M1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 180,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "MLOM_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 60,
                    "PhysicalContext": "NetworkingDevice",
                    "ReadingCelsius": 54,
                    "UpperThresholdCritical": 90
                },
                {
                    "Name": "P1_TEMP_SENS",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 196,
                    "PhysicalContext": "CPU",
                    "ReadingCelsius": 39.5,
                    "UpperThresholdCritical": 100
                },
                {
                    "Name": "P2_TEMP_SENS",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 197,
                    "PhysicalContext": "CPU",
                    "ReadingCelsius": 39.5,
                    "UpperThresholdCritical": 100
                },
                {
                    "Name": "PCH_TEMP_SENS",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 209,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 33,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "PCIE_SWITCH_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 239,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 39,
                    "UpperThresholdCritical": 100
                },
                {
                    "Name": "PSU1_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 207,
                    "PhysicalContext": "PowerSupply",
                    "ReadingCelsius": 21,
                    "UpperThresholdCritical": 65
                },
                {
                    "Name": "PSU2_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 208,
                    "PhysicalContext": "PowerSupply",
                    "ReadingCelsius": 19,
                    "UpperThresholdCritical": 65
                },
                {
                    "Name": "RISER1_INLET_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 250,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 32,
                    "UpperThresholdCritical": 70
                },
                {
                    "Name": "RISER1_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 245,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 24,
                    "UpperThresholdCritical": 70
                },
                {
                    "Name": "RISER2_INLET_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 249,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 31,
                    "UpperThresholdCritical": 70
                },
                {
                    "Name": "RISER2_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 246,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 70
                },
                {
                    "Name": "TEMP_SENS_FRONT",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 84,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 25,
                    "UpperThresholdCritical": 45
                }
            ],
            "Fan": [
                {
                    "Name": "MOD1_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD1_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7056,
                    "Value": "7056 RPM"
                },
                {
                    "Name": "MOD2_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD2_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7056,
                    "Value": "7056 RPM"
                },
                {
                    "Name": "MOD3_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD3_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7056,
                    "Value": "7056 RPM"
                },
                {
                    "Name": "MOD4_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7070,
                    "Value": "7070 RPM"
                },
                {
                    "Name": "MOD4_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7056,
                    "Value": "7056 RPM"
                },
                {
                    "Name": "MOD5_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD5_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7056,
                    "Value": "7056 RPM"
                },
                {
                    "Name": "MOD6_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD6_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7056,
                    "Value": "7056 RPM"
                },
                {
                    "Name": "MOD7_FAN1_SPEED",
                    "State": "Absent",
                    "Health": "",
                    "PhysicalContext": "",
                    "ReadingUnits": "",
                    "Reading": "",
                    "Value": " "
                }
            ]
        },
        "Summary": {
            "FanHealth": true,
            "SensorHealth": true,
            "HighestTemperature": 54,
            "SmallestGap": 20,
            "OverThreshold": 0
        }
    },
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
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --thermal

Developer output

{
    "duration": 16741,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 9446
    },
    "redfish": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "path": 4,
        "connect_time": 2383,
        "disconnect_time": 0,
        "path_time": 1473,
        "total_time": 3856
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

2023-01-05 20:22:24.938039	True	3109	93	isctl get compute rackunit   -o json --top 100
2023-01-05 20:22:26.849823	True	1898	10	isctl get compute blade   -o json --top 100
2023-01-05 20:22:31.170942	True	1445	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2023-01-05 20:22:32.573764	True	1401	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2023-01-05 20:22:37.588351	True	1593	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T20:22:35.000Z"  -o json --top 100


Log: redfish
-------------

2023-01-05 20:22:34.489071	True	1891	connect 10.58.50.41
2023-01-05 20:22:34.551209	True	60	10.58.50.41:/redfish/v1/Systems
2023-01-05 20:22:34.626008	True	69	10.58.50.41:/redfish/v1/Chassis
2023-01-05 20:22:34.812876	True	182	10.58.50.41:/redfish/v1/Chassis/1
2023-01-05 20:22:35.983154	True	1162	10.58.50.41:/redfish/v1/Chassis/1/Thermal
2023-01-05 20:22:38.179704	True	492	disconnect 10.58.50.41
```

