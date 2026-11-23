# Find resource property by key

[[Next]](./Value.md) [[Back]](./README.md)

Support for key search by value defined in multiple --key parameters with logical OR operation.
- eq(value) will match case-insensitive properties with name value
- EQ(value) will match case-sensitive properties with name value
- in(value) will match case-insensitive properties that contain value
- IN(value) will match case-sensitive properties that contain value
- value is the same as eq(value)

Add --deep for recursive search starting with --uri.

## eq()

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --key state

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "HostWatchdogTimer": {
        "Status": {
            "State": "Disabled"
        }
    },
    "Status": {
        "State": "Enabled"
    }
}
```

## EQ()

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --key "EQ(target)"

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "Actions": {
        "#ComputerSystem.Reset": {
            "target": "/redfish/v1/Systems/FA11122233/Actions/ComputerSystem.Reset"
        },
        "Oem": {
            "#CiscoUCSExtensions.ResetBIOSCMOS": {
                "target": "/redfish/v1/Systems/FA11122233/Actions/Oem/ComputerSystem.ResetBIOSCMOS"
            }
        }
    }
}
```

## in()

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --key "in(timer)"

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "HostWatchdogTimer": {
        "Status": {
            "State": "Disabled"
        },
        "WarningAction": "None",
        "FunctionEnabled": false,
        "TimeoutAction": "PowerDown"
    }
}
```

## IN()

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --key "in(Tag)"

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "AssetTag": "666"
}
```

## Recursive search

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Chassis \
    --key "in(power)"
    --deep

/redfish/v1/Chassis/1
---------------------
{
    "Links": {
        "PoweredBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/Power"
            }
        ]
    },
    "Power": {
        "@odata.id": "/redfish/v1/Chassis/1/Power"
    },
    "PowerState": "On"
}

/redfish/v1/Chassis/1/Power
---------------------------
{
    "PowerControl": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/1",
            ...
        }
    ],
    "PowerSupplies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/PSU1",
            ...
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/PSU2",
            ...
        }
    ]
}
```

[[Back]](./README.md)