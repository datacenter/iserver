# Dell Thermal Templates

```
# iserver get redfish endpoint
    --type dell
    --ip 10.58.24.210
    --port 49153
    --username administrator
    --password ******
    --template thermal

+----------------------------+----------+---------+--------------+------------------+----------------------------+
| Name                       | State    | Health  | Location     | Value (Celcius)  | Upper Threshold (Celcius)  |
+----------------------------+----------+---------+--------------+------------------+----------------------------+
| CPU1 Temp                  | Enabled  | OK      | CPU          | 57               | 98                         | 
| CPU2 Temp                  | Enabled  | OK      | CPU          | 54               | 98                         | 
| System Board Exhaust Temp  | Enabled  | OK      | SystemBoard  | 34               | 80                         | 
| System Board Inlet Temp    | Enabled  | OK      | SystemBoard  | 18               | 42                         | 
+----------------------------+----------+---------+--------------+------------------+----------------------------+

+---------------------+----------+---------+-----------+
| Name                | State    | Health  | Value     |
+---------------------+----------+---------+-----------+
| System Board Fan1A  | Enabled  | OK      | 9000 RPM  | 
| System Board Fan1B  | Enabled  | OK      | 5400 RPM  | 
| System Board Fan1C  | Enabled  | OK      | 9240 RPM  | 
| System Board Fan1D  | Enabled  | OK      | 5400 RPM  | 
| System Board Fan2A  | Enabled  | OK      | 9120 RPM  | 
| System Board Fan2B  | Enabled  | OK      | 5520 RPM  | 
| System Board Fan2C  | Enabled  | OK      | 9240 RPM  | 
| System Board Fan2D  | Enabled  | OK      | 5400 RPM  | 
| System Board Fan3A  | Enabled  | OK      | 9240 RPM  | 
| System Board Fan3B  | Enabled  | OK      | 5520 RPM  | 
| System Board Fan3C  | Enabled  | OK      | 9120 RPM  | 
| System Board Fan3D  | Enabled  | OK      | 5400 RPM  | 
| System Board Fan4A  | Enabled  | OK      | 9000 RPM  | 
| System Board Fan4B  | Enabled  | OK      | 5400 RPM  | 
| System Board Fan4C  | Enabled  | OK      | 9120 RPM  | 
| System Board Fan4D  | Enabled  | OK      | 5400 RPM  | 
+---------------------+----------+---------+-----------+
```

```
# iserver get redfish endpoint
    --type dell
    --ip 10.58.24.210
    --port 49153
    --username administrator
    --password ******
    --template thermal
    --output json

{
    "Temperature": [
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 1,
            "Name": "CPU1 Temp",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 57,
            "UpperThresholdCritical": 98
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 2,
            "Name": "CPU2 Temp",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 54,
            "UpperThresholdCritical": 98
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 6,
            "Name": "System Board Exhaust Temp",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 34,
            "UpperThresholdCritical": 80
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 5,
            "Name": "System Board Inlet Temp",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 18,
            "UpperThresholdCritical": 42
        }
    ],
    "Fan": [
        {
            "Name": "System Board Fan1A",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 9000,
            "Value": "9000 RPM"
        },
        {
            "Name": "System Board Fan1B",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 5400,
            "Value": "5400 RPM"
        },
        {
            "Name": "System Board Fan1C",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 9240,
            "Value": "9240 RPM"
        },
        {
            "Name": "System Board Fan1D",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 5400,
            "Value": "5400 RPM"
        },
        {
            "Name": "System Board Fan2A",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 9120,
            "Value": "9120 RPM"
        },
        {
            "Name": "System Board Fan2B",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 5520,
            "Value": "5520 RPM"
        },
        {
            "Name": "System Board Fan2C",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 9240,
            "Value": "9240 RPM"
        },
        {
            "Name": "System Board Fan2D",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 5400,
            "Value": "5400 RPM"
        },
        {
            "Name": "System Board Fan3A",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 9240,
            "Value": "9240 RPM"
        },
        {
            "Name": "System Board Fan3B",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 5520,
            "Value": "5520 RPM"
        },
        {
            "Name": "System Board Fan3C",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 9120,
            "Value": "9120 RPM"
        },
        {
            "Name": "System Board Fan3D",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 5400,
            "Value": "5400 RPM"
        },
        {
            "Name": "System Board Fan4A",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 9000,
            "Value": "9000 RPM"
        },
        {
            "Name": "System Board Fan4B",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 5400,
            "Value": "5400 RPM"
        },
        {
            "Name": "System Board Fan4C",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 9120,
            "Value": "9120 RPM"
        },
        {
            "Name": "System Board Fan4D",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "SystemBoard",
            "ReadingUnits": "RPM",
            "Reading": 5400,
            "Value": "5400 RPM"
        }
    ]
}
```
