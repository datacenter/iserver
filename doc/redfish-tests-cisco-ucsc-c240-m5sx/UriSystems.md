# Resource: /redfish/v1/Systems

Vendor | Model
--- | ---
Cisco | UCSC-C240-M5SX

## /redfish/v1/Systems

```{
    "@odata.context": "/redfish/v1/$metadata#ComputerSystemCollection.ComputerSystemCollection",
    "@odata.id": "/redfish/v1/Systems",
    "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection",
    "Description": "Collection of Computer Systems",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Computer System Collection"
}
```

## /redfish/v1/Systems/WZP23450C8K

```{
    "@odata.context": "/redfish/v1/$metadata#ComputerSystem.ComputerSystem",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K",
    "@odata.type": "#ComputerSystem.v1_9_0.ComputerSystem",
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
            "target": "/redfish/v1/Systems/WZP23450C8K/Actions/ComputerSystem.Reset"
        },
        "Oem": {
            "#CiscoUCSExtensions.ResetBIOSCMOS": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetBIOSCMOS",
                "target": "/redfish/v1/Systems/WZP23450C8K/Actions/Oem/ComputerSystem.ResetBIOSCMOS"
            }
        }
    },
    "AssetTag": "02ACA39",
    "Bios": {
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Bios"
    },
    "BiosVersion": "C240M5.4.1.3i.0.0713210713",
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
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces"
    },
    "HostName": "aio3-p5g-eu-spdc-WZP23450C8K",
    "HostWatchdogTimer": {
        "FunctionEnabled": false,
        "Status": {
            "State": "Disabled"
        },
        "TimeoutAction": "PowerDown",
        "WarningAction": "None"
    },
    "Id": "WZP23450C8K",
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
    "LogServices": {
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/LogServices"
    },
    "Manufacturer": "Cisco Systems Inc",
    "Memory": {
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory"
    },
    "MemoryDomains": {
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/MemoryDomains"
    },
    "MemorySummary": {
        "Status": {
            "Health": "OK",
            "HealthRollup": "OK"
        },
        "TotalSystemMemoryGiB": 384
    },
    "Model": "UCSC-C240-M5SX",
    "Name": "UCS C240 M5SX",
    "NetworkInterfaces": {
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/NetworkInterfaces"
    },
    "Oem": {
        "Cisco": {
            "DimmBlacklistingEnabled": true,
            "FrontPanelButtonsLocked": false,
            "PostCompletionStatus": true,
            "SystemEffectiveMemory": 384,
            "SystemEffectiveSpeed": 2666
        }
    },
    "PCIeDevices": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MLOM"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MRAID"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/L"
        }
    ],
    "PCIeDevices@odata.count": 5,
    "PCIeFunctions": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/4/PCIeFunctions/4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/6/PCIeFunctions/6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MLOM/PCIeFunctions/MLOM"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MRAID/PCIeFunctions/MRAID"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/L/PCIeFunctions/L"
        }
    ],
    "PCIeFunctions@odata.count": 5,
    "PowerRestorePolicy": "AlwaysOff",
    "PowerState": "On",
    "ProcessorSummary": {
        "Count": 2,
        "Model": "Intel(R) Xeon(R) Platinum 8168 CPU @ 2.70GHz"
    },
    "Processors": {
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Processors"
    },
    "SecureBoot": {
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/SecureBoot"
    },
    "SerialNumber": "WZP23450C8K",
    "SimpleStorage": {
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/SimpleStorage"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "Storage": {
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage"
    },
    "SystemType": "Physical",
    "TrustedModules": [
        {
            "FirmwareVersion": "7.63",
            "InterfaceType": "TPM2_0",
            "InterfaceTypeSelection": "BiosSetting",
            "Oem": {
                "Cisco": {
                    "TPM": {
                        "Manufacturer": "Cisco Systems Inc",
                        "Model": "UCSX-TPM2-002",
                        "OwnershipStatus": "Unknown",
                        "Revision": 1,
                        "SerialNumber": "FCH2352747A"
                    }
                }
            },
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ],
    "UUID": "9A6D909E-F7C5-4481-BF21-424340DA652C"
}
```

