# Resource: /redfish/v1/Systems

Vendor | Model
--- | ---
Cisco | UCSC-C220-M4S

## /redfish/v1/Systems

```{
    "@odata.context": "/redfish/v1/$metadata#Systems",
    "@odata.id": "/redfish/v1/Systems",
    "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection",
    "Description": "Collection of Computer Systems",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Computer System Collection"
}
```

## /redfish/v1/Systems/FCH2017V24J

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J",
    "@odata.type": "#ComputerSystem.v1_7_0.ComputerSystem",
    "Actions": {
        "#ComputerSystem.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff",
                "GracefulShutdown",
                "ForceRestart",
                "Nmi",
                "PowerCycle"
            ],
            "target": "/redfish/v1/Systems/FCH2017V24J/Actions/ComputerSystem.Reset"
        }
    },
    "AssetTag": "",
    "Bios": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Bios"
    },
    "BiosVersion": "C220M4.4.1.2c.0.0202211901",
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
    "Description": "comp6-p3b-eu-spdc-FCH2017V24J",
    "EthernetInterfaces": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces"
    },
    "HostName": "comp6-p3b-eu-spdc-FCH2017V24J",
    "HostWatchdogTimer": {
        "FunctionEnabled": false,
        "Status": {
            "State": "Disabled"
        },
        "TimeoutAction": "PowerDown",
        "WarningAction": "None"
    },
    "Id": "FCH2017V24J",
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
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/LogServices"
    },
    "Manufacturer": "Cisco Systems Inc",
    "Memory": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory"
    },
    "MemorySummary": {
        "Status": {
            "Health": "OK",
            "HealthRollup": "OK"
        },
        "TotalSystemMemoryGiB": 256
    },
    "Model": "UCSC-C220-M4S",
    "Name": "UCS C220 M4S",
    "NetworkInterfaces": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces"
    },
    "Oem": {
        "Cisco": {
            "SystemEffectiveMemory": 256,
            "SystemEffectiveSpeed": 2133
        }
    },
    "PCIeDevices": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/L"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/MLOM"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/HBA"
        }
    ],
    "PCIeDevices@odata.count": 5,
    "PCIeFunctions": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/L/PCIeFunctions/L"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/1/PCIeFunctions/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/2/PCIeFunctions/2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/MLOM/PCIeFunctions/MLOM"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/HBA/PCIeFunctions/HBA"
        }
    ],
    "PCIeFunctions@odata.count": 5,
    "PowerRestorePolicy": "AlwaysOff",
    "PowerState": "Off",
    "ProcessorSummary": {
        "Count": 2,
        "Model": "Intel(R) Xeon(R) CPU E5-2695 v3 @ 2.30GHz"
    },
    "Processors": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Processors"
    },
    "SecureBoot": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/SecureBoot"
    },
    "SerialNumber": "FCH2017V24J",
    "SimpleStorage": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/SimpleStorage"
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Storage": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage"
    },
    "SystemType": "Physical",
    "TrustedModules": [
        {
            "FirmwareVersion": "1.2",
            "InterfaceType": "TPM1_2",
            "InterfaceTypeSelection": "BiosSetting",
            "Status": {
                "Health": "OK",
                "State": "Disabled"
            }
        }
    ],
    "UUID": "48753718-3DB4-4502-B2A0-58BC21922BA3"
}
```

## /redfish/v1/Systems/FCH2017V24J/Bios

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Bios",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Bios",
    "@odata.type": "#Bios.v1_0_4.Bios",
    "Actions": {
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/FCH2017V24J/Bios/Actions/Bios.ResetBios"
        }
    },
    "AttributeRegistry": "CiscoBiosAttributeRegistry.v1_0_0",
    "Attributes": {
        "ATS": "Enabled",
        "AdjacentCacheLinePrefetch": "Disabled",
        "AllLomPortControl": "Enabled",
        "AllUsbDevices": "Enabled",
        "Altitude": "300 M",
        "AutonumousCstateEnable": "Disabled",
        "BaudRate": "115200",
        "BootPerformanceMode": "Max Performance",
        "CPUPowerManagement": "Custom",
        "ChannelInterLeave": "Auto",
        "CmciEnable": "Disabled",
        "CoherencySupport": "Disabled",
        "ConsoleRedir": "Disabled",
        "CoreMultiProcessing": "All",
        "CpuEngPerfBias": "Performance",
        "CpuPerformanceProfile": "High Throughput",
        "DcuIpPrefetch": "Enabled",
        "DcuStreamerPrefetch": "Disabled",
        "DemandScrub": "Enabled",
        "DirectCacheAccess": "Auto",
        "EnhancedIntelSpeedStep": "Disabled",
        "ExecuteDisable": "Enabled",
        "FRB_2": "Enabled",
        "FlowCtrl": "None",
        "HWPMEnable": "Disabled",
        "HardwarePrefetch": "Disabled",
        "IntelHyperThread": "Enabled",
        "IntelTurboBoostTech": "Disabled",
        "IntelVT": "Enabled",
        "IntelVTD": "Enabled",
        "InterruptRemap": "Enabled",
        "LegacyUSBSupport": "Enabled",
        "LocalX2Apic": "XAPIC",
        "LomOpromControlPort0": "Disabled",
        "LomOpromControlPort1": "Disabled",
        "MemoryMappedIOAbove4GB": "Enabled",
        "NUMAOptimize": "Enabled",
        "OSBootWatchdogTimer": "Disabled",
        "OSBootWatchdogTimerPolicy": "Power Down",
        "OSBootWatchdogTimerTimeout": "10 mins",
        "PCIROMCLP": "Disabled",
        "PCIeSSDHotPlugSupport": "Disabled",
        "POPSupport": "Disabled",
        "PackageCstateLimit": "C0/C1",
        "PanicHighWatermark": "Low",
        "PassThroughDMA": "Disabled",
        "PatrolScrub": "Enabled",
        "PchUsb30Mode": "Disabled",
        "PcieOptionROMs": "Enabled",
        "PcieSlot1OptionROM": "Enabled",
        "PcieSlot2OptionROM": "Enabled",
        "PcieSlotFrontSlot5LinkSpeed": "Auto",
        "PcieSlotFrontSlot6LinkSpeed": "Auto",
        "PcieSlotHBALinkSpeed": "GEN3",
        "PcieSlotHBAOptionROM": "Enabled",
        "PcieSlotMLOMLinkSpeed": "GEN3",
        "PcieSlotMLOMOptionROM": "Enabled",
        "PcieSlotN1OptionROM": "Disabled",
        "PcieSlotN2OptionROM": "Disabled",
        "PcieSlotRiser1LinkSpeed": "GEN3",
        "PcieSlotRiser2LinkSpeed": "GEN3",
        "ProcessorC1E": "Disabled",
        "ProcessorC3Report": "Disabled",
        "ProcessorC6Report": "Disabled",
        "PsdCoordType": "HW ALL",
        "PuttyFunctionKeyPad": "ESCN",
        "PwrPerfTuning": "OS",
        "QPILinkFrequency": "Auto",
        "QpiSnoopMode": "Auto",
        "RankInterLeave": "Auto",
        "RedirectionAfterPOST": "Always Enable",
        "SataModeSelect": "AHCI",
        "SelectMemoryRAS": "Maximum Performance",
        "SrIov": "Enabled",
        "TPMAdminCtrl": "Enabled",
        "TerminalType": "VT100",
        "UsbEmul6064": "Enabled",
        "UsbPortFront": "Enabled",
        "UsbPortInt": "Enabled",
        "UsbPortKVM": "Enabled",
        "UsbPortRear": "Enabled",
        "UsbPortVMedia": "Enabled",
        "UsbXhciSupport": "Enabled",
        "VgaPriority": "Onboard",
        "WorkLdConfig": "Balanced",
        "cdnEnable": "Disabled",
        "comSpcrEnable": "Disabled"
    },
    "Description": "BIOS Configuration Current Settings",
    "Id": "BiosToken",
    "Name": "BiosToken"
}
```

