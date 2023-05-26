# Resource: /redfish/v1/Systems

Vendor | Model
--- | ---
HPE | vServer

## /redfish/v1/Systems

```{
    "@odata.context": "/redfish/v1/$metadata#ComputerSystemCollection.ComputerSystemCollection",
    "@odata.etag": "W/\"AA6D42B0\"",
    "@odata.id": "/redfish/v1/Systems",
    "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection",
    "Description": "Computer Systems view",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Computer Systems"
}
```

## /redfish/v1/Systems/1

```{
    "@odata.context": "/redfish/v1/$metadata#ComputerSystem.ComputerSystem",
    "@odata.etag": "W/\"B93F7124\"",
    "@odata.id": "/redfish/v1/Systems/1",
    "@odata.type": "#ComputerSystem.v1_10_0.ComputerSystem",
    "Actions": {
        "#ComputerSystem.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff",
                "GracefulShutdown",
                "ForceRestart",
                "Nmi",
                "PushPowerButton",
                "GracefulRestart"
            ],
            "target": "/redfish/v1/Systems/1/Actions/ComputerSystem.Reset"
        }
    },
    "AssetTag": "hp-new",
    "Bios": {
        "@odata.id": "/redfish/v1/Systems/1/bios"
    },
    "BiosVersion": "U46 v1.56 (11/29/2021)",
    "Boot": {
        "BootOptions": {
            "@odata.id": "/redfish/v1/Systems/1/BootOptions"
        },
        "BootOrder": [
            "Boot0019",
            "Boot000E",
            "Boot000F",
            "Boot0010",
            "Boot0011",
            "Boot0015",
            "Boot0016",
            "Boot0013",
            "Boot0014",
            "Boot0012"
        ],
        "BootSourceOverrideEnabled": "Disabled",
        "BootSourceOverrideMode": "UEFI",
        "BootSourceOverrideTarget": "None",
        "BootSourceOverrideTarget@Redfish.AllowableValues": [
            "None",
            "Cd",
            "Hdd",
            "Usb",
            "SDCard",
            "Utilities",
            "Diags",
            "BiosSetup",
            "Pxe",
            "UefiShell",
            "UefiHttp",
            "UefiTarget"
        ],
        "UefiTargetBootSourceOverride": "None",
        "UefiTargetBootSourceOverride@Redfish.AllowableValues": [
            "HD(1,GPT,E0462D22-8BF6-4172-B8A3-B8F56754A170,0x40,0x32000)/\\EFI\\VMware\\safeboot64.efi",
            "UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)",
            "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x1,0x0)",
            "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x2,0x0)",
            "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x3,0x0)",
            "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv4(0.0.0.0)/Uri()",
            "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv4(0.0.0.0)",
            "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)",
            "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()",
            "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)/NVMe(0x1,01-00-00-0A-0A-43-50-00)"
        ]
    },
    "EthernetInterfaces": {
        "@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces"
    },
    "HostName": "VYRBX9UJ4S.cisco.lab",
    "Id": "1",
    "IndicatorLED": "Off",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "ManagedBy": [
            {
                "@odata.id": "/redfish/v1/Managers/1"
            }
        ]
    },
    "LogServices": {
        "@odata.id": "/redfish/v1/Systems/1/LogServices"
    },
    "Manufacturer": "HPE",
    "Memory": {
        "@odata.id": "/redfish/v1/Systems/1/Memory"
    },
    "MemoryDomains": {
        "@odata.id": "/redfish/v1/Systems/1/MemoryDomains"
    },
    "MemorySummary": {
        "Status": {
            "HealthRollup": "OK"
        },
        "TotalSystemMemoryGiB": 32,
        "TotalSystemPersistentMemoryGiB": 0
    },
    "Model": "ProLiant DL360 Gen10 Plus",
    "Name": "Computer System",
    "NetworkInterfaces": {
        "@odata.id": "/redfish/v1/Systems/1/NetworkInterfaces"
    },
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeComputerSystemExt.HpeComputerSystemExt",
            "@odata.type": "#HpeComputerSystemExt.v2_9_0.HpeComputerSystemExt",
            "Actions": {
                "#HpeComputerSystemExt.PowerButton": {
                    "PushType@Redfish.AllowableValues": [
                        "Press",
                        "PressAndHold"
                    ],
                    "target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.PowerButton"
                },
                "#HpeComputerSystemExt.RestoreManufacturingDefaults": {
                    "target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.RestoreManufacturingDefaults"
                },
                "#HpeComputerSystemExt.RestoreSystemDefaults": {
                    "target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.RestoreSystemDefaults"
                },
                "#HpeComputerSystemExt.SecureSystemErase": {
                    "target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.SecureSystemErase"
                },
                "#HpeComputerSystemExt.ServerIntelligentDiagnosticsMode": {
                    "target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.ServerIntelligentDiagnosticsMode"
                },
                "#HpeComputerSystemExt.ServerSafeMode": {
                    "target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.ServerSafeMode"
                },
                "#HpeComputerSystemExt.SystemReset": {
                    "ResetType@Redfish.AllowableValues": [
                        "ColdBoot",
                        "AuxCycle"
                    ],
                    "target": "/redfish/v1/Systems/1/Actions/Oem/Hpe/HpeComputerSystemExt.SystemReset"
                }
            },
            "AggregateHealthStatus": {
                "AgentlessManagementService": "Ready",
                "BiosOrHardwareHealth": {
                    "Status": {
                        "Health": "OK"
                    }
                },
                "FanRedundancy": "Redundant",
                "Fans": {
                    "Status": {
                        "Health": "OK"
                    }
                },
                "Memory": {
                    "Status": {
                        "Health": "OK"
                    }
                },
                "Network": {
                    "Status": {
                        "Health": "OK"
                    }
                },
                "PowerSupplies": {
                    "PowerSuppliesMismatch": false,
                    "Status": {
                        "Health": "OK"
                    }
                },
                "PowerSupplyRedundancy": "Redundant",
                "Processors": {
                    "Status": {
                        "Health": "OK"
                    }
                },
                "SmartStorageBattery": {
                    "Status": {
                        "Health": "OK"
                    }
                },
                "Storage": {
                    "Status": {
                        "Health": "OK"
                    }
                },
                "Temperatures": {
                    "Status": {
                        "Health": "OK"
                    }
                }
            },
            "Bios": {
                "Backup": {
                    "Date": "05/26/2021",
                    "Family": "U46",
                    "VersionString": "U46 v1.42 (05/26/2021)"
                },
                "Current": {
                    "Date": "11/29/2021",
                    "Family": "U46",
                    "VersionString": "U46 v1.56 (11/29/2021)"
                },
                "UefiClass": 2
            },
            "CriticalTempRemainOff": false,
            "CurrentPowerOnTimeSeconds": 1659546593,
            "DeviceDiscoveryComplete": {
                "AMSDeviceDiscovery": "Complete",
                "DeviceDiscovery": "vMainDeviceDiscoveryComplete",
                "SmartArrayDiscovery": "Complete"
            },
            "ElapsedEraseTimeInMinutes": 0,
            "EndOfPostDelaySeconds": null,
            "EstimatedEraseTimeInMinutes": 0,
            "HostOS": {
                "OsName": "VMware ESXi",
                "OsSysDescription": "VMkernel VYRBX9UJ4S.cisco.lab 7.0.0 #1 SMP Release build-16324942 Jun  2 2020 10:08:07 x86_64 x86_64 x86_64 ESXi",
                "OsType": 25,
                "OsVersion": "7.0.0 Build-16324942 Patch 25"
            },
            "IntelligentProvisioningAlwaysOn": true,
            "IntelligentProvisioningIndex": 9,
            "IntelligentProvisioningLocation": "System Board",
            "IntelligentProvisioningVersion": "3.64.2",
            "IsColdBooting": false,
            "Links": {
                "EthernetInterfaces": {
                    "@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces"
                },
                "NetworkAdapters": {
                    "@odata.id": "/redfish/v1/Systems/1/BaseNetworkAdapters"
                },
                "PCIDevices": {
                    "@odata.id": "/redfish/v1/Systems/1/PCIDevices"
                },
                "PCISlots": {
                    "@odata.id": "/redfish/v1/Systems/1/PCISlots"
                },
                "SUT": {
                    "@odata.id": "/redfish/v1/Systems/1/hpsut"
                },
                "SecureEraseReportService": {
                    "@odata.id": "/redfish/v1/Systems/1/SecureEraseReportService"
                },
                "SmartStorage": {
                    "@odata.id": "/redfish/v1/Systems/1/SmartStorage"
                },
                "USBDevices": {
                    "@odata.id": "/redfish/v1/Systems/1/USBDevices"
                },
                "USBPorts": {
                    "@odata.id": "/redfish/v1/Systems/1/USBPorts"
                },
                "WorkloadPerformanceAdvisor": {
                    "@odata.id": "/redfish/v1/Systems/1/WorkloadPerformanceAdvisor"
                }
            },
            "PCAPartNumber": "P09120-111",
            "PCASerialNumber": "PZCRC0BRHF005L",
            "PostDiscoveryCompleteTimeStamp": "2022-07-19T05:09:26Z",
            "PostDiscoveryMode": null,
            "PostMode": null,
            "PostState": "FinishedPost",
            "PowerAllocationLimit": 1600,
            "PowerAutoOn": "Restore",
            "PowerOnDelay": "Minimum",
            "PowerOnMinutes": 159973,
            "PowerRegulatorMode": "Dynamic",
            "PowerRegulatorModesSupported": [
                "OSControl",
                "Dynamic",
                "Max",
                "Min"
            ],
            "SMBIOS": {
                "extref": "/smbios"
            },
            "ServerFQDN": "10.29.152.144",
            "ServerIntelligentDiagnosticsModeEnabled": false,
            "ServerSafeModeEnabled": false,
            "SystemROMAndiLOEraseComponentStatus": {
                "BIOSSettingsEraseStatus": "Idle",
                "iLOSettingsEraseStatus": "Idle"
            },
            "SystemROMAndiLOEraseStatus": "Idle",
            "SystemUsage": {
                "AvgCPU0Freq": 0,
                "AvgCPU1Freq": 21,
                "CPU0Power": 53,
                "CPU1Power": 47,
                "CPUICUtil": 0,
                "CPUUtil": 0,
                "IOBusUtil": 0,
                "JitterCount": 4,
                "MemoryBusUtil": 0
            },
            "UserDataEraseComponentStatus": {},
            "UserDataEraseStatus": "Idle",
            "VirtualProfile": "Inactive"
        }
    },
    "PowerState": "On",
    "ProcessorSummary": {
        "Count": 2,
        "Model": "Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz",
        "Status": {
            "HealthRollup": "OK"
        }
    },
    "Processors": {
        "@odata.id": "/redfish/v1/Systems/1/Processors"
    },
    "SKU": "P28948-B21",
    "SecureBoot": {
        "@odata.id": "/redfish/v1/Systems/1/SecureBoot"
    },
    "SerialNumber": "VYRBX9UJ4S",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "Storage": {
        "@odata.id": "/redfish/v1/Systems/1/Storage"
    },
    "SystemType": "Physical",
    "TrustedModules": [
        {
            "Oem": {
                "Hpe": {
                    "@odata.context": "/redfish/v1/$metadata#HpeTrustedModuleExt.HpeTrustedModuleExt",
                    "@odata.type": "#HpeTrustedModuleExt.v2_0_0.HpeTrustedModuleExt"
                }
            },
            "Status": {
                "State": "Absent"
            }
        }
    ],
    "UUID": "39383250-3834-4D32-3231-33323034374B"
}
```

## /redfish/v1/Systems/1/BaseNetworkAdapters

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBaseNetworkAdapterCollection.HpeBaseNetworkAdapterCollection",
    "@odata.etag": "W/\"AA6D42B0\"",
    "@odata.id": "/redfish/v1/Systems/1/BaseNetworkAdapters",
    "@odata.type": "#HpeBaseNetworkAdapterCollection.HpeBaseNetworkAdapterCollection",
    "Description": "NetworkAdapters view",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1/BaseNetworkAdapters/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "NetworkAdapters Collection"
}
```

## /redfish/v1/Systems/1/BaseNetworkAdapters/1

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBaseNetworkAdapter.HpeBaseNetworkAdapter",
    "@odata.etag": "W/\"B753AFAA\"",
    "@odata.id": "/redfish/v1/Systems/1/BaseNetworkAdapters/1",
    "@odata.type": "#HpeBaseNetworkAdapter.v2_0_0.HpeBaseNetworkAdapter",
    "FcPorts": [],
    "Firmware": {
        "Current": {
            "VersionString": "1.2839.0"
        }
    },
    "Id": "1",
    "Location": "OCP 3.0 Slot 10",
    "Name": "Intel Eth Adptr I350T4 OCPv3",
    "PartNumber": "MM#999HCV",
    "PhysicalPorts": [
        {
            "FullDuplex": true,
            "IPv4Addresses": [
                {
                    "Address": "10.29.152.144"
                }
            ],
            "IPv6Addresses": [
                {
                    "Address": "fe80::6a05:caff:fee1:367c"
                }
            ],
            "LinkStatus": "LinkUp",
            "MacAddress": "68:05:ca:e1:36:7c",
            "Name": "vmnic0",
            "Oem": {
                "Hpe": {
                    "@odata.context": "/redfish/v1/$metadata#HpeBaseNetworkAdapterExt.HpeBaseNetworkAdapterExt",
                    "@odata.type": "#HpeBaseNetworkAdapterExt.v2_0_0.HpeBaseNetworkAdapterExt",
                    "BadReceives": 0,
                    "BadTransmits": 0,
                    "GoodReceives": 0,
                    "GoodTransmits": 1767251
                }
            },
            "SpeedMbps": 1000,
            "Status": {
                "Health": "OK"
            }
        },
        {
            "FullDuplex": true,
            "IPv4Addresses": [],
            "IPv6Addresses": [
                {
                    "Address": "N/A"
                }
            ],
            "LinkStatus": "LinkUp",
            "MacAddress": "68:05:ca:e1:36:7d",
            "Name": "vmnic1",
            "Oem": {
                "Hpe": {
                    "@odata.context": "/redfish/v1/$metadata#HpeBaseNetworkAdapterExt.HpeBaseNetworkAdapterExt",
                    "@odata.type": "#HpeBaseNetworkAdapterExt.v2_0_0.HpeBaseNetworkAdapterExt",
                    "BadReceives": 0,
                    "BadTransmits": 0,
                    "GoodReceives": 0,
                    "GoodTransmits": 0
                }
            },
            "SpeedMbps": 1000,
            "Status": {
                "Health": "OK"
            }
        },
        {
            "FullDuplex": false,
            "IPv4Addresses": [],
            "IPv6Addresses": [
                {
                    "Address": "N/A"
                }
            ],
            "LinkStatus": null,
            "MacAddress": "68:05:ca:e1:36:7e",
            "Name": "vmnic2",
            "Oem": {
                "Hpe": {
                    "@odata.context": "/redfish/v1/$metadata#HpeBaseNetworkAdapterExt.HpeBaseNetworkAdapterExt",
                    "@odata.type": "#HpeBaseNetworkAdapterExt.v2_0_0.HpeBaseNetworkAdapterExt",
                    "BadReceives": 0,
                    "BadTransmits": 0,
                    "GoodReceives": 0,
                    "GoodTransmits": 0
                }
            },
            "SpeedMbps": 0
        },
        {
            "FullDuplex": false,
            "IPv4Addresses": [],
            "IPv6Addresses": [
                {
                    "Address": "N/A"
                }
            ],
            "LinkStatus": null,
            "MacAddress": "68:05:ca:e1:36:7f",
            "Name": "vmnic3",
            "Oem": {
                "Hpe": {
                    "@odata.context": "/redfish/v1/$metadata#HpeBaseNetworkAdapterExt.HpeBaseNetworkAdapterExt",
                    "@odata.type": "#HpeBaseNetworkAdapterExt.v2_0_0.HpeBaseNetworkAdapterExt",
                    "BadReceives": 0,
                    "BadTransmits": 0,
                    "GoodReceives": 0,
                    "GoodTransmits": 0
                }
            },
            "SpeedMbps": 0
        }
    ],
    "SerialNumber": "6805CAE1367C",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StructuredName": "OCP.Slot.10.1",
    "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/BootOptions

```{
    "@odata.context": "/redfish/v1/$metadata#BootOptionCollection.BootOptionCollection",
    "@odata.etag": "W/\"21C260DB\"",
    "@odata.id": "/redfish/v1/Systems/1/BootOptions",
    "@odata.type": "#BootOptionCollection.BootOptionCollection",
    "Description": "Configuration of Boot Options",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1/BootOptions/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/BootOptions/2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/BootOptions/3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/BootOptions/4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/BootOptions/5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/BootOptions/6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/BootOptions/7"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/BootOptions/8"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/BootOptions/9"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/BootOptions/10"
        }
    ],
    "Members@odata.count": 10,
    "Name": "Boot Options"
}
```

## /redfish/v1/Systems/1/BootOptions/1

```{
    "@odata.context": "/redfish/v1/$metadata#BootOption.BootOption",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Systems/1/BootOptions/1",
    "@odata.type": "#BootOption.v1_0_1.BootOption",
    "Alias": "None",
    "BootOptionReference": "Boot0019",
    "DisplayName": "VMware ESXi",
    "Id": "1",
    "Name": "Boot Option",
    "UefiDevicePath": "HD(1,GPT,E0462D22-8BF6-4172-B8A3-B8F56754A170,0x40,0x32000)/\\EFI\\VMware\\safeboot64.efi"
}
```

## /redfish/v1/Systems/1/BootOptions/10

```{
    "@odata.context": "/redfish/v1/$metadata#BootOption.BootOption",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Systems/1/BootOptions/10",
    "@odata.type": "#BootOption.v1_0_1.BootOption",
    "Alias": "None",
    "BootOptionReference": "Boot0012",
    "DisplayName": "Storage Slot 13 NVMe Drive 0 : HPE NS204i-r Gen10+ Boot Controller",
    "Id": "10",
    "Name": "Boot Option",
    "UefiDevicePath": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)/NVMe(0x1,01-00-00-0A-0A-43-50-00)"
}
```

## /redfish/v1/Systems/1/BootOptions/2

```{
    "@odata.context": "/redfish/v1/$metadata#BootOption.BootOption",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Systems/1/BootOptions/2",
    "@odata.type": "#BootOption.v1_0_1.BootOption",
    "Alias": "None",
    "BootOptionReference": "Boot000E",
    "DisplayName": "Generic USB Boot",
    "Id": "2",
    "Name": "Boot Option",
    "UefiDevicePath": "UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)"
}
```

## /redfish/v1/Systems/1/BootOptions/3

```{
    "@odata.context": "/redfish/v1/$metadata#BootOption.BootOption",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Systems/1/BootOptions/3",
    "@odata.type": "#BootOption.v1_0_1.BootOption",
    "Alias": "None",
    "BootOptionReference": "Boot000F",
    "DisplayName": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 1",
    "Id": "3",
    "Name": "Boot Option",
    "UefiDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x1,0x0)"
}
```

## /redfish/v1/Systems/1/BootOptions/4

```{
    "@odata.context": "/redfish/v1/$metadata#BootOption.BootOption",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Systems/1/BootOptions/4",
    "@odata.type": "#BootOption.v1_0_1.BootOption",
    "Alias": "None",
    "BootOptionReference": "Boot0010",
    "DisplayName": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 2",
    "Id": "4",
    "Name": "Boot Option",
    "UefiDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x2,0x0)"
}
```

## /redfish/v1/Systems/1/BootOptions/5

```{
    "@odata.context": "/redfish/v1/$metadata#BootOption.BootOption",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Systems/1/BootOptions/5",
    "@odata.type": "#BootOption.v1_0_1.BootOption",
    "Alias": "None",
    "BootOptionReference": "Boot0011",
    "DisplayName": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 3",
    "Id": "5",
    "Name": "Boot Option",
    "UefiDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x3,0x0)"
}
```

## /redfish/v1/Systems/1/BootOptions/6

```{
    "@odata.context": "/redfish/v1/$metadata#BootOption.BootOption",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Systems/1/BootOptions/6",
    "@odata.type": "#BootOption.v1_0_1.BootOption",
    "Alias": "None",
    "BootOptionReference": "Boot0015",
    "DisplayName": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (HTTP(S) IPv4)",
    "Id": "6",
    "Name": "Boot Option",
    "UefiDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv4(0.0.0.0)/Uri()"
}
```

## /redfish/v1/Systems/1/BootOptions/7

```{
    "@odata.context": "/redfish/v1/$metadata#BootOption.BootOption",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Systems/1/BootOptions/7",
    "@odata.type": "#BootOption.v1_0_1.BootOption",
    "Alias": "None",
    "BootOptionReference": "Boot0016",
    "DisplayName": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (PXE IPv4)",
    "Id": "7",
    "Name": "Boot Option",
    "UefiDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv4(0.0.0.0)"
}
```

## /redfish/v1/Systems/1/BootOptions/8

```{
    "@odata.context": "/redfish/v1/$metadata#BootOption.BootOption",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Systems/1/BootOptions/8",
    "@odata.type": "#BootOption.v1_0_1.BootOption",
    "Alias": "None",
    "BootOptionReference": "Boot0013",
    "DisplayName": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (PXE IPv6)",
    "Id": "8",
    "Name": "Boot Option",
    "UefiDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)"
}
```

## /redfish/v1/Systems/1/BootOptions/9

```{
    "@odata.context": "/redfish/v1/$metadata#BootOption.BootOption",
    "@odata.etag": "W/\"A3A6BF43\"",
    "@odata.id": "/redfish/v1/Systems/1/BootOptions/9",
    "@odata.type": "#BootOption.v1_0_1.BootOption",
    "Alias": "None",
    "BootOptionReference": "Boot0014",
    "DisplayName": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (HTTP(S) IPv6)",
    "Id": "9",
    "Name": "Boot Option",
    "UefiDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()"
}
```

## /redfish/v1/Systems/1/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "@odata.etag": "W/\"96E00A2C\"",
    "@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Description": "Collection of System Ethernet Interfaces",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces/2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces/3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces/4"
        }
    ],
    "Members@odata.count": 4,
    "Name": "System Ethernet Interfaces"
}
```

## /redfish/v1/Systems/1/EthernetInterfaces/1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.etag": "W/\"73501AB2\"",
    "@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces/1",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "FullDuplex": true,
    "IPv4Addresses": [
        {
            "Address": "10.29.152.144"
        }
    ],
    "IPv4StaticAddresses": [],
    "IPv6AddressPolicyTable": [],
    "IPv6Addresses": [
        {
            "Address": "fe80::6a05:caff:fee1:367c"
        }
    ],
    "IPv6StaticAddresses": [],
    "IPv6StaticDefaultGateways": [],
    "Id": "1",
    "InterfaceEnabled": true,
    "LinkStatus": "LinkUp",
    "MACAddress": "68:05:ca:e1:36:7c",
    "Name": "vmnic0",
    "NameServers": [],
    "SpeedMbps": 1000,
    "StaticNameServers": [],
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "UefiDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/EthernetInterfaces/2

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.etag": "W/\"763904A5\"",
    "@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces/2",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "FullDuplex": true,
    "IPv4Addresses": [],
    "IPv4StaticAddresses": [],
    "IPv6AddressPolicyTable": [],
    "IPv6Addresses": [
        {
            "Address": "N/A"
        }
    ],
    "IPv6StaticAddresses": [],
    "IPv6StaticDefaultGateways": [],
    "Id": "2",
    "InterfaceEnabled": true,
    "LinkStatus": "LinkUp",
    "MACAddress": "68:05:ca:e1:36:7d",
    "Name": "vmnic1",
    "NameServers": [],
    "SpeedMbps": 1000,
    "StaticNameServers": [],
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/1/EthernetInterfaces/3

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.etag": "W/\"16846800\"",
    "@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces/3",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "FullDuplex": false,
    "IPv4Addresses": [],
    "IPv4StaticAddresses": [],
    "IPv6AddressPolicyTable": [],
    "IPv6Addresses": [
        {
            "Address": "N/A"
        }
    ],
    "IPv6StaticAddresses": [],
    "IPv6StaticDefaultGateways": [],
    "Id": "3",
    "InterfaceEnabled": false,
    "LinkStatus": null,
    "MACAddress": "68:05:ca:e1:36:7e",
    "Name": "vmnic2",
    "NameServers": [],
    "SpeedMbps": null,
    "StaticNameServers": [],
    "Status": {
        "Health": null,
        "State": null
    }
}
```

## /redfish/v1/Systems/1/EthernetInterfaces/4

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.etag": "W/\"40C0E3BF\"",
    "@odata.id": "/redfish/v1/Systems/1/EthernetInterfaces/4",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "FullDuplex": false,
    "IPv4Addresses": [],
    "IPv4StaticAddresses": [],
    "IPv6AddressPolicyTable": [],
    "IPv6Addresses": [
        {
            "Address": "N/A"
        }
    ],
    "IPv6StaticAddresses": [],
    "IPv6StaticDefaultGateways": [],
    "Id": "4",
    "InterfaceEnabled": false,
    "LinkStatus": null,
    "MACAddress": "68:05:ca:e1:36:7f",
    "Name": "vmnic3",
    "NameServers": [],
    "SpeedMbps": null,
    "StaticNameServers": [],
    "Status": {
        "Health": null,
        "State": null
    }
}
```

## /redfish/v1/Systems/1/LogServices

```
```

## /redfish/v1/Systems/1/LogServices/IML

```
```

## /redfish/v1/Systems/1/LogServices/SL

```
```

## /redfish/v1/Systems/1/Memory

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryCollection.MemoryCollection",
    "@odata.etag": "W/\"52C2F4CA\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory",
    "@odata.type": "#MemoryCollection.MemoryCollection",
    "Description": "Memory DIMM Collection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm7"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm8"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm9"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm10"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm11"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm12"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm13"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm14"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm15"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm16"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm7"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm8"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm9"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm10"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm11"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm12"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm13"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm14"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm15"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm16"
        }
    ],
    "Members@odata.count": 32,
    "Name": "Memory DIMM Collection",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeAdvancedMemoryProtection.HpeAdvancedMemoryProtection",
            "@odata.type": "#HpeAdvancedMemoryProtection.v2_0_0.HpeAdvancedMemoryProtection",
            "AmpModeActive": "AdvancedECC",
            "AmpModeStatus": "AdvancedECC",
            "AmpModeSupported": [
                "AdvancedECC",
                "IntrasocketMirroring",
                "A3DC"
            ],
            "MemoryList": [
                {
                    "BoardCpuNumber": 1,
                    "BoardNumberOfSockets": 16,
                    "BoardOperationalFrequency": 2933,
                    "BoardOperationalVoltage": 1200,
                    "BoardTotalMemorySize": 16384
                },
                {
                    "BoardCpuNumber": 2,
                    "BoardNumberOfSockets": 16,
                    "BoardOperationalFrequency": 2933,
                    "BoardOperationalVoltage": 1200,
                    "BoardTotalMemorySize": 16384
                }
            ]
        }
    }
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm1",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": -1,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 1",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm1",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 6,
        "MemoryController": 3,
        "Slot": 1,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm1",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm10

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm10",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": -1,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 10",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm10",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 3,
        "MemoryController": 2,
        "Slot": 10,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm10",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm11

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm11",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": -1,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 11",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm11",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 4,
        "MemoryController": 2,
        "Slot": 11,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm11",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm12

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm12",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": -1,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 12",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm12",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 4,
        "MemoryController": 2,
        "Slot": 12,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm12",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm13

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm13",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": -1,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 13",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm13",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 1,
        "MemoryController": 1,
        "Slot": 13,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm13",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm14

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"E6EC3A2C\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm14",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BaseModuleType": "RDIMM",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 16384,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 14",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm14",
    "LogicalSizeMiB": 0,
    "Manufacturer": "Hynix",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 1,
        "MemoryController": 1,
        "Slot": 14,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm14",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "Attributes": [
                "HpeSmartMemory"
            ],
            "BaseModuleType": "RDIMM",
            "DIMMStatus": "GoodInUse",
            "MaxOperatingSpeedMTs": 3200,
            "MinimumVoltageVoltsX10": 12,
            "PartNumber": "P11443-091",
            "VendorName": "SK Hynix"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2933,
    "PartNumber": "HMA82GR7DJR8N-XN",
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": 2,
    "SecurityCapabilities": {},
    "SerialNumber": "74AAF456",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VendorID": "44288",
    "VolatileRegionSizeLimitMiB": 16384,
    "VolatileSizeMiB": 16384
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm15

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm15",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 15",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm15",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 2,
        "MemoryController": 1,
        "Slot": 15,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm15",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm16

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm16",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 16",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm16",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 2,
        "MemoryController": 1,
        "Slot": 16,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm16",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm2",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": -1,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 2",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm2",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 6,
        "MemoryController": 3,
        "Slot": 2,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm2",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm3

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm3",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": -1,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 3",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm3",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 5,
        "MemoryController": 3,
        "Slot": 3,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm3",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm4

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm4",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": -1,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 4",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm4",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 5,
        "MemoryController": 3,
        "Slot": 4,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm4",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm5

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm5",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": -1,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 5",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm5",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 8,
        "MemoryController": 4,
        "Slot": 5,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm5",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm6

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm6",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": -1,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 6",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm6",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 8,
        "MemoryController": 4,
        "Slot": 6,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm6",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm7

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm7",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": -1,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 7",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm7",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 7,
        "MemoryController": 4,
        "Slot": 7,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm7",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm8

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm8",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": -1,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 8",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm8",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 7,
        "MemoryController": 4,
        "Slot": 8,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm8",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc1dimm9

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc1dimm9",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": -1,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 1 DIMM 9",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc1dimm9",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 3,
        "MemoryController": 2,
        "Slot": 9,
        "Socket": 1
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc1dimm9",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm1",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 1",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm1",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 6,
        "MemoryController": 7,
        "Slot": 1,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm1",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm10

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm10",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 10",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm10",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 3,
        "MemoryController": 6,
        "Slot": 10,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm10",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm11

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm11",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 11",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm11",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 4,
        "MemoryController": 6,
        "Slot": 11,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm11",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm12

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm12",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 12",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm12",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 4,
        "MemoryController": 6,
        "Slot": 12,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm12",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm13

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm13",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 13",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm13",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 1,
        "MemoryController": 5,
        "Slot": 13,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm13",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm14

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"E6EC3A2C\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm14",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BaseModuleType": "RDIMM",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 16384,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 14",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm14",
    "LogicalSizeMiB": 0,
    "Manufacturer": "Hynix",
    "MemoryDeviceType": "DDR4",
    "MemoryLocation": {
        "Channel": 1,
        "MemoryController": 5,
        "Slot": 14,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm14",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "Attributes": [
                "HpeSmartMemory"
            ],
            "BaseModuleType": "RDIMM",
            "DIMMStatus": "GoodInUse",
            "MaxOperatingSpeedMTs": 3200,
            "MinimumVoltageVoltsX10": 12,
            "PartNumber": "P11443-091",
            "VendorName": "SK Hynix"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingSpeedMhz": 2933,
    "PartNumber": "HMA82GR7DJR8N-XN",
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": 2,
    "SecurityCapabilities": {},
    "SerialNumber": "74AAF451",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VendorID": "44288",
    "VolatileRegionSizeLimitMiB": 16384,
    "VolatileSizeMiB": 16384
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm15

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm15",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 15",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm15",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 2,
        "MemoryController": 5,
        "Slot": 15,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm15",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm16

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm16",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 16",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm16",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 2,
        "MemoryController": 5,
        "Slot": 16,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm16",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm2",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 2",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm2",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 6,
        "MemoryController": 7,
        "Slot": 2,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm2",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm3

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm3",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 3",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm3",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 5,
        "MemoryController": 7,
        "Slot": 3,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm3",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm4

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm4",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 4",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm4",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 5,
        "MemoryController": 7,
        "Slot": 4,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm4",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm5

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm5",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 5",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm5",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 8,
        "MemoryController": 8,
        "Slot": 5,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm5",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm6

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm6",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 6",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm6",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 8,
        "MemoryController": 8,
        "Slot": 6,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm6",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm7

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm7",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 7",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm7",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 7,
        "MemoryController": 8,
        "Slot": 7,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm7",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm8

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm8",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 8",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm8",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 7,
        "MemoryController": 8,
        "Slot": 8,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm8",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/Memory/proc2dimm9

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.etag": "W/\"6165906D\"",
    "@odata.id": "/redfish/v1/Systems/1/Memory/proc2dimm9",
    "@odata.type": "#Memory.v1_7_1.Memory",
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 0,
    "DataWidthBits": 64,
    "DeviceLocator": "PROC 2 DIMM 9",
    "ErrorCorrection": "MultiBitECC",
    "Id": "proc2dimm9",
    "LogicalSizeMiB": 0,
    "MemoryLocation": {
        "Channel": 3,
        "MemoryController": 6,
        "Slot": 9,
        "Socket": 2
    },
    "MemoryMedia": [
        "DRAM"
    ],
    "MemoryType": "DRAM",
    "Name": "proc2dimm9",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeMemoryExt.HpeMemoryExt",
            "@odata.type": "#HpeMemoryExt.v2_5_0.HpeMemoryExt",
            "DIMMStatus": "NotPresent",
            "MinimumVoltageVoltsX10": 0,
            "PartNumber": "Unknown"
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "PersistentRegionSizeLimitMiB": 0,
    "RankCount": null,
    "SecurityCapabilities": {},
    "Status": {
        "Health": "OK",
        "State": "Absent"
    },
    "VendorID": "0",
    "VolatileRegionSizeLimitMiB": 0,
    "VolatileSizeMiB": 0
}
```

## /redfish/v1/Systems/1/MemoryDomains

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryDomainCollection.MemoryDomainCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/Systems/1/MemoryDomains",
    "@odata.type": "#MemoryDomainCollection.MemoryDomainCollection",
    "Description": "Memory Domains Collection",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Memory Domains Collection"
}
```

