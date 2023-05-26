# Resource: /api-explorer/resources/redfish/v1/Systems

Vendor | Model
--- | ---
Cisco | UCSX-210C-M6

## /api-explorer/resources/redfish/v1/Systems

```{
    "@odata.context": "/redfish/v1/$metadata#ComputerSystemCollection.ComputerSystemCollection",
    "@odata.id": "/redfish/v1/Systems",
    "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection",
    "Description": "Collection of Computer Systems",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Computer System Collection"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM

```{
    "@odata.context": "/redfish/v1/$metadata#ComputerSystem.ComputerSystem",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM",
    "@odata.type": "#ComputerSystem.v1_13_0.ComputerSystem",
    "Actions": {
        "#ComputerSystem.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff",
                "ForceRestart",
                "GracefulShutdown",
                "GracefulRestart",
                "PowerCycle"
            ],
            "target": "/redfish/v1/Systems/FCH25337EHM/Actions/ComputerSystem.Reset"
        },
        "Oem": {
            "#CiscoUCSExtensions.ResetBIOSCMOS": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetBIOSCMOS",
                "target": "/redfish/v1/Systems/FCH25337EHM/Actions/Oem/ComputerSystem.ResetBIOSCMOS"
            },
            "#CiscoUCSExtensions.TPMClear": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.TPMClear",
                "target": "/redfish/v1/Systems/FCH25337EHM/Actions/Oem/ComputerSystem.TPMClear"
            }
        }
    },
    "AssetTag": null,
    "BiosVersion": "X210M6.5.0.1i.0.0709221354",
    "Boot": {
        "BootSourceOverrideEnabled": "Disabled",
        "BootSourceOverrideEnabled@Redfish.AllowableValues": [
            "Once",
            "Continuous",
            "Disabled"
        ],
        "BootSourceOverrideTarget": "None",
        "BootSourceOverrideTarget@Redfish.AllowableValues": [
            "None",
            "Pxe",
            "Floppy",
            "Cd",
            "Hdd",
            "BiosSetup",
            "Diags"
        ]
    },
    "Description": "Represents general resources for the overall system",
    "Id": "FCH25337EHM",
    "Links": {
        "ManagedBy": [
            {
                "@odata.id": "/redfish/v1/Managers/CIMC"
            }
        ],
        "Oem": {
            "Cisco": {
                "SPDMDeviceCertificates": {
                    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Oem/Cisco/SPDMDevice/Certificates"
                },
                "SPDMTrustStoreCertificateCollection": {
                    "@odata.id": "/redfish/v1/Managers/CIMC/Oem/Cisco/SPDMTrustStore/Certificates"
                }
            }
        }
    },
    "LocationIndicatorActive": false,
    "Manufacturer": "Cisco Systems Inc",
    "Memory": {
        "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory"
    },
    "MemorySummary": {
        "TotalSystemMemoryGiB": 128
    },
    "Model": "UCSX-210C-M6",
    "Name": "UCSX-210C-M6",
    "NetworkInterfaces": {
        "@odata.id": "/redfish/v1/Systems/FCH25337EHM/NetworkInterfaces"
    },
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "DimmBlacklistingEnabled": true,
            "FrontPanelButtonsLocked": true,
            "MCTP": {
                "FaultAlertSetting": "Partial",
                "SPDMHandShakeStatus": "Completed"
            },
            "PostCompletionStatus": true,
            "PowerProfilingEnabled": true,
            "SystemEffectiveMemory": 128,
            "SystemEffectiveSpeed": 3200
        }
    },
    "PCIeDevices": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/0-MLOM"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/MSTOR-RAID"
        }
    ],
    "PCIeDevices@odata.count": 2,
    "PCIeFunctions": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/0-MLOM/PCIeFunctions/0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/MSTOR-RAID/PCIeFunctions/0"
        }
    ],
    "PCIeFunctions@odata.count": 2,
    "PowerRestorePolicy": "LastState",
    "PowerState": "On",
    "ProcessorSummary": {
        "Count": 2,
        "Model": "Intel(R) Xeon(R) Gold 6348 CPU @ 2.60GHz"
    },
    "Processors": {
        "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Processors"
    },
    "SerialNumber": "FCH25337EHM",
    "SimpleStorage": {
        "@odata.id": "/redfish/v1/Systems/FCH25337EHM/SimpleStorage"
    },
    "Status": {
        "Health": "OK",
        "Health@Message.ExtendedInfo": [],
        "HealthRollup": "OK",
        "HealthRollup@Message.ExtendedInfo": [],
        "State": "Enabled"
    },
    "Storage": {
        "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage"
    },
    "SystemType": "Physical",
    "TrustedModules": [
        {
            "FirmwareVersion": "7.85.459.0",
            "InterfaceType": "TPM2_0",
            "Oem": {
                "Cisco": {
                    "TPM": {
                        "Manufacturer": "Cisco Systems Inc",
                        "Model": "UCSX-TPM-002C",
                        "OwnershipStatus": "Owned",
                        "Revision": 1,
                        "SerialNumber": "FCH25257242"
                    }
                }
            },
            "Status": {
                "State": "Enabled"
            }
        }
    ],
    "UUID": "BBBBBBBB-BBBB-BBBB-0000-666666666668"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryCollection.MemoryCollection",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory",
    "@odata.type": "#MemoryCollection.MemoryCollection",
    "Description": "Collection of Memory resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_A1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_A2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_B1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_B2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_C1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_C2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_D1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_D2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_E1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_E2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_F1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_F2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_G1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_G2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_H1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_H2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_A1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_A2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_B1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_B2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_C1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_C2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_D1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_D2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_E1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_E2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_F1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_F2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_G1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_G2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_H1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_H2"
        }
    ],
    "Members@odata.count": 32,
    "Name": "Memory Collection"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_A1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_A1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "BaseModuleType": "RDIMM",
    "CapacityMiB": 65536,
    "DataWidthBits": 64,
    "Id": "1",
    "Manufacturer": "0xCE00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 0,
        "Slot": 0,
        "Socket": 0
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_P1_A1",
    "OperatingSpeedMhz": 3200,
    "PartNumber": "M393A8G40AB2-CWE    ",
    "SerialNumber": "2102-23ECEA4E",
    "Status": {
        "Health": "OK",
        "Health@Message.ExtendedInfo": [],
        "State": "Enabled"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_A2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_A2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "2",
    "Name": "DIMM_P1_A2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_B1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_B1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "3",
    "Name": "DIMM_P1_B1",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_B2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_B2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "4",
    "Name": "DIMM_P1_B2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_C1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_C1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "5",
    "Name": "DIMM_P1_C1",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_C2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_C2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "6",
    "Name": "DIMM_P1_C2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_D1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_D1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "7",
    "Name": "DIMM_P1_D1",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_D2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_D2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "8",
    "Name": "DIMM_P1_D2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_E1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_E1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "9",
    "Name": "DIMM_P1_E1",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_E2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_E2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "10",
    "Name": "DIMM_P1_E2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_F1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_F1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "11",
    "Name": "DIMM_P1_F1",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_F2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_F2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "12",
    "Name": "DIMM_P1_F2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_G1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_G1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "13",
    "Name": "DIMM_P1_G1",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_G2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_G2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "14",
    "Name": "DIMM_P1_G2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_H1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_H1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "15",
    "Name": "DIMM_P1_H1",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_H2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P1_H2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "16",
    "Name": "DIMM_P1_H2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_A1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_A1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "BaseModuleType": "RDIMM",
    "CapacityMiB": 65536,
    "DataWidthBits": 64,
    "Id": "17",
    "Manufacturer": "0xCE00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 0,
        "Slot": 0,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_P2_A1",
    "OperatingSpeedMhz": 3200,
    "PartNumber": "M393A8G40AB2-CWE    ",
    "SerialNumber": "2102-23ECEA5F",
    "Status": {
        "Health": "OK",
        "Health@Message.ExtendedInfo": [],
        "State": "Enabled"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_A2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_A2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "18",
    "Name": "DIMM_P2_A2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_B1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_B1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "19",
    "Name": "DIMM_P2_B1",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_B2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_B2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "20",
    "Name": "DIMM_P2_B2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_C1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_C1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "21",
    "Name": "DIMM_P2_C1",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_C2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_C2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "22",
    "Name": "DIMM_P2_C2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_D1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_D1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "23",
    "Name": "DIMM_P2_D1",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_D2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_D2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "24",
    "Name": "DIMM_P2_D2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_E1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_E1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "25",
    "Name": "DIMM_P2_E1",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_E2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_E2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "26",
    "Name": "DIMM_P2_E2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_F1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_F1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "27",
    "Name": "DIMM_P2_F1",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_F2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_F2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "28",
    "Name": "DIMM_P2_F2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_G1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_G1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "29",
    "Name": "DIMM_P2_G1",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_G2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_G2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "30",
    "Name": "DIMM_P2_G2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_H1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_H1",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "31",
    "Name": "DIMM_P2_H1",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_H2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Memory/DIMM_P2_H2",
    "@odata.type": "#Memory.v1_10_0.Memory",
    "Id": "32",
    "Name": "DIMM_P2_H2",
    "Status": {
        "State": "Absent"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/NetworkInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/NetworkInterfaces",
    "@odata.type": "#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "Description": "Collection of NetworkAdapter resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/NetworkInterfaces/UCSX-V4-Q25GML_FCH25337EE9"
        }
    ],
    "Members@odata.count": 1,
    "Name": "NetworkInterface Collection"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/NetworkInterfaces/UCSX-V4-Q25GML_FCH25337EE9

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterface.NetworkInterface",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/NetworkInterfaces/UCSX-V4-Q25GML_FCH25337EE9",
    "@odata.type": "#NetworkInterface.v1_2_0.NetworkInterface",
    "Description": "It represents the properties for Adapter Card UCSX-V4-Q25GML_FCH25337EE9",
    "Id": "UCSX-V4-Q25GML",
    "Links": {
        "NetworkAdapter": {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9"
        }
    },
    "Name": "Adapter Card UCSX-V4-Q25GML_FCH25337EE9"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Oem/Cisco/SPDMDevice/Certificates

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateCollection.CertificateCollection",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Oem/Cisco/SPDMDevice/Certificates",
    "@odata.type": "#CertificateCollection.CertificateCollecation",
    "Description": "Collection of Certificates",
    "Members": [],
    "Name": "Certificate"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/PCIeDevices/0-MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/0-MLOM",
    "@odata.type": "#PCIeDevice.v1_5_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "Id": "0-MLOM",
    "Name": "Cisco Network controller",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/0-MLOM/PCIeFunctions"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/PCIeDevices/0-MLOM/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/0-MLOM/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIe Functions",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/0-MLOM/PCIeFunctions/0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIe Function Collection"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/PCIeDevices/0-MLOM/PCIeFunctions/0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/0-MLOM/PCIeFunctions/0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0043",
    "Id": "0-MLOM",
    "Name": "Cisco Network controller",
    "SubsystemId": "0x02cf",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1137"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/PCIeDevices/MSTOR-RAID

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/MSTOR-RAID",
    "@odata.type": "#PCIeDevice.v1_5_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "Id": "MSTOR-RAID",
    "Name": "Cisco Boot Optimized M.2 RAID Controller",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/MSTOR-RAID/PCIeFunctions"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/PCIeDevices/MSTOR-RAID/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/MSTOR-RAID/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIe Functions",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/MSTOR-RAID/PCIeFunctions/0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIe Function Collection"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/PCIeDevices/MSTOR-RAID/PCIeFunctions/0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/MSTOR-RAID/PCIeFunctions/0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x9230",
    "Id": "MSTOR-RAID",
    "Name": "Cisco Boot Optimized M.2 RAID Controller",
    "SubsystemId": "0x0251",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1b4b"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Processors

```{
    "@odata.context": "/redfish/v1/$metadata#ProcessorCollection.ProcessorCollection",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Processors",
    "@odata.type": "#ProcessorCollection.ProcessorCollection",
    "Description": "Collection of Processors for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Processors/CPU1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Processors/CPU2"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Processors Collection"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Processors/CPU1

```{
    "@odata.context": "/redfish/v1/$metadata#Processor.Processor",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Processors/CPU1",
    "@odata.type": "#Processor.v1_10_0.Processor",
    "Id": "1",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) Gold 6348 CPU @ 2.60GHz",
    "Name": "CPU1",
    "OperatingSpeedMHz": 2600,
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "6",
        "EffectiveModel": "106",
        "Step": "6",
        "VendorId": "Intel(R) Corporation"
    },
    "ProcessorType": "CPU",
    "Socket": "CPU1",
    "Status": {
        "Health": "OK",
        "Health@Message.ExtendedInfo": [],
        "State": "Enabled"
    },
    "TotalCores": 28,
    "TotalEnabledCores": 4,
    "TotalThreads": 56
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Processors/CPU2

