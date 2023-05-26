# UCS Rack Standalone Power Templates

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --template power

Power Consumption (Watt)
------------------------
- Current      : 324
- Min          : 186
- Average      : 349
- Max          : 495
- Limit action : NoAction


+-----------------+----------+---------+---------+------------------+
| Name            | State    | Health  | Volts   | Upper Threshold  |
+-----------------+----------+---------+---------+------------------+
| PSU1_VOUT       | Enabled  | OK      | 12.2    | 14               | 
| PSU2_VOUT       | Enabled  | OK      | 12.2    | 14               | 
| P12V            | Enabled  | OK      | 11.832  | 13.166           | 
| P3V_BAT_SCALED  | Enabled  | OK      | 3.026   | 3.588            | 
+-----------------+----------+---------+---------+------------------+

+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
| Name  | State    | Health  | Serial       | Firmware  | Output (Watt)  | Input (Watt)  | Max (V)  | Min (V)  | Max (Hz)  | Min (Hz)  |
+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
| PSU1  | Enabled  | OK      | LIT241244RQ  | 10062019  | 153            | 170           | 264      | 90       | 63        | 47        | 
| PSU2  | Enabled  | OK      | LIT241242TS  | 10062019  | 149            | 168           | 264      | 90       | 63        | 47        | 
+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
```

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --template power
    --output json

{
    "PowerControl": {
        "PowerConsumedWatts": 324,
        "LimitException": "NoAction",
        "MinConsumedWatts": 186,
        "AverageConsumedWatts": 349,
        "MaxConsumedWatts": 495
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
            "ReadingVolts": 11.832,
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
            "State": "Enabled",
            "Health": "OK",
            "PowerSupplyType": "AC",
            "PowerOutputWatts": 155,
            "LastPowerOutputWatts": 155,
            "PowerInputWatts": 168,
            "OutputWattage": 1050,
            "MaximumFrequencyHz": 63,
            "MaximumVoltage": 264,
            "MinimumVoltage": 90,
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
            "State": "Enabled",
            "Health": "OK",
            "PowerSupplyType": "AC",
            "PowerOutputWatts": 150,
            "LastPowerOutputWatts": 150,
            "PowerInputWatts": 168,
            "OutputWattage": 1050,
            "MaximumFrequencyHz": 63,
            "MaximumVoltage": 264,
            "MinimumVoltage": 90,
            "MinimumFrequencyHz": 47
        }
    ]
}
```