## /redfish/v1/Systems/1/NetworkInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "@odata.etag": "W/\"F303ECE9\"",
    "@odata.id": "/redfish/v1/Systems/1/NetworkInterfaces",
    "@odata.type": "#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "Description": "The collection of network interfaces available in this system.",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Network Interface Collection",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeNetworkInterfaceStatus.HpeNetworkInterfaceStatus",
            "@odata.type": "#HpeNetworkInterfaceStatus.v1_0_0.HpeNetworkInterfaceStatus",
            "MemberContents": "AllDevices"
        }
    }
}
```

## /redfish/v1/Systems/1/PCIDevices

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPciDeviceCollection.HpeServerPciDeviceCollection",
    "@odata.etag": "W/\"96E00A2C\"",
    "@odata.id": "/redfish/v1/Systems/1/PCIDevices",
    "@odata.type": "#HpeServerPciDeviceCollection.HpeServerPciDeviceCollection",
    "Description": " PciDevices view",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1/PCIDevices/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCIDevices/2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCIDevices/3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCIDevices/4"
        }
    ],
    "Members@odata.count": 4,
    "Name": "PciDevices"
}
```

## /redfish/v1/Systems/1/PCIDevices/1

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPciDevice.HpeServerPciDevice",
    "@odata.etag": "W/\"5ABCB1B9\"",
    "@odata.id": "/redfish/v1/Systems/1/PCIDevices/1",
    "@odata.type": "#HpeServerPciDevice.v2_0_0.HpeServerPciDevice",
    "Bifurcated": "BifurcationNotSupported",
    "BusNumber": 1,
    "ClassCode": 3,
    "DeviceID": 1336,
    "DeviceInstance": 1,
    "DeviceLocation": "Embedded",
    "DeviceNumber": 0,
    "DeviceSubInstance": 1,
    "DeviceType": "Video",
    "FunctionNumber": 1,
    "Id": "1",
    "LocationString": "Embedded Video Controller",
    "Name": "Embedded Video Controller",
    "SegmentNumber": 0,
    "StructuredName": "PCI.Emb.1.1",
    "SubclassCode": 0,
    "SubsystemDeviceID": 228,
    "SubsystemVendorID": 5520,
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x1C,0x4)/Pci(0x0,0x1)",
    "VendorID": 4139
}
```

## /redfish/v1/Systems/1/PCIDevices/2

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPciDevice.HpeServerPciDevice",
    "@odata.etag": "W/\"6FB5B14B\"",
    "@odata.id": "/redfish/v1/Systems/1/PCIDevices/2",
    "@odata.type": "#HpeServerPciDevice.v2_0_0.HpeServerPciDevice",
    "Bifurcated": "BifurcationNotSupported",
    "BusNumber": 15,
    "ClassCode": 1,
    "DeviceID": 4322,
    "DeviceInstance": 1,
    "DeviceLocation": "PCI-E Slot 1",
    "DeviceNumber": 0,
    "DeviceSubInstance": 1,
    "DeviceType": "Storage Controller",
    "FunctionNumber": 0,
    "Id": "2",
    "LocationString": "Slot 1",
    "Name": "HPE MR416i-p Gen10+",
    "SegmentNumber": 0,
    "StructuredName": "Storage.Slot.1.1",
    "SubclassCode": 4,
    "SubsystemDeviceID": 659,
    "SubsystemVendorID": 5520,
    "UEFIDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
    "VendorID": 4096
}
```

## /redfish/v1/Systems/1/PCIDevices/3

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPciDevice.HpeServerPciDevice",
    "@odata.etag": "W/\"31275441\"",
    "@odata.id": "/redfish/v1/Systems/1/PCIDevices/3",
    "@odata.type": "#HpeServerPciDevice.v2_0_0.HpeServerPciDevice",
    "Bifurcated": "BifurcationNotSupported",
    "BusNumber": 72,
    "ClassCode": 2,
    "DeviceID": 5409,
    "DeviceInstance": 10,
    "DeviceLocation": "OCP Slot 10",
    "DeviceNumber": 0,
    "DeviceSubInstance": 1,
    "DeviceType": "NIC",
    "FunctionNumber": 0,
    "Id": "3",
    "LocationString": "OCP Slot 10",
    "Name": "Intel Eth Adptr I350T4 OCPv3",
    "SegmentNumber": 0,
    "StructuredName": "OCP.Slot.10.1",
    "SubclassCode": 0,
    "SubsystemDeviceID": 163,
    "SubsystemVendorID": 32902,
    "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
    "VendorID": 32902
}
```

## /redfish/v1/Systems/1/PCIDevices/4

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPciDevice.HpeServerPciDevice",
    "@odata.etag": "W/\"EDD4B250\"",
    "@odata.id": "/redfish/v1/Systems/1/PCIDevices/4",
    "@odata.type": "#HpeServerPciDevice.v2_0_0.HpeServerPciDevice",
    "Bifurcated": "BifurcationNotSupported",
    "BusNumber": 44,
    "ClassCode": 1,
    "DeviceID": 8769,
    "DeviceInstance": 13,
    "DeviceLocation": "Storage Controller Slot 13",
    "DeviceNumber": 0,
    "DeviceSubInstance": 1,
    "DeviceType": "Storage Controller",
    "FunctionNumber": 0,
    "Id": "4",
    "LocationString": "Storage Slot 13",
    "Name": "HPE NS204i-r Gen10+ Boot Controller",
    "SegmentNumber": 0,
    "StructuredName": "Storage.Slot.13.1",
    "SubclassCode": 8,
    "SubsystemDeviceID": 783,
    "SubsystemVendorID": 5520,
    "UEFIDevicePath": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)",
    "VendorID": 6987
}
```

## /redfish/v1/Systems/1/PCISlots

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPCISlotCollection.HpeServerPCISlotCollection",
    "@odata.etag": "W/\"361137E2\"",
    "@odata.id": "/redfish/v1/Systems/1/PCISlots",
    "@odata.type": "#HpeServerPCISlotCollection.HpeServerPCISlotCollection",
    "Description": "PciSlots view",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1/PCISlots/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCISlots/2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCISlots/3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCISlots/4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCISlots/5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCISlots/6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCISlots/7"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCISlots/8"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCISlots/9"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCISlots/10"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCISlots/11"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCISlots/12"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/PCISlots/13"
        }
    ],
    "Members@odata.count": 13,
    "Name": "PciSlots"
}
```

## /redfish/v1/Systems/1/PCISlots/1

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
    "@odata.etag": "W/\"301B55CE\"",
    "@odata.id": "/redfish/v1/Systems/1/PCISlots/1",
    "@odata.type": "#HpeServerPCISlot.v2_1_0.HpeServerPCISlot",
    "BusNumber": 15,
    "Characteristics": {
        "Provides3_3Volts": true,
        "SupportsPowerManagementEventSignal": true
    },
    "DeviceNumber": 0,
    "FunctionNumber": 0,
    "Id": "1",
    "Length": "Long",
    "LinkLanes": "x16",
    "Name": "PCI-E Slot 1",
    "Status": {
        "OperationalStatus": [
            {
                "Status": "InUse"
            }
        ]
    },
    "SupportsHotPlug": false,
    "Technology": "PCIExpressGen4",
    "UEFIDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/PCISlots/10

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
    "@odata.etag": "W/\"46A14746\"",
    "@odata.id": "/redfish/v1/Systems/1/PCISlots/10",
    "@odata.type": "#HpeServerPCISlot.v2_1_0.HpeServerPCISlot",
    "BusNumber": 222,
    "Characteristics": {
        "Provides3_3Volts": true,
        "SupportsHotPlugDevices": true,
        "SupportsSMBusSignal": true
    },
    "DeviceNumber": 0,
    "FunctionNumber": 0,
    "Id": "10",
    "Length": "Other",
    "LinkLanes": "x4",
    "Name": "NVMe Slot 48",
    "Status": {
        "OperationalStatus": [
            {
                "Status": "Empty"
            }
        ]
    },
    "SupportsHotPlug": true,
    "Technology": "PCIExpressGen4",
    "UEFIDevicePath": "PciRoot(0xB)/Pci(0x2,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/PCISlots/11

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
    "@odata.etag": "W/\"AF5C42CF\"",
    "@odata.id": "/redfish/v1/Systems/1/PCISlots/11",
    "@odata.type": "#HpeServerPCISlot.v2_1_0.HpeServerPCISlot",
    "BusNumber": 223,
    "Characteristics": {
        "Provides3_3Volts": true,
        "SupportsHotPlugDevices": true,
        "SupportsSMBusSignal": true
    },
    "DeviceNumber": 0,
    "FunctionNumber": 0,
    "Id": "11",
    "Length": "Other",
    "LinkLanes": "x4",
    "Name": "NVMe Slot 49",
    "Status": {
        "OperationalStatus": [
            {
                "Status": "Empty"
            }
        ]
    },
    "SupportsHotPlug": true,
    "Technology": "PCIExpressGen4",
    "UEFIDevicePath": "PciRoot(0xB)/Pci(0x3,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/PCISlots/12

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
    "@odata.etag": "W/\"5F3C50B3\"",
    "@odata.id": "/redfish/v1/Systems/1/PCISlots/12",
    "@odata.type": "#HpeServerPCISlot.v2_1_0.HpeServerPCISlot",
    "BusNumber": 224,
    "Characteristics": {
        "Provides3_3Volts": true,
        "SupportsHotPlugDevices": true,
        "SupportsSMBusSignal": true
    },
    "DeviceNumber": 0,
    "FunctionNumber": 0,
    "Id": "12",
    "Length": "Other",
    "LinkLanes": "x4",
    "Name": "NVMe Slot 50",
    "Status": {
        "OperationalStatus": [
            {
                "Status": "Empty"
            }
        ]
    },
    "SupportsHotPlug": true,
    "Technology": "PCIExpressGen4",
    "UEFIDevicePath": "PciRoot(0xB)/Pci(0x4,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/PCISlots/13

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
    "@odata.etag": "W/\"B6C1553A\"",
    "@odata.id": "/redfish/v1/Systems/1/PCISlots/13",
    "@odata.type": "#HpeServerPCISlot.v2_1_0.HpeServerPCISlot",
    "BusNumber": 225,
    "Characteristics": {
        "Provides3_3Volts": true,
        "SupportsHotPlugDevices": true,
        "SupportsSMBusSignal": true
    },
    "DeviceNumber": 0,
    "FunctionNumber": 0,
    "Id": "13",
    "Length": "Other",
    "LinkLanes": "x4",
    "Name": "NVMe Slot 51",
    "Status": {
        "OperationalStatus": [
            {
                "Status": "Empty"
            }
        ]
    },
    "SupportsHotPlug": true,
    "Technology": "PCIExpressGen4",
    "UEFIDevicePath": "PciRoot(0xB)/Pci(0x5,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/PCISlots/2

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
    "@odata.etag": "W/\"6B1B2BE6\"",
    "@odata.id": "/redfish/v1/Systems/1/PCISlots/2",
    "@odata.type": "#HpeServerPCISlot.v2_1_0.HpeServerPCISlot",
    "BusNumber": 43,
    "Characteristics": {
        "Provides3_3Volts": true,
        "SupportsPowerManagementEventSignal": true
    },
    "DeviceNumber": 0,
    "FunctionNumber": 0,
    "Id": "2",
    "Length": "Short",
    "LinkLanes": "x8",
    "Name": "PCI-E Slot 2",
    "Status": {
        "OperationalStatus": [
            {
                "Status": "Empty"
            }
        ]
    },
    "SupportsHotPlug": false,
    "Technology": "PCIExpressGen4",
    "UEFIDevicePath": "PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/PCISlots/3

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
    "@odata.etag": "W/\"59D8E538\"",
    "@odata.id": "/redfish/v1/Systems/1/PCISlots/3",
    "@odata.type": "#HpeServerPCISlot.v2_1_0.HpeServerPCISlot",
    "BusNumber": 72,
    "Characteristics": {
        "Provides3_3Volts": true,
        "SupportsPowerManagementEventSignal": true
    },
    "DeviceNumber": 0,
    "FunctionNumber": 0,
    "Id": "3",
    "Length": "Other",
    "LinkLanes": "x8",
    "Name": "OCP Slot 10",
    "Status": {
        "OperationalStatus": [
            {
                "Status": "InUse"
            }
        ]
    },
    "SupportsHotPlug": false,
    "Technology": "OCP NIC 3.0",
    "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/PCISlots/4

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
    "@odata.etag": "W/\"BF058F91\"",
    "@odata.id": "/redfish/v1/Systems/1/PCISlots/4",
    "@odata.type": "#HpeServerPCISlot.v2_1_0.HpeServerPCISlot",
    "BusNumber": 71,
    "Characteristics": {
        "Provides3_3Volts": true,
        "SupportsPowerManagementEventSignal": true
    },
    "DeviceNumber": 0,
    "FunctionNumber": 0,
    "Id": "4",
    "Length": "Other",
    "LinkLanes": "x8",
    "Name": "Storage Controller Slot 12",
    "Status": {
        "OperationalStatus": [
            {
                "Status": "Empty"
            }
        ]
    },
    "SupportsHotPlug": false,
    "Technology": "PCIExpressGen4",
    "UEFIDevicePath": "PciRoot(0x4)/Pci(0x2,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/PCISlots/5

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
    "@odata.etag": "W/\"F7F1F706\"",
    "@odata.id": "/redfish/v1/Systems/1/PCISlots/5",
    "@odata.type": "#HpeServerPCISlot.v2_1_0.HpeServerPCISlot",
    "BusNumber": 44,
    "Characteristics": {
        "Provides3_3Volts": true,
        "SupportsPowerManagementEventSignal": true
    },
    "DeviceNumber": 0,
    "FunctionNumber": 0,
    "Id": "5",
    "Length": "Other",
    "LinkLanes": "x4",
    "Name": "Storage Controller Slot 13",
    "Status": {
        "OperationalStatus": [
            {
                "Status": "InUse"
            }
        ]
    },
    "SupportsHotPlug": false,
    "Technology": "PCIExpressGen4",
    "UEFIDevicePath": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/PCISlots/6

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
    "@odata.etag": "W/\"1AF5F09F\"",
    "@odata.id": "/redfish/v1/Systems/1/PCISlots/6",
    "@odata.type": "#HpeServerPCISlot.v2_1_0.HpeServerPCISlot",
    "BusNumber": 99,
    "Characteristics": {
        "Provides3_3Volts": true,
        "SupportsHotPlugDevices": true,
        "SupportsSMBusSignal": true
    },
    "DeviceNumber": 0,
    "FunctionNumber": 0,
    "Id": "6",
    "Length": "Other",
    "LinkLanes": "x4",
    "Name": "NVMe Slot 32",
    "Status": {
        "OperationalStatus": [
            {
                "Status": "Empty"
            }
        ]
    },
    "SupportsHotPlug": true,
    "Technology": "PCIExpressGen4",
    "UEFIDevicePath": "PciRoot(0x5)/Pci(0x2,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/PCISlots/7

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
    "@odata.etag": "W/\"D630ECAE\"",
    "@odata.id": "/redfish/v1/Systems/1/PCISlots/7",
    "@odata.type": "#HpeServerPCISlot.v2_1_0.HpeServerPCISlot",
    "BusNumber": 100,
    "Characteristics": {
        "Provides3_3Volts": true,
        "SupportsHotPlugDevices": true,
        "SupportsSMBusSignal": true
    },
    "DeviceNumber": 0,
    "FunctionNumber": 0,
    "Id": "7",
    "Length": "Other",
    "LinkLanes": "x4",
    "Name": "NVMe Slot 33",
    "Status": {
        "OperationalStatus": [
            {
                "Status": "Empty"
            }
        ]
    },
    "SupportsHotPlug": true,
    "Technology": "PCIExpressGen4",
    "UEFIDevicePath": "PciRoot(0x5)/Pci(0x3,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/PCISlots/8

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
    "@odata.etag": "W/\"C9F0ECE1\"",
    "@odata.id": "/redfish/v1/Systems/1/PCISlots/8",
    "@odata.type": "#HpeServerPCISlot.v2_1_0.HpeServerPCISlot",
    "BusNumber": 101,
    "Characteristics": {
        "Provides3_3Volts": true,
        "SupportsHotPlugDevices": true,
        "SupportsSMBusSignal": true
    },
    "DeviceNumber": 0,
    "FunctionNumber": 0,
    "Id": "8",
    "Length": "Other",
    "LinkLanes": "x4",
    "Name": "NVMe Slot 34",
    "Status": {
        "OperationalStatus": [
            {
                "Status": "Empty"
            }
        ]
    },
    "SupportsHotPlug": true,
    "Technology": "PCIExpressGen4",
    "UEFIDevicePath": "PciRoot(0x5)/Pci(0x4,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/PCISlots/9

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerPCISlot.HpeServerPCISlot",
    "@odata.etag": "W/\"CC42E546\"",
    "@odata.id": "/redfish/v1/Systems/1/PCISlots/9",
    "@odata.type": "#HpeServerPCISlot.v2_1_0.HpeServerPCISlot",
    "BusNumber": 102,
    "Characteristics": {
        "Provides3_3Volts": true,
        "SupportsHotPlugDevices": true,
        "SupportsSMBusSignal": true
    },
    "DeviceNumber": 0,
    "FunctionNumber": 0,
    "Id": "9",
    "Length": "Other",
    "LinkLanes": "x4",
    "Name": "NVMe Slot 35",
    "Status": {
        "OperationalStatus": [
            {
                "Status": "Empty"
            }
        ]
    },
    "SupportsHotPlug": true,
    "Technology": "PCIExpressGen4",
    "UEFIDevicePath": "PciRoot(0x5)/Pci(0x5,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/1/Processors

```{
    "@odata.context": "/redfish/v1/$metadata#ProcessorCollection.ProcessorCollection",
    "@odata.etag": "W/\"570254F2\"",
    "@odata.id": "/redfish/v1/Systems/1/Processors",
    "@odata.type": "#ProcessorCollection.ProcessorCollection",
    "Description": "Processors view",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Processors/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Processors/2"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Processors Collection"
}
```

## /redfish/v1/Systems/1/Processors/1

```{
    "@odata.context": "/redfish/v1/$metadata#Processor.Processor",
    "@odata.etag": "W/\"F2193828\"",
    "@odata.id": "/redfish/v1/Systems/1/Processors/1",
    "@odata.type": "#Processor.v1_7_2.Processor",
    "Id": "1",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz",
    "Name": "Processors",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeProcessorExt.HpeProcessorExt",
            "@odata.type": "#HpeProcessorExt.v2_0_0.HpeProcessorExt",
            "AssetTag": "UNKNOWN",
            "Cache": [
                {
                    "Associativity": "8waySetAssociative",
                    "CacheSpeedns": 0,
                    "CurrentSRAMType": [
                        "Synchronous"
                    ],
                    "EccType": "SingleBitECC",
                    "InstalledSizeKB": 2240,
                    "Location": "Internal",
                    "MaximumSizeKB": 2240,
                    "Name": "L1-Cache",
                    "Policy": "WriteBack",
                    "Socketed": false,
                    "SupportedSRAMType": [
                        "Synchronous"
                    ],
                    "SystemCacheType": "Unified"
                },
                {
                    "Associativity": "20waySetAssociative",
                    "CacheSpeedns": 0,
                    "CurrentSRAMType": [
                        "Synchronous"
                    ],
                    "EccType": "SingleBitECC",
                    "InstalledSizeKB": 35840,
                    "Location": "Internal",
                    "MaximumSizeKB": 35840,
                    "Name": "L2-Cache",
                    "Policy": "Varies",
                    "Socketed": false,
                    "SupportedSRAMType": [
                        "Synchronous"
                    ],
                    "SystemCacheType": "Unified"
                },
                {
                    "Associativity": "12waySetAssociative",
                    "CacheSpeedns": 0,
                    "CurrentSRAMType": [
                        "Synchronous"
                    ],
                    "EccType": "SingleBitECC",
                    "InstalledSizeKB": 43008,
                    "Location": "Internal",
                    "MaximumSizeKB": 43008,
                    "Name": "L3-Cache",
                    "Policy": "Varies",
                    "Socketed": false,
                    "SupportedSRAMType": [
                        "Synchronous"
                    ],
                    "SystemCacheType": "Unified"
                }
            ],
            "Characteristics": [
                "64Bit",
                "MultiCore",
                "HwThread",
                "ExecuteProtection",
                "EnhancedVirtualization",
                "PowerPerfControl"
            ],
            "ConfigStatus": {
                "Populated": true,
                "State": "Enabled"
            },
            "CoresEnabled": 28,
            "ExternalClockMHz": 100,
            "MicrocodePatches": [
                {
                    "CpuId": "0x000606A4",
                    "Date": "2020-08-17T00:00:00Z",
                    "PatchId": "0x0B000280"
                },
                {
                    "CpuId": "0x000606A5",
                    "Date": "2021-03-08T00:00:00Z",
                    "PatchId": "0x0C0002F0"
                },
                {
                    "CpuId": "0x000606A6",
                    "Date": "2021-09-10T00:00:00Z",
                    "PatchId": "0x0D0002F2"
                }
            ],
            "PartNumber": "",
            "RatedSpeedMHz": 2000,
            "SerialNumber": "",
            "VoltageVoltsX10": 16
        }
    },
    "PartNumber": "",
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "179",
        "EffectiveModel": "10",
        "IdentificationRegisters": "0x06a60006fbffbfeb",
        "MicrocodeInfo": null,
        "Step": "6",
        "VendorId": "Intel(R) Corporation"
    },
    "ProcessorType": "CPU",
    "SerialNumber": "",
    "Socket": "Proc 1",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TotalCores": 28,
    "TotalThreads": 56
}
```

## /redfish/v1/Systems/1/Processors/2

```{
    "@odata.context": "/redfish/v1/$metadata#Processor.Processor",
    "@odata.etag": "W/\"F2193828\"",
    "@odata.id": "/redfish/v1/Systems/1/Processors/2",
    "@odata.type": "#Processor.v1_7_2.Processor",
    "Id": "2",
    "InstructionSet": "x86-64",
    "Manufacturer": "Intel(R) Corporation",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz",
    "Name": "Processors",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeProcessorExt.HpeProcessorExt",
            "@odata.type": "#HpeProcessorExt.v2_0_0.HpeProcessorExt",
            "AssetTag": "UNKNOWN",
            "Cache": [
                {
                    "Associativity": "8waySetAssociative",
                    "CacheSpeedns": 0,
                    "CurrentSRAMType": [
                        "Synchronous"
                    ],
                    "EccType": "SingleBitECC",
                    "InstalledSizeKB": 2240,
                    "Location": "Internal",
                    "MaximumSizeKB": 2240,
                    "Name": "L1-Cache",
                    "Policy": "WriteBack",
                    "Socketed": false,
                    "SupportedSRAMType": [
                        "Synchronous"
                    ],
                    "SystemCacheType": "Unified"
                },
                {
                    "Associativity": "20waySetAssociative",
                    "CacheSpeedns": 0,
                    "CurrentSRAMType": [
                        "Synchronous"
                    ],
                    "EccType": "SingleBitECC",
                    "InstalledSizeKB": 35840,
                    "Location": "Internal",
                    "MaximumSizeKB": 35840,
                    "Name": "L2-Cache",
                    "Policy": "Varies",
                    "Socketed": false,
                    "SupportedSRAMType": [
                        "Synchronous"
                    ],
                    "SystemCacheType": "Unified"
                },
                {
                    "Associativity": "12waySetAssociative",
                    "CacheSpeedns": 0,
                    "CurrentSRAMType": [
                        "Synchronous"
                    ],
                    "EccType": "SingleBitECC",
                    "InstalledSizeKB": 43008,
                    "Location": "Internal",
                    "MaximumSizeKB": 43008,
                    "Name": "L3-Cache",
                    "Policy": "Varies",
                    "Socketed": false,
                    "SupportedSRAMType": [
                        "Synchronous"
                    ],
                    "SystemCacheType": "Unified"
                }
            ],
            "Characteristics": [
                "64Bit",
                "MultiCore",
                "HwThread",
                "ExecuteProtection",
                "EnhancedVirtualization",
                "PowerPerfControl"
            ],
            "ConfigStatus": {
                "Populated": true,
                "State": "Enabled"
            },
            "CoresEnabled": 28,
            "ExternalClockMHz": 100,
            "MicrocodePatches": [
                {
                    "CpuId": "0x000606A4",
                    "Date": "2020-08-17T00:00:00Z",
                    "PatchId": "0x0B000280"
                },
                {
                    "CpuId": "0x000606A5",
                    "Date": "2021-03-08T00:00:00Z",
                    "PatchId": "0x0C0002F0"
                },
                {
                    "CpuId": "0x000606A6",
                    "Date": "2021-09-10T00:00:00Z",
                    "PatchId": "0x0D0002F2"
                }
            ],
            "PartNumber": "",
            "RatedSpeedMHz": 2000,
            "SerialNumber": "",
            "VoltageVoltsX10": 16
        }
    },
    "PartNumber": "",
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "179",
        "EffectiveModel": "10",
        "IdentificationRegisters": "0x06a60006fbffbfeb",
        "MicrocodeInfo": null,
        "Step": "6",
        "VendorId": "Intel(R) Corporation"
    },
    "ProcessorType": "CPU",
    "SerialNumber": "",
    "Socket": "Proc 2",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TotalCores": 28,
    "TotalThreads": 56
}
```

## /redfish/v1/Systems/1/SecureBoot

```{
    "@odata.context": "/redfish/v1/$metadata#SecureBoot.SecureBoot",
    "@odata.etag": "W/\"4A4CB737\"",
    "@odata.id": "/redfish/v1/Systems/1/SecureBoot",
    "@odata.type": "#SecureBoot.v1_0_0.SecureBoot",
    "Actions": {
        "#SecureBoot.ResetKeys": {
            "target": "/redfish/v1/Systems/1/SecureBoot/Actions/SecureBoot.ResetKeys"
        }
    },
    "Id": "SecureBoot",
    "Name": "SecureBoot",
    "SecureBootCurrentBoot": "Disabled",
    "SecureBootEnable": false,
    "SecureBootMode": "UserMode"
}
```

## /redfish/v1/Systems/1/SecureEraseReportService

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSecureEraseReportService.HpeSecureEraseReportService",
    "@odata.etag": "W/\"A45204F5\"",
    "@odata.id": "/redfish/v1/Systems/1/SecureEraseReportService",
    "@odata.type": "#HpeSecureEraseReportService.v1_0_0.HpeSecureEraseReportService",
    "Actions": {
        "#HpeSecureEraseReportService.DeleteSecureEraseReport": {
            "target": "/redfish/v1/Systems/1/SecureEraseReportService/Actions/HpeSecureEraseReportService.DeleteSecureEraseReport"
        }
    },
    "Description": "HPE SecureErase Report Service",
    "EraseInitiatedBy": null,
    "Id": "SecureEraseReportService",
    "Links": {
        "SecureEraseReportEntries": {
            "@odata.id": "/redfish/v1/Systems/1/SecureEraseReportService/SecureEraseReportEntries"
        }
    },
    "Name": "HpeSecureEraseReportService",
    "ServerSerialNumber": null
}
```

