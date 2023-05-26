# Resource: /redfish/v1/Systems

Vendor | Model
--- | ---
Cisco | UCSC-C220-M5SX

## /redfish/v1/Systems

```{
    "@odata.context": "/redfish/v1/$metadata#ComputerSystemCollection.ComputerSystemCollection",
    "@odata.id": "/redfish/v1/Systems",
    "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection",
    "Description": "Collection of Computer Systems",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Computer System Collection"
}
```

## /redfish/v1/Systems/WZP22490ZCU

```{
    "@odata.context": "/redfish/v1/$metadata#ComputerSystem.ComputerSystem",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU",
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
            "target": "/redfish/v1/Systems/WZP22490ZCU/Actions/ComputerSystem.Reset"
        },
        "Oem": {
            "#CiscoUCSExtensions.ResetBIOSCMOS": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetBIOSCMOS",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Actions/Oem/ComputerSystem.ResetBIOSCMOS"
            }
        }
    },
    "AssetTag": "029056F",
    "Bios": {
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Bios"
    },
    "BiosVersion": "C220M5.4.1.3i.0.0713210713",
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
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces"
    },
    "HostName": "aio-1-p1-eu-spdc-WZP22490ZCU",
    "HostWatchdogTimer": {
        "FunctionEnabled": false,
        "Status": {
            "State": "Disabled"
        },
        "TimeoutAction": "PowerDown",
        "WarningAction": "None"
    },
    "Id": "WZP22490ZCU",
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
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/LogServices"
    },
    "Manufacturer": "Cisco Systems Inc",
    "Memory": {
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory"
    },
    "MemoryDomains": {
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/MemoryDomains"
    },
    "MemorySummary": {
        "Status": {
            "Health": "OK",
            "HealthRollup": "OK"
        },
        "TotalSystemMemoryGiB": 256
    },
    "Model": "UCSC-C220-M5SX",
    "Name": "UCS C220 M5SX",
    "NetworkInterfaces": {
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/NetworkInterfaces"
    },
    "Oem": {
        "Cisco": {
            "DimmBlacklistingEnabled": true,
            "FrontPanelButtonsLocked": false,
            "PostCompletionStatus": true,
            "SystemEffectiveMemory": 256,
            "SystemEffectiveSpeed": 2666
        }
    },
    "PCIeDevices": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/MRAID"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/L"
        }
    ],
    "PCIeDevices@odata.count": 4,
    "PCIeFunctions": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/1/PCIeFunctions/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/2/PCIeFunctions/2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/MRAID/PCIeFunctions/MRAID"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/L/PCIeFunctions/L"
        }
    ],
    "PCIeFunctions@odata.count": 4,
    "PowerRestorePolicy": "AlwaysOff",
    "PowerState": "On",
    "ProcessorSummary": {
        "Count": 2,
        "Model": "Intel(R) Xeon(R) Gold 6152 CPU @ 2.10GHz"
    },
    "Processors": {
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Processors"
    },
    "SecureBoot": {
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/SecureBoot"
    },
    "SerialNumber": "WZP22490ZCU",
    "SimpleStorage": {
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/SimpleStorage"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "Storage": {
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage"
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
                        "SerialNumber": "FCH22427C51"
                    }
                }
            },
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ],
    "UUID": "B16A1200-1CCF-42EA-8B33-6C4D50110704"
}
```

## /redfish/v1/Systems/WZP22490ZCU/Bios

