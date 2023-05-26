# Resource: /redfish/v1/Systems

Vendor | Model
--- | ---
Cisco | UCSS-S3260

## /redfish/v1/Systems

```{
    "@odata.context": "/redfish/v1/$metadata#Systems",
    "@odata.id": "/redfish/v1/Systems",
    "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection",
    "Description": "Collection of Computer Systems",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Computer System Collection"
}
```

## /redfish/v1/Systems/FCH21067808

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808",
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
            "target": "/redfish/v1/Systems/FCH21067808/Actions/ComputerSystem.Reset"
        }
    },
    "Bios": {
        "@odata.id": "/redfish/v1/Systems/FCH21067808/Bios"
    },
    "BiosVersion": "C3X60M4.4.1.2c.0.0202211901",
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
    "Description": "",
    "EthernetInterfaces": {
        "@odata.id": "/redfish/v1/Systems/FCH21067808/EthernetInterfaces"
    },
    "HostName": "ynas-eu-spdc-FCH21067808",
    "HostWatchdogTimer": {
        "FunctionEnabled": false,
        "Status": {
            "State": "Disabled"
        },
        "TimeoutAction": "PowerDown",
        "WarningAction": "None"
    },
    "Id": "FCH21067808",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/CMC"
            }
        ],
        "CooledBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/CMC/Thermal"
            }
        ],
        "ManagedBy": [
            {
                "@odata.id": "/redfish/v1/Managers/BMC1"
            }
        ],
        "PoweredBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/CMC/Power"
            }
        ]
    },
    "LogServices": {
        "@odata.id": "/redfish/v1/Systems/FCH21067808/LogServices"
    },
    "Manufacturer": "Cisco Systems",
    "Memory": {
        "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory"
    },
    "MemorySummary": {
        "Status": {
            "Health": "OK",
            "HealthRollup": "OK"
        },
        "TotalSystemMemoryGiB": 256
    },
    "Model": "UCS S3260",
    "Name": "UCS S3260",
    "NetworkInterfaces": {
        "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces"
    },
    "PCIeDevices": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SIOC1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SBMezz1"
        }
    ],
    "PCIeDevices@odata.count": 2,
    "PCIeFunctions": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SIOC1/PCIeFunctions/SIOC1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SBMezz1/PCIeFunctions/SBMezz1"
        }
    ],
    "PCIeFunctions@odata.count": 2,
    "PowerRestorePolicy": "AlwaysOff",
    "PowerState": "On",
    "ProcessorSummary": {
        "Count": 2,
        "Model": "Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz"
    },
    "Processors": {
        "@odata.id": "/redfish/v1/Systems/FCH21067808/Processors"
    },
    "SecureBoot": {
        "@odata.id": "/redfish/v1/Systems/FCH21067808/SecureBoot"
    },
    "SerialNumber": "FCH21067808",
    "SimpleStorage": {
        "@odata.id": "/redfish/v1/Systems/FCH21067808/SimpleStorage"
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Storage": {
        "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage"
    },
    "SystemType": "Physical",
    "UUID": "937E6EE7-0EA5-42CE-9EAE-A960BF1F0BAD"
}
```

## /redfish/v1/Systems/FCH21067808/Bios

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Bios",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Bios",
    "@odata.type": "#Bios.v1_0_4.Bios",
    "Actions": {
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/FCH21067808/Bios/Actions/Bios.ResetBios"
        }
    },
    "Attributes": {
        "ATS": "Enabled",
        "AdjacentCacheLinePrefetch": "Enabled",
        "AllUsbDevices": "Enabled",
        "Altitude": "300 M",
        "AutonumousCstateEnable": "Disabled",
        "BaudRate": "115200",
        "BootPerformanceMode": "Max Performance",
        "CPUPowerManagement": "Performance",
        "ChannelInterLeave": "Auto",
        "CmciEnable": "Enabled",
        "CoherencySupport": "Disabled",
        "ConsoleRedir": "COM 0",
        "CoreMultiProcessing": "All",
        "CpuEngPerfBias": "Balanced Performance",
        "CpuPerformanceProfile": "Enterprise",
        "DcuIpPrefetch": "Enabled",
        "DcuStreamerPrefetch": "Enabled",
        "DemandScrub": "Enabled",
        "DirectCacheAccess": "Auto",
        "EnhancedIntelSpeedStep": "Enabled",
        "ExecuteDisable": "Enabled",
        "FRB_2": "Enabled",
        "FlowCtrl": "None",
        "HWPMEnable": "Disabled",
        "HardwarePrefetch": "Enabled",
        "IOEMezz1LinkSpeed": "Auto",
        "IOEMezz1OptionROM": "Enabled",
        "IOENVMe1LinkSpeed": "Auto",
        "IOENVMe1OptionROM": "Enabled",
        "IOENVMe2LinkSpeed": "Auto",
        "IOENVMe2OptionROM": "Enabled",
        "IOESlot1LinkSpeed": "Auto",
        "IOESlot1OptionROM": "Enabled",
        "IOESlot2LinkSpeed": "Auto",
        "IOESlot2OptionROM": "Enabled",
        "IntelHyperThread": "Enabled",
        "IntelTurboBoostTech": "Enabled",
        "IntelVT": "Enabled",
        "IntelVTD": "Enabled",
        "InterruptRemap": "Enabled",
        "LegacyUSBSupport": "Enabled",
        "LocalX2Apic": "XAPIC",
        "MemoryMappedIOAbove4GB": "Enabled",
        "NUMAOptimize": "Enabled",
        "OSBootWatchdogTimer": "Disabled",
        "OSBootWatchdogTimerPolicy": "Power Down",
        "OSBootWatchdogTimerTimeout": "10 mins",
        "PCIROMCLP": "Disabled",
        "POPSupport": "Disabled",
        "PackageCstateLimit": "C6 Retention",
        "PassThroughDMA": "Disabled",
        "PatrolScrub": "Enabled",
        "PchUsb30Mode": "Disabled",
        "PcieOptionROMs": "Enabled",
        "ProcessorC1E": "Enabled",
        "ProcessorC3Report": "Disabled",
        "ProcessorC6Report": "Enabled",
        "PsdCoordType": "HW ALL",
        "PuttyFunctionKeyPad": "ESCN",
        "PwrPerfTuning": "OS",
        "QPILinkFrequency": "Auto",
        "QpiSnoopMode": "Auto",
        "RankInterLeave": "Auto",
        "RedirectionAfterPOST": "Always Enable",
        "SBMezz1LinkSpeed": "Auto",
        "SBMezz1OptionROM": "Enabled",
        "SBMezz2LinkSpeed": "Auto",
        "SBMezz2OptionROM": "Enabled",
        "SBNVMe1LinkSpeed": "Auto",
        "SBNVMe1OptionROM": "Enabled",
        "SIOC1LinkSpeed": "Auto",
        "SIOC1OptionROM": "Enabled",
        "SIOC2LinkSpeed": "Auto",
        "SIOC2OptionROM": "Enabled",
        "SataModeSelect": "AHCI",
        "SelectMemoryRAS": "Maximum Performance",
        "SrIov": "Enabled",
        "TPMAdminCtrl": "Enabled",
        "TerminalType": "VT100",
        "UsbEmul6064": "Enabled",
        "UsbPortKVM": "Enabled",
        "UsbPortRear": "Enabled",
        "UsbPortVMedia": "Enabled",
        "UsbXhciSupport": "Enabled",
        "WorkLdConfig": "Balanced",
        "cdnEnable": "Disabled",
        "comSpcrEnable": "Disabled"
    },
    "Description": "BIOS Configuration Current Settings",
    "Id": "BiosToken",
    "Name": "BiosToken"
}
```