## /redfish/v1/Systems/FCH2017V24J/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Description": "Collection of EthernetInterfaces for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/2.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/2.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/L.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/L.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/MLOM.0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/MLOM.1"
        }
    ],
    "Members@odata.count": 10,
    "Name": "Ethernet Interfaces Collection"
}
```

## /redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "1.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:f0:3e:28",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:f0:3e:28"
}
```

## /redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "1.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:f0:3e:29",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:f0:3e:29"
}
```

## /redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.3

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.3",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "1.3",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:f0:3e:2a",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:f0:3e:2a"
}
```

## /redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.4

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.4",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "1.4",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:f0:3e:2b",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:f0:3e:2b"
}
```

## /redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/2.1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/2.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "2.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "90:e2:ba:d6:7d:7c",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "90:e2:ba:d6:7d:7c"
}
```

## /redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/2.2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/2.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "2.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "90:e2:ba:d6:7d:7d",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "90:e2:ba:d6:7d:7d"
}
```

## /redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/L.1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/L.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "L.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "00:62:ec:15:dc:b2",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "00:62:ec:15:dc:b2"
}
```

## /redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/L.2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/L.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "L.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "00:62:ec:15:dc:b3",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "00:62:ec:15:dc:b3"
}
```

## /redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/MLOM.0

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/MLOM.0",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "MLOM.0",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "00:3A:7D:D0:1C:32",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "00:3A:7D:D0:1C:32"
}
```