```{
    "@odata.context": "/redfish/v1/$metadata#Bios.Bios",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Bios",
    "@odata.type": "#Bios.v1_0_4.Bios",
    "Actions": {
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/WZP22490ZCU/Bios/Actions/Bios.ResetBios"
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
        "ConsoleRedir": "COM 0",
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
        "EnhancedIntelSpeedStep": "Disabled",
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
        "PcieSlotFrontNvme1LinkSpeed": "Auto",
        "PcieSlotFrontNvme2LinkSpeed": "Auto",
        "PcieSlotMLOMLinkSpeed": "Auto",
        "PcieSlotMLOMOptionROM": "Enabled",
        "PcieSlotMRAIDLinkSpeed": "Auto",
        "PcieSlotMRAIDOptionROM": "Enabled",
        "PcieSlotMSTORRAIDOptionROM": "Enabled",
        "PcieSlotN1OptionROM": "Enabled",
        "PcieSlotN2OptionROM": "Enabled",
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
        "XPTPrefetch": "Disabled",
        "cdnEnable": "Enabled",
        "pSATA": "Disabled"
    },
    "Description": "BIOS Configuration Current Settings",
    "Id": "BiosToken",
    "Name": "BiosToken"
}
```

## /redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Description": "Collection of EthernetInterfaces for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/L.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/L.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.1"
        }
    ],
    "Members@odata.count": 10,
    "Name": "Ethernet Interfaces Collection"
}
```

## /redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "1.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ce:13:a8",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ce:13:a8"
}
```

## /redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.2

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "1.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ce:13:a9",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ce:13:a9"
}
```

## /redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.3

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.3",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "1.3",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ce:13:aa",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ce:13:aa"
}
```

## /redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.4

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.4",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "1.4",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ce:13:ab",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ce:13:ab"
}
```

## /redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "2.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ce:16:48",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ce:16:48"
}
```

## /redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.2

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "2.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ce:16:49",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ce:16:49"
}
```

## /redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.3

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.3",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "2.3",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ce:16:4a",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ce:16:4a"
}
```

## /redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.4

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.4",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "2.4",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ce:16:4b",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ce:16:4b"
}
```

## /redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/L.1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/L.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "L.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "70:ea:1a:59:c9:a2",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "70:ea:1a:59:c9:a2"
}
```

## /redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/L.2

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/L.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "L.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "70:ea:1a:59:c9:a3",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "70:ea:1a:59:c9:a3"
}
```

## /redfish/v1/Systems/WZP22490ZCU/LogServices

```
```

## /redfish/v1/Systems/WZP22490ZCU/Memory

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryCollection.MemoryCollection",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory",
    "@odata.type": "#MemoryCollection.MemoryCollection",
    "Description": "Collection of Memory resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_J2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_D2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_C2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_E2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_B1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_A2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_L2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_K2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_H1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_M2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_J1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_G2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_D1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_C1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_E1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_F2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_A1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_B2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_K1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_L1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_M1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_F1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_G1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_H2"
        }
    ],
    "Members@odata.count": 24,
    "Name": "Memory Collection"
}
```

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_A1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_A1",
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
    "PartNumber": "HMA84GR7AFR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "1222C96C",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_A2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_A2",
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

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_B1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_B1",
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
    "PartNumber": "HMA84GR7AFR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "1222C984",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_B2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_B2",
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

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_C1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_C1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "5",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_C1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_C2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_C2",
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

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_D1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_D1",
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
    "PartNumber": "HMA84GR7AFR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "1222C9FA",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_D2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_D2",
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

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_E1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_E1",
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
    "PartNumber": "HMA84GR7AFR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "1222C9CE",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_E2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_E2",
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

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_F1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_F1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "11",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_F1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_F2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_F2",
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

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_G1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_G1",
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
    "PartNumber": "HMA84GR7AFR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "825EFEDA",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_G2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_G2",
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

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_H1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_H1",
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
    "PartNumber": "HMA84GR7AFR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "1222CB02",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_H2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_H2",
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

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_J1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_J1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "17",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_J1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_J2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_J2",
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

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_K1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_K1",
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
    "PartNumber": "HMA84GR7AFR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "1222CA2C",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_K2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_K2",
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

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_L1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_L1",
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
    "PartNumber": "HMA84GR7AFR4N-VK    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "1222C97A",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_L2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_L2",
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

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_M1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_M1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "Description": "Computer Memory",
    "Id": "23",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "DIMM_M1",
    "Status": {
        "State": "Absent"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_M2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Memory/DIMM_M2",
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

## /redfish/v1/Systems/WZP22490ZCU/MemoryDomains

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryDomainCollection.MemoryDomainCollection",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/MemoryDomains",
    "@odata.type": "#MemoryDomainCollection.MemoryDomainCollection",
    "Description": "Collection of Memory Domain resource instances for this system",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Memory Domain Collection"
}
```

## /redfish/v1/Systems/WZP22490ZCU/NetworkInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/NetworkInterfaces",
    "@odata.type": "#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "Description": "Collection of NetworkInterface resource instances for this system",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "NetworkInterface Collection"
}
```