## /redfish/v1/Systems/WZP23450C8K/Bios

```{
    "@odata.context": "/redfish/v1/$metadata#Bios.Bios",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Bios",
    "@odata.type": "#Bios.v1_0_4.Bios",
    "Actions": {
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/WZP23450C8K/Bios/Actions/Bios.ResetBios"
        }
    },
    "AttributeRegistry": "CiscoBiosAttributeRegistry.v1_0_0",
    "Attributes": {
        "ATS": "Enabled",
        "AdjacentCacheLinePrefetch": "Enabled",
        "AdvancedMemTest": "Auto",
        "AllLomPortControl": "Enabled",
        "AutoCCState": "Disabled",
        "BaudRate": "115.2k",
        "BmeDmaMitigation": "Disabled",
        "BootPerformanceMode": "Max Performance",
        "CPUPerformance": "Custom",
        "CRQos": "Disabled",
        "CiscoAdaptiveMemTraining": "Enabled",
        "CiscoDebugLevel": "Minimum",
        "CiscoOpromLaunchOptimization": "Enabled",
        "CoherencySupport": "Disabled",
        "ConfigTDPLevel": "Normal",
        "ConsoleRedir": "Disabled",
        "CoreMultiProcessing": "All",
        "CpuEngPerfBias": "Balanced Performance",
        "CpuHWPM": "HWPM Native Mode",
        "CrfastgoConfig": "Auto",
        "DCPMMFirmwareDowngrade": "Disabled",
        "DcuIpPrefetch": "Enabled",
        "DcuStreamerPrefetch": "Enabled",
        "EPPEnable": "Enabled",
        "EPPProfile": "Balanced Performance",
        "EnableClockSpreadSpec": "Enabled",
        "EnergyEfficientTurbo": "Disabled",
        "EnhancedIntelSpeedStep": "Enabled",
        "ExecuteDisable": "Enabled",
        "FRB_2": "Enabled",
        "FlowCtrl": "None",
        "HardwarePrefetch": "Enabled",
        "IMCInterleave": "Auto",
        "IPV4HTTP": "Disabled",
        "IPV4PXE": "Enabled",
        "IPV6HTTP": "Disabled",
        "IPV6PXE": "Disabled",
        "IntelHyperThread": "Enabled",
        "IntelSpeedSelect": "Base",
        "IntelTurboBoostTech": "Enabled",
        "IntelVT": "Enabled",
        "IntelVTD": "Enabled",
        "KTIPrefetch": "Enabled",
        "LLCPrefetch": "Disabled",
        "LocalX2Apic": "Disabled",
        "LomOpromControlPort0": "Enabled",
        "LomOpromControlPort1": "Enabled",
        "MemoryMappedIOAbove4GB": "Enabled",
        "MemoryRefreshRate": "1x Refresh",
        "MemorySizeLimit": "00000",
        "MemoryThermalThrottling": "CLTT with PECI",
        "NUMAOptimize": "Enabled",
        "NetworkStack": "Enabled",
        "NvmdimmPerformConfig": "BW Optimized",
        "OSBootWatchdogTimer": "Disabled",
        "OSBootWatchdogTimerPolicy": "Power Off",
        "OSBootWatchdogTimerTimeout": "10 minutes",
        "PCIeRASSupport": "Enabled",
        "PackageCstateLimit": "C0 C1 State",
        "PanicHighWatermark": "Low",
        "PartialMirrorModeConfig": "Disabled",
        "PartialMirrorPercent": "00.00",
        "PartialMirrorValue1": "0000",
        "PartialMirrorValue2": "0000",
        "PartialMirrorValue3": "0000",
        "PartialMirrorValue4": "0000",
        "PatrolScrub": "Enabled",
        "PciePllSsc": "Disabled",
        "PcieSlot1LinkSpeed": "Auto",
        "PcieSlot1OptionROM": "Enabled",
        "PcieSlot2LinkSpeed": "Auto",
        "PcieSlot2OptionROM": "Enabled",
        "PcieSlot3LinkSpeed": "Disabled",
        "PcieSlot3OptionROM": "Enabled",
        "PcieSlot4LinkSpeed": "Auto",
        "PcieSlot4OptionROM": "Enabled",
        "PcieSlot5LinkSpeed": "Auto",
        "PcieSlot5OptionROM": "Enabled",
        "PcieSlot6LinkSpeed": "Auto",
        "PcieSlot6OptionROM": "Enabled",
        "PcieSlotFrontNvme1LinkSpeed": "Disabled",
        "PcieSlotFrontNvme2LinkSpeed": "Disabled",
        "PcieSlotMLOMLinkSpeed": "Auto",
        "PcieSlotMLOMOptionROM": "Enabled",
        "PcieSlotMRAIDLinkSpeed": "Auto",
        "PcieSlotMRAIDOptionROM": "Enabled",
        "PcieSlotMSTORRAIDOptionROM": "Enabled",
        "PcieSlotN1OptionROM": "Enabled",
        "PcieSlotN2OptionROM": "Enabled",
        "PcieSlotRearNvme1LinkSpeed": "Disabled",
        "PcieSlotRearNvme1OptionRom": "Enabled",
        "PcieSlotRearNvme2LinkSpeed": "Disabled",
        "PcieSlotRearNvme2OptionRom": "Enabled",
        "PcieSlotsCdnEnable": "Disabled",
        "PowerOnPassword": "Disabled",
        "ProcessorC1E": "Disabled",
        "ProcessorC6Report": "Disabled",
        "ProcessorCMCI": "Enabled",
        "PsdCoordType": "HW ALL",
        "PwrPerfTuning": "OS",
        "QpiLinkSpeed": "Auto",
        "SHA1PCRBank": "Enabled",
        "SHA256PCRBank": "Enabled",
        "SNC": "Disabled",
        "SataModeSelect": "AHCI",
        "SelectMemoryRAS": "ADDDC Sparing",
        "SelectPprType": "Hard PPR",
        "SnoopyModeFor2LM": "Disabled",
        "SnoopyModeForAD": "Disabled",
        "TPMControl": "Enabled",
        "TXTSupport": "Disabled",
        "TerminalType": "VT100",
        "UFSDisable": "Enabled",
        "UsbLegacySupport": "Enabled",
        "UsbPortFront": "Enabled",
        "UsbPortInt": "Enabled",
        "UsbPortKVM": "Enabled",
        "UsbPortRear": "Enabled",
        "UsbPortSdCard": "Enabled",
        "VMDEnable": "Disabled",
        "VgaPriority": "Onboard",
        "WorkLdConfig": "IO Sensitive",
        "XPTPrefetch": "Auto",
        "cdnEnable": "Enabled",
        "pSATA": "LSI SW RAID"
    },
    "Description": "BIOS Configuration Current Settings",
    "Id": "BiosToken",
    "Name": "BiosToken"
}
```