## /redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/MLOM.1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/MLOM.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "MLOM.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "00:3A:7D:D0:1C:33",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "00:3A:7D:D0:1C:33"
}
```

## /redfish/v1/Systems/FCH2017V24J/LogServices

```
```

## /redfish/v1/Systems/FCH2017V24J/Memory

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory",
    "@odata.type": "#MemoryCollection.MemoryCollection",
    "Description": "Collection of Memory resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_A1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_B1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_C1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_D1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_E1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_F1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_G1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_H1"
        }
    ],
    "Members@odata.count": 8,
    "Name": "Memory Collection"
}
```

## /redfish/v1/Systems/FCH2017V24J/Memory/DIMM_A1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_A1",
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
    "Name": "DIMM_A1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2133,
    "PartNumber": "M393A4K40BB0-CPB    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "31E814A7",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/Memory/DIMM_B1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_B1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_B1",
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
    "OperatingSpeedMhz": 2133,
    "PartNumber": "M393A4K40BB0-CPB    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "31E815FB",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/Memory/DIMM_C1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_C1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_C1",
    "Id": "7",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xCE00",
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
    "OperatingSpeedMhz": 2133,
    "PartNumber": "M393A4K40BB0-CPB    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "31E8168C",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/Memory/DIMM_D1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_D1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_D1",
    "Id": "10",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xCE00",
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
    "OperatingSpeedMhz": 2133,
    "PartNumber": "M393A4K40BB0-CPB    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "31E81882",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/Memory/DIMM_E1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_E1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_E1",
    "Id": "13",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
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
    "Name": "DIMM_E1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2133,
    "PartNumber": "M393A4K40BB0-CPB    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "31E81945",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/Memory/DIMM_F1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_F1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_F1",
    "Id": "16",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xCE00",
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
    "Name": "DIMM_F1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2133,
    "PartNumber": "M393A4K40BB0-CPB    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "31E81691",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/Memory/DIMM_G1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_G1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_G1",
    "Id": "19",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xCE00",
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
    "Name": "DIMM_G1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2133,
    "PartNumber": "M393A4K40BB0-CPB    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "31E81884",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/Memory/DIMM_H1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Memory/DIMM_H1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_H1",
    "Id": "22",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Manufacturer": "0xCE00",
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
    "Name": "DIMM_H1",
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2133,
    "PartNumber": "M393A4K40BB0-CPB    ",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "31E815F8",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/NetworkInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/NetworkInterfaces",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces",
    "@odata.type": "#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "Description": "Collection of NetworkInterface resource instances for this system",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "NetworkInterface Collection"
}
```

## /redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/eth0

```null
```

## /redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/eth1

```null
```

## /redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/fc0

```null
```

## /redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/fc1

```null
```

## /redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/i0

```null
```

## /redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/i1

```null
```

## /redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/vs0

```null
```

## /redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/vs1

```null
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/1",
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
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/1/PCIeFunctions/1"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco(R) Ethernet Converged NIC X710-DA4",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/1/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/1/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/1/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/1/PCIeFunctions/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/1/PCIeFunctions/1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/1/PCIeFunctions/1",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1572",
    "Id": "1",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/1.2"
            }
        ],
        "EthernetInterfaces@odata.count": 4,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/1"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Cisco(R) Ethernet Converged NIC X710-DA4",
    "SubsystemId": "0x013b",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/2",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x800008A4-1.819.0",
    "Id": "2",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/2/PCIeFunctions/2"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel X520-DA2 10 Gbps 2 port NIC",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/2/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/2/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/2/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/2/PCIeFunctions/2"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/2/PCIeFunctions/2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/2/PCIeFunctions/2",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x10fb",
    "Id": "2",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/2.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/2.2"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/2"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel X520-DA2 10 Gbps 2 port NIC",
    "SubsystemId": "0x000c",
    "SubsystemVendorId": "0x8086",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/HBA

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/HBA",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "24.12.1-0456",
    "Id": "HBA",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/HBA/PCIeFunctions/HBA"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco 12G SAS Modular Raid Controller",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/HBA/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/HBA/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/HBA/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/HBA/PCIeFunctions/HBA"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/HBA/PCIeFunctions/HBA

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/HBA/PCIeFunctions/HBA",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x005d",
    "Id": "HBA",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-2"
            }
        ],
        "Drives@odata.count": 2,
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/HBA"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "Cisco 12G SAS Modular Raid Controller",
    "SubsystemId": "0x00db",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1000"
}
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/L

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/L",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80000E74-1.819.0",
    "Id": "L",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/L/PCIeFunctions/L"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel(R) I350 1 Gbps Network Controller",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/L/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/L/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/L/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/L/PCIeFunctions/L"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/L/PCIeFunctions/L

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/L/PCIeFunctions/L",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1521",
    "Id": "L",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/L.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/L.2"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/L"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel(R) I350 1 Gbps Network Controller",
    "SubsystemId": "0x00d5",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/MLOM",
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
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/MLOM/PCIeFunctions/MLOM"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "UCS VIC 1227 10Gbps 2 port CNA SFP+",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/MLOM/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/MLOM/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/MLOM/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/MLOM/PCIeFunctions/MLOM"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/FCH2017V24J/PCIeDevices/MLOM/PCIeFunctions/MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/MLOM/PCIeFunctions/MLOM",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0042",
    "Id": "MLOM",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/MLOM.0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/MLOM.1"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/eth0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/eth1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/vs0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/vs1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/i0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/i1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/fc0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/fc1"
            }
        ],
        "NetworkDeviceFunctions@odata.count": 8,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/PCIeDevices/MLOM"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "UCS VIC 1227 10Gbps 2 port CNA SFP+",
    "SubsystemId": "0x012e",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1137"
}
```

## /redfish/v1/Systems/FCH2017V24J/Processors

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Processors",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Processors",
    "@odata.type": "#ProcessorCollection.ProcessorCollection",
    "Description": "Collection of Processors for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Processors/CPU1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Processors/CPU2"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Processors Collection"
}
```