## /redfish/v1/Systems/WZP22490ZCU/PCIeDevices/1

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/1",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80009E63-1.823.2",
    "Id": "1",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/1/PCIeFunctions/1"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/1/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/PCIeDevices/1/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/1/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/1/PCIeFunctions/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP22490ZCU/PCIeDevices/1/PCIeFunctions/1

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/1/PCIeFunctions/1",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1572",
    "Id": "1",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.2"
            }
        ],
        "EthernetInterfaces@odata.count": 4,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/1"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC",
    "SubsystemId": "0x013b",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/WZP22490ZCU/PCIeDevices/2

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/2",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80009E63-1.823.2",
    "Id": "2",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/2/PCIeFunctions/2"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/2/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/PCIeDevices/2/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/2/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/2/PCIeFunctions/2"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP22490ZCU/PCIeDevices/2/PCIeFunctions/2

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/2/PCIeFunctions/2",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1572",
    "Id": "2",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.1"
            }
        ],
        "EthernetInterfaces@odata.count": 4,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/2"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC",
    "SubsystemId": "0x013b",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/WZP22490ZCU/PCIeDevices/L

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/L",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80001514-1.823.2",
    "Id": "L",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/L/PCIeFunctions/L"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel X550 LOM",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/L/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/PCIeDevices/L/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/L/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/L/PCIeFunctions/L"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP22490ZCU/PCIeDevices/L/PCIeFunctions/L

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/L/PCIeFunctions/L",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1563",
    "Id": "L",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/L.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/L.2"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/L"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel X550 LOM",
    "SubsystemId": "0x01a3",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/WZP22490ZCU/PCIeDevices/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/MRAID",
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
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/MRAID/PCIeFunctions/MRAID"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/MRAID/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/PCIeDevices/MRAID/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/MRAID/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/MRAID/PCIeFunctions/MRAID"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/WZP22490ZCU/PCIeDevices/MRAID/PCIeFunctions/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/MRAID/PCIeFunctions/MRAID",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0014",
    "Id": "MRAID",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/7"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/8"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/9"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/10"
            }
        ],
        "Drives@odata.count": 10,
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeDevices/MRAID"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID"
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

## /redfish/v1/Systems/WZP22490ZCU/PCIeFunctions/MRAID

```null
```

## /redfish/v1/Systems/WZP22490ZCU/Processors

```{
    "@odata.context": "/redfish/v1/$metadata#ProcessorCollection.ProcessorCollection",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Processors",
    "@odata.type": "#ProcessorCollection.ProcessorCollection",
    "Description": "Collection of Processors for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Processors/CPU2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Processors/CPU1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Processors Collection"
}
```

## /redfish/v1/Systems/WZP22490ZCU/Processors/CPU1

```{
    "@odata.context": "/redfish/v1/$metadata#Processor.Processor",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Processors/CPU1",
    "@odata.type": "#Processor.v1_5_0.Processor",
    "Description": "Intel(R) Xeon(R) Gold 6152 2.10 GHz 140W 22C 30.25MB Cache DDR4 2666MHz 768GB",
    "Id": "1",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) Gold 6152 CPU @ 2.10GHz",
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
    "TotalCores": 22,
    "TotalEnabledCores": 22,
    "TotalThreads": 22
}
```

## /redfish/v1/Systems/WZP22490ZCU/Processors/CPU2

