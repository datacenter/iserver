# UCS Chassis Power Templates

```
# iserver get redfish endpoint
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Chassis
    --inventory-id IoCard-1-1
    --template power

Power Control
-------------
- CurrentConsumedWatts : 769


+---------+----------+---------+-----------------------+-----------------------+-------------------+-------------------+----------------+----------------+
| Name    | State    | Health  | AverageConsumedWatts  | CurrentConsumedWatts  | MaxConsumedWatts  | MinConsumedWatts  | MaxPowerWatts  | MinPowerWatts  |
+---------+----------+---------+-----------------------+-----------------------+-------------------+-------------------+----------------+----------------+
| Blade1  | Enabled  | OK      | 255                   | 234                   | 287               | 13                | 1414           | 381            | 
| Blade2  | Absent   | OK      | 0                     | 0                     | 0                 | 0                 | 0              | 0              | 
| Blade3  | Enabled  | OK      | 140                   | 140                   | 169               | 13                | 1414           | 381            | 
| Blade4  | Absent   | OK      | 0                     | 0                     | 0                 | 0                 | 0              | 0              | 
| Blade5  | Enabled  | OK      | 258                   | 259                   | 284               | 12                | 1414           | 381            | 
| Blade6  | Absent   | OK      | 0                     | 0                     | 0                 | 0                 | 0              | 0              | 
| Blade7  | Enabled  | OK      | 140                   | 136                   | 171               | 13                | 1414           | 381            | 
| Blade8  | Absent   | OK      | 0                     | 0                     | 0                 | 0                 | 0              | 0              | 
+---------+----------+---------+-----------------------+-----------------------+-------------------+-------------------+----------------+----------------+

+-----------------+----------+--------------------+------------------+---------------+
| Name            | State    | Manufacturer       | Model            | SerialNumber  |
+-----------------+----------+--------------------+------------------+---------------+
| Power Supply 1  | Enabled  | Cisco Systems Inc  | UCSX-PSU-2800AC  | ART2510F5AT   | 
| Power Supply 2  | Absent   |                    |                  |               | 
| Power Supply 3  | Absent   |                    |                  |               | 
| Power Supply 4  | Enabled  | Cisco Systems Inc  | UCSX-PSU-2800AC  | ART2510F5AD   | 
| Power Supply 5  | Absent   |                    |                  |               | 
| Power Supply 6  | Absent   |                    |                  |               | 
+-----------------+----------+--------------------+------------------+---------------+
```

