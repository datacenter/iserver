# Resource: /redfish/v1/Systems

Vendor | Model
--- | ---
Cisco | UCSC-C240-M4SX

## /redfish/v1/Systems

```{
    "@odata.context": "/redfish/v1/$metadata#Systems",
    "@odata.id": "/redfish/v1/Systems",
    "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection",
    "Description": "Collection of Computer Systems",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Computer System Collection"
}
```

## /redfish/v1/Systems/FCH2017V1J7

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7",
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
            "target": "/redfish/v1/Systems/FCH2017V1J7/Actions/ComputerSystem.Reset"
        }
    },
    "AssetTag": "",
    "Bios": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Bios"
    },
    "BiosVersion": "C240M4.4.1.2c.0.0202211902",
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
    "Description": "comp1-p3b-eu-spdc-FCH2017V1J7",
    "EthernetInterfaces": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces"
    },
    "HostName": "comp1-p3b-eu-spdc-FCH2017V1J7",
    "HostWatchdogTimer": {
        "FunctionEnabled": false,
        "Status": {
            "State": "Disabled"
        },
        "TimeoutAction": "PowerDown",
        "WarningAction": "None"
    },
    "Id": "FCH2017V1J7",
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
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/LogServices"
    },
    "Manufacturer": "Cisco Systems Inc",
    "Memory": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Memory"
    },
    "MemorySummary": {
        "Status": {
            "Health": "OK",
            "HealthRollup": "OK"
        },
        "TotalSystemMemoryGiB": 128
    },
    "Model": "UCSC-C240-M4SX",
    "Name": "UCS C240 M4SX",
    "NetworkInterfaces": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces"
    },
    "Oem": {
        "Cisco": {
            "SystemEffectiveMemory": 128,
            "SystemEffectiveSpeed": 1866
        }
    },
    "PCIeDevices": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/L"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/MLOM"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/HBA"
        }
    ],
    "PCIeDevices@odata.count": 5,
    "PCIeFunctions": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/L/PCIeFunctions/L"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/3/PCIeFunctions/3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/5/PCIeFunctions/5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/MLOM/PCIeFunctions/MLOM"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/HBA/PCIeFunctions/HBA"
        }
    ],
    "PCIeFunctions@odata.count": 5,
    "PowerRestorePolicy": "AlwaysOff",
    "PowerState": "Off",
    "ProcessorSummary": {
        "Count": 2,
        "Model": "Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz"
    },
    "Processors": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Processors"
    },
    "SecureBoot": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/SecureBoot"
    },
    "SerialNumber": "FCH2017V1J7",
    "SimpleStorage": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/SimpleStorage"
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Storage": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage"
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
    "UUID": "BB16A414-DF14-47B4-8889-BAD3872F8926"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Bios

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Bios",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Bios",
    "@odata.type": "#Bios.v1_0_4.Bios",
    "Actions": {
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Bios/Actions/Bios.ResetBios"
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
        "CmciEnable": "Enabled",
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
        "PcieSlot1OptionROM": "Disabled",
        "PcieSlot2OptionROM": "Disabled",
        "PcieSlot3OptionROM": "Disabled",
        "PcieSlot4OptionROM": "Disabled",
        "PcieSlot5OptionROM": "Disabled",
        "PcieSlot6OptionROM": "Disabled",
        "PcieSlotFLOMLinkSpeed": "GEN3",
        "PcieSlotHBALinkSpeed": "GEN3",
        "PcieSlotHBAOptionROM": "Enabled",
        "PcieSlotMLOMOptionROM": "Enabled",
        "PcieSlotN1OptionROM": "Disabled",
        "PcieSlotN2OptionROM": "Disabled",
        "PcieSlotRiser1Slot1LinkSpeed": "GEN3",
        "PcieSlotRiser1Slot2LinkSpeed": "GEN3",
        "PcieSlotRiser1Slot3LinkSpeed": "GEN3",
        "PcieSlotRiser2Slot4LinkSpeed": "GEN3",
        "PcieSlotRiser2Slot5LinkSpeed": "GEN3",
        "PcieSlotRiser2Slot6LinkSpeed": "GEN3",
        "PcieSlotSSDSlot1LinkSpeed": "GEN3",
        "PcieSlotSSDSlot2LinkSpeed": "GEN3",
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

## /redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Description": "Collection of EthernetInterfaces for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/5.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/5.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/L.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/L.2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/MLOM.0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/MLOM.1"
        }
    ],
    "Members@odata.count": 10,
    "Name": "Ethernet Interfaces Collection"
}
```

## /redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "3.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ef:6b:a8",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ef:6b:a8"
}
```

## /redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "3.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ef:6b:a9",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ef:6b:a9"
}
```

## /redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.3

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.3",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "3.3",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ef:6b:aa",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ef:6b:aa"
}
```

