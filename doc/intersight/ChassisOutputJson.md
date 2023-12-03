# Intersight Chassis

## JSON output

```
# iserver get chassis --name ucsx -o json

[
    {
        "__Output": {
            "Health": "Green",
            "OperStateTick": "Green"
        },
        "ConnectionPath": "A,B",
        "ConnectionStatus": "A,B",
        "Description": "Cisco Blade Server Chassis, 7U with Eight Vertical Blade Server Slots",
        "Dn": "chassis-1",
        "DeviceMoId": "64be6ab66f726131018165d8",
        "Moid": "64be876876752d39013ea7f4",
        "Model": "UCSX-9508",
        "Name": "ucsx-eu-spdc-1",
        "OperState": "OK",
        "PartNumber": "68-6847-03",
        "Pid": "UCSX-9508",
        "ProductName": "Cisco UCSX 9508 Chassis",
        "Serial": "FOX2642P1SA",
        "Sku": "UCSX-9508",
        "Vendor": "Cisco Systems Inc",
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
        "OperStateTick": "\u2713",
        "NodeCount": 3,
        "FanModuleCount": 4,
        "IoCount": 2,
        "ExpanderModuleCount": 2,
        "PsuCount": 6,
        "Inventory": [
            {
                "Order": 1,
                "SubOrder": 1,
                "Type": "Chassis",
                "Name": "ucsx-eu-spdc-1",
                "Model": "UCSX-9508",
                "Vendor": "Cisco Systems Inc",
                "Serial": "FOX2642P1SA",
                "Pid": "UCSX-9508",
                "ChassisMoid": "64be876876752d39013ea7f4",
                "ServerType": "N/A",
                "ServerPid": "N/A",
                "ServerSerial": "N/A"
            }
        ],
        "ChassisPid": "UCSX-9508",
        "ChassisSerial": "FOX2642P1SA",
        "ProfileInfo": null
    }
]
```

Developer output

```
# iserver get chassis --name ucsx -o json

{
    "duration": 7042,
    "isctl": {
        "read": true,
        "calls": 2,
        "success": 2,
        "failed": 0,
        "total_time": 4921
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
        "lines": 4
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 14:36:32.490424	True	2406	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:36:35.031861	True	2515	1	isctl get chassis profile --filter "AssignedChassis/Moid in ('64be876876752d39013ea7f4')" --expand "ConfigResult" -o json --top 100
```

[[Back]](./ChassisInventory.md)