```{
    "@odata.context": "/redfish/v1/$metadata#Processor.Processor",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Processors/CPU2",
    "@odata.type": "#Processor.v1_5_0.Processor",
    "Description": "Intel(R) Xeon(R) Gold 6152 2.10 GHz 140W 22C 30.25MB Cache DDR4 2666MHz 768GB",
    "Id": "2",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) Gold 6152 CPU @ 2.10GHz",
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
    "TotalCores": 22,
    "TotalEnabledCores": 22,
    "TotalThreads": 22
}
```

## /redfish/v1/Systems/WZP22490ZCU/SecureBoot

```{
    "@odata.context": "/redfish/v1/$metadata#SecureBoot.SecureBoot",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/SecureBoot",
    "@odata.type": "#SecureBoot.v1_0_4.SecureBoot",
    "Description": "UEFI SecureBoot configuration of this system",
    "Id": "SecureBoot",
    "Name": "SecureBoot",
    "SecureBootCurrentBoot": "Enabled",
    "SecureBootEnable": false
}
```

## /redfish/v1/Systems/WZP22490ZCU/SimpleStorage

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorageCollection.SimpleStorageCollection",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/SimpleStorage",
    "@odata.type": "#SimpleStorageCollection.SimpleStorageCollection",
    "Description": "Collection of storage controllers for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/SimpleStorage/MRAID"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Simple Storage Collection"
}
```

## /redfish/v1/Systems/WZP22490ZCU/SimpleStorage/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorage.SimpleStorage",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/SimpleStorage/MRAID",
    "@odata.type": "#SimpleStorage.v1_2_1.SimpleStorage",
    "Description": "Simple Storage Controller",
    "Devices": [],
    "Id": "MRAID",
    "Name": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
    "Status": {}
}
```

## /redfish/v1/Systems/WZP22490ZCU/Storage

```{
    "@odata.context": "/redfish/v1/$metadata#StorageCollection.StorageCollection",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage",
    "@odata.type": "#StorageCollection.StorageCollection",
    "Description": "Collection of storage resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Storage Collection"
}
```

