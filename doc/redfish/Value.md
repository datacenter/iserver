# Find resource property by value

[[Next]](./Resource.md) [[Back]](./README.md)

Support for property search by value defined in multiple --value parameters with logical OR operation.

Supported value parameters (string):
- eq(value) will match case-insensitive value
- EQ(value) will match case-sensitive value
- in(sub-value) will match case-insensitive values that contain sub-value
- IN(sub-value) will match case-sensitive values that contain sub-value
- value is the same as eq(value)

Supported value parameters (numeric):
- eq(value) is == check
- gt(value) is > check
- ge(value) is >= check
- lt(value) is < check
- le(value) is <= check

Add --deep for recursive search starting with --uri.

## eq(value) or value

String

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --value disabled

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "Boot": {
        "BootSourceOverrideEnabled": "Disabled"
    },
    "HostWatchdogTimer": {
        "Status": {
            "State": "Disabled"
        }
    }
}
```

Integer

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --value 384

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "Oem": {
        "Cisco": {
            "SystemEffectiveMemory": 384
        }
    },
    "MemorySummary": {
        "TotalSystemMemoryGiB": 384
    }
}
```

## EQ(value)

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --value FA11122233

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "SerialNumber": "FA11122233",
    "Id": "FA11122233"
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
    --value "in(down)"

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "HostWatchdogTimer": {
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
    --value "in(Off)"

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "PowerRestorePolicy": "AlwaysOff",
    "IndicatorLED": "Off"
}
```

## gt()

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --value "gt(5)"

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "Oem": {
        "Cisco": {
            "SystemEffectiveMemory": 384,
            "SystemEffectiveSpeed": 2933
        }
    },
    "MemorySummary": {
        "TotalSystemMemoryGiB": 384
    }
}
```

## ge()

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --value "ge(5)"

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "PCIeDevices@odata.count": 5,
    "PCIeFunctions@odata.count": 5,
    "Oem": {
        "Cisco": {
            "SystemEffectiveMemory": 384,
            "SystemEffectiveSpeed": 2933
        }
    },
    "MemorySummary": {
        "TotalSystemMemoryGiB": 384
    }
}
```

## lt()

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --value "lt(384)"

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "ProcessorSummary": {
        "Count": 2
    },
    "PCIeDevices@odata.count": 5,
    "PCIeFunctions@odata.count": 5,
    "HostWatchdogTimer": {
        "FunctionEnabled": false
    },
    "Oem": {
        "Cisco": {
            "DimmBlacklistingEnabled": true,
            "PostCompletionStatus": true,
            "FrontPanelButtonsLocked": false
        }
    }
}
```

## le()

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --value "le(384)"

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "ProcessorSummary": {
        "Count": 2
    },
    "PCIeDevices@odata.count": 5,
    "PCIeFunctions@odata.count": 5,
    "HostWatchdogTimer": {
        "FunctionEnabled": false
    },
    "Oem": {
        "Cisco": {
            "DimmBlacklistingEnabled": true,
            "SystemEffectiveMemory": 384,
            "PostCompletionStatus": true,
            "FrontPanelButtonsLocked": false
        }
    },
    "MemorySummary": {
        "TotalSystemMemoryGiB": 384
    }
}
```

## Multiple values

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --value "eq(384)"
    --value ok

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "Oem": {
        "Cisco": {
            "SystemEffectiveMemory": 384
        }
    },
    "MemorySummary": {
        "TotalSystemMemoryGiB": 384,
        "Status": {
            "HealthRollup": "OK",
            "Health": "OK"
        }
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK"
    }
}
```

## Recursive search

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --value "ge(384)"
    --deep

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "MemorySummary": {
        "TotalSystemMemoryGiB": 384
    },
    "Oem": {
        "Cisco": {
            "SystemEffectiveMemory": 384,
            "SystemEffectiveSpeed": 2933
        }
    }
}

/redfish/v1/Systems/FA11122233/Memory/DIMM_A1
----------------------------------------------
{
    "CapacityMiB": 32768,
    "OperatingSpeedMhz": 2933
}

/redfish/v1/Systems/FA11122233/Memory/DIMM_B1
----------------------------------------------
{
    "CapacityMiB": 32768,
    "OperatingSpeedMhz": 2933
}

...
```

[[Back]](./README.md