## /redfish/v1/Systems/FCH21067808/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Description": "Collection of EthernetInterfaces for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/EthernetInterfaces/SIOC1.0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/EthernetInterfaces/SIOC1.1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Ethernet Interfaces Collection"
}
```

## /redfish/v1/Systems/FCH21067808/EthernetInterfaces/SIOC1.0

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/EthernetInterfaces/SIOC1.0",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "SIOC1.0",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/Server1"
        }
    },
    "MACAddress": "2C:5A:0F:6F:6B:F4",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "2C:5A:0F:6F:6B:F4"
}
```

## /redfish/v1/Systems/FCH21067808/EthernetInterfaces/SIOC1.1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/EthernetInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/EthernetInterfaces/SIOC1.1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "Description": "Network Interface",
    "Id": "SIOC1.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/Server1"
        }
    },
    "MACAddress": "2C:5A:0F:6F:6B:F5",
    "Name": "Ethernet Interface",
    "PermanentMACAddress": "2C:5A:0F:6F:6B:F5"
}
```

## /redfish/v1/Systems/FCH21067808/LogServices

```
```

## /redfish/v1/Systems/FCH21067808/Memory

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory",
    "@odata.type": "#MemoryCollection.MemoryCollection",
    "Description": "Collection of Memory resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_A1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_B1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_C1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_D1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_E1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_F1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_G1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_H1"
        }
    ],
    "Members@odata.count": 8,
    "Name": "Memory Collection"
}
```