## /redfish/v1/Systems/FCH2017V24J/Processors/CPU1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Processors/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Processors/CPU1",
    "@odata.type": "#Processor.v1_5_0.Processor",
    "Description": "Intel(R) Xeon(R) CPU E5-2695 v3 @ 2.30GHz/120W 14C/35MB Cache/DDR4 2133MHz",
    "Id": "1",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) CPU E5-2695 v3 @ 2.30GHz",
    "Name": "CPU1",
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "6",
        "EffectiveModel": "63",
        "Step": "2",
        "VendorId": "Intel(R) Corporation"
    },
    "ProcessorType": "CPU",
    "Socket": "CPU1",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TotalCores": 14,
    "TotalEnabledCores": 14,
    "TotalThreads": 14
}
```

## /redfish/v1/Systems/FCH2017V24J/Processors/CPU2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Processors/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Processors/CPU2",
    "@odata.type": "#Processor.v1_5_0.Processor",
    "Description": "Intel(R) Xeon(R) CPU E5-2695 v3 @ 2.30GHz/120W 14C/35MB Cache/DDR4 2133MHz",
    "Id": "2",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) CPU E5-2695 v3 @ 2.30GHz",
    "Name": "CPU2",
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "6",
        "EffectiveModel": "63",
        "Step": "2",
        "VendorId": "Intel(R) Corporation"
    },
    "ProcessorType": "CPU",
    "Socket": "CPU2",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TotalCores": 14,
    "TotalEnabledCores": 14,
    "TotalThreads": 14
}
```