## /redfish/v1/Systems/WZP23450C8K/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Description": "Collection of EthernetInterfaces for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/4.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/7.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/L.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/L.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/4.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/7.0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/6.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/6.2"
        }
    ],
    "Members@odata.count": 8,
    "Name": "Ethernet Interfaces Collection"
}
```

## /redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/4.1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/4.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "4.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:e2:ec:98",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:e2:ec:98"
}
```

## /redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/4.2

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/4.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "4.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:e2:ec:99",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:e2:ec:99"
}
```

## /redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/6.1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/6.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "6.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:e2:e6:60",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:e2:e6:60"
}
```

## /redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/6.2

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/6.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "6.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:e2:e6:61",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:e2:e6:61"
}
```

## /redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/7.0

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/7.0",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "7.0",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "7C:31:0E:ED:9A:60",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "7C:31:0E:ED:9A:60"
}
```

## /redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/7.1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/7.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "7.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "7C:31:0E:ED:9A:61",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "7C:31:0E:ED:9A:61"
}
```

## /redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/L.1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/L.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "L.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "5c:71:0d:c6:91:56",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "5c:71:0d:c6:91:56"
}
```

## /redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/L.2

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/L.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "L.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "5c:71:0d:c6:91:57",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "5c:71:0d:c6:91:57"
}
```

## /redfish/v1/Systems/WZP23450C8K/LogServices

```
```

## /redfish/v1/Systems/WZP23450C8K/Memory

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryCollection.MemoryCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory",
    "@odata.type": "#MemoryCollection.MemoryCollection",
    "Description": "Collection of Memory resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_J2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_D2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_C2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_E2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_B1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_A2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_L2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_K2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_H1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_M2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_J1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_G2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_D1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_C1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_E1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_F2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_A1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_B2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_K1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_L1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_M1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_F1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_G1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_H2"
        }
    ],
    "Members@odata.count": 24,
    "Name": "Memory Collection"
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_A1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_A1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_A1",
    "Id": "1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xAD00",
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
    "Name": "DIMM_A1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2666,
    "PartNumber": "HMA84GR7CJR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "834C0F26",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_A2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_A2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_A2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_B1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_B1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_B1",
    "Id": "3",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xAD00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 1,
        "Slot": 0,
        "Socket": 0
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_B1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2666,
    "PartNumber": "HMA84GR7CJR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "834C0FBB",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_B2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_B2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "4",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_B2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_C1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_C1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_C1",
    "Id": "5",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xAD00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 2,
        "Slot": 0,
        "Socket": 0
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_C1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2666,
    "PartNumber": "HMA84GR7CJR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "834C0F27",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_C2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_C2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "6",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_C2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_D1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_D1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_D1",
    "Id": "7",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xAD00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 3,
        "Slot": 0,
        "Socket": 0
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_D1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2666,
    "PartNumber": "HMA84GR7CJR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "834C0F1D",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_D2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_D2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "8",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_D2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_E1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_E1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_E1",
    "Id": "9",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xAD00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 4,
        "Slot": 0,
        "Socket": 0
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_E1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2666,
    "PartNumber": "HMA84GR7CJR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "834C106E",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_E2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_E2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "10",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_E2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_F1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_F1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_F1",
    "Id": "11",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xAD00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 5,
        "Slot": 0,
        "Socket": 0
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_F1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2666,
    "PartNumber": "HMA84GR7CJR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "834C0F1C",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_F2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_F2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "12",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_F2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_G1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_G1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_G1",
    "Id": "13",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xAD00",
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
    "Name": "DIMM_G1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2666,
    "PartNumber": "HMA84GR7CJR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "834C0FE6",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_G2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_G2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "14",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_G2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_H1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_H1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_H1",
    "Id": "15",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xAD00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 1,
        "Slot": 0,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_H1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2666,
    "PartNumber": "HMA84GR7CJR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "834C101B",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_H2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_H2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "16",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_H2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_J1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_J1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_J1",
    "Id": "17",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xAD00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 2,
        "Slot": 0,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_J1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2666,
    "PartNumber": "HMA84GR7CJR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "834C1076",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_J2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_J2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "18",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_J2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_K1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_K1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_K1",
    "Id": "19",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xAD00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 3,
        "Slot": 0,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_K1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2666,
    "PartNumber": "HMA84GR7CJR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "834C0F66",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_K2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_K2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "20",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_K2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_L1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_L1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_L1",
    "Id": "21",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xAD00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 4,
        "Slot": 0,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_L1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2666,
    "PartNumber": "HMA84GR7CJR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "834C0F70",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_L2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_L2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "22",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_L2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_M1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_M1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_M1",
    "Id": "23",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xAD00",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 5,
        "Slot": 0,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "DIMM_M1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2666,
    "PartNumber": "HMA84GR7CJR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "834C1078",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Memory/DIMM_M2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Memory/DIMM_M2",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "24",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_M2",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/MemoryDomains

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryDomainCollection.MemoryDomainCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/MemoryDomains",
    "@odata.type": "#MemoryDomainCollection.MemoryDomainCollection",
    "Description": "Collection of Memory Domain resource instances for this system",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Memory Domain Collection"
}
```