## /redfish/v1/Systems/FCH21067808/Memory/DIMM_A1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_A1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_A1",
    "Id": "1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/Server1"
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
    "OperatingSpeedMhz": 2400,
    "PartNumber": "M393A4K40BB1-CRC",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "34C5C2D5",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH21067808/Memory/DIMM_B1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_B1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_B1",
    "Id": "3",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/Server1"
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
    "OperatingSpeedMhz": 2400,
    "PartNumber": "M393A4K40BB1-CRC",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "34C5C315",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH21067808/Memory/DIMM_C1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_C1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_C1",
    "Id": "5",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/Server1"
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
    "OperatingSpeedMhz": 2400,
    "PartNumber": "M393A4K40BB1-CRC",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "34C5C2D3",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH21067808/Memory/DIMM_D1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_D1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_D1",
    "Id": "7",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/Server1"
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
    "OperatingSpeedMhz": 2400,
    "PartNumber": "M393A4K40BB1-CRC",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "34C5C2D6",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH21067808/Memory/DIMM_E1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_E1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_E1",
    "Id": "9",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/Server1"
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
    "OperatingSpeedMhz": 2400,
    "PartNumber": "M393A4K40BB1-CRC",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "34C5D61D",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH21067808/Memory/DIMM_F1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_F1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_F1",
    "Id": "11",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/Server1"
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
    "OperatingSpeedMhz": 2400,
    "PartNumber": "M393A4K40BB1-CRC",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "34C5CBA2",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH21067808/Memory/DIMM_G1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_G1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_G1",
    "Id": "13",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/Server1"
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
    "OperatingSpeedMhz": 2400,
    "PartNumber": "M393A4K40BB1-CRC",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "34C5C2D7",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH21067808/Memory/DIMM_H1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Memory/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Memory/DIMM_H1",
    "@odata.type": "#Memory.v1_7_0.Memory",
    "CapacityMiB": 32768,
    "DataWidthBits": 64,
    "Description": "Computer Memory",
    "DeviceLocator": "DIMM_H1",
    "Id": "15",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/Server1"
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
    "OperatingSpeedMhz": 2400,
    "PartNumber": "M393A4K40BB1-CRC",
    "SecurityCapabilities": {
        "PassphraseCapable": false
    },
    "SerialNumber": "34C5C31C",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH21067808/NetworkInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/NetworkInterfaces",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces",
    "@odata.type": "#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "Description": "Collection of NetworkInterface resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "NetworkInterface Collection"
}
```

## /redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/NetworkInterfaces/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1",
    "@odata.type": "#NetworkInterface.v1_1_1.NetworkInterface",
    "Description": "It represents the properties for Adapter Card SIOC1",
    "Id": "UCSC-C3260-SIOC",
    "Links": {
        "NetworkAdapter": {
            "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1"
        }
    },
    "Name": "Adapter Card SIOC1",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkPorts"
    },
    "Status": {
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/NetworkInterfaces/Members/$entity/NetworkDeviceFunctions",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions",
    "@odata.type": "#NetworkDeviceFunctionCollection.NetworkDeviceFunctionCollection",
    "Description": "Collection of NetworkDeviceFunction resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/eth0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/eth1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/fc0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/fc1"
        }
    ],
    "Members@odata.count": 4,
    "Name": "NetworkDeviceFunction Collection"
}
```

## /redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/eth0

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/NetworkInterfaces/Members/$entity/NetworkDeviceFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/eth0",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "2C:5A:0F:6F:6C:00",
        "MTUSize": 9000,
        "VLAN": {
            "VLANEnable": true
        }
    },
    "Id": "eth0",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkPorts/Port-0"
        }
    },
    "Name": "eth0"
}
```

## /redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/eth1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/NetworkInterfaces/Members/$entity/NetworkDeviceFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/eth1",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "2C:5A:0F:6F:6C:01",
        "MTUSize": 9000,
        "VLAN": {
            "VLANEnable": true
        }
    },
    "Id": "eth1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkPorts/Port-1"
        }
    },
    "Name": "eth1"
}
```