## /redfish/v1/Systems/FCH2017V24J/SecureBoot

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/SecureBoot",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/SecureBoot",
    "@odata.type": "#SecureBoot.v1_0_4.SecureBoot",
    "Description": "UEFI SecureBoot configuration of this system",
    "Id": "SecureBoot",
    "Name": "SecureBoot",
    "SecureBootCurrentBoot": "Disabled",
    "SecureBootEnable": false
}
```

## /redfish/v1/Systems/FCH2017V24J/SimpleStorage

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/SimpleStorage",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/SimpleStorage",
    "@odata.type": "#SimpleStorageCollection.SimpleStorageCollection",
    "Description": "Collection of storage controllers for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/SimpleStorage/SLOT-HBA"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Simple Storage Collection"
}
```

## /redfish/v1/Systems/FCH2017V24J/SimpleStorage/SLOT-HBA

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/SimpleStorage/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/SimpleStorage/SLOT-HBA",
    "@odata.type": "#SimpleStorage.v1_2_1.SimpleStorage",
    "Description": "Simple Storage Controller",
    "Devices": [],
    "Id": "SLOT-HBA",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "Name": "Cisco 12G SAS Modular Raid Controller",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/Storage

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage",
    "@odata.type": "#StorageCollection.StorageCollection",
    "Description": "Collection of storage resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Storage Collection"
}
```

## /redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0

```null
```

## /redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Drives/SLOT-1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Drives/SLOT-1",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Drives/SLOT-1/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapacityBytes": 63863521280,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        },
        "Volumes": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/SCU"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/HUU"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/Drivers"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/UserPartition"
            }
        ],
        "Volumes@odata.count": 4
    },
    "Location": [
        {
            "Info": "SLOT-1"
        }
    ],
    "Manufacturer": "SD",
    "Model": "SE64G",
    "Name": "SLOT-1",
    "Revision": "8.0",
    "SerialNumber": "0x311093",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Drives/SLOT-2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Drives/SLOT-2",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Drives/SLOT-2/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapacityBytes": 63863521280,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        },
        "Volumes": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/Hypervisor"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/NA"
            }
        ],
        "Volumes@odata.count": 2
    },
    "Location": [
        {
            "Info": "SLOT-2"
        }
    ],
    "Manufacturer": "SD",
    "Model": "SE64G",
    "Name": "SLOT-2",
    "Revision": "8.0",
    "SerialNumber": "0x311024",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/Drivers

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Volumes/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/Drivers",
    "@odata.type": "#Volume.v1_0_3.Volume",
    "Actions": {
        "#Volume.Initialize": {
            "target": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/Drivers/Actions/Volume.Initialize"
        }
    },
    "CapacityBytes": 8589934592,
    "Encrypted": false,
    "Id": "3",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Drives/SLOT-1"
            }
        ],
        "Drives@odata.count": 1
    },
    "Name": "Drivers",
    "Operations": [
        {
            "OperationName": "No operation in progress"
        }
    ],
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolumeType": "NonRedundant"
}
```

## /redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/HUU

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Volumes/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/HUU",
    "@odata.type": "#Volume.v1_0_3.Volume",
    "Actions": {
        "#Volume.Initialize": {
            "target": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/HUU/Actions/Volume.Initialize"
        }
    },
    "CapacityBytes": 1610612736,
    "Encrypted": false,
    "Id": "2",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Drives/SLOT-1"
            }
        ],
        "Drives@odata.count": 1
    },
    "Name": "HUU",
    "Operations": [
        {
            "OperationName": "No operation in progress"
        }
    ],
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolumeType": "NonRedundant"
}
```

## /redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/Hypervisor

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Volumes/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/Hypervisor",
    "@odata.type": "#Volume.v1_0_3.Volume",
    "Actions": {
        "#Volume.Initialize": {
            "target": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/Hypervisor/Actions/Volume.Initialize"
        }
    },
    "CapacityBytes": 63859326976,
    "Encrypted": false,
    "Id": "5",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Drives/SLOT-2"
            }
        ],
        "Drives@odata.count": 1
    },
    "Name": "Hypervisor",
    "Operations": [
        {
            "OperationName": "No operation in progress"
        }
    ],
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolumeType": "NonRedundant"
}
```

## /redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/NA

```null
```