## /redfish/v1/Systems/1/SecureEraseReportService/SecureEraseReportEntries

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSecureEraseReportCollection.HpeSecureEraseReportCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/Systems/1/SecureEraseReportService/SecureEraseReportEntries",
    "@odata.type": "#HpeSecureEraseReportCollection.HpeSecureEraseReportCollection",
    "Description": "Secure Erase Report Collection View",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Secure Erase Report Collection"
}
```

## /redfish/v1/Systems/1/SmartStorage

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSmartStorage.HpeSmartStorage",
    "@odata.etag": "W/\"0B5F770C\"",
    "@odata.id": "/redfish/v1/Systems/1/SmartStorage",
    "@odata.type": "#HpeSmartStorage.v2_0_0.HpeSmartStorage",
    "Description": "HPE Smart Storage",
    "Id": "SmartStorage",
    "Links": {
        "ArrayControllers": {
            "@odata.id": "/redfish/v1/Systems/1/SmartStorage/ArrayControllers"
        },
        "HostBusAdapters": {
            "@odata.id": "/redfish/v1/Systems/1/SmartStorage/HostBusAdapters"
        }
    },
    "Name": "HpeSmartStorage",
    "Status": {
        "Health": "OK"
    }
}
```

## /redfish/v1/Systems/1/SmartStorage/ArrayControllers

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSmartStorageArrayControllerCollection.HpeSmartStorageArrayControllerCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/Systems/1/SmartStorage/ArrayControllers",
    "@odata.type": "#HpeSmartStorageArrayControllerCollection.HpeSmartStorageArrayControllerCollection",
    "Description": "HPE Smart Storage Array Controllers View",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "HpeSmartStorageArrayControllers"
}
```

## /redfish/v1/Systems/1/SmartStorage/HostBusAdapters

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSmartStorageHostBusAdapterCollection.HpeSmartStorageHostBusAdapterCollection",
    "@odata.etag": "W/\"570254F2\"",
    "@odata.id": "/redfish/v1/Systems/1/SmartStorage/HostBusAdapters",
    "@odata.type": "#HpeSmartStorageHostBusAdapterCollection.HpeSmartStorageHostBusAdapterCollection",
    "Description": "HPE Smart Storage Host Bus Adapters View",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1/SmartStorage/HostBusAdapters/0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/SmartStorage/HostBusAdapters/3"
        }
    ],
    "Members@odata.count": 2,
    "Name": "HpeSmartStorageHostBusAdapters"
}
```

## /redfish/v1/Systems/1/SmartStorage/HostBusAdapters/0

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSmartStorageHostBusAdapter.HpeSmartStorageHostBusAdapter",
    "@odata.etag": "W/\"552B04BD\"",
    "@odata.id": "/redfish/v1/Systems/1/SmartStorage/HostBusAdapters/0",
    "@odata.type": "#HpeSmartStorageHostBusAdapter.v2_0_0.HpeSmartStorageHostBusAdapter",
    "Description": "HPE Smart Storage Host Bus Adapter View",
    "FirmwareVersion": {
        "Current": {
            "VersionString": "52.16.3-3913"
        }
    },
    "Id": "0",
    "Links": {
        "Drives": {
            "@odata.id": "/redfish/v1/Systems/1/SmartStorage/HostBusAdapters/0/DiskDrives"
        }
    },
    "Location": "Slot 1",
    "LocationFormat": "PCISlot",
    "Model": "HPE MR416i-p Gen10+",
    "Name": "HpeSmartStorageHostBusAdapter",
    "SerialNumber": "PWTXP0ACDEX05D",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/1/SmartStorage/HostBusAdapters/0/DiskDrives

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSmartStorageDiskDriveCollection.HpeSmartStorageDiskDriveCollection",
    "@odata.etag": "W/\"570254F2\"",
    "@odata.id": "/redfish/v1/Systems/1/SmartStorage/HostBusAdapters/0/DiskDrives",
    "@odata.type": "#HpeSmartStorageDiskDriveCollection.HpeSmartStorageDiskDriveCollection",
    "Description": "HpeSmartStorageDiskDrive Collection View",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1/SmartStorage/HostBusAdapters/0/DiskDrives/0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/SmartStorage/HostBusAdapters/0/DiskDrives/1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "HpeSmartStorageDiskDrive Collection"
}
```

## /redfish/v1/Systems/1/SmartStorage/HostBusAdapters/0/DiskDrives/0

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSmartStorageDiskDrive.HpeSmartStorageDiskDrive",
    "@odata.etag": "W/\"CA779103\"",
    "@odata.id": "/redfish/v1/Systems/1/SmartStorage/HostBusAdapters/0/DiskDrives/0",
    "@odata.type": "#HpeSmartStorageDiskDrive.v2_1_0.HpeSmartStorageDiskDrive",
    "CapacityMiB": 960000,
    "Description": "HPE Smart Storage Disk Drive View",
    "DiskDriveUse": "Raw",
    "FirmwareVersion": {
        "Current": {
            "VersionString": "HPK3"
        }
    },
    "Id": "0",
    "Location": "Port 1I Box 1 Bay 1",
    "MediaType": "SSD",
    "Model": "VO000960KXAVL",
    "Name": "HpeSmartStorageDiskDrive",
    "SerialNumber": "SS0AN9970I010BC3W",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/1/SmartStorage/HostBusAdapters/0/DiskDrives/1

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSmartStorageDiskDrive.HpeSmartStorageDiskDrive",
    "@odata.etag": "W/\"42C566F0\"",
    "@odata.id": "/redfish/v1/Systems/1/SmartStorage/HostBusAdapters/0/DiskDrives/1",
    "@odata.type": "#HpeSmartStorageDiskDrive.v2_1_0.HpeSmartStorageDiskDrive",
    "CapacityMiB": 960000,
    "Description": "HPE Smart Storage Disk Drive View",
    "DiskDriveUse": "Raw",
    "FirmwareVersion": {
        "Current": {
            "VersionString": "HPK3"
        }
    },
    "Id": "1",
    "Location": "Port 1I Box 1 Bay 3",
    "MediaType": "SSD",
    "Model": "VO000960KXAVL",
    "Name": "HpeSmartStorageDiskDrive",
    "SerialNumber": "SS0AN9970I010BC3U",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/1/SmartStorage/HostBusAdapters/3

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSmartStorageHostBusAdapter.HpeSmartStorageHostBusAdapter",
    "@odata.etag": "W/\"65B0C723\"",
    "@odata.id": "/redfish/v1/Systems/1/SmartStorage/HostBusAdapters/3",
    "@odata.type": "#HpeSmartStorageHostBusAdapter.v2_0_0.HpeSmartStorageHostBusAdapter",
    "Description": "HPE Smart Storage Host Bus Adapter View",
    "FirmwareVersion": {
        "Current": {
            "VersionString": "1.0.14.1055"
        }
    },
    "Id": "3",
    "Links": {
        "Drives": {
            "@odata.id": "/redfish/v1/Systems/1/SmartStorage/HostBusAdapters/3/DiskDrives"
        }
    },
    "Location": "Slot 13",
    "LocationFormat": "PCISlot",
    "Model": "HPE NS204i-r Gen10+ Boot Controller",
    "Name": "HpeSmartStorageHostBusAdapter",
    "SerialNumber": "PZCSR0ARHEL005",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/1/SmartStorage/HostBusAdapters/3/DiskDrives

```{
    "@odata.context": "/redfish/v1/$metadata#HpeSmartStorageDiskDriveCollection.HpeSmartStorageDiskDriveCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/Systems/1/SmartStorage/HostBusAdapters/3/DiskDrives",
    "@odata.type": "#HpeSmartStorageDiskDriveCollection.HpeSmartStorageDiskDriveCollection",
    "Description": "HpeSmartStorageDiskDrive Collection View",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "HpeSmartStorageDiskDrive Collection"
}
```

## /redfish/v1/Systems/1/Storage

```{
    "@odata.context": "/redfish/v1/$metadata#StorageCollection.StorageCollection",
    "@odata.etag": "W/\"570254F2\"",
    "@odata.id": "/redfish/v1/Systems/1/Storage",
    "@odata.type": "#StorageCollection.StorageCollection",
    "Description": "Storage subSystems known to this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Storage"
}
```

## /redfish/v1/Systems/1/Storage/DE009000

```{
    "@odata.etag": "W/\"e7e66c43\"",
    "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000",
    "@odata.type": "#Storage.v1_7_1.Storage",
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000/Drives/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000/Drives/2"
        }
    ],
    "Drives@odata.count": 2,
    "Id": "DE009000",
    "Name": "HPE NS204i-r Gen10+ Boot Controller",
    "Status": {
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000#/StorageControllers/0",
            "CacheSummary": {
                "PersistentCacheSizeMiB": 0,
                "Status": {
                    "Health": "OK",
                    "State": "Absent"
                },
                "TotalCacheSizeMiB": 0
            },
            "ControllerRates": {
                "ConsistencyCheckRatePercent": 100,
                "RebuildRatePercent": 100
            },
            "FirmwareVersion": "1.0.14.1055",
            "Identifiers": [
                {
                    "DurableName": "51:40:2e:c0:15:e6:19:cc",
                    "DurableNameFormat": "NAA"
                }
            ],
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 13,
                    "LocationType": "Slot",
                    "ServiceLabel": "Slot 13"
                }
            },
            "Manufacturer": "HPE",
            "MemberId": "0",
            "Model": "HPE NS204i-r Gen10+ Boot Controller",
            "PCIeInterface": {
                "LanesInUse": 4,
                "MaxLanes": 4,
                "MaxPCIeType": "Gen3",
                "PCIeType": "Gen3"
            },
            "PartNumber": "P28340-001",
            "SKU": "P26463-B21",
            "SerialNumber": "LY0CEP001O",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "SupportedControllerProtocols": [
                "PCIe"
            ],
            "SupportedDeviceProtocols": [
                "NVMe"
            ],
            "SupportedRAIDTypes": [
                "RAID1"
            ]
        }
    ],
    "Volumes": {
        "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000/Volumes"
    }
}
```

## /redfish/v1/Systems/1/Storage/DE009000/Drives/1

```{
    "@odata.etag": "W/\"8e4df3ff\"",
    "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000/Drives/1",
    "@odata.type": "#Drive.v1_7_0.Drive",
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 16,
    "CapacityBytes": 480103981056,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "1",
    "Identifiers": [
        {
            "DurableName": "ace42e0005fcd346",
            "DurableNameFormat": "NAA"
        }
    ],
    "IndicatorLED": "Off",
    "Links": {
        "Volumes": [
            {
                "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000/Volumes/1"
            }
        ],
        "Volumes@odata.count": 1
    },
    "MediaType": "SSD",
    "Model": "VS000480KXALB",
    "Name": "480GB 16G NVMe SSD",
    "NegotiatedSpeedGbs": 16,
    "Operations": [],
    "PhysicalLocation": {
        "PartLocation": {
            "LocationOrdinalValue": 1,
            "LocationType": "Bay",
            "ServiceLabel": "Slot=13:Bay=1"
        }
    },
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "NVMe",
    "Revision": "85031G00",
    "SerialNumber": "FS0AN4320I110A52G",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/1/Storage/DE009000/Drives/2

```{
    "@odata.etag": "W/\"5ef2c366\"",
    "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000/Drives/2",
    "@odata.type": "#Drive.v1_7_0.Drive",
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 16,
    "CapacityBytes": 480103981056,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "2",
    "Identifiers": [
        {
            "DurableName": "ace42e0005fcd345",
            "DurableNameFormat": "NAA"
        }
    ],
    "IndicatorLED": "Off",
    "Links": {
        "Volumes": [
            {
                "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000/Volumes/1"
            }
        ],
        "Volumes@odata.count": 1
    },
    "MediaType": "SSD",
    "Model": "VS000480KXALB",
    "Name": "480GB 16G NVMe SSD",
    "NegotiatedSpeedGbs": 16,
    "Operations": [],
    "PhysicalLocation": {
        "PartLocation": {
            "LocationOrdinalValue": 2,
            "LocationType": "Bay",
            "ServiceLabel": "Slot=13:Bay=2"
        }
    },
    "PredictedMediaLifeLeftPercent": 100,
    "Protocol": "NVMe",
    "Revision": "85031G00",
    "SerialNumber": "FS0AN4320I110A52F",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/1/Storage/DE009000/Volumes

```{
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000/Volumes/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "NS Volume Collection"
}
```

## /redfish/v1/Systems/1/Storage/DE009000/Volumes/1

```{
    "@odata.etag": "W/\"6bc48aa3\"",
    "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000/Volumes/1",
    "@odata.type": "#Volume.v1_4_0.Volume",
    "BlockSizeBytes": 512,
    "CapacityBytes": 480036519936,
    "DisplayName": "VD_1",
    "Encrypted": false,
    "Id": "1",
    "Identifiers": [
        {
            "DurableName": "0050430a0a000001",
            "DurableNameFormat": "EUI"
        }
    ],
    "Links": {
        "DedicatedSpareDrives": [],
        "DedicatedSpareDrives@odata.count": 0,
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000/Drives/1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000/Drives/2"
            }
        ],
        "Drives@odata.count": 2
    },
    "LogicalUnitNumber": 1,
    "Name": "NS Volume",
    "Operations": [],
    "OptimumIOSizeBytes": 131072,
    "RAIDType": "RAID1",
    "ReadCachePolicy": "Off",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StripSizeBytes": 131072,
    "VolumeUsage": "Data",
    "WriteCachePolicy": "Off"
}
```

## /redfish/v1/Systems/1/Storage/DE00A000

```{
    "@odata.etag": "\"fc874d4b\"",
    "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000",
    "@odata.type": "#Storage.v1_7_1.Storage",
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/Drives/0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/Drives/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/Drives/2"
        }
    ],
    "Drives@odata.count": 3,
    "Id": "DE00A000",
    "Name": "HPE MR416i-p Gen10+",
    "Status": {
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000#/StorageControllers/0",
            "CacheSummary": {
                "PersistentCacheSizeMiB": 3687,
                "Status": {
                    "Health": "OK",
                    "State": "Enabled"
                },
                "TotalCacheSizeMiB": 4096
            },
            "ControllerRates": {
                "ConsistencyCheckRatePercent": 30,
                "RebuildRatePercent": 30,
                "TransformationRatePercent": 30
            },
            "FirmwareVersion": "52.16.3-3913",
            "Identifiers": [
                {
                    "DurableName": "606B7C745A21816FF",
                    "DurableNameFormat": "NAA"
                }
            ],
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 1,
                    "LocationType": "Slot",
                    "ServiceLabel": "Slot 1"
                }
            },
            "Manufacturer": "HPE",
            "MemberId": "0",
            "Model": "HPE MR416i-p Gen10+",
            "PCIeInterface": {
                "LanesInUse": 6,
                "MaxLanes": 16,
                "MaxPCIeType": "Gen4",
                "PCIeType": "Gen4"
            },
            "PartNumber": "P28344-001",
            "Ports": {
                "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/StorageControllers/0/Ports"
            },
            "SKU": "P06367-B21",
            "SerialNumber": "PWTXP0ACDEX05D",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "SupportedControllerProtocols": [
                "PCIe"
            ],
            "SupportedDeviceProtocols": [
                "NVMe",
                "SAS",
                "SATA"
            ],
            "SupportedRAIDTypes": [
                "RAID0",
                "RAID1",
                "RAID10",
                "RAID5",
                "RAID50",
                "RAID6",
                "RAID60"
            ]
        }
    ],
    "Volumes": {
        "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/Volumes"
    }
}
```

## /redfish/v1/Systems/1/Storage/DE00A000/Drives/0

```{
    "@odata.etag": "\"71dee044\"",
    "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/Drives/0",
    "@odata.type": "#Drive.v1_7_0.Drive",
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 32.0,
    "CapacityBytes": 960197124096,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "0",
    "Identifiers": [
        {
            "DurableName": "3CE42E000613ACCC",
            "DurableNameFormat": "NAA"
        }
    ],
    "IndicatorLED": "Off",
    "Links": {
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "MediaType": "SSD",
    "Model": "VO000960KXAVL",
    "Name": "960GB 32G NVMe SSD",
    "NegotiatedSpeedGbs": 32.0,
    "Operations": [],
    "PhysicalLocation": {
        "PartLocation": {
            "LocationOrdinalValue": 1,
            "LocationType": "Bay",
            "ServiceLabel": "Port=1I:Box=1:Bay=1"
        }
    },
    "PredictedMediaLifeLeftPercent": 100.0,
    "Protocol": "NVMe",
    "Revision": "HPK3",
    "SerialNumber": "SS0AN9970I010BC3W",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/1/Storage/DE00A000/Drives/1

```{
    "@odata.etag": "\"dd7bcdb3\"",
    "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/Drives/1",
    "@odata.type": "#Drive.v1_7_0.Drive",
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 32.0,
    "CapacityBytes": 960197124096,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "1",
    "Identifiers": [
        {
            "DurableName": "3CE42E000613ACCA",
            "DurableNameFormat": "NAA"
        }
    ],
    "IndicatorLED": "Off",
    "Links": {
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "MediaType": "SSD",
    "Model": "VO000960KXAVL",
    "Name": "960GB 32G NVMe SSD",
    "NegotiatedSpeedGbs": 32.0,
    "Operations": [],
    "PhysicalLocation": {
        "PartLocation": {
            "LocationOrdinalValue": 3,
            "LocationType": "Bay",
            "ServiceLabel": "Port=1I:Box=1:Bay=3"
        }
    },
    "PredictedMediaLifeLeftPercent": 100.0,
    "Protocol": "NVMe",
    "Revision": "HPK3",
    "SerialNumber": "SS0AN9970I010BC3U",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/1/Storage/DE00A000/Drives/2

```{
    "@odata.etag": "\"94f9d98e\"",
    "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/Drives/2",
    "@odata.type": "#Drive.v1_7_0.Drive",
    "BlockSizeBytes": 512,
    "CapableSpeedGbs": 32.0,
    "CapacityBytes": 960197124096,
    "EncryptionAbility": "None",
    "EncryptionStatus": "Unencrypted",
    "FailurePredicted": false,
    "HotspareType": "None",
    "Id": "2",
    "Identifiers": [
        {
            "DurableName": "3CE42E000613ACC0",
            "DurableNameFormat": "NAA"
        }
    ],
    "IndicatorLED": "Off",
    "Links": {
        "Volumes": [],
        "Volumes@odata.count": 0
    },
    "MediaType": "SSD",
    "Model": "VO000960KXAVL",
    "Name": "960GB 32G NVMe SSD",
    "NegotiatedSpeedGbs": 32.0,
    "Operations": [],
    "PhysicalLocation": {
        "PartLocation": {
            "LocationOrdinalValue": 2,
            "LocationType": "Bay",
            "ServiceLabel": "Port=1I:Box=1:Bay=2"
        }
    },
    "PredictedMediaLifeLeftPercent": 100.0,
    "Protocol": "NVMe",
    "Revision": "HPK3",
    "SerialNumber": "SS0AN9970I010BC3K",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "StatusIndicator": "OK"
}
```

## /redfish/v1/Systems/1/Storage/DE00A000/StorageControllers/0/Ports

```{
    "@odata.etag": "\"32f2ca76\"",
    "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/StorageControllers/0/Ports",
    "@odata.type": "#PortCollection.PortCollection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/StorageControllers/0/Ports/1I"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/StorageControllers/0/Ports/2I"
        }
    ],
    "Members@odata.count": 2,
    "Name": "PortCollection"
}
```

## /redfish/v1/Systems/1/Storage/DE00A000/StorageControllers/0/Ports/1I

```{
    "@odata.etag": "\"4befaebf\"",
    "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/StorageControllers/0/Ports/1I",
    "@odata.type": "#Port.v1_1_3.Port",
    "CurrentSpeedGbps": 12.0,
    "Id": "1I",
    "Location": {
        "PartLocation": {
            "LocationOrdinalValue": 1,
            "LocationType": "Connector",
            "ServiceLabel": "Port 1I"
        }
    },
    "MaxSpeedGbps": 12.0,
    "Name": "Port 1I",
    "PortId": "1I",
    "Status": {
        "Health": "OK"
    },
    "Width": 8
}
```

## /redfish/v1/Systems/1/Storage/DE00A000/StorageControllers/0/Ports/2I

```{
    "@odata.etag": "\"75d09af2\"",
    "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/StorageControllers/0/Ports/2I",
    "@odata.type": "#Port.v1_1_3.Port",
    "CurrentSpeedGbps": 12.0,
    "Id": "2I",
    "Location": {
        "PartLocation": {
            "LocationOrdinalValue": 2,
            "LocationType": "Connector",
            "ServiceLabel": "Port 2I"
        }
    },
    "MaxSpeedGbps": 12.0,
    "Name": "Port 2I",
    "PortId": "2I",
    "Status": {
        "Health": "OK"
    },
    "Width": 8
}
```

## /redfish/v1/Systems/1/Storage/DE00A000/Volumes

```{
    "@odata.etag": "\"54b42149\"",
    "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "MR Volume Collection"
}
```

## /redfish/v1/Systems/1/USBDevices

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBDevicesCollection.HpeUSBDevicesCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/Systems/1/USBDevices",
    "@odata.type": "#HpeUSBDevicesCollection.HpeUSBDevicesCollection",
    "Description": "USB Device collection view",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "USB Device collection"
}
```

## /redfish/v1/Systems/1/USBPorts

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPortsCollection.HpeUSBPortsCollection",
    "@odata.etag": "W/\"33C11E14\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts",
    "@odata.type": "#HpeUSBPortsCollection.HpeUSBPortsCollection",
    "Description": "USB Port Connectors View",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1/USBPorts/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/USBPorts/2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/USBPorts/3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/USBPorts/4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/USBPorts/5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/USBPorts/6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/USBPorts/7"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/USBPorts/8"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/USBPorts/9"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/USBPorts/10"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/USBPorts/11"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/USBPorts/12"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/USBPorts/13"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/USBPorts/14"
        }
    ],
    "Members@odata.count": 14,
    "Name": "USB Port Connectors"
}
```

## /redfish/v1/Systems/1/USBPorts/1

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPort.HpeUSBPort",
    "@odata.etag": "W/\"1F4226E1\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts/1",
    "@odata.type": "#HpeUSBPort.v2_0_0.HpeUSBPort",
    "Description": "USB Port Connector Information",
    "Id": "1",
    "InstanceNumber": 1,
    "Location": "InternalManagement",
    "Name": "USB Port Connector",
    "PCIBusNumber": 0,
    "PCIDeviceNumber": 20,
    "PCIFunctionNumber": 0,
    "ParentHubInstance": 0,
    "SharedCapability": "UnsharedManagement",
    "SpeedCapability": "USB2HighSpeed",
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x14,0x0)/USB(0x2,0x0)"
}
```

## /redfish/v1/Systems/1/USBPorts/10

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPort.HpeUSBPort",
    "@odata.etag": "W/\"70E9693C\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts/10",
    "@odata.type": "#HpeUSBPort.v2_0_0.HpeUSBPort",
    "Description": "USB Port Connector Information",
    "Id": "10",
    "InstanceNumber": 2,
    "Location": "Internal",
    "Name": "USB Port Connector",
    "PCIBusNumber": 0,
    "PCIDeviceNumber": 20,
    "PCIFunctionNumber": 0,
    "ParentHubInstance": 0,
    "SharedCapability": "UnsharedManagement",
    "SpeedCapability": "USB3SuperSpeed",
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x14,0x0)/USB(0x10,0x0)"
}
```

## /redfish/v1/Systems/1/USBPorts/11

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPort.HpeUSBPort",
    "@odata.etag": "W/\"00A86578\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts/11",
    "@odata.type": "#HpeUSBPort.v2_0_0.HpeUSBPort",
    "Description": "USB Port Connector Information",
    "Id": "11",
    "InstanceNumber": 2,
    "Location": "Back",
    "Name": "USB Port Connector",
    "PCIBusNumber": 0,
    "PCIDeviceNumber": 20,
    "PCIFunctionNumber": 0,
    "ParentHubInstance": 0,
    "SharedCapability": "UnsharedManagement",
    "SpeedCapability": "USB2HighSpeed",
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x14,0x0)/USB(0xC,0x0)"
}
```

## /redfish/v1/Systems/1/USBPorts/12

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPort.HpeUSBPort",
    "@odata.etag": "W/\"C7DA55A4\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts/12",
    "@odata.type": "#HpeUSBPort.v2_0_0.HpeUSBPort",
    "Description": "USB Port Connector Information",
    "Id": "12",
    "InstanceNumber": 2,
    "Location": "Back",
    "Name": "USB Port Connector",
    "PCIBusNumber": 0,
    "PCIDeviceNumber": 20,
    "PCIFunctionNumber": 0,
    "ParentHubInstance": 0,
    "SharedCapability": "UnsharedManagement",
    "SpeedCapability": "USB3SuperSpeed",
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x14,0x0)/USB(0x14,0x0)"
}
```

## /redfish/v1/Systems/1/USBPorts/13

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPort.HpeUSBPort",
    "@odata.etag": "W/\"0F67E82B\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts/13",
    "@odata.type": "#HpeUSBPort.v2_0_0.HpeUSBPort",
    "Description": "USB Port Connector Information",
    "Id": "13",
    "InstanceNumber": 1,
    "Location": "Back",
    "Name": "USB Port Connector",
    "PCIBusNumber": 0,
    "PCIDeviceNumber": 20,
    "PCIFunctionNumber": 0,
    "ParentHubInstance": 0,
    "SharedCapability": "UnsharedManagement",
    "SpeedCapability": "USB2HighSpeed",
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x14,0x0)/USB(0xD,0x0)"
}
```

## /redfish/v1/Systems/1/USBPorts/14

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPort.HpeUSBPort",
    "@odata.etag": "W/\"EB33B086\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts/14",
    "@odata.type": "#HpeUSBPort.v2_0_0.HpeUSBPort",
    "Description": "USB Port Connector Information",
    "Id": "14",
    "InstanceNumber": 1,
    "Location": "Back",
    "Name": "USB Port Connector",
    "PCIBusNumber": 0,
    "PCIDeviceNumber": 20,
    "PCIFunctionNumber": 0,
    "ParentHubInstance": 0,
    "SharedCapability": "UnsharedManagement",
    "SpeedCapability": "USB3SuperSpeed",
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x14,0x0)/USB(0x15,0x0)"
}
```

## /redfish/v1/Systems/1/USBPorts/2

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPort.HpeUSBPort",
    "@odata.etag": "W/\"F57F2899\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts/2",
    "@odata.type": "#HpeUSBPort.v2_0_0.HpeUSBPort",
    "Description": "USB Port Connector Information",
    "Id": "2",
    "InstanceNumber": 1,
    "Location": "Internal",
    "Name": "USB Port Connector",
    "PCIBusNumber": 0,
    "PCIDeviceNumber": 20,
    "PCIFunctionNumber": 0,
    "ParentHubInstance": 0,
    "SharedCapability": "UnsharedManagement",
    "SpeedCapability": "USB2HighSpeed",
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x14,0x0)/USB(0x7,0x0)"
}
```

## /redfish/v1/Systems/1/USBPorts/3

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPort.HpeUSBPort",
    "@odata.etag": "W/\"B11F7396\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts/3",
    "@odata.type": "#HpeUSBPort.v2_0_0.HpeUSBPort",
    "Description": "USB Port Connector Information",
    "Id": "3",
    "InstanceNumber": 1,
    "Location": "Internal",
    "Name": "USB Port Connector",
    "PCIBusNumber": 0,
    "PCIDeviceNumber": 20,
    "PCIFunctionNumber": 0,
    "ParentHubInstance": 0,
    "SharedCapability": "UnsharedManagement",
    "SpeedCapability": "USB3SuperSpeed",
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x14,0x0)/USB(0x12,0x0)"
}
```

## /redfish/v1/Systems/1/USBPorts/4

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPort.HpeUSBPort",
    "@odata.etag": "W/\"EAC501DD\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts/4",
    "@odata.type": "#HpeUSBPort.v2_0_0.HpeUSBPort",
    "Description": "USB Port Connector Information",
    "Id": "4",
    "InstanceNumber": 1,
    "Location": "Front",
    "Name": "USB Port Connector",
    "PCIBusNumber": 0,
    "PCIDeviceNumber": 20,
    "PCIFunctionNumber": 0,
    "ParentHubInstance": 0,
    "SharedCapability": "UnsharedManagement",
    "SpeedCapability": "USB2HighSpeed",
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x14,0x0)/USB(0x5,0x0)"
}
```

## /redfish/v1/Systems/1/USBPorts/5

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPort.HpeUSBPort",
    "@odata.etag": "W/\"EDC2A99F\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts/5",
    "@odata.type": "#HpeUSBPort.v2_0_0.HpeUSBPort",
    "Description": "USB Port Connector Information",
    "Id": "5",
    "InstanceNumber": 1,
    "Location": "Front",
    "Name": "USB Port Connector",
    "PCIBusNumber": 0,
    "PCIDeviceNumber": 20,
    "PCIFunctionNumber": 0,
    "ParentHubInstance": 0,
    "SharedCapability": "UnsharedManagement",
    "SpeedCapability": "USB3SuperSpeed",
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x14,0x0)/USB(0x11,0x0)"
}
```

## /redfish/v1/Systems/1/USBPorts/6

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPort.HpeUSBPort",
    "@odata.etag": "W/\"B063A349\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts/6",
    "@odata.type": "#HpeUSBPort.v2_0_0.HpeUSBPort",
    "Description": "USB Port Connector Information",
    "Id": "6",
    "InstanceNumber": 2,
    "Location": "Front",
    "Name": "USB Port Connector",
    "PCIBusNumber": 0,
    "PCIDeviceNumber": 20,
    "PCIFunctionNumber": 0,
    "ParentHubInstance": 0,
    "SharedCapability": "UnsharedManagement",
    "SpeedCapability": "USB2HighSpeed",
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x14,0x0)/USB(0x4,0x0)"
}
```

