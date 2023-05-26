# HPE Power Templates

```
# iserver get redfish endpoint
    --type hp
    --ip 10.58.24.211
    --port 49153
    --username administrator
    --password ******
    --template power

Power Consumption (Watt)
------------------------
- Current : 165
- Min     : 159
- Average : 167
- Max     : 270


+-----------------------+----------+---------+-----------------+-----------+----------------+------------+
| Name                  | State    | Health  | Serial          | Firmware  | Output (Watt)  | Input (V)  |
+-----------------------+----------+---------+-----------------+-----------+----------------+------------+
| HpeServerPowerSupply  | Enabled  | OK      | 5WBYE0D4DEF1FM  | 1.00      | 89             | 206        | 
| HpeServerPowerSupply  | Enabled  | OK      | 5WBYE0D4DEF1H5  | 1.00      | 76             | 205        | 
+-----------------------+----------+---------+-----------------+-----------+----------------+------------+
```

```
# iserver get redfish endpoint
    --type hp
    --ip 10.58.24.211
    --port 49153
    --username administrator
    --password ******
    --template power
    --output json

{
    "PowerControl": {
        "PowerConsumedWatts": 165,
        "AverageConsumedWatts": 167,
        "IntervalInMin": 20,
        "MaxConsumedWatts": 270,
        "MinConsumedWatts": 159
    },
    "PowerSupply": [
        {
            "Name": "HpeServerPowerSupply",
            "Model": "865438-B21",
            "SerialNumber": "5WBYE0D4DEF1FM",
            "SparePartNumber": "866793-001",
            "Manufacturer": "DELTA",
            "FirmwareVersion": "1.00",
            "State": "Enabled",
            "Health": "OK",
            "PowerSupplyType": "AC",
            "LastPowerOutputWatts": 89,
            "LineInputVoltage": 206
        },
        {
            "Name": "HpeServerPowerSupply",
            "Model": "865438-B21",
            "SerialNumber": "5WBYE0D4DEF1H5",
            "SparePartNumber": "866793-001",
            "Manufacturer": "DELTA",
            "FirmwareVersion": "1.00",
            "State": "Enabled",
            "Health": "OK",
            "PowerSupplyType": "AC",
            "LastPowerOutputWatts": 76,
            "LineInputVoltage": 205
        }
    ]
}
```