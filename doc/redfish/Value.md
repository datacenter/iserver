# Find resource property by value

iserver supports searching for properties by value defined in multiple --value parameters with logical OR operation.

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
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --value disabled

/redfish/v1/Systems/WZP23400AK4
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
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --value 384

/redfish/v1/Systems/WZP23400AK4
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
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --value WZP23400AK4

/redfish/v1/Systems/WZP23400AK4
-------------------------------
{
    "SerialNumber": "WZP23400AK4",
    "Id": "WZP23400AK4"
}
```

## in()

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --value "in(down)"

/redfish/v1/Systems/WZP23400AK4
-------------------------------
{
    "HostWatchdogTimer": {
        "TimeoutAction": "PowerDown"
    }
}
```

## IN()

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --value "in(Off)"

/redfish/v1/Systems/WZP23400AK4
-------------------------------
{
    "PowerRestorePolicy": "AlwaysOff",
    "IndicatorLED": "Off"
}
```

## gt()

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --value "gt(5)"

/redfish/v1/Systems/WZP23400AK4
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
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --value "ge(5)"

/redfish/v1/Systems/WZP23400AK4
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
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --value "lt(384)"

/redfish/v1/Systems/WZP23400AK4
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
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --value "le(384)"

/redfish/v1/Systems/WZP23400AK4
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
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --value "eq(384)"
    --value ok

/redfish/v1/Systems/WZP23400AK4
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

## Reference

All outputs above are in the context of the System resource outputs

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID

/redfish/v1/Systems/WZP23400AK4
-------------------------------
{
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4",
    "@odata.type": "#ComputerSystem.v1_9_0.ComputerSystem",
    "@odata.context": "/redfish/v1/$metadata#ComputerSystem.ComputerSystem",
    "Description": "Represents general resources for the overall system",
    "Processors": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Processors"
    },
    "SimpleStorage": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/SimpleStorage"
    },
    "Storage": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage"
    },
    "Memory": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory"
    },
    "MemoryDomains": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/MemoryDomains"
    },
    "NetworkInterfaces": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/NetworkInterfaces"
    },
    "Bios": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Bios"
    },
    "SecureBoot": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/SecureBoot"
    },
    "EthernetInterfaces": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces"
    },
    "LogServices": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/LogServices"
    },
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "CooledBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/Thermal"
            }
        ],
        "ManagedBy": [
            {
                "@odata.id": "/redfish/v1/Managers/CIMC"
            }
        ],
        "PoweredBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/Power"
            }
        ]
    },
    "SerialNumber": "WZP23400AK4",
    "Boot": {
        "BootSourceOverrideTarget": "None",
        "BootSourceOverrideTarget@Redfish.AllowableValues": [
            "None",
            "Pxe",
            "Floppy",
            "Cd",
            "Hdd",
            "BiosSetup",
            "Diags"
        ],
        "BootSourceOverrideEnabled@Redfish.AllowableValues": [
            "Once",
            "Continuous",
            "Disabled"
        ],
        "BootSourceOverrideEnabled": "Disabled"
    },
    "Id": "WZP23400AK4",
    "AssetTag": "022C2F7",
    "PowerState": "On",
    "SystemType": "Physical",
    "ProcessorSummary": {
        "Model": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
        "Count": 2
    },
    "HostName": "aio-2-p2b-eu-spdc-WZP23400AK4",
    "PowerRestorePolicy": "AlwaysOff",
    "PCIeDevices@odata.count": 5,
    "PCIeFunctions@odata.count": 5,
    "UUID": "B813910F-BFD2-439F-9C3B-75B376C5B160",
    "TrustedModules": [
        {
            "Status": {
                "State": "Absent"
            },
            "Oem": {
                "Cisco": {
                    "TPM": null
                }
            }
        }
    ],
    "Name": "UCS C240 M5SN",
    "HostWatchdogTimer": {
        "Status": {
            "State": "Disabled"
        },
        "WarningAction": "None",
        "FunctionEnabled": false,
        "TimeoutAction": "PowerDown"
    },
    "PCIeFunctions": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/3/PCIeFunctions/3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/6/PCIeFunctions/6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MLOM/PCIeFunctions/MLOM"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MRAID/PCIeFunctions/MRAID"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/L/PCIeFunctions/L"
        }
    ],
    "Oem": {
        "Cisco": {
            "DimmBlacklistingEnabled": true,
            "SystemEffectiveMemory": 384,
            "SystemEffectiveSpeed": 2933,
            "PostCompletionStatus": true,
            "FrontPanelButtonsLocked": false
        }
    },
    "PCIeDevices": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MLOM"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MRAID"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/L"
        }
    ],
    "BiosVersion": "C240M5.4.1.3i.0.0713210713",
    "Manufacturer": "Cisco Systems Inc",
    "MemorySummary": {
        "TotalSystemMemoryGiB": 384,
        "Status": {
            "HealthRollup": "OK",
            "Health": "OK"
        }
    },
    "Model": "UCSC-C240-M5SN",
    "IndicatorLED": "Off",
    "Status": {
        "State": "Enabled",
        "Health": "OK",
        "HealthRollup": "OK"
    },
    "Actions": {
        "#ComputerSystem.Reset": {
            "target": "/redfish/v1/Systems/WZP23400AK4/Actions/ComputerSystem.Reset",
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff",
                "GracefulShutdown",
                "GracefulRestart",
                "ForceRestart",
                "Nmi",
                "PowerCycle"
            ]
        },
        "Oem": {
            "#CiscoUCSExtensions.ResetBIOSCMOS": {
                "target": "/redfish/v1/Systems/WZP23400AK4/Actions/Oem/ComputerSystem.ResetBIOSCMOS",
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetBIOSCMOS"
            }
        }
    }
}
```

