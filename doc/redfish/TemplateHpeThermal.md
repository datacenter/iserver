# HPE Thermal Templates

```
# iserver get redfish endpoint
    --type hp
    --ip 10.58.24.211
    --port 49153
    --username administrator
    --password ******
    --template thermal

+-------------------+----------+---------+--------------+------------------+----------------------------+
| Name              | State    | Health  | Location     | Value (Celcius)  | Upper Threshold (Celcius)  |
+-------------------+----------+---------+--------------+------------------+----------------------------+
| 01-Inlet Ambient  | Enabled  | OK      | Intake       | 23               | 42                         | 
| 02-CPU 1          | Enabled  | OK      | CPU          | 40               | 70                         | 
| 03-CPU 2          | Enabled  | OK      | CPU          | 40               | 70                         | 
| 04-P1 DIMM 1-8    | Absent   |         | SystemBoard  | 0                | None                       | 
| 05-P1 PMM 1-8     | Absent   |         | SystemBoard  | 0                | None                       | 
| 06-P1 DIMM 9-16   | Enabled  | OK      | SystemBoard  | 31               | 85                         | 
| 07-P1 PMM 9-16    | Absent   |         | SystemBoard  | 0                | None                       | 
| 08-P2 DIMM 1-8    | Absent   |         | SystemBoard  | 0                | None                       | 
| 09-P2 PMM 1-8     | Absent   |         | SystemBoard  | 0                | None                       | 
| 10-P2 DIMM 9-16   | Enabled  | OK      | SystemBoard  | 31               | 85                         | 
| 11-P2 PMM 9-16    | Absent   |         | SystemBoard  | 0                | None                       | 
| 12-VR P1          | Enabled  | OK      | SystemBoard  | 38               | 110                        | 
| 13-VR P2          | Enabled  | OK      | SystemBoard  | 39               | 110                        | 
| 14-VR P1 Mem 1    | Enabled  | OK      | SystemBoard  | 30               | 110                        | 
| 15-VR P1 Mem 2    | Enabled  | OK      | SystemBoard  | 32               | 110                        | 
| 16-VR P2 Mem 1    | Enabled  | OK      | SystemBoard  | 33               | 110                        | 
| 17-VR P2 Mem 2    | Enabled  | OK      | SystemBoard  | 31               | 110                        | 
| 18-Chipset        | Enabled  | OK      | SystemBoard  | 39               | 100                        | 
| 19-BMC            | Enabled  | OK      | SystemBoard  | 65               | 110                        | 
| 20-HD Max         | Enabled  | OK      | SystemBoard  | 40               | 60                         | 
| 21-Exp Bay Drive  | Absent   |         | SystemBoard  | 0                | None                       | 
| 22-Stor Batt      | Enabled  | OK      | SystemBoard  | 24               | 60                         | 
| 23-E-Fuse         | Enabled  | OK      | SystemBoard  | 32               | 100                        | 
| 24-P/S 1          | Enabled  | OK      | PowerSupply  | 40               | None                       | 
| 25-P/S 1 Inlet    | Enabled  | OK      | PowerSupply  | 35               | None                       | 
| 26-P/S 2          | Enabled  | OK      | PowerSupply  | 40               | None                       | 
| 27-P/S 2 Inlet    | Enabled  | OK      | PowerSupply  | 35               | None                       | 
| 29-LOM Card       | Enabled  | OK      | SystemBoard  | 40               | 95                         | 
| 30-HD Controller  | Absent   |         | SystemBoard  | 0                | None                       | 
| 31-HD Cntlr Zone  | Absent   |         | SystemBoard  | 0                | None                       | 
| 32-Board Inlet    | Enabled  | OK      | SystemBoard  | 26               | 60                         | 
| 33-BMC Zone       | Enabled  | OK      | SystemBoard  | 38               | 90                         | 
| 34-P/S 2 Zone     | Enabled  | OK      | PowerSupply  | 34               | 90                         | 
| 35-I/O Zone       | Enabled  | OK      | SystemBoard  | 33               | 90                         | 
| 36-Battery Zone   | Enabled  | OK      | SystemBoard  | 31               | 90                         | 
| 37-PCI 1          | Enabled  | OK      | SystemBoard  | 40               | 100                        | 
| 38-PCI 1 Zone     | Enabled  | OK      | SystemBoard  | 42               | 90                         | 
| 39-PCI 2          | Absent   |         | SystemBoard  | 0                | None                       | 
| 40-PCI 2 Zone     | Enabled  | OK      | SystemBoard  | 41               | 90                         | 
| 41-PCI 3          | Absent   |         | SystemBoard  | 0                | None                       | 
| 42-PCI 3 Zone     | Absent   |         | SystemBoard  | 0                | None                       | 
| 43-ExpBayBoot     | Enabled  | OK      | SystemBoard  | 35               | 60                         | 
| 46-AHCI HD Max    | Absent   |         | SystemBoard  | 0                | None                       | 
| 50-CPU 1 PkgTmp   | Enabled  | OK      | CPU          | 44               | None                       | 
| 51-CPU 2 PkgTmp   | Enabled  | OK      | CPU          | 39               | None                       | 
+-------------------+----------+---------+--------------+------------------+----------------------------+

+--------+----------+---------+-------------+
| Name   | State    | Health  | Value       |
+--------+----------+---------+-------------+
| Fan 1  | Enabled  | OK      | 16 Percent  | 
| Fan 2  | Enabled  | OK      | 16 Percent  | 
| Fan 3  | Enabled  | OK      | 16 Percent  | 
| Fan 4  | Enabled  | OK      | 16 Percent  | 
| Fan 5  | Enabled  | OK      | 16 Percent  | 
| Fan 6  | Enabled  | OK      | 16 Percent  | 
| Fan 7  | Enabled  | OK      | 16 Percent  | 
+--------+----------+---------+-------------+
```

