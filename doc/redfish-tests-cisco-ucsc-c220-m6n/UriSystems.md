# Resource: /redfish/v1/Systems

Vendor | Model
--- | ---
Cisco | UCSC-C220-M6N

## /redfish/v1/Systems

```{
    "@odata.context": "/redfish/v1/$metadata#ComputerSystemCollection.ComputerSystemCollection",
    "@odata.id": "/redfish/v1/Systems",
    "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection",
    "Description": "Collection of Computer Systems",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Computer System Collection"
}
```

## /redfish/v1/Systems/WZP262207W0

```{
    "@odata.context": "/redfish/v1/$metadata#ComputerSystem.ComputerSystem",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0",
    "@odata.type": "#ComputerSystem.v1_15_0.ComputerSystem",
    "Actions": {
        "#ComputerSystem.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff",
                "GracefulShutdown",
                "GracefulRestart",
                "ForceRestart",
                "Nmi",
                "PowerCycle"
            ],
            "target": "/redfish/v1/Systems/WZP262207W0/Actions/ComputerSystem.Reset"
        },
        "Oem": {
            "#CiscoUCSExtensions.ResetBIOSCMOS": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetBIOSCMOS",
                "target": "/redfish/v1/Systems/WZP262207W0/Actions/Oem/ComputerSystem.ResetBIOSCMOS"
            }
        }
    },
    "AssetTag": "Unknown",
    "Bios": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/Bios"
    },
    "BiosVersion": "C225M6.4.2.2b.0.0509222122",
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
    "EthernetInterfaces": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces"
    },
    "HostName": "C225-WZP262207W0",
    "HostWatchdogTimer": {
        "FunctionEnabled": false,
        "Status": {
            "State": "Disabled"
        },
        "TimeoutAction": "PowerDown",
        "WarningAction": "None"
    },
    "Id": "WZP262207W0",
    "IndicatorLED": "Off",
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
    "LocationIndicatorActive": false,
    "LogServices": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/LogServices"
    },
    "Manufacturer": "Cisco Systems Inc",
    "Memory": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory"
    },
    "MemoryDomains": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/MemoryDomains"
    },
    "MemorySummary": {
        "TotalSystemMemoryGiB": 512
    },
    "Model": "UCSC-C225-M6S",
    "Name": "UCS C225 M6S",
    "NetworkInterfaces": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/NetworkInterfaces"
    },
    "Oem": {
        "Cisco": {
            "FrontPanelButtonsLocked": false,
            "PostCompletionStatus": false,
            "SystemEffectiveMemory": 512,
            "SystemEffectiveSpeed": 3200
        }
    },
    "PCIeDevices": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MRAID"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MLOM"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MSTOR-RAID"
        }
    ],
    "PCIeDevices@odata.count": 5,
    "PCIeFunctions": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/1/PCIeFunctions/0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/3/PCIeFunctions/0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MRAID/PCIeFunctions/0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MLOM/PCIeFunctions/0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MSTOR-RAID/PCIeFunctions/0"
        }
    ],
    "PCIeFunctions@odata.count": 5,
    "PowerRestorePolicy": "AlwaysOff",
    "PowerState": "Off",
    "ProcessorSummary": {
        "CoreCount": 64,
        "Count": 1,
        "Model": "AMD EPYC 7763 64-Core Processor                "
    },
    "Processors": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/Processors"
    },
    "SecureBoot": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/SecureBoot"
    },
    "SerialNumber": "WZP262207W0",
    "SimpleStorage": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/SimpleStorage"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "Storage": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage"
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
                        "Model": "UCSX-TPM2-002B-C",
                        "OwnershipStatus": "Owned",
                        "Revision": 1,
                        "SerialNumber": "FCH262076S0"
                    }
                }
            },
            "Status": {
                "State": "Enabled"
            }
        }
    ],
    "UUID": "3FC6BE04-7B3E-4240-A269-D87F44A1F7DD"
}
```

## /redfish/v1/Systems/WZP262207W0/Bios