```
# iserver get redfish endpoint
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Chassis
    --inventory-id IoCard-1-1
    --template power
    --output json

{
    "PowerControl": {
        "CurrentConsumedWatts": 768,
        "PowerExtendedEnabled": false,
        "PowerGridMaxWatts": 3044,
        "PowerN+1MaxWatts": 3044,
        "PowerN+2MaxWatts": 3044,
        "PowerNotRedundantMaxWatts": 6087,
        "PowerProfileMaxWatts": 8027,
        "PowerProfileMinWatts": 4060,
        "PowerRebalanceEnabled": true,
        "PowerSaveEnabled": false
    },
    "Blade": [
        {
            "MemberId": "Blade1",
            "State": "Enabled",
            "Health": "OK",
            "PowerLimitInWatts": 862,
            "AverageConsumedWatts": 255,
            "CurrentConsumedWatts": 234,
            "IntervalInMsec": 1000,
            "MaxConsumedWatts": 287,
            "MinConsumedWatts": 13,
            "MaxPowerWatts": 1414,
            "MinPowerWatts": 381,
            "PowerProfileMaxWatts": 734,
            "PowerProfileMinWatts": 448
        },
        {
            "MemberId": "Blade2",
            "State": "Absent",
            "Health": "OK",
            "PowerLimitInWatts": 0,
            "AverageConsumedWatts": 0,
            "CurrentConsumedWatts": 0,
            "IntervalInMsec": 1000,
            "MaxConsumedWatts": 0,
            "MinConsumedWatts": 0,
            "MaxPowerWatts": 0,
            "MinPowerWatts": 0,
            "PowerProfileMaxWatts": 0,
            "PowerProfileMinWatts": 0
        },
        {
            "MemberId": "Blade3",
            "State": "Enabled",
            "Health": "OK",
            "PowerLimitInWatts": 867,
            "AverageConsumedWatts": 140,
            "CurrentConsumedWatts": 139,
            "IntervalInMsec": 1000,
            "MaxConsumedWatts": 169,
            "MinConsumedWatts": 13,
            "MaxPowerWatts": 1414,
            "MinPowerWatts": 381,
            "PowerProfileMaxWatts": 742,
            "PowerProfileMinWatts": 456
        },
        {
            "MemberId": "Blade4",
            "State": "Absent",
            "Health": "OK",
            "PowerLimitInWatts": 0,
            "AverageConsumedWatts": 0,
            "CurrentConsumedWatts": 0,
            "IntervalInMsec": 1000,
            "MaxConsumedWatts": 0,
            "MinConsumedWatts": 0,
            "MaxPowerWatts": 0,
            "MinPowerWatts": 0,
            "PowerProfileMaxWatts": 0,
            "PowerProfileMinWatts": 0
        },
        {
            "MemberId": "Blade5",
            "State": "Enabled",
            "Health": "OK",
            "PowerLimitInWatts": 821,
            "AverageConsumedWatts": 258,
            "CurrentConsumedWatts": 259,
            "IntervalInMsec": 1000,
            "MaxConsumedWatts": 284,
            "MinConsumedWatts": 12,
            "MaxPowerWatts": 1414,
            "MinPowerWatts": 381,
            "PowerProfileMaxWatts": 670,
            "PowerProfileMinWatts": 348
        },
        {
            "MemberId": "Blade6",
            "State": "Absent",
            "Health": "OK",
            "PowerLimitInWatts": 0,
            "AverageConsumedWatts": 0,
            "CurrentConsumedWatts": 0,
            "IntervalInMsec": 1000,
            "MaxConsumedWatts": 0,
            "MinConsumedWatts": 0,
            "MaxPowerWatts": 0,
            "MinPowerWatts": 0,
            "PowerProfileMaxWatts": 0,
            "PowerProfileMinWatts": 0
        },
        {
            "MemberId": "Blade7",
            "State": "Enabled",
            "Health": "OK",
            "PowerLimitInWatts": 866,
            "AverageConsumedWatts": 140,
            "CurrentConsumedWatts": 136,
            "IntervalInMsec": 1000,
            "MaxConsumedWatts": 171,
            "MinConsumedWatts": 13,
            "MaxPowerWatts": 1414,
            "MinPowerWatts": 381,
            "PowerProfileMaxWatts": 740,
            "PowerProfileMinWatts": 435
        },
        {
            "MemberId": "Blade8",
            "State": "Absent",
            "Health": "OK",
            "PowerLimitInWatts": 0,
            "AverageConsumedWatts": 0,
            "CurrentConsumedWatts": 0,
            "IntervalInMsec": 1000,
            "MaxConsumedWatts": 0,
            "MinConsumedWatts": 0,
            "MaxPowerWatts": 0,
            "MinPowerWatts": 0,
            "PowerProfileMaxWatts": 0,
            "PowerProfileMinWatts": 0
        }
    ],
    "PowerSupply": [
        {
            "MemberId": "1",
            "Name": "Power Supply 1",
            "State": "Enabled",
            "Manufacturer": "Cisco Systems Inc",
            "Model": "UCSX-PSU-2800AC",
            "SerialNumber": "ART2510F5AT"
        },
        {
            "MemberId": "2",
            "Name": "Power Supply 2",
            "State": "Absent",
            "Manufacturer": "",
            "Model": "",
            "SerialNumber": ""
        },
        {
            "MemberId": "3",
            "Name": "Power Supply 3",
            "State": "Absent",
            "Manufacturer": "",
            "Model": "",
            "SerialNumber": ""
        },
        {
            "MemberId": "4",
            "Name": "Power Supply 4",
            "State": "Enabled",
            "Manufacturer": "Cisco Systems Inc",
            "Model": "UCSX-PSU-2800AC",
            "SerialNumber": "ART2510F5AD"
        },
        {
            "MemberId": "5",
            "Name": "Power Supply 5",
            "State": "Absent",
            "Manufacturer": "",
            "Model": "",
            "SerialNumber": ""
        },
        {
            "MemberId": "6",
            "Name": "Power Supply 6",
            "State": "Absent",
            "Manufacturer": "",
            "Model": "",
            "SerialNumber": ""
        }
    ]
}
```