```
# iserver get redfish endpoint
    --type hp
    --ip 10.58.24.211
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
            "Name": "01-Inlet Ambient",
            "PhysicalContext": "Intake",
            "ReadingCelsius": 23,
            "UpperThresholdCritical": 42
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 2,
            "Name": "02-CPU 1",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 40,
            "UpperThresholdCritical": 70
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 3,
            "Name": "03-CPU 2",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 40,
            "UpperThresholdCritical": 70
        },
        {
            "State": "Absent",
            "Health": "",
            "SensorNumber": 4,
            "Name": "04-P1 DIMM 1-8",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": null
        },
        {
            "State": "Absent",
            "Health": "",
            "SensorNumber": 5,
            "Name": "05-P1 PMM 1-8",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": null
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 6,
            "Name": "06-P1 DIMM 9-16",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 31,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Absent",
            "Health": "",
            "SensorNumber": 7,
            "Name": "07-P1 PMM 9-16",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": null
        },
        {
            "State": "Absent",
            "Health": "",
            "SensorNumber": 8,
            "Name": "08-P2 DIMM 1-8",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": null
        },
        {
            "State": "Absent",
            "Health": "",
            "SensorNumber": 9,
            "Name": "09-P2 PMM 1-8",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": null
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 10,
            "Name": "10-P2 DIMM 9-16",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 31,
            "UpperThresholdCritical": 85
        },
        {
            "State": "Absent",
            "Health": "",
            "SensorNumber": 11,
            "Name": "11-P2 PMM 9-16",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": null
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 12,
            "Name": "12-VR P1",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 38,
            "UpperThresholdCritical": 110
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 13,
            "Name": "13-VR P2",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 39,
            "UpperThresholdCritical": 110
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 14,
            "Name": "14-VR P1 Mem 1",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 30,
            "UpperThresholdCritical": 110
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 15,
            "Name": "15-VR P1 Mem 2",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 32,
            "UpperThresholdCritical": 110
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 16,
            "Name": "16-VR P2 Mem 1",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 33,
            "UpperThresholdCritical": 110
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 17,
            "Name": "17-VR P2 Mem 2",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 31,
            "UpperThresholdCritical": 110
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 18,
            "Name": "18-Chipset",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 39,
            "UpperThresholdCritical": 100
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 19,
            "Name": "19-BMC",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 65,
            "UpperThresholdCritical": 110
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 20,
            "Name": "20-HD Max",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 40,
            "UpperThresholdCritical": 60
        },
        {
            "State": "Absent",
            "Health": "",
            "SensorNumber": 21,
            "Name": "21-Exp Bay Drive",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": null
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 22,
            "Name": "22-Stor Batt",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 24,
            "UpperThresholdCritical": 60
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 23,
            "Name": "23-E-Fuse",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 32,
            "UpperThresholdCritical": 100
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 24,
            "Name": "24-P/S 1",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 40,
            "UpperThresholdCritical": null
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 25,
            "Name": "25-P/S 1 Inlet",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 35,
            "UpperThresholdCritical": null
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 26,
            "Name": "26-P/S 2",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 40,
            "UpperThresholdCritical": null
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 27,
            "Name": "27-P/S 2 Inlet",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 35,
            "UpperThresholdCritical": null
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 28,
            "Name": "29-LOM Card",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 40,
            "UpperThresholdCritical": 95
        },
        {
            "State": "Absent",
            "Health": "",
            "SensorNumber": 29,
            "Name": "30-HD Controller",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": null
        },
        {
            "State": "Absent",
            "Health": "",
            "SensorNumber": 30,
            "Name": "31-HD Cntlr Zone",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": null
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 31,
            "Name": "32-Board Inlet",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 26,
            "UpperThresholdCritical": 60
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 32,
            "Name": "33-BMC Zone",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 38,
            "UpperThresholdCritical": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 33,
            "Name": "34-P/S 2 Zone",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 34,
            "UpperThresholdCritical": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 34,
            "Name": "35-I/O Zone",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 33,
            "UpperThresholdCritical": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 35,
            "Name": "36-Battery Zone",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 31,
            "UpperThresholdCritical": 90
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 36,
            "Name": "37-PCI 1",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 40,
            "UpperThresholdCritical": 100
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 37,
            "Name": "38-PCI 1 Zone",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 42,
            "UpperThresholdCritical": 90
        },
        {
            "State": "Absent",
            "Health": "",
            "SensorNumber": 38,
            "Name": "39-PCI 2",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": null
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 39,
            "Name": "40-PCI 2 Zone",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 41,
            "UpperThresholdCritical": 90
        },
        {
            "State": "Absent",
            "Health": "",
            "SensorNumber": 40,
            "Name": "41-PCI 3",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": null
        },
        {
            "State": "Absent",
            "Health": "",
            "SensorNumber": 41,
            "Name": "42-PCI 3 Zone",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": null
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 42,
            "Name": "43-ExpBayBoot",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 35,
            "UpperThresholdCritical": 60
        },
        {
            "State": "Absent",
            "Health": "",
            "SensorNumber": 43,
            "Name": "46-AHCI HD Max",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "UpperThresholdCritical": null
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 44,
            "Name": "50-CPU 1 PkgTmp",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 44,
            "UpperThresholdCritical": null
        },
        {
            "State": "Enabled",
            "Health": "OK",
            "SensorNumber": 45,
            "Name": "51-CPU 2 PkgTmp",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 39,
            "UpperThresholdCritical": null
        }
    ],
    "Fan": [
        {
            "Name": "Fan 1",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "",
            "ReadingUnits": "Percent",
            "Reading": 16,
            "Value": "16 Percent"
        },
        {
            "Name": "Fan 2",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "",
            "ReadingUnits": "Percent",
            "Reading": 16,
            "Value": "16 Percent"
        },
        {
            "Name": "Fan 3",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "",
            "ReadingUnits": "Percent",
            "Reading": 16,
            "Value": "16 Percent"
        },
        {
            "Name": "Fan 4",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "",
            "ReadingUnits": "Percent",
            "Reading": 16,
            "Value": "16 Percent"
        },
        {
            "Name": "Fan 5",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "",
            "ReadingUnits": "Percent",
            "Reading": 16,
            "Value": "16 Percent"
        },
        {
            "Name": "Fan 6",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "",
            "ReadingUnits": "Percent",
            "Reading": 16,
            "Value": "16 Percent"
        },
        {
            "Name": "Fan 7",
            "State": "Enabled",
            "Health": "OK",
            "PhysicalContext": "",
            "ReadingUnits": "Percent",
            "Reading": 16,
            "Value": "16 Percent"
        }
    ]
}
```