## /redfish/v1/Systems/1/USBPorts/7

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPort.HpeUSBPort",
    "@odata.etag": "W/\"AD744BC1\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts/7",
    "@odata.type": "#HpeUSBPort.v2_0_0.HpeUSBPort",
    "Description": "USB Port Connector Information",
    "Id": "7",
    "InstanceNumber": 1,
    "Location": "InternalSDCard",
    "Name": "USB Port Connector",
    "PCIBusNumber": 0,
    "PCIDeviceNumber": 20,
    "PCIFunctionNumber": 0,
    "ParentHubInstance": 0,
    "SharedCapability": "UnsharedManagement",
    "SpeedCapability": "USB2HighSpeed",
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x14,0x0)/USB(0x6,0x0)"
}
```

## /redfish/v1/Systems/1/USBPorts/8

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPort.HpeUSBPort",
    "@odata.etag": "W/\"34AEA783\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts/8",
    "@odata.type": "#HpeUSBPort.v2_0_0.HpeUSBPort",
    "Description": "USB Port Connector Information",
    "Id": "8",
    "InstanceNumber": 1,
    "Location": "InternalSDCard",
    "Name": "USB Port Connector",
    "PCIBusNumber": 0,
    "PCIDeviceNumber": 20,
    "PCIFunctionNumber": 0,
    "ParentHubInstance": 0,
    "SharedCapability": "UnsharedManagement",
    "SpeedCapability": "USB3SuperSpeed",
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x14,0x0)/USB(0x13,0x0)"
}
```

## /redfish/v1/Systems/1/USBPorts/9

```{
    "@odata.context": "/redfish/v1/$metadata#HpeUSBPort.HpeUSBPort",
    "@odata.etag": "W/\"E9253163\"",
    "@odata.id": "/redfish/v1/Systems/1/USBPorts/9",
    "@odata.type": "#HpeUSBPort.v2_0_0.HpeUSBPort",
    "Description": "USB Port Connector Information",
    "Id": "9",
    "InstanceNumber": 2,
    "Location": "Internal",
    "Name": "USB Port Connector",
    "PCIBusNumber": 0,
    "PCIDeviceNumber": 20,
    "PCIFunctionNumber": 0,
    "ParentHubInstance": 0,
    "SharedCapability": "UnsharedManagement",
    "SpeedCapability": "USB2HighSpeed",
    "UEFIDevicePath": "PciRoot(0x0)/Pci(0x14,0x0)/USB(0x3,0x0)"
}
```

## /redfish/v1/Systems/1/WorkloadPerformanceAdvisor

```{
    "@odata.context": "/redfish/v1/$metadata#HpeWorkloadPerformanceAdvisorCollection.HpeWorkloadPerformanceAdvisorCollection",
    "@odata.etag": "W/\"E589C4BF\"",
    "@odata.id": "/redfish/v1/Systems/1/WorkloadPerformanceAdvisor",
    "@odata.type": "#HpeWorkloadPerformanceAdvisorCollection.HpeWorkloadPerformanceAdvisorCollection",
    "Description": "Workload Performance Advisor view",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/1/WorkloadPerformanceAdvisor/1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/WorkloadPerformanceAdvisor/2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/1/WorkloadPerformanceAdvisor/3"
        }
    ],
    "Members@odata.count": 3,
    "Name": "Workload Performance Advisor"
}
```

## /redfish/v1/Systems/1/WorkloadPerformanceAdvisor/1

```{
    "@odata.context": "/redfish/v1/$metadata#HpeWorkloadPerformanceAdvisor.HpeWorkloadPerformanceAdvisor",
    "@odata.etag": "W/\"E7F95F0C\"",
    "@odata.id": "/redfish/v1/Systems/1/WorkloadPerformanceAdvisor/1",
    "@odata.type": "#HpeWorkloadPerformanceAdvisor.v1_0_0.HpeWorkloadPerformanceAdvisor",
    "Description": "Workload Performance Advisor for 10 min",
    "Duration": "PT10M",
    "Id": "1",
    "Name": "Workload Performance Advisor for 10 min",
    "PerformanceTuningOption": [
        {
            "BIOSAttributeName": "SubNumaClustering",
            "RecommendedValue": "EnableSnc2"
        },
        {
            "BIOSAttributeName": "NumaGroupSizeOpt",
            "RecommendedValue": "Clustered"
        },
        {
            "BIOSAttributeName": "UncoreFreqScaling",
            "RecommendedValue": null
        },
        {
            "BIOSAttributeName": "MemRefreshRate",
            "RecommendedValue": null
        },
        {
            "BIOSAttributeName": "PowerRegulator",
            "RecommendedValue": "DynamicPowerSavings"
        },
        {
            "BIOSAttributeName": "MinProcIdlePkgState",
            "RecommendedValue": null
        },
        {
            "BIOSAttributeName": "EnergyPerfBias",
            "RecommendedValue": null
        }
    ],
    "WorkloadCharacteristics": [
        {
            "MetricId": "CPUUtil",
            "MetricValue": "Low"
        },
        {
            "MetricId": "MemoryBusUtil",
            "MetricValue": "Low"
        },
        {
            "MetricId": "IOBusUtil",
            "MetricValue": "Low"
        },
        {
            "MetricId": "CPUICUtil",
            "MetricValue": "High"
        }
    ]
}
```

## /redfish/v1/Systems/1/WorkloadPerformanceAdvisor/2

```{
    "@odata.context": "/redfish/v1/$metadata#HpeWorkloadPerformanceAdvisor.HpeWorkloadPerformanceAdvisor",
    "@odata.etag": "W/\"E7F95F0C\"",
    "@odata.id": "/redfish/v1/Systems/1/WorkloadPerformanceAdvisor/2",
    "@odata.type": "#HpeWorkloadPerformanceAdvisor.v1_0_0.HpeWorkloadPerformanceAdvisor",
    "Description": "Workload Performance Advisor for 60 min",
    "Duration": "PT60M",
    "Id": "2",
    "Name": "Workload Performance Advisor for 60 min",
    "PerformanceTuningOption": [
        {
            "BIOSAttributeName": "SubNumaClustering",
            "RecommendedValue": "EnableSnc2"
        },
        {
            "BIOSAttributeName": "NumaGroupSizeOpt",
            "RecommendedValue": "Clustered"
        },
        {
            "BIOSAttributeName": "UncoreFreqScaling",
            "RecommendedValue": null
        },
        {
            "BIOSAttributeName": "MemRefreshRate",
            "RecommendedValue": null
        },
        {
            "BIOSAttributeName": "PowerRegulator",
            "RecommendedValue": "DynamicPowerSavings"
        },
        {
            "BIOSAttributeName": "MinProcIdlePkgState",
            "RecommendedValue": null
        },
        {
            "BIOSAttributeName": "EnergyPerfBias",
            "RecommendedValue": null
        }
    ],
    "WorkloadCharacteristics": [
        {
            "MetricId": "CPUUtil",
            "MetricValue": "Low"
        },
        {
            "MetricId": "MemoryBusUtil",
            "MetricValue": "Low"
        },
        {
            "MetricId": "IOBusUtil",
            "MetricValue": "Low"
        },
        {
            "MetricId": "CPUICUtil",
            "MetricValue": "High"
        }
    ]
}
```

## /redfish/v1/Systems/1/WorkloadPerformanceAdvisor/3

```{
    "@odata.context": "/redfish/v1/$metadata#HpeWorkloadPerformanceAdvisor.HpeWorkloadPerformanceAdvisor",
    "@odata.etag": "W/\"E7F95F0C\"",
    "@odata.id": "/redfish/v1/Systems/1/WorkloadPerformanceAdvisor/3",
    "@odata.type": "#HpeWorkloadPerformanceAdvisor.v1_0_0.HpeWorkloadPerformanceAdvisor",
    "Description": "Workload Performance Advisor for 1440 min",
    "Duration": "PT1440M",
    "Id": "3",
    "Name": "Workload Performance Advisor for 1440 min",
    "PerformanceTuningOption": [
        {
            "BIOSAttributeName": "SubNumaClustering",
            "RecommendedValue": "EnableSnc2"
        },
        {
            "BIOSAttributeName": "NumaGroupSizeOpt",
            "RecommendedValue": "Clustered"
        },
        {
            "BIOSAttributeName": "UncoreFreqScaling",
            "RecommendedValue": null
        },
        {
            "BIOSAttributeName": "MemRefreshRate",
            "RecommendedValue": null
        },
        {
            "BIOSAttributeName": "PowerRegulator",
            "RecommendedValue": "DynamicPowerSavings"
        },
        {
            "BIOSAttributeName": "MinProcIdlePkgState",
            "RecommendedValue": null
        },
        {
            "BIOSAttributeName": "EnergyPerfBias",
            "RecommendedValue": null
        }
    ],
    "WorkloadCharacteristics": [
        {
            "MetricId": "CPUUtil",
            "MetricValue": "Low"
        },
        {
            "MetricId": "MemoryBusUtil",
            "MetricValue": "Low"
        },
        {
            "MetricId": "IOBusUtil",
            "MetricValue": "Low"
        },
        {
            "MetricId": "CPUICUtil",
            "MetricValue": "High"
        }
    ]
}
```

## /redfish/v1/Systems/1/bios

```{
    "@Redfish.Settings": {
        "@odata.type": "#Settings.v1_0_0.Settings",
        "ETag": "69D913AB",
        "Messages": [
            {
                "MessageId": "Base.1.0.Success"
            }
        ],
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/1/bios/settings/"
        },
        "Time": "1970-01-01T00:20:09+00:00"
    },
    "@odata.context": "/redfish/v1/$metadata#Bios.Bios",
    "@odata.etag": "W/\"EED4B675ECF6FBFBFB288381322325BD\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/",
    "@odata.type": "#Bios.v1_0_4.Bios",
    "Actions": {
        "#Bios.ChangePassword": {
            "target": "/redfish/v1/Systems/1/bios/settings/Actions/Bios.ChangePasswords/"
        },
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/1/bios/settings/Actions/Bios.ResetBios/"
        }
    },
    "AttributeRegistry": "BiosAttributeRegistryU46.v1_1_56",
    "Attributes": {
        "AccessControlService": "Enabled",
        "AcpiHpet": "Enabled",
        "AcpiRootBridgePxm": "Enabled",
        "AcpiSlit": "Enabled",
        "AdjSecPrefetch": "Enabled",
        "AdminEmail": "",
        "AdminName": "",
        "AdminOtherInfo": "",
        "AdminPhone": "",
        "AdvCrashDumpMode": "Disabled",
        "AdvancedMemProtection": "Auto",
        "AllowLoginWithIlo": "Disabled",
        "AssetTagProtection": "Unlocked",
        "AutoPowerOn": "RestoreLastState",
        "BootMode": "Uefi",
        "BootOrderPolicy": "RetryIndefinitely",
        "CollabPowerControl": "Enabled",
        "ConsistentDevNaming": "LomsAndSlots",
        "CustomPostMessage": "",
        "DaylightSavingsTime": "DaylightSavingsTimeDisabled",
        "DcuIpPrefetcher": "Enabled",
        "DcuStreamPrefetcher": "Enabled",
        "DeadBlockPredictor": "Disabled",
        "Dhcpv4": "Enabled",
        "DirectToUpi": "Auto",
        "DramRapl": 0,
        "DramRaplLimit": "Disabled",
        "DramRaplReport": "Enabled",
        "DynamicPowerCapping": "Disabled",
        "EmbVideoConnection": "Auto",
        "EmbeddedDiagnostics": "Enabled",
        "EmbeddedIpxe": "Enabled",
        "EmbeddedSata": "Ahci",
        "EmbeddedSerialPort": "Com2Irq3",
        "EmbeddedUefiShell": "Enabled",
        "EmsConsole": "Disabled",
        "EnabledCoresPerProc": 0,
        "EnergyEfficientTurbo": "Enabled",
        "EnergyPerfBias": "BalancedPerf",
        "EnhancedProcPerf": "Disabled",
        "EppProfile": "Moderate",
        "EraseUserDefaults": "No",
        "ExtendedAmbientTemp": "Disabled",
        "ExtendedMemTest": "Disabled",
        "F11BootMenu": "Enabled",
        "FCScanPolicy": "CardConfig",
        "FanFailPolicy": "Shutdown",
        "FanInstallReq": "EnableMessaging",
        "HourFormat": "24Hours",
        "HttpSupport": "Auto",
        "HwPrefetcher": "Enabled",
        "IODCConfiguration": "Auto",
        "IntelDmiLinkFreq": "Auto",
        "IntelNicDmaChannels": "Enabled",
        "IntelPerfMonitoring": "Disabled",
        "IntelPriorityBaseFreq": "Disabled",
        "IntelProcVtd": "Enabled",
        "IntelUpiFreq": "Auto",
        "IntelUpiLinkEn": "Auto",
        "IntelUpiPowerManagement": "Enabled",
        "IntelVmdDirectAssign": "VmdDirectAssignEnabledAll",
        "IntelVmdSupport": "Disabled",
        "IntelVrocSupport": "None",
        "IntelligentProvisioning": "Enabled",
        "IpmiWatchdogTimerAction": "PowerCycle",
        "IpmiWatchdogTimerStatus": "IpmiWatchdogTimerOff",
        "IpmiWatchdogTimerTimeout": "Timeout30Min",
        "Ipv4Address": "0.0.0.0",
        "Ipv4Gateway": "0.0.0.0",
        "Ipv4PrimaryDNS": "0.0.0.0",
        "Ipv4SubnetMask": "0.0.0.0",
        "Ipv6Address": "::",
        "Ipv6ConfigPolicy": "Automatic",
        "Ipv6Duid": "Auto",
        "Ipv6Gateway": "::",
        "Ipv6PrimaryDNS": "::",
        "IpxeAutoStartScriptLocation": "Auto",
        "IpxeBootOrder": "Disabled",
        "IpxeScriptAutoStart": "Disabled",
        "IpxeScriptVerification": "Disabled",
        "IpxeStartupUrl": "",
        "LLCDeadLineAllocation": "Enabled",
        "LlcPrefetch": "Disabled",
        "LocalRemoteThreshold": "Auto",
        "MaxMemBusFreqMHz": "Auto",
        "MaxPcieSpeed": "PerPortCtrl",
        "MemClearWarmReset": "Disabled",
        "MemFastTraining": "Enabled",
        "MemMirrorMode": "Full",
        "MemPatrolScrubbing": "Enabled",
        "MemRefreshRate": "Refreshx1",
        "MemoryConfigurationViolationReporting": "Enabled",
        "MemoryRemap": "NoAction",
        "MicrosoftSecuredCoreSupport": "Disabled",
        "MinProcIdlePkgState": "C6NonRetention",
        "MinProcIdlePower": "C6",
        "MixedPowerSupplyReporting": "Enabled",
        "MkTme": "Disabled",
        "NetworkBootRetry": "Enabled",
        "NetworkBootRetryCount": 20,
        "NoExecutionProtection": "Enabled",
        "Numa": "Enabled",
        "NumaGroupSizeOpt": "Flat",
        "NvmeOptionRom": "Enabled",
        "NvmePort1": "Nvme",
        "NvmePort10": "Nvme",
        "NvmePort11": "Nvme",
        "NvmePort12": "Nvme",
        "NvmePort13": "Nvme",
        "NvmePort14": "Nvme",
        "NvmePort15": "Nvme",
        "NvmePort16": "Nvme",
        "NvmePort2": "Nvme",
        "NvmePort3": "Nvme",
        "NvmePort4": "Nvme",
        "NvmePort5": "Nvme",
        "NvmePort6": "Nvme",
        "NvmePort7": "Nvme",
        "NvmePort8": "Nvme",
        "NvmePort9": "Nvme",
        "NvmeRaid": "Disabled",
        "Ocp1AuxiliaryPower": "Enabled",
        "PatrolScrubDuration": 24,
        "PciPeerToPeerSerialization": "Disabled",
        "PciResourcePadding": "Normal",
        "PciSlot10Aspm": "Disabled",
        "PciSlot10Bifurcation": "Auto",
        "PciSlot10Enable": "Auto",
        "PciSlot10LinkSpeed": "Auto",
        "PciSlot10OptionROM": "Enabled",
        "PciSlot13Aspm": "Disabled",
        "PciSlot13Enable": "Auto",
        "PciSlot13LinkSpeed": "Auto",
        "PciSlot13OptionROM": "Enabled",
        "PciSlot1Aspm": "Disabled",
        "PciSlot1Bifurcation": "Auto",
        "PciSlot1Enable": "Auto",
        "PciSlot1LinkSpeed": "Auto",
        "PciSlot1OptionROM": "Enabled",
        "PciSlot2Bifurcation": "Auto",
        "PcieHotPlugErrControl": "HotplugSurprise",
        "PcuPMax": 0,
        "PersistentMemAddressRangeScrub": "Enabled",
        "PersistentMemBackupPowerPolicy": "WaitForBackupPower",
        "PersistentMemNumaAffinity": "IsolatedNumaDomains",
        "PersistentMemScanMem": "Enabled",
        "PlatformCertificate": "Enabled",
        "PlatformRASPolicy": "FirmwareFirst",
        "PostAsr": "PostAsrOff",
        "PostAsrDelay": "Delay30Min",
        "PostBootProgress": "Disabled",
        "PostDiscoveryMode": "Auto",
        "PostF1Prompt": "Delayed20Sec",
        "PostScreenMode": "VerboseMode",
        "PostVideoSupport": "DisplayAll",
        "PowerButton": "Enabled",
        "PowerOnDelay": "NoDelay",
        "PowerRegulator": "DynamicPowerSavings",
        "PreBootNetwork": "Auto",
        "PrebootNetworkEnvPolicy": "Auto",
        "PrebootNetworkProxy": "",
        "ProcAes": "Enabled",
        "ProcHyperthreading": "Enabled",
        "ProcRapl": 0,
        "ProcTurbo": "Enabled",
        "ProcVirtualization": "Enabled",
        "ProcX2Apic": "Enabled",
        "ProcessorConfigTDPLevel": "Normal",
        "ProcessorPhysicalAddress": "Limited",
        "ProductId": "P28948-B21",
        "RedundantPowerSupply": "BalancedMode",
        "RemoteXptPrefetcher": "Auto",
        "RemovableFlashBootSeq": "ExternalKeysFirst",
        "RestoreDefaults": "No",
        "RestoreManufacturingDefaults": "No",
        "RomSelection": "CurrentRom",
        "SataSanitize": "Disabled",
        "SataSecureErase": "Disabled",
        "SaveUserDefaults": "No",
        "SciRasSupport": "Ghesv1Support",
        "SecStartBackupImage": "Disabled",
        "SecureBootStatus": "Disabled",
        "SerialConsoleBaudRate": "BaudRate115200",
        "SerialConsoleEmulation": "Vt100Plus",
        "SerialConsolePort": "Auto",
        "SerialNumber": "VYRBX9UJ4S",
        "SerialPortDtrSupport": "Disabled",
        "ServerAssetTag": "hp-new",
        "ServerConfigLockStatus": "Disabled",
        "ServerName": "VYRBX9UJ4S.cisco.lab",
        "ServerOtherInfo": "",
        "ServerPrimaryOs": "",
        "ServiceEmail": "",
        "ServiceName": "",
        "ServiceOtherInfo": "",
        "ServicePhone": "",
        "SetupBrowserSelection": "Auto",
        "SgxAutoMpRegistrationAgent": "Enabled",
        "SgxEnable": "Disabled",
        "SgxLaunchControlPolicy": "IntelLocked",
        "SgxLePublicKeyHash0": "",
        "SgxLePublicKeyHash1": "",
        "SgxLePublicKeyHash2": "",
        "SgxLePublicKeyHash3": "",
        "SgxLePublicKeyWriteEnable": "Enabled",
        "SgxPrmrrSize": "2Gb",
        "Slot10EoiBroadcastSupport": "Disabled",
        "Slot10MctpBroadcastSupport": "Enabled",
        "Slot10NicBoot1": "NetworkBoot",
        "Slot10NicBoot2": "Disabled",
        "Slot10NicBoot3": "Disabled",
        "Slot10NicBoot4": "Disabled",
        "Slot1EoiBroadcastSupport": "Disabled",
        "Slot1MctpBroadcastSupport": "Enabled",
        "Slot1StorageBoot": "ThirtyTwoTargets",
        "Slot2EoiBroadcastSupport": "Disabled",
        "Slot2MctpBroadcastSupport": "Enabled",
        "SnoopResponseHoldOff": 0,
        "Sriov": "Enabled",
        "StaleAtoS": "Disabled",
        "SubNumaClustering": "Disabled",
        "ThermalConfig": "OptimalCooling",
        "ThermalShutdown": "Enabled",
        "TimeFormat": "Utc",
        "TimeZone": "Utc0",
        "Tme": "Disabled",
        "TmeExclusiveBase": "",
        "TmeExclusiveLen": "",
        "TpmChipId": "None",
        "TpmFips": "NotSpecified",
        "TpmState": "NotPresent",
        "TpmType": "NoTpm",
        "Tsx": "Enabled",
        "UefiOptimizedBoot": "Enabled",
        "UefiSerialDebugLevel": "ErrorsOnly",
        "UefiShellBootOrder": "Disabled",
        "UefiShellPhysicalPresenceKeystroke": "Enabled",
        "UefiShellScriptVerification": "Disabled",
        "UefiShellStartup": "Disabled",
        "UefiShellStartupLocation": "Auto",
        "UefiShellStartupUrl": "",
        "UefiShellStartupUrlFromDhcp": "Disabled",
        "UefiVariableAccessFwControl": "Disabled",
        "UncoreFreqScaling": "Auto",
        "UpiPrefetcher": "Enabled",
        "UrlBootFile": "",
        "UrlBootFile2": "",
        "UrlBootFile3": "",
        "UrlBootFile4": "",
        "UsbBoot": "Enabled",
        "UsbControl": "UsbEnabled",
        "UserDefaultsState": "Disabled",
        "UtilityLang": "English",
        "VirtualNuma": "Disabled",
        "VirtualSerialPort": "Com1Irq4",
        "VlanControl": "Disabled",
        "VlanId": 0,
        "VlanPriority": 0,
        "VmProprietaryPageRetireSupport": "Enabled",
        "VmdonCpu1Stack5Port1": "Disabled",
        "VmdonCpu1Stack5Port2": "Disabled",
        "VmdonCpu1Stack5Port3": "Disabled",
        "VmdonCpu1Stack5Port4": "Disabled",
        "VmdonCpu2Stack5Port1": "Disabled",
        "VmdonCpu2Stack5Port2": "Disabled",
        "VmdonCpu2Stack5Port3": "Disabled",
        "VmdonCpu2Stack5Port4": "Disabled",
        "WakeOnLan": "Enabled",
        "WorkloadProfile": "GeneralPowerEfficientCompute",
        "XptPrefetcher": "Auto",
        "iSCSISoftwareInitiator": "Enabled"
    },
    "Id": "bios",
    "Name": "BIOS Current Settings",
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/baseconfigs/"
                },
                "Boot": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/"
                },
                "KmsConfig": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/"
                },
                "Mappings": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/mappings/"
                },
                "ServerConfigLock": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/"
                },
                "TlsConfig": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/"
                },
                "iScsi": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"1D9FCF6419ED0C0C0C42B979DC024DFF\""
            }
        }
    }
}
```

## /redfish/v1/Systems/1/bios/