```{
    "@odata.context": "/redfish/v1/$metadata#Bios.Bios",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Bios",
    "@odata.type": "#Bios.v1_0_4.Bios",
    "Actions": {
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/WZP262207W0/Bios/Actions/Bios.ResetBios"
        }
    },
    "AttributeRegistry": "CiscoBiosAttributeRegistry.v1_0_0",
    "Attributes": {
        "BaudRate": "115.2k",
        "BmeDmaMitigation": "Disabled",
        "BurstAndPostponedRefresh": "Disabled",
        "CbsCmnApbdis": "Auto",
        "CbsCmnCpuCpb": "Auto",
        "CbsCmnCpuGenDowncoreCtrl": "Auto",
        "CbsCmnCpuGlobalCstateCtrl": "Auto",
        "CbsCmnCpuL1StreamHwPrefetcher": "Auto",
        "CbsCmnCpuL2StreamHwPrefetcher": "Auto",
        "CbsCmnCpuSmee": "Auto",
        "CbsCmnCpuStreamingStoresCtrl": "Auto",
        "CbsCmnDeterminismSlider": "Auto",
        "CbsCmnEfficiencyModeEn": "Auto",
        "CbsCmnFixedSocPstate": "Auto",
        "CbsCmnGnbNbIOMMU": "Auto",
        "CbsCmnGnbSMUCPPC": "Auto",
        "CbsCmnGnbSMUDfCstates": "Auto",
        "CbsCmnMemCtrlBankGroupSwapDdr4": "Auto",
        "CbsCmnMemMapBankInterleaveDdr4": "Auto",
        "CbsCpuCcdCtrlSsp": "Auto",
        "CbsCpuCoreCtrl": "Auto",
        "CbsCpuSmtCtrl": "Enabled",
        "CbsDbgCpuSnpMemCover": "Auto",
        "CbsDbgCpuSnpMemSizeCover": "0",
        "CbsDfCmnAcpiSratL3Numa": "Auto",
        "CbsDfCmnDramNps": "Auto",
        "CbsDfCmnMemIntlvSize": "Auto",
        "CbsSevSnpSupport": "Disabled",
        "CiscoDebugLevel": "Minimum",
        "CiscoOpromLaunchOptimization": "Enabled",
        "CiscoXgmiMaxSpeed": "Disabled",
        "ConsoleRedir": "Disabled",
        "FRB_2": "Enabled",
        "FlowCtrl": "None",
        "IPV4HTTP": "Enabled",
        "IPV4PXE": "Enabled",
        "IPV6HTTP": "Enabled",
        "IPV6PXE": "Disabled",
        "MemoryMappedIOAbove4GB": "Enabled",
        "NetworkStack": "Enabled",
        "OSBootWatchdogTimer": "Disabled",
        "OSBootWatchdogTimerPolicy": "Power Off",
        "OSBootWatchdogTimerTimeout": "10 minutes",
        "PcieARISupport": "Auto",
        "PcieSlot1LinkSpeed": "Auto",
        "PcieSlot1OptionROM": "Enabled",
        "PcieSlot3LinkSpeed": "Auto",
        "PcieSlot3OptionROM": "Enabled",
        "PcieSlotFrontNvme1LinkSpeed": "Auto",
        "PcieSlotFrontNvme1OptionROM": "Enabled",
        "PcieSlotFrontNvme2LinkSpeed": "Auto",
        "PcieSlotFrontNvme2OptionROM": "Enabled",
        "PcieSlotFrontNvme3LinkSpeed": "Auto",
        "PcieSlotFrontNvme3OptionROM": "Enabled",
        "PcieSlotFrontNvme4LinkSpeed": "Auto",
        "PcieSlotFrontNvme4OptionROM": "Enabled",
        "PcieSlotMLOMLinkSpeed": "Auto",
        "PcieSlotMLOMOptionROM": "Enabled",
        "PcieSlotMRAIDLinkSpeed": "Auto",
        "PcieSlotMRAIDOptionROM": "Enabled",
        "PcieSlotMSTORRAIDLinkSpeed": "Auto",
        "PcieSlotMSTORRAIDOptionROM": "Enabled",
        "PostPackageRepair": "Hard PPR",
        "PowerOnPassword": "Disabled",
        "SHA1PCRBank": "Enabled",
        "SHA256PCRBank": "Enabled",
        "SrIov": "Enabled",
        "SvmMode": "Enabled",
        "TPMControl": "Enabled",
        "TSME": "Auto",
        "TerminalType": "VT100",
        "cdnEnable": "Enabled"
    },
    "Description": "BIOS Configuration Current Settings",
    "Id": "BiosToken",
    "Name": "BiosToken"
}
```

## /redfish/v1/Systems/WZP262207W0/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Description": "Collection of EthernetInterfaces for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/MLOM.0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/MLOM.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.0"
        }
    ],
    "Members@odata.count": 6,
    "Name": "Ethernet Interfaces Collection"
}
```

## /redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.0

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.0",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "1.0",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3C:8B:7F:F3:29:CC",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3C:8B:7F:F3:29:CC"
}
```

