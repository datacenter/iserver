# Resource: /redfish/v1/Systems

Vendor | Model
--- | ---
Cisco | UCSC-C240-M5SN

## /redfish/v1/Systems

```{
    "@odata.context": "/redfish/v1/$metadata#ComputerSystemCollection.ComputerSystemCollection",
    "@odata.id": "/redfish/v1/Systems",
    "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection",
    "Description": "Collection of Computer Systems",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Computer System Collection"
}
```

## /redfish/v1/Systems/WZP23400AK4

```{
    "@odata.context": "/redfish/v1/$metadata#ComputerSystem.ComputerSystem",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4",
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
            "target": "/redfish/v1/Systems/WZP23400AK4/Actions/ComputerSystem.Reset"
        },
        "Oem": {
            "#CiscoUCSExtensions.ResetBIOSCMOS": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetBIOSCMOS",
                "target": "/redfish/v1/Systems/WZP23400AK4/Actions/Oem/ComputerSystem.ResetBIOSCMOS"
            }
        }
    },
    "AssetTag": "022C2F7",
    "Bios": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Bios"
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
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces"
    },
    "HostName": "comp-2-p2b-eu-spdc-WZP23400AK4",
    "HostWatchdogTimer": {
        "FunctionEnabled": false,
        "Status": {
            "State": "Disabled"
        },
        "TimeoutAction": "PowerDown",
        "WarningAction": "None"
    },
    "Id": "WZP23400AK4",
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
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/LogServices"
    },
    "Manufacturer": "Cisco Systems Inc",
    "Memory": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory"
    },
    "MemoryDomains": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/MemoryDomains"
    },
    "MemorySummary": {
        "Status": {
            "Health": "OK",
            "HealthRollup": "OK"
        },
        "TotalSystemMemoryGiB": 384
    },
    "Model": "UCSC-C240-M5SN",
    "Name": "UCS C240 M5SN",
    "NetworkInterfaces": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/NetworkInterfaces"
    },
    "Oem": {
        "Cisco": {
            "DimmBlacklistingEnabled": true,
            "FrontPanelButtonsLocked": false,
            "PostCompletionStatus": true,
            "SystemEffectiveMemory": 384,
            "SystemEffectiveSpeed": 2933
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
    "PCIeDevices@odata.count": 5,
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
    "PCIeFunctions@odata.count": 5,
    "PowerRestorePolicy": "AlwaysOff",
    "PowerState": "On",
    "ProcessorSummary": {
        "Count": 2,
        "Model": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz"
    },
    "Processors": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Processors"
    },
    "SecureBoot": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/SecureBoot"
    },
    "SerialNumber": "WZP23400AK4",
    "SimpleStorage": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/SimpleStorage"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "Storage": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage"
    },
    "SystemType": "Physical",
    "TrustedModules": [
        {
            "Oem": {
                "Cisco": {
                    "TPM": null
                }
            },
            "Status": {
                "State": "Absent"
            }
        }
    ],
    "UUID": "B813910F-BFD2-439F-9C3B-75B376C5B160"
}
```

## /redfish/v1/Systems/WZP23400AK4/Bios