## /redfish/v1/Systems/WZP22490ZCU/Storage/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#Storage.Storage",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID",
    "@odata.type": "#Storage.v1_8_0.Storage",
    "Actions": {
        "Oem": {
            "#Cisco.BbuStartLearnCycle": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.BbuStartLearnCycle",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Actions/Oem/Cisco.BbuStartLearnCycle"
            },
            "#Cisco.ClearConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ClearConfig",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Actions/Oem/Cisco.ClearConfig"
            },
            "#Cisco.DoForeignConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.DoForeignConfig",
                "ForeignCfgOp@Redfish.AllowableValues": [
                    "Clear",
                    "Import"
                ],
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Actions/Oem/Cisco.DoForeignConfig"
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
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Actions/Oem/Cisco.EncryptionOp"
            },
            "#Cisco.GetLogs": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.GetLogs",
                "OutputFile@Redfish.AllowableValues": [
                    "A string of length between 1-64 alpha numeric characters for output file name"
                ],
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Actions/Oem/Cisco.GetLogs"
            },
            "#Cisco.ResetToFactoryDefaults": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetToFactoryDefaults",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Actions/Oem/Cisco.ResetToFactoryDefaults"
            },
            "#Cisco.UnpinCache": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UnpinCache",
                "DiscardType@Redfish.AllowableValues": [
                    "all",
                    "missing"
                ],
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Actions/Oem/Cisco.UnpinCache"
            }
        }
    },
    "Description": "Storage Controller",
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/7"
        }
    ],
    "Id": "MRAID",
    "Links": {
        "Oem": {
            "Cisco": {
                "PCIeInfo": [
                    {
                        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/PCIeFunctions/MRAID"
                    }
                ]
            }
        }
    },
    "Name": "MRAID",
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID",
            "CacheSummary": {
                "PersistentCacheSizeMiB": 1374,
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
                        "BbuManufacturingDate": "2018-06-08",
                        "BbuModuleVersion": "05668-01",
                        "BbuSerialNumber": 11012,
                        "BbuStatus": "Optimal",
                        "BbuTemperatureInCel": 27,
                        "BbuType": "TMMC",
                        "BbuVendor": "LSI",
                        "BbuVoltageInVolts": 12.445,
                        "CapacitanceInPercent": 100,
                        "DesignCapacityInJoules": 306,
                        "IsBatteryPresent": true,
                        "IsCapacitor": true,
                        "IsLearnCycleRequested": false,
                        "IsLearnCycleTransparent": true,
                        "IsTemperatureHigh": false,
                        "IsVoltageLow": false,
                        "LearnCycleProgressEndTimeStamp": "1669586228",
                        "LearnCycleProgressStartTimeStamp": "1669586100",
                        "LearnCycleProgressStatus": "Success",
                        "LearnMode": "Auto",
                        "NextLearnCycleTimeStamp": "2022-12-25 20:56",
                        "PackEnergyInJoules": 611,
                        "RemainingPoolSpaceInPercent": 0
                    },
                    "BootDevices": [
                        "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Volumes/0"
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
                    "StorageInstanceId": 4,
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
            "SerialNumber": "SK82392277",
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
        "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Volumes"
    }
}
```

## /redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/1

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/1",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/1/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/1/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/1/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/1/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/1/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/1/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 6,
    "CapacityBytes": 240056795136,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "1",
    "IndicatorLED": "Off",
    "Manufacturer": "ATA     ",
    "MediaType": "SSD",
    "Model": "UCS-SD240G61X-EV",
    "Name": "SAMSUNG MZ7LM240HMHQ-00003 - 240GB 2.5 inch 6Gb Enterprise Value SSD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 238999830528,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Jbod",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 239519924224,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "PercentLifeLeft": 98,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 126,
                "PowerOnHours": 29661,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1788
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
    "PredictedMediaLifeLeftPercent": 98,
    "Protocol": "SATA",
    "Revision": "GXT51F3Q",
    "SerialNumber": "S3LKNX0K800827      ",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/10

```null
```

## /redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 1200243081216,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "2",
    "IndicatorLED": "Off",
    "Manufacturer": "TOSHIBA ",
    "MediaType": "HDD",
    "Model": "UCS-HD12TB10K12N",
    "Name": "AL15SEB120N - 1.2TB 12G SAS 10K RPM SFF HDD",
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
                "ThresholdOperatingTemperatureInCel": 65
            },
            "StorageInstanceId": 2
        }
    },
    "Operations": [
        {
            "OperationName": "PatrolRead",
            "PercentageComplete": 0
        }
    ],
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "2"
        }
    },
    "Protocol": "SAS",
    "Revision": "5703",
    "SerialNumber": "Z830A00MFJRG",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 1200243081216,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "3",
    "IndicatorLED": "Off",
    "Manufacturer": "TOSHIBA ",
    "MediaType": "HDD",
    "Model": "UCS-HD12TB10K12N",
    "Name": "AL15SEB120N - 1.2TB 12G SAS 10K RPM SFF HDD",
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
                "ThresholdOperatingTemperatureInCel": 65
            },
            "StorageInstanceId": 3
        }
    },
    "Operations": [
        {
            "OperationName": "PatrolRead",
            "PercentageComplete": 0
        }
    ],
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "3"
        }
    },
    "Protocol": "SAS",
    "Revision": "5703",
    "SerialNumber": "Z820A07VFJRG",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/4

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/4",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/4/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/4/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/4/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/4/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/4/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/4/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 1200243081216,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "4",
    "IndicatorLED": "Off",
    "Manufacturer": "TOSHIBA ",
    "MediaType": "HDD",
    "Model": "UCS-HD12TB10K12N",
    "Name": "AL15SEB120N - 1.2TB 12G SAS 10K RPM SFF HDD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Jbod",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 65
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
    "Protocol": "SAS",
    "Revision": "5703",
    "SerialNumber": "Z830A01YFJRG",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/5

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/5",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/5/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/5/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/5/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/5/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/5/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/5/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 1200243081216,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "5",
    "IndicatorLED": "Off",
    "Manufacturer": "TOSHIBA ",
    "MediaType": "HDD",
    "Model": "UCS-HD12TB10K12N",
    "Name": "AL15SEB120N - 1.2TB 12G SAS 10K RPM SFF HDD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Jbod",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 65
            },
            "StorageInstanceId": 5
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "5"
        }
    },
    "Protocol": "SAS",
    "Revision": "5703",
    "SerialNumber": "Z830A02JFJRG",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/6

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/6",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/6/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/6/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/6/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/6/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/6/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/6/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 1200243081216,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "6",
    "IndicatorLED": "Off",
    "Manufacturer": "TOSHIBA ",
    "MediaType": "HDD",
    "Model": "UCS-HD12TB10K12N",
    "Name": "AL15SEB120N - 1.2TB 12G SAS 10K RPM SFF HDD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Jbod",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 65
            },
            "StorageInstanceId": 6
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "6"
        }
    },
    "Protocol": "SAS",
    "Revision": "5703",
    "SerialNumber": "Z830A02DFJRG",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/7

```{
    "@odata.context": "/redfish/v1/$metadata#Drive.Drive",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/7",
    "@odata.type": "#Drive.v1_9_0.Drive",
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/7/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/7/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/7/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/7/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/7/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/7/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 1200243081216,
    "EncryptionAbility": "None",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "7",
    "IndicatorLED": "Off",
    "Manufacturer": "TOSHIBA ",
    "MediaType": "HDD",
    "Model": "UCS-HD12TB10K12N",
    "Name": "AL15SEB120N - 1.2TB 12G SAS 10K RPM SFF HDD",
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Jbod",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 65
            },
            "StorageInstanceId": 7
        }
    },
    "PhysicalLocation": {
        "PartLocation": {
            "LocationType": "Slot",
            "ServiceLabel": "7"
        }
    },
    "Protocol": "SAS",
    "Revision": "5703",
    "SerialNumber": "Z830A003FJRG",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/8