## /redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "1.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3C:8B:7F:F3:29:CE",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3C:8B:7F:F3:29:CE"
}
```

## /redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.2

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "1.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3C:8B:7F:F3:29:CD",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3C:8B:7F:F3:29:CD"
}
```

## /redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.3

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.3",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "1.3",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3C:8B:7F:F3:29:CF",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3C:8B:7F:F3:29:CF"
}
```

## /redfish/v1/Systems/WZP262207W0/EthernetInterfaces/MLOM.0

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/MLOM.0",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "MLOM.0",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "04:BD:97:7B:67:AC",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "04:BD:97:7B:67:AC"
}
```

## /redfish/v1/Systems/WZP262207W0/EthernetInterfaces/MLOM.1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/MLOM.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "MLOM.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "04:BD:97:7B:67:AD",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "04:BD:97:7B:67:AD"
}
```

## /redfish/v1/Systems/WZP262207W0/LogServices

```
```

## /redfish/v1/Systems/WZP262207W0/Memory

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryCollection.MemoryCollection",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory",
    "@odata.type": "#MemoryCollection.MemoryCollection",
    "Description": "Collection of Memory resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_B2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_A2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_A2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_G1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_H1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_G1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_H2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_E2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_F2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_C1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_D2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_A1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_F1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_G2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_H1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_E2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_F1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_E1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_D1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_C2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_B2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_D1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_B1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_A1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_H2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_C1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_F2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_G2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_D2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_E1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_B1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_C2"
        }
    ],
    "Members@odata.count": 32,
    "Name": "Memory Collection"
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_A1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_A1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P1_A1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_A2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_A2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 65536,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_P1_A2",
    "Id": "2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xCE00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 0,
        "Slot": 1,
        "Socket": 0
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_P1_A2",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 3200,
    "PartNumber": "M393A8G40AB2-CWE    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "13F08E04",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_B1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_B1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "3",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P1_B1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_B2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_B2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 65536,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_P1_B2",
    "Id": "4",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xCE00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 1,
        "Slot": 1,
        "Socket": 0
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_P1_B2",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 3200,
    "PartNumber": "M393A8G40AB2-CWE    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "13F08E7A",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_C1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_C1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "5",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P1_C1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_C2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_C2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 65536,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_P1_C2",
    "Id": "6",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xCE00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 2,
        "Slot": 1,
        "Socket": 0
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_P1_C2",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 3200,
    "PartNumber": "M393A8G40AB2-CWE    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "13F08E78",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_D1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_D1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "7",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P1_D1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_D2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_D2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 65536,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_P1_D2",
    "Id": "8",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xCE00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 3,
        "Slot": 1,
        "Socket": 0
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_P1_D2",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 3200,
    "PartNumber": "M393A8G40AB2-CWE    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "13F08F2A",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_E1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_E1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "9",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P1_E1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_E2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_E2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 65536,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_P1_E2",
    "Id": "10",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xCE00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 4,
        "Slot": 1,
        "Socket": 0
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_P1_E2",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 3200,
    "PartNumber": "M393A8G40AB2-CWE    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "13F0A022",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_F1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_F1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "11",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P1_F1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_F2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_F2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 65536,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_P1_F2",
    "Id": "12",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xCE00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 5,
        "Slot": 1,
        "Socket": 0
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_P1_F2",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 3200,
    "PartNumber": "M393A8G40AB2-CWE    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "13F08E7B",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_G1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_G1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "13",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P1_G1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_G2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_G2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 65536,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_P1_G2",
    "Id": "14",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xCE00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 6,
        "Slot": 1,
        "Socket": 0
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_P1_G2",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 3200,
    "PartNumber": "M393A8G40AB2-CWE    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "13F08E03",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_H1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_H1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "15",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P1_H1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_H2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P1_H2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 65536,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_P1_H2",
    "Id": "16",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xCE00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 7,
        "Slot": 1,
        "Socket": 0
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_P1_H2",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 3200,
    "PartNumber": "M393A8G40AB2-CWE    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "13F08E08",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_A1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_A1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "17",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_A1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_A2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_A2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "18",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_A2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_B1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_B1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "19",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_B1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_B2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_B2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "20",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_B2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_C1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_C1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "21",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_C1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_C2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_C2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "22",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_C2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_D1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_D1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "23",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_D1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_D2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_D2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "24",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_D2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_E1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_E1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "25",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_E1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_E2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_E2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "26",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_E2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_F1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_F1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "27",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_F1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_F2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_F2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "28",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_F2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_G1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_G1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "29",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_G1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_G2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_G2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "30",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_G2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_H1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_H1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "31",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_H1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_H2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Memory/DIMM_P2_H2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "32",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_P2_H2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/MemoryDomains

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryDomainCollection.MemoryDomainCollection",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/MemoryDomains",
    "@odata.type": "#MemoryDomainCollection.MemoryDomainCollection",
    "Description": "Collection of Memory Domain resource instances for this system",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Memory Domain Collection"
}
```