## /redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.4

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.4",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "3.4",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "3c:fd:fe:ef:6b:ab",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "3c:fd:fe:ef:6b:ab"
}
```

## /redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/5.1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/5.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "5.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "90:e2:ba:0e:51:dc",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "90:e2:ba:0e:51:dc"
}
```

## /redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/5.2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/5.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "5.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "90:e2:ba:0e:51:dd",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "90:e2:ba:0e:51:dd"
}
```

## /redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/L.1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/L.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "L.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "00:3a:7d:d3:eb:74",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "00:3a:7d:d3:eb:74"
}
```

## /redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/L.2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/L.2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "L.2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "00:3a:7d:d3:eb:75",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "00:3a:7d:d3:eb:75"
}
```

## /redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/MLOM.0

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/MLOM.0",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "MLOM.0",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "00:3A:7D:D0:4A:B2",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "00:3A:7D:D0:4A:B2"
}
```

## /redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/MLOM.1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/MLOM.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "MLOM.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "00:3A:7D:D0:4A:B3",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "00:3A:7D:D0:4A:B3"
}
```

## /redfish/v1/Systems/FCH2017V1J7/LogServices

```
```

## /redfish/v1/Systems/FCH2017V1J7/Memory

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Memory",
    "@odata.type": "#MemoryCollection.MemoryCollection",
    "Description": "Collection of Memory resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Memory/DIMM_A1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Memory/DIMM_B1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Memory/DIMM_E1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Memory/DIMM_F1"
        }
    ],
    "Members@odata.count": 4,
    "Name": "Memory Collection"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Memory/DIMM_A1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Memory/DIMM_A1",
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
    "SerialNumber": "3195D246",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH2017V1J7/Memory/DIMM_B1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Memory/DIMM_B1",
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
    "SerialNumber": "3195D193",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH2017V1J7/Memory/DIMM_E1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Memory/DIMM_E1",
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
    "SerialNumber": "3195D1AD",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH2017V1J7/Memory/DIMM_F1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Memory/DIMM_F1",
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
    "SerialNumber": "3195D24C",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/NetworkInterfaces",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces",
    "@odata.type": "#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "Description": "Collection of NetworkInterface resource instances for this system",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "NetworkInterface Collection"
}
```

## /redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/eth0

```null
```

## /redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/eth1

```null
```

## /redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/fc0

```null
```

## /redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/fc1

```null
```

## /redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/i0

```null
```

## /redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/i1

```null
```

## /redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/vs0

```null
```

## /redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/vs1

```null
```

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/3

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/3",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80009E63-1.823.2",
    "Id": "3",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/3/PCIeFunctions/3"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco(R) Ethernet Converged NIC X710-DA4",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/3/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/3/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/3/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/3/PCIeFunctions/3"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/3/PCIeFunctions/3

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/3/PCIeFunctions/3",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1572",
    "Id": "3",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.2"
            }
        ],
        "EthernetInterfaces@odata.count": 4,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/3"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Cisco(R) Ethernet Converged NIC X710-DA4",
    "SubsystemId": "0x013b",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/5

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/5",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x800008A4-1.812.1",
    "Id": "5",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/5/PCIeFunctions/5"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel X520-DA2 10 Gbps 2 port NIC",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/5/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/5/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/5/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/5/PCIeFunctions/5"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/5/PCIeFunctions/5

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/5/PCIeFunctions/5",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x10fb",
    "Id": "5",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/5.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/5.2"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/5"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel X520-DA2 10 Gbps 2 port NIC",
    "SubsystemId": "0x000c",
    "SubsystemVendorId": "0x8086",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/HBA

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/HBA",
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
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/HBA/PCIeFunctions/HBA"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco 12G SAS Modular Raid Controller",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/HBA/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/HBA/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/HBA/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/HBA/PCIeFunctions/HBA"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/HBA/PCIeFunctions/HBA

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/HBA/PCIeFunctions/HBA",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x005d",
    "Id": "HBA",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-7"
            }
        ],
        "Drives@odata.count": 7,
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/HBA"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA"
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

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/L

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/L",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80000E75-1.819.0",
    "Id": "L",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/L/PCIeFunctions/L"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel(R) I350 1 Gbps Network Controller",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/L/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/L/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/L/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/L/PCIeFunctions/L"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/L/PCIeFunctions/L

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/L/PCIeFunctions/L",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1521",
    "Id": "L",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/L.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/L.2"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/L"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel(R) I350 1 Gbps Network Controller",
    "SubsystemId": "0x00d6",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/MLOM",
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
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/MLOM/PCIeFunctions/MLOM"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "UCS VIC 1227 10Gbps 2 port CNA SFP+",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/MLOM/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/MLOM/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/MLOM/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/MLOM/PCIeFunctions/MLOM"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/FCH2017V1J7/PCIeDevices/MLOM/PCIeFunctions/MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/MLOM/PCIeFunctions/MLOM",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0042",
    "Id": "MLOM",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/MLOM.0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/MLOM.1"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/eth0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/eth1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/vs0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/vs1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/i0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/i1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/fc0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/NetworkInterfaces/MLOM/NetworkDeviceFunctions/fc1"
            }
        ],
        "NetworkDeviceFunctions@odata.count": 8,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/PCIeDevices/MLOM"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "UCS VIC 1227 10Gbps 2 port CNA SFP+",
    "SubsystemId": "0x012e",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1137"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Processors

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Processors",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Processors",
    "@odata.type": "#ProcessorCollection.ProcessorCollection",
    "Description": "Collection of Processors for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Processors/CPU1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Processors/CPU2"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Processors Collection"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Processors/CPU1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Processors/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Processors/CPU1",
    "@odata.type": "#Processor.v1_5_0.Processor",
    "Description": "Intel(R) Xeon(R) E5-2630 v3 @ 2.40GHz",
    "Id": "1",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz",
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
    "TotalCores": 8,
    "TotalEnabledCores": 8,
    "TotalThreads": 8
}
```

## /redfish/v1/Systems/FCH2017V1J7/Processors/CPU2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Processors/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Processors/CPU2",
    "@odata.type": "#Processor.v1_5_0.Processor",
    "Description": "Intel(R) Xeon(R) E5-2630 v3 @ 2.40GHz",
    "Id": "2",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz",
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
    "TotalCores": 8,
    "TotalEnabledCores": 8,
    "TotalThreads": 8
}
```

