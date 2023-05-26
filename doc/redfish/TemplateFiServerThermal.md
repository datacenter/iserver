# FI-Attached Server Thermal Templates

```
# iserver get redfish endpoint
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Server
    --inventory-id FI4-1-1
    --template thermal

Summary
-------
- State  : Enabled
- Health : OK


+---------------------+----------+---------+--------------+------------------+----------------------------+
| Name                | State    | Health  | Location     | Value (Celcius)  | Upper Threshold (Celcius)  |
+---------------------+----------+---------+--------------+------------------+----------------------------+
| DDR4_P1_A1_TMP      | Enabled  | OK      | SystemBoard  | 23               | 85                         | 
| DDR4_P1_A2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_B1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_B2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_C1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_C2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_D1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_D2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_E1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_E2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_F1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_F2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_G1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_G2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_H1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P1_H2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_A1_TMP      | Enabled  | OK      | SystemBoard  | 23               | 85                         | 
| DDR4_P2_A2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_B1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_B2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_C1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_C2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_D1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_D2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_E1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_E2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_F1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_F2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_G1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_G2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_H1_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| DDR4_P2_H2_TMP      | Enabled  | OK      | SystemBoard  | 0                | 85                         | 
| NOEVALLEY_PD0_TEMP  | Enabled  | OK      | SystemBoard  | 31               |                            | 
| NOEVALLEY_PD1_TEMP  | Enabled  | OK      | SystemBoard  | 29               |                            | 
| P1_TEMP_SENS        | Enabled  | OK      | CPU          | 33.5             | 101                        | 
| P2_TEMP_SENS        | Enabled  | OK      | CPU          | 36.5             | 101                        | 
| PWR_BRICK_TEMP      | Enabled  | OK      | SystemBoard  | 43               |                            | 
| TEMP_FRONT          | Enabled  | OK      | SystemBoard  | 15               | 45                         | 
| TEMP_REAR_BOT       | Enabled  | OK      | SystemBoard  | 22               |                            | 
| TEMP_REAR_MID       | Enabled  | OK      | SystemBoard  | 29               |                            | 
| TEMP_REAR_TOP       | Enabled  | OK      | SystemBoard  | 22               |                            | 
+---------------------+----------+---------+--------------+------------------+----------------------------+
```

```
# iserver get redfish endpoint
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Server
    --inventory-id FI4-1-1
    --template thermal
    --output json

{
    "State": "Enabled",
    "Health": "OK",
    "Temperature": [
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_A1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 24,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_A2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_B1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_B2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_C1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_C2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_D1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_D2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_E1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_E2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_F1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_F2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_G1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_G2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_H1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P1_H2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_A1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 23,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_A2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_B1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_B2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_C1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_C2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_D1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_D2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_E1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_E2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_F1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_F2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_G1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_G2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_H1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "DDR4_P2_H2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "NOEVALLEY_PD0_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 31,
            "UpperThresholdCritical": "",
            "UpperThresholdFatal": ""
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "NOEVALLEY_PD1_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 29,
            "UpperThresholdCritical": "",
            "UpperThresholdFatal": ""
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "P1_TEMP_SENS",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 32.5,
            "UpperThresholdCritical": 101,
            "UpperThresholdFatal": 102
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "P2_TEMP_SENS",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 35.5,
            "UpperThresholdCritical": 101,
            "UpperThresholdFatal": 102
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "PWR_BRICK_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 43,
            "UpperThresholdCritical": "",
            "UpperThresholdFatal": ""
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "TEMP_FRONT",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 15,
            "UpperThresholdCritical": 45,
            "UpperThresholdFatal": 50
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "TEMP_REAR_BOT",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 22,
            "UpperThresholdCritical": "",
            "UpperThresholdFatal": ""
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "TEMP_REAR_MID",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 28,
            "UpperThresholdCritical": "",
            "UpperThresholdFatal": ""
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "Name": "TEMP_REAR_TOP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 22,
            "UpperThresholdCritical": "",
            "UpperThresholdFatal": ""
        }
    ]
}
```