## /redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/SCU

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Volumes/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/SCU",
    "@odata.type": "#Volume.v1_0_3.Volume",
    "Actions": {
        "#Volume.Initialize": {
            "target": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/SCU/Actions/Volume.Initialize"
        }
    },
    "CapacityBytes": 2684354560,
    "Encrypted": false,
    "Id": "1",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Drives/SLOT-1"
            }
        ],
        "Drives@odata.count": 1
    },
    "Name": "SCU",
    "Operations": [
        {
            "OperationName": "No operation in progress"
        }
    ],
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolumeType": "NonRedundant"
}
```

## /redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/UserPartition

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Volumes/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/UserPartition",
    "@odata.type": "#Volume.v1_0_3.Volume",
    "Actions": {
        "#Volume.Initialize": {
            "target": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Volumes/UserPartition/Actions/Volume.Initialize"
        }
    },
    "CapacityBytes": 42384490496,
    "Encrypted": false,
    "Id": "4",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Drives/SLOT-1"
            }
        ],
        "Drives@odata.count": 1
    },
    "Name": "UserPartition",
    "Operations": [
        {
            "OperationName": "No operation in progress"
        }
    ],
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolumeType": "NonRedundant"
}
```

## /redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA",
    "@odata.type": "#Storage.v1_5_0.Storage",
    "Actions": {
        "#Storage.SetEncryptionKey": {
            "SecurityKey@Redfish.AllowableValues": [
                "Security Key"
            ],
            "SecurityKeyId@Redfish.AllowableValues": [
                "Security Key Identifier"
            ],
            "target": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Actions/Storage.SetEncryptionKey"
        }
    },
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-2"
        }
    ],
    "Id": "SLOT-HBA",
    "Links": {
        "Enclosures": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ]
    },
    "Name": "SLOT-HBA",
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA#StorageControllers",
            "CacheSummary": {
                "TotalCacheSizeMiB": 3519
            },
            "FirmwareVersion": "4.620.00-7341",
            "Manufacturer": "LSI Logic",
            "MemberId": "RAID",
            "Model": "Cisco 12G SAS Modular Raid Controller",
            "Name": "Cisco 12G SAS Modular Raid Controller",
            "SerialNumber": "SV61227054",
            "Status": {
                "Health": "OK",
                "HealthRollup": "OK",
                "State": "Enabled"
            },
            "SupportedControllerProtocols": [
                "PCIe"
            ],
            "SupportedDeviceProtocols": [
                "SAS"
            ]
        }
    ],
    "Volumes": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Volumes"
    }
}
```

## /redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-1",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-1/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 1200243081216,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-1",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        },
        "Volumes": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Volumes/VD-0"
            }
        ],
        "Volumes@odata.count": 1
    },
    "Location": [
        {
            "Info": "SLOT-1"
        }
    ],
    "Manufacturer": "SEAGATE",
    "MediaType": "HDD",
    "Model": "ST1200MM0088",
    "Name": "PD-1",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "N0A4",
    "SerialNumber": "Z40064XY0000R630FDZW",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-2",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-2/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 1200243081216,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-2",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        },
        "Volumes": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Volumes/VD-0"
            }
        ],
        "Volumes@odata.count": 1
    },
    "Location": [
        {
            "Info": "SLOT-2"
        }
    ],
    "Manufacturer": "SEAGATE",
    "MediaType": "HDD",
    "Model": "ST1200MM0088",
    "Name": "PD-2",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "N0A4",
    "SerialNumber": "Z4007WV60000R632VEJS",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Volumes

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Volumes",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection of Storage resource instances",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Volumes/VD-0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Volumes Collection"
}
```

## /redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Volumes/VD-0

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Volumes/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Volumes/VD-0",
    "@odata.type": "#Volume.v1_0_3.Volume",
    "Actions": {
        "#Volume.Initialize": {
            "target": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Volumes/VD-0/Actions/Volume.Initialize"
        }
    },
    "BlockSizeBytes": 65536,
    "CapacityBytes": 1198999470080,
    "Encrypted": false,
    "Id": "0",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-2"
            }
        ],
        "Drives@odata.count": 2
    },
    "Name": "",
    "Operations": [
        {
            "OperationName": "No operation in progress",
            "PercentageComplete": 0
        }
    ],
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolumeType": "Mirrored"
}
```