## /redfish/v1/Systems/WZP262207W0/NetworkInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/NetworkInterfaces",
    "@odata.type": "#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "Description": "Collection of NetworkInterface resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/NetworkInterfaces/UCSC-PCIE-C25Q-04_FCH26277TA5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/NetworkInterfaces/UCSC-M-V100-04_FCH26147UVK"
        }
    ],
    "Members@odata.count": 2,
    "Name": "NetworkInterface Collection"
}
```

## /redfish/v1/Systems/WZP262207W0/NetworkInterfaces/UCSC-M-V100-04_FCH26147UVK

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterface.NetworkInterface",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/NetworkInterfaces/UCSC-M-V100-04_FCH26147UVK",
    "@odata.type": "#NetworkInterface.v1_1_1.NetworkInterface",
    "Description": "NetworkInterface contains references linking NetworkAdapter, NetworkPort, and NetworkDeviceFunction resources and represents the functionality available to the containing system.",
    "Id": "UCSC-M-V100-04_FCH26147UVK",
    "Links": {
        "NetworkAdapter": {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-M-V100-04_FCH26147UVK"
        }
    },
    "Name": "Adapter Card UCSC-M-V100-04_FCH26147UVK",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-M-V100-04_FCH26147UVK/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-M-V100-04_FCH26147UVK/NetworkPorts"
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/NetworkInterfaces/UCSC-PCIE-C25Q-04_FCH26277TA5

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterface.NetworkInterface",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/NetworkInterfaces/UCSC-PCIE-C25Q-04_FCH26277TA5",
    "@odata.type": "#NetworkInterface.v1_1_1.NetworkInterface",
    "Description": "NetworkInterface contains references linking NetworkAdapter, NetworkPort, and NetworkDeviceFunction resources and represents the functionality available to the containing system.",
    "Id": "UCSC-PCIE-C25Q-04_FCH26277TA5",
    "Links": {
        "NetworkAdapter": {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-PCIE-C25Q-04_FCH26277TA5"
        }
    },
    "Name": "Adapter Card UCSC-PCIE-C25Q-04_FCH26277TA5",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-PCIE-C25Q-04_FCH26277TA5/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-PCIE-C25Q-04_FCH26277TA5/NetworkPorts"
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/1

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/1",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "5.2(2b)",
    "Id": "1",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/1/PCIeFunctions/0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco UCS VIC 1455",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/1/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/1/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/1/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/1/PCIeFunctions/0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/1/PCIeFunctions/0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/1/PCIeFunctions/0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0042",
    "Id": "1",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.0"
            }
        ],
        "EthernetInterfaces@odata.count": 4,
        "NetworkDeviceFunctions": [],
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/1"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "Cisco UCS VIC 1455",
    "SubsystemId": "0x0217",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1137"
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/3

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/3",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "N/A",
    "Id": "3",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/3/PCIeFunctions/0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "NVIDIA T4 PCIe 16GB 70W",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/3/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/3/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/3/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/3/PCIeFunctions/0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/3/PCIeFunctions/0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/3/PCIeFunctions/0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1eb8",
    "Id": "3",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions": [],
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/3"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "NVIDIA T4 PCIe 16GB 70W",
    "SubsystemId": "0x12a2",
    "SubsystemVendorId": "0x10de",
    "VendorId": "0x10de"
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MLOM",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "5.2(2b)",
    "Id": "MLOM",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MLOM/PCIeFunctions/0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco UCS VIC 1477 MLOM",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MLOM/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/MLOM/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MLOM/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MLOM/PCIeFunctions/0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/MLOM/PCIeFunctions/0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MLOM/PCIeFunctions/0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0042",
    "Id": "MLOM",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/MLOM.0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/MLOM.1"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions": [],
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MLOM"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "Cisco UCS VIC 1477 MLOM",
    "SubsystemId": "0x02b0",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1137"
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MRAID",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "52.20.0-4432",
    "Id": "MRAID",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MRAID/PCIeFunctions/0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco 12G SAS RAID Controller with 4GB FBWC (16 Drives)",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MRAID/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/MRAID/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MRAID/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MRAID/PCIeFunctions/0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/MRAID/PCIeFunctions/0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MRAID/PCIeFunctions/0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x10e2",
    "Id": "MRAID",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/7"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/8"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/9"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/10"
            }
        ],
        "Drives@odata.count": 10,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions": [],
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MRAID"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "Cisco 12G SAS RAID Controller with 4GB FBWC (16 Drives)",
    "SubsystemId": "0x02a4",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1000"
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/MSTOR-RAID

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MSTOR-RAID",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "N/A",
    "Id": "MSTOR-RAID",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MSTOR-RAID/PCIeFunctions/0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco Boot optimized M.2 Raid controller",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MSTOR-RAID/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/MSTOR-RAID/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MSTOR-RAID/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MSTOR-RAID/PCIeFunctions/0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP262207W0/PCIeDevices/MSTOR-RAID/PCIeFunctions/0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MSTOR-RAID/PCIeFunctions/0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x9230",
    "Id": "MSTOR-RAID",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Drives/253"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Drives/254"
            }
        ],
        "Drives@odata.count": 2,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions": [],
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MSTOR-RAID"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "Cisco Boot optimized M.2 Raid controller",
    "SubsystemId": "0x0251",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1b4b"
}
```