```{
    "@odata.context": "/redfish/v1/$metadata#Bios.Bios",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Bios",
    "@odata.type": "#Bios.v1_0_4.Bios",
    "Actions": {
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/WZP23400AK4/Bios/Actions/Bios.ResetBios"
        }
    },
    "AttributeRegistry": "CiscoBiosAttributeRegistry.v1_0_0",
    "Attributes": {
        "ATS": "Enabled",
        "AdjacentCacheLinePrefetch": "Disabled",
        "AdvancedMemTest": "Auto",
        "AllLomPortControl": "Enabled",
        "AutoCCState": "Disabled",
        "BaudRate": "115.2k",
        "BmeDmaMitigation": "Disabled",
        "BootPerformanceMode": "Max Performance",
        "CPUPerformance": "High Throughput",
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
        "DcuStreamerPrefetch": "Disabled",
        "EPPEnable": "Enabled",
        "EPPProfile": "Balanced Performance",
        "EnableClockSpreadSpec": "Enabled",
        "EnergyEfficientTurbo": "Disabled",
        "EnhancedIntelSpeedStep": "Enabled",
        "ExecuteDisable": "Enabled",
        "FRB_2": "Enabled",
        "FlowCtrl": "None",
        "HardwarePrefetch": "Disabled",
        "IMCInterleave": "Auto",
        "IPV4HTTP": "Disabled",
        "IPV4PXE": "Enabled",
        "IPV6HTTP": "Disabled",
        "IPV6PXE": "Disabled",
        "IntelHyperThread": "Enabled",
        "IntelSpeedSelect": "Base",
        "IntelTurboBoostTech": "Disabled",
        "IntelVT": "Enabled",
        "IntelVTD": "Enabled",
        "KTIPrefetch": "Enabled",
        "LLCPrefetch": "Disabled",
        "LocalX2Apic": "Disabled",
        "LomOpromControlPort0": "Disabled",
        "LomOpromControlPort1": "Disabled",
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
        "PcieSlot3LinkSpeed": "Auto",
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
        "PcieSlotN3OptionROM": "Enabled",
        "PcieSlotN4OptionROM": "Enabled",
        "PcieSlotN5OptionROM": "Enabled",
        "PcieSlotN6OptionROM": "Enabled",
        "PcieSlotN7OptionROM": "Enabled",
        "PcieSlotN8OptionROM": "Enabled",
        "PcieSlotRearNvme1LinkSpeed": "Auto",
        "PcieSlotRearNvme1OptionRom": "Enabled",
        "PcieSlotRearNvme2LinkSpeed": "Auto",
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
        "TPMControl": "Disabled",
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

## /redfish/v1/Systems/WZP23400AK4/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Description": "Collection of EthernetInterfaces for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/3.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/7.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/3.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/L.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/L.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/6.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/7.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/7.0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/6.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/7.3"
        }
    ],
    "Members@odata.count": 10,
    "Name": "Ethernet Interfaces Collection"
}
```

## /redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/3.1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/3.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "3.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ee:2a:4c",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ee:2a:4c"
}
```

## /redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/3.2

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/3.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "3.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ee:2a:4d",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ee:2a:4d"
}
```

## /redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/6.1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/6.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "6.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ee:2d:24",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ee:2d:24"
}
```

## /redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/6.2

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/6.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "6.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ee:2d:25",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ee:2d:25"
}
```

## /redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/7.0

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/7.0",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "7.0",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3C:57:31:CC:14:02",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3C:57:31:CC:14:02"
}
```

## /redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/7.1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/7.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "7.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3C:57:31:CC:14:04",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3C:57:31:CC:14:04"
}
```

## /redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/7.2

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/7.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "7.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3C:57:31:CC:14:03",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3C:57:31:CC:14:03"
}
```

## /redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/7.3

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/7.3",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "7.3",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3C:57:31:CC:14:05",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3C:57:31:CC:14:05"
}
```

## /redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/L.1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/L.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "L.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "5c:71:0d:26:2b:d2",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "5c:71:0d:26:2b:d2"
}
```

## /redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/L.2

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/L.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "L.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "5c:71:0d:26:2b:d3",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "5c:71:0d:26:2b:d3"
}
```

## /redfish/v1/Systems/WZP23400AK4/LogServices

```
```

