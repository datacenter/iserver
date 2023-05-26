# FI-Attached Server Power Templates

```
# iserver get redfish endpoint
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Server
    --inventory-id FI4-1-1
    --template power

Power Consumption (Watt)
------------------------
- Current : 252
- Average : 255
- Max     : 287
- Min     : 13


+-------+----------+---------+---------------------+-------------------+
| Name  | State    | Health  | Volts               | Upper Threshold   |
+-------+----------+---------+---------------------+-------------------+
| P12V  | Enabled  | OK      | 12.095000267028809  | 12.6850004196167  | 
+-------+----------+---------+---------------------+-------------------+
```

```
# iserver get redfish endpoint
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Server
    --inventory-id FI4-1-1
    --template power
    --output json

{
    "PowerControl": {
        "PowerConsumedWatts": 248,
        "MaxPowerWatts": 1414,
        "MinPowerWatts": 381,
        "PowerProfileMaxWatts": 734,
        "PowerProfileMinWatts": 448,
        "AverageConsumedWatts": 255,
        "CurrentConsumedWatts": 252,
        "IntervalInMsec": 1000,
        "MaxConsumedWatts": 287,
        "MinConsumedWatts": 13
    },
    "Voltage": [
        {
            "Name": "P12V",
            "ReadingVolts": 12.095000267028809,
            "UpperThresholdCritical": 12.6850004196167,
            "PhysicalContext": "PowerSupply",
            "State": "Enabled",
            "Health": "OK"
        }
    ]
}
```