```{
    "@Redfish.Settings": {
        "@odata.type": "#Settings.v1_0_0.Settings",
        "ETag": "69D913AB",
        "Messages": [
            {
                "MessageId": "Base.1.0.Success"
            }
        ],
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/1/bios/settings/"
        },
        "Time": "1970-01-01T00:20:09+00:00"
    },
    "@odata.context": "/redfish/v1/$metadata#Bios.Bios",
    "@odata.etag": "W/\"EED4B675ECF6FBFBFB288381322325BD\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/",
    "@odata.type": "#Bios.v1_0_4.Bios",
    "Actions": {
        "#Bios.ChangePassword": {
            "target": "/redfish/v1/Systems/1/bios/settings/Actions/Bios.ChangePasswords/"
        },
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/1/bios/settings/Actions/Bios.ResetBios/"
        }
    },
    "AttributeRegistry": "BiosAttributeRegistryU46.v1_1_56",
    "Attributes": {
        "AccessControlService": "Enabled",
        "AcpiHpet": "Enabled",
        "AcpiRootBridgePxm": "Enabled",
        "AcpiSlit": "Enabled",
        "AdjSecPrefetch": "Enabled",
        "AdminEmail": "",
        "AdminName": "",
        "AdminOtherInfo": "",
        "AdminPhone": "",
        "AdvCrashDumpMode": "Disabled",
        "AdvancedMemProtection": "Auto",
        "AllowLoginWithIlo": "Disabled",
        "AssetTagProtection": "Unlocked",
        "AutoPowerOn": "RestoreLastState",
        "BootMode": "Uefi",
        "BootOrderPolicy": "RetryIndefinitely",
        "CollabPowerControl": "Enabled",
        "ConsistentDevNaming": "LomsAndSlots",
        "CustomPostMessage": "",
        "DaylightSavingsTime": "DaylightSavingsTimeDisabled",
        "DcuIpPrefetcher": "Enabled",
        "DcuStreamPrefetcher": "Enabled",
        "DeadBlockPredictor": "Disabled",
        "Dhcpv4": "Enabled",
        "DirectToUpi": "Auto",
        "DramRapl": 0,
        "DramRaplLimit": "Disabled",
        "DramRaplReport": "Enabled",
        "DynamicPowerCapping": "Disabled",
        "EmbVideoConnection": "Auto",
        "EmbeddedDiagnostics": "Enabled",
        "EmbeddedIpxe": "Enabled",
        "EmbeddedSata": "Ahci",
        "EmbeddedSerialPort": "Com2Irq3",
        "EmbeddedUefiShell": "Enabled",
        "EmsConsole": "Disabled",
        "EnabledCoresPerProc": 0,
        "EnergyEfficientTurbo": "Enabled",
        "EnergyPerfBias": "BalancedPerf",
        "EnhancedProcPerf": "Disabled",
        "EppProfile": "Moderate",
        "EraseUserDefaults": "No",
        "ExtendedAmbientTemp": "Disabled",
        "ExtendedMemTest": "Disabled",
        "F11BootMenu": "Enabled",
        "FCScanPolicy": "CardConfig",
        "FanFailPolicy": "Shutdown",
        "FanInstallReq": "EnableMessaging",
        "HourFormat": "24Hours",
        "HttpSupport": "Auto",
        "HwPrefetcher": "Enabled",
        "IODCConfiguration": "Auto",
        "IntelDmiLinkFreq": "Auto",
        "IntelNicDmaChannels": "Enabled",
        "IntelPerfMonitoring": "Disabled",
        "IntelPriorityBaseFreq": "Disabled",
        "IntelProcVtd": "Enabled",
        "IntelUpiFreq": "Auto",
        "IntelUpiLinkEn": "Auto",
        "IntelUpiPowerManagement": "Enabled",
        "IntelVmdDirectAssign": "VmdDirectAssignEnabledAll",
        "IntelVmdSupport": "Disabled",
        "IntelVrocSupport": "None",
        "IntelligentProvisioning": "Enabled",
        "IpmiWatchdogTimerAction": "PowerCycle",
        "IpmiWatchdogTimerStatus": "IpmiWatchdogTimerOff",
        "IpmiWatchdogTimerTimeout": "Timeout30Min",
        "Ipv4Address": "0.0.0.0",
        "Ipv4Gateway": "0.0.0.0",
        "Ipv4PrimaryDNS": "0.0.0.0",
        "Ipv4SubnetMask": "0.0.0.0",
        "Ipv6Address": "::",
        "Ipv6ConfigPolicy": "Automatic",
        "Ipv6Duid": "Auto",
        "Ipv6Gateway": "::",
        "Ipv6PrimaryDNS": "::",
        "IpxeAutoStartScriptLocation": "Auto",
        "IpxeBootOrder": "Disabled",
        "IpxeScriptAutoStart": "Disabled",
        "IpxeScriptVerification": "Disabled",
        "IpxeStartupUrl": "",
        "LLCDeadLineAllocation": "Enabled",
        "LlcPrefetch": "Disabled",
        "LocalRemoteThreshold": "Auto",
        "MaxMemBusFreqMHz": "Auto",
        "MaxPcieSpeed": "PerPortCtrl",
        "MemClearWarmReset": "Disabled",
        "MemFastTraining": "Enabled",
        "MemMirrorMode": "Full",
        "MemPatrolScrubbing": "Enabled",
        "MemRefreshRate": "Refreshx1",
        "MemoryConfigurationViolationReporting": "Enabled",
        "MemoryRemap": "NoAction",
        "MicrosoftSecuredCoreSupport": "Disabled",
        "MinProcIdlePkgState": "C6NonRetention",
        "MinProcIdlePower": "C6",
        "MixedPowerSupplyReporting": "Enabled",
        "MkTme": "Disabled",
        "NetworkBootRetry": "Enabled",
        "NetworkBootRetryCount": 20,
        "NoExecutionProtection": "Enabled",
        "Numa": "Enabled",
        "NumaGroupSizeOpt": "Flat",
        "NvmeOptionRom": "Enabled",
        "NvmePort1": "Nvme",
        "NvmePort10": "Nvme",
        "NvmePort11": "Nvme",
        "NvmePort12": "Nvme",
        "NvmePort13": "Nvme",
        "NvmePort14": "Nvme",
        "NvmePort15": "Nvme",
        "NvmePort16": "Nvme",
        "NvmePort2": "Nvme",
        "NvmePort3": "Nvme",
        "NvmePort4": "Nvme",
        "NvmePort5": "Nvme",
        "NvmePort6": "Nvme",
        "NvmePort7": "Nvme",
        "NvmePort8": "Nvme",
        "NvmePort9": "Nvme",
        "NvmeRaid": "Disabled",
        "Ocp1AuxiliaryPower": "Enabled",
        "PatrolScrubDuration": 24,
        "PciPeerToPeerSerialization": "Disabled",
        "PciResourcePadding": "Normal",
        "PciSlot10Aspm": "Disabled",
        "PciSlot10Bifurcation": "Auto",
        "PciSlot10Enable": "Auto",
        "PciSlot10LinkSpeed": "Auto",
        "PciSlot10OptionROM": "Enabled",
        "PciSlot13Aspm": "Disabled",
        "PciSlot13Enable": "Auto",
        "PciSlot13LinkSpeed": "Auto",
        "PciSlot13OptionROM": "Enabled",
        "PciSlot1Aspm": "Disabled",
        "PciSlot1Bifurcation": "Auto",
        "PciSlot1Enable": "Auto",
        "PciSlot1LinkSpeed": "Auto",
        "PciSlot1OptionROM": "Enabled",
        "PciSlot2Bifurcation": "Auto",
        "PcieHotPlugErrControl": "HotplugSurprise",
        "PcuPMax": 0,
        "PersistentMemAddressRangeScrub": "Enabled",
        "PersistentMemBackupPowerPolicy": "WaitForBackupPower",
        "PersistentMemNumaAffinity": "IsolatedNumaDomains",
        "PersistentMemScanMem": "Enabled",
        "PlatformCertificate": "Enabled",
        "PlatformRASPolicy": "FirmwareFirst",
        "PostAsr": "PostAsrOff",
        "PostAsrDelay": "Delay30Min",
        "PostBootProgress": "Disabled",
        "PostDiscoveryMode": "Auto",
        "PostF1Prompt": "Delayed20Sec",
        "PostScreenMode": "VerboseMode",
        "PostVideoSupport": "DisplayAll",
        "PowerButton": "Enabled",
        "PowerOnDelay": "NoDelay",
        "PowerRegulator": "DynamicPowerSavings",
        "PreBootNetwork": "Auto",
        "PrebootNetworkEnvPolicy": "Auto",
        "PrebootNetworkProxy": "",
        "ProcAes": "Enabled",
        "ProcHyperthreading": "Enabled",
        "ProcRapl": 0,
        "ProcTurbo": "Enabled",
        "ProcVirtualization": "Enabled",
        "ProcX2Apic": "Enabled",
        "ProcessorConfigTDPLevel": "Normal",
        "ProcessorPhysicalAddress": "Limited",
        "ProductId": "P28948-B21",
        "RedundantPowerSupply": "BalancedMode",
        "RemoteXptPrefetcher": "Auto",
        "RemovableFlashBootSeq": "ExternalKeysFirst",
        "RestoreDefaults": "No",
        "RestoreManufacturingDefaults": "No",
        "RomSelection": "CurrentRom",
        "SataSanitize": "Disabled",
        "SataSecureErase": "Disabled",
        "SaveUserDefaults": "No",
        "SciRasSupport": "Ghesv1Support",
        "SecStartBackupImage": "Disabled",
        "SecureBootStatus": "Disabled",
        "SerialConsoleBaudRate": "BaudRate115200",
        "SerialConsoleEmulation": "Vt100Plus",
        "SerialConsolePort": "Auto",
        "SerialNumber": "VYRBX9UJ4S",
        "SerialPortDtrSupport": "Disabled",
        "ServerAssetTag": "hp-new",
        "ServerConfigLockStatus": "Disabled",
        "ServerName": "VYRBX9UJ4S.cisco.lab",
        "ServerOtherInfo": "",
        "ServerPrimaryOs": "",
        "ServiceEmail": "",
        "ServiceName": "",
        "ServiceOtherInfo": "",
        "ServicePhone": "",
        "SetupBrowserSelection": "Auto",
        "SgxAutoMpRegistrationAgent": "Enabled",
        "SgxEnable": "Disabled",
        "SgxLaunchControlPolicy": "IntelLocked",
        "SgxLePublicKeyHash0": "",
        "SgxLePublicKeyHash1": "",
        "SgxLePublicKeyHash2": "",
        "SgxLePublicKeyHash3": "",
        "SgxLePublicKeyWriteEnable": "Enabled",
        "SgxPrmrrSize": "2Gb",
        "Slot10EoiBroadcastSupport": "Disabled",
        "Slot10MctpBroadcastSupport": "Enabled",
        "Slot10NicBoot1": "NetworkBoot",
        "Slot10NicBoot2": "Disabled",
        "Slot10NicBoot3": "Disabled",
        "Slot10NicBoot4": "Disabled",
        "Slot1EoiBroadcastSupport": "Disabled",
        "Slot1MctpBroadcastSupport": "Enabled",
        "Slot1StorageBoot": "ThirtyTwoTargets",
        "Slot2EoiBroadcastSupport": "Disabled",
        "Slot2MctpBroadcastSupport": "Enabled",
        "SnoopResponseHoldOff": 0,
        "Sriov": "Enabled",
        "StaleAtoS": "Disabled",
        "SubNumaClustering": "Disabled",
        "ThermalConfig": "OptimalCooling",
        "ThermalShutdown": "Enabled",
        "TimeFormat": "Utc",
        "TimeZone": "Utc0",
        "Tme": "Disabled",
        "TmeExclusiveBase": "",
        "TmeExclusiveLen": "",
        "TpmChipId": "None",
        "TpmFips": "NotSpecified",
        "TpmState": "NotPresent",
        "TpmType": "NoTpm",
        "Tsx": "Enabled",
        "UefiOptimizedBoot": "Enabled",
        "UefiSerialDebugLevel": "ErrorsOnly",
        "UefiShellBootOrder": "Disabled",
        "UefiShellPhysicalPresenceKeystroke": "Enabled",
        "UefiShellScriptVerification": "Disabled",
        "UefiShellStartup": "Disabled",
        "UefiShellStartupLocation": "Auto",
        "UefiShellStartupUrl": "",
        "UefiShellStartupUrlFromDhcp": "Disabled",
        "UefiVariableAccessFwControl": "Disabled",
        "UncoreFreqScaling": "Auto",
        "UpiPrefetcher": "Enabled",
        "UrlBootFile": "",
        "UrlBootFile2": "",
        "UrlBootFile3": "",
        "UrlBootFile4": "",
        "UsbBoot": "Enabled",
        "UsbControl": "UsbEnabled",
        "UserDefaultsState": "Disabled",
        "UtilityLang": "English",
        "VirtualNuma": "Disabled",
        "VirtualSerialPort": "Com1Irq4",
        "VlanControl": "Disabled",
        "VlanId": 0,
        "VlanPriority": 0,
        "VmProprietaryPageRetireSupport": "Enabled",
        "VmdonCpu1Stack5Port1": "Disabled",
        "VmdonCpu1Stack5Port2": "Disabled",
        "VmdonCpu1Stack5Port3": "Disabled",
        "VmdonCpu1Stack5Port4": "Disabled",
        "VmdonCpu2Stack5Port1": "Disabled",
        "VmdonCpu2Stack5Port2": "Disabled",
        "VmdonCpu2Stack5Port3": "Disabled",
        "VmdonCpu2Stack5Port4": "Disabled",
        "WakeOnLan": "Enabled",
        "WorkloadProfile": "GeneralPowerEfficientCompute",
        "XptPrefetcher": "Auto",
        "iSCSISoftwareInitiator": "Enabled"
    },
    "Id": "bios",
    "Name": "BIOS Current Settings",
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/baseconfigs/"
                },
                "Boot": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/"
                },
                "KmsConfig": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/"
                },
                "Mappings": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/mappings/"
                },
                "ServerConfigLock": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/"
                },
                "TlsConfig": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/"
                },
                "iScsi": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"1D9FCF6419ED0C0C0C42B979DC024DFF\""
            }
        }
    }
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/baseconfigs

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBaseConfigs.HpeBaseConfigs",
    "@odata.etag": "W/\"2BF923428033A4A4A4746C0150A2AC0B\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/baseconfigs/",
    "@odata.type": "#HpeBaseConfigs.v2_0_0.HpeBaseConfigs",
    "BaseConfigs": [
        {
            "default": {
                "AccessControlService": "Enabled",
                "AcpiHpet": "Enabled",
                "AcpiRootBridgePxm": "Enabled",
                "AcpiSlit": "Enabled",
                "AdjSecPrefetch": "Enabled",
                "AdminEmail": "",
                "AdminName": "",
                "AdminOtherInfo": "",
                "AdminPhone": "",
                "AdvCrashDumpMode": "Disabled",
                "AdvancedMemProtection": "Auto",
                "AllowLoginWithIlo": "Disabled",
                "AssetTagProtection": "Unlocked",
                "AutoPowerOn": "RestoreLastState",
                "BootMode": "Uefi",
                "BootOrderPolicy": "RetryIndefinitely",
                "CollabPowerControl": "Enabled",
                "ConsistentDevNaming": "LomsAndSlots",
                "CustomPostMessage": "",
                "DaylightSavingsTime": "DaylightSavingsTimeDisabled",
                "DcuIpPrefetcher": "Enabled",
                "DcuStreamPrefetcher": "Enabled",
                "DeadBlockPredictor": "Disabled",
                "Dhcpv4": "Enabled",
                "DirectToUpi": "Auto",
                "DramRapl": 0,
                "DramRaplLimit": "Disabled",
                "DramRaplReport": "Enabled",
                "DynamicPowerCapping": "Disabled",
                "EmbVideoConnection": "Auto",
                "EmbeddedDiagnostics": "Enabled",
                "EmbeddedIpxe": "Enabled",
                "EmbeddedSata": "Ahci",
                "EmbeddedSerialPort": "Com2Irq3",
                "EmbeddedUefiShell": "Enabled",
                "EmsConsole": "Disabled",
                "EnabledCoresPerProc": 0,
                "EnergyEfficientTurbo": "Enabled",
                "EnergyPerfBias": "BalancedPerf",
                "EnhancedProcPerf": "Disabled",
                "EppProfile": "Moderate",
                "EraseUserDefaults": "No",
                "ExtendedAmbientTemp": "Disabled",
                "ExtendedMemTest": "Disabled",
                "F11BootMenu": "Enabled",
                "FCScanPolicy": "CardConfig",
                "FanFailPolicy": "Shutdown",
                "FanInstallReq": "EnableMessaging",
                "HourFormat": "24Hours",
                "HttpSupport": "Auto",
                "HwPrefetcher": "Enabled",
                "IODCConfiguration": "Auto",
                "IntelDmiLinkFreq": "Auto",
                "IntelNicDmaChannels": "Enabled",
                "IntelPerfMonitoring": "Disabled",
                "IntelPriorityBaseFreq": "Disabled",
                "IntelProcVtd": "Enabled",
                "IntelUpiFreq": "Auto",
                "IntelUpiLinkEn": "Auto",
                "IntelUpiPowerManagement": "Enabled",
                "IntelVmdDirectAssign": "VmdDirectAssignEnabledAll",
                "IntelVmdSupport": "Disabled",
                "IntelVrocSupport": "None",
                "IntelligentProvisioning": "Enabled",
                "IpmiWatchdogTimerAction": "PowerCycle",
                "IpmiWatchdogTimerStatus": "IpmiWatchdogTimerOff",
                "IpmiWatchdogTimerTimeout": "Timeout30Min",
                "Ipv4Address": "0.0.0.0",
                "Ipv4Gateway": "0.0.0.0",
                "Ipv4PrimaryDNS": "0.0.0.0",
                "Ipv4SubnetMask": "0.0.0.0",
                "Ipv6Address": "::",
                "Ipv6ConfigPolicy": "Automatic",
                "Ipv6Duid": "Auto",
                "Ipv6Gateway": "::",
                "Ipv6PrimaryDNS": "::",
                "IpxeAutoStartScriptLocation": "Auto",
                "IpxeBootOrder": "Disabled",
                "IpxeScriptAutoStart": "Disabled",
                "IpxeScriptVerification": "Disabled",
                "IpxeStartupUrl": "",
                "LLCDeadLineAllocation": "Enabled",
                "LlcPrefetch": "Disabled",
                "LocalRemoteThreshold": "Auto",
                "MaxMemBusFreqMHz": "Auto",
                "MaxPcieSpeed": "PerPortCtrl",
                "MemClearWarmReset": "Disabled",
                "MemFastTraining": "Enabled",
                "MemMirrorMode": "Full",
                "MemPatrolScrubbing": "Enabled",
                "MemRefreshRate": "Refreshx1",
                "MemoryConfigurationViolationReporting": "Enabled",
                "MemoryRemap": "NoAction",
                "MicrosoftSecuredCoreSupport": "Disabled",
                "MinProcIdlePkgState": "C6NonRetention",
                "MinProcIdlePower": "C6",
                "MixedPowerSupplyReporting": "Enabled",
                "MkTme": "Disabled",
                "NetworkBootRetry": "Enabled",
                "NetworkBootRetryCount": 20,
                "NoExecutionProtection": "Enabled",
                "Numa": "Enabled",
                "NumaGroupSizeOpt": "Flat",
                "NvmeOptionRom": "Enabled",
                "NvmePort1": "Nvme",
                "NvmePort10": "Nvme",
                "NvmePort11": "Nvme",
                "NvmePort12": "Nvme",
                "NvmePort13": "Nvme",
                "NvmePort14": "Nvme",
                "NvmePort15": "Nvme",
                "NvmePort16": "Nvme",
                "NvmePort2": "Nvme",
                "NvmePort3": "Nvme",
                "NvmePort4": "Nvme",
                "NvmePort5": "Nvme",
                "NvmePort6": "Nvme",
                "NvmePort7": "Nvme",
                "NvmePort8": "Nvme",
                "NvmePort9": "Nvme",
                "NvmeRaid": "Disabled",
                "Ocp1AuxiliaryPower": "Enabled",
                "PatrolScrubDuration": 24,
                "PciPeerToPeerSerialization": "Disabled",
                "PciResourcePadding": "Normal",
                "PciSlot10Aspm": "Disabled",
                "PciSlot10Bifurcation": "Auto",
                "PciSlot10Enable": "Auto",
                "PciSlot10LinkSpeed": "Auto",
                "PciSlot10OptionROM": "Enabled",
                "PciSlot13Aspm": "Disabled",
                "PciSlot13Enable": "Auto",
                "PciSlot13LinkSpeed": "Auto",
                "PciSlot13OptionROM": "Enabled",
                "PciSlot1Aspm": "Disabled",
                "PciSlot1Bifurcation": "Auto",
                "PciSlot1Enable": "Auto",
                "PciSlot1LinkSpeed": "Auto",
                "PciSlot1OptionROM": "Enabled",
                "PciSlot2Bifurcation": "Auto",
                "PcieHotPlugErrControl": "HotplugSurprise",
                "PcuPMax": 0,
                "PersistentMemAddressRangeScrub": "Enabled",
                "PersistentMemBackupPowerPolicy": "WaitForBackupPower",
                "PersistentMemNumaAffinity": "IsolatedNumaDomains",
                "PersistentMemScanMem": "Enabled",
                "PlatformCertificate": "Enabled",
                "PlatformRASPolicy": "FirmwareFirst",
                "PostAsr": "PostAsrOff",
                "PostAsrDelay": "Delay30Min",
                "PostBootProgress": "Disabled",
                "PostDiscoveryMode": "Auto",
                "PostF1Prompt": "Delayed20Sec",
                "PostScreenMode": "VerboseMode",
                "PostVideoSupport": "DisplayAll",
                "PowerButton": "Enabled",
                "PowerOnDelay": "NoDelay",
                "PowerRegulator": "DynamicPowerSavings",
                "PreBootNetwork": "Auto",
                "PrebootNetworkEnvPolicy": "Auto",
                "PrebootNetworkProxy": "",
                "ProcAes": "Enabled",
                "ProcHyperthreading": "Enabled",
                "ProcRapl": 0,
                "ProcTurbo": "Enabled",
                "ProcVirtualization": "Enabled",
                "ProcX2Apic": "Enabled",
                "ProcessorConfigTDPLevel": "Normal",
                "ProcessorPhysicalAddress": "Limited",
                "RedundantPowerSupply": "BalancedMode",
                "RemoteXptPrefetcher": "Auto",
                "RemovableFlashBootSeq": "ExternalKeysFirst",
                "RestoreDefaults": "No",
                "RestoreManufacturingDefaults": "No",
                "SataSanitize": "Disabled",
                "SataSecureErase": "Disabled",
                "SaveUserDefaults": "No",
                "SciRasSupport": "Ghesv1Support",
                "SecStartBackupImage": "Disabled",
                "SecureBootStatus": "Disabled",
                "SerialConsoleBaudRate": "BaudRate115200",
                "SerialConsoleEmulation": "Vt100Plus",
                "SerialConsolePort": "Auto",
                "SerialPortDtrSupport": "Disabled",
                "ServerAssetTag": "",
                "ServerConfigLockStatus": "Disabled",
                "ServerName": "",
                "ServerOtherInfo": "",
                "ServerPrimaryOs": "",
                "ServiceEmail": "",
                "ServiceName": "",
                "ServiceOtherInfo": "",
                "ServicePhone": "",
                "SetupBrowserSelection": "Auto",
                "SgxAutoMpRegistrationAgent": "Enabled",
                "SgxEnable": "Disabled",
                "SgxLaunchControlPolicy": "IntelLocked",
                "SgxLePublicKeyHash0": "",
                "SgxLePublicKeyHash1": "",
                "SgxLePublicKeyHash2": "",
                "SgxLePublicKeyHash3": "",
                "SgxLePublicKeyWriteEnable": "Enabled",
                "SgxPrmrrSize": "2Gb",
                "Slot10EoiBroadcastSupport": "Disabled",
                "Slot10MctpBroadcastSupport": "Enabled",
                "Slot10NicBoot1": "NetworkBoot",
                "Slot10NicBoot2": "Disabled",
                "Slot10NicBoot3": "Disabled",
                "Slot10NicBoot4": "Disabled",
                "Slot1EoiBroadcastSupport": "Disabled",
                "Slot1MctpBroadcastSupport": "Enabled",
                "Slot1StorageBoot": "ThirtyTwoTargets",
                "Slot2EoiBroadcastSupport": "Disabled",
                "Slot2MctpBroadcastSupport": "Enabled",
                "SnoopResponseHoldOff": 9,
                "Sriov": "Enabled",
                "StaleAtoS": "Disabled",
                "SubNumaClustering": "Disabled",
                "ThermalConfig": "OptimalCooling",
                "ThermalShutdown": "Enabled",
                "TimeFormat": "Utc",
                "TimeZone": "Utc0",
                "Tme": "Disabled",
                "TmeExclusiveBase": "",
                "TmeExclusiveLen": "",
                "TpmChipId": "None",
                "TpmFips": "NotSpecified",
                "TpmState": "NotPresent",
                "TpmType": "NoTpm",
                "Tsx": "Enabled",
                "UefiOptimizedBoot": "Enabled",
                "UefiSerialDebugLevel": "ErrorsOnly",
                "UefiShellBootOrder": "Disabled",
                "UefiShellPhysicalPresenceKeystroke": "Enabled",
                "UefiShellScriptVerification": "Disabled",
                "UefiShellStartup": "Disabled",
                "UefiShellStartupLocation": "Auto",
                "UefiShellStartupUrl": "",
                "UefiShellStartupUrlFromDhcp": "Disabled",
                "UefiVariableAccessFwControl": "Disabled",
                "UncoreFreqScaling": "Auto",
                "UpiPrefetcher": "Enabled",
                "UrlBootFile": "",
                "UrlBootFile2": "",
                "UrlBootFile3": "",
                "UrlBootFile4": "",
                "UsbBoot": "Enabled",
                "UsbControl": "UsbEnabled",
                "UserDefaultsState": "Disabled",
                "UtilityLang": "English",
                "VirtualNuma": "Disabled",
                "VirtualSerialPort": "Com1Irq4",
                "VlanControl": "Disabled",
                "VlanId": 0,
                "VlanPriority": 0,
                "VmProprietaryPageRetireSupport": "Enabled",
                "VmdonCpu1Stack5Port1": "Disabled",
                "VmdonCpu1Stack5Port2": "Disabled",
                "VmdonCpu1Stack5Port3": "Disabled",
                "VmdonCpu1Stack5Port4": "Disabled",
                "VmdonCpu2Stack5Port1": "Disabled",
                "VmdonCpu2Stack5Port2": "Disabled",
                "VmdonCpu2Stack5Port3": "Disabled",
                "VmdonCpu2Stack5Port4": "Disabled",
                "WakeOnLan": "Enabled",
                "WorkloadProfile": "GeneralPowerEfficientCompute",
                "XptPrefetcher": "Auto",
                "iSCSISoftwareInitiator": "Enabled"
            }
        }
    ],
    "Capabilities": {
        "BaseConfig": true,
        "BaseConfigs": false
    },
    "Id": "baseconfigs",
    "Name": "BIOS Default Settings"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/baseconfigs/

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBaseConfigs.HpeBaseConfigs",
    "@odata.etag": "W/\"2BF923428033A4A4A4746C0150A2AC0B\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/baseconfigs/",
    "@odata.type": "#HpeBaseConfigs.v2_0_0.HpeBaseConfigs",
    "BaseConfigs": [
        {
            "default": {
                "AccessControlService": "Enabled",
                "AcpiHpet": "Enabled",
                "AcpiRootBridgePxm": "Enabled",
                "AcpiSlit": "Enabled",
                "AdjSecPrefetch": "Enabled",
                "AdminEmail": "",
                "AdminName": "",
                "AdminOtherInfo": "",
                "AdminPhone": "",
                "AdvCrashDumpMode": "Disabled",
                "AdvancedMemProtection": "Auto",
                "AllowLoginWithIlo": "Disabled",
                "AssetTagProtection": "Unlocked",
                "AutoPowerOn": "RestoreLastState",
                "BootMode": "Uefi",
                "BootOrderPolicy": "RetryIndefinitely",
                "CollabPowerControl": "Enabled",
                "ConsistentDevNaming": "LomsAndSlots",
                "CustomPostMessage": "",
                "DaylightSavingsTime": "DaylightSavingsTimeDisabled",
                "DcuIpPrefetcher": "Enabled",
                "DcuStreamPrefetcher": "Enabled",
                "DeadBlockPredictor": "Disabled",
                "Dhcpv4": "Enabled",
                "DirectToUpi": "Auto",
                "DramRapl": 0,
                "DramRaplLimit": "Disabled",
                "DramRaplReport": "Enabled",
                "DynamicPowerCapping": "Disabled",
                "EmbVideoConnection": "Auto",
                "EmbeddedDiagnostics": "Enabled",
                "EmbeddedIpxe": "Enabled",
                "EmbeddedSata": "Ahci",
                "EmbeddedSerialPort": "Com2Irq3",
                "EmbeddedUefiShell": "Enabled",
                "EmsConsole": "Disabled",
                "EnabledCoresPerProc": 0,
                "EnergyEfficientTurbo": "Enabled",
                "EnergyPerfBias": "BalancedPerf",
                "EnhancedProcPerf": "Disabled",
                "EppProfile": "Moderate",
                "EraseUserDefaults": "No",
                "ExtendedAmbientTemp": "Disabled",
                "ExtendedMemTest": "Disabled",
                "F11BootMenu": "Enabled",
                "FCScanPolicy": "CardConfig",
                "FanFailPolicy": "Shutdown",
                "FanInstallReq": "EnableMessaging",
                "HourFormat": "24Hours",
                "HttpSupport": "Auto",
                "HwPrefetcher": "Enabled",
                "IODCConfiguration": "Auto",
                "IntelDmiLinkFreq": "Auto",
                "IntelNicDmaChannels": "Enabled",
                "IntelPerfMonitoring": "Disabled",
                "IntelPriorityBaseFreq": "Disabled",
                "IntelProcVtd": "Enabled",
                "IntelUpiFreq": "Auto",
                "IntelUpiLinkEn": "Auto",
                "IntelUpiPowerManagement": "Enabled",
                "IntelVmdDirectAssign": "VmdDirectAssignEnabledAll",
                "IntelVmdSupport": "Disabled",
                "IntelVrocSupport": "None",
                "IntelligentProvisioning": "Enabled",
                "IpmiWatchdogTimerAction": "PowerCycle",
                "IpmiWatchdogTimerStatus": "IpmiWatchdogTimerOff",
                "IpmiWatchdogTimerTimeout": "Timeout30Min",
                "Ipv4Address": "0.0.0.0",
                "Ipv4Gateway": "0.0.0.0",
                "Ipv4PrimaryDNS": "0.0.0.0",
                "Ipv4SubnetMask": "0.0.0.0",
                "Ipv6Address": "::",
                "Ipv6ConfigPolicy": "Automatic",
                "Ipv6Duid": "Auto",
                "Ipv6Gateway": "::",
                "Ipv6PrimaryDNS": "::",
                "IpxeAutoStartScriptLocation": "Auto",
                "IpxeBootOrder": "Disabled",
                "IpxeScriptAutoStart": "Disabled",
                "IpxeScriptVerification": "Disabled",
                "IpxeStartupUrl": "",
                "LLCDeadLineAllocation": "Enabled",
                "LlcPrefetch": "Disabled",
                "LocalRemoteThreshold": "Auto",
                "MaxMemBusFreqMHz": "Auto",
                "MaxPcieSpeed": "PerPortCtrl",
                "MemClearWarmReset": "Disabled",
                "MemFastTraining": "Enabled",
                "MemMirrorMode": "Full",
                "MemPatrolScrubbing": "Enabled",
                "MemRefreshRate": "Refreshx1",
                "MemoryConfigurationViolationReporting": "Enabled",
                "MemoryRemap": "NoAction",
                "MicrosoftSecuredCoreSupport": "Disabled",
                "MinProcIdlePkgState": "C6NonRetention",
                "MinProcIdlePower": "C6",
                "MixedPowerSupplyReporting": "Enabled",
                "MkTme": "Disabled",
                "NetworkBootRetry": "Enabled",
                "NetworkBootRetryCount": 20,
                "NoExecutionProtection": "Enabled",
                "Numa": "Enabled",
                "NumaGroupSizeOpt": "Flat",
                "NvmeOptionRom": "Enabled",
                "NvmePort1": "Nvme",
                "NvmePort10": "Nvme",
                "NvmePort11": "Nvme",
                "NvmePort12": "Nvme",
                "NvmePort13": "Nvme",
                "NvmePort14": "Nvme",
                "NvmePort15": "Nvme",
                "NvmePort16": "Nvme",
                "NvmePort2": "Nvme",
                "NvmePort3": "Nvme",
                "NvmePort4": "Nvme",
                "NvmePort5": "Nvme",
                "NvmePort6": "Nvme",
                "NvmePort7": "Nvme",
                "NvmePort8": "Nvme",
                "NvmePort9": "Nvme",
                "NvmeRaid": "Disabled",
                "Ocp1AuxiliaryPower": "Enabled",
                "PatrolScrubDuration": 24,
                "PciPeerToPeerSerialization": "Disabled",
                "PciResourcePadding": "Normal",
                "PciSlot10Aspm": "Disabled",
                "PciSlot10Bifurcation": "Auto",
                "PciSlot10Enable": "Auto",
                "PciSlot10LinkSpeed": "Auto",
                "PciSlot10OptionROM": "Enabled",
                "PciSlot13Aspm": "Disabled",
                "PciSlot13Enable": "Auto",
                "PciSlot13LinkSpeed": "Auto",
                "PciSlot13OptionROM": "Enabled",
                "PciSlot1Aspm": "Disabled",
                "PciSlot1Bifurcation": "Auto",
                "PciSlot1Enable": "Auto",
                "PciSlot1LinkSpeed": "Auto",
                "PciSlot1OptionROM": "Enabled",
                "PciSlot2Bifurcation": "Auto",
                "PcieHotPlugErrControl": "HotplugSurprise",
                "PcuPMax": 0,
                "PersistentMemAddressRangeScrub": "Enabled",
                "PersistentMemBackupPowerPolicy": "WaitForBackupPower",
                "PersistentMemNumaAffinity": "IsolatedNumaDomains",
                "PersistentMemScanMem": "Enabled",
                "PlatformCertificate": "Enabled",
                "PlatformRASPolicy": "FirmwareFirst",
                "PostAsr": "PostAsrOff",
                "PostAsrDelay": "Delay30Min",
                "PostBootProgress": "Disabled",
                "PostDiscoveryMode": "Auto",
                "PostF1Prompt": "Delayed20Sec",
                "PostScreenMode": "VerboseMode",
                "PostVideoSupport": "DisplayAll",
                "PowerButton": "Enabled",
                "PowerOnDelay": "NoDelay",
                "PowerRegulator": "DynamicPowerSavings",
                "PreBootNetwork": "Auto",
                "PrebootNetworkEnvPolicy": "Auto",
                "PrebootNetworkProxy": "",
                "ProcAes": "Enabled",
                "ProcHyperthreading": "Enabled",
                "ProcRapl": 0,
                "ProcTurbo": "Enabled",
                "ProcVirtualization": "Enabled",
                "ProcX2Apic": "Enabled",
                "ProcessorConfigTDPLevel": "Normal",
                "ProcessorPhysicalAddress": "Limited",
                "RedundantPowerSupply": "BalancedMode",
                "RemoteXptPrefetcher": "Auto",
                "RemovableFlashBootSeq": "ExternalKeysFirst",
                "RestoreDefaults": "No",
                "RestoreManufacturingDefaults": "No",
                "SataSanitize": "Disabled",
                "SataSecureErase": "Disabled",
                "SaveUserDefaults": "No",
                "SciRasSupport": "Ghesv1Support",
                "SecStartBackupImage": "Disabled",
                "SecureBootStatus": "Disabled",
                "SerialConsoleBaudRate": "BaudRate115200",
                "SerialConsoleEmulation": "Vt100Plus",
                "SerialConsolePort": "Auto",
                "SerialPortDtrSupport": "Disabled",
                "ServerAssetTag": "",
                "ServerConfigLockStatus": "Disabled",
                "ServerName": "",
                "ServerOtherInfo": "",
                "ServerPrimaryOs": "",
                "ServiceEmail": "",
                "ServiceName": "",
                "ServiceOtherInfo": "",
                "ServicePhone": "",
                "SetupBrowserSelection": "Auto",
                "SgxAutoMpRegistrationAgent": "Enabled",
                "SgxEnable": "Disabled",
                "SgxLaunchControlPolicy": "IntelLocked",
                "SgxLePublicKeyHash0": "",
                "SgxLePublicKeyHash1": "",
                "SgxLePublicKeyHash2": "",
                "SgxLePublicKeyHash3": "",
                "SgxLePublicKeyWriteEnable": "Enabled",
                "SgxPrmrrSize": "2Gb",
                "Slot10EoiBroadcastSupport": "Disabled",
                "Slot10MctpBroadcastSupport": "Enabled",
                "Slot10NicBoot1": "NetworkBoot",
                "Slot10NicBoot2": "Disabled",
                "Slot10NicBoot3": "Disabled",
                "Slot10NicBoot4": "Disabled",
                "Slot1EoiBroadcastSupport": "Disabled",
                "Slot1MctpBroadcastSupport": "Enabled",
                "Slot1StorageBoot": "ThirtyTwoTargets",
                "Slot2EoiBroadcastSupport": "Disabled",
                "Slot2MctpBroadcastSupport": "Enabled",
                "SnoopResponseHoldOff": 9,
                "Sriov": "Enabled",
                "StaleAtoS": "Disabled",
                "SubNumaClustering": "Disabled",
                "ThermalConfig": "OptimalCooling",
                "ThermalShutdown": "Enabled",
                "TimeFormat": "Utc",
                "TimeZone": "Utc0",
                "Tme": "Disabled",
                "TmeExclusiveBase": "",
                "TmeExclusiveLen": "",
                "TpmChipId": "None",
                "TpmFips": "NotSpecified",
                "TpmState": "NotPresent",
                "TpmType": "NoTpm",
                "Tsx": "Enabled",
                "UefiOptimizedBoot": "Enabled",
                "UefiSerialDebugLevel": "ErrorsOnly",
                "UefiShellBootOrder": "Disabled",
                "UefiShellPhysicalPresenceKeystroke": "Enabled",
                "UefiShellScriptVerification": "Disabled",
                "UefiShellStartup": "Disabled",
                "UefiShellStartupLocation": "Auto",
                "UefiShellStartupUrl": "",
                "UefiShellStartupUrlFromDhcp": "Disabled",
                "UefiVariableAccessFwControl": "Disabled",
                "UncoreFreqScaling": "Auto",
                "UpiPrefetcher": "Enabled",
                "UrlBootFile": "",
                "UrlBootFile2": "",
                "UrlBootFile3": "",
                "UrlBootFile4": "",
                "UsbBoot": "Enabled",
                "UsbControl": "UsbEnabled",
                "UserDefaultsState": "Disabled",
                "UtilityLang": "English",
                "VirtualNuma": "Disabled",
                "VirtualSerialPort": "Com1Irq4",
                "VlanControl": "Disabled",
                "VlanId": 0,
                "VlanPriority": 0,
                "VmProprietaryPageRetireSupport": "Enabled",
                "VmdonCpu1Stack5Port1": "Disabled",
                "VmdonCpu1Stack5Port2": "Disabled",
                "VmdonCpu1Stack5Port3": "Disabled",
                "VmdonCpu1Stack5Port4": "Disabled",
                "VmdonCpu2Stack5Port1": "Disabled",
                "VmdonCpu2Stack5Port2": "Disabled",
                "VmdonCpu2Stack5Port3": "Disabled",
                "VmdonCpu2Stack5Port4": "Disabled",
                "WakeOnLan": "Enabled",
                "WorkloadProfile": "GeneralPowerEfficientCompute",
                "XptPrefetcher": "Auto",
                "iSCSISoftwareInitiator": "Enabled"
            }
        }
    ],
    "Capabilities": {
        "BaseConfig": true,
        "BaseConfigs": false
    },
    "Id": "baseconfigs",
    "Name": "BIOS Default Settings"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/boot

```{
    "@Redfish.Settings": {
        "@odata.type": "#Settings.v1_0_0.Settings",
        "ETag": "6F4A7D2F",
        "Messages": [
            {
                "MessageId": "Base.1.0.Success"
            }
        ],
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/settings/"
        },
        "Time": "2021-08-18T10:46:50+00:00"
    },
    "@odata.context": "/redfish/v1/$metadata#HpeServerBootSettings.HpeServerBootSettings",
    "@odata.etag": "W/\"CEDA1C821C18636363CC620E5E2751D0\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/",
    "@odata.type": "#HpeServerBootSettings.v2_0_0.HpeServerBootSettings",
    "BootSources": [
        {
            "BootOptionNumber": "0019",
            "BootString": "VMware ESXi",
            "CorrelatableID": "HD(1,GPT,E0462D22-8BF6-4172-B8A3-B8F56754A170,0x40,0x32000)/\\EFI\\VMware\\safeboot64.efi",
            "StructuredBootString": "Unknown.Unknown.200.2",
            "UEFIDevicePath": "HD(1,GPT,E0462D22-8BF6-4172-B8A3-B8F56754A170,0x40,0x32000)/\\EFI\\VMware\\safeboot64.efi"
        },
        {
            "BootOptionNumber": "000E",
            "BootString": "Generic USB Boot",
            "CorrelatableID": "UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)",
            "StructuredBootString": "Generic.USB.1.1",
            "UEFIDevicePath": "UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)"
        },
        {
            "BootOptionNumber": "000F",
            "BootString": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 1",
            "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "HD.Slot.1.2",
            "UEFIDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x1,0x0)"
        },
        {
            "BootOptionNumber": "0010",
            "BootString": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 2",
            "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "HD.Slot.1.3",
            "UEFIDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x2,0x0)"
        },
        {
            "BootOptionNumber": "0011",
            "BootString": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 3",
            "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "HD.Slot.1.4",
            "UEFIDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x3,0x0)"
        },
        {
            "BootOptionNumber": "0015",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (HTTP(S) IPv4)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.Httpv4",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv4(0.0.0.0)/Uri()"
        },
        {
            "BootOptionNumber": "0016",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (PXE IPv4)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.IPv4",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv4(0.0.0.0)"
        },
        {
            "BootOptionNumber": "0013",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (PXE IPv6)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.IPv6",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)"
        },
        {
            "BootOptionNumber": "0014",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (HTTP(S) IPv6)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.Httpv6",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()"
        },
        {
            "BootOptionNumber": "0012",
            "BootString": "Storage Slot 13 NVMe Drive 0 : HPE NS204i-r Gen10+ Boot Controller",
            "CorrelatableID": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "NVMe.Slot.2.1",
            "UEFIDevicePath": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)/NVMe(0x1,01-00-00-0A-0A-43-50-00)"
        }
    ],
    "DefaultBootOrder": [
        "Cd",
        "Usb",
        "EmbeddedStorage",
        "PcieSlotStorage",
        "EmbeddedFlexLOM",
        "PcieSlotNic",
        "UefiShell",
        "iPXE"
    ],
    "DesiredBootDevices": [
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        }
    ],
    "Id": "boot",
    "Name": "Boot Order Current Settings",
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"8A7B2429C5664C4C4C1ADDE811DA8FDB\""
            }
        }
    },
    "PersistentBootConfigOrder": [
        "Unknown.Unknown.200.2",
        "Generic.USB.1.1",
        "HD.Slot.1.2",
        "HD.Slot.1.3",
        "HD.Slot.1.4",
        "OCP.Slot.10.1.Httpv4",
        "OCP.Slot.10.1.IPv4",
        "OCP.Slot.10.1.IPv6",
        "OCP.Slot.10.1.Httpv6",
        "NVMe.Slot.2.1"
    ]
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/boot/