## /redfish/v1/Systems/WZP23400AK4/Memory

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryCollection.MemoryCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory",
    "@odata.type": "#MemoryCollection.MemoryCollection",
    "Description": "Collection of Memory resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_J2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_D2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_C2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_E2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_B1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_A2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_L2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_K2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_H1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_M2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_J1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_G2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_D1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_C1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_E1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_F2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_A1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_B2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_K1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_L1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_M1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_F1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_G1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_H2"
        }
    ],
    "Members@odata.count": 24,
    "Name": "Memory Collection"
}
```

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_A1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_A1",
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
    "Manufacturer": "0x2C00",
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
    "OperatingSpeedMhz": 2933,
    "PartNumber": "36ASF4G72PZ-2G9E2   ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "F0F736F1",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_A2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_A2",
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

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_B1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_B1",
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
    "Manufacturer": "0x2C00",
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
    "OperatingSpeedMhz": 2933,
    "PartNumber": "36ASF4G72PZ-2G9E2   ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "F0F7370D",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_B2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_B2",
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

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_C1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_C1",
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
    "Manufacturer": "0x2C00",
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
    "OperatingSpeedMhz": 2933,
    "PartNumber": "36ASF4G72PZ-2G9E2   ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "F0F736F9",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_C2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_C2",
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

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_D1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_D1",
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
    "Manufacturer": "0x2C00",
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
    "OperatingSpeedMhz": 2933,
    "PartNumber": "36ASF4G72PZ-2G9E2   ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "F0F73709",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_D2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_D2",
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

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_E1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_E1",
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
    "Manufacturer": "0x2C00",
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
    "OperatingSpeedMhz": 2933,
    "PartNumber": "36ASF4G72PZ-2G9E2   ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "F0F736F7",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_E2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_E2",
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

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_F1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_F1",
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
    "Manufacturer": "0x2C00",
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
    "OperatingSpeedMhz": 2933,
    "PartNumber": "36ASF4G72PZ-2G9E2   ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "F0F7370A",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_F2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_F2",
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

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_G1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_G1",
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
    "Manufacturer": "0x2C00",
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
    "OperatingSpeedMhz": 2933,
    "PartNumber": "36ASF4G72PZ-2G9E2   ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "F0F736F8",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_G2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_G2",
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

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_H1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_H1",
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
    "Manufacturer": "0x2C00",
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
    "OperatingSpeedMhz": 2933,
    "PartNumber": "36ASF4G72PZ-2G9E2   ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "F0F736ED",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_H2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_H2",
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

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_J1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_J1",
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
    "Manufacturer": "0x2C00",
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
    "OperatingSpeedMhz": 2933,
    "PartNumber": "36ASF4G72PZ-2G9E2   ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "F0F736F6",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_J2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_J2",
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

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_K1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_K1",
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
    "Manufacturer": "0x2C00",
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
    "OperatingSpeedMhz": 2933,
    "PartNumber": "36ASF4G72PZ-2G9E2   ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "F0EFB85E",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_K2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_K2",
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

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_L1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_L1",
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
    "Manufacturer": "0x2C00",
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
    "OperatingSpeedMhz": 2933,
    "PartNumber": "36ASF4G72PZ-2G9E2   ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "F0F72BFA",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_L2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_L2",
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

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_M1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_M1",
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
    "Manufacturer": "0x2C00",
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
    "OperatingSpeedMhz": 2933,
    "PartNumber": "36ASF4G72PZ-2G9E2   ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "F0F72BFE",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/Memory/DIMM_M2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Memory/DIMM_M2",
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

## /redfish/v1/Systems/WZP23400AK4/MemoryDomains

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryDomainCollection.MemoryDomainCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/MemoryDomains",
    "@odata.type": "#MemoryDomainCollection.MemoryDomainCollection",
    "Description": "Collection of Memory Domain resource instances for this system",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Memory Domain Collection"
}
```

## /redfish/v1/Systems/WZP23400AK4/NetworkInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/NetworkInterfaces",
    "@odata.type": "#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "Description": "Collection of NetworkInterface resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/NetworkInterfaces/UCSC-MLOM-C25Q-04_FCH24157DE1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "NetworkInterface Collection"
}
```

## /redfish/v1/Systems/WZP23400AK4/NetworkInterfaces/UCSC-MLOM-C25Q-04_FCH24157DE1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterface.NetworkInterface",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/NetworkInterfaces/UCSC-MLOM-C25Q-04_FCH24157DE1",
    "@odata.type": "#NetworkInterface.v1_1_1.NetworkInterface",
    "Description": "NetworkInterface contains references linking NetworkAdapter, NetworkPort, and NetworkDeviceFunction resources and represents the functionality available to the containing system.",
    "Id": "UCSC-MLOM-C25Q-04_FCH24157DE1",
    "Links": {
        "NetworkAdapter": {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1"
        }
    },
    "Name": "Adapter Card UCSC-MLOM-C25Q-04_FCH24157DE1",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts"
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/3

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/3",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80009E5D-1.823.2",
    "Id": "3",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/3/PCIeFunctions/3"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/3/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/3/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/3/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/3/PCIeFunctions/3"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/3/PCIeFunctions/3

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/3/PCIeFunctions/3",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x158b",
    "Id": "3",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/3.2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/3.1"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/3"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
    "SubsystemId": "0x0225",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/6

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/6",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80009E5D-1.823.2",
    "Id": "6",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/6/PCIeFunctions/6"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/6/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/6/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/6/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/6/PCIeFunctions/6"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/6/PCIeFunctions/6

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/6/PCIeFunctions/6",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x158b",
    "Id": "6",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/6.2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/6.1"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/6"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
    "SubsystemId": "0x0225",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/L

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/L",
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
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/L/PCIeFunctions/L"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel X550 LOM",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/L/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/L/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/L/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/L/PCIeFunctions/L"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/L/PCIeFunctions/L

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/L/PCIeFunctions/L",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1563",
    "Id": "L",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/L.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/L.2"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/L"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel X550 LOM",
    "SubsystemId": "0x01a4",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MLOM",
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
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MLOM/PCIeFunctions/MLOM"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco UCS VIC 1457 MLOM",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MLOM/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/MLOM/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MLOM/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MLOM/PCIeFunctions/MLOM"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/MLOM/PCIeFunctions/MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MLOM/PCIeFunctions/MLOM",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0042",
    "Id": "MLOM",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/eth0"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/eth1"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/fc0"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/fc1"
            }
        ],
        "NetworkDeviceFunctions@odata.count": 4,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MLOM"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Cisco UCS VIC 1457 MLOM",
    "SubsystemId": "0x0218",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1137"
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MRAID",
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
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MRAID/PCIeFunctions/MRAID"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MRAID/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/MRAID/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MRAID/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MRAID/PCIeFunctions/MRAID"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeDevices/MRAID/PCIeFunctions/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MRAID/PCIeFunctions/MRAID",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0014",
    "Id": "MRAID",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/7"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/8"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/19"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/20"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/21"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/22"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/23"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/24"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/25"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/26"
            }
        ],
        "Drives@odata.count": 26,
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MRAID"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
    "SubsystemId": "0x020e",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1000"
}
```