## /redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/fc0

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/NetworkInterfaces/Members/$entity/NetworkDeviceFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/fc0",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "2C:5A:0F:6F:6C:02"
    },
    "FibreChannel": {
        "BootTargets": [],
        "WWNN": "10:00:2C:5A:0F:6F:6C:02",
        "WWNSource": "ConfiguredLocally",
        "WWPN": "20:00:2C:5A:0F:6F:6C:02"
    },
    "Id": "fc0",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkPorts/Port-0"
        }
    },
    "Name": "fc0"
}
```

## /redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/fc1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/NetworkInterfaces/Members/$entity/NetworkDeviceFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/fc1",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "2C:5A:0F:6F:6C:03"
    },
    "FibreChannel": {
        "BootTargets": [],
        "WWNN": "10:00:2C:5A:0F:6F:6C:03",
        "WWNSource": "ConfiguredLocally",
        "WWPN": "20:00:2C:5A:0F:6F:6C:03"
    },
    "Id": "fc1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkPorts/Port-1"
        }
    },
    "Name": "fc1"
}
```

## /redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkPorts

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/NetworkInterfaces/Members/$entity/NetworkPorts",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkPorts",
    "@odata.type": "#NetworkPortCollection.NetworkPortCollection",
    "Description": "Collection of NetworkPort resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkPorts/Port-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkPorts/Port-1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "NetworkPort Collection"
}
```

## /redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkPorts/Port-0

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/NetworkInterfaces/Members/$entity/NetworkPorts/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkPorts/Port-0",
    "@odata.type": "#NetworkPort.v1_2_0.NetworkPort",
    "AssociatedNetworkAddresses": [
        "2C:5A:0F:6F:6B:F4"
    ],
    "Id": "0",
    "LinkStatus": "Up",
    "Name": "Port-0",
    "PhysicalPortNumber": "0",
    "SupportedLinkCapabilities": [
        {
            "LinkNetworkTechnology": "Ethernet"
        }
    ]
}
```

## /redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkPorts/Port-1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/NetworkInterfaces/Members/$entity/NetworkPorts/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkPorts/Port-1",
    "@odata.type": "#NetworkPort.v1_2_0.NetworkPort",
    "AssociatedNetworkAddresses": [
        "2C:5A:0F:6F:6B:F5"
    ],
    "Id": "1",
    "LinkStatus": "Up",
    "Name": "Port-1",
    "PhysicalPortNumber": "1",
    "SupportedLinkCapabilities": [
        {
            "LinkNetworkTechnology": "Ethernet"
        }
    ]
}
```

## /redfish/v1/Systems/FCH21067808/PCIeDevices/SBMezz1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SBMezz1",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "29.00.1-0360",
    "Id": "SBMezz1",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/Server1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SBMezz1/PCIeFunctions/SBMezz1"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco UCS C3000 RAID Controller for M4 Server",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SBMezz1/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/FCH21067808/PCIeDevices/SBMezz1/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SBMezz1/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SBMezz1/PCIeFunctions/SBMezz1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/FCH21067808/PCIeDevices/SBMezz1/PCIeFunctions/SBMezz1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SBMezz1/PCIeFunctions/SBMezz1",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x00ce",
    "Id": "SBMezz1",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-7"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-8"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-9"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-10"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-11"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-12"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-13"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-14"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-15"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-55"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-56"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-201"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-202"
            }
        ],
        "Drives@odata.count": 19,
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SBMezz1"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "Cisco UCS C3000 RAID Controller for M4 Server",
    "SubsystemId": "0x0197",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1000"
}
```

## /redfish/v1/Systems/FCH21067808/PCIeDevices/SIOC1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SIOC1",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "4.4(3a)",
    "Id": "SIOC1",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/Server1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SIOC1/PCIeFunctions/SIOC1"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "UCSC-C3260-SIOC",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SIOC1/PCIeFunctions"
    }
}
```

## /redfish/v1/Systems/FCH21067808/PCIeDevices/SIOC1/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SIOC1/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SIOC1/PCIeFunctions/SIOC1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Systems/FCH21067808/PCIeDevices/SIOC1/PCIeFunctions/SIOC1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SIOC1/PCIeFunctions/SIOC1",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0042",
    "Id": "SIOC1",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/EthernetInterfaces/SIOC1.0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/EthernetInterfaces/SIOC1.1"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/eth0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/eth1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/fc0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/fc1"
            }
        ],
        "NetworkDeviceFunctions@odata.count": 4,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/PCIeDevices/SIOC1"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "UCSC-C3260-SIOC",
    "SubsystemId": "0x0157",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1137"
}
```