```{
    "@odata.context": "/redfish/v1/$metadata#Processor.Processor",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Processors/CPU2",
    "@odata.type": "#Processor.v1_10_0.Processor",
    "Id": "2",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) Gold 6348 CPU @ 2.60GHz",
    "Name": "CPU2",
    "OperatingSpeedMHz": 2600,
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "6",
        "EffectiveModel": "106",
        "Step": "6",
        "VendorId": "Intel(R) Corporation"
    },
    "ProcessorType": "CPU",
    "Socket": "CPU2",
    "Status": {
        "Health": "OK",
        "Health@Message.ExtendedInfo": [],
        "State": "Enabled"
    },
    "TotalCores": 28,
    "TotalEnabledCores": 4,
    "TotalThreads": 56
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/SimpleStorage

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorageCollection.SimpleStorageCollection",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/SimpleStorage",
    "@odata.type": "#SimpleStorageCollection.SimpleStorageCollection",
    "Description": "Collection of storage controllers for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/SimpleStorage/MSTOR-RAID"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Simple Storage Collection"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/SimpleStorage/MSTOR-RAID

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorage.SimpleStorage",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/SimpleStorage/MSTOR-RAID",
    "@odata.type": "#SimpleStorage.v1_2_1.SimpleStorage",
    "Description": "Simple Storage Controller",
    "Devices": [],
    "Id": "MSTOR-RAID",
    "Status": {}
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Storage

```{
    "@odata.context": "/redfish/v1/$metadata#StorageCollection.StorageCollection",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage",
    "@odata.type": "#StorageCollection.StorageCollection",
    "Description": "Collection of storage resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Storage Collection"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID

```{
    "@odata.context": "/redfish/v1/$metadata#Storage.Storage",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID",
    "@odata.type": "#Storage.v1_8_0.Storage",
    "Actions": {
        "Oem": {
            "#Cisco.DoForeignConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.DoForeignConfig",
                "ForeignCfgOp@Redfish.AllowableValues": [
                    "Clear",
                    "Import"
                ],
                "target": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Actions/Oem/Cisco.DoForeignConfig"
            }
        }
    },
    "Description": "Storage Controller",
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/253"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/254"
        }
    ],
    "Id": "MSTOR-RAID",
    "Links": {
        "Oem": {
            "Cisco": {
                "PCIeInfo": [
                    {
                        "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/MSTOR-RAID/PCIeFunctions/0"
                    }
                ]
            }
        }
    },
    "Name": "MSTOR-RAID",
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID",
            "FirmwareVersion": "2.3.17.1014",
            "Location": {
                "PartLocation": {
                    "LocationType": "Slot",
                    "ServiceLabel": "MSTOR-RAID"
                }
            },
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "MSTOR-RAID",
            "Model": "UCS-M2-HWRAID",
            "Name": "Cisco Boot optimized M.2 Raid controller",
            "Oem": {
                "Cisco": {
                    "ChipRevision": "V00",
                    "ControllerInterfaceType": "Sata",
                    "ControllerStatus": "Optimal",
                    "ControllerType": "M.2-Hwraid",
                    "DefaultStripeSizeKiBytes": 64,
                    "ForeignConfigPhysicalDriveCount": 0,
                    "HasForeignConfig": false,
                    "MaximumVolumesPerController": 1,
                    "PCIeSlot": "MSTOR-RAID",
                    "StorageControllerBiosVersion": "1.1.17.1002",
                    "StorageInstanceId": 2,
                    "SupportedStripeSizesKiBytes": [
                        32,
                        64
                    ]
                }
            },
            "SerialNumber": "FCH253574JR",
            "Status": {
                "Health": "OK",
                "HealthRollup": "OK",
                "State": "Enabled"
            },
            "SupportedControllerProtocols": [
                "PCIe"
            ],
            "SupportedDeviceProtocols": [
                "SATA"
            ],
            "SupportedRAIDTypes": [
                "RAID1"
            ]
        }
    ],
    "Volumes": {
        "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Volumes"
    }
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/253

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/253",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {}
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 6,
    "CapacityBytes": 240056795136,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "253",
    "IndicatorLED": "Off",
    "Manufacturer": "ATA",
    "MediaType": "SSD",
    "Model": "UCS-M2-240GB",
    "Name": "Micron_5100_MTFDDAV240TCB - 240GB M.2 6G SATA SSD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 240056795136,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 240056795136,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 68,
                "OperatingTemperatureInCel": 38,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 25,
                "PowerOnHours": 3734,
                "ThresholdOperatingTemperatureInCel": 75,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 253
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "253"
        }
    },
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "SATA",
    "Revision": "D0MH077",
    "SerialNumber": "MSA25230BH0",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/254

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/254",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {}
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 6,
    "CapacityBytes": 240056795136,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "254",
    "IndicatorLED": "Off",
    "Manufacturer": "ATA",
    "MediaType": "SSD",
    "Model": "UCS-M2-240GB",
    "Name": "Micron_5100_MTFDDAV240TCB - 240GB M.2 6G SATA SSD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 240056795136,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 240056795136,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 68,
                "OperatingTemperatureInCel": 37,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 25,
                "PowerOnHours": 3734,
                "ThresholdOperatingTemperatureInCel": 75,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 254
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "254"
        }
    },
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "SATA",
    "Revision": "D0MH077",
    "SerialNumber": "MSA25230BH7",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Volumes

```{
    "@odata.context": "/redfish/v1/$metadata#VolumeCollection.VolumeCollection",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection of Volumes for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Volumes/0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Volume Collection"
}
```

## /api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Volumes/0

```{
    "@odata.context": "/redfish/v1/$metadata#Volume.Volume",
    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Volumes/0",
    "@odata.type": "#Volume.v1_5_0.Volume",
    "Actions": {},
    "BlockSizeBytes": 512,
    "CapacityBytes": 239989686272,
    "Description": "Volume",
    "Encrypted": false,
    "Id": "0",
    "Identifiers": [
        {
            "DurableName": "0000000000000000db040e9f46720001 ",
            "DurableNameFormat": "UUID"
        }
    ],
    "Links": {
        "DedicatedSpareDrives": [],
        "DedicatedSpareDrives@odata.count": 0,
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/253"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/254"
            }
        ],
        "Drives@odata.count": 2,
        "Oem": {
            "Cisco": {
                "Spans": [
                    {
                        "DrivesList": [
                            {
                                "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/253"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/254"
                            }
                        ],
                        "DrivesList@odata.count": 2,
                        "SpanId": 0
                    }
                ],
                "Spans@odata.count": 1
            }
        },
        "SpareResourceSets": [],
        "SpareResourceSets@odata.count": 0
    },
    "Name": "MStorBootVd",
    "Oem": {
        "Cisco": {
            "AvailableSizeMiBytes": 0,
            "Bootable": true,
            "ConfiguredWriteCachePolicy": "WriteThrough",
            "FullDiskEncryptionCapable": false,
            "RequestedWriteCachePolicy": "WriteThrough",
            "VolumeAccessPolicy": "ReadWrite",
            "VolumeDriveCachePolicy": "NoChange",
            "VolumeIoPolicy": "DirectIo",
            "VolumeReadAheadPolicy": "NoReadAhead",
            "VolumeState": "Optimal"
        }
    },
    "OptimumIOSizeBytes": 65536,
    "RAIDType": "RAID1",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