## /redfish/v1/Systems/WZP23400AK4/PCIeFunctions/MRAID

```null
```

## /redfish/v1/Systems/WZP23400AK4/Processors

```{
    "@odata.context": "/redfish/v1/$metadata#ProcessorCollection.ProcessorCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Processors",
    "@odata.type": "#ProcessorCollection.ProcessorCollection",
    "Description": "Collection of Processors for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Processors/CPU2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Processors/CPU1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Processors Collection"
}
```

## /redfish/v1/Systems/WZP23400AK4/Processors/CPU1

```{
    "@odata.context": "/redfish/v1/$metadata#Processor.Processor",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Processors/CPU1",
    "@odata.type": "#Processor.v1_5_0.Processor",
    "Description": "Intel(R) Xeon(R) Gold 6248 2.50 GHz 150W 20C 27.50MB Cache DDR4 2933MHz 1TB",
    "Id": "1",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
    "Name": "CPU1",
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "6",
        "EffectiveModel": "85",
        "Step": "7",
        "VendorId": "Intel(R) Corporation"
    },
    "ProcessorType": "CPU",
    "Socket": "CPU1",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TotalCores": 20,
    "TotalEnabledCores": 20,
    "TotalThreads": 20
}
```

## /redfish/v1/Systems/WZP23400AK4/Processors/CPU2

```{
    "@odata.context": "/redfish/v1/$metadata#Processor.Processor",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Processors/CPU2",
    "@odata.type": "#Processor.v1_5_0.Processor",
    "Description": "Intel(R) Xeon(R) Gold 6248 2.50 GHz 150W 20C 27.50MB Cache DDR4 2933MHz 1TB",
    "Id": "2",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
    "Name": "CPU2",
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "6",
        "EffectiveModel": "85",
        "Step": "7",
        "VendorId": "Intel(R) Corporation"
    },
    "ProcessorType": "CPU",
    "Socket": "CPU2",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TotalCores": 20,
    "TotalEnabledCores": 20,
    "TotalThreads": 20
}
```

## /redfish/v1/Systems/WZP23400AK4/SecureBoot

```{
    "@odata.context": "/redfish/v1/$metadata#SecureBoot.SecureBoot",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/SecureBoot",
    "@odata.type": "#SecureBoot.v1_0_4.SecureBoot",
    "Description": "UEFI SecureBoot configuration of this system",
    "Id": "SecureBoot",
    "Name": "SecureBoot",
    "SecureBootCurrentBoot": "Enabled",
    "SecureBootEnable": false
}
```

