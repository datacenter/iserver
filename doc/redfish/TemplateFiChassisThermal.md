# UCS Chassis Thermal Templates

```
# iserver get redfish endpoint
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Chassis
    --inventory-id IoCard-1-1
    --template thermal

+-----------------------------+----------+------------------+
| Name                        | State    | Value (Celcius)  |
+-----------------------------+----------+------------------+
| ASIC_INLET_TEMP             | Enabled  | 30               | 
| ASIC_OUTLET_TEMP            | Enabled  | 45               | 
| ASIC_TEMP_A                 | Enabled  | 56               | 
| ASIC_TEMP_B                 | Enabled  | 56               | 
| FAN1_HOTSWAP_TEMP           | Absent   |                  | 
| FAN2_HOTSWAP_TEMP           | Absent   |                  | 
| FAN3_HOTSWAP_TEMP           | Absent   |                  | 
| FAN4_HOTSWAP_TEMP           | Absent   |                  | 
| FEM1_HOTSWAP_TEMP           | Absent   |                  | 
| FEM1_INLET_TEMP             | Absent   |                  | 
| FEM2_HOTSWAP_TEMP           | Absent   |                  | 
| FEM2_INLET_TEMP             | Absent   |                  | 
| IFM_HOTSWAP_TEMP            | Enabled  | 20               | 
| IFM_INLET_TEMP              | Enabled  | 21               | 
| IFM_OUTLET_TEMP             | Enabled  | 48               | 
| P1_TEMP                     | Enabled  | 29               | 
| PEER_SLOT_FEM_HOTSWAP_TEMP  | Absent   |                  | 
| PEER_SLOT_FEM_INLET_TEMP    | Absent   |                  | 
| PS1_TEMP1                   | Absent   |                  | 
| PS1_TEMP2                   | Absent   |                  | 
| PS1_TEMP3                   | Absent   |                  | 
| PS2_TEMP1                   | Absent   |                  | 
| PS2_TEMP2                   | Absent   |                  | 
| PS2_TEMP3                   | Absent   |                  | 
| PS3_TEMP1                   | Absent   |                  | 
| PS3_TEMP2                   | Absent   |                  | 
| PS3_TEMP3                   | Absent   |                  | 
| PS4_TEMP1                   | Absent   |                  | 
| PS4_TEMP2                   | Absent   |                  | 
| PS4_TEMP3                   | Absent   |                  | 
| PS5_TEMP1                   | Absent   |                  | 
| PS5_TEMP2                   | Absent   |                  | 
| PS5_TEMP3                   | Absent   |                  | 
| PS6_TEMP1                   | Absent   |                  | 
| PS6_TEMP2                   | Absent   |                  | 
| PS6_TEMP3                   | Absent   |                  | 
| PWR_BRICK_TEMP1             | Enabled  | 39               | 
| PWR_BRICK_TEMP2             | Enabled  | 40               | 
+-----------------------------+----------+------------------+

+---------------------+----------+----------------+---------------+
| Name                | State    | Model          | SerialNumber  |
+---------------------+----------+----------------+---------------+
| Fan Module 1 Fan 1  | Enabled  | UCSX-9508-FAN  | FCH2517709V   | 
| Fan Module 1 Fan 2  | Enabled  | UCSX-9508-FAN  | FCH2517709V   | 
| Fan Module 2 Fan 1  | Enabled  | UCSX-9508-FAN  | FCH2517701J   | 
| Fan Module 2 Fan 2  | Enabled  | UCSX-9508-FAN  | FCH2517701J   | 
| Fan Module 3 Fan 1  | Enabled  | UCSX-9508-FAN  | FCH2517704C   | 
| Fan Module 3 Fan 2  | Enabled  | UCSX-9508-FAN  | FCH2517704C   | 
| Fan Module 4 Fan 1  | Enabled  | UCSX-9508-FAN  | FCH2517701L   | 
| Fan Module 4 Fan 2  | Enabled  | UCSX-9508-FAN  | FCH2517701L   | 
+---------------------+----------+----------------+---------------+
```