```{
    "@Redfish.Settings": {
        "@odata.type": "#Settings.v1_0_0.Settings",
        "ETag": "6F4A7D2F",
        "Messages": [
            {
                "MessageId": "Base.1.0.Success"
            }
        ],
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/settings/"
        },
        "Time": "2021-08-18T10:46:50+00:00"
    },
    "@odata.context": "/redfish/v1/$metadata#HpeServerBootSettings.HpeServerBootSettings",
    "@odata.etag": "W/\"CEDA1C821C18636363CC620E5E2751D0\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/",
    "@odata.type": "#HpeServerBootSettings.v2_0_0.HpeServerBootSettings",
    "BootSources": [
        {
            "BootOptionNumber": "0019",
            "BootString": "VMware ESXi",
            "CorrelatableID": "HD(1,GPT,E0462D22-8BF6-4172-B8A3-B8F56754A170,0x40,0x32000)/\\EFI\\VMware\\safeboot64.efi",
            "StructuredBootString": "Unknown.Unknown.200.2",
            "UEFIDevicePath": "HD(1,GPT,E0462D22-8BF6-4172-B8A3-B8F56754A170,0x40,0x32000)/\\EFI\\VMware\\safeboot64.efi"
        },
        {
            "BootOptionNumber": "000E",
            "BootString": "Generic USB Boot",
            "CorrelatableID": "UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)",
            "StructuredBootString": "Generic.USB.1.1",
            "UEFIDevicePath": "UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)"
        },
        {
            "BootOptionNumber": "000F",
            "BootString": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 1",
            "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "HD.Slot.1.2",
            "UEFIDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x1,0x0)"
        },
        {
            "BootOptionNumber": "0010",
            "BootString": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 2",
            "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "HD.Slot.1.3",
            "UEFIDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x2,0x0)"
        },
        {
            "BootOptionNumber": "0011",
            "BootString": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 3",
            "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "HD.Slot.1.4",
            "UEFIDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x3,0x0)"
        },
        {
            "BootOptionNumber": "0015",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (HTTP(S) IPv4)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.Httpv4",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv4(0.0.0.0)/Uri()"
        },
        {
            "BootOptionNumber": "0016",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (PXE IPv4)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.IPv4",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv4(0.0.0.0)"
        },
        {
            "BootOptionNumber": "0013",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (PXE IPv6)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.IPv6",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)"
        },
        {
            "BootOptionNumber": "0014",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (HTTP(S) IPv6)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.Httpv6",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()"
        },
        {
            "BootOptionNumber": "0012",
            "BootString": "Storage Slot 13 NVMe Drive 0 : HPE NS204i-r Gen10+ Boot Controller",
            "CorrelatableID": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "NVMe.Slot.2.1",
            "UEFIDevicePath": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)/NVMe(0x1,01-00-00-0A-0A-43-50-00)"
        }
    ],
    "DefaultBootOrder": [
        "Cd",
        "Usb",
        "EmbeddedStorage",
        "PcieSlotStorage",
        "EmbeddedFlexLOM",
        "PcieSlotNic",
        "UefiShell",
        "iPXE"
    ],
    "DesiredBootDevices": [
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        }
    ],
    "Id": "boot",
    "Name": "Boot Order Current Settings",
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"8A7B2429C5664C4C4C1ADDE811DA8FDB\""
            }
        }
    },
    "PersistentBootConfigOrder": [
        "Unknown.Unknown.200.2",
        "Generic.USB.1.1",
        "HD.Slot.1.2",
        "HD.Slot.1.3",
        "HD.Slot.1.4",
        "OCP.Slot.10.1.Httpv4",
        "OCP.Slot.10.1.IPv4",
        "OCP.Slot.10.1.IPv6",
        "OCP.Slot.10.1.Httpv6",
        "NVMe.Slot.2.1"
    ]
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/boot/baseconfigs

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBaseConfigs.HpeBaseConfigs",
    "@odata.etag": "W/\"4917AC199B189F9F9FD676D8EEB3930E\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/baseconfigs/",
    "@odata.type": "#HpeBaseConfigs.v2_0_0.HpeBaseConfigs",
    "BaseConfigs": [
        {
            "default": {
                "DefaultBootOrder": [
                    "Cd",
                    "Usb",
                    "EmbeddedStorage",
                    "PcieSlotStorage",
                    "EmbeddedFlexLOM",
                    "PcieSlotNic",
                    "UefiShell",
                    "iPXE"
                ]
            }
        }
    ],
    "Capabilities": {
        "BaseConfig": true,
        "BaseConfigs": false
    },
    "Id": "baseconfigs",
    "Name": "BIOS Boot Order Default Settings"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/boot/baseconfigs/

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBaseConfigs.HpeBaseConfigs",
    "@odata.etag": "W/\"4917AC199B189F9F9FD676D8EEB3930E\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/baseconfigs/",
    "@odata.type": "#HpeBaseConfigs.v2_0_0.HpeBaseConfigs",
    "BaseConfigs": [
        {
            "default": {
                "DefaultBootOrder": [
                    "Cd",
                    "Usb",
                    "EmbeddedStorage",
                    "PcieSlotStorage",
                    "EmbeddedFlexLOM",
                    "PcieSlotNic",
                    "UefiShell",
                    "iPXE"
                ]
            }
        }
    ],
    "Capabilities": {
        "BaseConfig": true,
        "BaseConfigs": false
    },
    "Id": "baseconfigs",
    "Name": "BIOS Boot Order Default Settings"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/boot/settings

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerBootSettings.HpeServerBootSettings",
    "@odata.etag": "W/\"8A7B2429C5664C4C4C1ADDE811DA8FDB\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/settings/",
    "@odata.type": "#HpeServerBootSettings.v2_0_0.HpeServerBootSettings",
    "BootSources": [
        {
            "BootOptionNumber": "0019",
            "BootString": "VMware ESXi",
            "CorrelatableID": "HD(1,GPT,E0462D22-8BF6-4172-B8A3-B8F56754A170,0x40,0x32000)/\\EFI\\VMware\\safeboot64.efi",
            "StructuredBootString": "Unknown.Unknown.200.2",
            "UEFIDevicePath": "HD(1,GPT,E0462D22-8BF6-4172-B8A3-B8F56754A170,0x40,0x32000)/\\EFI\\VMware\\safeboot64.efi"
        },
        {
            "BootOptionNumber": "000E",
            "BootString": "Generic USB Boot",
            "CorrelatableID": "UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)",
            "StructuredBootString": "Generic.USB.1.1",
            "UEFIDevicePath": "UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)"
        },
        {
            "BootOptionNumber": "000F",
            "BootString": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 1",
            "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "HD.Slot.1.2",
            "UEFIDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x1,0x0)"
        },
        {
            "BootOptionNumber": "0010",
            "BootString": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 2",
            "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "HD.Slot.1.3",
            "UEFIDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x2,0x0)"
        },
        {
            "BootOptionNumber": "0011",
            "BootString": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 3",
            "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "HD.Slot.1.4",
            "UEFIDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x3,0x0)"
        },
        {
            "BootOptionNumber": "0015",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (HTTP(S) IPv4)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.Httpv4",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv4(0.0.0.0)/Uri()"
        },
        {
            "BootOptionNumber": "0016",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (PXE IPv4)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.IPv4",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv4(0.0.0.0)"
        },
        {
            "BootOptionNumber": "0013",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (PXE IPv6)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.IPv6",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)"
        },
        {
            "BootOptionNumber": "0014",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (HTTP(S) IPv6)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.Httpv6",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()"
        },
        {
            "BootOptionNumber": "0012",
            "BootString": "Storage Slot 13 NVMe Drive 0 : HPE NS204i-r Gen10+ Boot Controller",
            "CorrelatableID": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "NVMe.Slot.2.1",
            "UEFIDevicePath": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)/NVMe(0x1,01-00-00-0A-0A-43-50-00)"
        }
    ],
    "DefaultBootOrder": [
        "Cd",
        "Usb",
        "EmbeddedStorage",
        "PcieSlotStorage",
        "EmbeddedFlexLOM",
        "PcieSlotNic",
        "UefiShell",
        "iPXE"
    ],
    "DesiredBootDevices": [
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        }
    ],
    "Id": "settings",
    "Name": "Boot Order Pending Settings",
    "PersistentBootConfigOrder": [
        "Unknown.Unknown.200.2",
        "Generic.USB.1.1",
        "HD.Slot.1.2",
        "HD.Slot.1.3",
        "HD.Slot.1.4",
        "OCP.Slot.10.1.Httpv4",
        "OCP.Slot.10.1.IPv4",
        "OCP.Slot.10.1.IPv6",
        "OCP.Slot.10.1.Httpv6",
        "NVMe.Slot.2.1"
    ]
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/boot/settings/

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerBootSettings.HpeServerBootSettings",
    "@odata.etag": "W/\"8A7B2429C5664C4C4C1ADDE811DA8FDB\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/boot/settings/",
    "@odata.type": "#HpeServerBootSettings.v2_0_0.HpeServerBootSettings",
    "BootSources": [
        {
            "BootOptionNumber": "0019",
            "BootString": "VMware ESXi",
            "CorrelatableID": "HD(1,GPT,E0462D22-8BF6-4172-B8A3-B8F56754A170,0x40,0x32000)/\\EFI\\VMware\\safeboot64.efi",
            "StructuredBootString": "Unknown.Unknown.200.2",
            "UEFIDevicePath": "HD(1,GPT,E0462D22-8BF6-4172-B8A3-B8F56754A170,0x40,0x32000)/\\EFI\\VMware\\safeboot64.efi"
        },
        {
            "BootOptionNumber": "000E",
            "BootString": "Generic USB Boot",
            "CorrelatableID": "UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)",
            "StructuredBootString": "Generic.USB.1.1",
            "UEFIDevicePath": "UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)"
        },
        {
            "BootOptionNumber": "000F",
            "BootString": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 1",
            "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "HD.Slot.1.2",
            "UEFIDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x1,0x0)"
        },
        {
            "BootOptionNumber": "0010",
            "BootString": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 2",
            "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "HD.Slot.1.3",
            "UEFIDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x2,0x0)"
        },
        {
            "BootOptionNumber": "0011",
            "BootString": "Slot 1 : HPE MR416i-p Gen10+ - Box 1, Bay 3",
            "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "HD.Slot.1.4",
            "UEFIDevicePath": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Ctrl(0x0)/Scsi(0x3,0x0)"
        },
        {
            "BootOptionNumber": "0015",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (HTTP(S) IPv4)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.Httpv4",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv4(0.0.0.0)/Uri()"
        },
        {
            "BootOptionNumber": "0016",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (PXE IPv4)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.IPv4",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv4(0.0.0.0)"
        },
        {
            "BootOptionNumber": "0013",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (PXE IPv6)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.IPv6",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)"
        },
        {
            "BootOptionNumber": "0014",
            "BootString": "OCP Slot 10 Port 1 : Intel(R) Ethernet Network Adapter I350-T4 for OCP NIC 3.0 (HTTP(S) IPv6)",
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "OCP.Slot.10.1.Httpv6",
            "UEFIDevicePath": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(6805CAE1367C,0x1)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()"
        },
        {
            "BootOptionNumber": "0012",
            "BootString": "Storage Slot 13 NVMe Drive 0 : HPE NS204i-r Gen10+ Boot Controller",
            "CorrelatableID": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "StructuredBootString": "NVMe.Slot.2.1",
            "UEFIDevicePath": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)/NVMe(0x1,01-00-00-0A-0A-43-50-00)"
        }
    ],
    "DefaultBootOrder": [
        "Cd",
        "Usb",
        "EmbeddedStorage",
        "PcieSlotStorage",
        "EmbeddedFlexLOM",
        "PcieSlotNic",
        "UefiShell",
        "iPXE"
    ],
    "DesiredBootDevices": [
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        },
        {
            "CorrelatableID": "",
            "Lun": "",
            "Wwn": "",
            "iScsiTargetName": ""
        }
    ],
    "Id": "settings",
    "Name": "Boot Order Pending Settings",
    "PersistentBootConfigOrder": [
        "Unknown.Unknown.200.2",
        "Generic.USB.1.1",
        "HD.Slot.1.2",
        "HD.Slot.1.3",
        "HD.Slot.1.4",
        "OCP.Slot.10.1.Httpv4",
        "OCP.Slot.10.1.IPv4",
        "OCP.Slot.10.1.IPv6",
        "OCP.Slot.10.1.Httpv6",
        "NVMe.Slot.2.1"
    ]
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/iscsi

```{
    "@Redfish.Settings": {
        "@odata.type": "#Settings.v1_0_0.Settings",
        "ETag": "",
        "Messages": [
            {
                "MessageId": "Base.1.0.Success"
            }
        ],
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/settings/"
        },
        "Time": null
    },
    "@odata.context": "/redfish/v1/$metadata#HpeiSCSISoftwareInitiator.HpeiSCSISoftwareInitiator",
    "@odata.etag": "W/\"0ABDA0E8B8C4F7F7F70D5EBAF610760C\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/",
    "@odata.type": "#HpeiSCSISoftwareInitiator.v2_0_0.HpeiSCSISoftwareInitiator",
    "Id": "iscsi",
    "Name": "iSCSI Software Initiator Current Settings",
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"CB481BE787534A4A4A1EC439DA313400\""
            }
        }
    },
    "iSCSIInitiatorName": "iqn.2015-02.com.hpe:uefi-U46",
    "iSCSINicSources": [
        "Slot10NicBoot1",
        "Slot10NicBoot2",
        "Slot10NicBoot3",
        "Slot10NicBoot4"
    ],
    "iSCSISources": [
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        },
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        },
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        },
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        }
    ]
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/iscsi/

```{
    "@Redfish.Settings": {
        "@odata.type": "#Settings.v1_0_0.Settings",
        "ETag": "",
        "Messages": [
            {
                "MessageId": "Base.1.0.Success"
            }
        ],
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/settings/"
        },
        "Time": null
    },
    "@odata.context": "/redfish/v1/$metadata#HpeiSCSISoftwareInitiator.HpeiSCSISoftwareInitiator",
    "@odata.etag": "W/\"0ABDA0E8B8C4F7F7F70D5EBAF610760C\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/",
    "@odata.type": "#HpeiSCSISoftwareInitiator.v2_0_0.HpeiSCSISoftwareInitiator",
    "Id": "iscsi",
    "Name": "iSCSI Software Initiator Current Settings",
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"CB481BE787534A4A4A1EC439DA313400\""
            }
        }
    },
    "iSCSIInitiatorName": "iqn.2015-02.com.hpe:uefi-U46",
    "iSCSINicSources": [
        "Slot10NicBoot1",
        "Slot10NicBoot2",
        "Slot10NicBoot3",
        "Slot10NicBoot4"
    ],
    "iSCSISources": [
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        },
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        },
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        },
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        }
    ]
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/iscsi/baseconfigs

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBaseConfigs.HpeBaseConfigs",
    "@odata.etag": "W/\"2ECCA727C95F54545432B6277594742E\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/baseconfigs/",
    "@odata.type": "#HpeBaseConfigs.v2_0_0.HpeBaseConfigs",
    "BaseConfigs": [
        {
            "default": {
                "iSCSIInitiatorName": "iqn.2015-02.com.hpe:uefi-U46-VYRBX9UJ4S",
                "iSCSISources": [
                    {
                        "StructuredBootString": null,
                        "UEFIDevicePath": null,
                        "iSCSIAttemptInstance": 0,
                        "iSCSIAttemptName": "",
                        "iSCSIAuthenticationMethod": "None",
                        "iSCSIChapSecret": "",
                        "iSCSIChapType": "OneWay",
                        "iSCSIChapUsername": "",
                        "iSCSIConnectRetry": 3,
                        "iSCSIConnectTimeoutMS": 20000,
                        "iSCSIConnection": "Disabled",
                        "iSCSIInitiatorGateway": "0.0.0.0",
                        "iSCSIInitiatorInfoViaDHCP": true,
                        "iSCSIInitiatorIpAddress": "0.0.0.0",
                        "iSCSIInitiatorNetmask": "0.0.0.0",
                        "iSCSIIpAddressType": "IPv4",
                        "iSCSILUN": "0",
                        "iSCSINicSource": null,
                        "iSCSIReverseChapSecret": "",
                        "iSCSIReverseChapUsername": "",
                        "iSCSITargetInfoViaDHCP": true,
                        "iSCSITargetIpAddress": "0.0.0.0",
                        "iSCSITargetName": "",
                        "iSCSITargetTcpPort": 3260
                    },
                    {
                        "StructuredBootString": null,
                        "UEFIDevicePath": null,
                        "iSCSIAttemptInstance": 0,
                        "iSCSIAttemptName": "",
                        "iSCSIAuthenticationMethod": "None",
                        "iSCSIChapSecret": "",
                        "iSCSIChapType": "OneWay",
                        "iSCSIChapUsername": "",
                        "iSCSIConnectRetry": 3,
                        "iSCSIConnectTimeoutMS": 20000,
                        "iSCSIConnection": "Disabled",
                        "iSCSIInitiatorGateway": "0.0.0.0",
                        "iSCSIInitiatorInfoViaDHCP": true,
                        "iSCSIInitiatorIpAddress": "0.0.0.0",
                        "iSCSIInitiatorNetmask": "0.0.0.0",
                        "iSCSIIpAddressType": "IPv4",
                        "iSCSILUN": "0",
                        "iSCSINicSource": null,
                        "iSCSIReverseChapSecret": "",
                        "iSCSIReverseChapUsername": "",
                        "iSCSITargetInfoViaDHCP": true,
                        "iSCSITargetIpAddress": "0.0.0.0",
                        "iSCSITargetName": "",
                        "iSCSITargetTcpPort": 3260
                    },
                    {
                        "StructuredBootString": null,
                        "UEFIDevicePath": null,
                        "iSCSIAttemptInstance": 0,
                        "iSCSIAttemptName": "",
                        "iSCSIAuthenticationMethod": "None",
                        "iSCSIChapSecret": "",
                        "iSCSIChapType": "OneWay",
                        "iSCSIChapUsername": "",
                        "iSCSIConnectRetry": 3,
                        "iSCSIConnectTimeoutMS": 20000,
                        "iSCSIConnection": "Disabled",
                        "iSCSIInitiatorGateway": "0.0.0.0",
                        "iSCSIInitiatorInfoViaDHCP": true,
                        "iSCSIInitiatorIpAddress": "0.0.0.0",
                        "iSCSIInitiatorNetmask": "0.0.0.0",
                        "iSCSIIpAddressType": "IPv4",
                        "iSCSILUN": "0",
                        "iSCSINicSource": null,
                        "iSCSIReverseChapSecret": "",
                        "iSCSIReverseChapUsername": "",
                        "iSCSITargetInfoViaDHCP": true,
                        "iSCSITargetIpAddress": "0.0.0.0",
                        "iSCSITargetName": "",
                        "iSCSITargetTcpPort": 3260
                    },
                    {
                        "StructuredBootString": null,
                        "UEFIDevicePath": null,
                        "iSCSIAttemptInstance": 0,
                        "iSCSIAttemptName": "",
                        "iSCSIAuthenticationMethod": "None",
                        "iSCSIChapSecret": "",
                        "iSCSIChapType": "OneWay",
                        "iSCSIChapUsername": "",
                        "iSCSIConnectRetry": 3,
                        "iSCSIConnectTimeoutMS": 20000,
                        "iSCSIConnection": "Disabled",
                        "iSCSIInitiatorGateway": "0.0.0.0",
                        "iSCSIInitiatorInfoViaDHCP": true,
                        "iSCSIInitiatorIpAddress": "0.0.0.0",
                        "iSCSIInitiatorNetmask": "0.0.0.0",
                        "iSCSIIpAddressType": "IPv4",
                        "iSCSILUN": "0",
                        "iSCSINicSource": null,
                        "iSCSIReverseChapSecret": "",
                        "iSCSIReverseChapUsername": "",
                        "iSCSITargetInfoViaDHCP": true,
                        "iSCSITargetIpAddress": "0.0.0.0",
                        "iSCSITargetName": "",
                        "iSCSITargetTcpPort": 3260
                    }
                ]
            }
        }
    ],
    "Capabilities": {
        "BaseConfig": true,
        "BaseConfigs": false
    },
    "Id": "baseconfigs",
    "Name": "iSCSI Software Initiator Default Settings"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/iscsi/baseconfigs/

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBaseConfigs.HpeBaseConfigs",
    "@odata.etag": "W/\"2ECCA727C95F54545432B6277594742E\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/baseconfigs/",
    "@odata.type": "#HpeBaseConfigs.v2_0_0.HpeBaseConfigs",
    "BaseConfigs": [
        {
            "default": {
                "iSCSIInitiatorName": "iqn.2015-02.com.hpe:uefi-U46-VYRBX9UJ4S",
                "iSCSISources": [
                    {
                        "StructuredBootString": null,
                        "UEFIDevicePath": null,
                        "iSCSIAttemptInstance": 0,
                        "iSCSIAttemptName": "",
                        "iSCSIAuthenticationMethod": "None",
                        "iSCSIChapSecret": "",
                        "iSCSIChapType": "OneWay",
                        "iSCSIChapUsername": "",
                        "iSCSIConnectRetry": 3,
                        "iSCSIConnectTimeoutMS": 20000,
                        "iSCSIConnection": "Disabled",
                        "iSCSIInitiatorGateway": "0.0.0.0",
                        "iSCSIInitiatorInfoViaDHCP": true,
                        "iSCSIInitiatorIpAddress": "0.0.0.0",
                        "iSCSIInitiatorNetmask": "0.0.0.0",
                        "iSCSIIpAddressType": "IPv4",
                        "iSCSILUN": "0",
                        "iSCSINicSource": null,
                        "iSCSIReverseChapSecret": "",
                        "iSCSIReverseChapUsername": "",
                        "iSCSITargetInfoViaDHCP": true,
                        "iSCSITargetIpAddress": "0.0.0.0",
                        "iSCSITargetName": "",
                        "iSCSITargetTcpPort": 3260
                    },
                    {
                        "StructuredBootString": null,
                        "UEFIDevicePath": null,
                        "iSCSIAttemptInstance": 0,
                        "iSCSIAttemptName": "",
                        "iSCSIAuthenticationMethod": "None",
                        "iSCSIChapSecret": "",
                        "iSCSIChapType": "OneWay",
                        "iSCSIChapUsername": "",
                        "iSCSIConnectRetry": 3,
                        "iSCSIConnectTimeoutMS": 20000,
                        "iSCSIConnection": "Disabled",
                        "iSCSIInitiatorGateway": "0.0.0.0",
                        "iSCSIInitiatorInfoViaDHCP": true,
                        "iSCSIInitiatorIpAddress": "0.0.0.0",
                        "iSCSIInitiatorNetmask": "0.0.0.0",
                        "iSCSIIpAddressType": "IPv4",
                        "iSCSILUN": "0",
                        "iSCSINicSource": null,
                        "iSCSIReverseChapSecret": "",
                        "iSCSIReverseChapUsername": "",
                        "iSCSITargetInfoViaDHCP": true,
                        "iSCSITargetIpAddress": "0.0.0.0",
                        "iSCSITargetName": "",
                        "iSCSITargetTcpPort": 3260
                    },
                    {
                        "StructuredBootString": null,
                        "UEFIDevicePath": null,
                        "iSCSIAttemptInstance": 0,
                        "iSCSIAttemptName": "",
                        "iSCSIAuthenticationMethod": "None",
                        "iSCSIChapSecret": "",
                        "iSCSIChapType": "OneWay",
                        "iSCSIChapUsername": "",
                        "iSCSIConnectRetry": 3,
                        "iSCSIConnectTimeoutMS": 20000,
                        "iSCSIConnection": "Disabled",
                        "iSCSIInitiatorGateway": "0.0.0.0",
                        "iSCSIInitiatorInfoViaDHCP": true,
                        "iSCSIInitiatorIpAddress": "0.0.0.0",
                        "iSCSIInitiatorNetmask": "0.0.0.0",
                        "iSCSIIpAddressType": "IPv4",
                        "iSCSILUN": "0",
                        "iSCSINicSource": null,
                        "iSCSIReverseChapSecret": "",
                        "iSCSIReverseChapUsername": "",
                        "iSCSITargetInfoViaDHCP": true,
                        "iSCSITargetIpAddress": "0.0.0.0",
                        "iSCSITargetName": "",
                        "iSCSITargetTcpPort": 3260
                    },
                    {
                        "StructuredBootString": null,
                        "UEFIDevicePath": null,
                        "iSCSIAttemptInstance": 0,
                        "iSCSIAttemptName": "",
                        "iSCSIAuthenticationMethod": "None",
                        "iSCSIChapSecret": "",
                        "iSCSIChapType": "OneWay",
                        "iSCSIChapUsername": "",
                        "iSCSIConnectRetry": 3,
                        "iSCSIConnectTimeoutMS": 20000,
                        "iSCSIConnection": "Disabled",
                        "iSCSIInitiatorGateway": "0.0.0.0",
                        "iSCSIInitiatorInfoViaDHCP": true,
                        "iSCSIInitiatorIpAddress": "0.0.0.0",
                        "iSCSIInitiatorNetmask": "0.0.0.0",
                        "iSCSIIpAddressType": "IPv4",
                        "iSCSILUN": "0",
                        "iSCSINicSource": null,
                        "iSCSIReverseChapSecret": "",
                        "iSCSIReverseChapUsername": "",
                        "iSCSITargetInfoViaDHCP": true,
                        "iSCSITargetIpAddress": "0.0.0.0",
                        "iSCSITargetName": "",
                        "iSCSITargetTcpPort": 3260
                    }
                ]
            }
        }
    ],
    "Capabilities": {
        "BaseConfig": true,
        "BaseConfigs": false
    },
    "Id": "baseconfigs",
    "Name": "iSCSI Software Initiator Default Settings"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/iscsi/settings

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiSCSISoftwareInitiator.HpeiSCSISoftwareInitiator",
    "@odata.etag": "W/\"CB481BE787534A4A4A1EC439DA313400\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/settings/",
    "@odata.type": "#HpeiSCSISoftwareInitiator.v2_0_0.HpeiSCSISoftwareInitiator",
    "Id": "settings",
    "Name": "iSCSI Software Initiator Pending Settings",
    "iSCSIInitiatorName": "iqn.2015-02.com.hpe:uefi-U46",
    "iSCSINicSources": [
        "Slot10NicBoot1",
        "Slot10NicBoot2",
        "Slot10NicBoot3",
        "Slot10NicBoot4"
    ],
    "iSCSISources": [
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        },
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        },
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        },
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        }
    ]
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/iscsi/settings/

```{
    "@odata.context": "/redfish/v1/$metadata#HpeiSCSISoftwareInitiator.HpeiSCSISoftwareInitiator",
    "@odata.etag": "W/\"CB481BE787534A4A4A1EC439DA313400\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/iscsi/settings/",
    "@odata.type": "#HpeiSCSISoftwareInitiator.v2_0_0.HpeiSCSISoftwareInitiator",
    "Id": "settings",
    "Name": "iSCSI Software Initiator Pending Settings",
    "iSCSIInitiatorName": "iqn.2015-02.com.hpe:uefi-U46",
    "iSCSINicSources": [
        "Slot10NicBoot1",
        "Slot10NicBoot2",
        "Slot10NicBoot3",
        "Slot10NicBoot4"
    ],
    "iSCSISources": [
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        },
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        },
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        },
        {
            "StructuredBootString": null,
            "UEFIDevicePath": null,
            "iSCSIAttemptInstance": 0,
            "iSCSIAttemptName": "",
            "iSCSIAuthenticationMethod": "None",
            "iSCSIChapSecret": "",
            "iSCSIChapType": "OneWay",
            "iSCSIChapUsername": "",
            "iSCSIConnectRetry": 3,
            "iSCSIConnectTimeoutMS": 20000,
            "iSCSIConnection": "Disabled",
            "iSCSIInitiatorGateway": "0.0.0.0",
            "iSCSIInitiatorInfoViaDHCP": true,
            "iSCSIInitiatorIpAddress": "0.0.0.0",
            "iSCSIInitiatorNetmask": "0.0.0.0",
            "iSCSIIpAddressType": "IPv4",
            "iSCSILUN": "0",
            "iSCSINicSource": null,
            "iSCSIReverseChapSecret": "",
            "iSCSIReverseChapUsername": "",
            "iSCSITargetInfoViaDHCP": true,
            "iSCSITargetIpAddress": "0.0.0.0",
            "iSCSITargetName": "",
            "iSCSITargetTcpPort": 3260
        }
    ]
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/kmsconfig