## /redfish/v1/Systems/FCH2017V1J7/SecureBoot

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/SecureBoot",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/SecureBoot",
    "@odata.type": "#SecureBoot.v1_0_4.SecureBoot",
    "Description": "UEFI SecureBoot configuration of this system",
    "Id": "SecureBoot",
    "Name": "SecureBoot",
    "SecureBootCurrentBoot": "Disabled",
    "SecureBootEnable": false
}
```

## /redfish/v1/Systems/FCH2017V1J7/SimpleStorage

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/SimpleStorage",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/SimpleStorage",
    "@odata.type": "#SimpleStorageCollection.SimpleStorageCollection",
    "Description": "Collection of storage controllers for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/SimpleStorage/SLOT-HBA"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Simple Storage Collection"
}
```

## /redfish/v1/Systems/FCH2017V1J7/SimpleStorage/SLOT-HBA

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/SimpleStorage/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/SimpleStorage/SLOT-HBA",
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

## /redfish/v1/Systems/FCH2017V1J7/Storage

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage",
    "@odata.type": "#StorageCollection.StorageCollection",
    "Description": "Collection of storage resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Storage Collection"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0",
    "@odata.type": "#Storage.v1_5_0.Storage",
    "Actions": {
        "#Storage.SetEncryptionKey": {
            "SecurityKey@Redfish.AllowableValues": [
                "Security Key"
            ],
            "SecurityKeyId@Redfish.AllowableValues": [
                "Security Key Identifier"
            ],
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Actions/Storage.SetEncryptionKey"
        }
    },
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-2"
        }
    ],
    "Id": "FlexFlash-0",
    "Links": {
        "Enclosures": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ]
    },
    "Name": "FlexFlash-0",
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0#StorageControllers",
            "FirmwareVersion": "1.3.2 build 176",
            "Manufacturer": "Cypress",
            "MemberId": "FlexFlash",
            "Model": "Cisco FlexFlash",
            "Name": "Cisco FlexFlash",
            "Status": {
                "Health": "OK",
                "HealthRollup": "OK",
                "State": "Enabled"
            },
            "SupportedControllerProtocols": [
                "USB"
            ]
        }
    ],
    "Volumes": {
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Volumes"
    }
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-1",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-1/Actions/Drive.SecureErase"
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
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Volumes/Hypervisor"
            }
        ],
        "Volumes@odata.count": 1
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
    "SerialNumber": "0x310c16",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-2",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-2/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapacityBytes": 63863521280,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareType": "Dedicated",
    "Id": "2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        },
        "Volumes": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Volumes/Hypervisor"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Volumes/NA"
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
    "SerialNumber": "0x310c0d",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Volumes

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Volumes",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection of Storage resource instances",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Volumes/Hypervisor"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Volumes Collection"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Volumes/Hypervisor

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Volumes/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Volumes/Hypervisor",
    "@odata.type": "#Volume.v1_0_3.Volume",
    "Actions": {
        "#Volume.Initialize": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Volumes/Hypervisor/Actions/Volume.Initialize"
        }
    },
    "CapacityBytes": 63859326976,
    "Encrypted": false,
    "Id": "1",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-2"
            }
        ],
        "Drives@odata.count": 2
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
    "VolumeType": "Mirrored"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Volumes/NA