## Recursive search

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --value "ge(384)"
    --deep

/redfish/v1/Systems/WZP23400AK4
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

/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_A1
----------------------------------------------
{
    "CapacityMiB": 32768,
    "OperatingSpeedMhz": 2933
}

/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_B1
----------------------------------------------
{
    "CapacityMiB": 32768,
    "OperatingSpeedMhz": 2933
}

/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_C1
----------------------------------------------
{
    "CapacityMiB": 32768,
    "OperatingSpeedMhz": 2933
}

/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_D1
----------------------------------------------
{
    "CapacityMiB": 32768,
    "OperatingSpeedMhz": 2933
}

/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_E1
----------------------------------------------
{
    "CapacityMiB": 32768,
    "OperatingSpeedMhz": 2933
}

/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_F1
----------------------------------------------
{
    "CapacityMiB": 32768,
    "OperatingSpeedMhz": 2933
}

/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_G1
----------------------------------------------
{
    "CapacityMiB": 32768,
    "OperatingSpeedMhz": 2933
}

/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_H1
----------------------------------------------
{
    "CapacityMiB": 32768,
    "OperatingSpeedMhz": 2933
}

/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_J1
----------------------------------------------
{
    "CapacityMiB": 32768,
    "OperatingSpeedMhz": 2933
}

/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_K1
----------------------------------------------
{
    "CapacityMiB": 32768,
    "OperatingSpeedMhz": 2933
}

/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_L1
----------------------------------------------
{
    "CapacityMiB": 32768,
    "OperatingSpeedMhz": 2933
}

/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_M1
----------------------------------------------
{
    "CapacityMiB": 32768,
    "OperatingSpeedMhz": 2933
}

/redfish/v1/Systems/WZP23400AK4/Processors/CPU1
-----------------------------------------------
{
    "MaxSpeedMHz": 4000
}

/redfish/v1/Systems/WZP23400AK4/Processors/CPU2
-----------------------------------------------
{
    "MaxSpeedMHz": 4000
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10
-------------------------------------------------------
{
    "BlockSizeBytes": 512,
    "CapacityBytes": 960196771840,
    "Oem": {
        "Cisco": {
            "CoercedSizeBytes": 958999298048,
            "NonCoercedSizeBytes": 959659900928,
            "SmartData": {
                "PowerOnHours": 15660,
                "WearStatusInDays": 1806
            }
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11
-------------------------------------------------------
{
    "BlockSizeBytes": 512,
    "CapacityBytes": 960196771840,
    "Oem": {
        "Cisco": {
            "CoercedSizeBytes": 958999298048,
            "NonCoercedSizeBytes": 959659900928,
            "SmartData": {
                "PowerOnHours": 15645,
                "WearStatusInDays": 1825
            }
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12
-------------------------------------------------------
{
    "BlockSizeBytes": 512,
    "CapacityBytes": 960196771840,
    "Oem": {
        "Cisco": {
            "CoercedSizeBytes": 958999298048,
            "NonCoercedSizeBytes": 959659900928,
            "SmartData": {
                "PowerOnHours": 15645,
                "WearStatusInDays": 1825
            }
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13
-------------------------------------------------------
{
    "BlockSizeBytes": 512,
    "CapacityBytes": 1200243081216,
    "Oem": {
        "Cisco": {
            "CoercedSizeBytes": 1198999470080,
            "NonCoercedSizeBytes": 1199706210304
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14
-------------------------------------------------------
{
    "BlockSizeBytes": 512,
    "CapacityBytes": 1200243081216,
    "Oem": {
        "Cisco": {
            "CoercedSizeBytes": 1198999470080,
            "NonCoercedSizeBytes": 1199706210304
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15
-------------------------------------------------------
{
    "BlockSizeBytes": 512,
    "CapacityBytes": 1200243081216,
    "Oem": {
        "Cisco": {
            "CoercedSizeBytes": 1198999470080,
            "NonCoercedSizeBytes": 1199706210304
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16
-------------------------------------------------------
{
    "BlockSizeBytes": 512,
    "CapacityBytes": 1200243081216,
    "Oem": {
        "Cisco": {
            "CoercedSizeBytes": 1198999470080,
            "NonCoercedSizeBytes": 1199706210304
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17
-------------------------------------------------------
{
    "BlockSizeBytes": 512,
    "CapacityBytes": 1200243081216,
    "Oem": {
        "Cisco": {
            "CoercedSizeBytes": 1198999470080,
            "NonCoercedSizeBytes": 1199706210304
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18
-------------------------------------------------------
{
    "BlockSizeBytes": 512,
    "CapacityBytes": 1200243081216,
    "Oem": {
        "Cisco": {
            "CoercedSizeBytes": 1198999470080,
            "NonCoercedSizeBytes": 1199706210304
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9
------------------------------------------------------
{
    "BlockSizeBytes": 512,
    "CapacityBytes": 960196771840,
    "Oem": {
        "Cisco": {
            "CoercedSizeBytes": 958999298048,
            "NonCoercedSizeBytes": 959659900928,
            "SmartData": {
                "PowerOnHours": 15660,
                "WearStatusInDays": 1806
            }
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/0
-------------------------------------------------------
{
    "BlockSizeBytes": 512,
    "CapacityBytes": 1917998596096,
    "OptimumIOSizeBytes": 65536
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/1
-------------------------------------------------------
{
    "BlockSizeBytes": 512,
    "CapacityBytes": 4795997880320,
    "OptimumIOSizeBytes": 65536
}
```