```{
    "@Redfish.Settings": {
        "@odata.type": "#Settings.v1_0_0.Settings",
        "ETag": "",
        "Messages": [
            {
                "MessageId": "Base.1.0.Success"
            }
        ],
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/settings/"
        },
        "Time": null
    },
    "@odata.context": "/redfish/v1/$metadata#HpeKmsConfig.HpeKmsConfig",
    "@odata.etag": "W/\"8B61C715BD8FCDCDCDBA7522391F27EC\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/",
    "@odata.type": "#HpeKmsConfig.v1_0_0.HpeKmsConfig",
    "DeleteUnusedEncryptionKeys": "Disabled",
    "EncryptableDevices": [],
    "Id": "kmsconfig",
    "KeyManagementType": "Disabled",
    "Name": "KMS Current Settings",
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"A6A5128F2F03080808E00797569D11A6\""
            }
        }
    },
    "OpalBlockSid": "Disabled"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/

```{
    "@Redfish.Settings": {
        "@odata.type": "#Settings.v1_0_0.Settings",
        "ETag": "",
        "Messages": [
            {
                "MessageId": "Base.1.0.Success"
            }
        ],
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/settings/"
        },
        "Time": null
    },
    "@odata.context": "/redfish/v1/$metadata#HpeKmsConfig.HpeKmsConfig",
    "@odata.etag": "W/\"8B61C715BD8FCDCDCDBA7522391F27EC\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/",
    "@odata.type": "#HpeKmsConfig.v1_0_0.HpeKmsConfig",
    "DeleteUnusedEncryptionKeys": "Disabled",
    "EncryptableDevices": [],
    "Id": "kmsconfig",
    "KeyManagementType": "Disabled",
    "Name": "KMS Current Settings",
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"A6A5128F2F03080808E00797569D11A6\""
            }
        }
    },
    "OpalBlockSid": "Disabled"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/baseconfigs

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBaseConfigs.HpeBaseConfigs",
    "@odata.etag": "W/\"3D9EDCC9EED28585854CD2B23D5923FC\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/baseconfigs/",
    "@odata.type": "#HpeBaseConfigs.v2_0_0.HpeBaseConfigs",
    "BaseConfigs": [
        {
            "default": {
                "DeleteUnusedEncryptionKeys": "Disabled",
                "EncryptableDevices": [],
                "KeyManagementType": "Disabled",
                "OpalBlockSid": "Disabled"
            }
        }
    ],
    "Capabilities": {
        "BaseConfig": true,
        "BaseConfigs": false
    },
    "Id": "baseconfigs",
    "Name": "Kms Default Settings"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/baseconfigs/

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBaseConfigs.HpeBaseConfigs",
    "@odata.etag": "W/\"3D9EDCC9EED28585854CD2B23D5923FC\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/baseconfigs/",
    "@odata.type": "#HpeBaseConfigs.v2_0_0.HpeBaseConfigs",
    "BaseConfigs": [
        {
            "default": {
                "DeleteUnusedEncryptionKeys": "Disabled",
                "EncryptableDevices": [],
                "KeyManagementType": "Disabled",
                "OpalBlockSid": "Disabled"
            }
        }
    ],
    "Capabilities": {
        "BaseConfig": true,
        "BaseConfigs": false
    },
    "Id": "baseconfigs",
    "Name": "Kms Default Settings"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/settings

```{
    "@odata.context": "/redfish/v1/$metadata#HpeKmsConfig.HpeKmsConfig",
    "@odata.etag": "W/\"A6A5128F2F03080808E00797569D11A6\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/settings/",
    "@odata.type": "#HpeKmsConfig.v1_0_0.HpeKmsConfig",
    "DeleteUnusedEncryptionKeys": "Disabled",
    "EncryptableDevices": [],
    "Id": "settings",
    "KeyManagementType": "Disabled",
    "Name": "KMS Pending Settings",
    "OpalBlockSid": "Disabled"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/settings/

```{
    "@odata.context": "/redfish/v1/$metadata#HpeKmsConfig.HpeKmsConfig",
    "@odata.etag": "W/\"A6A5128F2F03080808E00797569D11A6\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/kmsconfig/settings/",
    "@odata.type": "#HpeKmsConfig.v1_0_0.HpeKmsConfig",
    "DeleteUnusedEncryptionKeys": "Disabled",
    "EncryptableDevices": [],
    "Id": "settings",
    "KeyManagementType": "Disabled",
    "Name": "KMS Pending Settings",
    "OpalBlockSid": "Disabled"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/mappings

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBiosMapping.HpeBiosMapping",
    "@odata.etag": "W/\"A5189465C76EB6B6B61958020311B25F\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/mappings/",
    "@odata.type": "#HpeBiosMapping.v2_0_0.HpeBiosMapping",
    "BiosPciSettingsMappings": [
        {
            "Associations": [
                "EmbSata1PCIeOptionROM"
            ],
            "CorrelatableID": "PciRoot(0x0)/Pci(0x17,0x0)",
            "Instance": 1,
            "Subinstances": []
        },
        {
            "Associations": [
                "EmbSata2PCIeOptionROM"
            ],
            "CorrelatableID": "PciRoot(0x0)/Pci(0x11,0x5)",
            "Instance": 2,
            "Subinstances": []
        },
        {
            "Associations": [
                "PciSlot1Enable",
                "PciSlot1LinkSpeed",
                "PciSlot1Aspm",
                "PciSlot1OptionROM",
                "Ocp1AuxiliaryPower"
            ],
            "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "Instance": 3,
            "Subinstances": [
                {
                    "Associations": [
                        "Slot1StorageBoot"
                    ],
                    "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
                    "Subinstance": 1
                }
            ]
        },
        {
            "Associations": [
                "PciSlot2LinkSpeed",
                "PciSlot2OptionROM",
                "Ocp1AuxiliaryPower"
            ],
            "CorrelatableID": "PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "Instance": 4,
            "Subinstances": []
        },
        {
            "Associations": [
                "PciSlot10Enable",
                "PciSlot10LinkSpeed",
                "PciSlot10Aspm",
                "PciSlot10OptionROM",
                "Ocp1AuxiliaryPower"
            ],
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "Instance": 5,
            "Subinstances": [
                {
                    "Associations": [
                        {
                            "PreBootNetwork": "Slot10NicPort1"
                        },
                        "Slot10NicBoot1"
                    ],
                    "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
                    "Subinstance": 1
                },
                {
                    "Associations": [
                        "Slot10NicBoot2"
                    ],
                    "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x1)",
                    "Subinstance": 2
                },
                {
                    "Associations": [
                        "Slot10NicBoot3"
                    ],
                    "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x2)",
                    "Subinstance": 3
                },
                {
                    "Associations": [
                        "Slot10NicBoot4"
                    ],
                    "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x3)",
                    "Subinstance": 4
                }
            ]
        }
    ],
    "Id": "mappings",
    "Name": "BIOS mappings"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/mappings/

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBiosMapping.HpeBiosMapping",
    "@odata.etag": "W/\"A5189465C76EB6B6B61958020311B25F\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/mappings/",
    "@odata.type": "#HpeBiosMapping.v2_0_0.HpeBiosMapping",
    "BiosPciSettingsMappings": [
        {
            "Associations": [
                "EmbSata1PCIeOptionROM"
            ],
            "CorrelatableID": "PciRoot(0x0)/Pci(0x17,0x0)",
            "Instance": 1,
            "Subinstances": []
        },
        {
            "Associations": [
                "EmbSata2PCIeOptionROM"
            ],
            "CorrelatableID": "PciRoot(0x0)/Pci(0x11,0x5)",
            "Instance": 2,
            "Subinstances": []
        },
        {
            "Associations": [
                "PciSlot1Enable",
                "PciSlot1LinkSpeed",
                "PciSlot1Aspm",
                "PciSlot1OptionROM",
                "Ocp1AuxiliaryPower"
            ],
            "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "Instance": 3,
            "Subinstances": [
                {
                    "Associations": [
                        "Slot1StorageBoot"
                    ],
                    "CorrelatableID": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
                    "Subinstance": 1
                }
            ]
        },
        {
            "Associations": [
                "PciSlot2LinkSpeed",
                "PciSlot2OptionROM",
                "Ocp1AuxiliaryPower"
            ],
            "CorrelatableID": "PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "Instance": 4,
            "Subinstances": []
        },
        {
            "Associations": [
                "PciSlot10Enable",
                "PciSlot10LinkSpeed",
                "PciSlot10Aspm",
                "PciSlot10OptionROM",
                "Ocp1AuxiliaryPower"
            ],
            "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "Instance": 5,
            "Subinstances": [
                {
                    "Associations": [
                        {
                            "PreBootNetwork": "Slot10NicPort1"
                        },
                        "Slot10NicBoot1"
                    ],
                    "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
                    "Subinstance": 1
                },
                {
                    "Associations": [
                        "Slot10NicBoot2"
                    ],
                    "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x1)",
                    "Subinstance": 2
                },
                {
                    "Associations": [
                        "Slot10NicBoot3"
                    ],
                    "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x2)",
                    "Subinstance": 3
                },
                {
                    "Associations": [
                        "Slot10NicBoot4"
                    ],
                    "CorrelatableID": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x3)",
                    "Subinstance": 4
                }
            ]
        }
    ],
    "Id": "mappings",
    "Name": "BIOS mappings"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock

```{
    "@Redfish.Settings": {
        "@odata.type": "#Settings.v1_0_0.Settings",
        "ETag": "",
        "Messages": [
            {
                "MessageId": "Base.1.0.Success"
            }
        ],
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/settings/"
        },
        "Time": null
    },
    "@odata.context": "/redfish/v1/$metadata#HpeServerConfigLock.HpeServerConfigLock",
    "@odata.etag": "W/\"4CFAA64819CC555555F5D3236EF7D6C9\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/",
    "@odata.type": "#HpeServerConfigLock.v1_0_0.HpeServerConfigLock",
    "Id": "serverconfiglock",
    "Name": "Server Configuration Lock Current Settings",
    "NewServerConfigLockPassword": null,
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"38D6FCD3F5C05F5F5FA4075B84BC26B2\""
            }
        }
    },
    "ServerConfigLockChallenge": null,
    "ServerConfigLockDisable": null,
    "ServerConfigLockExcludeCpus": null,
    "ServerConfigLockExcludeDimms": null,
    "ServerConfigLockExcludeFwRevs": null,
    "ServerConfigLockExcludePciSlots": null,
    "ServerConfigLockExcludeSecurity": null,
    "ServerConfigLockLogStored": "False",
    "ServerConfigLockPassword": null,
    "ServerConfigLockState": "Disabled",
    "ServerConfigLockTamperHalt": null,
    "ServerConfigLockTransport": null
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/

```{
    "@Redfish.Settings": {
        "@odata.type": "#Settings.v1_0_0.Settings",
        "ETag": "",
        "Messages": [
            {
                "MessageId": "Base.1.0.Success"
            }
        ],
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/settings/"
        },
        "Time": null
    },
    "@odata.context": "/redfish/v1/$metadata#HpeServerConfigLock.HpeServerConfigLock",
    "@odata.etag": "W/\"4CFAA64819CC555555F5D3236EF7D6C9\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/",
    "@odata.type": "#HpeServerConfigLock.v1_0_0.HpeServerConfigLock",
    "Id": "serverconfiglock",
    "Name": "Server Configuration Lock Current Settings",
    "NewServerConfigLockPassword": null,
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"38D6FCD3F5C05F5F5FA4075B84BC26B2\""
            }
        }
    },
    "ServerConfigLockChallenge": null,
    "ServerConfigLockDisable": null,
    "ServerConfigLockExcludeCpus": null,
    "ServerConfigLockExcludeDimms": null,
    "ServerConfigLockExcludeFwRevs": null,
    "ServerConfigLockExcludePciSlots": null,
    "ServerConfigLockExcludeSecurity": null,
    "ServerConfigLockLogStored": "False",
    "ServerConfigLockPassword": null,
    "ServerConfigLockState": "Disabled",
    "ServerConfigLockTamperHalt": null,
    "ServerConfigLockTransport": null
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/baseconfigs

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBaseConfigs.HpeBaseConfigs",
    "@odata.etag": "W/\"AD0329B07DEB626262438CC303587AB9\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/baseconfigs/",
    "@odata.type": "#HpeBaseConfigs.v2_0_0.HpeBaseConfigs",
    "BaseConfigs": [
        {
            "default": {
                "NewServerConfigLockPassword": null,
                "ServerConfigLockChallenge": null,
                "ServerConfigLockDisable": null,
                "ServerConfigLockExcludeCpus": null,
                "ServerConfigLockExcludeDimms": null,
                "ServerConfigLockExcludeFwRevs": null,
                "ServerConfigLockExcludePciSlots": null,
                "ServerConfigLockExcludeSecurity": null,
                "ServerConfigLockLogStored": "False",
                "ServerConfigLockPassword": null,
                "ServerConfigLockState": "Disabled",
                "ServerConfigLockTamperHalt": null,
                "ServerConfigLockTransport": null
            }
        }
    ],
    "Capabilities": {
        "BaseConfig": true,
        "BaseConfigs": false
    },
    "Id": "baseconfigs",
    "Name": "Server Configuration Lock Default Settings"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/baseconfigs/

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBaseConfigs.HpeBaseConfigs",
    "@odata.etag": "W/\"AD0329B07DEB626262438CC303587AB9\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/baseconfigs/",
    "@odata.type": "#HpeBaseConfigs.v2_0_0.HpeBaseConfigs",
    "BaseConfigs": [
        {
            "default": {
                "NewServerConfigLockPassword": null,
                "ServerConfigLockChallenge": null,
                "ServerConfigLockDisable": null,
                "ServerConfigLockExcludeCpus": null,
                "ServerConfigLockExcludeDimms": null,
                "ServerConfigLockExcludeFwRevs": null,
                "ServerConfigLockExcludePciSlots": null,
                "ServerConfigLockExcludeSecurity": null,
                "ServerConfigLockLogStored": "False",
                "ServerConfigLockPassword": null,
                "ServerConfigLockState": "Disabled",
                "ServerConfigLockTamperHalt": null,
                "ServerConfigLockTransport": null
            }
        }
    ],
    "Capabilities": {
        "BaseConfig": true,
        "BaseConfigs": false
    },
    "Id": "baseconfigs",
    "Name": "Server Configuration Lock Default Settings"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/settings

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerConfigLock.HpeServerConfigLock",
    "@odata.etag": "W/\"38D6FCD3F5C05F5F5FA4075B84BC26B2\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/settings/",
    "@odata.type": "#HpeServerConfigLock.v1_0_0.HpeServerConfigLock",
    "Id": "settings",
    "Name": "Server Configuration Lock Pending Settings",
    "NewServerConfigLockPassword": null,
    "ServerConfigLockChallenge": null,
    "ServerConfigLockDisable": null,
    "ServerConfigLockExcludeCpus": null,
    "ServerConfigLockExcludeDimms": null,
    "ServerConfigLockExcludeFwRevs": null,
    "ServerConfigLockExcludePciSlots": null,
    "ServerConfigLockExcludeSecurity": null,
    "ServerConfigLockLogStored": "False",
    "ServerConfigLockPassword": null,
    "ServerConfigLockState": "Disabled",
    "ServerConfigLockTamperHalt": null,
    "ServerConfigLockTransport": null
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/settings/

```{
    "@odata.context": "/redfish/v1/$metadata#HpeServerConfigLock.HpeServerConfigLock",
    "@odata.etag": "W/\"38D6FCD3F5C05F5F5FA4075B84BC26B2\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/serverconfiglock/settings/",
    "@odata.type": "#HpeServerConfigLock.v1_0_0.HpeServerConfigLock",
    "Id": "settings",
    "Name": "Server Configuration Lock Pending Settings",
    "NewServerConfigLockPassword": null,
    "ServerConfigLockChallenge": null,
    "ServerConfigLockDisable": null,
    "ServerConfigLockExcludeCpus": null,
    "ServerConfigLockExcludeDimms": null,
    "ServerConfigLockExcludeFwRevs": null,
    "ServerConfigLockExcludePciSlots": null,
    "ServerConfigLockExcludeSecurity": null,
    "ServerConfigLockLogStored": "False",
    "ServerConfigLockPassword": null,
    "ServerConfigLockState": "Disabled",
    "ServerConfigLockTamperHalt": null,
    "ServerConfigLockTransport": null
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/tlsconfig

```{
    "@Redfish.Settings": {
        "@odata.type": "#Settings.v1_0_0.Settings",
        "ETag": "",
        "Messages": [
            {
                "MessageId": "Base.1.0.Success"
            }
        ],
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/settings/"
        },
        "Time": null
    },
    "@odata.context": "/redfish/v1/$metadata#HpeTlsConfig.HpeTlsConfig",
    "@odata.etag": "W/\"F48323138E3DC7C7C7F9ECC67D18ECFC\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/",
    "@odata.type": "#HpeTlsConfig.v1_0_0.HpeTlsConfig",
    "Certificates": [],
    "Ciphers": "AES128-SHA256:AES256-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-ARIA128-GCM-SHA256:DHE-RSA-ARIA256-GCM-SHA384:DHE-RSA-AES128-CCM8:DHE-RSA-AES256-CCM8",
    "DeleteCertificates": [],
    "HostnameCheck": "Disabled",
    "Id": "tlsconfig",
    "Name": "TLS Current Settings",
    "NewCertificates": [],
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"232BE31B46AC494949B10E80334FBD02\""
            }
        }
    },
    "ProtocolVersion": "AUTO",
    "TlsCaCertificateCount": 0,
    "VerifyMode": "PEER"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/

