# UCS Rack Standalone Thermal Templates

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --template thermal

Summary
-------
- State  : Enabled
- Health : OK


+-------------------+----------+---------+-------------------+------------------+----------------------------+
| Name              | State    | Health  | Location          | Value (Celcius)  | Upper Threshold (Celcius)  |
+-------------------+----------+---------+-------------------+------------------+----------------------------+
| DDR4_P1_A1_TMP    | Enabled  | OK      | Memory            | 30               | 85                         | 
| DDR4_P1_B1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| DDR4_P1_C1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| DDR4_P1_D1_TMP    | Enabled  | OK      | Memory            | 30               | 85                         | 
| DDR4_P1_E1_TMP    | Enabled  | OK      | Memory            | 30               | 85                         | 
| DDR4_P1_F1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| DDR4_P2_G1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| DDR4_P2_H1_TMP    | Enabled  | OK      | Memory            | 28               | 85                         | 
| DDR4_P2_J1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| DDR4_P2_K1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| DDR4_P2_L1_TMP    | Enabled  | OK      | Memory            | 28               | 85                         | 
| DDR4_P2_M1_TMP    | Enabled  | OK      | Memory            | 29               | 85                         | 
| MLOM_TEMP         | Enabled  | OK      | NetworkingDevice  | 55               | 90                         | 
| P1_TEMP_SENS      | Enabled  | OK      | CPU               | 40               | 100                        | 
| P2_TEMP_SENS      | Enabled  | OK      | CPU               | 44               | 100                        | 
| PCH_TEMP_SENS     | Enabled  | OK      | SystemBoard       | 36               | 85                         | 
| PCIE_SWITCH_TMP   | Enabled  | OK      | SystemBoard       | 41               | 100                        | 
| PSU1_TEMP         | Enabled  | OK      | PowerSupply       | 24               | 65                         | 
| PSU2_TEMP         | Enabled  | OK      | PowerSupply       | 22               | 65                         | 
| RISER1_INLET_TMP  | Enabled  | OK      | SystemBoard       | 33               | 70                         | 
| RISER1_TEMP       | Enabled  | OK      | SystemBoard       | 24               | 70                         | 
| RISER2_INLET_TMP  | Enabled  | OK      | SystemBoard       | 34               | 70                         | 
| RISER2_TEMP       | Enabled  | OK      | SystemBoard       | 29               | 70                         | 
| TEMP_SENS_FRONT   | Enabled  | OK      | SystemBoard       | 26               | 45                         | 
+-------------------+----------+---------+-------------------+------------------+----------------------------+

+------------------+----------+---------+-----------+
| Name             | State    | Health  | Value     |
+------------------+----------+---------+-----------+
| MOD1_FAN1_SPEED  | Enabled  | OK      | 6868 RPM  | 
| MOD1_FAN2_SPEED  | Enabled  | OK      | 7056 RPM  | 
| MOD2_FAN1_SPEED  | Enabled  | OK      | 7070 RPM  | 
| MOD2_FAN2_SPEED  | Enabled  | OK      | 7056 RPM  | 
| MOD3_FAN1_SPEED  | Enabled  | OK      | 6868 RPM  | 
| MOD3_FAN2_SPEED  | Enabled  | OK      | 7056 RPM  | 
| MOD4_FAN1_SPEED  | Enabled  | OK      | 7070 RPM  | 
| MOD4_FAN2_SPEED  | Enabled  | OK      | 7350 RPM  | 
| MOD5_FAN1_SPEED  | Enabled  | OK      | 7070 RPM  | 
| MOD5_FAN2_SPEED  | Enabled  | OK      | 7056 RPM  | 
| MOD6_FAN1_SPEED  | Enabled  | OK      | 6868 RPM  | 
| MOD6_FAN2_SPEED  | Enabled  | OK      | 7056 RPM  | 
| MOD7_FAN1_SPEED  | Absent   |         |           | 
+------------------+----------+---------+-----------+
```

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --template thermal
    --output json

{
    "State": "Enabled",
    "Health": "OK",
    "Temperature": [
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 114,
            "Name": "DDR4_P1_A1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 30,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 120,
            "Name": "DDR4_P1_B1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 29,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 126,
            "Name": "DDR4_P1_C1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 29,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 132,
            "Name": "DDR4_P1_D1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 30,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 138,
            "Name": "DDR4_P1_E1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 30,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 144,
            "Name": "DDR4_P1_F1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 29,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 150,
            "Name": "DDR4_P2_G1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 29,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 156,
            "Name": "DDR4_P2_H1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 28,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 162,
            "Name": "DDR4_P2_J1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 29,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 168,
            "Name": "DDR4_P2_K1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 30,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 174,
            "Name": "DDR4_P2_L1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 28,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 180,
            "Name": "DDR4_P2_M1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 29,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 60,
            "Name": "MLOM_TEMP",
            "PhysicalContext": "NetworkingDevice",
            "ReadingCelsius": 54,
            "UpperThresholdCritical": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 196,
            "Name": "P1_TEMP_SENS",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 40,
            "UpperThresholdCritical": 100
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 197,
            "Name": "P2_TEMP_SENS",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 44,
            "UpperThresholdCritical": 100
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 209,
            "Name": "PCH_TEMP_SENS",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 36,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 239,
            "Name": "PCIE_SWITCH_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 41,
            "UpperThresholdCritical": 100
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 207,
            "Name": "PSU1_TEMP",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 24,
            "UpperThresholdCritical": 65
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 208,
            "Name": "PSU2_TEMP",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 22,
            "UpperThresholdCritical": 65
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 250,
            "Name": "RISER1_INLET_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 33,
            "UpperThresholdCritical": 70
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 245,
            "Name": "RISER1_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 24,
            "UpperThresholdCritical": 70
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 249,
            "Name": "RISER2_INLET_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 34,
            "UpperThresholdCritical": 70
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 246,
            "Name": "RISER2_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 29,
            "UpperThresholdCritical": 70
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 84,
            "Name": "TEMP_SENS_FRONT",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 26,
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
            "Reading": 7070,
            "Value": "7070 RPM"
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
            "Reading": 6868,
            "Value": "6868 RPM"
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
}
```