## /redfish/v1/Systems/FCH21067808/Processors

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Processors",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Processors",
    "@odata.type": "#ProcessorCollection.ProcessorCollection",
    "Description": "Collection of Processors for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Processors/CPU1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Processors/CPU2"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Processors Collection"
}
```

## /redfish/v1/Systems/FCH21067808/Processors/CPU1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Processors/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Processors/CPU1",
    "@odata.type": "#Processor.v1_5_0.Processor",
    "Description": "Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz/105W 12C/30MB Cache/DDR4 2400MHz",
    "Id": "1",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz",
    "Name": "CPU1",
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "6",
        "EffectiveModel": "79",
        "Step": "1",
        "VendorId": "Intel(R) Corporation"
    },
    "ProcessorType": "CPU",
    "Socket": "CPU1",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TotalCores": 12,
    "TotalEnabledCores": 12,
    "TotalThreads": 24
}
```

## /redfish/v1/Systems/FCH21067808/Processors/CPU2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Processors/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Processors/CPU2",
    "@odata.type": "#Processor.v1_5_0.Processor",
    "Description": "Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz/105W 12C/30MB Cache/DDR4 2400MHz",
    "Id": "2",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz",
    "Name": "CPU2",
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "6",
        "EffectiveModel": "79",
        "Step": "1",
        "VendorId": "Intel(R) Corporation"
    },
    "ProcessorType": "CPU",
    "Socket": "CPU2",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TotalCores": 12,
    "TotalEnabledCores": 12,
    "TotalThreads": 24
}
```

## /redfish/v1/Systems/FCH21067808/SecureBoot

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/SecureBoot",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/SecureBoot",
    "@odata.type": "#SecureBoot.v1_0_4.SecureBoot",
    "Description": "UEFI SecureBoot configuration of this system",
    "Id": "SecureBoot",
    "Name": "SecureBoot",
    "SecureBootCurrentBoot": "Disabled",
    "SecureBootEnable": false
}
```