## /redfish/v1/Systems/WZP262207W0/Processors

```{
    "@odata.context": "/redfish/v1/$metadata#ProcessorCollection.ProcessorCollection",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Processors",
    "@odata.type": "#ProcessorCollection.ProcessorCollection",
    "Description": "Collection of Processors for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Processors/CPU2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Processors/CPU1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Processors Collection"
}
```

## /redfish/v1/Systems/WZP262207W0/Processors/CPU1

```{
    "@odata.context": "/redfish/v1/$metadata#Processor.Processor",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Processors/CPU1",
    "@odata.type": "#Processor.v1_5_0.Processor",
    "Description": "AMD 2.45GHz 7763 280W 64C/256MB Cache DDR4 3200MHz",
    "Id": "1",
    "InstructionSet": "x86-64",
    "Manufacturer": "Advanced Micro Devices, Inc.",
    "MaxSpeedMHz": 3525,
    "Model": "AMD EPYC 7763 64-Core Processor                ",
    "Name": "CPU1",
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "19h",
        "EffectiveModel": "1",
        "Step": "1",
        "VendorId": "Advanced Micro Devices, Inc."
    },
    "ProcessorType": "CPU",
    "Socket": "CPU1",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TotalCores": 64,
    "TotalEnabledCores": 64,
    "TotalThreads": 128
}
```

## /redfish/v1/Systems/WZP262207W0/Processors/CPU2

```{
    "@odata.context": "/redfish/v1/$metadata#Processor.Processor",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Processors/CPU2",
    "@odata.type": "#Processor.v1_5_0.Processor",
    "Description": "Computer Processor",
    "Id": "2",
    "Name": "Computer Processor",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/SecureBoot

```{
    "@odata.context": "/redfish/v1/$metadata#SecureBoot.SecureBoot",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/SecureBoot",
    "@odata.type": "#SecureBoot.v1_0_4.SecureBoot",
    "Description": "UEFI SecureBoot configuration of this system",
    "Id": "SecureBoot",
    "Name": "SecureBoot",
    "SecureBootCurrentBoot": "Enabled",
    "SecureBootEnable": false
}
```

## /redfish/v1/Systems/WZP262207W0/SimpleStorage

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorageCollection.SimpleStorageCollection",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/SimpleStorage",
    "@odata.type": "#SimpleStorageCollection.SimpleStorageCollection",
    "Description": "Collection of storage controllers for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/SimpleStorage/MRAID"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/SimpleStorage/MSTOR-RAID"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Simple Storage Collection"
}
```

## /redfish/v1/Systems/WZP262207W0/SimpleStorage/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorage.SimpleStorage",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/SimpleStorage/MRAID",
    "@odata.type": "#SimpleStorage.v1_2_1.SimpleStorage",
    "Description": "Simple Storage Controller",
    "Id": "MRAID",
    "Name": "Cisco 12G SAS RAID Controller with 4GB FBWC (16 Drives)"
}
```

## /redfish/v1/Systems/WZP262207W0/SimpleStorage/MSTOR-RAID

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorage.SimpleStorage",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/SimpleStorage/MSTOR-RAID",
    "@odata.type": "#SimpleStorage.v1_2_1.SimpleStorage",
    "Description": "Simple Storage Controller",
    "Id": "MSTOR-RAID",
    "Name": "Cisco Boot optimized M.2 Raid controller"
}
```