```null
```

## /redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/9

```null
```

## /redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Volumes

```{
    "@odata.context": "/redfish/v1/$metadata#VolumeCollection.VolumeCollection",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection of Volumes for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Volumes/0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Volume Collection"
}
```

## /redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Volumes/0

```{
    "@odata.context": "/redfish/v1/$metadata#Volume.Volume",
    "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Volumes/0",
    "@odata.type": "#Volume.v1_4_0.Volume",
    "Actions": {
        "#Volume.CheckConsistency": {
            "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Volumes/0/Actions/Volume.CheckConsistency"
        },
        "#Volume.Initialize": {
            "InitializeType@Redfish.AllowableValues": [
                "Fast",
                "Slow"
            ],
            "target": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Volumes/0/Actions/Volume.Initialize"
        }
    },
    "BlockSizeBytes": 512,
    "CapacityBytes": 1198999470080,
    "Description": "Volume",
    "Encrypted": false,
    "Id": "0",
    "Identifiers": [
        {
            "DurableName": "6cc167e972f353002a7d44b7962784f8 ",
            "DurableNameFormat": "UUID"
        }
    ],
    "Links": {
        "DedicatedSpareDrives": [],
        "DedicatedSpareDrives@odata.count": 0,
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3"
            }
        ],
        "Drives@odata.count": 2,
        "Oem": {
            "Cisco": {
                "Spans": [
                    {
                        "DrivesList": [
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3"
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
    "Name": "",
    "Oem": {
        "Cisco": {
            "AvailableSizeMiBytes": 0,
            "Bootable": true,
            "ConfiguredWriteCachePolicy": "WriteBack",
            "FullDiskEncryptionCapable": false,
            "RequestedWriteCachePolicy": "WriteBack",
            "VolumeAccessPolicy": "ReadWrite",
            "VolumeDriveCachePolicy": "NoChange",
            "VolumeIoPolicy": "DirectIo",
            "VolumeReadAheadPolicy": "ReadAhead",
            "VolumeState": "Optimal"
        }
    },
    "OptimumIOSizeBytes": 262144,
    "RAIDType": "RAID1",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