## /redfish/v1/Systems/FCH21067808/SimpleStorage

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/SimpleStorage",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/SimpleStorage",
    "@odata.type": "#SimpleStorageCollection.SimpleStorageCollection",
    "Description": "Collection of storage controllers for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/SimpleStorage/SBMezz1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Simple Storage Collection"
}
```

## /redfish/v1/Systems/FCH21067808/SimpleStorage/SBMezz1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/SimpleStorage/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/SimpleStorage/SBMezz1",
    "@odata.type": "#SimpleStorage.v1_2_1.SimpleStorage",
    "Description": "Simple Storage Controller",
    "Devices": [
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "HGST",
            "Name": "PD-1",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "HGST",
            "Name": "PD-2",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "HGST",
            "Name": "PD-3",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "HGST",
            "Name": "PD-4",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "HGST",
            "Name": "PD-5",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "HGST",
            "Name": "PD-6",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "HGST",
            "Name": "PD-7",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "HGST",
            "Name": "PD-8",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "HGST",
            "Name": "PD-9",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "TOSHIBA",
            "Name": "PD-10",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "HGST",
            "Name": "PD-11",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "HGST",
            "Name": "PD-12",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "HGST",
            "Name": "PD-13",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "HGST",
            "Name": "PD-14",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 3907017728,
            "Manufacturer": "TOSHIBA",
            "Name": "PD-15",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 390711296,
            "Manufacturer": "TOSHIBA",
            "Name": "PD-55",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 390711296,
            "Manufacturer": "TOSHIBA",
            "Name": "PD-56",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 117220352,
            "Manufacturer": "ATA",
            "Name": "PD-201",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "CapacityBytes": 117220352,
            "Manufacturer": "ATA",
            "Name": "PD-202",
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        }
    ],
    "Id": "SBMezz1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/Server1"
        }
    },
    "Name": "Cisco UCS C3000 RAID Controller for M4 Server Blade with 4G RAID Cache",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/FCH21067808/Storage

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage",
    "@odata.type": "#StorageCollection.StorageCollection",
    "Description": "Collection of storage resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Storage Collection"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1",
    "@odata.type": "#Storage.v1_5_0.Storage",
    "Actions": {
        "#Storage.SetEncryptionKey": {
            "SecurityKey@Redfish.AllowableValues": [
                "Security Key"
            ],
            "SecurityKeyId@Redfish.AllowableValues": [
                "Security Key Identifier"
            ],
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Actions/Storage.SetEncryptionKey"
        }
    },
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-7"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-8"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-9"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-10"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-11"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-12"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-13"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-14"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-15"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-55"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-56"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-201"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-202"
        }
    ],
    "Id": "SBMezz1",
    "Links": {
        "Enclosures": [
            {
                "@odata.id": "/redfish/v1/Chassis/CMC"
            }
        ]
    },
    "Name": "SBMezz1",
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1#StorageControllers",
            "CacheSummary": {
                "TotalCacheSizeMiB": 3087
            },
            "FirmwareVersion": "4.700.00-7337",
            "Manufacturer": "LSI Logic",
            "MemberId": "RAID",
            "Model": "Cisco UCS C3000 RAID Controller for M4 Server Blade with 4G RAID Cache",
            "Name": "Cisco UCS C3000 RAID Controller for M4 Server Blade with 4G RAID Cache",
            "SerialNumber": "FCH210472FC",
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
        "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Volumes"
    }
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-1

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-1",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-1/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-1",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-1"
        }
    ],
    "Manufacturer": "HGST",
    "MediaType": "HDD",
    "Model": "HUS724040ALS640",
    "Name": "PD-1",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "A320",
    "SerialNumber": "PEK504BX",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-10

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-10",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-10/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-10",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-10"
        }
    ],
    "Manufacturer": "TOSHIBA",
    "MediaType": "HDD",
    "Model": "MG04SCA40EN",
    "Name": "PD-10",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "5705",
    "SerialNumber": "58R0A0FAFW0C",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-11

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-11",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-11/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-11",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-11"
        }
    ],
    "Manufacturer": "HGST",
    "MediaType": "HDD",
    "Model": "HUS724040ALS640",
    "Name": "PD-11",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "A320",
    "SerialNumber": "PEK3J55X",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-12

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-12",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-12/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-12",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-12"
        }
    ],
    "Manufacturer": "HGST",
    "MediaType": "HDD",
    "Model": "HUS724040ALS640",
    "Name": "PD-12",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "A320",
    "SerialNumber": "PEK4TNNX",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-13

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-13",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-13/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-13",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-13"
        }
    ],
    "Manufacturer": "HGST",
    "MediaType": "HDD",
    "Model": "HUS724040ALS640",
    "Name": "PD-13",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "A320",
    "SerialNumber": "PEK4SG5X",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-14

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-14",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-14/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-14",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-14"
        }
    ],
    "Manufacturer": "HGST",
    "MediaType": "HDD",
    "Model": "HUS724040ALS640",
    "Name": "PD-14",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "A320",
    "SerialNumber": "PEK4V2RX",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-15

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-15",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-15/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-15",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-15"
        }
    ],
    "Manufacturer": "TOSHIBA",
    "MediaType": "HDD",
    "Model": "MG04SCA40EN",
    "Name": "PD-15",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "5705",
    "SerialNumber": "58R0A0FJFW0C",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-2

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-2",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-2/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-2",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-2"
        }
    ],
    "Manufacturer": "HGST",
    "MediaType": "HDD",
    "Model": "HUS724040ALS640",
    "Name": "PD-2",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "A320",
    "SerialNumber": "PEK3JNMX",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-201

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-201",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-201/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 6,
    "CapacityBytes": 114473,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-201",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Volumes/VD-0"
            }
        ],
        "Volumes@odata.count": 1
    },
    "Location": [
        {
            "Info": "PD-201"
        }
    ],
    "Manufacturer": "ATA",
    "MediaType": "SSD",
    "Model": "INTEL SSDSC2BB120G6K",
    "Name": "PD-201",
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "SATA",
    "Revision": "G201CS01",
    "SerialNumber": "BTWA706604R4120CGN",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-202

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-202",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-202/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 6,
    "CapacityBytes": 114473,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-202",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Volumes/VD-0"
            }
        ],
        "Volumes@odata.count": 1
    },
    "Location": [
        {
            "Info": "PD-202"
        }
    ],
    "Manufacturer": "ATA",
    "MediaType": "SSD",
    "Model": "INTEL SSDSC2BB120G6K",
    "Name": "PD-202",
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "SATA",
    "Revision": "G201CS01",
    "SerialNumber": "BTWA706604QL120CGN",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-3

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-3",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-3/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-3",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-3"
        }
    ],
    "Manufacturer": "HGST",
    "MediaType": "HDD",
    "Model": "HUS724040ALS640",
    "Name": "PD-3",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "A320",
    "SerialNumber": "PEK1NPWX",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-4

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-4",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-4/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-4",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-4"
        }
    ],
    "Manufacturer": "HGST",
    "MediaType": "HDD",
    "Model": "HUS724040ALS640",
    "Name": "PD-4",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "A320",
    "SerialNumber": "PEK4YMVX",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-5

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-5",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-5/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-5",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-5"
        }
    ],
    "Manufacturer": "HGST",
    "MediaType": "HDD",
    "Model": "HUS724040ALS640",
    "Name": "PD-5",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "A320",
    "SerialNumber": "PEK4TBZX",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-55

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-55",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-55/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 381554,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-55",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-55"
        }
    ],
    "Manufacturer": "TOSHIBA",
    "MediaType": "SSD",
    "Model": "PX05SVB040",
    "Name": "PD-55",
    "PredictedMediaLifeLeftPercent": 90,
    "Protocol": "SAS",
    "Revision": "0104",
    "SerialNumber": "58G0A044TS8E",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-56

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-56",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-56/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 381554,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-56",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-56"
        }
    ],
    "Manufacturer": "TOSHIBA",
    "MediaType": "SSD",
    "Model": "PX05SVB040",
    "Name": "PD-56",
    "PredictedMediaLifeLeftPercent": 90,
    "Protocol": "SAS",
    "Revision": "0104",
    "SerialNumber": "58G0A03YTS8E",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-6

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-6",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-6/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-6",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-6"
        }
    ],
    "Manufacturer": "HGST",
    "MediaType": "HDD",
    "Model": "HUS724040ALS640",
    "Name": "PD-6",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "A320",
    "SerialNumber": "PEK4TK9X",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-7

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-7",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-7/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-7",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-7"
        }
    ],
    "Manufacturer": "HGST",
    "MediaType": "HDD",
    "Model": "HUS724040ALS640",
    "Name": "PD-7",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "A320",
    "SerialNumber": "PEK4TA9X",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-8

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-8",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-8/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-8",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-8"
        }
    ],
    "Manufacturer": "HGST",
    "MediaType": "HDD",
    "Model": "HUS724040ALS640",
    "Name": "PD-8",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "A320",
    "SerialNumber": "PEK3GJXX",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-9

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Drives/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-9",
    "@odata.type": "#Drive.v1_5_0.Drive",
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-9/Actions/Drive.SecureErase"
        }
    },
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 12,
    "CapacityBytes": 3815447,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareReplacementMode": "Revertible",
    "HotspareType": "None",
    "Id": "PD-9",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "Location": [
        {
            "Info": "PD-9"
        }
    ],
    "Manufacturer": "HGST",
    "MediaType": "HDD",
    "Model": "HUS724040ALS640",
    "Name": "PD-9",
    "PredictedMediaLifeLeftPercent": 0,
    "Protocol": "SAS",
    "Revision": "A320",
    "SerialNumber": "PEK4SJHX",
    "Status": {
        "Health": "OK"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Volumes

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Volumes",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection of Storage resource instances",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Volumes/VD-0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Volumes Collection"
}
```

## /redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Volumes/VD-0

```{
    "@odata.context": "/redfish/v1/$metadata#Systems/Members/$entity/Storage/Members/$entity/Volumes/Members/$entity",
    "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Volumes/VD-0",
    "@odata.type": "#Volume.v1_0_3.Volume",
    "Actions": {
        "#Volume.Initialize": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Volumes/VD-0/Actions/Volume.Initialize"
        }
    },
    "BlockSizeBytes": 65536,
    "CapacityBytes": 118999744512,
    "Encrypted": false,
    "Id": "0",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-201"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-202"
            }
        ],
        "Drives@odata.count": 2
    },
    "Name": "BootSSD-201-202",
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

## /redfish/v1/Systems/FOX2034GCLV

```null
```

## /redfish/v1/Systems/Server1/NetworkInterfaces/SIOC1/NetworkPorts/Port-0

```null
```

## /redfish/v1/Systems/Server1/NetworkInterfaces/SIOC1/NetworkPorts/Port-1

```null
```