## /redfish/v1/Systems/WZP23400AK4/SimpleStorage

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorageCollection.SimpleStorageCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/SimpleStorage",
    "@odata.type": "#SimpleStorageCollection.SimpleStorageCollection",
    "Description": "Collection of storage controllers for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/SimpleStorage/MRAID"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Simple Storage Collection"
}
```

## /redfish/v1/Systems/WZP23400AK4/SimpleStorage/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorage.SimpleStorage",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/SimpleStorage/MRAID",
    "@odata.type": "#SimpleStorage.v1_2_1.SimpleStorage",
    "Description": "Simple Storage Controller",
    "Devices": [],
    "Id": "MRAID",
    "Name": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
    "Status": {}
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage

```{
    "@odata.context": "/redfish/v1/$metadata#StorageCollection.StorageCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage",
    "@odata.type": "#StorageCollection.StorageCollection",
    "Description": "Collection of storage resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Storage Collection"
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#Storage.Storage",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID",
    "@odata.type": "#Storage.v1_8_0.Storage",
    "Actions": {
        "Oem": {
            "#Cisco.BbuStartLearnCycle": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.BbuStartLearnCycle",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.BbuStartLearnCycle"
            },
            "#Cisco.ClearConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ClearConfig",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.ClearConfig"
            },
            "#Cisco.DoForeignConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.DoForeignConfig",
                "ForeignCfgOp@Redfish.AllowableValues": [
                    "Clear",
                    "Import"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.DoForeignConfig"
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
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.EncryptionOp"
            },
            "#Cisco.GetLogs": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.GetLogs",
                "OutputFile@Redfish.AllowableValues": [
                    "A string of length between 1-64 alpha numeric characters for output file name"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.GetLogs"
            },
            "#Cisco.ResetToFactoryDefaults": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetToFactoryDefaults",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.ResetToFactoryDefaults"
            },
            "#Cisco.UnpinCache": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UnpinCache",
                "DiscardType@Redfish.AllowableValues": [
                    "all",
                    "missing"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.UnpinCache"
            }
        }
    },
    "Description": "Storage Controller",
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18"
        }
    ],
    "Id": "MRAID",
    "Links": {
        "Oem": {
            "Cisco": {
                "PCIeInfo": [
                    {
                        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeFunctions/MRAID"
                    }
                ]
            }
        }
    },
    "Name": "MRAID",
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID",
            "CacheSummary": {
                "PersistentCacheSizeMiB": 1332,
                "TotalCacheSizeMiB": 2048
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
            "Model": "UCSC-RAID-M5",
            "Name": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
            "Oem": {
                "Cisco": {
                    "Bbu": {
                        "BbuChargingState": "Unknown",
                        "BbuCurrentInAmps": 0,
                        "BbuDesignVoltageInVolts": 9.5,
                        "BbuDeviceName": "CVPM05",
                        "BbuManufacturingDate": "2019-12-26",
                        "BbuModuleVersion": "05668-01",
                        "BbuSerialNumber": 22303,
                        "BbuStatus": "Optimal",
                        "BbuTemperatureInCel": 22,
                        "BbuType": "TMMC",
                        "BbuVendor": "LSI",
                        "BbuVoltageInVolts": 12.497,
                        "CapacitanceInPercent": 100,
                        "DesignCapacityInJoules": 306,
                        "IsBatteryPresent": true,
                        "IsCapacitor": true,
                        "IsLearnCycleRequested": false,
                        "IsLearnCycleTransparent": true,
                        "IsTemperatureHigh": false,
                        "IsVoltageLow": false,
                        "LearnCycleProgressEndTimeStamp": "1668451929",
                        "LearnCycleProgressStartTimeStamp": "1668451804",
                        "LearnCycleProgressStatus": "Success",
                        "LearnMode": "Auto",
                        "NextLearnCycleTimeStamp": "2022-12-12 17:51",
                        "PackEnergyInJoules": 616,
                        "RemainingPoolSpaceInPercent": 0
                    },
                    "BootDevices": [
                        "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/0"
                    ],
                    "ChipRevision": "08004",
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
                    "SubOEMId": 3,
                    "SupportedStripeSizesKiBytes": [
                        64,
                        128,
                        256,
                        512,
                        1024
                    ]
                }
            },
            "SerialNumber": "SK00481450",
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
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/1

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 6,
    "CapacityBytes": 960196771840,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "10",
    "IndicatorLED": "Off",
    "Manufacturer": "ATA     ",
    "MediaType": "SSD",
    "Model": "UCS-SD960G6I1X-EV",
    "Name": "SSDSC2KB960G7K - 960GB 2.5 inch Enterprise Value 6G SATA SSD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 958999298048,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 959659900928,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "PercentLifeLeft": 99,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 98,
                "PowerOnHours": 15827,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1806
            },
            "StorageInstanceId": 10
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "10"
        }
    },
    "PredictedMediaLifeLeftPercent": 99,
    "Protocol": "SATA",
    "Revision": "SCV1CS08",
    "SerialNumber": "PHYS746002M1960CGN  ",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 6,
    "CapacityBytes": 960196771840,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "11",
    "IndicatorLED": "Off",
    "Manufacturer": "ATA     ",
    "MediaType": "SSD",
    "Model": "UCS-SD960G6I1X-EV",
    "Name": "SSDSC2KB960G7K - 960GB 2.5 inch Enterprise Value 6G SATA SSD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 958999298048,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "UnConfiguredGood",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 959659900928,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 89,
                "PowerOnHours": 15812,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 11
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "11"
        }
    },
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "SATA",
    "Revision": "SCV1CS08",
    "SerialNumber": "PHYS746002ME960CGN  ",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 6,
    "CapacityBytes": 960196771840,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "12",
    "IndicatorLED": "Off",
    "Manufacturer": "ATA     ",
    "MediaType": "SSD",
    "Model": "UCS-SD960G6I1X-EV",
    "Name": "SSDSC2KB960G7K - 960GB 2.5 inch Enterprise Value 6G SATA SSD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 958999298048,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "UnConfiguredGood",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 959659900928,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 90,
                "PowerOnHours": 15812,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 12
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "12"
        }
    },
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "SATA",
    "Revision": "SCV1CS08",
    "SerialNumber": "PHYS746003DM960CGN  ",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 1200243081216,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "13",
    "IndicatorLED": "Off",
    "Manufacturer": "SEAGATE ",
    "MediaType": "HDD",
    "Model": "UCS-HD12TB10K12N",
    "Name": "ST1200MM0009 - 1.2TB 12G SAS 10K RPM SFF HDD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 60
            },
            "StorageInstanceId": 13
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "13"
        }
    },
    "Protocol": "SAS",
    "Revision": "CN03",
    "SerialNumber": "WFK65JQF0000C0259760",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 1200243081216,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "14",
    "IndicatorLED": "Off",
    "Manufacturer": "SEAGATE ",
    "MediaType": "HDD",
    "Model": "UCS-HD12TB10K12N",
    "Name": "ST1200MM0009 - 1.2TB 12G SAS 10K RPM SFF HDD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 60
            },
            "StorageInstanceId": 14
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "14"
        }
    },
    "Protocol": "SAS",
    "Revision": "CN03",
    "SerialNumber": "WFK65LZ70000C02597DN",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 1200243081216,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "15",
    "IndicatorLED": "Off",
    "Manufacturer": "SEAGATE ",
    "MediaType": "HDD",
    "Model": "UCS-HD12TB10K12N",
    "Name": "ST1200MM0009 - 1.2TB 12G SAS 10K RPM SFF HDD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 60
            },
            "StorageInstanceId": 15
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "15"
        }
    },
    "Protocol": "SAS",
    "Revision": "CN03",
    "SerialNumber": "WFK65LD10000C024KKJM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 1200243081216,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "16",
    "IndicatorLED": "Off",
    "Manufacturer": "SEAGATE ",
    "MediaType": "HDD",
    "Model": "UCS-HD12TB10K12N",
    "Name": "ST1200MM0009 - 1.2TB 12G SAS 10K RPM SFF HDD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 60
            },
            "StorageInstanceId": 16
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "16"
        }
    },
    "Protocol": "SAS",
    "Revision": "CN03",
    "SerialNumber": "WFK64DPD0000C0244K8B",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 1200243081216,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "17",
    "IndicatorLED": "Off",
    "Manufacturer": "SEAGATE ",
    "MediaType": "HDD",
    "Model": "UCS-HD12TB10K12N",
    "Name": "ST1200MM0009 - 1.2TB 12G SAS 10K RPM SFF HDD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 60
            },
            "StorageInstanceId": 17
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "17"
        }
    },
    "Protocol": "SAS",
    "Revision": "CN03",
    "SerialNumber": "WFK64DX60000C025BW6X",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 1200243081216,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "18",
    "IndicatorLED": "Off",
    "Manufacturer": "SEAGATE ",
    "MediaType": "HDD",
    "Model": "UCS-HD12TB10K12N",
    "Name": "ST1200MM0088 - 1.2TB SAS 12Gb 10K rpm SFF HDD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 60
            },
            "StorageInstanceId": 18
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "18"
        }
    },
    "Protocol": "SAS",
    "Revision": "N0A4",
    "SerialNumber": "Z4000FFD0000R616HPN9",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/19

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/2

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/20

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/21

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/22

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/23

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/24

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/25

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/26

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/3

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/4

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/5

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/6

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/7

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/8