## /redfish/v1/Systems/WZP262207W0/Storage

```null
```

## /redfish/v1/Systems/WZP262207W0/Storage/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#Storage.Storage",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID",
    "@odata.type": "#Storage.v1_8_0.Storage",
    "Actions": {
        "Oem": {
            "#Cisco.BbuStartLearnCycle": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.BbuStartLearnCycle",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Actions/Oem/Cisco.BbuStartLearnCycle"
            },
            "#Cisco.ClearConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ClearConfig",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Actions/Oem/Cisco.ClearConfig"
            },
            "#Cisco.DoForeignConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.DoForeignConfig",
                "ForeignCfgOp@Redfish.AllowableValues": [
                    "Clear",
                    "Import"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Actions/Oem/Cisco.DoForeignConfig"
            },
            "#Cisco.EncryptionOp": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.EncryptionOp",
                "DriveEncryptionModeRemote@Redfish.AllowableValues": [
                    true,
                    false
                ],
                "EnOpName@Redfish.AllowableValues": [
                    "Enable",
                    "Disable",
                    "Migrate",
                    "Modify",
                    "Unlock"
                ],
                "EncryptionKey@Redfish.AllowableValues": [
                    "A unique string generated by requester, min is 1 and max is 32"
                ],
                "KeyId@Redfish.AllowableValues": [
                    "A unique string generated by requester, min is 1 and max is 255"
                ],
                "NewEncryptionKey@Redfish.AllowableValues": [
                    "A unique string generated by requester, min is 1 and max is 32"
                ],
                "Remote@Redfish.AllowableValues": [
                    true,
                    false
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Actions/Oem/Cisco.EncryptionOp"
            },
            "#Cisco.GetLogs": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.GetLogs",
                "OutputFile@Redfish.AllowableValues": [
                    "A string of length between 1-64 alpha numeric characters for output file name"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Actions/Oem/Cisco.GetLogs"
            },
            "#Cisco.ResetToFactoryDefaults": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetToFactoryDefaults",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Actions/Oem/Cisco.ResetToFactoryDefaults"
            },
            "#Cisco.UnpinCache": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UnpinCache",
                "DiscardType@Redfish.AllowableValues": [
                    "all",
                    "missing"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Actions/Oem/Cisco.UnpinCache"
            }
        }
    },
    "Description": "Storage Controller",
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/7"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/8"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/9"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/10"
        }
    ],
    "Id": "MRAID",
    "Links": {
        "Oem": {
            "Cisco": {
                "PCIeInfo": [
                    {
                        "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MRAID/PCIeFunctions/0"
                    }
                ]
            }
        }
    },
    "Name": "MRAID",
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID",
            "CacheSummary": {
                "PersistentCacheSizeMiB": 0,
                "TotalCacheSizeMiB": 4096
            },
            "FirmwareVersion": "52.20.0-4432",
            "Location": {
                "PartLocation": {
                    "LocationType": "Slot",
                    "ServiceLabel": "MRAID"
                }
            },
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "MRAID",
            "Model": "UCSC-RAID-M6T",
            "Name": "Cisco 12G SAS RAID Controller with 4GB FBWC (16 Drives)",
            "Oem": {
                "Cisco": {
                    "Bbu": {
                        "BbuChargingState": "Unknown",
                        "BbuCurrentInAmps": 0,
                        "BbuDesignVoltageInVolts": 4.862,
                        "BbuDeviceName": "CVPM05",
                        "BbuManufacturingDate": "2021-09-09",
                        "BbuModuleVersion": "241-4GB",
                        "BbuSerialNumber": 4714,
                        "BbuStatus": "Optimal",
                        "BbuTemperatureInCel": 20,
                        "BbuType": "TMMC",
                        "BbuVendor": "LSI",
                        "BbuVoltageInVolts": 6.955,
                        "CapacitanceInPercent": 100,
                        "DesignCapacityInJoules": 92,
                        "IsBatteryPresent": true,
                        "IsCapacitor": true,
                        "IsLearnCycleRequested": false,
                        "IsLearnCycleTransparent": true,
                        "IsTemperatureHigh": false,
                        "IsVoltageLow": false,
                        "LearnCycleProgressEndTimeStamp": "0",
                        "LearnCycleProgressStartTimeStamp": "0",
                        "LearnCycleProgressStatus": "Success",
                        "LearnMode": "Auto",
                        "NextLearnCycleTimeStamp": "2022-12-05 16:16",
                        "PackEnergyInJoules": 172,
                        "RemainingPoolSpaceInPercent": 0
                    },
                    "BootDevices": [],
                    "ChipRevision": "00003",
                    "ConnectedSasExpander": true,
                    "ControllerEncryptionEnabled": false,
                    "ControllerInterfaceType": "Sas",
                    "ControllerStatus": "Optimal",
                    "ControllerType": "Raid",
                    "DefaultStripeSizeKiBytes": 64,
                    "EccBucketLeakRate": 1440,
                    "ForeignConfigPhysicalDriveCount": 0,
                    "FullDiskEncryptionCapable": true,
                    "HasForeignConfig": false,
                    "MaximumVolumesPerController": 240,
                    "MemoryCorrectableErrors": 0,
                    "PCIeSlot": "MRAID",
                    "PinnedCacheState": 0,
                    "RebuildRatePercent": 30,
                    "StorageControllerBiosVersion": "7.20.01.0_0x07140000",
                    "StorageControllerDefaultDriveMode": "UnConfiguredGood",
                    "StorageInstanceId": 2,
                    "SubOEMId": 0,
                    "SupportedStripeSizesKiBytes": [
                        64,
                        128,
                        256,
                        512,
                        1024
                    ]
                }
            },
            "SerialNumber": "SKB4401750",
            "Status": {
                "Health": "OK",
                "HealthRollup": "OK",
                "State": "Enabled"
            },
            "SupportedControllerProtocols": [
                "PCIe"
            ],
            "SupportedDeviceProtocols": [
                "SATA",
                "SAS"
            ],
            "SupportedRAIDTypes": [
                "RAID0",
                "RAID1",
                "RAID5",
                "RAID6",
                "RAID10",
                "RAID50",
                "RAID60"
            ]
        }
    ],
    "Volumes": {
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Volumes"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.Spindown": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spindown",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.Spindown"
            },
            "#Cisco.Spinup": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spinup",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.Spinup"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 6,
    "CapacityBytes": 1920383057920,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "1",
    "IndicatorLED": "Off",
    "Manufacturer": "ATA     ",
    "MediaType": "SSD",
    "Model": "UCS-SD19T61X-EV",
    "Name": "SAMSUNG MZ7LH1T9HMLT-00003 - 1.9TB 2.5 inch Enterprise Value 6G SATA SSD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1918999986176,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "UnConfiguredGood",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1919846187008,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 70,
                "OperatingTemperatureInCel": 23,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 41,
                "PowerOnHours": 27,
                "PowerOnHoursPercentage": 0,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 1
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "1"
        }
    },
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "SATA",
    "Revision": "HXT79F3Q",
    "SerialNumber": "S6MTNA0T107431      ",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/10

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/10",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Id": "10",
    "Name": "10",
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "10"
        }
    },
    "Status": {
        "Health": "OK",
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.Spindown": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spindown",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.Spindown"
            },
            "#Cisco.Spinup": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spinup",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.Spinup"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 6,
    "CapacityBytes": 1920383057920,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "2",
    "IndicatorLED": "Off",
    "Manufacturer": "ATA     ",
    "MediaType": "SSD",
    "Model": "UCS-SD19T61X-EV",
    "Name": "SAMSUNG MZ7LH1T9HMLT-00003 - 1.9TB 2.5 inch Enterprise Value 6G SATA SSD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1918999986176,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "UnConfiguredGood",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1919846187008,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 70,
                "OperatingTemperatureInCel": 23,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 41,
                "PowerOnHours": 27,
                "PowerOnHoursPercentage": 0,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 2
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "2"
        }
    },
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "SATA",
    "Revision": "HXT79F3Q",
    "SerialNumber": "S6MTNA0T107463      ",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.Spindown": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spindown",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.Spindown"
            },
            "#Cisco.Spinup": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spinup",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.Spinup"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 6,
    "CapacityBytes": 1920383057920,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "3",
    "IndicatorLED": "Off",
    "Manufacturer": "ATA     ",
    "MediaType": "SSD",
    "Model": "UCS-SD19T61X-EV",
    "Name": "SAMSUNG MZ7LH1T9HMLT-00003 - 1.9TB 2.5 inch Enterprise Value 6G SATA SSD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1918999986176,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "UnConfiguredGood",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1919846187008,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 70,
                "OperatingTemperatureInCel": 23,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 41,
                "PowerOnHours": 27,
                "PowerOnHoursPercentage": 0,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 3
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "3"
        }
    },
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "SATA",
    "Revision": "HXT79F3Q",
    "SerialNumber": "S6MTNA0T107461      ",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.Spindown": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spindown",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.Spindown"
            },
            "#Cisco.Spinup": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spinup",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.Spinup"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 6,
    "CapacityBytes": 1920383057920,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "4",
    "IndicatorLED": "Off",
    "Manufacturer": "ATA     ",
    "MediaType": "SSD",
    "Model": "UCS-SD19T61X-EV",
    "Name": "SAMSUNG MZ7LH1T9HMLT-00003 - 1.9TB 2.5 inch Enterprise Value 6G SATA SSD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1918999986176,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "UnConfiguredGood",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1919846187008,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 70,
                "OperatingTemperatureInCel": 23,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 41,
                "PowerOnHours": 27,
                "PowerOnHoursPercentage": 0,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 4
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "4"
        }
    },
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "SATA",
    "Revision": "HXT79F3Q",
    "SerialNumber": "S6MTNA0T107459      ",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/5

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/5",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Id": "5",
    "Name": "5",
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "5"
        }
    },
    "Status": {
        "Health": "OK",
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/6

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/6",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Id": "6",
    "Name": "6",
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "6"
        }
    },
    "Status": {
        "Health": "OK",
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/7

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/7",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Id": "7",
    "Name": "7",
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "7"
        }
    },
    "Status": {
        "Health": "OK",
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/8

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/8",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Id": "8",
    "Name": "8",
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "8"
        }
    },
    "Status": {
        "Health": "OK",
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/9

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/9",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Id": "9",
    "Name": "9",
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "9"
        }
    },
    "Status": {
        "Health": "OK",
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MRAID/Volumes

```{
    "@odata.context": "/redfish/v1/$metadata#VolumeCollection.VolumeCollection",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection of Volumes for this system",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Volume Collection"
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID

```{
    "@odata.context": "/redfish/v1/$metadata#Storage.Storage",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID",
    "@odata.type": "#Storage.v1_8_0.Storage",
    "Actions": {
        "Oem": {
            "#Cisco.DoForeignConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.DoForeignConfig",
                "ForeignCfgOp@Redfish.AllowableValues": [
                    "Clear",
                    "Import"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Actions/Oem/Cisco.DoForeignConfig"
            }
        }
    },
    "Description": "Storage Controller",
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Drives/253"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Drives/254"
        }
    ],
    "Id": "MSTOR-RAID",
    "Links": {
        "Oem": {
            "Cisco": {
                "PCIeInfo": [
                    {
                        "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MSTOR-RAID/PCIeFunctions/0"
                    }
                ]
            }
        }
    },
    "Name": "MSTOR-RAID",
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID",
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
                    "ChipRevision": "V02",
                    "ControllerInterfaceType": "Sata",
                    "ControllerStatus": "Optimal",
                    "ControllerType": "M.2-Hwraid",
                    "DefaultStripeSizeKiBytes": 64,
                    "ForeignConfigPhysicalDriveCount": 0,
                    "HasForeignConfig": false,
                    "MaximumVolumesPerController": 1,
                    "PCIeSlot": "MSTOR-RAID",
                    "StorageControllerBiosVersion": "1.1.17.1002",
                    "StorageControllerDefaultDriveMode": "Jbod",
                    "StorageInstanceId": 3,
                    "SupportedStripeSizesKiBytes": [
                        32,
                        64
                    ]
                }
            },
            "SerialNumber": "FCH262374RR",
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
        "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Volumes"
    }
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Drives/253

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Drives/253",
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
    "Name": "Micron_5300_MTFDDAV240TDS - 240GB SATA M.2",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 240056795136,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Jbod",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 240056795136,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 75,
                "OperatingTemperatureInCel": 42,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 20,
                "PowerOnHours": 62,
                "PowerOnHoursPercentage": 0,
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
    "Revision": "D3MC000",
    "SerialNumber": "MSY26191WKA",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Drives/254

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Drives/254",
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
    "Name": "Micron_5300_MTFDDAV240TDS - 240GB SATA M.2",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 240056795136,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Jbod",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 240056795136,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 75,
                "OperatingTemperatureInCel": 44,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 20,
                "PowerOnHours": 62,
                "PowerOnHoursPercentage": 0,
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
    "Revision": "D3MC000",
    "SerialNumber": "MSY26191Y04",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Volumes

```{
    "@odata.context": "/redfish/v1/$metadata#VolumeCollection.VolumeCollection",
    "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection of Volumes for this system",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Volume Collection"
}
```