## /redfish/v1/Systems/WZP23450C8K/NetworkInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/NetworkInterfaces",
    "@odata.type": "#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "Description": "Collection of NetworkInterface resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/NetworkInterfaces/UCSC-MLOM-C40Q-03_FCH23507ASW"
        }
    ],
    "Members@odata.count": 1,
    "Name": "NetworkInterface Collection"
}
```

## /redfish/v1/Systems/WZP23450C8K/NetworkInterfaces/UCSC-MLOM-C40Q-03_FCH23507ASW

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterface.NetworkInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/NetworkInterfaces/UCSC-MLOM-C40Q-03_FCH23507ASW",
    "@odata.type": "#NetworkInterface.v1_1_1.NetworkInterface",
    "Description": "NetworkInterface contains references linking NetworkAdapter, NetworkPort, and NetworkDeviceFunction resources and represents the functionality available to the containing system.",
    "Id": "UCSC-MLOM-C40Q-03_FCH23507ASW",
    "Links": {
        "NetworkAdapter": {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C40Q-03_FCH23507ASW"
        }
    },
    "Name": "Adapter Card UCSC-MLOM-C40Q-03_FCH23507ASW",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C40Q-03_FCH23507ASW/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C40Q-03_FCH23507ASW/NetworkPorts"
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/4

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/4",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80009E5A-1.823.2",
    "Id": "4",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/4/PCIeFunctions/4"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel XL710-QDA2 Dual Port 40Gb QSFP converged NIC",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/4/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/4/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/4/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/4/PCIeFunctions/4"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/4/PCIeFunctions/4

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/4/PCIeFunctions/4",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1583",
    "Id": "4",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/4.2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/4.1"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/4"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel XL710-QDA2 Dual Port 40Gb QSFP converged NIC",
    "SubsystemId": "0x013c",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/6

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/6",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80009E5A-1.823.2",
    "Id": "6",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/6/PCIeFunctions/6"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel XL710-QDA2 Dual Port 40Gb QSFP converged NIC",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/6/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/6/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/6/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/6/PCIeFunctions/6"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/6/PCIeFunctions/6

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/6/PCIeFunctions/6",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1583",
    "Id": "6",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/6.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/6.2"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/6"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel XL710-QDA2 Dual Port 40Gb QSFP converged NIC",
    "SubsystemId": "0x013c",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/L

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/L",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80001516-1.823.2",
    "Id": "L",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/L/PCIeFunctions/L"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel X550 LOM",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/L/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/L/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/L/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/L/PCIeFunctions/L"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/L/PCIeFunctions/L

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/L/PCIeFunctions/L",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1563",
    "Id": "L",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/L.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/EthernetInterfaces/L.2"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/L"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel X550 LOM",
    "SubsystemId": "0x01a4",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MLOM",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "N/A",
    "Id": "MLOM",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MLOM/PCIeFunctions/MLOM"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco UCS VIC 1387 MLOM",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MLOM/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/MLOM/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MLOM/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MLOM/PCIeFunctions/MLOM"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/MLOM/PCIeFunctions/MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MLOM/PCIeFunctions/MLOM",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0042",
    "Id": "MLOM",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C40Q-03_FCH23507ASW/NetworkDeviceFunctions/eth0"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C40Q-03_FCH23507ASW/NetworkDeviceFunctions/eth1"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C40Q-03_FCH23507ASW/NetworkDeviceFunctions/fc0"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C40Q-03_FCH23507ASW/NetworkDeviceFunctions/fc1"
            }
        ],
        "NetworkDeviceFunctions@odata.count": 4,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MLOM"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Cisco UCS VIC 1387 MLOM",
    "SubsystemId": "0x015d",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1137"
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MRAID",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "51.10.0-3612",
    "Id": "MRAID",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MRAID/PCIeFunctions/MRAID"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco 12G Modular Raid Controller with 4GB cache (max 26 drives)",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MRAID/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/MRAID/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MRAID/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MRAID/PCIeFunctions/MRAID"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeDevices/MRAID/PCIeFunctions/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MRAID/PCIeFunctions/MRAID",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0016",
    "Id": "MRAID",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/7"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/8"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/9"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/10"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/11"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/12"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/13"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/14"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/15"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/16"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/17"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/18"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/19"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/20"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/21"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/22"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/23"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/24"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/25"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/26"
            }
        ],
        "Drives@odata.count": 26,
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeDevices/MRAID"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "Cisco 12G Modular Raid Controller with 4GB cache (max 26 drives)",
    "SubsystemId": "0x0210",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1000"
}
```