```null
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA",
    "@odata.type": "#Storage.v1_5_0.Storage",
    "Actions": {
        "#Storage.SetEncryptionKey": {
            "SecurityKey@Redfish.AllowableValues": [
                "Security Key"
            ],
            "SecurityKeyId@Redfish.AllowableValues": [
                "Security Key Identifier"
            ],
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Actions/Storage.SetEncryptionKey"
        }
    },
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-7"
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
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA#StorageControllers",
            "CacheSummary": {
                "TotalCacheSizeMiB": 0
            },
            "FirmwareVersion": "4.620.01-7340",
            "Manufacturer": "LSI Logic",
            "MemberId": "RAID",
            "Model": "Cisco 12G SAS Modular Raid Controller",
            "Name": "Cisco 12G SAS Modular Raid Controller",
            "SerialNumber": "SV60910918",
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
        "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes"
    }
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-1",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-1/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 6,
    "CapacityBytes": 480103104512,
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
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "SLOT-1"
        }
    ],
    "Manufacturer": "ATA",
    "MediaType": "SSD",
    "Model": "INTEL SSDSC2BB480G6K",
    "Name": "PD-1",
    "PredictedMediaLifeLeftPercent": 76,
    "Protocol": "SATA",
    "Revision": "G201CS01",
    "SerialNumber": "BTWA6150014L480FGN",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-2",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-2/Actions/Drive.SecureErase"
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
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes/VD-0"
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
    "SerialNumber": "Z4006JEL0000R6302WLG",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-3

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-3",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-3/Actions/Drive.SecureErase"
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
    "Id": "PD-3",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        },
        "Volumes": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes/VD-0"
            }
        ],
        "Volumes@odata.count": 1
    },
    "Location": [
        {
            "Info": "SLOT-3"
        }
    ],
    "Manufacturer": "SEAGATE",
    "MediaType": "HDD",
    "Model": "ST1200MM0088",
    "Name": "PD-3",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "N0A4",
    "SerialNumber": "Z40053750000R628KD8C",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-4

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-4",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-4/Actions/Drive.SecureErase"
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
    "Id": "PD-4",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        },
        "Volumes": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes/VD-0"
            }
        ],
        "Volumes@odata.count": 1
    },
    "Location": [
        {
            "Info": "SLOT-4"
        }
    ],
    "Manufacturer": "SEAGATE",
    "MediaType": "HDD",
    "Model": "ST1200MM0088",
    "Name": "PD-4",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "N0A4",
    "SerialNumber": "Z4006CWZ0000R630FCDT",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-5

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-5",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-5/Actions/Drive.SecureErase"
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
    "Id": "PD-5",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        },
        "Volumes": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes/VD-0"
            }
        ],
        "Volumes@odata.count": 1
    },
    "Location": [
        {
            "Info": "SLOT-5"
        }
    ],
    "Manufacturer": "SEAGATE",
    "MediaType": "HDD",
    "Model": "ST1200MM0088",
    "Name": "PD-5",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "N0A4",
    "SerialNumber": "Z40069JP0000R629MV05",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-6

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-6",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-6/Actions/Drive.SecureErase"
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
    "Id": "PD-6",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        },
        "Volumes": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes/VD-0"
            }
        ],
        "Volumes@odata.count": 1
    },
    "Location": [
        {
            "Info": "SLOT-6"
        }
    ],
    "Manufacturer": "SEAGATE",
    "MediaType": "HDD",
    "Model": "ST1200MM0088",
    "Name": "PD-6",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "N0A4",
    "SerialNumber": "Z4006CGC0000R629MUZ8",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-7

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-7",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-7/Actions/Drive.SecureErase"
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
    "Id": "PD-7",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        },
        "Volumes": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes/VD-0"
            }
        ],
        "Volumes@odata.count": 1
    },
    "Location": [
        {
            "Info": "SLOT-7"
        }
    ],
    "Manufacturer": "SEAGATE",
    "MediaType": "HDD",
    "Model": "ST1200MM0088",
    "Name": "PD-7",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "N0A4",
    "SerialNumber": "Z400694R0000R629MMEM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Volumes",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection of Storage resource instances",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes/VD-0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Volumes Collection"
}
```

## /redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes/VD-0

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Volumes/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes/VD-0",
    "@odata.type": "#Volume.v1_0_3.Volume",
    "Actions": {
        "#Volume.Initialize": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes/VD-0/Actions/Volume.Initialize"
        }
    },
    "BlockSizeBytes": 65536,
    "CapacityBytes": 3596998410240,
    "Encrypted": false,
    "Id": "0",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-7"
            }
        ],
        "Drives@odata.count": 6
    },
    "Name": "RAID10_234576",
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
    "VolumeType": "SpannedMirrors"
}
```