```
# iserver get redfish endpoint
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Chassis
    --inventory-id IoCard-1-1
    --template thermal
    --output json

{
    "Temperature": [
        {
            "State": "Enabled",
            "Name": "ASIC_INLET_TEMP",
            "ReadingCelsius": 30
        },
        {
            "State": "Enabled",
            "Name": "ASIC_OUTLET_TEMP",
            "ReadingCelsius": 45
        },
        {
            "State": "Enabled",
            "Name": "ASIC_TEMP_A",
            "ReadingCelsius": 54
        },
        {
            "State": "Enabled",
            "Name": "ASIC_TEMP_B",
            "ReadingCelsius": 54
        },
        {
            "State": "Absent",
            "Name": "FAN1_HOTSWAP_TEMP",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "FAN2_HOTSWAP_TEMP",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "FAN3_HOTSWAP_TEMP",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "FAN4_HOTSWAP_TEMP",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "FEM1_HOTSWAP_TEMP",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "FEM1_INLET_TEMP",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "FEM2_HOTSWAP_TEMP",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "FEM2_INLET_TEMP",
            "ReadingCelsius": ""
        },
        {
            "State": "Enabled",
            "Name": "IFM_HOTSWAP_TEMP",
            "ReadingCelsius": 20
        },
        {
            "State": "Enabled",
            "Name": "IFM_INLET_TEMP",
            "ReadingCelsius": 21
        },
        {
            "State": "Enabled",
            "Name": "IFM_OUTLET_TEMP",
            "ReadingCelsius": 47
        },
        {
            "State": "Enabled",
            "Name": "P1_TEMP",
            "ReadingCelsius": 30
        },
        {
            "State": "Absent",
            "Name": "PEER_SLOT_FEM_HOTSWAP_TEMP",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PEER_SLOT_FEM_INLET_TEMP",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS1_TEMP1",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS1_TEMP2",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS1_TEMP3",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS2_TEMP1",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS2_TEMP2",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS2_TEMP3",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS3_TEMP1",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS3_TEMP2",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS3_TEMP3",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS4_TEMP1",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS4_TEMP2",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS4_TEMP3",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS5_TEMP1",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS5_TEMP2",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS5_TEMP3",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS6_TEMP1",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS6_TEMP2",
            "ReadingCelsius": ""
        },
        {
            "State": "Absent",
            "Name": "PS6_TEMP3",
            "ReadingCelsius": ""
        },
        {
            "State": "Enabled",
            "Name": "PWR_BRICK_TEMP1",
            "ReadingCelsius": 39
        },
        {
            "State": "Enabled",
            "Name": "PWR_BRICK_TEMP2",
            "ReadingCelsius": 40
        }
    ],
    "Fan": [
        {
            "Name": "Fan Module 1 Fan 1",
            "State": "Enabled",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517709V",
            "Model": "UCSX-9508-FAN",
            "Manufacturer": "Cisco Systems Inc"
        },
        {
            "Name": "Fan Module 1 Fan 2",
            "State": "Enabled",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517709V",
            "Model": "UCSX-9508-FAN",
            "Manufacturer": "Cisco Systems Inc"
        },
        {
            "Name": "Fan Module 2 Fan 1",
            "State": "Enabled",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517701J",
            "Model": "UCSX-9508-FAN",
            "Manufacturer": "Cisco Systems Inc"
        },
        {
            "Name": "Fan Module 2 Fan 2",
            "State": "Enabled",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517701J",
            "Model": "UCSX-9508-FAN",
            "Manufacturer": "Cisco Systems Inc"
        },
        {
            "Name": "Fan Module 3 Fan 1",
            "State": "Enabled",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517704C",
            "Model": "UCSX-9508-FAN",
            "Manufacturer": "Cisco Systems Inc"
        },
        {
            "Name": "Fan Module 3 Fan 2",
            "State": "Enabled",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517704C",
            "Model": "UCSX-9508-FAN",
            "Manufacturer": "Cisco Systems Inc"
        },
        {
            "Name": "Fan Module 4 Fan 1",
            "State": "Enabled",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517701L",
            "Model": "UCSX-9508-FAN",
            "Manufacturer": "Cisco Systems Inc"
        },
        {
            "Name": "Fan Module 4 Fan 2",
            "State": "Enabled",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517701L",
            "Model": "UCSX-9508-FAN",
            "Manufacturer": "Cisco Systems Inc"
        }
    ]
}
```