## /redfish/v1/Systems/WZP23450C8K/PCIeFunctions/MRAID

```null
```

## /redfish/v1/Systems/WZP23450C8K/Processors

```{
    "@odata.context": "/redfish/v1/$metadata#ProcessorCollection.ProcessorCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Processors",
    "@odata.type": "#ProcessorCollection.ProcessorCollection",
    "Description": "Collection of Processors for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Processors/CPU2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Processors/CPU1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Processors Collection"
}
```

## /redfish/v1/Systems/WZP23450C8K/Processors/CPU1

```{
    "@odata.context": "/redfish/v1/$metadata#Processor.Processor",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Processors/CPU1",
    "@odata.type": "#Processor.v1_5_0.Processor",
    "Description": "Intel(R) Xeon(R) Platinum 8168 2.70 GHz 205W 24C 33.00MB Cache DDR4 2666MHz 768GB",
    "Id": "1",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) Platinum 8168 CPU @ 2.70GHz",
    "Name": "CPU1",
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "6",
        "EffectiveModel": "85",
        "Step": "4",
        "VendorId": "Intel(R) Corporation"
    },
    "ProcessorType": "CPU",
    "Socket": "CPU1",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TotalCores": 24,
    "TotalEnabledCores": 24,
    "TotalThreads": 24
}
```