```{
    "@Redfish.Settings": {
        "@odata.type": "#Settings.v1_0_0.Settings",
        "ETag": "",
        "Messages": [
            {
                "MessageId": "Base.1.0.Success"
            }
        ],
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/settings/"
        },
        "Time": null
    },
    "@odata.context": "/redfish/v1/$metadata#HpeTlsConfig.HpeTlsConfig",
    "@odata.etag": "W/\"F48323138E3DC7C7C7F9ECC67D18ECFC\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/",
    "@odata.type": "#HpeTlsConfig.v1_0_0.HpeTlsConfig",
    "Certificates": [],
    "Ciphers": "AES128-SHA256:AES256-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-ARIA128-GCM-SHA256:DHE-RSA-ARIA256-GCM-SHA384:DHE-RSA-AES128-CCM8:DHE-RSA-AES256-CCM8",
    "DeleteCertificates": [],
    "HostnameCheck": "Disabled",
    "Id": "tlsconfig",
    "Name": "TLS Current Settings",
    "NewCertificates": [],
    "Oem": {
        "Hpe": {
            "@odata.type": "#HpeBiosExt.v2_0_0.HpeBiosExt",
            "Links": {
                "BaseConfigs": {
                    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/baseconfigs/"
                }
            },
            "SettingsObject": {
                "UnmodifiedETag": "W/\"232BE31B46AC494949B10E80334FBD02\""
            }
        }
    },
    "ProtocolVersion": "AUTO",
    "TlsCaCertificateCount": 0,
    "VerifyMode": "PEER"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/baseconfigs

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBaseConfigs.HpeBaseConfigs",
    "@odata.etag": "W/\"15A6A9871F0B7777770A9160820BB027\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/baseconfigs/",
    "@odata.type": "#HpeBaseConfigs.v2_0_0.HpeBaseConfigs",
    "BaseConfigs": [
        {
            "default": {
                "Certificates": [],
                "Ciphers": "AES256-SHA:AES256-SHA256:AES256-GCM-SHA384:AES128-SHA:AES128-SHA256:AES128-GCM-SHA256",
                "DeleteCertificates": [],
                "HostnameCheck": "Disabled",
                "NewCertificates": [],
                "ProtocolVersion": "AUTO",
                "TlsCaCertificateCount": 0,
                "VerifyMode": "PEER"
            }
        }
    ],
    "Capabilities": {
        "BaseConfig": true,
        "BaseConfigs": false
    },
    "Id": "baseconfigs",
    "Name": "TLS Default Settings"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/baseconfigs/

```{
    "@odata.context": "/redfish/v1/$metadata#HpeBaseConfigs.HpeBaseConfigs",
    "@odata.etag": "W/\"15A6A9871F0B7777770A9160820BB027\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/baseconfigs/",
    "@odata.type": "#HpeBaseConfigs.v2_0_0.HpeBaseConfigs",
    "BaseConfigs": [
        {
            "default": {
                "Certificates": [],
                "Ciphers": "AES256-SHA:AES256-SHA256:AES256-GCM-SHA384:AES128-SHA:AES128-SHA256:AES128-GCM-SHA256",
                "DeleteCertificates": [],
                "HostnameCheck": "Disabled",
                "NewCertificates": [],
                "ProtocolVersion": "AUTO",
                "TlsCaCertificateCount": 0,
                "VerifyMode": "PEER"
            }
        }
    ],
    "Capabilities": {
        "BaseConfig": true,
        "BaseConfigs": false
    },
    "Id": "baseconfigs",
    "Name": "TLS Default Settings"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/settings

```{
    "@odata.context": "/redfish/v1/$metadata#HpeTlsConfig.HpeTlsConfig",
    "@odata.etag": "W/\"232BE31B46AC494949B10E80334FBD02\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/settings/",
    "@odata.type": "#HpeTlsConfig.v1_0_0.HpeTlsConfig",
    "Certificates": [],
    "Ciphers": "AES128-SHA256:AES256-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-ARIA128-GCM-SHA256:DHE-RSA-ARIA256-GCM-SHA384:DHE-RSA-AES128-CCM8:DHE-RSA-AES256-CCM8",
    "DeleteCertificates": [],
    "HostnameCheck": "Disabled",
    "Id": "settings",
    "Name": "TLS Pending Settings",
    "NewCertificates": [],
    "ProtocolVersion": "AUTO",
    "TlsCaCertificateCount": 0,
    "VerifyMode": "PEER"
}
```

## /redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/settings/

```{
    "@odata.context": "/redfish/v1/$metadata#HpeTlsConfig.HpeTlsConfig",
    "@odata.etag": "W/\"232BE31B46AC494949B10E80334FBD02\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/oem/hpe/tlsconfig/settings/",
    "@odata.type": "#HpeTlsConfig.v1_0_0.HpeTlsConfig",
    "Certificates": [],
    "Ciphers": "AES128-SHA256:AES256-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-ARIA128-GCM-SHA256:DHE-RSA-ARIA256-GCM-SHA384:DHE-RSA-AES128-CCM8:DHE-RSA-AES256-CCM8",
    "DeleteCertificates": [],
    "HostnameCheck": "Disabled",
    "Id": "settings",
    "Name": "TLS Pending Settings",
    "NewCertificates": [],
    "ProtocolVersion": "AUTO",
    "TlsCaCertificateCount": 0,
    "VerifyMode": "PEER"
}
```

## /redfish/v1/Systems/1/bios/settings

```{
    "@odata.context": "/redfish/v1/$metadata#Bios.Bios",
    "@odata.etag": "W/\"1D9FCF6419ED0C0C0C42B979DC024DFF\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/settings/",
    "@odata.type": "#Bios.v1_0_4.Bios",
    "AttributeRegistry": "BiosAttributeRegistryU46.v1_1_56",
    "Attributes": {
        "AccessControlService": "Enabled",
        "AcpiHpet": "Enabled",
        "AcpiRootBridgePxm": "Enabled",
        "AcpiSlit": "Enabled",
        "AdjSecPrefetch": "Enabled",
        "AdminEmail": "",
        "AdminName": "",
        "AdminOtherInfo": "",
        "AdminPhone": "",
        "AdvCrashDumpMode": "Disabled",
        "AdvancedMemProtection": "Auto",
        "AllowLoginWithIlo": "Disabled",
        "AssetTagProtection": "Unlocked",
        "AutoPowerOn": "RestoreLastState",
        "BootMode": "Uefi",
        "BootOrderPolicy": "RetryIndefinitely",
        "CollabPowerControl": "Enabled",
        "ConsistentDevNaming": "LomsAndSlots",
        "CustomPostMessage": "",
        "DaylightSavingsTime": "DaylightSavingsTimeDisabled",
        "DcuIpPrefetcher": "Enabled",
        "DcuStreamPrefetcher": "Enabled",
        "DeadBlockPredictor": "Disabled",
        "Dhcpv4": "Enabled",
        "DirectToUpi": "Auto",
        "DramRapl": 0,
        "DramRaplLimit": "Disabled",
        "DramRaplReport": "Enabled",
        "DynamicPowerCapping": "Disabled",
        "EmbVideoConnection": "Auto",
        "EmbeddedDiagnostics": "Enabled",
        "EmbeddedIpxe": "Enabled",
        "EmbeddedSata": "Ahci",
        "EmbeddedSerialPort": "Com2Irq3",
        "EmbeddedUefiShell": "Enabled",
        "EmsConsole": "Disabled",
        "EnabledCoresPerProc": 0,
        "EnergyEfficientTurbo": "Enabled",
        "EnergyPerfBias": "BalancedPerf",
        "EnhancedProcPerf": "Disabled",
        "EppProfile": "Moderate",
        "EraseUserDefaults": "No",
        "ExtendedAmbientTemp": "Disabled",
        "ExtendedMemTest": "Disabled",
        "F11BootMenu": "Enabled",
        "FCScanPolicy": "CardConfig",
        "FanFailPolicy": "Shutdown",
        "FanInstallReq": "EnableMessaging",
        "HourFormat": "24Hours",
        "HttpSupport": "Auto",
        "HwPrefetcher": "Enabled",
        "IODCConfiguration": "Auto",
        "IntelDmiLinkFreq": "Auto",
        "IntelNicDmaChannels": "Enabled",
        "IntelPerfMonitoring": "Disabled",
        "IntelPriorityBaseFreq": "Disabled",
        "IntelProcVtd": "Enabled",
        "IntelUpiFreq": "Auto",
        "IntelUpiLinkEn": "Auto",
        "IntelUpiPowerManagement": "Enabled",
        "IntelVmdDirectAssign": "VmdDirectAssignEnabledAll",
        "IntelVmdSupport": "Disabled",
        "IntelVrocSupport": "None",
        "IntelligentProvisioning": "Enabled",
        "IpmiWatchdogTimerAction": "PowerCycle",
        "IpmiWatchdogTimerStatus": "IpmiWatchdogTimerOff",
        "IpmiWatchdogTimerTimeout": "Timeout30Min",
        "Ipv4Address": "0.0.0.0",
        "Ipv4Gateway": "0.0.0.0",
        "Ipv4PrimaryDNS": "0.0.0.0",
        "Ipv4SubnetMask": "0.0.0.0",
        "Ipv6Address": "::",
        "Ipv6ConfigPolicy": "Automatic",
        "Ipv6Duid": "Auto",
        "Ipv6Gateway": "::",
        "Ipv6PrimaryDNS": "::",
        "IpxeAutoStartScriptLocation": "Auto",
        "IpxeBootOrder": "Disabled",
        "IpxeScriptAutoStart": "Disabled",
        "IpxeScriptVerification": "Disabled",
        "IpxeStartupUrl": "",
        "LLCDeadLineAllocation": "Enabled",
        "LlcPrefetch": "Disabled",
        "LocalRemoteThreshold": "Auto",
        "MaxMemBusFreqMHz": "Auto",
        "MaxPcieSpeed": "PerPortCtrl",
        "MemClearWarmReset": "Disabled",
        "MemFastTraining": "Enabled",
        "MemMirrorMode": "Full",
        "MemPatrolScrubbing": "Enabled",
        "MemRefreshRate": "Refreshx1",
        "MemoryConfigurationViolationReporting": "Enabled",
        "MemoryRemap": "NoAction",
        "MicrosoftSecuredCoreSupport": "Disabled",
        "MinProcIdlePkgState": "C6NonRetention",
        "MinProcIdlePower": "C6",
        "MixedPowerSupplyReporting": "Enabled",
        "MkTme": "Disabled",
        "NetworkBootRetry": "Enabled",
        "NetworkBootRetryCount": 20,
        "NoExecutionProtection": "Enabled",
        "Numa": "Enabled",
        "NumaGroupSizeOpt": "Flat",
        "NvmeOptionRom": "Enabled",
        "NvmePort1": "Nvme",
        "NvmePort10": "Nvme",
        "NvmePort11": "Nvme",
        "NvmePort12": "Nvme",
        "NvmePort13": "Nvme",
        "NvmePort14": "Nvme",
        "NvmePort15": "Nvme",
        "NvmePort16": "Nvme",
        "NvmePort2": "Nvme",
        "NvmePort3": "Nvme",
        "NvmePort4": "Nvme",
        "NvmePort5": "Nvme",
        "NvmePort6": "Nvme",
        "NvmePort7": "Nvme",
        "NvmePort8": "Nvme",
        "NvmePort9": "Nvme",
        "NvmeRaid": "Disabled",
        "Ocp1AuxiliaryPower": "Enabled",
        "PatrolScrubDuration": 24,
        "PciPeerToPeerSerialization": "Disabled",
        "PciResourcePadding": "Normal",
        "PciSlot10Aspm": "Disabled",
        "PciSlot10Bifurcation": "Auto",
        "PciSlot10Enable": "Auto",
        "PciSlot10LinkSpeed": "Auto",
        "PciSlot10OptionROM": "Enabled",
        "PciSlot13Aspm": "Disabled",
        "PciSlot13Enable": "Auto",
        "PciSlot13LinkSpeed": "Auto",
        "PciSlot13OptionROM": "Enabled",
        "PciSlot1Aspm": "Disabled",
        "PciSlot1Bifurcation": "Auto",
        "PciSlot1Enable": "Auto",
        "PciSlot1LinkSpeed": "Auto",
        "PciSlot1OptionROM": "Enabled",
        "PciSlot2Bifurcation": "Auto",
        "PcieHotPlugErrControl": "HotplugSurprise",
        "PcuPMax": 0,
        "PersistentMemAddressRangeScrub": "Enabled",
        "PersistentMemBackupPowerPolicy": "WaitForBackupPower",
        "PersistentMemNumaAffinity": "IsolatedNumaDomains",
        "PersistentMemScanMem": "Enabled",
        "PlatformCertificate": "Enabled",
        "PlatformRASPolicy": "FirmwareFirst",
        "PostAsr": "PostAsrOff",
        "PostAsrDelay": "Delay30Min",
        "PostBootProgress": "Disabled",
        "PostDiscoveryMode": "Auto",
        "PostF1Prompt": "Delayed20Sec",
        "PostScreenMode": "VerboseMode",
        "PostVideoSupport": "DisplayAll",
        "PowerButton": "Enabled",
        "PowerOnDelay": "NoDelay",
        "PowerRegulator": "DynamicPowerSavings",
        "PreBootNetwork": "Auto",
        "PrebootNetworkEnvPolicy": "Auto",
        "PrebootNetworkProxy": "",
        "ProcAes": "Enabled",
        "ProcHyperthreading": "Enabled",
        "ProcRapl": 0,
        "ProcTurbo": "Enabled",
        "ProcVirtualization": "Enabled",
        "ProcX2Apic": "Enabled",
        "ProcessorConfigTDPLevel": "Normal",
        "ProcessorPhysicalAddress": "Limited",
        "ProductId": "P28948-B21",
        "RedundantPowerSupply": "BalancedMode",
        "RemoteXptPrefetcher": "Auto",
        "RemovableFlashBootSeq": "ExternalKeysFirst",
        "RestoreDefaults": "No",
        "RestoreManufacturingDefaults": "No",
        "RomSelection": "CurrentRom",
        "SataSanitize": "Disabled",
        "SataSecureErase": "Disabled",
        "SaveUserDefaults": "No",
        "SciRasSupport": "Ghesv1Support",
        "SecStartBackupImage": "Disabled",
        "SecureBootStatus": "Disabled",
        "SerialConsoleBaudRate": "BaudRate115200",
        "SerialConsoleEmulation": "Vt100Plus",
        "SerialConsolePort": "Auto",
        "SerialNumber": "VYRBX9UJ4S",
        "SerialPortDtrSupport": "Disabled",
        "ServerAssetTag": "hp-new",
        "ServerConfigLockStatus": "Disabled",
        "ServerName": "VYRBX9UJ4S.cisco.lab",
        "ServerOtherInfo": "",
        "ServerPrimaryOs": "",
        "ServiceEmail": "",
        "ServiceName": "",
        "ServiceOtherInfo": "",
        "ServicePhone": "",
        "SetupBrowserSelection": "Auto",
        "SgxAutoMpRegistrationAgent": "Enabled",
        "SgxEnable": "Disabled",
        "SgxLaunchControlPolicy": "IntelLocked",
        "SgxLePublicKeyHash0": "",
        "SgxLePublicKeyHash1": "",
        "SgxLePublicKeyHash2": "",
        "SgxLePublicKeyHash3": "",
        "SgxLePublicKeyWriteEnable": "Enabled",
        "SgxPrmrrSize": "2Gb",
        "Slot10EoiBroadcastSupport": "Disabled",
        "Slot10MctpBroadcastSupport": "Enabled",
        "Slot10NicBoot1": "NetworkBoot",
        "Slot10NicBoot2": "Disabled",
        "Slot10NicBoot3": "Disabled",
        "Slot10NicBoot4": "Disabled",
        "Slot1EoiBroadcastSupport": "Disabled",
        "Slot1MctpBroadcastSupport": "Enabled",
        "Slot1StorageBoot": "ThirtyTwoTargets",
        "Slot2EoiBroadcastSupport": "Disabled",
        "Slot2MctpBroadcastSupport": "Enabled",
        "SnoopResponseHoldOff": 0,
        "Sriov": "Enabled",
        "StaleAtoS": "Disabled",
        "SubNumaClustering": "Disabled",
        "ThermalConfig": "OptimalCooling",
        "ThermalShutdown": "Enabled",
        "TimeFormat": "Utc",
        "TimeZone": "Utc0",
        "Tme": "Disabled",
        "TmeExclusiveBase": "",
        "TmeExclusiveLen": "",
        "TpmChipId": "None",
        "TpmFips": "NotSpecified",
        "TpmState": "NotPresent",
        "TpmType": "NoTpm",
        "Tsx": "Enabled",
        "UefiOptimizedBoot": "Enabled",
        "UefiSerialDebugLevel": "ErrorsOnly",
        "UefiShellBootOrder": "Disabled",
        "UefiShellPhysicalPresenceKeystroke": "Enabled",
        "UefiShellScriptVerification": "Disabled",
        "UefiShellStartup": "Disabled",
        "UefiShellStartupLocation": "Auto",
        "UefiShellStartupUrl": "",
        "UefiShellStartupUrlFromDhcp": "Disabled",
        "UefiVariableAccessFwControl": "Disabled",
        "UncoreFreqScaling": "Auto",
        "UpiPrefetcher": "Enabled",
        "UrlBootFile": "",
        "UrlBootFile2": "",
        "UrlBootFile3": "",
        "UrlBootFile4": "",
        "UsbBoot": "Enabled",
        "UsbControl": "UsbEnabled",
        "UserDefaultsState": "Disabled",
        "UtilityLang": "English",
        "VirtualNuma": "Disabled",
        "VirtualSerialPort": "Com1Irq4",
        "VlanControl": "Disabled",
        "VlanId": 0,
        "VlanPriority": 0,
        "VmProprietaryPageRetireSupport": "Enabled",
        "VmdonCpu1Stack5Port1": "Disabled",
        "VmdonCpu1Stack5Port2": "Disabled",
        "VmdonCpu1Stack5Port3": "Disabled",
        "VmdonCpu1Stack5Port4": "Disabled",
        "VmdonCpu2Stack5Port1": "Disabled",
        "VmdonCpu2Stack5Port2": "Disabled",
        "VmdonCpu2Stack5Port3": "Disabled",
        "VmdonCpu2Stack5Port4": "Disabled",
        "WakeOnLan": "Enabled",
        "WorkloadProfile": "GeneralPowerEfficientCompute",
        "XptPrefetcher": "Auto",
        "iSCSISoftwareInitiator": "Enabled"
    },
    "Id": "settings",
    "Name": "BIOS Pending Settings"
}
```

## /redfish/v1/Systems/1/bios/settings/

```{
    "@odata.context": "/redfish/v1/$metadata#Bios.Bios",
    "@odata.etag": "W/\"1D9FCF6419ED0C0C0C42B979DC024DFF\"",
    "@odata.id": "/redfish/v1/Systems/1/bios/settings/",
    "@odata.type": "#Bios.v1_0_4.Bios",
    "AttributeRegistry": "BiosAttributeRegistryU46.v1_1_56",
    "Attributes": {
        "AccessControlService": "Enabled",
        "AcpiHpet": "Enabled",
        "AcpiRootBridgePxm": "Enabled",
        "AcpiSlit": "Enabled",
        "AdjSecPrefetch": "Enabled",
        "AdminEmail": "",
        "AdminName": "",
        "AdminOtherInfo": "",
        "AdminPhone": "",
        "AdvCrashDumpMode": "Disabled",
        "AdvancedMemProtection": "Auto",
        "AllowLoginWithIlo": "Disabled",
        "AssetTagProtection": "Unlocked",
        "AutoPowerOn": "RestoreLastState",
        "BootMode": "Uefi",
        "BootOrderPolicy": "RetryIndefinitely",
        "CollabPowerControl": "Enabled",
        "ConsistentDevNaming": "LomsAndSlots",
        "CustomPostMessage": "",
        "DaylightSavingsTime": "DaylightSavingsTimeDisabled",
        "DcuIpPrefetcher": "Enabled",
        "DcuStreamPrefetcher": "Enabled",
        "DeadBlockPredictor": "Disabled",
        "Dhcpv4": "Enabled",
        "DirectToUpi": "Auto",
        "DramRapl": 0,
        "DramRaplLimit": "Disabled",
        "DramRaplReport": "Enabled",
        "DynamicPowerCapping": "Disabled",
        "EmbVideoConnection": "Auto",
        "EmbeddedDiagnostics": "Enabled",
        "EmbeddedIpxe": "Enabled",
        "EmbeddedSata": "Ahci",
        "EmbeddedSerialPort": "Com2Irq3",
        "EmbeddedUefiShell": "Enabled",
        "EmsConsole": "Disabled",
        "EnabledCoresPerProc": 0,
        "EnergyEfficientTurbo": "Enabled",
        "EnergyPerfBias": "BalancedPerf",
        "EnhancedProcPerf": "Disabled",
        "EppProfile": "Moderate",
        "EraseUserDefaults": "No",
        "ExtendedAmbientTemp": "Disabled",
        "ExtendedMemTest": "Disabled",
        "F11BootMenu": "Enabled",
        "FCScanPolicy": "CardConfig",
        "FanFailPolicy": "Shutdown",
        "FanInstallReq": "EnableMessaging",
        "HourFormat": "24Hours",
        "HttpSupport": "Auto",
        "HwPrefetcher": "Enabled",
        "IODCConfiguration": "Auto",
        "IntelDmiLinkFreq": "Auto",
        "IntelNicDmaChannels": "Enabled",
        "IntelPerfMonitoring": "Disabled",
        "IntelPriorityBaseFreq": "Disabled",
        "IntelProcVtd": "Enabled",
        "IntelUpiFreq": "Auto",
        "IntelUpiLinkEn": "Auto",
        "IntelUpiPowerManagement": "Enabled",
        "IntelVmdDirectAssign": "VmdDirectAssignEnabledAll",
        "IntelVmdSupport": "Disabled",
        "IntelVrocSupport": "None",
        "IntelligentProvisioning": "Enabled",
        "IpmiWatchdogTimerAction": "PowerCycle",
        "IpmiWatchdogTimerStatus": "IpmiWatchdogTimerOff",
        "IpmiWatchdogTimerTimeout": "Timeout30Min",
        "Ipv4Address": "0.0.0.0",
        "Ipv4Gateway": "0.0.0.0",
        "Ipv4PrimaryDNS": "0.0.0.0",
        "Ipv4SubnetMask": "0.0.0.0",
        "Ipv6Address": "::",
        "Ipv6ConfigPolicy": "Automatic",
        "Ipv6Duid": "Auto",
        "Ipv6Gateway": "::",
        "Ipv6PrimaryDNS": "::",
        "IpxeAutoStartScriptLocation": "Auto",
        "IpxeBootOrder": "Disabled",
        "IpxeScriptAutoStart": "Disabled",
        "IpxeScriptVerification": "Disabled",
        "IpxeStartupUrl": "",
        "LLCDeadLineAllocation": "Enabled",
        "LlcPrefetch": "Disabled",
        "LocalRemoteThreshold": "Auto",
        "MaxMemBusFreqMHz": "Auto",
        "MaxPcieSpeed": "PerPortCtrl",
        "MemClearWarmReset": "Disabled",
        "MemFastTraining": "Enabled",
        "MemMirrorMode": "Full",
        "MemPatrolScrubbing": "Enabled",
        "MemRefreshRate": "Refreshx1",
        "MemoryConfigurationViolationReporting": "Enabled",
        "MemoryRemap": "NoAction",
        "MicrosoftSecuredCoreSupport": "Disabled",
        "MinProcIdlePkgState": "C6NonRetention",
        "MinProcIdlePower": "C6",
        "MixedPowerSupplyReporting": "Enabled",
        "MkTme": "Disabled",
        "NetworkBootRetry": "Enabled",
        "NetworkBootRetryCount": 20,
        "NoExecutionProtection": "Enabled",
        "Numa": "Enabled",
        "NumaGroupSizeOpt": "Flat",
        "NvmeOptionRom": "Enabled",
        "NvmePort1": "Nvme",
        "NvmePort10": "Nvme",
        "NvmePort11": "Nvme",
        "NvmePort12": "Nvme",
        "NvmePort13": "Nvme",
        "NvmePort14": "Nvme",
        "NvmePort15": "Nvme",
        "NvmePort16": "Nvme",
        "NvmePort2": "Nvme",
        "NvmePort3": "Nvme",
        "NvmePort4": "Nvme",
        "NvmePort5": "Nvme",
        "NvmePort6": "Nvme",
        "NvmePort7": "Nvme",
        "NvmePort8": "Nvme",
        "NvmePort9": "Nvme",
        "NvmeRaid": "Disabled",
        "Ocp1AuxiliaryPower": "Enabled",
        "PatrolScrubDuration": 24,
        "PciPeerToPeerSerialization": "Disabled",
        "PciResourcePadding": "Normal",
        "PciSlot10Aspm": "Disabled",
        "PciSlot10Bifurcation": "Auto",
        "PciSlot10Enable": "Auto",
        "PciSlot10LinkSpeed": "Auto",
        "PciSlot10OptionROM": "Enabled",
        "PciSlot13Aspm": "Disabled",
        "PciSlot13Enable": "Auto",
        "PciSlot13LinkSpeed": "Auto",
        "PciSlot13OptionROM": "Enabled",
        "PciSlot1Aspm": "Disabled",
        "PciSlot1Bifurcation": "Auto",
        "PciSlot1Enable": "Auto",
        "PciSlot1LinkSpeed": "Auto",
        "PciSlot1OptionROM": "Enabled",
        "PciSlot2Bifurcation": "Auto",
        "PcieHotPlugErrControl": "HotplugSurprise",
        "PcuPMax": 0,
        "PersistentMemAddressRangeScrub": "Enabled",
        "PersistentMemBackupPowerPolicy": "WaitForBackupPower",
        "PersistentMemNumaAffinity": "IsolatedNumaDomains",
        "PersistentMemScanMem": "Enabled",
        "PlatformCertificate": "Enabled",
        "PlatformRASPolicy": "FirmwareFirst",
        "PostAsr": "PostAsrOff",
        "PostAsrDelay": "Delay30Min",
        "PostBootProgress": "Disabled",
        "PostDiscoveryMode": "Auto",
        "PostF1Prompt": "Delayed20Sec",
        "PostScreenMode": "VerboseMode",
        "PostVideoSupport": "DisplayAll",
        "PowerButton": "Enabled",
        "PowerOnDelay": "NoDelay",
        "PowerRegulator": "DynamicPowerSavings",
        "PreBootNetwork": "Auto",
        "PrebootNetworkEnvPolicy": "Auto",
        "PrebootNetworkProxy": "",
        "ProcAes": "Enabled",
        "ProcHyperthreading": "Enabled",
        "ProcRapl": 0,
        "ProcTurbo": "Enabled",
        "ProcVirtualization": "Enabled",
        "ProcX2Apic": "Enabled",
        "ProcessorConfigTDPLevel": "Normal",
        "ProcessorPhysicalAddress": "Limited",
        "ProductId": "P28948-B21",
        "RedundantPowerSupply": "BalancedMode",
        "RemoteXptPrefetcher": "Auto",
        "RemovableFlashBootSeq": "ExternalKeysFirst",
        "RestoreDefaults": "No",
        "RestoreManufacturingDefaults": "No",
        "RomSelection": "CurrentRom",
        "SataSanitize": "Disabled",
        "SataSecureErase": "Disabled",
        "SaveUserDefaults": "No",
        "SciRasSupport": "Ghesv1Support",
        "SecStartBackupImage": "Disabled",
        "SecureBootStatus": "Disabled",
        "SerialConsoleBaudRate": "BaudRate115200",
        "SerialConsoleEmulation": "Vt100Plus",
        "SerialConsolePort": "Auto",
        "SerialNumber": "VYRBX9UJ4S",
        "SerialPortDtrSupport": "Disabled",
        "ServerAssetTag": "hp-new",
        "ServerConfigLockStatus": "Disabled",
        "ServerName": "VYRBX9UJ4S.cisco.lab",
        "ServerOtherInfo": "",
        "ServerPrimaryOs": "",
        "ServiceEmail": "",
        "ServiceName": "",
        "ServiceOtherInfo": "",
        "ServicePhone": "",
        "SetupBrowserSelection": "Auto",
        "SgxAutoMpRegistrationAgent": "Enabled",
        "SgxEnable": "Disabled",
        "SgxLaunchControlPolicy": "IntelLocked",
        "SgxLePublicKeyHash0": "",
        "SgxLePublicKeyHash1": "",
        "SgxLePublicKeyHash2": "",
        "SgxLePublicKeyHash3": "",
        "SgxLePublicKeyWriteEnable": "Enabled",
        "SgxPrmrrSize": "2Gb",
        "Slot10EoiBroadcastSupport": "Disabled",
        "Slot10MctpBroadcastSupport": "Enabled",
        "Slot10NicBoot1": "NetworkBoot",
        "Slot10NicBoot2": "Disabled",
        "Slot10NicBoot3": "Disabled",
        "Slot10NicBoot4": "Disabled",
        "Slot1EoiBroadcastSupport": "Disabled",
        "Slot1MctpBroadcastSupport": "Enabled",
        "Slot1StorageBoot": "ThirtyTwoTargets",
        "Slot2EoiBroadcastSupport": "Disabled",
        "Slot2MctpBroadcastSupport": "Enabled",
        "SnoopResponseHoldOff": 0,
        "Sriov": "Enabled",
        "StaleAtoS": "Disabled",
        "SubNumaClustering": "Disabled",
        "ThermalConfig": "OptimalCooling",
        "ThermalShutdown": "Enabled",
        "TimeFormat": "Utc",
        "TimeZone": "Utc0",
        "Tme": "Disabled",
        "TmeExclusiveBase": "",
        "TmeExclusiveLen": "",
        "TpmChipId": "None",
        "TpmFips": "NotSpecified",
        "TpmState": "NotPresent",
        "TpmType": "NoTpm",
        "Tsx": "Enabled",
        "UefiOptimizedBoot": "Enabled",
        "UefiSerialDebugLevel": "ErrorsOnly",
        "UefiShellBootOrder": "Disabled",
        "UefiShellPhysicalPresenceKeystroke": "Enabled",
        "UefiShellScriptVerification": "Disabled",
        "UefiShellStartup": "Disabled",
        "UefiShellStartupLocation": "Auto",
        "UefiShellStartupUrl": "",
        "UefiShellStartupUrlFromDhcp": "Disabled",
        "UefiVariableAccessFwControl": "Disabled",
        "UncoreFreqScaling": "Auto",
        "UpiPrefetcher": "Enabled",
        "UrlBootFile": "",
        "UrlBootFile2": "",
        "UrlBootFile3": "",
        "UrlBootFile4": "",
        "UsbBoot": "Enabled",
        "UsbControl": "UsbEnabled",
        "UserDefaultsState": "Disabled",
        "UtilityLang": "English",
        "VirtualNuma": "Disabled",
        "VirtualSerialPort": "Com1Irq4",
        "VlanControl": "Disabled",
        "VlanId": 0,
        "VlanPriority": 0,
        "VmProprietaryPageRetireSupport": "Enabled",
        "VmdonCpu1Stack5Port1": "Disabled",
        "VmdonCpu1Stack5Port2": "Disabled",
        "VmdonCpu1Stack5Port3": "Disabled",
        "VmdonCpu1Stack5Port4": "Disabled",
        "VmdonCpu2Stack5Port1": "Disabled",
        "VmdonCpu2Stack5Port2": "Disabled",
        "VmdonCpu2Stack5Port3": "Disabled",
        "VmdonCpu2Stack5Port4": "Disabled",
        "WakeOnLan": "Enabled",
        "WorkloadProfile": "GeneralPowerEfficientCompute",
        "XptPrefetcher": "Auto",
        "iSCSISoftwareInitiator": "Enabled"
    },
    "Id": "settings",
    "Name": "BIOS Pending Settings"
}
```

## /redfish/v1/Systems/1/hpsut

```{
    "@odata.context": "/redfish/v1/$metadata#sut.sut/",
    "@odata.id": "/redfish/v1/Systems/1/hpsut/",
    "@odata.type": "#SUT.v2_5_6.SUT",
    "HPSUMPID": 0,
    "IsSelfUpdate": false,
    "LastBootUptime": "none",
    "LastOperationTime": "none",
    "Mode": "AutoDeploy",
    "OperationRequestor": "OS Administrator",
    "PollingIntervalInMinutes": 5,
    "SUTCompName": "",
    "SelfUpdateStatus": "none",
    "ServiceState": "Running",
    "ServiceVersion": "2.5.6.0",
    "StagingDirectory": "/tmp/stagingdirectory",
    "Verify": "autoVerify"
}
```

## /redfish/v1/Systems/1/hpsut/

```{
    "@odata.context": "/redfish/v1/$metadata#sut.sut/",
    "@odata.id": "/redfish/v1/Systems/1/hpsut/",
    "@odata.type": "#SUT.v2_5_6.SUT",
    "HPSUMPID": 0,
    "IsSelfUpdate": false,
    "LastBootUptime": "none",
    "LastOperationTime": "none",
    "Mode": "AutoDeploy",
    "OperationRequestor": "OS Administrator",
    "PollingIntervalInMinutes": 5,
    "SUTCompName": "",
    "SelfUpdateStatus": "none",
    "ServiceState": "Running",
    "ServiceVersion": "2.5.6.0",
    "StagingDirectory": "/tmp/stagingdirectory",
    "Verify": "autoVerify"
}
```

## /redfish/v1/Systems/1/hpsut/settings

```{
    "@odata.context": "/redfish/v1/$metadata#sut.sut/",
    "@odata.id": "/redfish/v1/Systems/1/hpsut/settings/",
    "@odata.type": "#SUT.v2_5_6.SUT",
    "AdditionalBaseline": "None",
    "AdditionalMessageIDs": [
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        }
    ],
    "DirectDeploy": false,
    "EnableiLOQueuedUpdates": true,
    "IgnoreWarnings": false,
    "InstallOrStageOccurredViaMode": "none",
    "InstallSet": [],
    "InstallationOptions": {
        "Downgrade": false,
        "FirmwareOnly": false,
        "Rewrite": false,
        "SoftwareOnly": false
    },
    "MessageID": "none",
    "OperationMode": "Online",
    "OptionalComponents": {
        "AMS": false,
        "SNMP": false,
        "WBEM": false
    },
    "RebootAllowed": false,
    "RebootOptions": {
        "Action": "IfNeeded",
        "DelaySeconds": 60,
        "RebootMessage": "Rebooting this server"
    },
    "RequestStatus": "Idle",
    "SaveLogs": true,
    "Schedule": {
        "DateTime": "",
        "Recurrence": 0,
        "ScheduleOptions": "",
        "ScheduleStatus": "",
        "ScheduleType": ""
    },
    "StageRetryCount": 2,
    "StageRetryDelay": 600,
    "TpmByPassFlag": true,
    "UriBaseline": "None",
    "UriBaselineVersion": "",
    "WaitTimeInSeconds": 0
}
```

## /redfish/v1/Systems/1/hpsut/settings/

```{
    "@odata.context": "/redfish/v1/$metadata#sut.sut/",
    "@odata.id": "/redfish/v1/Systems/1/hpsut/settings/",
    "@odata.type": "#SUT.v2_5_6.SUT",
    "AdditionalBaseline": "None",
    "AdditionalMessageIDs": [
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        },
        {
            "MessageID": ""
        }
    ],
    "DirectDeploy": false,
    "EnableiLOQueuedUpdates": true,
    "IgnoreWarnings": false,
    "InstallOrStageOccurredViaMode": "none",
    "InstallSet": [],
    "InstallationOptions": {
        "Downgrade": false,
        "FirmwareOnly": false,
        "Rewrite": false,
        "SoftwareOnly": false
    },
    "MessageID": "none",
    "OperationMode": "Online",
    "OptionalComponents": {
        "AMS": false,
        "SNMP": false,
        "WBEM": false
    },
    "RebootAllowed": false,
    "RebootOptions": {
        "Action": "IfNeeded",
        "DelaySeconds": 60,
        "RebootMessage": "Rebooting this server"
    },
    "RequestStatus": "Idle",
    "SaveLogs": true,
    "Schedule": {
        "DateTime": "",
        "Recurrence": 0,
        "ScheduleOptions": "",
        "ScheduleStatus": "",
        "ScheduleType": ""
    },
    "StageRetryCount": 2,
    "StageRetryDelay": 600,
    "TpmByPassFlag": true,
    "UriBaseline": "None",
    "UriBaselineVersion": "",
    "WaitTimeInSeconds": 0
}
```

## /redfish/v1/Systems/1/hpsut/systeminventory

```{
    "@odata.context": "/redfish/v1/$metadata#sut.sut/",
    "@odata.id": "/redfish/v1/Systems/1/hpsut/systeminventory/",
    "@odata.type": "#SUTSystemInventory.v2_5_6.SUTSystemInventory"
}
```

## /redfish/v1/Systems/1/hpsut/systeminventory/

```{
    "@odata.context": "/redfish/v1/$metadata#sut.sut/",
    "@odata.id": "/redfish/v1/Systems/1/hpsut/systeminventory/",
    "@odata.type": "#SUTSystemInventory.v2_5_6.SUTSystemInventory"
}
```

## /redfish/v1/Systems/1/hpsut/tasksettings

```{
    "@odata.context": "/redfish/v1/$metadata#sut.sut/",
    "@odata.id": "/redfish/v1/Systems/1/hpsut/tasksettings/",
    "@odata.type": "#SUTTaskSettings.v2_5_6.SUTTaskSettings",
    "TaskSettings": [
        {
            "Properties": {
                "BaselineSettings": {
                    "Arguments": "",
                    "Checksum": "",
                    "ChecksumProgramFile": "",
                    "Description": "",
                    "Order": "1",
                    "ProgramName": "",
                    "SourceUri": "",
                    "TargetUri": "",
                    "Type": "STORAGE"
                },
                "TaskResults": {
                    "MessageID": "",
                    "TaskState": ""
                }
            }
        },
        {
            "Properties": {
                "BaselineSettings": {
                    "Arguments": "",
                    "Checksum": "",
                    "ChecksumProgramFile": "",
                    "Description": "",
                    "Order": "2",
                    "ProgramName": "",
                    "SourceUri": "",
                    "TargetUri": "",
                    "Type": "BIOS"
                },
                "TaskResults": {
                    "MessageID": "",
                    "TaskState": ""
                }
            }
        }
    ]
}
```

## /redfish/v1/Systems/1/hpsut/tasksettings/

```{
    "@odata.context": "/redfish/v1/$metadata#sut.sut/",
    "@odata.id": "/redfish/v1/Systems/1/hpsut/tasksettings/",
    "@odata.type": "#SUTTaskSettings.v2_5_6.SUTTaskSettings",
    "TaskSettings": [
        {
            "Properties": {
                "BaselineSettings": {
                    "Arguments": "",
                    "Checksum": "",
                    "ChecksumProgramFile": "",
                    "Description": "",
                    "Order": "1",
                    "ProgramName": "",
                    "SourceUri": "",
                    "TargetUri": "",
                    "Type": "STORAGE"
                },
                "TaskResults": {
                    "MessageID": "",
                    "TaskState": ""
                }
            }
        },
        {
            "Properties": {
                "BaselineSettings": {
                    "Arguments": "",
                    "Checksum": "",
                    "ChecksumProgramFile": "",
                    "Description": "",
                    "Order": "2",
                    "ProgramName": "",
                    "SourceUri": "",
                    "TargetUri": "",
                    "Type": "BIOS"
                },
                "TaskResults": {
                    "MessageID": "",
                    "TaskState": ""
                }
            }
        }
    ]
}
```