```null
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 6,
    "CapacityBytes": 960196771840,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "9",
    "IndicatorLED": "Off",
    "Manufacturer": "ATA     ",
    "MediaType": "SSD",
    "Model": "UCS-SD960G6I1X-EV",
    "Name": "SSDSC2KB960G7K - 960GB 2.5 inch Enterprise Value 6G SATA SSD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 958999298048,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 959659900928,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "PercentLifeLeft": 99,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 100,
                "PowerOnHours": 15828,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1806
            },
            "StorageInstanceId": 9
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "9"
        }
    },
    "PredictedMediaLifeLeftPercent": 99,
    "Protocol": "SATA",
    "Revision": "SCV1CS08",
    "SerialNumber": "PHYS746100ZW960CGN  ",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes

```{
    "@odata.context": "/redfish/v1/$metadata#VolumeCollection.VolumeCollection",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection of Volumes for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Volume Collection"
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/0

```{
    "@odata.context": "/redfish/v1/$metadata#Volume.Volume",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/0",
    "@odata.type": "#Volume.v1_4_0.Volume",
    "Actions": {
        "#Volume.CheckConsistency": {
            "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/0/Actions/Volume.CheckConsistency"
        },
        "#Volume.Initialize": {
            "InitializeType@Redfish.AllowableValues": [
                "Fast",
                "Slow"
            ],
            "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/0/Actions/Volume.Initialize"
        }
    },
    "BlockSizeBytes": 512,
    "CapacityBytes": 1917998596096,
    "Description": "Volume",
    "Encrypted": false,
    "Id": "0",
    "Identifiers": [
        {
            "DurableName": "6cc167e9736dad0028f9415ba7e91321 ",
            "DurableNameFormat": "UUID"
        }
    ],
    "Links": {
        "DedicatedSpareDrives": [],
        "DedicatedSpareDrives@odata.count": 0,
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10"
            }
        ],
        "Drives@odata.count": 2,
        "Oem": {
            "Cisco": {
                "Spans": [
                    {
                        "DrivesList": [
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10"
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
    "Name": "RAID0_910",
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
    "RAIDType": "RAID0",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/1

```{
    "@odata.context": "/redfish/v1/$metadata#Volume.Volume",
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/1",
    "@odata.type": "#Volume.v1_4_0.Volume",
    "Actions": {
        "#Volume.CheckConsistency": {
            "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/1/Actions/Volume.CheckConsistency"
        },
        "#Volume.Initialize": {
            "InitializeType@Redfish.AllowableValues": [
                "Fast",
                "Slow"
            ],
            "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/1/Actions/Volume.Initialize"
        }
    },
    "BlockSizeBytes": 512,
    "CapacityBytes": 4795997880320,
    "Description": "Volume",
    "Encrypted": false,
    "Id": "1",
    "Identifiers": [
        {
            "DurableName": "6cc167e9736dad002aff9a51d0c7eed7 ",
            "DurableNameFormat": "UUID"
        }
    ],
    "Links": {
        "DedicatedSpareDrives": [],
        "DedicatedSpareDrives@odata.count": 0,
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18"
            }
        ],
        "Drives@odata.count": 6,
        "Oem": {
            "Cisco": {
                "Spans": [
                    {
                        "DrivesList": [
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18"
                            }
                        ],
                        "DrivesList@odata.count": 6,
                        "SpanId": 0
                    }
                ],
                "Spans@odata.count": 1
            }
        },
        "SpareResourceSets": [],
        "SpareResourceSets@odata.count": 0
    },
    "Name": "RAID6_131415161",
    "Oem": {
        "Cisco": {
            "AvailableSizeMiBytes": 0,
            "Bootable": false,
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
    "RAIDType": "RAID6",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