## /redfish/v1/Systems/WZP23450C8K/Processors/CPU2

```{
    "@odata.context": "/redfish/v1/$metadata#Processor.Processor",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Processors/CPU2",
    "@odata.type": "#Processor.v1_5_0.Processor",
    "Description": "Intel(R) Xeon(R) Platinum 8168 2.70 GHz 205W 24C 33.00MB Cache DDR4 2666MHz 768GB",
    "Id": "2",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) Platinum 8168 CPU @ 2.70GHz",
    "Name": "CPU2",
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "6",
        "EffectiveModel": "85",
        "Step": "4",
        "VendorId": "Intel(R) Corporation"
    },
    "ProcessorType": "CPU",
    "Socket": "CPU2",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TotalCores": 24,
    "TotalEnabledCores": 24,
    "TotalThreads": 24
}
```

## /redfish/v1/Systems/WZP23450C8K/SecureBoot

```{
    "@odata.context": "/redfish/v1/$metadata#SecureBoot.SecureBoot",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/SecureBoot",
    "@odata.type": "#SecureBoot.v1_0_4.SecureBoot",
    "Description": "UEFI SecureBoot configuration of this system",
    "Id": "SecureBoot",
    "Name": "SecureBoot",
    "SecureBootCurrentBoot": "Enabled",
    "SecureBootEnable": false
}
```

## /redfish/v1/Systems/WZP23450C8K/SimpleStorage

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorageCollection.SimpleStorageCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/SimpleStorage",
    "@odata.type": "#SimpleStorageCollection.SimpleStorageCollection",
    "Description": "Collection of storage controllers for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/SimpleStorage/MRAID"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Simple Storage Collection"
}
```

## /redfish/v1/Systems/WZP23450C8K/SimpleStorage/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorage.SimpleStorage",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/SimpleStorage/MRAID",
    "@odata.type": "#SimpleStorage.v1_2_1.SimpleStorage",
    "Description": "Simple Storage Controller",
    "Devices": [],
    "Id": "MRAID",
    "Name": "Cisco 12G Modular Raid Controller with 4GB cache (max 26 drives)",
    "Status": {}
}
```

## /redfish/v1/Systems/WZP23450C8K/Storage

```{
    "@odata.context": "/redfish/v1/$metadata#StorageCollection.StorageCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage",
    "@odata.type": "#StorageCollection.StorageCollection",
    "Description": "Collection of storage resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Storage Collection"
}
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#Storage.Storage",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID",
    "@odata.type": "#Storage.v1_8_0.Storage",
    "Actions": {
        "Oem": {
            "#Cisco.BbuStartLearnCycle": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.BbuStartLearnCycle",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Actions/Oem/Cisco.BbuStartLearnCycle"
            },
            "#Cisco.ClearConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ClearConfig",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Actions/Oem/Cisco.ClearConfig"
            },
            "#Cisco.DoForeignConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.DoForeignConfig",
                "ForeignCfgOp@Redfish.AllowableValues": [
                    "Clear",
                    "Import"
                ],
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Actions/Oem/Cisco.DoForeignConfig"
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
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Actions/Oem/Cisco.EncryptionOp"
            },
            "#Cisco.GetLogs": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.GetLogs",
                "OutputFile@Redfish.AllowableValues": [
                    "A string of length between 1-64 alpha numeric characters for output file name"
                ],
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Actions/Oem/Cisco.GetLogs"
            },
            "#Cisco.ResetToFactoryDefaults": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetToFactoryDefaults",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Actions/Oem/Cisco.ResetToFactoryDefaults"
            },
            "#Cisco.UnpinCache": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UnpinCache",
                "DiscardType@Redfish.AllowableValues": [
                    "all",
                    "missing"
                ],
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Actions/Oem/Cisco.UnpinCache"
            }
        }
    },
    "Description": "Storage Controller",
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/22"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/23"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/24"
        }
    ],
    "Id": "MRAID",
    "Links": {
        "Oem": {
            "Cisco": {
                "PCIeInfo": [
                    {
                        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/PCIeFunctions/MRAID"
                    }
                ]
            }
        }
    },
    "Name": "MRAID",
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID",
            "CacheSummary": {
                "PersistentCacheSizeMiB": 0,
                "TotalCacheSizeMiB": 4096
            },
            "FirmwareVersion": "51.10.0-3612",
            "Location": {
                "PartLocation": {
                    "LocationType": "Slot",
                    "ServiceLabel": "MRAID"
                }
            },
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "MRAID",
            "Model": "UCSC-RAID-M5HD",
            "Name": "Cisco 12G Modular Raid Controller with 4GB cache (max 26 drives)",
            "Oem": {
                "Cisco": {
                    "Bbu": {
                        "BbuChargingState": "Unknown",
                        "BbuCurrentInAmps": 0,
                        "BbuDesignVoltageInVolts": 9.5,
                        "BbuDeviceName": "CVPM05",
                        "BbuManufacturingDate": "2019-12-06",
                        "BbuModuleVersion": "06590-01",
                        "BbuSerialNumber": 38868,
                        "BbuStatus": "Optimal",
                        "BbuTemperatureInCel": 20,
                        "BbuType": "TMMC",
                        "BbuVendor": "LSI",
                        "BbuVoltageInVolts": 12.467,
                        "CapacitanceInPercent": 100,
                        "DesignCapacityInJoules": 306,
                        "IsBatteryPresent": true,
                        "IsCapacitor": true,
                        "IsLearnCycleRequested": false,
                        "IsLearnCycleTransparent": true,
                        "IsTemperatureHigh": false,
                        "IsVoltageLow": false,
                        "LearnCycleProgressEndTimeStamp": "1669154183",
                        "LearnCycleProgressStartTimeStamp": "1669154055",
                        "LearnCycleProgressStatus": "Success",
                        "LearnMode": "Auto",
                        "NextLearnCycleTimeStamp": "2022-12-20 20:54",
                        "PackEnergyInJoules": 629,
                        "RemainingPoolSpaceInPercent": 0
                    },
                    "BootDevices": [
                        "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/22"
                    ],
                    "ChipRevision": "04005",
                    "ConnectedSasExpander": true,
                    "ControllerEncryptionEnabled": false,
                    "ControllerInterfaceType": "Sas",
                    "ControllerStatus": "Optimal",
                    "ControllerType": "Raid",
                    "DefaultStripeSizeKiBytes": 64,
                    "EccBucketLeakRate": 1440,
                    "FullDiskEncryptionCapable": true,
                    "HasForeignConfig": false,
                    "JbodMode": true,
                    "MaximumVolumesPerController": 64,
                    "MemoryCorrectableErrors": 0,
                    "PCIeSlot": "MRAID",
                    "PinnedCacheState": 0,
                    "RebuildRatePercent": 30,
                    "StorageControllerBiosVersion": "7.10.03.1_0x070A0402",
                    "StorageControllerDefaultDriveMode": "UnConfiguredGood",
                    "StorageInstanceId": 8,
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
            "SerialNumber": "SK94286040",
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
        "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Volumes"
    }
}
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/1

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/1",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/1/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/1/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/1/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/1/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/1/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/1/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 800165199872,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "1",
    "IndicatorLED": "Off",
    "Manufacturer": "TOSHIBA ",
    "MediaType": "SSD",
    "Model": "UCS-SD800G123X-EP",
    "Name": "KPM51VUG800G - 800GB 2.5inch Enterprise performance 12G SAS SSD (3X DWPD)",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 798999183360,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Jbod",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 799628328960,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "PercentLifeLeft": 100,
                "PowerOnHours": 14516,
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
    "Protocol": "SAS",
    "Revision": "0108",
    "SerialNumber": "Y9B0A00LTSMF",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/10

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/11

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/12

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/13

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/14

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/15

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/16

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/17

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/18

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/19

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/2

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/2",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/2/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/2/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/2/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/2/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/2/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/2/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 800165199872,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "2",
    "IndicatorLED": "Off",
    "Manufacturer": "TOSHIBA ",
    "MediaType": "SSD",
    "Model": "UCS-SD800G123X-EP",
    "Name": "KPM51VUG800G - 800GB 2.5inch Enterprise performance 12G SAS SSD (3X DWPD)",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 798999183360,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Jbod",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 799628328960,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "PercentLifeLeft": 100,
                "PowerOnHours": 9257,
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
    "Protocol": "SAS",
    "Revision": "0108",
    "SerialNumber": "Y9B0A00VTSMF",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/20

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/21

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/22

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/22",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/22/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/22/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/22/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/22/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/22/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/22/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 800165199872,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "22",
    "IndicatorLED": "Off",
    "Manufacturer": "TOSHIBA ",
    "MediaType": "SSD",
    "Model": "UCS-SD800G123X-EP",
    "Name": "KPM51VUG800G - 800GB 2.5inch Enterprise performance 12G SAS SSD (3X DWPD)",
    "Oem": {
        "Cisco": {
            "Bootable": true,
            "CoercedSizeBytes": 798999183360,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Jbod",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 799628328960,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "PercentLifeLeft": 100,
                "PowerOnHours": 9257,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 22
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "22"
        }
    },
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "SAS",
    "Revision": "0108",
    "SerialNumber": "Y9B0A00CTSMF",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/23

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/23",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/23/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/23/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/23/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/23/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/23/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/23/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 800165199872,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "23",
    "IndicatorLED": "Off",
    "Manufacturer": "TOSHIBA ",
    "MediaType": "SSD",
    "Model": "UCS-SD800G123X-EP",
    "Name": "KPM51VUG800G - 800GB 2.5inch Enterprise performance 12G SAS SSD (3X DWPD)",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 798999183360,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Jbod",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 799628328960,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "PercentLifeLeft": 100,
                "PowerOnHours": 14516,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 23
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "23"
        }
    },
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "SAS",
    "Revision": "0108",
    "SerialNumber": "Y9B0A00NTSMF",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/24

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/24",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/24/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/24/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/24/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/24/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/24/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/24/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 800165199872,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "24",
    "IndicatorLED": "Off",
    "Manufacturer": "TOSHIBA ",
    "MediaType": "SSD",
    "Model": "UCS-SD800G123X-EP",
    "Name": "KPM51VUG800G - 800GB 2.5inch Enterprise performance 12G SAS SSD (3X DWPD)",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 798999183360,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Jbod",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 799628328960,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "PercentLifeLeft": 100,
                "PowerOnHours": 9257,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 24
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "24"
        }
    },
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "SAS",
    "Revision": "0108",
    "SerialNumber": "Y9B0A00STSMF",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/25

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/26

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/3

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/4

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/5

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/6

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/7

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/8

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/9

```null
```

## /redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Volumes

```{
    "@odata.context": "/redfish/v1/$metadata#VolumeCollection.VolumeCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection of Volumes for this system",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Volume Collection"
}
```

