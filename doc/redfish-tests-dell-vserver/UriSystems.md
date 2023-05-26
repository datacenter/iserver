# Resource: /redfish/v1/Systems

Vendor | Model
--- | ---
Dell | vServer

## /redfish/v1/Systems

```{
    "@odata.context": "/redfish/v1/$metadata#ComputerSystemCollection.ComputerSystemCollection",
    "@odata.id": "/redfish/v1/Systems",
    "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection",
    "Description": "Collection of Computer Systems",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Computer System Collection"
}
```

## /redfish/v1/Systems/System.Embedded.1

```{
    "@odata.context": "/redfish/v1/$metadata#ComputerSystem.ComputerSystem",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1",
    "@odata.type": "#ComputerSystem.v1_12_0.ComputerSystem",
    "Actions": {
        "#ComputerSystem.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff",
                "ForceRestart",
                "GracefulRestart",
                "GracefulShutdown",
                "PushPowerButton",
                "Nmi",
                "PowerCycle"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Actions/ComputerSystem.Reset"
        }
    },
    "AssetTag": "testdell",
    "Bios": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Bios"
    },
    "BiosVersion": "1.2.4",
    "Boot": {
        "BootOptions": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/BootOptions"
        },
        "BootOrder": [
            "Boot0004",
            "Boot0000"
        ],
        "BootOrder@odata.count": 2,
        "BootSourceOverrideEnabled": "Disabled",
        "BootSourceOverrideMode": "UEFI",
        "BootSourceOverrideTarget": "None",
        "BootSourceOverrideTarget@Redfish.AllowableValues": [
            "None",
            "Pxe",
            "Floppy",
            "Cd",
            "Hdd",
            "BiosSetup",
            "Utilities",
            "UefiTarget",
            "SDCard",
            "UefiHttp"
        ],
        "Certificates": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Boot/Certificates"
        },
        "UefiTargetBootSourceOverride": null
    },
    "Description": "Computer System which represents a machine (physical or virtual) and the local resources such as memory, cpu and other devices that can be accessed from that machine.",
    "EthernetInterfaces": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces"
    },
    "HostName": "",
    "HostWatchdogTimer": {
        "FunctionEnabled": false,
        "Status": {
            "State": "Disabled"
        },
        "TimeoutAction": "None"
    },
    "HostingRoles": [],
    "HostingRoles@odata.count": 0,
    "Id": "System.Embedded.1",
    "IndicatorLED": "Blinking",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Chassis@odata.count": 1,
        "CooledBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/0"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/1"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/2"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/3"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/4"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/5"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/6"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/7"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/8"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/9"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/10"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/11"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/12"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/13"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/14"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/15"
            }
        ],
        "CooledBy@odata.count": 16,
        "ManagedBy": [
            {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1"
            }
        ],
        "ManagedBy@odata.count": 1,
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "BootOrder": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBootSources"
                },
                "DellBIOSService": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBIOSService"
                },
                "DellBootSources": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBootSources"
                },
                "DellChassisCollection": {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellChassis"
                },
                "DellGPUSensorCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellGPUSensors"
                },
                "DellMetricService": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellMetricService"
                },
                "DellNumericSensorCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors"
                },
                "DellOSDeploymentService": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService"
                },
                "DellPSNumericSensorCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors"
                },
                "DellPresenceAndStatusSensorCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPresenceAndStatusSensors"
                },
                "DellRaidService": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService"
                },
                "DellRollupStatusCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus"
                },
                "DellSensorCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors"
                },
                "DellSlotCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots"
                },
                "DellSoftwareInstallationService": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService"
                },
                "DellVideoCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellVideo"
                },
                "DellVideoNetworkCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellVideoNetwork"
                }
            }
        },
        "PoweredBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerSupplies/0"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerSupplies/1"
            }
        ],
        "PoweredBy@odata.count": 2
    },
    "Manufacturer": "Dell Inc.",
    "Memory": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory"
    },
    "MemorySummary": {
        "MemoryMirroring": "System",
        "Status": {
            "Health": "OK",
            "HealthRollup": "OK",
            "State": "Enabled"
        },
        "TotalSystemMemoryGiB": 128
    },
    "Model": "PowerEdge R650",
    "Name": "System",
    "NetworkInterfaces": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkInterfaces"
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellSystem": {
                "@odata.context": "/redfish/v1/$metadata#DellSystem.DellSystem",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSystem/System.Embedded.1",
                "@odata.type": "#DellSystem.v1_3_0.DellSystem",
                "BIOSReleaseDate": "05/28/2021",
                "BaseBoardChassisSlot": "NA",
                "BatteryRollupStatus": "OK",
                "BladeGeometry": "NotApplicable",
                "CMCIP": null,
                "CPURollupStatus": "OK",
                "ChassisModel": "",
                "ChassisName": "Main System Chassis",
                "ChassisServiceTag": "U8OIL5X",
                "ChassisSystemHeightUnit": 1,
                "CurrentRollupStatus": "OK",
                "EstimatedExhaustTemperatureCelsius": 255,
                "EstimatedSystemAirflowCFM": 255,
                "ExpressServiceCode": "2440875279",
                "FanRollupStatus": "OK",
                "IDSDMRollupStatus": null,
                "Id": "System.Embedded.1",
                "IntrusionRollupStatus": "OK",
                "IsOEMBranded": "False",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-08-30T23:00:48+00:00",
                "LicensingRollupStatus": "OK",
                "ManagedSystemSize": "1 U",
                "MaxCPUSockets": 2,
                "MaxDIMMSlots": 32,
                "MaxPCIeSlots": 3,
                "MemoryOperationMode": "OptimizerMode",
                "Name": "DellSystem",
                "NodeID": "U8OIL5X",
                "PSRollupStatus": "OK",
                "PlatformGUID": "3346464f-c0b1-3880-4410-00344c4c4544",
                "PopulatedDIMMSlots": 16,
                "PopulatedPCIeSlots": 1,
                "PowerCapEnabledState": "Disabled",
                "SDCardRollupStatus": null,
                "SELRollupStatus": "OK",
                "ServerAllocationWatts": null,
                "StorageRollupStatus": "OK",
                "SysMemErrorMethodology": "Multi-bitECC",
                "SysMemFailOverState": "NotInUse",
                "SysMemLocation": "SystemBoardOrMotherboard",
                "SysMemPrimaryStatus": "OK",
                "SystemGeneration": "15G Monolithic",
                "SystemID": 2322,
                "SystemRevision": "I",
                "TempRollupStatus": "OK",
                "TempStatisticsRollupStatus": "OK",
                "UUID": "4c4c4544-0034-4410-8038-b1c04f464633",
                "VoltRollupStatus": "OK",
                "smbiosGUID": "44454c4c-3400-1044-8038-b1c04f464633"
            }
        }
    },
    "PCIeDevices": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/103-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/3-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/102-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/101-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0"
        }
    ],
    "PCIeDevices@odata.count": 12,
    "PCIeFunctions": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23/PCIeFunctions/0-23-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/103-0/PCIeFunctions/103-0-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17/PCIeFunctions/0-17-5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/3-0/PCIeFunctions/3-0-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/102-0/PCIeFunctions/102-0-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/101-0/PCIeFunctions/101-0-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-0"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0/PCIeFunctions/5-0-0"
        }
    ],
    "PCIeFunctions@odata.count": 17,
    "PartNumber": "0JDN4VA00",
    "PowerState": "On",
    "ProcessorSummary": {
        "Count": 2,
        "LogicalProcessorCount": 112,
        "Model": "Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz",
        "Status": {
            "Health": "OK",
            "HealthRollup": "OK",
            "State": "Enabled"
        }
    },
    "Processors": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors"
    },
    "SKU": "U8OIL5X",
    "SecureBoot": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SecureBoot"
    },
    "SerialNumber": "YGFCBTJSO8WOMR",
    "SimpleStorage": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SimpleStorage"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "Storage": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage"
    },
    "SystemType": "Physical",
    "TrustedModules": [
        {
            "FirmwareVersion": "NotAvailable",
            "InterfaceType": "TPM2_0",
            "Status": {
                "State": "Disabled"
            }
        }
    ],
    "TrustedModules@odata.count": 1,
    "UUID": "4c4c4544-0034-4410-8038-b1c04f464633"
}
```

## /redfish/v1/Systems/System.Embedded.1/Bios

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Bios/Settings"
        },
        "SupportedApplyTimes": [
            "OnReset",
            "AtMaintenanceWindowStart",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#Bios.Bios",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Bios",
    "@odata.type": "#Bios.v1_1_1.Bios",
    "Actions": {
        "#Bios.ChangePassword": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Bios/Actions/Bios.ChangePassword"
        },
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Bios/Actions/Bios.ResetBios"
        },
        "Oem": {
            "#DellBios.RunBIOSLiveScanning": {
                "target": "/redfish/v1/Systems/System.Embedded.1/Bios/Actions/Oem/DellBios.RunBIOSLiveScanning"
            }
        }
    },
    "AttributeRegistry": "BiosAttributeRegistry.v1_0_3",
    "Attributes": {
        "AcPwrRcvry": "Last",
        "AcPwrRcvryDelay": "Immediate",
        "AcPwrRcvryUserDelay": 60,
        "AdddcSetting": "Disabled",
        "AesNi": "Enabled",
        "AssetTag": "testdell",
        "AuthorizeDeviceFirmware": "Disabled",
        "AvxIccpPreGrantLevel": "IccpHeavy128",
        "AvxIccpPreGrantLicense": "Disabled",
        "BiosNvmeDriver": "DellQualifiedDrives",
        "BootMode": "Uefi",
        "BootSeqRetry": "Enabled",
        "CECriticalSEL": "Enabled",
        "ConTermType": "Vt100Vt220",
        "ControlledTurbo": "Disabled",
        "ControlledTurboMinusBin": 0,
        "CorrEccSmi": "Enabled",
        "CpuInterconnectBusLinkPower": "Disabled",
        "CpuInterconnectBusSpeed": "MaxDataRate",
        "CurrentEmbVideoState": "Enabled",
        "DcuIpPrefetcher": "Enabled",
        "DcuStreamerPrefetcher": "Enabled",
        "DeadLineLlcAlloc": "Enabled",
        "DellAutoDiscovery": "PlatformDefault",
        "DellWyseP25BIOSAccess": "Enabled",
        "DirectoryAtoS": "Disabled",
        "DirectoryMode": "Enabled",
        "DynamicCoreAllocation": "Disabled",
        "DynamicL1": "Disabled",
        "EmbNic1Nic2": "Enabled",
        "EmbSata": "AhciMode",
        "EmbVideo": "Enabled",
        "EnablePkgcCriteria": "Disabled",
        "EnergyPerformanceBias": "MaxPower",
        "ErrPrompt": "Enabled",
        "ExtSerialConnector": "Serial1",
        "FRMPercent": "FRM_25_Percent",
        "FailSafeBaud": "115200",
        "ForceInt10": "Disabled",
        "GenericUsbBoot": "Disabled",
        "HddFailover": "Disabled",
        "HddPlaceholder": "Disabled",
        "HttpDev1DhcpEnDis": "Enabled",
        "HttpDev1Dns1": "",
        "HttpDev1Dns2": "",
        "HttpDev1DnsDhcpEnDis": "Enabled",
        "HttpDev1EnDis": "Disabled",
        "HttpDev1Gateway": "",
        "HttpDev1Interface": "NIC.Embedded.1-1-1",
        "HttpDev1Ip": "",
        "HttpDev1Mask": "",
        "HttpDev1Protocol": "IPv4",
        "HttpDev1TlsMode": "None",
        "HttpDev1Uri": "",
        "HttpDev1VlanEnDis": "Disabled",
        "HttpDev1VlanId": 1,
        "HttpDev1VlanPriority": 0,
        "HttpDev2DhcpEnDis": "Enabled",
        "HttpDev2Dns1": "",
        "HttpDev2Dns2": "",
        "HttpDev2DnsDhcpEnDis": "Enabled",
        "HttpDev2EnDis": "Disabled",
        "HttpDev2Gateway": "",
        "HttpDev2Interface": "NIC.Embedded.1-1-1",
        "HttpDev2Ip": "",
        "HttpDev2Mask": "",
        "HttpDev2Protocol": "IPv4",
        "HttpDev2TlsMode": "None",
        "HttpDev2Uri": "",
        "HttpDev2VlanEnDis": "Disabled",
        "HttpDev2VlanId": 1,
        "HttpDev2VlanPriority": 0,
        "HttpDev3DhcpEnDis": "Enabled",
        "HttpDev3Dns1": "",
        "HttpDev3Dns2": "",
        "HttpDev3DnsDhcpEnDis": "Enabled",
        "HttpDev3EnDis": "Disabled",
        "HttpDev3Gateway": "",
        "HttpDev3Interface": "NIC.Embedded.1-1-1",
        "HttpDev3Ip": "",
        "HttpDev3Mask": "",
        "HttpDev3Protocol": "IPv4",
        "HttpDev3TlsMode": "None",
        "HttpDev3Uri": "",
        "HttpDev3VlanEnDis": "Disabled",
        "HttpDev3VlanId": 1,
        "HttpDev3VlanPriority": 0,
        "HttpDev4DhcpEnDis": "Enabled",
        "HttpDev4Dns1": "",
        "HttpDev4Dns2": "",
        "HttpDev4DnsDhcpEnDis": "Enabled",
        "HttpDev4EnDis": "Disabled",
        "HttpDev4Gateway": "",
        "HttpDev4Interface": "NIC.Embedded.1-1-1",
        "HttpDev4Ip": "",
        "HttpDev4Mask": "",
        "HttpDev4Protocol": "IPv4",
        "HttpDev4TlsMode": "None",
        "HttpDev4Uri": "",
        "HttpDev4VlanEnDis": "Disabled",
        "HttpDev4VlanId": 1,
        "HttpDev4VlanPriority": 0,
        "InBandManageabilityInterface": "Enabled",
        "IntegratedNetwork1": "Enabled",
        "IntelSgx": "Off",
        "IntelTxt": "Off",
        "IoatEngine": "Disabled",
        "IscsiDev1Con1Auth": "None",
        "IscsiDev1Con1ChapName": "",
        "IscsiDev1Con1ChapSecret": "",
        "IscsiDev1Con1ChapType": "OneWay",
        "IscsiDev1Con1DhcpEnDis": "Disabled",
        "IscsiDev1Con1EnDis": "Disabled",
        "IscsiDev1Con1Gateway": "",
        "IscsiDev1Con1Interface": "NIC.Embedded.1-1-1",
        "IscsiDev1Con1Ip": "",
        "IscsiDev1Con1IsId": "",
        "IscsiDev1Con1Lun": "0",
        "IscsiDev1Con1Mask": "",
        "IscsiDev1Con1Port": 3260,
        "IscsiDev1Con1Protocol": "IPv4",
        "IscsiDev1Con1Retry": 3,
        "IscsiDev1Con1RevChapName": "",
        "IscsiDev1Con1RevChapSecret": "",
        "IscsiDev1Con1TargetIp": "",
        "IscsiDev1Con1TargetName": "",
        "IscsiDev1Con1TgtDhcpEnDis": "Disabled",
        "IscsiDev1Con1Timeout": 10000,
        "IscsiDev1Con1VlanEnDis": "Disabled",
        "IscsiDev1Con1VlanId": 1,
        "IscsiDev1Con1VlanPriority": 0,
        "IscsiDev1Con2Auth": "None",
        "IscsiDev1Con2ChapName": "",
        "IscsiDev1Con2ChapSecret": "",
        "IscsiDev1Con2ChapType": "OneWay",
        "IscsiDev1Con2DhcpEnDis": "Disabled",
        "IscsiDev1Con2EnDis": "Disabled",
        "IscsiDev1Con2Gateway": "",
        "IscsiDev1Con2Interface": "NIC.Embedded.1-1-1",
        "IscsiDev1Con2Ip": "",
        "IscsiDev1Con2IsId": "",
        "IscsiDev1Con2Lun": "0",
        "IscsiDev1Con2Mask": "",
        "IscsiDev1Con2Port": 3260,
        "IscsiDev1Con2Protocol": "IPv4",
        "IscsiDev1Con2Retry": 3,
        "IscsiDev1Con2RevChapName": "",
        "IscsiDev1Con2RevChapSecret": "",
        "IscsiDev1Con2TargetIp": "",
        "IscsiDev1Con2TargetName": "",
        "IscsiDev1Con2TgtDhcpEnDis": "Disabled",
        "IscsiDev1Con2Timeout": 10000,
        "IscsiDev1Con2VlanEnDis": "Disabled",
        "IscsiDev1Con2VlanId": 1,
        "IscsiDev1Con2VlanPriority": 0,
        "IscsiDev1ConOrder": "Con1Con2",
        "IscsiDev1EnDis": "Disabled",
        "IscsiInitiatorName": "",
        "LlcPrefetch": "Enabled",
        "LmceEn": "Disabled",
        "LogicalProc": "Enabled",
        "MadtCoreEnumeration": "RoundRobin",
        "MemFrequency": "MaxPerf",
        "MemOpMode": "OptimizerMode",
        "MemPatrolScrub": "Standard",
        "MemRefreshRate": "1x",
        "MemTest": "Disabled",
        "MemoryEncryption": "Disabled",
        "MemoryMappedIOH": "56TB",
        "MemoryTraining": "MemoryTrainingFast",
        "MmioAbove4Gb": "Enabled",
        "MonitorMwait": "Enabled",
        "NodeInterleave": "Disabled",
        "NumLock": "On",
        "NvmeMode": "NonRaid",
        "OneTimeBootMode": "Disabled",
        "OneTimeUefiBootSeqDev": "AHCI.SL.6-2",
        "OptimizerMode": "Auto",
        "OsAcpiCx": "OsCxC2",
        "OsWatchdogTimer": "Disabled",
        "PCIRootDeviceUnhide": "Disabled",
        "PackageCStates": "Enabled",
        "PasswordStatus": "Unlocked",
        "PcieAspmL1": "Disabled",
        "PkgCLatNeg": "Disabled",
        "PowerCycleRequest": "None",
        "Proc1Brand": "Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz",
        "Proc1Id": "6-6A-6",
        "Proc1L2Cache": "28x1280 KB",
        "Proc1L3Cache": "42 MB",
        "Proc1MaxMemoryCapacity": "6 TB",
        "Proc1Microcode": "0xD0002B1",
        "Proc1NumCores": 28,
        "Proc2Brand": "Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz",
        "Proc2Id": "6-6A-6",
        "Proc2L2Cache": "28x1280 KB",
        "Proc2L3Cache": "42 MB",
        "Proc2MaxMemoryCapacity": "6 TB",
        "Proc2Microcode": "0xD0002B1",
        "Proc2NumCores": 28,
        "ProcAdjCacheLine": "Enabled",
        "ProcAvxP1": "Normal",
        "ProcBusSpeed": "11.2 GT/s",
        "ProcC1E": "Disabled",
        "ProcCStates": "Disabled",
        "ProcCoreSpeed": "2.0 GHz",
        "ProcCores": "All",
        "ProcHwPrefetcher": "Enabled",
        "ProcPwrPerf": "MaxPerf",
        "ProcTurboMode": "Enabled",
        "ProcVirtualization": "Enabled",
        "ProcX2Apic": "Enabled",
        "ProcessorActivePbf": "Disabled",
        "ProcessorC1AutoDemotion": "Disabled",
        "ProcessorC1AutoUnDemotion": "Disabled",
        "ProcessorEist": "Enabled",
        "ProcessorGpssTimer": "500us",
        "ProcessorRaplPrioritization": "Disabled",
        "PwrButton": "Enabled",
        "PxeDev1EnDis": "Enabled",
        "PxeDev1Interface": "NIC.Embedded.1-1-1",
        "PxeDev1Protocol": "IPv4",
        "PxeDev1VlanEnDis": "Disabled",
        "PxeDev1VlanId": 1,
        "PxeDev1VlanPriority": 0,
        "PxeDev2EnDis": "Disabled",
        "PxeDev2Interface": "NIC.Integrated.1-1-1",
        "PxeDev2Protocol": "IPv4",
        "PxeDev2VlanEnDis": "Disabled",
        "PxeDev2VlanId": 1,
        "PxeDev2VlanPriority": 0,
        "PxeDev3EnDis": "Disabled",
        "PxeDev3Interface": "NIC.Embedded.1-1-1",
        "PxeDev3Protocol": "IPv4",
        "PxeDev3VlanEnDis": "Disabled",
        "PxeDev3VlanId": 1,
        "PxeDev3VlanPriority": 0,
        "PxeDev4EnDis": "Disabled",
        "PxeDev4Interface": "NIC.Embedded.1-1-1",
        "PxeDev4Protocol": "IPv4",
        "PxeDev4VlanEnDis": "Disabled",
        "PxeDev4VlanId": 1,
        "PxeDev4VlanPriority": 0,
        "RedirAfterBoot": "Enabled",
        "RedundantOsBoot": "Disabled",
        "RedundantOsLocation": "None",
        "RedundantOsState": "Visible",
        "SataPortA": "Auto",
        "SataPortACapacity": "N/A",
        "SataPortADriveType": "Unknown Device",
        "SataPortAModel": "Unknown",
        "SataPortB": "Auto",
        "SataPortBCapacity": "N/A",
        "SataPortBDriveType": "Unknown Device",
        "SataPortBModel": "Unknown",
        "SataPortC": "Auto",
        "SataPortCCapacity": "N/A",
        "SataPortCDriveType": "Unknown Device",
        "SataPortCModel": "Unknown",
        "SataPortD": "Auto",
        "SataPortDCapacity": "N/A",
        "SataPortDDriveType": "Unknown Device",
        "SataPortDModel": "Unknown",
        "SecureBoot": "Disabled",
        "SecureBootMode": "DeployedMode",
        "SecureBootPolicy": "Standard",
        "SecurityFreezeLock": "Enabled",
        "SerialComm": "Off",
        "SerialPortAddress": "Com1",
        "SetBootOrderDis": "",
        "SetBootOrderEn": "AHCI.SL.6-2,NIC.PxeDevice.1-1",
        "SetBootOrderFqdd1": "",
        "SetBootOrderFqdd10": "",
        "SetBootOrderFqdd11": "",
        "SetBootOrderFqdd12": "",
        "SetBootOrderFqdd13": "",
        "SetBootOrderFqdd14": "",
        "SetBootOrderFqdd15": "",
        "SetBootOrderFqdd16": "",
        "SetBootOrderFqdd2": "",
        "SetBootOrderFqdd3": "",
        "SetBootOrderFqdd4": "",
        "SetBootOrderFqdd5": "",
        "SetBootOrderFqdd6": "",
        "SetBootOrderFqdd7": "",
        "SetBootOrderFqdd8": "",
        "SetBootOrderFqdd9": "",
        "SetLegacyHddOrderFqdd1": "",
        "SetLegacyHddOrderFqdd10": "",
        "SetLegacyHddOrderFqdd11": "",
        "SetLegacyHddOrderFqdd12": "",
        "SetLegacyHddOrderFqdd13": "",
        "SetLegacyHddOrderFqdd14": "",
        "SetLegacyHddOrderFqdd15": "",
        "SetLegacyHddOrderFqdd16": "",
        "SetLegacyHddOrderFqdd2": "",
        "SetLegacyHddOrderFqdd3": "",
        "SetLegacyHddOrderFqdd4": "",
        "SetLegacyHddOrderFqdd5": "",
        "SetLegacyHddOrderFqdd6": "",
        "SetLegacyHddOrderFqdd7": "",
        "SetLegacyHddOrderFqdd8": "",
        "SetLegacyHddOrderFqdd9": "",
        "SetupPassword": null,
        "Slot1": "Enabled",
        "Slot1Bif": "x16",
        "Slot2": "Enabled",
        "Slot2Bif": "x16",
        "SmmSecurityMitigation": "Disabled",
        "SnoopHldOff": "Roll256Cycles",
        "SriovGlobalEnable": "Disabled",
        "SubNumaCluster": "Disabled",
        "SysMemSize": "128 GB",
        "SysMemSpeed": "2933 MT/s",
        "SysMemType": "ECC DDR4",
        "SysMemVolt": "1.20 V",
        "SysMfrContactInfo": "www.dell.com",
        "SysPassword": null,
        "SysPrepClean": "None",
        "SysProfile": "PerfOptimized",
        "SystemBiosVersion": "1.2.4",
        "SystemCpldVersion": "1.0.5",
        "SystemManufacturer": "Dell Inc.",
        "SystemMeVersion": "4.4.4.56",
        "SystemModelName": "PowerEdge R650",
        "SystemServiceTag": "U8OIL5X",
        "Tpm2Algorithm": "SHA1",
        "Tpm2Hierarchy": "Enabled",
        "TpmFirmware": "NotAvailable",
        "TpmInfo": "Type: 2.0-NTC",
        "TpmPpiBypassClear": "Disabled",
        "TpmPpiBypassProvision": "Disabled",
        "TpmSecurity": "Off",
        "UefiComplianceVersion": "2.7",
        "UefiVariableAccess": "Standard",
        "UncoreFrequency": "MaxUFS",
        "UpiPrefetch": "Enabled",
        "UsbManagedPort": "On",
        "UsbPorts": "AllOn",
        "VideoMem": "16 MB",
        "WorkloadConfiguration": "Balance",
        "WorkloadProfile": "WriteOnly",
        "WriteCache": "Disabled",
        "XptPrefetch": "Enabled"
    },
    "Description": "BIOS Configuration Current Settings",
    "Id": "Bios",
    "Links": {
        "ActiveSoftwareImage": {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Installed-159-1.2.4__BIOS.Setup.1-1"
        },
        "SoftwareImages": [
            {
                "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Installed-159-1.2.4__BIOS.Setup.1-1"
            },
            {
                "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Current-159-1.2.4__BIOS.Setup.1-1"
            }
        ],
        "SoftwareImages@odata.count": 2
    },
    "Name": "BIOS Configuration Current Settings"
}
```

## /redfish/v1/Systems/System.Embedded.1/Bios/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#Bios.Bios",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Bios/Settings",
    "@odata.type": "#Bios.v1_1_1.Bios",
    "Actions": {
        "Oem": {
            "DellManager.v1_0_0#DellManager.ClearPending": {
                "target": "/redfish/v1/Systems/System.Embedded.1/Bios/Settings/Actions/Oem/DellManager.ClearPending"
            }
        }
    },
    "AttributeRegistry": "BiosAttributeRegistry.v1_0_3",
    "Attributes": {},
    "Description": "BIOS Configuration Pending Settings. These settings will be applied on next system reboot.",
    "Id": "Settings",
    "Name": "BIOS Configuration Pending Settings",
    "Oem": {
        "Dell": {
            "@odata.context": "/redfish/v1/$metadata#DellManager.DellManager",
            "@odata.type": "#DellManager.v1_1_0.DellManager",
            "Jobs": {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/Jobs"
            }
        }
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/Boot/Certificates

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateCollection.CertificateCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Boot/Certificates",
    "@odata.type": "#CertificateCollection.CertificateCollection",
    "Description": "A Collection of BIOS HTTP Boot Certificate resource instances.",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Certificate Collection"
}
```

## /redfish/v1/Systems/System.Embedded.1/BootOptions

```{
    "@odata.context": "/redfish/v1/$metadata#BootOptionCollection.BootOptionCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/BootOptions",
    "@odata.type": "#BootOptionCollection.BootOptionCollection",
    "Description": "Collection of BootOptions",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/BootOptions/Boot0004"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/BootOptions/Boot0000"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Boot Options Collection"
}
```

## /redfish/v1/Systems/System.Embedded.1/BootOptions/Boot0000

```{
    "@odata.context": "/redfish/v1/$metadata#BootOption.BootOption",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/BootOptions/Boot0000",
    "@odata.type": "#BootOption.v1_0_4.BootOption",
    "BootOptionEnabled": true,
    "BootOptionReference": "Boot0000",
    "Description": "Current settings of the UEFI Boot option",
    "DisplayName": "PXE Device 1: Embedded NIC 1 Port 1 Partition 1",
    "Id": "Boot0000",
    "Name": "Uefi Boot Option",
    "UefiDevicePath": "VenHw(3A191845-5F86-4E78-8FCE-C4CFF59F9DAA)"
}
```

## /redfish/v1/Systems/System.Embedded.1/BootOptions/Boot0004

```{
    "@odata.context": "/redfish/v1/$metadata#BootOption.BootOption",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/BootOptions/Boot0004",
    "@odata.type": "#BootOption.v1_0_4.BootOption",
    "BootOptionEnabled": true,
    "BootOptionReference": "Boot0004",
    "Description": "Current settings of the UEFI Boot option",
    "DisplayName": "AHCI Controller in SL 6: VMware ESXi",
    "Id": "Boot0004",
    "Name": "Uefi Boot Option",
    "UefiDevicePath": "HD(1,GPT,02BE3442-A00F-477A-B0F0-C387A1B858B7,0x40,0x32000)/\\EFI\\VMware\\safeboot64.efi"
}
```

## /redfish/v1/Systems/System.Embedded.1/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Description": "Collection of Ethernet Interfaces for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Embedded.2-1-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Embedded.1-1-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Integrated.1-2-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Integrated.1-1-1"
        }
    ],
    "Members@odata.count": 4,
    "Name": "System Ethernet Interface Collection"
}
```

## /redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Embedded.1-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Embedded.1-1-1",
    "@odata.type": "#EthernetInterface.v1_6_1.EthernetInterface",
    "AutoNeg": false,
    "Description": "Embedded NIC 1 Port 1 Partition 1",
    "EthernetInterfaceType": "Physical",
    "FQDN": null,
    "FullDuplex": false,
    "HostName": null,
    "IPv4Addresses": [],
    "IPv4Addresses@odata.count": 0,
    "IPv6AddressPolicyTable": [],
    "IPv6AddressPolicyTable@odata.count": 0,
    "IPv6Addresses": [],
    "IPv6Addresses@odata.count": 0,
    "IPv6DefaultGateway": null,
    "IPv6StaticAddresses": [],
    "IPv6StaticAddresses@odata.count": 0,
    "Id": "NIC.Embedded.1-1-1",
    "InterfaceEnabled": true,
    "LinkStatus": "LinkDown",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        }
    },
    "MACAddress": "70:B5:E8:F0:25:52",
    "MTUSize": null,
    "MaxIPv6StaticAddresses": null,
    "Name": "System Ethernet Interface",
    "NameServers": [],
    "NameServers@odata.count": 0,
    "PermanentMACAddress": "70:B5:E8:F0:25:52",
    "SpeedMbps": 0,
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "UefiDevicePath": "PciRoot(0x0)/Pci(0x1C,0x5)/Pci(0x0,0x0)",
    "VLAN": {}
}
```

## /redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Embedded.2-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Embedded.2-1-1",
    "@odata.type": "#EthernetInterface.v1_6_1.EthernetInterface",
    "AutoNeg": false,
    "Description": "Embedded NIC 1 Port 2 Partition 1",
    "EthernetInterfaceType": "Physical",
    "FQDN": null,
    "FullDuplex": false,
    "HostName": null,
    "IPv4Addresses": [],
    "IPv4Addresses@odata.count": 0,
    "IPv6AddressPolicyTable": [],
    "IPv6AddressPolicyTable@odata.count": 0,
    "IPv6Addresses": [],
    "IPv6Addresses@odata.count": 0,
    "IPv6DefaultGateway": null,
    "IPv6StaticAddresses": [],
    "IPv6StaticAddresses@odata.count": 0,
    "Id": "NIC.Embedded.2-1-1",
    "InterfaceEnabled": true,
    "LinkStatus": "LinkDown",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        }
    },
    "MACAddress": "70:B5:E8:F0:25:53",
    "MTUSize": null,
    "MaxIPv6StaticAddresses": null,
    "Name": "System Ethernet Interface",
    "NameServers": [],
    "NameServers@odata.count": 0,
    "PermanentMACAddress": "70:B5:E8:F0:25:53",
    "SpeedMbps": 0,
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "UefiDevicePath": "PciRoot(0x0)/Pci(0x1C,0x5)/Pci(0x0,0x1)",
    "VLAN": {}
}
```

## /redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Integrated.1-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Integrated.1-1-1",
    "@odata.type": "#EthernetInterface.v1_6_1.EthernetInterface",
    "AutoNeg": true,
    "Description": "Integrated NIC 1 Port 1 Partition 1",
    "EthernetInterfaceType": "Physical",
    "FQDN": null,
    "FullDuplex": true,
    "HostName": null,
    "IPv4Addresses": [],
    "IPv4Addresses@odata.count": 0,
    "IPv6AddressPolicyTable": [],
    "IPv6AddressPolicyTable@odata.count": 0,
    "IPv6Addresses": [],
    "IPv6Addresses@odata.count": 0,
    "IPv6DefaultGateway": null,
    "IPv6StaticAddresses": [],
    "IPv6StaticAddresses@odata.count": 0,
    "Id": "NIC.Integrated.1-1-1",
    "InterfaceEnabled": true,
    "LinkStatus": "LinkUp",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        }
    },
    "MACAddress": "B8:CE:F6:94:F0:B8",
    "MTUSize": null,
    "MaxIPv6StaticAddresses": null,
    "Name": "System Ethernet Interface",
    "NameServers": [],
    "NameServers@odata.count": 0,
    "PermanentMACAddress": "B8:CE:F6:94:F0:B8",
    "SpeedMbps": 10000,
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "UefiDevicePath": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)/MAC(B8CEF694F0B8,0x1)",
    "VLAN": {}
}
```

## /redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Integrated.1-2-1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Integrated.1-2-1",
    "@odata.type": "#EthernetInterface.v1_6_1.EthernetInterface",
    "AutoNeg": true,
    "Description": "Integrated NIC 1 Port 2 Partition 1",
    "EthernetInterfaceType": "Physical",
    "FQDN": null,
    "FullDuplex": true,
    "HostName": null,
    "IPv4Addresses": [],
    "IPv4Addresses@odata.count": 0,
    "IPv6AddressPolicyTable": [],
    "IPv6AddressPolicyTable@odata.count": 0,
    "IPv6Addresses": [],
    "IPv6Addresses@odata.count": 0,
    "IPv6DefaultGateway": null,
    "IPv6StaticAddresses": [],
    "IPv6StaticAddresses@odata.count": 0,
    "Id": "NIC.Integrated.1-2-1",
    "InterfaceEnabled": true,
    "LinkStatus": "LinkUp",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        }
    },
    "MACAddress": "B8:CE:F6:94:F0:B9",
    "MTUSize": null,
    "MaxIPv6StaticAddresses": null,
    "Name": "System Ethernet Interface",
    "NameServers": [],
    "NameServers@odata.count": 0,
    "PermanentMACAddress": "B8:CE:F6:94:F0:B9",
    "SpeedMbps": 10000,
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "UefiDevicePath": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x1)/MAC(B8CEF694F0B9,0x1)",
    "VLAN": {}
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryCollection.MemoryCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory",
    "@odata.type": "#MemoryCollection.MemoryCollection",
    "Description": "Collection of memory devices for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2"
        }
    ],
    "Members@odata.count": 16,
    "Name": "Memory Devices Collection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM A1",
    "DeviceLocator": "DIMM A1",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.A1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM A1",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1/Oem/Dell/DellMemory/DIMM.Socket.A1",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "19949A6B",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A1#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A1_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.A1",
                        "Id": "DIMM.Socket.A1#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A6B"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.A1#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.A1",
    "Name": "DIMM A1 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1/Oem/Dell/DellMemory/DIMM.Socket.A1

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A1/Oem/Dell/DellMemory/DIMM.Socket.A1",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "A",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.A1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM A2",
    "DeviceLocator": "DIMM A2",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.A2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM A2",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2/Oem/Dell/DellMemory/DIMM.Socket.A2",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A2",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "19949A55",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A2#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A2_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.A2",
                        "Id": "DIMM.Socket.A2#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A55"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.A2#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.A2",
    "Name": "DIMM A2 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2/Oem/Dell/DellMemory/DIMM.Socket.A2

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A2/Oem/Dell/DellMemory/DIMM.Socket.A2",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "A",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.A2",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM A3",
    "DeviceLocator": "DIMM A3",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.A3",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM A3",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3/Oem/Dell/DellMemory/DIMM.Socket.A3",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A3",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "19949A27",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A3#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A3_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.A3",
                        "Id": "DIMM.Socket.A3#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A27"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.A3#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.A3",
    "Name": "DIMM A3 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3/Oem/Dell/DellMemory/DIMM.Socket.A3

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A3/Oem/Dell/DellMemory/DIMM.Socket.A3",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "A",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.A3",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM A4",
    "DeviceLocator": "DIMM A4",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.A4",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM A4",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4/Oem/Dell/DellMemory/DIMM.Socket.A4",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A4",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "19949A29",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A4#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A4_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.A4",
                        "Id": "DIMM.Socket.A4#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A29"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.A4#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.A4",
    "Name": "DIMM A4 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4/Oem/Dell/DellMemory/DIMM.Socket.A4

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A4/Oem/Dell/DellMemory/DIMM.Socket.A4",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "A",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.A4",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM A5",
    "DeviceLocator": "DIMM A5",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.A5",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM A5",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5/Oem/Dell/DellMemory/DIMM.Socket.A5",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A5",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "19949A26",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A5#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A5_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.A5",
                        "Id": "DIMM.Socket.A5#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A26"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.A5#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.A5",
    "Name": "DIMM A5 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5/Oem/Dell/DellMemory/DIMM.Socket.A5

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A5/Oem/Dell/DellMemory/DIMM.Socket.A5",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "A",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.A5",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM A6",
    "DeviceLocator": "DIMM A6",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.A6",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM A6",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6/Oem/Dell/DellMemory/DIMM.Socket.A6",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A6",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "19949A56",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A6#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A6_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.A6",
                        "Id": "DIMM.Socket.A6#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A56"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.A6#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.A6",
    "Name": "DIMM A6 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6/Oem/Dell/DellMemory/DIMM.Socket.A6

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A6/Oem/Dell/DellMemory/DIMM.Socket.A6",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "A",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.A6",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM A7",
    "DeviceLocator": "DIMM A7",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.A7",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM A7",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7/Oem/Dell/DellMemory/DIMM.Socket.A7",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A7",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "19949A67",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A7#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A7_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.A7",
                        "Id": "DIMM.Socket.A7#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A67"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.A7#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.A7",
    "Name": "DIMM A7 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7/Oem/Dell/DellMemory/DIMM.Socket.A7

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A7/Oem/Dell/DellMemory/DIMM.Socket.A7",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "A",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.A7",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM A8",
    "DeviceLocator": "DIMM A8",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.A8",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM A8",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8/Oem/Dell/DellMemory/DIMM.Socket.A8",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "A",
                "Id": "DIMM.Socket.A8",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "19949A1F",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A8#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A8_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.A8",
                        "Id": "DIMM.Socket.A8#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A1F"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.A8#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.A8",
    "Name": "DIMM A8 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8/Oem/Dell/DellMemory/DIMM.Socket.A8

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.A8/Oem/Dell/DellMemory/DIMM.Socket.A8",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "A",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.A8",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM B1",
    "DeviceLocator": "DIMM B1",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.B1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM B1",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1/Oem/Dell/DellMemory/DIMM.Socket.B1",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "19949A25",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B1#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B1_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.B1",
                        "Id": "DIMM.Socket.B1#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A25"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.B1#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.B1",
    "Name": "DIMM B1 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1/Oem/Dell/DellMemory/DIMM.Socket.B1

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B1/Oem/Dell/DellMemory/DIMM.Socket.B1",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "B",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.B1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM B2",
    "DeviceLocator": "DIMM B2",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.B2",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM B2",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2/Oem/Dell/DellMemory/DIMM.Socket.B2",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B2",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "19949A23",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B2#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B2_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.B2",
                        "Id": "DIMM.Socket.B2#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A23"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.B2#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.B2",
    "Name": "DIMM B2 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2/Oem/Dell/DellMemory/DIMM.Socket.B2

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B2/Oem/Dell/DellMemory/DIMM.Socket.B2",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "B",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.B2",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM B3",
    "DeviceLocator": "DIMM B3",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.B3",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM B3",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3/Oem/Dell/DellMemory/DIMM.Socket.B3",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B3",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "1994CC0F",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B3#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B3_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.B3",
                        "Id": "DIMM.Socket.B3#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "1994CC0F"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.B3#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.B3",
    "Name": "DIMM B3 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3/Oem/Dell/DellMemory/DIMM.Socket.B3

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B3/Oem/Dell/DellMemory/DIMM.Socket.B3",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "B",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.B3",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM B4",
    "DeviceLocator": "DIMM B4",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.B4",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM B4",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4/Oem/Dell/DellMemory/DIMM.Socket.B4",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B4",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "19949A66",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B4#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B4_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.B4",
                        "Id": "DIMM.Socket.B4#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A66"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.B4#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.B4",
    "Name": "DIMM B4 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4/Oem/Dell/DellMemory/DIMM.Socket.B4

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B4/Oem/Dell/DellMemory/DIMM.Socket.B4",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "B",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.B4",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM B5",
    "DeviceLocator": "DIMM B5",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.B5",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM B5",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5/Oem/Dell/DellMemory/DIMM.Socket.B5",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B5",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "19949A52",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B5#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B5_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.B5",
                        "Id": "DIMM.Socket.B5#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A52"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.B5#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.B5",
    "Name": "DIMM B5 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5/Oem/Dell/DellMemory/DIMM.Socket.B5

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B5/Oem/Dell/DellMemory/DIMM.Socket.B5",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "B",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.B5",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM B6",
    "DeviceLocator": "DIMM B6",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.B6",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM B6",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6/Oem/Dell/DellMemory/DIMM.Socket.B6",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B6",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "1994CC0E",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B6#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B6_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.B6",
                        "Id": "DIMM.Socket.B6#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "1994CC0E"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.B6#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.B6",
    "Name": "DIMM B6 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6/Oem/Dell/DellMemory/DIMM.Socket.B6

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B6/Oem/Dell/DellMemory/DIMM.Socket.B6",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "B",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.B6",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM B7",
    "DeviceLocator": "DIMM B7",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.B7",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM B7",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7/Oem/Dell/DellMemory/DIMM.Socket.B7",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B7",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "1994BEBD",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B7#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B7_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.B7",
                        "Id": "DIMM.Socket.B7#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "1994BEBD"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.B7#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.B7",
    "Name": "DIMM B7 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7/Oem/Dell/DellMemory/DIMM.Socket.B7

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B7/Oem/Dell/DellMemory/DIMM.Socket.B7",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "B",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.B7",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8

```{
    "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8",
    "@odata.type": "#Memory.v1_9_2.Memory",
    "AllowedSpeedsMHz": [
        3200
    ],
    "AllowedSpeedsMHz@odata.count": 1,
    "Assembly": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8/Assembly"
    },
    "BaseModuleType": null,
    "BusWidthBits": 72,
    "CacheSizeMiB": 0,
    "CapacityMiB": 8192,
    "DataWidthBits": 64,
    "Description": "DIMM B8",
    "DeviceLocator": "DIMM B8",
    "ErrorCorrection": "MultiBitECC",
    "FirmwareRevision": null,
    "Id": "DIMM.Socket.B8",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "LogicalSizeMiB": 0,
    "Manufacturer": "Samsung",
    "MaxTDPMilliWatts": [],
    "MaxTDPMilliWatts@odata.count": 0,
    "MemoryDeviceType": "DDR4",
    "MemorySubsystemControllerManufacturerID": null,
    "MemorySubsystemControllerProductID": null,
    "MemoryType": "DRAM",
    "Metrics": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8/MemoryMetrics"
    },
    "ModuleManufacturerID": "0xce80",
    "ModuleProductID": null,
    "Name": "DIMM B8",
    "NonVolatileSizeMiB": 0,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellMemory": {
                "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8/Oem/Dell/DellMemory/DIMM.Socket.B8",
                "@odata.type": "#DellMemory.v1_1_0.DellMemory",
                "BankLabel": "B",
                "Id": "DIMM.Socket.B8",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
                "MemoryTechnology": "DRAM",
                "Model": "DDR4 DIMM",
                "Name": "DellMemory",
                "RemainingRatedWriteEndurancePercent": null,
                "SystemEraseCapability": "NotSupported"
            }
        }
    },
    "OperatingMemoryModes": [
        "Volatile"
    ],
    "OperatingMemoryModes@odata.count": 1,
    "OperatingSpeedMhz": 2933,
    "PartNumber": "M393A1K43DB2-CWE",
    "RankCount": 1,
    "SerialNumber": "19949A8A",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VolatileSizeMiB": 8192
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B8#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B8_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "DIMM.Socket.B8",
                        "Id": "DIMM.Socket.B8#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A8A"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "DIMM.Socket.B8#FRU"
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8/MemoryMetrics

```{
    "@odata.context": "/redfish/v1/$metadata#MemoryMetrics.MemoryMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8/MemoryMetrics",
    "@odata.type": "#MemoryMetrics.v1_3_0.MemoryMetrics",
    "Description": "Metrics of the memory device",
    "HealthData": {
        "AlarmTrips": {
            "AddressParityError": false,
            "CorrectableECCError": false,
            "SpareBlock": false,
            "Temperature": false,
            "UncorrectableECCError": false
        },
        "DataLossDetected": null,
        "PredictedMediaLifeLeftPercent": null
    },
    "Id": "DIMM.Socket.B8",
    "Name": "DIMM B8 Metrics",
    "OperatingSpeedMHz": 2933
}
```

## /redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8/Oem/Dell/DellMemory/DIMM.Socket.B8

```{
    "@odata.context": "/redfish/v1/$metadata#DellMemory.DellMemory",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory/DIMM.Socket.B8/Oem/Dell/DellMemory/DIMM.Socket.B8",
    "@odata.type": "#DellMemory.v1_1_0.DellMemory",
    "BankLabel": "B",
    "Description": "An instance of DellMemory will have Memory Device specific data.",
    "Id": "DIMM.Socket.B8",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "ManufactureDate": "Mon Apr 26 07:00:00 2021 UTC",
    "MemoryTechnology": "DRAM",
    "Model": "DDR4 DIMM",
    "Name": "DellMemory",
    "RemainingRatedWriteEndurancePercent": null,
    "SystemEraseCapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Settings",
    "@odata.type": "#NetworkDeviceFunction.v1_5_1.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-1"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 1,
    "Description": "NetworkDeviceFunction",
    "Ethernet": {},
    "FibreChannel": {
        "BootTargets": [
            {
                "LUNID": "0",
                "WWPN": "00:00:00:00:00:00:00:00"
            }
        ],
        "BootTargets@odata.count": 1,
        "FCoEActiveVLANId": null,
        "FCoELocalVLANId": null,
        "PermanentWWNN": "20:00:00:10:9B:5A:4A:58",
        "PermanentWWPN": "10:00:00:10:9B:5A:4A:58",
        "WWNN": "20:00:00:10:9B:5A:4A:58",
        "WWNSource": "ProvidedByFabric",
        "WWPN": "10:00:00:10:9B:5A:4A:58"
    },
    "Id": "FC.Slot.1-1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-1"
        }
    },
    "MaxVirtualFunctions": null,
    "Name": "NetworkDeviceFunction",
    "NetDevFuncCapabilities": [
        "Disabled",
        "FibreChannel"
    ],
    "NetDevFuncCapabilities@odata.count": 2,
    "NetDevFuncType": "FibreChannel",
    "PhysicalPortAssignment": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-1"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "iSCSIBoot": {}
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Settings",
    "@odata.type": "#NetworkDeviceFunction.v1_5_1.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-2"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 1,
    "Description": "NetworkDeviceFunction",
    "Ethernet": {},
    "FibreChannel": {
        "BootTargets": [
            {
                "LUNID": "0",
                "WWPN": "00:00:00:00:00:00:00:00"
            }
        ],
        "BootTargets@odata.count": 1,
        "FCoEActiveVLANId": null,
        "FCoELocalVLANId": null,
        "PermanentWWNN": "20:00:00:10:9B:5A:4A:59",
        "PermanentWWPN": "10:00:00:10:9B:5A:4A:59",
        "WWNN": "20:00:00:10:9B:5A:4A:59",
        "WWNSource": "ProvidedByFabric",
        "WWPN": "10:00:00:10:9B:5A:4A:59"
    },
    "Id": "FC.Slot.1-2",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-2"
        }
    },
    "MaxVirtualFunctions": null,
    "Name": "NetworkDeviceFunction",
    "NetDevFuncCapabilities": [
        "Disabled",
        "FibreChannel"
    ],
    "NetDevFuncCapabilities@odata.count": 2,
    "NetDevFuncType": "FibreChannel",
    "PhysicalPortAssignment": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-2"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "iSCSIBoot": {}
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNIC/NIC.Embedded.1-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellNIC.DellNIC",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNIC/NIC.Embedded.1-1-1",
    "@odata.type": "#DellNIC.v1_4_0.DellNIC",
    "BusNumber": 4,
    "CableLengthMetres": null,
    "ControllerBIOSVersion": "1.39",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellNIC will have NIC device specific data.",
    "DeviceDescription": "Embedded NIC 1 Port 1 Partition 1",
    "EFIVersion": "21.6.12",
    "FCoEOffloadMode": "Unknown",
    "FQDD": "NIC.Embedded.1-1-1",
    "FamilyVersion": "21.80.8",
    "Id": "NIC.Embedded.1-1-1",
    "IdentifierType": null,
    "InstanceID": "NIC.Embedded.1-1-1",
    "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
    "LastUpdateTime": "2021-07-14T03:23:00+00:00",
    "LinkDuplex": "Unknown",
    "MediaType": "Base T",
    "Name": "DellNIC",
    "NicMode": "Unknown",
    "PCIDeviceID": "165f",
    "PCISubDeviceID": "08ff",
    "PCISubVendorID": "1028",
    "PCIVendorID": "14e4",
    "PartNumber": null,
    "PermanentFCOEMACAddress": null,
    "PermanentiSCSIMACAddress": null,
    "ProductName": "Broadcom Gigabit Ethernet BCM5720 - 70:B5:E8:F0:25:52",
    "Protocol": "NIC",
    "Revision": null,
    "SNAPIState": "Disabled",
    "SNAPISupport": "NotAvailable",
    "SerialNumber": null,
    "SlotLength": "Unknown",
    "SlotType": "Unknown",
    "TransceiverPartNumber": null,
    "TransceiverSerialNumber": null,
    "TransceiverVendorName": null,
    "VPISupport": "NotAvailable",
    "VendorName": "Broadcom Corp",
    "iScsiOffloadMode": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNICCapabilities/NIC.Embedded.1-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellNICCapabilities.DellNICCapabilities",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNICCapabilities/NIC.Embedded.1-1-1",
    "@odata.type": "#DellNICCapabilities.v1_1_0.DellNICCapabilities",
    "BPESupport": "NotSupported",
    "CongestionNotification": "NotSupported",
    "Description": "An instance of DellNICCapabilities will have data specific to NIC and its port and partitions capabilities.",
    "ETS": "NotSupported",
    "EVBModesSupport": "NotSupported",
    "FCoEBootSupport": "NotSupported",
    "FCoEMaxIOsPerSession": 0,
    "FCoEMaxNPIVPerPort": 0,
    "FCoEMaxNumberExchanges": 0,
    "FCoEMaxNumberLogins": 0,
    "FCoEMaxNumberOfFCTargets": 0,
    "FCoEMaxNumberOutStandingCommands": 0,
    "FCoEOffloadSupport": "NotSupported",
    "FeatureLicensingSupport": "NotSupported",
    "FlexAddressingSupport": "Supported",
    "IPSecOffloadSupport": "NotSupported",
    "Id": "NIC.Embedded.1-1-1",
    "MACSecSupport": "NotSupported",
    "NWManagementPassThrough": "Supported",
    "Name": "DellNICCapabilities",
    "OSBMCManagementPassThrough": "Supported",
    "OnChipThermalSensor": "Supported",
    "OpenFlowSupport": "NotSupported",
    "PXEBootSupport": "Supported",
    "PartitionWOLSupport": "NotSupported",
    "PersistencePolicySupport": "Supported",
    "PriorityFlowControl": "NotSupported",
    "RDMASupport": "NotSupported",
    "RemotePHY": "NotSupported",
    "TCPChimneySupport": "NotSupported",
    "VEB": "NotSupported",
    "VEBVEPAMultiChannel": "NotSupported",
    "VEBVEPASingleChannel": "NotSupported",
    "VirtualLinkControl": "NotSupported",
    "iSCSIBootSupport": "NotSupported",
    "iSCSIOffloadSupport": "NotSupported",
    "uEFISupport": "Supported"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNICPortMetrics/NIC.Embedded.1-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellNICPortMetrics.DellNICPortMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNICPortMetrics/NIC.Embedded.1-1-1",
    "@odata.type": "#DellNICPortMetrics.v1_1_1.DellNICPortMetrics",
    "Description": "Represents the statistics of the NIC, NIC port, or partition.",
    "DiscardedPkts": 0,
    "FCCRCErrorCount": null,
    "FCOELinkFailures": null,
    "FCOEPktRxCount": null,
    "FCOEPktTxCount": null,
    "FCOERxPktDroppedCount": null,
    "FQDD": "NIC.Embedded.1-1-1",
    "LanFCSRxErrors": null,
    "LanUnicastPktRXCount": null,
    "LanUnicastPktTXCount": null,
    "OSDriverState": "Operational",
    "PartitionLinkStatus": null,
    "PartitionOSDriverState": null,
    "RDMARxTotalBytes": null,
    "RDMARxTotalPackets": null,
    "RDMATotalProtectionErrors": null,
    "RDMATotalProtocolErrors": null,
    "RDMATxTotalBytes": null,
    "RDMATxTotalPackets": null,
    "RDMATxTotalReadReqPkts": null,
    "RDMATxTotalSendPkts": null,
    "RDMATxTotalWritePkts": null,
    "RxBroadcast": 0,
    "RxBytes": 0,
    "RxErrorPktAlignmentErrors": 0,
    "RxErrorPktFCSErrors": 0,
    "RxFalseCarrierDetection": null,
    "RxJabberPkt": 0,
    "RxMutlicastPackets": 0,
    "RxPauseXOFFFrames": 0,
    "RxPauseXONFrames": 0,
    "RxRuntPkt": 0,
    "RxUnicastPackets": 0,
    "StartStatisticTime": "2022-08-30T17:01:47-05:00",
    "StatisticTime": "2022-10-26T15:50:35-05:00",
    "TxBroadcast": 0,
    "TxBytes": 0,
    "TxErrorPktExcessiveCollision": 0,
    "TxErrorPktLateCollision": 0,
    "TxErrorPktMultipleCollision": 0,
    "TxErrorPktSingleCollision": 0,
    "TxMutlicastPackets": 0,
    "TxPauseXOFFFrames": 0,
    "TxPauseXONFrames": 0,
    "TxUnicastPackets": 0
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Settings",
    "@odata.type": "#NetworkDeviceFunction.v1_5_1.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.1-1"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 1,
    "Description": "NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "70:B5:E8:F0:25:52",
        "MTUSize": null,
        "PermanentMACAddress": "70:B5:E8:F0:25:52",
        "VLAN": {
            "VLANEnable": false,
            "VLANId": 1
        }
    },
    "FibreChannel": {
        "BootTargets": [
            {
                "LUNID": null,
                "WWPN": null
            }
        ],
        "BootTargets@odata.count": 1,
        "FCoEActiveVLANId": null,
        "FCoELocalVLANId": null,
        "PermanentWWNN": null,
        "PermanentWWPN": null,
        "WWNN": null,
        "WWNSource": null,
        "WWPN": null
    },
    "Id": "NIC.Embedded.1-1-1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.1-1"
        }
    },
    "MaxVirtualFunctions": null,
    "Name": "NetworkDeviceFunction",
    "NetDevFuncCapabilities": [
        "Disabled",
        "Ethernet"
    ],
    "NetDevFuncCapabilities@odata.count": 2,
    "NetDevFuncType": "Ethernet",
    "PhysicalPortAssignment": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.1-1"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "iSCSIBoot": {}
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Settings",
    "@odata.type": "#NetworkDeviceFunction.v1_5_1.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.2-1"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 1,
    "Description": "NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "70:B5:E8:F0:25:53",
        "MTUSize": null,
        "PermanentMACAddress": "70:B5:E8:F0:25:53",
        "VLAN": {
            "VLANEnable": false,
            "VLANId": 1
        }
    },
    "FibreChannel": {
        "BootTargets": [
            {
                "LUNID": null,
                "WWPN": null
            }
        ],
        "BootTargets@odata.count": 1,
        "FCoEActiveVLANId": null,
        "FCoELocalVLANId": null,
        "PermanentWWNN": null,
        "PermanentWWPN": null,
        "WWNN": null,
        "WWNSource": null,
        "WWPN": null
    },
    "Id": "NIC.Embedded.2-1-1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.2-1"
        }
    },
    "MaxVirtualFunctions": null,
    "Name": "NetworkDeviceFunction",
    "NetDevFuncCapabilities": [
        "Disabled",
        "Ethernet"
    ],
    "NetDevFuncCapabilities@odata.count": 2,
    "NetDevFuncType": "Ethernet",
    "PhysicalPortAssignment": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.2-1"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "iSCSIBoot": {}
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.2/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNIC/NIC.Embedded.2-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellNIC.DellNIC",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.2/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNIC/NIC.Embedded.2-1-1",
    "@odata.type": "#DellNIC.v1_4_0.DellNIC",
    "BusNumber": 4,
    "CableLengthMetres": null,
    "ControllerBIOSVersion": "1.39",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellNIC will have NIC device specific data.",
    "DeviceDescription": "Embedded NIC 1 Port 2 Partition 1",
    "EFIVersion": "21.6.12",
    "FCoEOffloadMode": "Unknown",
    "FQDD": "NIC.Embedded.2-1-1",
    "FamilyVersion": "21.80.8",
    "Id": "NIC.Embedded.2-1-1",
    "IdentifierType": null,
    "InstanceID": "NIC.Embedded.2-1-1",
    "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
    "LastUpdateTime": "2021-07-02T22:29:07+00:00",
    "LinkDuplex": "Unknown",
    "MediaType": "Base T",
    "Name": "DellNIC",
    "NicMode": "Unknown",
    "PCIDeviceID": "165f",
    "PCISubDeviceID": "08ff",
    "PCISubVendorID": "1028",
    "PCIVendorID": "14e4",
    "PartNumber": null,
    "PermanentFCOEMACAddress": null,
    "PermanentiSCSIMACAddress": null,
    "ProductName": "Broadcom Gigabit Ethernet BCM5720 - 70:B5:E8:F0:25:53",
    "Protocol": "NIC",
    "Revision": null,
    "SNAPIState": "Disabled",
    "SNAPISupport": "NotAvailable",
    "SerialNumber": null,
    "SlotLength": "Unknown",
    "SlotType": "Unknown",
    "TransceiverPartNumber": null,
    "TransceiverSerialNumber": null,
    "TransceiverVendorName": null,
    "VPISupport": "NotAvailable",
    "VendorName": "Broadcom Corp",
    "iScsiOffloadMode": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.2/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNICCapabilities/NIC.Embedded.2-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellNICCapabilities.DellNICCapabilities",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.2/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNICCapabilities/NIC.Embedded.2-1-1",
    "@odata.type": "#DellNICCapabilities.v1_1_0.DellNICCapabilities",
    "BPESupport": "NotSupported",
    "CongestionNotification": "NotSupported",
    "Description": "An instance of DellNICCapabilities will have data specific to NIC and its port and partitions capabilities.",
    "ETS": "NotSupported",
    "EVBModesSupport": "NotSupported",
    "FCoEBootSupport": "NotSupported",
    "FCoEMaxIOsPerSession": 0,
    "FCoEMaxNPIVPerPort": 0,
    "FCoEMaxNumberExchanges": 0,
    "FCoEMaxNumberLogins": 0,
    "FCoEMaxNumberOfFCTargets": 0,
    "FCoEMaxNumberOutStandingCommands": 0,
    "FCoEOffloadSupport": "NotSupported",
    "FeatureLicensingSupport": "NotSupported",
    "FlexAddressingSupport": "Supported",
    "IPSecOffloadSupport": "NotSupported",
    "Id": "NIC.Embedded.2-1-1",
    "MACSecSupport": "NotSupported",
    "NWManagementPassThrough": "Supported",
    "Name": "DellNICCapabilities",
    "OSBMCManagementPassThrough": "Supported",
    "OnChipThermalSensor": "Supported",
    "OpenFlowSupport": "NotSupported",
    "PXEBootSupport": "Supported",
    "PartitionWOLSupport": "NotSupported",
    "PersistencePolicySupport": "Supported",
    "PriorityFlowControl": "NotSupported",
    "RDMASupport": "NotSupported",
    "RemotePHY": "NotSupported",
    "TCPChimneySupport": "NotSupported",
    "VEB": "NotSupported",
    "VEBVEPAMultiChannel": "NotSupported",
    "VEBVEPASingleChannel": "NotSupported",
    "VirtualLinkControl": "NotSupported",
    "iSCSIBootSupport": "NotSupported",
    "iSCSIOffloadSupport": "NotSupported",
    "uEFISupport": "Supported"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.2/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNICPortMetrics/NIC.Embedded.2-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellNICPortMetrics.DellNICPortMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.2/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNICPortMetrics/NIC.Embedded.2-1-1",
    "@odata.type": "#DellNICPortMetrics.v1_1_1.DellNICPortMetrics",
    "Description": "Represents the statistics of the NIC, NIC port, or partition.",
    "DiscardedPkts": 0,
    "FCCRCErrorCount": null,
    "FCOELinkFailures": null,
    "FCOEPktRxCount": null,
    "FCOEPktTxCount": null,
    "FCOERxPktDroppedCount": null,
    "FQDD": "NIC.Embedded.2-1-1",
    "LanFCSRxErrors": null,
    "LanUnicastPktRXCount": null,
    "LanUnicastPktTXCount": null,
    "OSDriverState": "Operational",
    "PartitionLinkStatus": null,
    "PartitionOSDriverState": null,
    "RDMARxTotalBytes": null,
    "RDMARxTotalPackets": null,
    "RDMATotalProtectionErrors": null,
    "RDMATotalProtocolErrors": null,
    "RDMATxTotalBytes": null,
    "RDMATxTotalPackets": null,
    "RDMATxTotalReadReqPkts": null,
    "RDMATxTotalSendPkts": null,
    "RDMATxTotalWritePkts": null,
    "RxBroadcast": 0,
    "RxBytes": 0,
    "RxErrorPktAlignmentErrors": 0,
    "RxErrorPktFCSErrors": 0,
    "RxFalseCarrierDetection": null,
    "RxJabberPkt": 0,
    "RxMutlicastPackets": 0,
    "RxPauseXOFFFrames": 0,
    "RxPauseXONFrames": 0,
    "RxRuntPkt": 0,
    "RxUnicastPackets": 0,
    "StartStatisticTime": "2022-08-30T17:01:47-05:00",
    "StatisticTime": "2022-10-26T15:50:35-05:00",
    "TxBroadcast": 0,
    "TxBytes": 0,
    "TxErrorPktExcessiveCollision": 0,
    "TxErrorPktLateCollision": 0,
    "TxErrorPktMultipleCollision": 0,
    "TxErrorPktSingleCollision": 0,
    "TxMutlicastPackets": 0,
    "TxPauseXOFFFrames": 0,
    "TxPauseXONFrames": 0,
    "TxUnicastPackets": 0
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNIC/NIC.Integrated.1-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellNIC.DellNIC",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNIC/NIC.Integrated.1-1-1",
    "@odata.type": "#DellNIC.v1_4_0.DellNIC",
    "BusNumber": 49,
    "CableLengthMetres": null,
    "ControllerBIOSVersion": null,
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellNIC will have NIC device specific data.",
    "DeviceDescription": "Integrated NIC 1 Port 1 Partition 1",
    "EFIVersion": "14.22.15",
    "FCoEOffloadMode": "Unknown",
    "FQDD": "NIC.Integrated.1-1-1",
    "FamilyVersion": "16.28.45.12",
    "Id": "NIC.Integrated.1-1-1",
    "IdentifierType": null,
    "InstanceID": "NIC.Integrated.1-1-1",
    "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
    "LastUpdateTime": "2022-08-04T16:53:47+00:00",
    "LinkDuplex": "FullDuplex",
    "MediaType": "SFF_CAGE",
    "Name": "DellNIC",
    "NicMode": "Enabled",
    "PCIDeviceID": "1017",
    "PCISubDeviceID": "0097",
    "PCISubVendorID": "15b3",
    "PCIVendorID": "15b3",
    "PartNumber": "04TRD3",
    "PermanentFCOEMACAddress": null,
    "PermanentiSCSIMACAddress": null,
    "ProductName": "Mellanox ConnectX-5 EN 25GbE Dual-port SFP28 Adapter - B8:CE:F6:94:F0:B8",
    "Protocol": "NIC,RDMA",
    "Revision": null,
    "SNAPIState": "Disabled",
    "SNAPISupport": "NotAvailable",
    "SerialNumber": "INJBNM414TJ0AL",
    "SlotLength": "Unknown",
    "SlotType": "Unknown",
    "TransceiverPartNumber": null,
    "TransceiverSerialNumber": null,
    "TransceiverVendorName": null,
    "VPISupport": "NotAvailable",
    "VendorName": "Mellanox Technologies, Inc.",
    "iScsiOffloadMode": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNICCapabilities/NIC.Integrated.1-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellNICCapabilities.DellNICCapabilities",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNICCapabilities/NIC.Integrated.1-1-1",
    "@odata.type": "#DellNICCapabilities.v1_1_0.DellNICCapabilities",
    "BPESupport": "NotSupported",
    "CongestionNotification": "Supported",
    "Description": "An instance of DellNICCapabilities will have data specific to NIC and its port and partitions capabilities.",
    "ETS": "Supported",
    "EVBModesSupport": "NotSupported",
    "FCoEBootSupport": "NotSupported",
    "FCoEMaxIOsPerSession": 0,
    "FCoEMaxNPIVPerPort": 0,
    "FCoEMaxNumberExchanges": 0,
    "FCoEMaxNumberLogins": 0,
    "FCoEMaxNumberOfFCTargets": 0,
    "FCoEMaxNumberOutStandingCommands": 0,
    "FCoEOffloadSupport": "NotSupported",
    "FeatureLicensingSupport": "NotSupported",
    "FlexAddressingSupport": "Supported",
    "IPSecOffloadSupport": "NotSupported",
    "Id": "NIC.Integrated.1-1-1",
    "MACSecSupport": "NotSupported",
    "NWManagementPassThrough": "Supported",
    "Name": "DellNICCapabilities",
    "OSBMCManagementPassThrough": "Supported",
    "OnChipThermalSensor": "Supported",
    "OpenFlowSupport": "NotSupported",
    "PXEBootSupport": "Supported",
    "PartitionWOLSupport": "NotSupported",
    "PersistencePolicySupport": "Supported",
    "PriorityFlowControl": "Supported",
    "RDMASupport": "Supported",
    "RemotePHY": "NotSupported",
    "TCPChimneySupport": "NotSupported",
    "VEB": "NotSupported",
    "VEBVEPAMultiChannel": "NotSupported",
    "VEBVEPASingleChannel": "NotSupported",
    "VirtualLinkControl": "NotSupported",
    "iSCSIBootSupport": "Supported",
    "iSCSIOffloadSupport": "NotSupported",
    "uEFISupport": "Supported"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNICPortMetrics/NIC.Integrated.1-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellNICPortMetrics.DellNICPortMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNICPortMetrics/NIC.Integrated.1-1-1",
    "@odata.type": "#DellNICPortMetrics.v1_1_1.DellNICPortMetrics",
    "Description": "Represents the statistics of the NIC, NIC port, or partition.",
    "DiscardedPkts": 0,
    "FCCRCErrorCount": null,
    "FCOELinkFailures": null,
    "FCOEPktRxCount": null,
    "FCOEPktTxCount": null,
    "FCOERxPktDroppedCount": null,
    "FQDD": "NIC.Integrated.1-1-1",
    "LanFCSRxErrors": null,
    "LanUnicastPktRXCount": null,
    "LanUnicastPktTXCount": null,
    "OSDriverState": "Operational",
    "PartitionLinkStatus": null,
    "PartitionOSDriverState": null,
    "RDMARxTotalBytes": 0,
    "RDMARxTotalPackets": 0,
    "RDMATotalProtectionErrors": null,
    "RDMATotalProtocolErrors": null,
    "RDMATxTotalBytes": 0,
    "RDMATxTotalPackets": 0,
    "RDMATxTotalReadReqPkts": null,
    "RDMATxTotalSendPkts": null,
    "RDMATxTotalWritePkts": null,
    "RxBroadcast": 4304449747,
    "RxBytes": 828323997018,
    "RxErrorPktAlignmentErrors": 0,
    "RxErrorPktFCSErrors": 0,
    "RxFalseCarrierDetection": 0,
    "RxJabberPkt": 0,
    "RxMutlicastPackets": 963469206,
    "RxPauseXOFFFrames": 0,
    "RxPauseXONFrames": 0,
    "RxRuntPkt": 0,
    "RxUnicastPackets": 969898405,
    "StartStatisticTime": "2022-08-30T17:01:47-05:00",
    "StatisticTime": "2022-10-26T15:50:45-05:00",
    "TxBroadcast": 82721,
    "TxBytes": 15381706231,
    "TxErrorPktExcessiveCollision": 0,
    "TxErrorPktLateCollision": 0,
    "TxErrorPktMultipleCollision": 0,
    "TxErrorPktSingleCollision": 0,
    "TxMutlicastPackets": 545996,
    "TxPauseXOFFFrames": 0,
    "TxPauseXONFrames": 0,
    "TxUnicastPackets": 25776787
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Settings",
    "@odata.type": "#NetworkDeviceFunction.v1_5_1.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-1"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 1,
    "Description": "NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "B8:CE:F6:94:F0:B8",
        "MTUSize": null,
        "PermanentMACAddress": "B8:CE:F6:94:F0:B8",
        "VLAN": {
            "VLANEnable": false,
            "VLANId": 1
        }
    },
    "FibreChannel": {
        "BootTargets": [
            {
                "LUNID": null,
                "WWPN": null
            }
        ],
        "BootTargets@odata.count": 1,
        "FCoEActiveVLANId": null,
        "FCoELocalVLANId": null,
        "PermanentWWNN": null,
        "PermanentWWPN": null,
        "WWNN": null,
        "WWNSource": null,
        "WWPN": null
    },
    "Id": "NIC.Integrated.1-1-1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-1"
        }
    },
    "MaxVirtualFunctions": 127,
    "Name": "NetworkDeviceFunction",
    "NetDevFuncCapabilities": [
        "Disabled",
        "Ethernet"
    ],
    "NetDevFuncCapabilities@odata.count": 2,
    "NetDevFuncType": "Ethernet",
    "PhysicalPortAssignment": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-1"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "iSCSIBoot": {
        "AuthenticationMethod": "None",
        "CHAPSecret": null,
        "CHAPUsername": null,
        "IPAddressType": "IPv4",
        "IPMaskDNSViaDHCP": false,
        "InitiatorDefaultGateway": "0.0.0.0",
        "InitiatorIPAddress": "0.0.0.0",
        "InitiatorName": null,
        "InitiatorNetmask": "0.0.0.0",
        "PrimaryDNS": "0.0.0.0",
        "PrimaryLUN": 0,
        "PrimaryTargetIPAddress": "0.0.0.0",
        "PrimaryTargetName": null,
        "PrimaryTargetTCPPort": 3260,
        "PrimaryVLANEnable": null,
        "PrimaryVLANId": null,
        "SecondaryDNS": null,
        "SecondaryLUN": null,
        "SecondaryTargetIPAddress": null,
        "SecondaryTargetName": null,
        "SecondaryTargetTCPPort": null,
        "SecondaryVLANEnable": null,
        "SecondaryVLANId": null,
        "TargetInfoViaDHCP": false
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNIC/NIC.Integrated.1-2-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellNIC.DellNIC",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNIC/NIC.Integrated.1-2-1",
    "@odata.type": "#DellNIC.v1_4_0.DellNIC",
    "BusNumber": 49,
    "CableLengthMetres": null,
    "ControllerBIOSVersion": null,
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellNIC will have NIC device specific data.",
    "DeviceDescription": "Integrated NIC 1 Port 2 Partition 1",
    "EFIVersion": "14.22.15",
    "FCoEOffloadMode": "Unknown",
    "FQDD": "NIC.Integrated.1-2-1",
    "FamilyVersion": "16.28.45.12",
    "Id": "NIC.Integrated.1-2-1",
    "IdentifierType": null,
    "InstanceID": "NIC.Integrated.1-2-1",
    "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
    "LastUpdateTime": "2022-08-04T16:53:47+00:00",
    "LinkDuplex": "FullDuplex",
    "MediaType": "SFF_CAGE",
    "Name": "DellNIC",
    "NicMode": "Enabled",
    "PCIDeviceID": "1017",
    "PCISubDeviceID": "0097",
    "PCISubVendorID": "15b3",
    "PCIVendorID": "15b3",
    "PartNumber": "04TRD3",
    "PermanentFCOEMACAddress": null,
    "PermanentiSCSIMACAddress": null,
    "ProductName": "Mellanox ConnectX-5 EN 25GbE Dual-port SFP28 Adapter - B8:CE:F6:94:F0:B9",
    "Protocol": "NIC,RDMA",
    "Revision": null,
    "SNAPIState": "Disabled",
    "SNAPISupport": "NotAvailable",
    "SerialNumber": "INJBNM414TJ0AL",
    "SlotLength": "Unknown",
    "SlotType": "Unknown",
    "TransceiverPartNumber": null,
    "TransceiverSerialNumber": null,
    "TransceiverVendorName": null,
    "VPISupport": "NotAvailable",
    "VendorName": "Mellanox Technologies, Inc.",
    "iScsiOffloadMode": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNICCapabilities/NIC.Integrated.1-2-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellNICCapabilities.DellNICCapabilities",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNICCapabilities/NIC.Integrated.1-2-1",
    "@odata.type": "#DellNICCapabilities.v1_1_0.DellNICCapabilities",
    "BPESupport": "NotSupported",
    "CongestionNotification": "Supported",
    "Description": "An instance of DellNICCapabilities will have data specific to NIC and its port and partitions capabilities.",
    "ETS": "Supported",
    "EVBModesSupport": "NotSupported",
    "FCoEBootSupport": "NotSupported",
    "FCoEMaxIOsPerSession": 0,
    "FCoEMaxNPIVPerPort": 0,
    "FCoEMaxNumberExchanges": 0,
    "FCoEMaxNumberLogins": 0,
    "FCoEMaxNumberOfFCTargets": 0,
    "FCoEMaxNumberOutStandingCommands": 0,
    "FCoEOffloadSupport": "NotSupported",
    "FeatureLicensingSupport": "NotSupported",
    "FlexAddressingSupport": "Supported",
    "IPSecOffloadSupport": "NotSupported",
    "Id": "NIC.Integrated.1-2-1",
    "MACSecSupport": "NotSupported",
    "NWManagementPassThrough": "Supported",
    "Name": "DellNICCapabilities",
    "OSBMCManagementPassThrough": "Supported",
    "OnChipThermalSensor": "Supported",
    "OpenFlowSupport": "NotSupported",
    "PXEBootSupport": "Supported",
    "PartitionWOLSupport": "NotSupported",
    "PersistencePolicySupport": "Supported",
    "PriorityFlowControl": "Supported",
    "RDMASupport": "Supported",
    "RemotePHY": "NotSupported",
    "TCPChimneySupport": "NotSupported",
    "VEB": "NotSupported",
    "VEBVEPAMultiChannel": "NotSupported",
    "VEBVEPASingleChannel": "NotSupported",
    "VirtualLinkControl": "NotSupported",
    "iSCSIBootSupport": "Supported",
    "iSCSIOffloadSupport": "NotSupported",
    "uEFISupport": "Supported"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNICPortMetrics/NIC.Integrated.1-2-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellNICPortMetrics.DellNICPortMetrics",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNICPortMetrics/NIC.Integrated.1-2-1",
    "@odata.type": "#DellNICPortMetrics.v1_1_1.DellNICPortMetrics",
    "Description": "Represents the statistics of the NIC, NIC port, or partition.",
    "DiscardedPkts": 0,
    "FCCRCErrorCount": null,
    "FCOELinkFailures": null,
    "FCOEPktRxCount": null,
    "FCOEPktTxCount": null,
    "FCOERxPktDroppedCount": null,
    "FQDD": "NIC.Integrated.1-2-1",
    "LanFCSRxErrors": null,
    "LanUnicastPktRXCount": null,
    "LanUnicastPktTXCount": null,
    "OSDriverState": "Operational",
    "PartitionLinkStatus": null,
    "PartitionOSDriverState": null,
    "RDMARxTotalBytes": 0,
    "RDMARxTotalPackets": 0,
    "RDMATotalProtectionErrors": null,
    "RDMATotalProtocolErrors": null,
    "RDMATxTotalBytes": 0,
    "RDMATxTotalPackets": 0,
    "RDMATxTotalReadReqPkts": null,
    "RDMATxTotalSendPkts": null,
    "RDMATxTotalWritePkts": null,
    "RxBroadcast": 3865711632,
    "RxBytes": 720933706011,
    "RxErrorPktAlignmentErrors": 0,
    "RxErrorPktFCSErrors": 0,
    "RxFalseCarrierDetection": 0,
    "RxJabberPkt": 0,
    "RxMutlicastPackets": 831027785,
    "RxPauseXOFFFrames": 0,
    "RxPauseXONFrames": 0,
    "RxRuntPkt": 0,
    "RxUnicastPackets": 855696971,
    "StartStatisticTime": "2022-08-30T17:01:47-05:00",
    "StatisticTime": "2022-10-26T15:50:40-05:00",
    "TxBroadcast": 1,
    "TxBytes": 14852656,
    "TxErrorPktExcessiveCollision": 0,
    "TxErrorPktLateCollision": 0,
    "TxErrorPktMultipleCollision": 0,
    "TxErrorPktSingleCollision": 0,
    "TxMutlicastPackets": 206286,
    "TxPauseXOFFFrames": 0,
    "TxPauseXONFrames": 0,
    "TxUnicastPackets": 0
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Settings",
    "@odata.type": "#NetworkDeviceFunction.v1_5_1.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-2"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 1,
    "Description": "NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "B8:CE:F6:94:F0:B9",
        "MTUSize": null,
        "PermanentMACAddress": "B8:CE:F6:94:F0:B9",
        "VLAN": {
            "VLANEnable": false,
            "VLANId": 1
        }
    },
    "FibreChannel": {
        "BootTargets": [
            {
                "LUNID": null,
                "WWPN": null
            }
        ],
        "BootTargets@odata.count": 1,
        "FCoEActiveVLANId": null,
        "FCoELocalVLANId": null,
        "PermanentWWNN": null,
        "PermanentWWPN": null,
        "WWNN": null,
        "WWNSource": null,
        "WWPN": null
    },
    "Id": "NIC.Integrated.1-2-1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-2"
        }
    },
    "MaxVirtualFunctions": 127,
    "Name": "NetworkDeviceFunction",
    "NetDevFuncCapabilities": [
        "Disabled",
        "Ethernet"
    ],
    "NetDevFuncCapabilities@odata.count": 2,
    "NetDevFuncType": "Ethernet",
    "PhysicalPortAssignment": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-2"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "iSCSIBoot": {
        "AuthenticationMethod": "None",
        "CHAPSecret": null,
        "CHAPUsername": null,
        "IPAddressType": "IPv4",
        "IPMaskDNSViaDHCP": false,
        "InitiatorDefaultGateway": "0.0.0.0",
        "InitiatorIPAddress": "0.0.0.0",
        "InitiatorName": null,
        "InitiatorNetmask": "0.0.0.0",
        "PrimaryDNS": "0.0.0.0",
        "PrimaryLUN": 0,
        "PrimaryTargetIPAddress": "0.0.0.0",
        "PrimaryTargetName": null,
        "PrimaryTargetTCPPort": 3260,
        "PrimaryVLANEnable": null,
        "PrimaryVLANId": null,
        "SecondaryDNS": null,
        "SecondaryLUN": null,
        "SecondaryTargetIPAddress": null,
        "SecondaryTargetName": null,
        "SecondaryTargetTCPPort": null,
        "SecondaryVLANEnable": null,
        "SecondaryVLANId": null,
        "TargetInfoViaDHCP": false
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkInterfaces",
    "@odata.type": "#NetworkInterfaceCollection.NetworkInterfaceCollection",
    "Description": "Collection Of Network Interface entities",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkInterfaces/NIC.Embedded.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkInterfaces/NIC.Integrated.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkInterfaces/FC.Slot.1"
        }
    ],
    "Members@odata.count": 3,
    "Name": "Network Interface Collection"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkInterfaces/FC.Slot.1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterface.NetworkInterface",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkInterfaces/FC.Slot.1",
    "@odata.type": "#NetworkInterface.v1_1_4.NetworkInterface",
    "Description": "Network Device View",
    "Id": "FC.Slot.1",
    "Links": {
        "NetworkAdapter": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1"
        }
    },
    "Name": "Network Device View",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkInterfaces/NIC.Embedded.1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterface.NetworkInterface",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkInterfaces/NIC.Embedded.1",
    "@odata.type": "#NetworkInterface.v1_1_4.NetworkInterface",
    "Description": "Network Device View",
    "Id": "NIC.Embedded.1",
    "Links": {
        "NetworkAdapter": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1"
        }
    },
    "Name": "Network Device View",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkInterfaces/NIC.Integrated.1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkInterface.NetworkInterface",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkInterfaces/NIC.Integrated.1",
    "@odata.type": "#NetworkInterface.v1_1_4.NetworkInterface",
    "Description": "Network Device View",
    "Id": "NIC.Integrated.1",
    "Links": {
        "NetworkAdapter": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1"
        }
    },
    "Name": "Network Device View",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections

```{
    "@odata.context": "/redfish/v1/$metadata#DellSwitchConnectionCollection.DellSwitchConnectionCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections",
    "@odata.type": "#DellSwitchConnectionCollection.DellSwitchConnectionCollection",
    "Description": "A collection of DellSwitchConnection resource",
    "Members": [
        {
            "@odata.context": "/redfish/v1/$metadata#DellSwitchConnection.DellSwitchConnection",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/iDRAC.Embedded.1",
            "@odata.type": "#DellSwitchConnection.v1_1_0.DellSwitchConnection",
            "Description": "An instance of DellSwitchConnection will have the switch connection view information of all the ports.",
            "FQDD": "iDRAC.Embedded.1",
            "Id": "iDRAC.Embedded.1",
            "InstanceID": "iDRAC.Embedded.1",
            "Name": "DellSwitchConnection",
            "StaleData": "NotStale",
            "SwitchConnectionID": "bc:26:c7:cf:ae:94",
            "SwitchPortConnectionID": "Ethernet1/23"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSwitchConnection.DellSwitchConnection",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/NIC.Embedded.1-1-1",
            "@odata.type": "#DellSwitchConnection.v1_1_0.DellSwitchConnection",
            "Description": "An instance of DellSwitchConnection will have the switch connection view information of all the ports.",
            "FQDD": "NIC.Embedded.1-1-1",
            "Id": "NIC.Embedded.1-1-1",
            "InstanceID": "NIC.Embedded.1-1-1",
            "Name": "DellSwitchConnection",
            "StaleData": "NotStale",
            "SwitchConnectionID": "No Link",
            "SwitchPortConnectionID": "No Link"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSwitchConnection.DellSwitchConnection",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/NIC.Embedded.2-1-1",
            "@odata.type": "#DellSwitchConnection.v1_1_0.DellSwitchConnection",
            "Description": "An instance of DellSwitchConnection will have the switch connection view information of all the ports.",
            "FQDD": "NIC.Embedded.2-1-1",
            "Id": "NIC.Embedded.2-1-1",
            "InstanceID": "NIC.Embedded.2-1-1",
            "Name": "DellSwitchConnection",
            "StaleData": "NotStale",
            "SwitchConnectionID": "No Link",
            "SwitchPortConnectionID": "No Link"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSwitchConnection.DellSwitchConnection",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/NIC.Integrated.1-1-1",
            "@odata.type": "#DellSwitchConnection.v1_1_0.DellSwitchConnection",
            "Description": "An instance of DellSwitchConnection will have the switch connection view information of all the ports.",
            "FQDD": "NIC.Integrated.1-1-1",
            "Id": "NIC.Integrated.1-1-1",
            "InstanceID": "NIC.Integrated.1-1-1",
            "Name": "DellSwitchConnection",
            "StaleData": "NotStale",
            "SwitchConnectionID": "bc:26:c7:cf:ae:94",
            "SwitchPortConnectionID": "Ethernet1/23"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSwitchConnection.DellSwitchConnection",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/NIC.Integrated.1-2-1",
            "@odata.type": "#DellSwitchConnection.v1_1_0.DellSwitchConnection",
            "Description": "An instance of DellSwitchConnection will have the switch connection view information of all the ports.",
            "FQDD": "NIC.Integrated.1-2-1",
            "Id": "NIC.Integrated.1-2-1",
            "InstanceID": "NIC.Integrated.1-2-1",
            "Name": "DellSwitchConnection",
            "StaleData": "NotStale",
            "SwitchConnectionID": "b0:8b:cf:bf:b2:ee",
            "SwitchPortConnectionID": "Ethernet1/23"
        }
    ],
    "Members@odata.count": 5,
    "Name": "DellSwitchConnectionCollection"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/NIC.Embedded.1-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellSwitchConnection.DellSwitchConnection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/NIC.Embedded.1-1-1",
    "@odata.type": "#DellSwitchConnection.v1_1_0.DellSwitchConnection",
    "Description": "An instance of DellSwitchConnection will have the switch connection view information of all the ports.",
    "FQDD": "NIC.Embedded.1-1-1",
    "Id": "NIC.Embedded.1-1-1",
    "InstanceID": "NIC.Embedded.1-1-1",
    "Name": "DellSwitchConnection",
    "StaleData": "NotStale",
    "SwitchConnectionID": "No Link",
    "SwitchPortConnectionID": "No Link"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/NIC.Embedded.2-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellSwitchConnection.DellSwitchConnection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/NIC.Embedded.2-1-1",
    "@odata.type": "#DellSwitchConnection.v1_1_0.DellSwitchConnection",
    "Description": "An instance of DellSwitchConnection will have the switch connection view information of all the ports.",
    "FQDD": "NIC.Embedded.2-1-1",
    "Id": "NIC.Embedded.2-1-1",
    "InstanceID": "NIC.Embedded.2-1-1",
    "Name": "DellSwitchConnection",
    "StaleData": "NotStale",
    "SwitchConnectionID": "No Link",
    "SwitchPortConnectionID": "No Link"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/NIC.Integrated.1-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellSwitchConnection.DellSwitchConnection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/NIC.Integrated.1-1-1",
    "@odata.type": "#DellSwitchConnection.v1_1_0.DellSwitchConnection",
    "Description": "An instance of DellSwitchConnection will have the switch connection view information of all the ports.",
    "FQDD": "NIC.Integrated.1-1-1",
    "Id": "NIC.Integrated.1-1-1",
    "InstanceID": "NIC.Integrated.1-1-1",
    "Name": "DellSwitchConnection",
    "StaleData": "NotStale",
    "SwitchConnectionID": "bc:26:c7:cf:ae:94",
    "SwitchPortConnectionID": "Ethernet1/23"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/NIC.Integrated.1-2-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellSwitchConnection.DellSwitchConnection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/NIC.Integrated.1-2-1",
    "@odata.type": "#DellSwitchConnection.v1_1_0.DellSwitchConnection",
    "Description": "An instance of DellSwitchConnection will have the switch connection view information of all the ports.",
    "FQDD": "NIC.Integrated.1-2-1",
    "Id": "NIC.Integrated.1-2-1",
    "InstanceID": "NIC.Integrated.1-2-1",
    "Name": "DellSwitchConnection",
    "StaleData": "NotStale",
    "SwitchConnectionID": "b0:8b:cf:bf:b2:ee",
    "SwitchPortConnectionID": "Ethernet1/23"
}
```

## /redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/iDRAC.Embedded.1

```{
    "@odata.context": "/redfish/v1/$metadata#DellSwitchConnection.DellSwitchConnection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections/iDRAC.Embedded.1",
    "@odata.type": "#DellSwitchConnection.v1_1_0.DellSwitchConnection",
    "Description": "An instance of DellSwitchConnection will have the switch connection view information of all the ports.",
    "FQDD": "iDRAC.Embedded.1",
    "Id": "iDRAC.Embedded.1",
    "InstanceID": "iDRAC.Embedded.1",
    "Name": "DellSwitchConnection",
    "StaleData": "NotStale",
    "SwitchConnectionID": "bc:26:c7:cf:ae:94",
    "SwitchPortConnectionID": "Ethernet1/23"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBIOSService

```{
    "@odata.context": "/redfish/v1/$metadata#DellBIOSService.DellBIOSService",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBIOSService",
    "@odata.type": "#DellBIOSService.v1_0_0.DellBIOSService",
    "Actions": {
        "#DellBIOSService.DeviceRecovery": {
            "Device@Redfish.AllowableValues": [
                "BIOS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBIOSService/Actions/DellBIOSService.DeviceRecovery"
        }
    },
    "Description": "The DellBIOSService resource provides some actions to support BIOS functionality.",
    "Id": "DellBIOSService",
    "Name": "DellBIOSService"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBootSources

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBootSources/Settings"
        },
        "SupportedApplyTimes": [
            "OnReset",
            "AtMaintenanceWindowStart",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#DellBootSources.DellBootSources",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBootSources",
    "@odata.type": "#DellBootSources.v1_0_0.DellBootSources",
    "AttributeRegistry": "DellBootSourcesRegistry.v1_1_0",
    "Attributes": {
        "UefiBootSeq": [
            {
                "Enabled": true,
                "Id": "BIOS.Setup.1-1#UefiBootSeq#AHCI.SL.6-2#706bb9a08c75fae537397178cede23a8",
                "Index": 0,
                "Name": "AHCI.SL.6-2"
            },
            {
                "Enabled": true,
                "Id": "BIOS.Setup.1-1#UefiBootSeq#NIC.PxeDevice.1-1#f7dbc53a281f0f61e8e4c4fb27008828",
                "Index": 1,
                "Name": "NIC.PxeDevice.1-1"
            }
        ]
    },
    "Description": "Boot Sources Current Settings",
    "Id": "DellBootSources",
    "Name": "Boot Sources Configuration Current Settings"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBootSources/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#DellBootSources.DellBootSources",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBootSources/Settings",
    "@odata.type": "#DellBootSources.v1_0_0.DellBootSources",
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellBootSources/Settings/Actions/DellManager.ClearPending"
        }
    },
    "AttributeRegistry": "DellBootSourcesRegistry.v1_1_0",
    "Attributes": {},
    "Description": "Boot Sources Pending Settings. These settings will be applied on next system reboot.",
    "Id": "Settings",
    "Name": "Boot Sources Configuration Pending Settings",
    "Oem": {
        "Dell": {
            "@odata.context": "/redfish/v1/$metadata#DellManager.DellManager",
            "@odata.type": "#DellManager.v1_1_0.DellManager",
            "Jobs": {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/Jobs"
            }
        }
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellGPUSensors

```{
    "@odata.context": "/redfish/v1/$metadata#DellGPUSensorCollection.DellGPUSensorCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellGPUSensors",
    "@odata.type": "#DellGPUSensorCollection.DellGPUSensorCollection",
    "Description": "A collection of DellGPUSensor resource",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "DellGPUSensorCollection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellMetricService

```{
    "@odata.context": "/redfish/v1/$metadata#DellMetricService.DellMetricService",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellMetricService",
    "@odata.type": "#DellMetricService.v1_1_0.DellMetricService",
    "Actions": {
        "#DellMetricService.ControlMetrics": {
            "MetricCollectionEnabled@Redfish.AllowableValues": [
                "Reset"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellMetricService/Actions/DellMetricService.ControlMetrics"
        },
        "#DellMetricService.ExportThermalHistory": {
            "FileType@Redfish.AllowableValues": [
                "CSV",
                "XML"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellMetricService/Actions/DellMetricService.ExportThermalHistory"
        }
    },
    "Description": "Provides the ability to manage metrics.",
    "Id": "DellMetricService",
    "Name": "DellMetricService"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensorCollection.DellNumericSensorCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors",
    "@odata.type": "#DellNumericSensorCollection.DellNumericSensorCollection",
    "Description": "A collection of DellNumericSensor resource",
    "Members": [
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_PS1Voltage",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 208.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#PS1Voltage",
            "ElementName": "PS1 Voltage 1",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_PS1Voltage",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Volts",
            "RequestedState": "NotApplicable",
            "SensorType": "Voltage",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_PS2Voltage",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 208.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#PS2Voltage",
            "ElementName": "PS2 Voltage 2",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_PS2Voltage",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Volts",
            "RequestedState": "NotApplicable",
            "SensorType": "Voltage",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardIOUsage",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 0.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#SystemBoardIOUsage",
            "ElementName": "System Board IO Usage",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_SystemBoardIOUsage",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": "IO Usage Statistics",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Percentage",
            "RequestedState": "NotApplicable",
            "SensorType": "Other",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": 101,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardMEMUsage",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 0.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#SystemBoardMEMUsage",
            "ElementName": "System Board MEM Usage",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_SystemBoardMEMUsage",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": "Memory Usage Statistics",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Percentage",
            "RequestedState": "NotApplicable",
            "SensorType": "Other",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": 101,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardSYSUsage",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 7.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#SystemBoardSYSUsage",
            "ElementName": "System Board SYS Usage",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_SystemBoardSYSUsage",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": "System Usage Statistics",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Percentage",
            "RequestedState": "NotApplicable",
            "SensorType": "Other",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": 101,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardCPUUsage",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 6.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#SystemBoardCPUUsage",
            "ElementName": "System Board CPU Usage",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_SystemBoardCPUUsage",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": "CPU Usage Statistics",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Percentage",
            "RequestedState": "NotApplicable",
            "SensorType": "Other",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": 101,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU1VCOREVR",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 1.79,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#CPU1VCOREVR",
            "ElementName": "CPU1 VCORE VR",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1VCOREVR",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Volts",
            "RequestedState": "NotApplicable",
            "SensorType": "Voltage",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU2VCOREVR",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 1.79,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#CPU2VCOREVR",
            "ElementName": "CPU2 VCORE VR",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2VCOREVR",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Volts",
            "RequestedState": "NotApplicable",
            "SensorType": "Voltage",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU1MEM0123VR",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 1.22,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#CPU1MEM0123VR",
            "ElementName": "CPU1 MEM0123 VR",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1MEM0123VR",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Volts",
            "RequestedState": "NotApplicable",
            "SensorType": "Voltage",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU1MEM4567VR",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 1.22,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#CPU1MEM4567VR",
            "ElementName": "CPU1 MEM4567 VR",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1MEM4567VR",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Volts",
            "RequestedState": "NotApplicable",
            "SensorType": "Voltage",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU2MEM0123VR",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 1.22,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#CPU2MEM0123VR",
            "ElementName": "CPU2 MEM0123 VR",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2MEM0123VR",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Volts",
            "RequestedState": "NotApplicable",
            "SensorType": "Voltage",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU2MEM4567VR",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 1.22,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#CPU2MEM4567VR",
            "ElementName": "CPU2 MEM4567 VR",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2MEM4567VR",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Volts",
            "RequestedState": "NotApplicable",
            "SensorType": "Voltage",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.1A",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 9000.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.1A",
            "ElementName": "System Board Fan1A",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.1A",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.2A",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 9000.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.2A",
            "ElementName": "System Board Fan2A",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.2A",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.3A",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 9240.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.3A",
            "ElementName": "System Board Fan3A",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.3A",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.4A",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 9000.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.4A",
            "ElementName": "System Board Fan4A",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.4A",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.1B",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 5400.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.1B",
            "ElementName": "System Board Fan1B",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.1B",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.2B",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 5520.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.2B",
            "ElementName": "System Board Fan2B",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.2B",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.3B",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 5520.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.3B",
            "ElementName": "System Board Fan3B",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.3B",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.4B",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 5400.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.4B",
            "ElementName": "System Board Fan4B",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.4B",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.1C",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 9240.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.1C",
            "ElementName": "System Board Fan1C",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.1C",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.2C",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 9120.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.2C",
            "ElementName": "System Board Fan2C",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.2C",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.3C",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 9120.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.3C",
            "ElementName": "System Board Fan3C",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.3C",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.4C",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 9120.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.4C",
            "ElementName": "System Board Fan4C",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.4C",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.1D",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 5400.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.1D",
            "ElementName": "System Board Fan1D",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.1D",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.2D",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 5400.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.2D",
            "ElementName": "System Board Fan2D",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.2D",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.3D",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 5400.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.3D",
            "ElementName": "System Board Fan3D",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.3D",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.4D",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 5400.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "0x17__Fan.Embedded.4D",
            "ElementName": "System Board Fan4D",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "0x17__Fan.Embedded.4D",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 480,
            "LowerThresholdNonCritical": 840,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "RPM",
            "RequestedState": "NotApplicable",
            "SensorType": "Tachometer",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU1Temp",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 570.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#CPU1Temp",
            "ElementName": "CPU1 Temp",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1Temp",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 30,
            "LowerThresholdNonCritical": null,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "DegreesC",
            "RequestedState": "NotApplicable",
            "SensorType": "Temperature",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": -1,
            "UpperThresholdCritical": 980,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU2Temp",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 530.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#CPU2Temp",
            "ElementName": "CPU2 Temp",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2Temp",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 30,
            "LowerThresholdNonCritical": null,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "DegreesC",
            "RequestedState": "NotApplicable",
            "SensorType": "Temperature",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": -1,
            "UpperThresholdCritical": 980,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardInletTemp",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 180.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#SystemBoardInletTemp",
            "ElementName": "System Board Inlet Temp",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_SystemBoardInletTemp",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": -70,
            "LowerThresholdNonCritical": 30,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "DegreesC",
            "RequestedState": "NotApplicable",
            "SensorType": "Temperature",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": -1,
            "UpperThresholdCritical": 420,
            "UpperThresholdNonCritical": 380,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardExhaustTemp",
            "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
            "CurrentReading": 340.0,
            "CurrentState": "Normal",
            "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
            "DeviceID": "iDRAC.Embedded.1#SystemBoardExhaustTemp",
            "ElementName": "System Board Exhaust Temp",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_SystemBoardExhaustTemp",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "LowerThresholdCritical": 30,
            "LowerThresholdNonCritical": 80,
            "Name": "DellNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "OtherSensorTypeDescription": null,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "DegreesC",
            "RequestedState": "NotApplicable",
            "SensorType": "Temperature",
            "SystemName": "system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": -1,
            "UpperThresholdCritical": 800,
            "UpperThresholdNonCritical": 750,
            "ValueFormulation": 2
        }
    ],
    "Members@odata.count": 32,
    "Name": "DellNumericSensorCollection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.1A

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.1A",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 9000.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.1A",
    "ElementName": "System Board Fan1A",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.1A",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.1B

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.1B",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 5400.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.1B",
    "ElementName": "System Board Fan1B",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.1B",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.1C

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.1C",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 9240.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.1C",
    "ElementName": "System Board Fan1C",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.1C",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.1D

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.1D",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 5400.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.1D",
    "ElementName": "System Board Fan1D",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.1D",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.2A

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.2A",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 9000.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.2A",
    "ElementName": "System Board Fan2A",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.2A",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.2B

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.2B",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 5520.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.2B",
    "ElementName": "System Board Fan2B",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.2B",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.2C

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.2C",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 9120.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.2C",
    "ElementName": "System Board Fan2C",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.2C",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.2D

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.2D",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 5400.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.2D",
    "ElementName": "System Board Fan2D",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.2D",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.3A

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.3A",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 9240.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.3A",
    "ElementName": "System Board Fan3A",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.3A",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.3B

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.3B",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 5520.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.3B",
    "ElementName": "System Board Fan3B",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.3B",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.3C

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.3C",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 9120.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.3C",
    "ElementName": "System Board Fan3C",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.3C",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.3D

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.3D",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 5400.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.3D",
    "ElementName": "System Board Fan3D",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.3D",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.4A

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.4A",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 9000.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.4A",
    "ElementName": "System Board Fan4A",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.4A",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.4B

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.4B",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 5400.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.4B",
    "ElementName": "System Board Fan4B",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.4B",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.4C

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.4C",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 9120.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.4C",
    "ElementName": "System Board Fan4C",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.4C",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.4D

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/0x17__Fan.Embedded.4D",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 5400.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "0x17__Fan.Embedded.4D",
    "ElementName": "System Board Fan4D",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "0x17__Fan.Embedded.4D",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 480,
    "LowerThresholdNonCritical": 840,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "RPM",
    "RequestedState": "NotApplicable",
    "SensorType": "Tachometer",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU1MEM0123VR

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU1MEM0123VR",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 1.22,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#CPU1MEM0123VR",
    "ElementName": "CPU1 MEM0123 VR",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1MEM0123VR",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Volts",
    "RequestedState": "NotApplicable",
    "SensorType": "Voltage",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU1MEM4567VR

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU1MEM4567VR",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 1.22,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#CPU1MEM4567VR",
    "ElementName": "CPU1 MEM4567 VR",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1MEM4567VR",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Volts",
    "RequestedState": "NotApplicable",
    "SensorType": "Voltage",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU1Temp

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU1Temp",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 570.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#CPU1Temp",
    "ElementName": "CPU1 Temp",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1Temp",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 30,
    "LowerThresholdNonCritical": null,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "DegreesC",
    "RequestedState": "NotApplicable",
    "SensorType": "Temperature",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": -1,
    "UpperThresholdCritical": 980,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU1VCOREVR

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU1VCOREVR",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 1.79,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#CPU1VCOREVR",
    "ElementName": "CPU1 VCORE VR",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1VCOREVR",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Volts",
    "RequestedState": "NotApplicable",
    "SensorType": "Voltage",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU2MEM0123VR

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU2MEM0123VR",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 1.22,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#CPU2MEM0123VR",
    "ElementName": "CPU2 MEM0123 VR",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2MEM0123VR",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Volts",
    "RequestedState": "NotApplicable",
    "SensorType": "Voltage",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU2MEM4567VR

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU2MEM4567VR",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 1.22,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#CPU2MEM4567VR",
    "ElementName": "CPU2 MEM4567 VR",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2MEM4567VR",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Volts",
    "RequestedState": "NotApplicable",
    "SensorType": "Voltage",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU2Temp

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU2Temp",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 530.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#CPU2Temp",
    "ElementName": "CPU2 Temp",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2Temp",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 30,
    "LowerThresholdNonCritical": null,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "DegreesC",
    "RequestedState": "NotApplicable",
    "SensorType": "Temperature",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": -1,
    "UpperThresholdCritical": 980,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU2VCOREVR

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_CPU2VCOREVR",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 1.79,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#CPU2VCOREVR",
    "ElementName": "CPU2 VCORE VR",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2VCOREVR",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Volts",
    "RequestedState": "NotApplicable",
    "SensorType": "Voltage",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_PS1Voltage

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_PS1Voltage",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 208.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#PS1Voltage",
    "ElementName": "PS1 Voltage 1",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_PS1Voltage",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Volts",
    "RequestedState": "NotApplicable",
    "SensorType": "Voltage",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_PS2Voltage

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_PS2Voltage",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 208.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#PS2Voltage",
    "ElementName": "PS2 Voltage 2",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_PS2Voltage",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Volts",
    "RequestedState": "NotApplicable",
    "SensorType": "Voltage",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardCPUUsage

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardCPUUsage",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 6.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#SystemBoardCPUUsage",
    "ElementName": "System Board CPU Usage",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_SystemBoardCPUUsage",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": "CPU Usage Statistics",
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Percentage",
    "RequestedState": "NotApplicable",
    "SensorType": "Other",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": 101,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardExhaustTemp

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardExhaustTemp",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 340.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#SystemBoardExhaustTemp",
    "ElementName": "System Board Exhaust Temp",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_SystemBoardExhaustTemp",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": 30,
    "LowerThresholdNonCritical": 80,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "DegreesC",
    "RequestedState": "NotApplicable",
    "SensorType": "Temperature",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": -1,
    "UpperThresholdCritical": 800,
    "UpperThresholdNonCritical": 750,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardIOUsage

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardIOUsage",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 0.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#SystemBoardIOUsage",
    "ElementName": "System Board IO Usage",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_SystemBoardIOUsage",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": "IO Usage Statistics",
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Percentage",
    "RequestedState": "NotApplicable",
    "SensorType": "Other",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": 101,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardInletTemp

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardInletTemp",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 180.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#SystemBoardInletTemp",
    "ElementName": "System Board Inlet Temp",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_SystemBoardInletTemp",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": -70,
    "LowerThresholdNonCritical": 30,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": null,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "DegreesC",
    "RequestedState": "NotApplicable",
    "SensorType": "Temperature",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": -1,
    "UpperThresholdCritical": 420,
    "UpperThresholdNonCritical": 380,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardMEMUsage

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardMEMUsage",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 0.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#SystemBoardMEMUsage",
    "ElementName": "System Board MEM Usage",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_SystemBoardMEMUsage",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": "Memory Usage Statistics",
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Percentage",
    "RequestedState": "NotApplicable",
    "SensorType": "Other",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": 101,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardSYSUsage

```{
    "@odata.context": "/redfish/v1/$metadata#DellNumericSensor.DellNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardSYSUsage",
    "@odata.type": "#DellNumericSensor.v1_1_1.DellNumericSensor",
    "CurrentReading": 7.0,
    "CurrentState": "Normal",
    "Description": "An instance of DellNumericSensor will have data specific to sensor devices that returns only numeric readings and optionally supports thresholds settings.",
    "DeviceID": "iDRAC.Embedded.1#SystemBoardSYSUsage",
    "ElementName": "System Board SYS Usage",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_SystemBoardSYSUsage",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "OtherSensorTypeDescription": "System Usage Statistics",
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Percentage",
    "RequestedState": "NotApplicable",
    "SensorType": "Other",
    "SystemName": "system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": 101,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService

```{
    "@odata.context": "/redfish/v1/$metadata#DellOSDeploymentService.DellOSDeploymentService",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService",
    "@odata.type": "#DellOSDeploymentService.v1_1_0.DellOSDeploymentService",
    "Actions": {
        "#DellOSDeploymentService.BootToHD": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.BootToHD"
        },
        "#DellOSDeploymentService.BootToISOFromVFlash": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.BootToISOFromVFlash"
        },
        "#DellOSDeploymentService.BootToNetworkISO": {
            "HashType@Redfish.AllowableValues": [
                "MD5",
                "SHA1"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.BootToNetworkISO"
        },
        "#DellOSDeploymentService.ConfigurableBootToNetworkISO": {
            "HashType@Redfish.AllowableValues": [
                "MD5",
                "SHA1"
            ],
            "ResetType@Redfish.AllowableValues": [
                "ColdReset",
                "NoReset",
                "WarmReset"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.ConfigurableBootToNetworkISO"
        },
        "#DellOSDeploymentService.ConnectNetworkISOImage": {
            "HashType@Redfish.AllowableValues": [
                "MD5",
                "SHA1"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.ConnectNetworkISOImage"
        },
        "#DellOSDeploymentService.DeleteISOFromVFlash": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.DeleteISOFromVFlash"
        },
        "#DellOSDeploymentService.DetachDrivers": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.DetachDrivers"
        },
        "#DellOSDeploymentService.DetachISOFromVFlash": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.DetachISOFromVFlash"
        },
        "#DellOSDeploymentService.DetachISOImage": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.DetachISOImage"
        },
        "#DellOSDeploymentService.DisconnectNetworkISOImage": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.DisconnectNetworkISOImage"
        },
        "#DellOSDeploymentService.DownloadISOToVFlash": {
            "HashType@Redfish.AllowableValues": [
                "MD5",
                "SHA1"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS",
                "TFTP"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.DownloadISOToVFlash"
        },
        "#DellOSDeploymentService.GetAttachStatus": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.GetAttachStatus"
        },
        "#DellOSDeploymentService.GetDriverPackInfo": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.GetDriverPackInfo"
        },
        "#DellOSDeploymentService.GetNetworkISOImageConnectionInfo": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.GetNetworkISOImageConnectionInfo"
        },
        "#DellOSDeploymentService.SkipISOImageBoot": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.SkipISOImageBoot"
        },
        "#DellOSDeploymentService.UnpackAndAttach": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.UnpackAndAttach"
        },
        "#DellOSDeploymentService.UnpackAndShare": {
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellOSDeploymentService/Actions/DellOSDeploymentService.UnpackAndShare"
        }
    },
    "Description": "The DellOSDeploymentService resource provides some actions to support OS deployment configurations.",
    "Id": "DellOSDeploymentService",
    "Name": "DellOSDeploymentService"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors

```{
    "@odata.context": "/redfish/v1/$metadata#DellPSNumericSensorCollection.DellPSNumericSensorCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors",
    "@odata.type": "#DellPSNumericSensorCollection.DellPSNumericSensorCollection",
    "Description": "A collection of DellPSNumericSensor resource",
    "Members": [
        {
            "@odata.context": "/redfish/v1/$metadata#DellPSNumericSensor.DellPSNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors/iDRAC.Embedded.1_0x23_PS1Current1",
            "@odata.type": "#DellPSNumericSensor.v1_1_0.DellPSNumericSensor",
            "CurrentReading": 18,
            "CurrentState": "Normal",
            "Description": "An instance of DellPSNumericSensor will have data specific to a power sensor device that returns only numeric readings and optionally supports of thresholds settings.",
            "ElementName": "PS1 Current 1",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_PS1Current1",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                },
                "DellPowerSupplyCollection": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupply/PSU.Slot.1"
                    }
                ],
                "DellPowerSupplyCollection@odata.count": 1
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellPSNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Amps",
            "RequestedState": "NotApplicable",
            "Resolution": 1,
            "SensorType": "PowerConsumption",
            "SystemName": "srv:system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": -1,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellPSNumericSensor.DellPSNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors/iDRAC.Embedded.1_0x23_PS2Current2",
            "@odata.type": "#DellPSNumericSensor.v1_1_0.DellPSNumericSensor",
            "CurrentReading": 2,
            "CurrentState": "Normal",
            "Description": "An instance of DellPSNumericSensor will have data specific to a power sensor device that returns only numeric readings and optionally supports of thresholds settings.",
            "ElementName": "PS2 Current 2",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_PS2Current2",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                },
                "DellPowerSupplyCollection": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupply/PSU.Slot.2"
                    }
                ],
                "DellPowerSupplyCollection@odata.count": 1
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellPSNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Amps",
            "RequestedState": "NotApplicable",
            "Resolution": 1,
            "SensorType": "PowerConsumption",
            "SystemName": "srv:system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": -1,
            "UpperThresholdCritical": null,
            "UpperThresholdNonCritical": null,
            "ValueFormulation": 2
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellPSNumericSensor.DellPSNumericSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardPwrConsumption",
            "@odata.type": "#DellPSNumericSensor.v1_1_0.DellPSNumericSensor",
            "CurrentReading": 384,
            "CurrentState": "Normal",
            "Description": "An instance of DellPSNumericSensor will have data specific to a power sensor device that returns only numeric readings and optionally supports of thresholds settings.",
            "ElementName": "System Board Pwr Consumption",
            "EnabledDefault": "Enabled",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_SystemBoardPwrConsumption",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                },
                "DellPowerSupplyCollection": [],
                "DellPowerSupplyCollection@odata.count": 0
            },
            "LowerThresholdCritical": null,
            "LowerThresholdNonCritical": null,
            "Name": "DellPSNumericSensor",
            "OperationalStatus": [
                "OK"
            ],
            "OperationalStatus@odata.count": 1,
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "PrimaryStatus": "OK",
            "RateUnits": "None",
            "ReadingUnits": "Watts",
            "RequestedState": "NotApplicable",
            "Resolution": 1,
            "SensorType": "PowerConsumption",
            "SystemName": "srv:system",
            "TransitioningToState": "NotApplicable",
            "UnitModifier": 0,
            "UpperThresholdCritical": 1656,
            "UpperThresholdNonCritical": 1512,
            "ValueFormulation": 2
        }
    ],
    "Members@odata.count": 3,
    "Name": "DellPSNumericSensorCollection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors/iDRAC.Embedded.1_0x23_PS1Current1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPSNumericSensor.DellPSNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors/iDRAC.Embedded.1_0x23_PS1Current1",
    "@odata.type": "#DellPSNumericSensor.v1_1_0.DellPSNumericSensor",
    "CurrentReading": 18,
    "CurrentState": "Normal",
    "Description": "An instance of DellPSNumericSensor will have data specific to a power sensor device that returns only numeric readings and optionally supports of thresholds settings.",
    "ElementName": "PS1 Current 1",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_PS1Current1",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        },
        "DellPowerSupplyCollection": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupply/PSU.Slot.1"
            }
        ],
        "DellPowerSupplyCollection@odata.count": 1
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellPSNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Amps",
    "RequestedState": "NotApplicable",
    "Resolution": 1,
    "SensorType": "PowerConsumption",
    "SystemName": "srv:system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": -1,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors/iDRAC.Embedded.1_0x23_PS2Current2

```{
    "@odata.context": "/redfish/v1/$metadata#DellPSNumericSensor.DellPSNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors/iDRAC.Embedded.1_0x23_PS2Current2",
    "@odata.type": "#DellPSNumericSensor.v1_1_0.DellPSNumericSensor",
    "CurrentReading": 2,
    "CurrentState": "Normal",
    "Description": "An instance of DellPSNumericSensor will have data specific to a power sensor device that returns only numeric readings and optionally supports of thresholds settings.",
    "ElementName": "PS2 Current 2",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_PS2Current2",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        },
        "DellPowerSupplyCollection": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupply/PSU.Slot.2"
            }
        ],
        "DellPowerSupplyCollection@odata.count": 1
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellPSNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Amps",
    "RequestedState": "NotApplicable",
    "Resolution": 1,
    "SensorType": "PowerConsumption",
    "SystemName": "srv:system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": -1,
    "UpperThresholdCritical": null,
    "UpperThresholdNonCritical": null,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardPwrConsumption

```{
    "@odata.context": "/redfish/v1/$metadata#DellPSNumericSensor.DellPSNumericSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors/iDRAC.Embedded.1_0x23_SystemBoardPwrConsumption",
    "@odata.type": "#DellPSNumericSensor.v1_1_0.DellPSNumericSensor",
    "CurrentReading": 384,
    "CurrentState": "Normal",
    "Description": "An instance of DellPSNumericSensor will have data specific to a power sensor device that returns only numeric readings and optionally supports of thresholds settings.",
    "ElementName": "System Board Pwr Consumption",
    "EnabledDefault": "Enabled",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_SystemBoardPwrConsumption",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        },
        "DellPowerSupplyCollection": [],
        "DellPowerSupplyCollection@odata.count": 0
    },
    "LowerThresholdCritical": null,
    "LowerThresholdNonCritical": null,
    "Name": "DellPSNumericSensor",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "PossibleStates": [
        "Unknown",
        "Fatal",
        "Normal",
        "Upper Fatal",
        "Upper Critical",
        "Upper Non-Critical",
        "Lower Non-Critical",
        "Lower Critical",
        "Lower Fatal"
    ],
    "PossibleStates@odata.count": 9,
    "PrimaryStatus": "OK",
    "RateUnits": "None",
    "ReadingUnits": "Watts",
    "RequestedState": "NotApplicable",
    "Resolution": 1,
    "SensorType": "PowerConsumption",
    "SystemName": "srv:system",
    "TransitioningToState": "NotApplicable",
    "UnitModifier": 0,
    "UpperThresholdCritical": 1656,
    "UpperThresholdNonCritical": 1512,
    "ValueFormulation": 2
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPresenceAndStatusSensors

```{
    "@odata.context": "/redfish/v1/$metadata#DellPresenceAndStatusSensorCollection.DellPresenceAndStatusSensorCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPresenceAndStatusSensors",
    "@odata.type": "#DellPresenceAndStatusSensorCollection.DellPresenceAndStatusSensorCollection",
    "Description": "A collection of DellPresenceAndStatusSensor resource",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "DellPresenceAndStatusSensorCollection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService

```{
    "@odata.context": "/redfish/v1/$metadata#DellRaidService.DellRaidService",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService",
    "@odata.type": "#DellRaidService.v1_4_0.DellRaidService",
    "Actions": {
        "#DellRaidService.AssignSpare": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.AssignSpare"
        },
        "#DellRaidService.BlinkTarget": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.BlinkTarget"
        },
        "#DellRaidService.CancelBackgroundInitialization": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.CancelBackgroundInitialization"
        },
        "#DellRaidService.CancelCheckConsistency": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.CancelCheckConsistency"
        },
        "#DellRaidService.CancelRebuildPhysicalDisk": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.CancelRebuildPhysicalDisk"
        },
        "#DellRaidService.ChangePDState": {
            "State@Redfish.AllowableValues": [
                "Offline",
                "Online"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ChangePDState"
        },
        "#DellRaidService.CheckVDValues": {
            "VDPropNameArrayIn@Redfish.AllowableValues": [
                "RAIDLevel",
                "Size",
                "SpanDepth",
                "SpanLength",
                "StartingLBA",
                "T10PIStatus"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.CheckVDValues"
        },
        "#DellRaidService.ClearControllerPreservedCache": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ClearControllerPreservedCache"
        },
        "#DellRaidService.ClearForeignConfig": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ClearForeignConfig"
        },
        "#DellRaidService.ConvertToNonRAID": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ConvertToNonRAID"
        },
        "#DellRaidService.ConvertToRAID": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ConvertToRAID"
        },
        "#DellRaidService.CryptographicEraseWithPSID": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.CryptographicEraseWithPSID"
        },
        "#DellRaidService.DisableSecurity": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.DisableSecurity"
        },
        "#DellRaidService.EnableControllerEncryption": {
            "Mode@Redfish.AllowableValues": [
                "DKM",
                "LKM",
                "LKM_TO_SEKM",
                "SEKM"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.EnableControllerEncryption"
        },
        "#DellRaidService.EnableSecurity": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.EnableSecurity"
        },
        "#DellRaidService.GetAvailableDisks": {
            "BlockSizeInBytes@Redfish.AllowableValues": [
                "4096",
                "512",
                "All"
            ],
            "DiskEncrypt@Redfish.AllowableValues": [
                "All",
                "FDE",
                "NonFDE"
            ],
            "DiskType@Redfish.AllowableValues": [
                "All",
                "HDD",
                "SSD"
            ],
            "Diskprotocol@Redfish.AllowableValues": [
                "AllProtocols",
                "NVMe",
                "SAS",
                "SATA"
            ],
            "FormFactor@Redfish.AllowableValues": [
                "All",
                "M.2"
            ],
            "RaidLevel@Redfish.AllowableValues": [
                "NoRAID",
                "RAID0",
                "RAID1",
                "RAID10",
                "RAID5",
                "RAID50",
                "RAID6",
                "RAID60"
            ],
            "T10PIStatus@Redfish.AllowableValues": [
                "All",
                "T10PICapable",
                "T10PIIncapable"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.GetAvailableDisks"
        },
        "#DellRaidService.GetDHSDisks": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.GetDHSDisks"
        },
        "#DellRaidService.GetRAIDLevels": {
            "BlockSizeInBytes@Redfish.AllowableValues": [
                "4096",
                "512",
                "All"
            ],
            "DiskEncrypt@Redfish.AllowableValues": [
                "All",
                "FDE",
                "NonFDE"
            ],
            "DiskType@Redfish.AllowableValues": [
                "All",
                "HDD",
                "SSD"
            ],
            "Diskprotocol@Redfish.AllowableValues": [
                "AllProtocols",
                "NVMe",
                "SAS",
                "SATA"
            ],
            "FormFactor@Redfish.AllowableValues": [
                "All",
                "M.2"
            ],
            "T10PIStatus@Redfish.AllowableValues": [
                "All",
                "T10PICapable",
                "T10PIIncapable"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.GetRAIDLevels"
        },
        "#DellRaidService.ImportForeignConfig": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ImportForeignConfig"
        },
        "#DellRaidService.LockVirtualDisk": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.LockVirtualDisk"
        },
        "#DellRaidService.OnlineCapacityExpansion": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.OnlineCapacityExpansion"
        },
        "#DellRaidService.PrepareToRemove": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.PrepareToRemove"
        },
        "#DellRaidService.RAIDLevelMigration": {
            "NewRaidLevel@Redfish.AllowableValues": [
                "NoRAID",
                "RAID0",
                "RAID1",
                "RAID10",
                "RAID5",
                "RAID50",
                "RAID6",
                "RAID60"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.RAIDLevelMigration"
        },
        "#DellRaidService.ReKey": {
            "Mode@Redfish.AllowableValues": [
                "LKM",
                "SEKM"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ReKey"
        },
        "#DellRaidService.RebuildPhysicalDisk": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.RebuildPhysicalDisk"
        },
        "#DellRaidService.RemoveControllerKey": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.RemoveControllerKey"
        },
        "#DellRaidService.RenameVD": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.RenameVD"
        },
        "#DellRaidService.ReplacePhysicalDisk": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ReplacePhysicalDisk"
        },
        "#DellRaidService.ResetConfig": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.ResetConfig"
        },
        "#DellRaidService.SetAssetName": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.SetAssetName"
        },
        "#DellRaidService.SetBootVD": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.SetBootVD"
        },
        "#DellRaidService.SetControllerKey": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.SetControllerKey"
        },
        "#DellRaidService.StartPatrolRead": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.StartPatrolRead"
        },
        "#DellRaidService.StopPatrolRead": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.StopPatrolRead"
        },
        "#DellRaidService.UnBlinkTarget": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.UnBlinkTarget"
        },
        "#DellRaidService.UnLockSecureForeignConfig": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.UnLockSecureForeignConfig"
        },
        "#DellRaidService.UnassignSpare": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRaidService/Actions/DellRaidService.UnassignSpare"
        }
    },
    "Description": "The DellRaidService resource provides some actions to support RAID functionality.",
    "Id": "DellRaidService",
    "Name": "DellRaidService"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus

```{
    "@odata.context": "/redfish/v1/$metadata#DellRollupStatusCollection.DellRollupStatusCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus",
    "@odata.type": "#DellRollupStatusCollection.DellRollupStatusCollection",
    "Description": "A collection of DellRollupStatus resource",
    "Members": [
        {
            "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Current",
            "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
            "CollectionName": "CurrentRollupStatus",
            "Description": "Represents the subcomponent roll-up statuses.",
            "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Current",
            "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Current",
            "Name": "DellRollupStatus",
            "RollupStatus": "Ok",
            "SubSystem": "Current"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Voltage",
            "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
            "CollectionName": "VoltageRollupStatus",
            "Description": "Represents the subcomponent roll-up statuses.",
            "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Voltage",
            "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Voltage",
            "Name": "DellRollupStatus",
            "RollupStatus": "Ok",
            "SubSystem": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Intrusion",
            "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
            "CollectionName": "IntrusionRollupStatus",
            "Description": "Represents the subcomponent roll-up statuses.",
            "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Intrusion",
            "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Intrusion",
            "Name": "DellRollupStatus",
            "RollupStatus": "Ok",
            "SubSystem": "Intrusion"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Processor",
            "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
            "CollectionName": "ProcessorRollupStatus",
            "Description": "Represents the subcomponent roll-up statuses.",
            "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Processor",
            "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Processor",
            "Name": "DellRollupStatus",
            "RollupStatus": "Ok",
            "SubSystem": "Processor"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_PowerSupply",
            "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
            "CollectionName": "PowerSupplyRollupStatus",
            "Description": "Represents the subcomponent roll-up statuses.",
            "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_PowerSupply",
            "InstanceID": "iDRAC.Embedded.1#SubSystem.1#PowerSupply",
            "Name": "DellRollupStatus",
            "RollupStatus": "Ok",
            "SubSystem": "PowerSupply"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Memory",
            "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
            "CollectionName": "MemoryRollupStatus",
            "Description": "Represents the subcomponent roll-up statuses.",
            "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Memory",
            "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Memory",
            "Name": "DellRollupStatus",
            "RollupStatus": "Ok",
            "SubSystem": "Memory"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Fan",
            "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
            "CollectionName": "FanRollupStatus",
            "Description": "Represents the subcomponent roll-up statuses.",
            "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Fan",
            "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Fan",
            "Name": "DellRollupStatus",
            "RollupStatus": "Ok",
            "SubSystem": "Fan"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Temperature",
            "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
            "CollectionName": "TemperatureRollupStatus",
            "Description": "Represents the subcomponent roll-up statuses.",
            "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Temperature",
            "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Temperature",
            "Name": "DellRollupStatus",
            "RollupStatus": "Ok",
            "SubSystem": "Temperature"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Battery",
            "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
            "CollectionName": "BatteryRollupStatus",
            "Description": "Represents the subcomponent roll-up statuses.",
            "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Battery",
            "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Battery",
            "Name": "DellRollupStatus",
            "RollupStatus": "Ok",
            "SubSystem": "Battery"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Storage",
            "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
            "CollectionName": "StorageRollupStatus",
            "Description": "Represents the subcomponent roll-up statuses.",
            "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Storage",
            "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Storage",
            "Name": "DellRollupStatus",
            "RollupStatus": "Ok",
            "SubSystem": "Storage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/System.Chassis.1_0x23_SubSystem.1_0x23_Fan",
            "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
            "CollectionName": "FanRollupStatus",
            "Description": "Represents the subcomponent roll-up statuses.",
            "Id": "System.Chassis.1_0x23_SubSystem.1_0x23_Fan",
            "InstanceID": "System.Chassis.1#SubSystem.1#Fan",
            "Name": "DellRollupStatus",
            "RollupStatus": "Ok",
            "SubSystem": "Fan"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_SEL_0x2F_Misc",
            "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
            "CollectionName": "SEL/MiscRollupStatus",
            "Description": "Represents the subcomponent roll-up statuses.",
            "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_SEL_0x2F_Misc",
            "InstanceID": "iDRAC.Embedded.1#SubSystem.1#SEL/Misc",
            "Name": "DellRollupStatus",
            "RollupStatus": "Ok",
            "SubSystem": "SEL/Misc"
        }
    ],
    "Members@odata.count": 12,
    "Name": "DellRollupStatusCollection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/System.Chassis.1_0x23_SubSystem.1_0x23_Fan

```{
    "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/System.Chassis.1_0x23_SubSystem.1_0x23_Fan",
    "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
    "CollectionName": "FanRollupStatus",
    "Description": "Represents the subcomponent roll-up statuses.",
    "Id": "System.Chassis.1_0x23_SubSystem.1_0x23_Fan",
    "InstanceID": "System.Chassis.1#SubSystem.1#Fan",
    "Name": "DellRollupStatus",
    "RollupStatus": "Ok",
    "SubSystem": "Fan"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Battery

```{
    "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Battery",
    "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
    "CollectionName": "BatteryRollupStatus",
    "Description": "Represents the subcomponent roll-up statuses.",
    "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Battery",
    "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Battery",
    "Name": "DellRollupStatus",
    "RollupStatus": "Ok",
    "SubSystem": "Battery"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Current

```{
    "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Current",
    "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
    "CollectionName": "CurrentRollupStatus",
    "Description": "Represents the subcomponent roll-up statuses.",
    "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Current",
    "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Current",
    "Name": "DellRollupStatus",
    "RollupStatus": "Ok",
    "SubSystem": "Current"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Fan

```{
    "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Fan",
    "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
    "CollectionName": "FanRollupStatus",
    "Description": "Represents the subcomponent roll-up statuses.",
    "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Fan",
    "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Fan",
    "Name": "DellRollupStatus",
    "RollupStatus": "Ok",
    "SubSystem": "Fan"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Intrusion

```{
    "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Intrusion",
    "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
    "CollectionName": "IntrusionRollupStatus",
    "Description": "Represents the subcomponent roll-up statuses.",
    "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Intrusion",
    "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Intrusion",
    "Name": "DellRollupStatus",
    "RollupStatus": "Ok",
    "SubSystem": "Intrusion"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Memory

```{
    "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Memory",
    "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
    "CollectionName": "MemoryRollupStatus",
    "Description": "Represents the subcomponent roll-up statuses.",
    "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Memory",
    "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Memory",
    "Name": "DellRollupStatus",
    "RollupStatus": "Ok",
    "SubSystem": "Memory"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_PowerSupply

```{
    "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_PowerSupply",
    "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
    "CollectionName": "PowerSupplyRollupStatus",
    "Description": "Represents the subcomponent roll-up statuses.",
    "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_PowerSupply",
    "InstanceID": "iDRAC.Embedded.1#SubSystem.1#PowerSupply",
    "Name": "DellRollupStatus",
    "RollupStatus": "Ok",
    "SubSystem": "PowerSupply"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Processor

```{
    "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Processor",
    "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
    "CollectionName": "ProcessorRollupStatus",
    "Description": "Represents the subcomponent roll-up statuses.",
    "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Processor",
    "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Processor",
    "Name": "DellRollupStatus",
    "RollupStatus": "Ok",
    "SubSystem": "Processor"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_SEL_0x2F_Misc

```{
    "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_SEL_0x2F_Misc",
    "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
    "CollectionName": "SEL/MiscRollupStatus",
    "Description": "Represents the subcomponent roll-up statuses.",
    "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_SEL_0x2F_Misc",
    "InstanceID": "iDRAC.Embedded.1#SubSystem.1#SEL/Misc",
    "Name": "DellRollupStatus",
    "RollupStatus": "Ok",
    "SubSystem": "SEL/Misc"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Storage

```{
    "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Storage",
    "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
    "CollectionName": "StorageRollupStatus",
    "Description": "Represents the subcomponent roll-up statuses.",
    "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Storage",
    "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Storage",
    "Name": "DellRollupStatus",
    "RollupStatus": "Ok",
    "SubSystem": "Storage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Temperature

```{
    "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Temperature",
    "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
    "CollectionName": "TemperatureRollupStatus",
    "Description": "Represents the subcomponent roll-up statuses.",
    "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Temperature",
    "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Temperature",
    "Name": "DellRollupStatus",
    "RollupStatus": "Ok",
    "SubSystem": "Temperature"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Voltage

```{
    "@odata.context": "/redfish/v1/$metadata#DellRollupStatus.DellRollupStatus",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellRollupStatus/iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Voltage",
    "@odata.type": "#DellRollupStatus.v1_0_0.DellRollupStatus",
    "CollectionName": "VoltageRollupStatus",
    "Description": "Represents the subcomponent roll-up statuses.",
    "Id": "iDRAC.Embedded.1_0x23_SubSystem.1_0x23_Voltage",
    "InstanceID": "iDRAC.Embedded.1#SubSystem.1#Voltage",
    "Name": "DellRollupStatus",
    "RollupStatus": "Ok",
    "SubSystem": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensorCollection.DellSensorCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors",
    "@odata.type": "#DellSensorCollection.DellSensorCollection",
    "Description": "A collection of DellSensor resource",
    "Members": [
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU11P8PG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU1 1P8 PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU11P8PG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1ANAPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU1 ANA PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1ANAPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1FIVRPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU1 FIVR PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1FIVRPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMABCDVDDPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU1 MEMABCD VDD PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1MEMABCDVDDPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMABCDVPPPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU1 MEMABCD VPP PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1MEMABCDVPPPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMABCDVTTPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU1 MEMABCD VTT PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1MEMABCDVTTPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMEFGHVDDPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU1 MEMEFGH VDD PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1MEMEFGHVDDPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMEFGHVPPPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU1 MEMEFGH VPP PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1MEMEFGHVPPPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMEFGHVTTPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU1 MEMEFGH VTT PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1MEMEFGHVTTPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1Status",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU1 Status",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1Status",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1VCCINPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU1 VCCIN PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1VCCINPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1VCCIOPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU1 VCCIO PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1VCCIOPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1VSAPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU1 VSA PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU1VSAPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU21P8PG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU2 1P8 PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU21P8PG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2ANAPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU2 ANA PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2ANAPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2FIVRPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU2 FIVR PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2FIVRPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMABCDVDDPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU2 MEMABCD VDD PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2MEMABCDVDDPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMABCDVPPPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU2 MEMABCD VPP PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2MEMABCDVPPPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMABCDVTTPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU2 MEMABCD VTT PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2MEMABCDVTTPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMEFGHVDDPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU2 MEMEFGH VDD PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2MEMEFGHVDDPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMEFGHVPPPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU2 MEMEFGH VPP PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2MEMEFGHVPPPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMEFGHVTTPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU2 MEMEFGH VTT PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2MEMEFGHVTTPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2Status",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU2 Status",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2Status",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2VCCINPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU2 VCCIN PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2VCCINPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2VCCIOPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU2 VCCIO PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2VCCIOPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2VSAPG",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Good",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "CPU2 VSA PG",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_CPU2VSAPG",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Voltage"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA1",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Presence Detected",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A1",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA1",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA10",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A10",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA10",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA11",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A11",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA11",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA12",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A12",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA12",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA13",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A13",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA13",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA14",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A14",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA14",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA15",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A15",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA15",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA16",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A16",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA16",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA2",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Presence Detected",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A2",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA2",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA3",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Presence Detected",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A3",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA3",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA4",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Presence Detected",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A4",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA4",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA5",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Presence Detected",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A5",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA5",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA6",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Presence Detected",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A6",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA6",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA7",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Presence Detected",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A7",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA7",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA8",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Presence Detected",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A8",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA8",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA9",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT A9",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA9",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB1",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Presence Detected",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT B1",
            "EnabledState": "Enabled",
            "HealthState": "OK",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB1",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB10",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT B10",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB10",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB11",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT B11",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB11",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB12",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT B12",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB12",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB13",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT B13",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB13",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB14",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT B14",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB14",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB15",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT B15",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB15",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB16",
            "@odata.type": "#DellSensor.v1_0_0.DellSensor",
            "CurrentState": "Unknown",
            "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
            "ElementName": "DIMM SLOT B16",
            "EnabledState": "Enabled",
            "HealthState": "Unknown",
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB16",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellSensor",
            "SensorType": "Other"
        }
    ],
    "Members@odata.count": 77,
    "Members@odata.nextLink": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors?$skip=50",
    "Name": "DellSensorCollection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU11P8PG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU11P8PG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU1 1P8 PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU11P8PG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1ANAPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1ANAPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU1 ANA PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1ANAPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1FIVRPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1FIVRPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU1 FIVR PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1FIVRPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMABCDVDDPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMABCDVDDPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU1 MEMABCD VDD PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1MEMABCDVDDPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMABCDVPPPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMABCDVPPPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU1 MEMABCD VPP PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1MEMABCDVPPPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMABCDVTTPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMABCDVTTPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU1 MEMABCD VTT PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1MEMABCDVTTPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMEFGHVDDPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMEFGHVDDPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU1 MEMEFGH VDD PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1MEMEFGHVDDPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMEFGHVPPPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMEFGHVPPPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU1 MEMEFGH VPP PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1MEMEFGHVPPPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMEFGHVTTPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1MEMEFGHVTTPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU1 MEMEFGH VTT PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1MEMEFGHVTTPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1Status

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1Status",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU1 Status",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1Status",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1VCCINPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1VCCINPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU1 VCCIN PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1VCCINPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1VCCIOPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1VCCIOPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU1 VCCIO PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1VCCIOPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1VSAPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU1VSAPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU1 VSA PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU1VSAPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU21P8PG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU21P8PG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU2 1P8 PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU21P8PG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2ANAPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2ANAPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU2 ANA PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2ANAPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2FIVRPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2FIVRPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU2 FIVR PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2FIVRPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMABCDVDDPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMABCDVDDPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU2 MEMABCD VDD PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2MEMABCDVDDPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMABCDVPPPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMABCDVPPPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU2 MEMABCD VPP PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2MEMABCDVPPPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMABCDVTTPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMABCDVTTPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU2 MEMABCD VTT PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2MEMABCDVTTPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMEFGHVDDPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMEFGHVDDPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU2 MEMEFGH VDD PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2MEMEFGHVDDPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMEFGHVPPPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMEFGHVPPPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU2 MEMEFGH VPP PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2MEMEFGHVPPPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMEFGHVTTPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2MEMEFGHVTTPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU2 MEMEFGH VTT PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2MEMEFGHVTTPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2Status

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2Status",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU2 Status",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2Status",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2VCCINPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2VCCINPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU2 VCCIN PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2VCCINPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2VCCIOPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2VCCIOPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU2 VCCIO PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2VCCIOPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2VSAPG

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_CPU2VSAPG",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Good",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "CPU2 VSA PG",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_CPU2VSAPG",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Voltage"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA1

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA1",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Presence Detected",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A1",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA1",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA10

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA10",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A10",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA10",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA11

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA11",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A11",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA11",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA12

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA12",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A12",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA12",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA13

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA13",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A13",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA13",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA14

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA14",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A14",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA14",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA15

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA15",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A15",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA15",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA16

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA16",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A16",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA16",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA2

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA2",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Presence Detected",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A2",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA2",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA3

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA3",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Presence Detected",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A3",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA3",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA4

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA4",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Presence Detected",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A4",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA4",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA5

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA5",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Presence Detected",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A5",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA5",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA6

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA6",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Presence Detected",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A6",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA6",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA7

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA7",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Presence Detected",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A7",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA7",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA8

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA8",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Presence Detected",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A8",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA8",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA9

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTA9",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT A9",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA9",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB1

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB1",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Presence Detected",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT B1",
    "EnabledState": "Enabled",
    "HealthState": "OK",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB1",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB10

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB10",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT B10",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB10",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB11

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB11",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT B11",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB11",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB12

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB12",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT B12",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB12",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB13

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB13",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT B13",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB13",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB14

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB14",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT B14",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB14",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB15

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB15",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT B15",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB15",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB16

```{
    "@odata.context": "/redfish/v1/$metadata#DellSensor.DellSensor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSensors/iDRAC.Embedded.1_0x23_DIMMSLOTB16",
    "@odata.type": "#DellSensor.v1_0_0.DellSensor",
    "CurrentState": "Unknown",
    "Description": "An instance of DellSensor will represent a sensor, a hardware device that is capable of measuring the characteristics of a physical property.",
    "ElementName": "DIMM SLOT B16",
    "EnabledState": "Enabled",
    "HealthState": "Unknown",
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB16",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellSensor",
    "SensorType": "Other"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlotCollection.DellSlotCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots",
    "@odata.type": "#DellSlotCollection.DellSlotCollection",
    "Description": "A collection of DellSlot resource",
    "Members": [
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.1A_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.1A",
            "EmptySlot": false,
            "Id": "Fan.Embedded.1A_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 1,
            "NumberDescription": "1A",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.1A#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.2A_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.2A",
            "EmptySlot": false,
            "Id": "Fan.Embedded.2A_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 2,
            "NumberDescription": "2A",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.2A#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.3A_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.3A",
            "EmptySlot": false,
            "Id": "Fan.Embedded.3A_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 3,
            "NumberDescription": "3A",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.3A#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.4A_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.4A",
            "EmptySlot": false,
            "Id": "Fan.Embedded.4A_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 4,
            "NumberDescription": "4A",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.4A#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.1B_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.1B",
            "EmptySlot": false,
            "Id": "Fan.Embedded.1B_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 1,
            "NumberDescription": "1B",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.1B#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.2B_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.2B",
            "EmptySlot": false,
            "Id": "Fan.Embedded.2B_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 2,
            "NumberDescription": "2B",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.2B#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.3B_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.3B",
            "EmptySlot": false,
            "Id": "Fan.Embedded.3B_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 3,
            "NumberDescription": "3B",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.3B#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.4B_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.4B",
            "EmptySlot": false,
            "Id": "Fan.Embedded.4B_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 4,
            "NumberDescription": "4B",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.4B#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.1C_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.1C",
            "EmptySlot": false,
            "Id": "Fan.Embedded.1C_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 1,
            "NumberDescription": "1C",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.1C#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.2C_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.2C",
            "EmptySlot": false,
            "Id": "Fan.Embedded.2C_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 2,
            "NumberDescription": "2C",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.2C#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.3C_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.3C",
            "EmptySlot": false,
            "Id": "Fan.Embedded.3C_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 3,
            "NumberDescription": "3C",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.3C#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.4C_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.4C",
            "EmptySlot": false,
            "Id": "Fan.Embedded.4C_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 4,
            "NumberDescription": "4C",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.4C#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.1D_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.1D",
            "EmptySlot": false,
            "Id": "Fan.Embedded.1D_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 1,
            "NumberDescription": "1D",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.1D#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.2D_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.2D",
            "EmptySlot": false,
            "Id": "Fan.Embedded.2D_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 2,
            "NumberDescription": "2D",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.2D#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.3D_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.3D",
            "EmptySlot": false,
            "Id": "Fan.Embedded.3D_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 3,
            "NumberDescription": "3D",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.3D#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.4D_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Fan",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "Fan.Embedded.4D",
            "EmptySlot": false,
            "Id": "Fan.Embedded.4D_0x23_Slot",
            "Name": "Fan Slot",
            "Number": 4,
            "NumberDescription": "4D",
            "SlotEnabledState": "Enabled",
            "Tag": "Fan.Embedded.4D#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_IDSDMSD1_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "IDSDM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": null,
            "EmptySlot": true,
            "Id": "iDRAC.Embedded.1_0x23_IDSDMSD1_0x23_Slot",
            "Name": "Dell Internal Dual SD Card Slot",
            "Number": 1,
            "NumberDescription": "1",
            "SlotEnabledState": "Disabled",
            "Tag": "iDRAC.Embedded.1#IDSDMSD1#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_IDSDMSD2_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "IDSDM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": null,
            "EmptySlot": true,
            "Id": "iDRAC.Embedded.1_0x23_IDSDMSD2_0x23_Slot",
            "Name": "Dell Internal Dual SD Card Slot",
            "Number": 2,
            "NumberDescription": "2",
            "SlotEnabledState": "Disabled",
            "Tag": "iDRAC.Embedded.1#IDSDMSD2#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/CPU.Socket.1_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Processor",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "CPU.Socket.1",
            "EmptySlot": false,
            "Id": "CPU.Socket.1_0x23_Slot",
            "Name": "Processor Slot",
            "Number": 1,
            "NumberDescription": "1",
            "SlotEnabledState": "Enabled",
            "Tag": "CPU.Socket.1#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/CPU.Socket.2_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "Processor",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "CPU.Socket.2",
            "EmptySlot": false,
            "Id": "CPU.Socket.2_0x23_Slot",
            "Name": "Processor Slot",
            "Number": 2,
            "NumberDescription": "2",
            "SlotEnabledState": "Enabled",
            "Tag": "CPU.Socket.2#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/PSU.Slot.1_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "PowerSupply",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "PSU.Slot.1",
            "EmptySlot": false,
            "Id": "PSU.Slot.1_0x23_Slot",
            "Name": "Power Supply Slot",
            "Number": 1,
            "NumberDescription": "1",
            "SlotEnabledState": "Enabled",
            "Tag": "PSU.Slot.1#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/PSU.Slot.2_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "PowerSupply",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "PSU.Slot.2",
            "EmptySlot": false,
            "Id": "PSU.Slot.2_0x23_Slot",
            "Name": "Power Supply Slot",
            "Number": 2,
            "NumberDescription": "2",
            "SlotEnabledState": "Enabled",
            "Tag": "PSU.Slot.2#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA1_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.A1",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA1_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A1",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA1#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA2_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.A2",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA2_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A2",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA2#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA3_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.A3",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA3_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A3",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA3#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA4_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.A4",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA4_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A4",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA4#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA5_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.A5",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA5_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A5",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA5#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA6_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.A6",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA6_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A6",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA6#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA7_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.A7",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA7_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A7",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA7#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA8_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.A8",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA8_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A8",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA8#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA9_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": null,
            "EmptySlot": true,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA9_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A9",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA9#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA10_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": null,
            "EmptySlot": true,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA10_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A10",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA10#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA11_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": null,
            "EmptySlot": true,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA11_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A11",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA11#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA12_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": null,
            "EmptySlot": true,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA12_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A12",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA12#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA13_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": null,
            "EmptySlot": true,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA13_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A13",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA13#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA14_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": null,
            "EmptySlot": true,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA14_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A14",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA14#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA15_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": null,
            "EmptySlot": true,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA15_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A15",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA15#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA16_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": null,
            "EmptySlot": true,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA16_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "A16",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTA16#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB1_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.B1",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB1_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "B1",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTB1#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB2_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.B2",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB2_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "B2",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTB2#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB3_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.B3",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB3_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "B3",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTB3#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB4_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.B4",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB4_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "B4",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTB4#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB5_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.B5",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB5_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "B5",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTB5#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB6_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.B6",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB6_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "B6",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTB6#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB7_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.B7",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB7_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "B7",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTB7#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB8_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": "DIMM.Socket.B8",
            "EmptySlot": false,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB8_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "B8",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTB8#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB9_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": null,
            "EmptySlot": true,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB9_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "B9",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTB9#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB10_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": null,
            "EmptySlot": true,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB10_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "B10",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTB10#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB11_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": null,
            "EmptySlot": true,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB11_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "B11",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTB11#Slot"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB12_0x23_Slot",
            "@odata.type": "#DellSlot.v1_0_0.DellSlot",
            "ConnectorLayout": "DIMM",
            "Description": "DellSlot provides slot occupancy and device correlation information.",
            "DeviceFQDD": null,
            "EmptySlot": true,
            "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB12_0x23_Slot",
            "Name": "Memory Slot",
            "Number": 0,
            "NumberDescription": "B12",
            "SlotEnabledState": "Enabled",
            "Tag": "iDRAC.Embedded.1#DIMMSLOTB12#Slot"
        }
    ],
    "Members@odata.count": 76,
    "Members@odata.nextLink": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots?$skip=50",
    "Name": "DellSlotCollection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/CPU.Socket.1_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/CPU.Socket.1_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Processor",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "CPU.Socket.1",
    "EmptySlot": false,
    "Id": "CPU.Socket.1_0x23_Slot",
    "Name": "Processor Slot",
    "Number": 1,
    "NumberDescription": "1",
    "SlotEnabledState": "Enabled",
    "Tag": "CPU.Socket.1#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/CPU.Socket.2_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/CPU.Socket.2_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Processor",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "CPU.Socket.2",
    "EmptySlot": false,
    "Id": "CPU.Socket.2_0x23_Slot",
    "Name": "Processor Slot",
    "Number": 2,
    "NumberDescription": "2",
    "SlotEnabledState": "Enabled",
    "Tag": "CPU.Socket.2#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.1A_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.1A_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.1A",
    "EmptySlot": false,
    "Id": "Fan.Embedded.1A_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 1,
    "NumberDescription": "1A",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.1A#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.1B_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.1B_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.1B",
    "EmptySlot": false,
    "Id": "Fan.Embedded.1B_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 1,
    "NumberDescription": "1B",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.1B#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.1C_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.1C_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.1C",
    "EmptySlot": false,
    "Id": "Fan.Embedded.1C_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 1,
    "NumberDescription": "1C",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.1C#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.1D_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.1D_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.1D",
    "EmptySlot": false,
    "Id": "Fan.Embedded.1D_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 1,
    "NumberDescription": "1D",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.1D#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.2A_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.2A_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.2A",
    "EmptySlot": false,
    "Id": "Fan.Embedded.2A_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 2,
    "NumberDescription": "2A",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.2A#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.2B_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.2B_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.2B",
    "EmptySlot": false,
    "Id": "Fan.Embedded.2B_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 2,
    "NumberDescription": "2B",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.2B#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.2C_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.2C_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.2C",
    "EmptySlot": false,
    "Id": "Fan.Embedded.2C_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 2,
    "NumberDescription": "2C",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.2C#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.2D_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.2D_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.2D",
    "EmptySlot": false,
    "Id": "Fan.Embedded.2D_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 2,
    "NumberDescription": "2D",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.2D#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.3A_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.3A_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.3A",
    "EmptySlot": false,
    "Id": "Fan.Embedded.3A_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 3,
    "NumberDescription": "3A",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.3A#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.3B_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.3B_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.3B",
    "EmptySlot": false,
    "Id": "Fan.Embedded.3B_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 3,
    "NumberDescription": "3B",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.3B#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.3C_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.3C_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.3C",
    "EmptySlot": false,
    "Id": "Fan.Embedded.3C_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 3,
    "NumberDescription": "3C",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.3C#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.3D_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.3D_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.3D",
    "EmptySlot": false,
    "Id": "Fan.Embedded.3D_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 3,
    "NumberDescription": "3D",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.3D#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.4A_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.4A_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.4A",
    "EmptySlot": false,
    "Id": "Fan.Embedded.4A_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 4,
    "NumberDescription": "4A",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.4A#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.4B_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.4B_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.4B",
    "EmptySlot": false,
    "Id": "Fan.Embedded.4B_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 4,
    "NumberDescription": "4B",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.4B#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.4C_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.4C_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.4C",
    "EmptySlot": false,
    "Id": "Fan.Embedded.4C_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 4,
    "NumberDescription": "4C",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.4C#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.4D_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/Fan.Embedded.4D_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "Fan",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "Fan.Embedded.4D",
    "EmptySlot": false,
    "Id": "Fan.Embedded.4D_0x23_Slot",
    "Name": "Fan Slot",
    "Number": 4,
    "NumberDescription": "4D",
    "SlotEnabledState": "Enabled",
    "Tag": "Fan.Embedded.4D#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/PSU.Slot.1_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/PSU.Slot.1_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "PowerSupply",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "PSU.Slot.1",
    "EmptySlot": false,
    "Id": "PSU.Slot.1_0x23_Slot",
    "Name": "Power Supply Slot",
    "Number": 1,
    "NumberDescription": "1",
    "SlotEnabledState": "Enabled",
    "Tag": "PSU.Slot.1#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/PSU.Slot.2_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/PSU.Slot.2_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "PowerSupply",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "PSU.Slot.2",
    "EmptySlot": false,
    "Id": "PSU.Slot.2_0x23_Slot",
    "Name": "Power Supply Slot",
    "Number": 2,
    "NumberDescription": "2",
    "SlotEnabledState": "Enabled",
    "Tag": "PSU.Slot.2#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA10_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA10_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": null,
    "EmptySlot": true,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA10_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A10",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA10#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA11_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA11_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": null,
    "EmptySlot": true,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA11_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A11",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA11#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA12_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA12_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": null,
    "EmptySlot": true,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA12_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A12",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA12#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA13_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA13_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": null,
    "EmptySlot": true,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA13_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A13",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA13#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA14_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA14_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": null,
    "EmptySlot": true,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA14_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A14",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA14#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA15_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA15_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": null,
    "EmptySlot": true,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA15_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A15",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA15#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA16_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA16_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": null,
    "EmptySlot": true,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA16_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A16",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA16#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA1_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA1_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.A1",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA1_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A1",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA1#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA2_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA2_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.A2",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA2_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A2",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA2#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA3_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA3_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.A3",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA3_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A3",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA3#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA4_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA4_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.A4",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA4_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A4",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA4#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA5_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA5_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.A5",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA5_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A5",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA5#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA6_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA6_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.A6",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA6_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A6",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA6#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA7_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA7_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.A7",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA7_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A7",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA7#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA8_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA8_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.A8",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA8_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A8",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA8#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA9_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTA9_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": null,
    "EmptySlot": true,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTA9_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "A9",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTA9#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB10_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB10_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": null,
    "EmptySlot": true,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB10_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "B10",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTB10#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB11_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB11_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": null,
    "EmptySlot": true,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB11_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "B11",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTB11#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB12_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB12_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": null,
    "EmptySlot": true,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB12_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "B12",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTB12#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB1_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB1_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.B1",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB1_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "B1",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTB1#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB2_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB2_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.B2",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB2_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "B2",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTB2#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB3_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB3_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.B3",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB3_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "B3",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTB3#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB4_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB4_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.B4",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB4_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "B4",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTB4#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB5_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB5_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.B5",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB5_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "B5",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTB5#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB6_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB6_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.B6",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB6_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "B6",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTB6#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB7_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB7_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.B7",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB7_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "B7",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTB7#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB8_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB8_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": "DIMM.Socket.B8",
    "EmptySlot": false,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB8_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "B8",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTB8#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB9_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_DIMMSLOTB9_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "DIMM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": null,
    "EmptySlot": true,
    "Id": "iDRAC.Embedded.1_0x23_DIMMSLOTB9_0x23_Slot",
    "Name": "Memory Slot",
    "Number": 0,
    "NumberDescription": "B9",
    "SlotEnabledState": "Enabled",
    "Tag": "iDRAC.Embedded.1#DIMMSLOTB9#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_IDSDMSD1_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_IDSDMSD1_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "IDSDM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": null,
    "EmptySlot": true,
    "Id": "iDRAC.Embedded.1_0x23_IDSDMSD1_0x23_Slot",
    "Name": "Dell Internal Dual SD Card Slot",
    "Number": 1,
    "NumberDescription": "1",
    "SlotEnabledState": "Disabled",
    "Tag": "iDRAC.Embedded.1#IDSDMSD1#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_IDSDMSD2_0x23_Slot

```{
    "@odata.context": "/redfish/v1/$metadata#DellSlot.DellSlot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSlots/iDRAC.Embedded.1_0x23_IDSDMSD2_0x23_Slot",
    "@odata.type": "#DellSlot.v1_0_0.DellSlot",
    "ConnectorLayout": "IDSDM",
    "Description": "DellSlot provides slot occupancy and device correlation information.",
    "DeviceFQDD": null,
    "EmptySlot": true,
    "Id": "iDRAC.Embedded.1_0x23_IDSDMSD2_0x23_Slot",
    "Name": "Dell Internal Dual SD Card Slot",
    "Number": 2,
    "NumberDescription": "2",
    "SlotEnabledState": "Disabled",
    "Tag": "iDRAC.Embedded.1#IDSDMSD2#Slot"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService

```{
    "@odata.context": "/redfish/v1/$metadata#DellSoftwareInstallationService.DellSoftwareInstallationService",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService",
    "@odata.type": "#DellSoftwareInstallationService.v1_1_2.DellSoftwareInstallationService",
    "Actions": {
        "#DellSoftwareInstallationService.ClearUpdateSchedule": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService/Actions/DellSoftwareInstallationService.ClearUpdateSchedule"
        },
        "#DellSoftwareInstallationService.GetRepoBasedUpdateList": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService/Actions/DellSoftwareInstallationService.GetRepoBasedUpdateList"
        },
        "#DellSoftwareInstallationService.GetUpdateSchedule": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService/Actions/DellSoftwareInstallationService.GetUpdateSchedule"
        },
        "#DellSoftwareInstallationService.InstallFromRepository": {
            "ApplyUpdate@Redfish.AllowableValues": [
                "False",
                "True"
            ],
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "FTP",
                "HTTP",
                "HTTPS",
                "NFS",
                "TFTP"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService/Actions/DellSoftwareInstallationService.InstallFromRepository"
        },
        "#DellSoftwareInstallationService.InstallFromURI": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService/Actions/DellSoftwareInstallationService.InstallFromURI"
        },
        "#DellSoftwareInstallationService.SetUpdateSchedule": {
            "ApplyReboot@Redfish.AllowableValues": [
                "NoReboot",
                "RebootRequired"
            ],
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "FTP",
                "HTTP",
                "HTTPS",
                "NFS"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSoftwareInstallationService/Actions/DellSoftwareInstallationService.SetUpdateSchedule"
        }
    },
    "Description": "The DellSoftwareInstallationService resource provides some actions to support software installation functionality.",
    "Id": "DellSoftwareInstallationService",
    "Name": "DellSoftwareInstallationService"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSwitchConnectionService

```{
    "@odata.context": "/redfish/v1/$metadata#DellSwitchConnectionService.DellSwitchConnectionService",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSwitchConnectionService",
    "@odata.type": "#DellSwitchConnectionService.v1_0_0.DellSwitchConnectionService",
    "Actions": {
        "#DellSwitchConnectionService.ServerPortConnectionRefresh": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSwitchConnectionService/Actions/DellSwitchConnectionService.ServerPortConnectionRefresh"
        }
    },
    "Description": "DellSwitchConnectionService provides actions to support switch connection view functionality.",
    "Id": "DellSwitchConnectionService",
    "Name": "DellSwitchConnectionService"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSystem/System.Embedded.1

```{
    "@odata.context": "/redfish/v1/$metadata#DellSystem.DellSystem",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSystem/System.Embedded.1",
    "@odata.type": "#DellSystem.v1_3_0.DellSystem",
    "BIOSReleaseDate": "05/28/2021",
    "BaseBoardChassisSlot": "NA",
    "BatteryRollupStatus": "OK",
    "BladeGeometry": "NotApplicable",
    "CMCIP": null,
    "CPURollupStatus": "OK",
    "ChassisModel": "",
    "ChassisName": "Main System Chassis",
    "ChassisServiceTag": "U8OIL5X",
    "ChassisSystemHeightUnit": 1,
    "CurrentRollupStatus": "OK",
    "Description": "An instance of DellSystem will have data representing the overall system devices in the managed system.",
    "EstimatedExhaustTemperatureCelsius": 255,
    "EstimatedSystemAirflowCFM": 255,
    "ExpressServiceCode": "2440875279",
    "FanRollupStatus": "OK",
    "IDSDMRollupStatus": null,
    "Id": "System.Embedded.1",
    "IntrusionRollupStatus": "OK",
    "IsOEMBranded": "False",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2022-08-30T23:00:48+00:00",
    "LicensingRollupStatus": "OK",
    "ManagedSystemSize": "1 U",
    "MaxCPUSockets": 2,
    "MaxDIMMSlots": 32,
    "MaxPCIeSlots": 3,
    "MemoryOperationMode": "OptimizerMode",
    "Name": "DellSystem",
    "NodeID": "U8OIL5X",
    "PSRollupStatus": "OK",
    "PlatformGUID": "3346464f-c0b1-3880-4410-00344c4c4544",
    "PopulatedDIMMSlots": 16,
    "PopulatedPCIeSlots": 1,
    "PowerCapEnabledState": "Disabled",
    "SDCardRollupStatus": null,
    "SELRollupStatus": "OK",
    "ServerAllocationWatts": null,
    "StorageRollupStatus": "OK",
    "SysMemErrorMethodology": "Multi-bitECC",
    "SysMemFailOverState": "NotInUse",
    "SysMemLocation": "SystemBoardOrMotherboard",
    "SysMemPrimaryStatus": "OK",
    "SystemGeneration": "15G Monolithic",
    "SystemID": 2322,
    "SystemRevision": "I",
    "TempRollupStatus": "OK",
    "TempStatisticsRollupStatus": "OK",
    "UUID": "4c4c4544-0034-4410-8038-b1c04f464633",
    "VoltRollupStatus": "OK",
    "smbiosGUID": "44454c4c-3400-1044-8038-b1c04f464633"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSystemManagementService

```{
    "@odata.context": "/redfish/v1/$metadata#DellSystemManagementService.DellSystemManagementService",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSystemManagementService",
    "@odata.type": "#DellSystemManagementService.v1_0_0.DellSystemManagementService",
    "Actions": {
        "#DellSystemManagementService.ShowErrorsOnLCD": {
            "target": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSystemManagementService/Actions/DellSystemManagementService.ShowErrorsOnLCD"
        }
    },
    "Description": "DellSystemManagementService provides actions to support System Management functionalities.",
    "Id": "DellSystemManagementService",
    "Name": "DellSystemManagementService"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellVideo

```{
    "@odata.context": "/redfish/v1/$metadata#DellVideoCollection.DellVideoCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellVideo",
    "@odata.type": "#DellVideoCollection.DellVideoCollection",
    "Description": "A collection of DellVideo resource",
    "Members": [
        {
            "@odata.context": "/redfish/v1/$metadata#DellVideo.DellVideo",
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellVideo/Video.Embedded.1-1",
            "@odata.type": "#DellVideo.v1_1_0.DellVideo",
            "BoardPartNumber": null,
            "BuildDate": null,
            "BusNumber": 3,
            "DataBusWidth": "Unknown",
            "Description": "DellVideo provides Video specific data which includes supported GPU properties if supported.",
            "DeviceNumber": 0,
            "FQDD": "Video.Embedded.1-1",
            "FirmwareVersion": null,
            "FunctionNumber": 0,
            "GPUGUID": null,
            "GPUHealth": null,
            "GPUPartNumber": null,
            "GPUState": null,
            "Id": "Video.Embedded.1-1",
            "InstanceID": "Video.Embedded.1-1",
            "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
            "LastUpdateTime": "2021-07-02T21:31:25+00:00",
            "Manufacturer": "Matrox Electronics Systems Ltd.",
            "MarketingName": null,
            "Name": "Embedded Video Controller 1",
            "OEMInfo": null,
            "PCIDeviceID": "0536",
            "PCISubDeviceID": "0912",
            "PCISubVendorID": "1028",
            "PCIVendorID": "102B",
            "SerialNumber": null,
            "SlotLength": "Unknown",
            "SlotType": "Unknown"
        }
    ],
    "Members@odata.count": 1,
    "Name": "DellVideoCollection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellVideo/Video.Embedded.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellVideo.DellVideo",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellVideo/Video.Embedded.1-1",
    "@odata.type": "#DellVideo.v1_1_0.DellVideo",
    "BoardPartNumber": null,
    "BuildDate": null,
    "BusNumber": 3,
    "DataBusWidth": "Unknown",
    "Description": "DellVideo provides Video specific data which includes supported GPU properties if supported.",
    "DeviceNumber": 0,
    "FQDD": "Video.Embedded.1-1",
    "FirmwareVersion": null,
    "FunctionNumber": 0,
    "GPUGUID": null,
    "GPUHealth": null,
    "GPUPartNumber": null,
    "GPUState": null,
    "Id": "Video.Embedded.1-1",
    "InstanceID": "Video.Embedded.1-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "Manufacturer": "Matrox Electronics Systems Ltd.",
    "MarketingName": null,
    "Name": "Embedded Video Controller 1",
    "OEMInfo": null,
    "PCIDeviceID": "0536",
    "PCISubDeviceID": "0912",
    "PCISubVendorID": "1028",
    "PCIVendorID": "102B",
    "SerialNumber": null,
    "SlotLength": "Unknown",
    "SlotType": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellVideoNetwork

```{
    "@odata.context": "/redfish/v1/$metadata#DellVideoNetworkCollection.DellVideoNetworkCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellVideoNetwork",
    "@odata.type": "#DellVideoNetworkCollection.DellVideoNetworkCollection",
    "Description": "A collection of DellVideoNetwork resource",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "DellVideoNetworkCollection"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.etag": "1661896871",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "AssetTag": null,
    "Description": "C620 Series Chipset Family SSATA Controller [AHCI mode]",
    "DeviceType": "MultiFunction",
    "FirmwareVersion": "",
    "Id": "0-17",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Chassis@odata.count": 1,
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17/PCIeFunctions/0-17-5"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Manufacturer": "Intel Corporation",
    "Model": null,
    "Name": "C620 Series Chipset Family SSATA Controller [AHCI mode]",
    "PartNumber": null,
    "SKU": null,
    "SerialNumber": null,
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17/PCIeFunctions/0-17-5

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896871",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17/PCIeFunctions/0-17-5",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x000001",
    "Description": "C620 Series Chipset Family SSATA Controller [AHCI mode]",
    "DeviceClass": "MassStorageController",
    "DeviceId": "0xa1d2",
    "FunctionId": 5,
    "FunctionType": "Physical",
    "Id": "0-17-5",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.1-1#/StorageControllers/0"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "C620 Series Chipset Family SSATA Controller [AHCI mode]",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17/PCIeFunctions/0-17-5/Oem/Dell/DellPCIeFunctions/AHCI.Embedded.1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "AHCI.Embedded.1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-04-06T08:56:37+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    },
    "RevisionId": "0x0a",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x0912",
    "SubsystemVendorId": "0x1028",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17/PCIeFunctions/0-17-5/Oem/Dell/DellPCIeFunctions/AHCI.Embedded.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17/PCIeFunctions/0-17-5/Oem/Dell/DellPCIeFunctions/AHCI.Embedded.1-1",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "AHCI.Embedded.1-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2022-04-06T08:56:37+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "Unknown",
    "SlotType": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.etag": "1661896870",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "AssetTag": null,
    "Description": "C620 Series Chipset Family SATA Controller [AHCI mode]",
    "DeviceType": "SingleFunction",
    "FirmwareVersion": "",
    "Id": "0-23",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Chassis@odata.count": 1,
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23/PCIeFunctions/0-23-0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Manufacturer": "Intel Corporation",
    "Model": null,
    "Name": "C620 Series Chipset Family SATA Controller [AHCI mode]",
    "PartNumber": null,
    "SKU": null,
    "SerialNumber": null,
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23/PCIeFunctions/0-23-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896870",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23/PCIeFunctions/0-23-0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x000001",
    "Description": "C620 Series Chipset Family SATA Controller [AHCI mode]",
    "DeviceClass": "MassStorageController",
    "DeviceId": "0xa182",
    "FunctionId": 0,
    "FunctionType": "Physical",
    "Id": "0-23-0",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.2-1#/StorageControllers/0"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "C620 Series Chipset Family SATA Controller [AHCI mode]",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23/PCIeFunctions/0-23-0/Oem/Dell/DellPCIeFunctions/AHCI.Embedded.2-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "AHCI.Embedded.2-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-04-06T08:56:37+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    },
    "RevisionId": "0x0a",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x0912",
    "SubsystemVendorId": "0x1028",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23/PCIeFunctions/0-23-0/Oem/Dell/DellPCIeFunctions/AHCI.Embedded.2-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23/PCIeFunctions/0-23-0/Oem/Dell/DellPCIeFunctions/AHCI.Embedded.2-1",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "AHCI.Embedded.2-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2022-04-06T08:56:37+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "Unknown",
    "SlotType": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.etag": "1661896870",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "AssetTag": null,
    "Description": "C620 Series Chipset Family PCI Express Root Port #5",
    "DeviceType": "MultiFunction",
    "FirmwareVersion": "",
    "Id": "0-28",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Chassis@odata.count": 1,
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-0"
            }
        ],
        "PCIeFunctions@odata.count": 2
    },
    "Manufacturer": "Intel Corporation",
    "Model": null,
    "Name": "C620 Series Chipset Family PCI Express Root Port #5",
    "PartNumber": null,
    "SKU": null,
    "SerialNumber": null,
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896871",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x000006",
    "Description": "C620 Series Chipset Family PCI Express Root Port #1",
    "DeviceClass": "Bridge",
    "DeviceId": "0xa190",
    "FunctionId": 0,
    "FunctionType": "Physical",
    "Id": "0-28-0",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "C620 Series Chipset Family PCI Express Root Port #1",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-0/Oem/Dell/DellPCIeFunctions/P2PBridge.Embedded.1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "P2PBridge.Embedded.1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    },
    "RevisionId": "0xfa",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x0912",
    "SubsystemVendorId": "0x1028",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-0/Oem/Dell/DellPCIeFunctions/P2PBridge.Embedded.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-0/Oem/Dell/DellPCIeFunctions/P2PBridge.Embedded.1-1",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "P2PBridge.Embedded.1-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "Unknown",
    "SlotType": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-4

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896870",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-4",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x000006",
    "Description": "C620 Series Chipset Family PCI Express Root Port #5",
    "DeviceClass": "Bridge",
    "DeviceId": "0xa194",
    "FunctionId": 4,
    "FunctionType": "Physical",
    "Id": "0-28-4",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "C620 Series Chipset Family PCI Express Root Port #5",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-4/Oem/Dell/DellPCIeFunctions/P2PBridge.Embedded.2-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "P2PBridge.Embedded.2-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    },
    "RevisionId": "0xfa",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x0912",
    "SubsystemVendorId": "0x1028",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-4/Oem/Dell/DellPCIeFunctions/P2PBridge.Embedded.2-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28/PCIeFunctions/0-28-4/Oem/Dell/DellPCIeFunctions/P2PBridge.Embedded.2-1",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "P2PBridge.Embedded.2-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "Unknown",
    "SlotType": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.etag": "1661896871",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "AssetTag": null,
    "Description": "C620 Series Chipset Family SMBus",
    "DeviceType": "SingleFunction",
    "FirmwareVersion": "",
    "Id": "0-31",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Chassis@odata.count": 1,
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-0"
            }
        ],
        "PCIeFunctions@odata.count": 2
    },
    "Manufacturer": "Intel Corporation",
    "Model": null,
    "Name": "C620 Series Chipset Family SMBus",
    "PartNumber": null,
    "SKU": null,
    "SerialNumber": null,
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896871",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x000006",
    "Description": "Intel Corporation",
    "DeviceClass": "Bridge",
    "DeviceId": "0xa1cb",
    "FunctionId": 0,
    "FunctionType": "Physical",
    "Id": "0-31-0",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel Corporation",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-0/Oem/Dell/DellPCIeFunctions/ISABridge.Embedded.1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "ISABridge.Embedded.1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    },
    "RevisionId": "0x0a",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x0912",
    "SubsystemVendorId": "0x1028",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-0/Oem/Dell/DellPCIeFunctions/ISABridge.Embedded.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-0/Oem/Dell/DellPCIeFunctions/ISABridge.Embedded.1-1",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "ISABridge.Embedded.1-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "Unknown",
    "SlotType": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-4

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896871",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-4",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x00000c",
    "Description": "C620 Series Chipset Family SMBus",
    "DeviceClass": "SerialBusController",
    "DeviceId": "0xa1a3",
    "FunctionId": 4,
    "FunctionType": "Physical",
    "Id": "0-31-4",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "C620 Series Chipset Family SMBus",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-4/Oem/Dell/DellPCIeFunctions/SMBus.Embedded.3-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "SMBus.Embedded.3-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    },
    "RevisionId": "0x0a",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x0912",
    "SubsystemVendorId": "0x1028",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-4/Oem/Dell/DellPCIeFunctions/SMBus.Embedded.3-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31/PCIeFunctions/0-31-4/Oem/Dell/DellPCIeFunctions/SMBus.Embedded.3-1",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "SMBus.Embedded.3-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "Unknown",
    "SlotType": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/101-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.etag": "1661896872",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/101-0",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "AssetTag": null,
    "Description": "Ent NVMe v2 AGN MU U.2 1.6TB",
    "DeviceType": "SingleFunction",
    "FirmwareVersion": "2.0.0",
    "Id": "101-0",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Chassis@odata.count": 1,
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/101-0/PCIeFunctions/101-0-0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Manufacturer": "Samsung Electronics Co Ltd",
    "Model": null,
    "Name": "Ent NVMe v2 AGN MU U.2 1.6TB",
    "PartNumber": "00MNMV",
    "SKU": null,
    "SerialNumber": "KRSSK0015M00ZR",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/101-0/PCIeFunctions/101-0-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896872",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/101-0/PCIeFunctions/101-0-0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x000001",
    "Description": "Ent NVMe v2 AGN MU U.2 1.6TB",
    "DeviceClass": "MassStorageController",
    "DeviceId": "0xa824",
    "FunctionId": 0,
    "FunctionType": "Physical",
    "Id": "101-0-0",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/101-0"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "Ent NVMe v2 AGN MU U.2 1.6TB",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/101-0/PCIeFunctions/101-0-0/Oem/Dell/DellPCIeFunctions/Disk.Bay.9:Enclosure.Internal.0-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "4XOrX4",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "Disk.Bay.9:Enclosure.Internal.0-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "2.5InchDriveFormFactor",
                "SlotType": "PCIExpressGen4SFF-8639"
            }
        }
    },
    "RevisionId": "0x00",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x2119",
    "SubsystemVendorId": "0x1028",
    "VendorId": "0x144d"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/102-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.etag": "1661896872",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/102-0",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "AssetTag": null,
    "Description": "Ent NVMe v2 AGN MU U.2 1.6TB",
    "DeviceType": "SingleFunction",
    "FirmwareVersion": "2.0.0",
    "Id": "102-0",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Chassis@odata.count": 1,
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/102-0/PCIeFunctions/102-0-0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Manufacturer": "Samsung Electronics Co Ltd",
    "Model": null,
    "Name": "Ent NVMe v2 AGN MU U.2 1.6TB",
    "PartNumber": "00MNMV",
    "SKU": null,
    "SerialNumber": "KRSSK0015M010C",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/102-0/PCIeFunctions/102-0-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896872",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/102-0/PCIeFunctions/102-0-0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x000001",
    "Description": "Ent NVMe v2 AGN MU U.2 1.6TB",
    "DeviceClass": "MassStorageController",
    "DeviceId": "0xa824",
    "FunctionId": 0,
    "FunctionType": "Physical",
    "Id": "102-0-0",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/102-0"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "Ent NVMe v2 AGN MU U.2 1.6TB",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/102-0/PCIeFunctions/102-0-0/Oem/Dell/DellPCIeFunctions/Disk.Bay.8:Enclosure.Internal.0-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "4XOrX4",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "Disk.Bay.8:Enclosure.Internal.0-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "2.5InchDriveFormFactor",
                "SlotType": "PCIExpressGen4SFF-8639"
            }
        }
    },
    "RevisionId": "0x00",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x2119",
    "SubsystemVendorId": "0x1028",
    "VendorId": "0x144d"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/103-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.etag": "1661896871",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/103-0",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "AssetTag": null,
    "Description": "PERC H745 Front",
    "DeviceType": "SingleFunction",
    "FirmwareVersion": "51.14.0-3900",
    "Id": "103-0",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Chassis@odata.count": 1,
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/103-0/PCIeFunctions/103-0-0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Manufacturer": "Broadcom / LSI",
    "Model": null,
    "Name": "PERC H745 Front",
    "PartNumber": "0JT47Y",
    "SKU": null,
    "SerialNumber": "CNIVC0013I0887",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/103-0/PCIeFunctions/103-0-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896871",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/103-0/PCIeFunctions/103-0-0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x000001",
    "Description": "PERC H745 Front",
    "DeviceClass": "MassStorageController",
    "DeviceId": "0x0014",
    "FunctionId": 0,
    "FunctionType": "Physical",
    "Id": "103-0-0",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1/Drives/Disk.Bay.1:Enclosure.Internal.0-1:RAID.SL.3-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1/Drives/Disk.Bay.0:Enclosure.Internal.0-1:RAID.SL.3-1"
            }
        ],
        "Drives@odata.count": 2,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/103-0"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1#/StorageControllers/0"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "PERC H745 Front",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/103-0/PCIeFunctions/103-0-0/Oem/Dell/DellPCIeFunctions/RAID.SL.3-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "RAID.SL.3-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-08-30T23:00:48+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    },
    "RevisionId": "0x01",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x1f3b",
    "SubsystemVendorId": "0x1028",
    "VendorId": "0x1000"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/103-0/PCIeFunctions/103-0-0/Oem/Dell/DellPCIeFunctions/RAID.SL.3-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/103-0/PCIeFunctions/103-0-0/Oem/Dell/DellPCIeFunctions/RAID.SL.3-1",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "RAID.SL.3-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2022-08-30T23:00:48+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "Unknown",
    "SlotType": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.etag": "1661896871",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "AssetTag": null,
    "Description": "LPe32002-M2-D 2-Port 32Gb Fibre Channel Adapter",
    "DeviceType": "MultiFunction",
    "FirmwareVersion": "03.00.14",
    "Id": "23-0",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Chassis@odata.count": 1,
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-0"
            }
        ],
        "PCIeFunctions@odata.count": 2
    },
    "Manufacturer": "Emulex Corporation",
    "Model": null,
    "Name": "LPe32002-M2-D 2-Port 32Gb Fibre Channel Adapter",
    "PartNumber": "0MHFHK",
    "SKU": null,
    "SerialNumber": "MYFLPB38BTM033",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896872",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x00000c",
    "Description": "LPe32002-M2-D 2-Port 32Gb Fibre Channel Adapter",
    "DeviceClass": "SerialBusController",
    "DeviceId": "0xe300",
    "FunctionId": 0,
    "FunctionType": "Physical",
    "Id": "23-0-0",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "LPe32002-M2-D 2-Port 32Gb Fibre Channel Adapter",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-0/Oem/Dell/DellPCIeFunctions/FC.Slot.1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "16XOrX16",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "FC.Slot.1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-04-29T01:38:52+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "LongLength",
                "SlotType": "PCIExpressGen4"
            }
        }
    },
    "RevisionId": "0x01",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0xe320",
    "SubsystemVendorId": "0x10df",
    "VendorId": "0x10df"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-0/Oem/Dell/DellPCIeFunctions/FC.Slot.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-0/Oem/Dell/DellPCIeFunctions/FC.Slot.1-1",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "16XOrX16",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "FC.Slot.1-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2022-04-29T01:38:52+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "LongLength",
    "SlotType": "PCIExpressGen4"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-1

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896871",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-1",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x00000c",
    "Description": "LPe32002-M2-D 2-Port 32Gb Fibre Channel Adapter",
    "DeviceClass": "SerialBusController",
    "DeviceId": "0xe300",
    "FunctionId": 1,
    "FunctionType": "Physical",
    "Id": "23-0-1",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "LPe32002-M2-D 2-Port 32Gb Fibre Channel Adapter",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-1/Oem/Dell/DellPCIeFunctions/FC.Slot.1-2",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "16XOrX16",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "FC.Slot.1-2",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-04-29T01:38:52+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "LongLength",
                "SlotType": "PCIExpressGen4"
            }
        }
    },
    "RevisionId": "0x01",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0xe320",
    "SubsystemVendorId": "0x10df",
    "VendorId": "0x10df"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-1/Oem/Dell/DellPCIeFunctions/FC.Slot.1-2

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0/PCIeFunctions/23-0-1/Oem/Dell/DellPCIeFunctions/FC.Slot.1-2",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "16XOrX16",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "FC.Slot.1-2",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2022-04-29T01:38:52+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "LongLength",
    "SlotType": "PCIExpressGen4"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/3-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.etag": "1661896871",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/3-0",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "AssetTag": null,
    "Description": "Integrated Matrox G200eW3 Graphics Controller",
    "DeviceType": "SingleFunction",
    "FirmwareVersion": "",
    "Id": "3-0",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Chassis@odata.count": 1,
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/3-0/PCIeFunctions/3-0-0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Manufacturer": "Matrox Electronics Systems Ltd.",
    "Model": null,
    "Name": "Integrated Matrox G200eW3 Graphics Controller",
    "PartNumber": null,
    "SKU": null,
    "SerialNumber": null,
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/3-0/PCIeFunctions/3-0-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896871",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/3-0/PCIeFunctions/3-0-0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x000003",
    "Description": "Integrated Matrox G200eW3 Graphics Controller",
    "DeviceClass": "DisplayController",
    "DeviceId": "0x0536",
    "FunctionId": 0,
    "FunctionType": "Physical",
    "Id": "3-0-0",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/3-0"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "Integrated Matrox G200eW3 Graphics Controller",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/3-0/PCIeFunctions/3-0-0/Oem/Dell/DellPCIeFunctions/Video.Embedded.1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "Video.Embedded.1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    },
    "RevisionId": "0x04",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x0912",
    "SubsystemVendorId": "0x1028",
    "VendorId": "0x102b"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/3-0/PCIeFunctions/3-0-0/Oem/Dell/DellPCIeFunctions/Video.Embedded.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/3-0/PCIeFunctions/3-0-0/Oem/Dell/DellPCIeFunctions/Video.Embedded.1-1",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "Video.Embedded.1-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "Unknown",
    "SlotType": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.etag": "1661896870",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "AssetTag": null,
    "Description": "PowerEdge Rx5xx LOM Board",
    "DeviceType": "MultiFunction",
    "FirmwareVersion": "21.80.8",
    "Id": "4-0",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Chassis@odata.count": 1,
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-0"
            }
        ],
        "PCIeFunctions@odata.count": 2
    },
    "Manufacturer": "Broadcom Inc. and subsidiaries",
    "Model": null,
    "Name": "PowerEdge Rx5xx LOM Board",
    "PartNumber": null,
    "SKU": null,
    "SerialNumber": null,
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896871",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x000002",
    "Description": "PowerEdge Rx5xx LOM Board",
    "DeviceClass": "NetworkController",
    "DeviceId": "0x165f",
    "FunctionId": 0,
    "FunctionType": "Physical",
    "Id": "4-0-0",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Embedded.1-1-1"
            }
        ],
        "EthernetInterfaces@odata.count": 1,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "PowerEdge Rx5xx LOM Board",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-0/Oem/Dell/DellPCIeFunctions/NIC.Embedded.1-1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "NIC.Embedded.1-1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-14T03:23:00+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    },
    "RevisionId": "0x00",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x08ff",
    "SubsystemVendorId": "0x1028",
    "VendorId": "0x14e4"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-0/Oem/Dell/DellPCIeFunctions/NIC.Embedded.1-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-0/Oem/Dell/DellPCIeFunctions/NIC.Embedded.1-1-1",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "NIC.Embedded.1-1-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-14T03:23:00+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "Unknown",
    "SlotType": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-1

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896870",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-1",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x000002",
    "Description": "PowerEdge Rx5xx LOM Board",
    "DeviceClass": "NetworkController",
    "DeviceId": "0x165f",
    "FunctionId": 1,
    "FunctionType": "Physical",
    "Id": "4-0-1",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Embedded.2-1-1"
            }
        ],
        "EthernetInterfaces@odata.count": 1,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "PowerEdge Rx5xx LOM Board",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-1/Oem/Dell/DellPCIeFunctions/NIC.Embedded.2-1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "NIC.Embedded.2-1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T22:29:07+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    },
    "RevisionId": "0x00",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x08ff",
    "SubsystemVendorId": "0x1028",
    "VendorId": "0x14e4"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-1/Oem/Dell/DellPCIeFunctions/NIC.Embedded.2-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0/PCIeFunctions/4-0-1/Oem/Dell/DellPCIeFunctions/NIC.Embedded.2-1-1",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "NIC.Embedded.2-1-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T22:29:07+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "Unknown",
    "SlotType": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.etag": "1661896872",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "AssetTag": null,
    "Description": "MT27800 Family [ConnectX-5]",
    "DeviceType": "MultiFunction",
    "FirmwareVersion": "16.28.45.12",
    "Id": "49-0",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Chassis@odata.count": 1,
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-0"
            }
        ],
        "PCIeFunctions@odata.count": 2
    },
    "Manufacturer": "Mellanox Technologies",
    "Model": null,
    "Name": "MT27800 Family [ConnectX-5]",
    "PartNumber": "04TRD3",
    "SKU": null,
    "SerialNumber": "INJBNM414TJ0AL",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896872",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x000002",
    "Description": "MT27800 Family [ConnectX-5]",
    "DeviceClass": "NetworkController",
    "DeviceId": "0x1017",
    "FunctionId": 0,
    "FunctionType": "Physical",
    "Id": "49-0-0",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Integrated.1-1-1"
            }
        ],
        "EthernetInterfaces@odata.count": 1,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "MT27800 Family [ConnectX-5]",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-0/Oem/Dell/DellPCIeFunctions/NIC.Integrated.1-1-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "NIC.Integrated.1-1-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-08-04T16:53:47+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    },
    "RevisionId": "0x00",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x0097",
    "SubsystemVendorId": "0x15b3",
    "VendorId": "0x15b3"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-0/Oem/Dell/DellPCIeFunctions/NIC.Integrated.1-1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-0/Oem/Dell/DellPCIeFunctions/NIC.Integrated.1-1-1",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "NIC.Integrated.1-1-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2022-08-04T16:53:47+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "Unknown",
    "SlotType": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-1

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896872",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-1",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x000002",
    "Description": "MT27800 Family [ConnectX-5]",
    "DeviceClass": "NetworkController",
    "DeviceId": "0x1017",
    "FunctionId": 1,
    "FunctionType": "Physical",
    "Id": "49-0-1",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/EthernetInterfaces/NIC.Integrated.1-2-1"
            }
        ],
        "EthernetInterfaces@odata.count": 1,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "MT27800 Family [ConnectX-5]",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-1/Oem/Dell/DellPCIeFunctions/NIC.Integrated.1-2-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "NIC.Integrated.1-2-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-08-04T16:53:47+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    },
    "RevisionId": "0x00",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x0097",
    "SubsystemVendorId": "0x15b3",
    "VendorId": "0x15b3"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-1/Oem/Dell/DellPCIeFunctions/NIC.Integrated.1-2-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0/PCIeFunctions/49-0-1/Oem/Dell/DellPCIeFunctions/NIC.Integrated.1-2-1",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "NIC.Integrated.1-2-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2022-08-04T16:53:47+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "Unknown",
    "SlotType": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.etag": "1661896872",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "AssetTag": null,
    "Description": "BOSS-S2 Adapter",
    "DeviceType": "SingleFunction",
    "FirmwareVersion": "2.5.13.4008",
    "Id": "5-0",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Chassis@odata.count": 1,
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0/PCIeFunctions/5-0-0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Manufacturer": "Marvell Technology Group Ltd.",
    "Model": null,
    "Name": "BOSS-S2 Adapter",
    "PartNumber": "0FGNRW",
    "SKU": null,
    "SerialNumber": "CNIVC0015I0958",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0/PCIeFunctions/5-0-0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.etag": "1661896872",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0/PCIeFunctions/5-0-0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "ClassCode": "0x000001",
    "Description": "BOSS-S2 Adapter",
    "DeviceClass": "MassStorageController",
    "DeviceId": "0x9230",
    "FunctionId": 0,
    "FunctionType": "Physical",
    "Id": "5-0-0",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1/Drives/Disk.Direct.0-0:AHCI.SL.6-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1/Drives/Disk.Direct.1-1:AHCI.SL.6-1"
            }
        ],
        "Drives@odata.count": 2,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1#/StorageControllers/0"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "BOSS-S2 Adapter",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellPCIeFunction": {
                "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0/PCIeFunctions/5-0-0/Oem/Dell/DellPCIeFunctions/AHCI.SL.6-1",
                "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
                "DataBusWidth": "Unknown",
                "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
                "Id": "AHCI.SL.6-1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-04-06T08:56:37+00:00",
                "Name": "DellPCIeFunction",
                "SlotLength": "Unknown",
                "SlotType": "Unknown"
            }
        }
    },
    "RevisionId": "0x11",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SubsystemId": "0x2010",
    "SubsystemVendorId": "0x1028",
    "VendorId": "0x1b4b"
}
```

## /redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0/PCIeFunctions/5-0-0/Oem/Dell/DellPCIeFunctions/AHCI.SL.6-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPCIeFunction.DellPCIeFunction",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0/PCIeFunctions/5-0-0/Oem/Dell/DellPCIeFunctions/AHCI.SL.6-1",
    "@odata.type": "#DellPCIeFunction.v1_3_0.DellPCIeFunction",
    "DataBusWidth": "Unknown",
    "Description": "An instance of DellPCIeFunction will have PCI device specific data.",
    "Id": "AHCI.SL.6-1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2022-04-06T08:56:37+00:00",
    "Name": "DellPCIeFunction",
    "SlotLength": "Unknown",
    "SlotType": "Unknown"
}
```

## /redfish/v1/Systems/System.Embedded.1/Processors

```{
    "@odata.context": "/redfish/v1/$metadata#ProcessorCollection.ProcessorCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors",
    "@odata.type": "#ProcessorCollection.ProcessorCollection",
    "Description": "Collection of Processors for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
        }
    ],
    "Members@odata.count": 2,
    "Name": "ProcessorsCollection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1

```{
    "@odata.context": "/redfish/v1/$metadata#Processor.Processor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1",
    "@odata.type": "#Processor.v1_9_0.Processor",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "Description": "Represents the properties of a Processor attached to this System",
    "Id": "CPU.Socket.1",
    "InstructionSet": "x86-64",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        }
    },
    "Manufacturer": "Intel",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz",
    "Name": "CPU 1",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellAccelerators": null,
            "DellProcessor": {
                "@odata.context": "/redfish/v1/$metadata#DellProcessor.DellProcessor",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1/Oem/Dell/DellProcessors/CPU.Socket.1",
                "@odata.type": "#DellProcessor.v1_1_0.DellProcessor",
                "CPUFamily": "Intel(R)Xeon(TM)",
                "CPUStatus": "CPUEnabled",
                "Cache1Associativity": "12-WaySet-Associative",
                "Cache1ErrorMethodology": "Parity",
                "Cache1InstalledSizeKB": 2240,
                "Cache1Level": "L1",
                "Cache1Location": "Internal",
                "Cache1PrimaryStatus": "OK",
                "Cache1SRAMType": "Unknown",
                "Cache1SizeKB": 2240,
                "Cache1Type": "Unified",
                "Cache1WritePolicy": "WriteBack",
                "Cache2Associativity": "20-WaySet-Associative",
                "Cache2ErrorMethodology": "Single-bitECC",
                "Cache2InstalledSizeKB": 35840,
                "Cache2Level": "L2",
                "Cache2Location": "Internal",
                "Cache2PrimaryStatus": "OK",
                "Cache2SRAMType": "Unknown",
                "Cache2SizeKB": 35840,
                "Cache2Type": "Unified",
                "Cache2WritePolicy": "WriteBack",
                "Cache3Associativity": "12-WaySet-Associative",
                "Cache3ErrorMethodology": "Single-bitECC",
                "Cache3InstalledSizeKB": 43008,
                "Cache3Level": "L3",
                "Cache3Location": "Internal",
                "Cache3PrimaryStatus": "OK",
                "Cache3SRAMType": "Unknown",
                "Cache3SizeKB": 43008,
                "Cache3Type": "Unified",
                "Cache3WritePolicy": "WriteBack",
                "CurrentClockSpeedMhz": 2000,
                "ExternalBusClockSpeedMhz": 11200,
                "HyperThreadingCapable": "Yes",
                "HyperThreadingEnabled": "Yes",
                "Id": "CPU.Socket.1",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellProcessor",
                "TurboModeCapable": "Yes",
                "TurboModeEnabled": "Yes",
                "VirtualizationTechnologyCapable": "Yes",
                "VirtualizationTechnologyEnabled": "Yes",
                "Volts": "1.6"
            },
            "PowerMetrics": null,
            "ThermalMetrics": null
        }
    },
    "OperatingSpeedMHz": 2000,
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "6",
        "EffectiveModel": "106",
        "IdentificationRegisters": "0x000606A6",
        "MicrocodeInfo": "0xD0002B1",
        "Step": "6",
        "VendorId": "GenuineIntel"
    },
    "ProcessorType": "CPU",
    "Socket": "CPU.Socket.1",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TotalCores": 28,
    "TotalEnabledCores": 28,
    "TotalThreads": 56,
    "TurboState": "Enabled",
    "Version": "Model 106 Stepping 6"
}
```

## /redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1/Oem/Dell/DellProcessors/CPU.Socket.1

```{
    "@odata.context": "/redfish/v1/$metadata#DellProcessor.DellProcessor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1/Oem/Dell/DellProcessors/CPU.Socket.1",
    "@odata.type": "#DellProcessor.v1_1_0.DellProcessor",
    "CPUFamily": "Intel(R)Xeon(TM)",
    "CPUStatus": "CPUEnabled",
    "Cache1Associativity": "12-WaySet-Associative",
    "Cache1ErrorMethodology": "Parity",
    "Cache1InstalledSizeKB": 2240,
    "Cache1Level": "L1",
    "Cache1Location": "Internal",
    "Cache1PrimaryStatus": "OK",
    "Cache1SRAMType": "Unknown",
    "Cache1SizeKB": 2240,
    "Cache1Type": "Unified",
    "Cache1WritePolicy": "WriteBack",
    "Cache2Associativity": "20-WaySet-Associative",
    "Cache2ErrorMethodology": "Single-bitECC",
    "Cache2InstalledSizeKB": 35840,
    "Cache2Level": "L2",
    "Cache2Location": "Internal",
    "Cache2PrimaryStatus": "OK",
    "Cache2SRAMType": "Unknown",
    "Cache2SizeKB": 35840,
    "Cache2Type": "Unified",
    "Cache2WritePolicy": "WriteBack",
    "Cache3Associativity": "12-WaySet-Associative",
    "Cache3ErrorMethodology": "Single-bitECC",
    "Cache3InstalledSizeKB": 43008,
    "Cache3Level": "L3",
    "Cache3Location": "Internal",
    "Cache3PrimaryStatus": "OK",
    "Cache3SRAMType": "Unknown",
    "Cache3SizeKB": 43008,
    "Cache3Type": "Unified",
    "Cache3WritePolicy": "WriteBack",
    "CurrentClockSpeedMhz": 2000,
    "Description": "An instance of DellProcessor will have CPU specific data.",
    "ExternalBusClockSpeedMhz": 11200,
    "HyperThreadingCapable": "Yes",
    "HyperThreadingEnabled": "Yes",
    "Id": "CPU.Socket.1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "Name": "DellProcessor",
    "TurboModeCapable": "Yes",
    "TurboModeEnabled": "Yes",
    "VirtualizationTechnologyCapable": "Yes",
    "VirtualizationTechnologyEnabled": "Yes",
    "Volts": "1.6"
}
```

## /redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2

```{
    "@odata.context": "/redfish/v1/$metadata#Processor.Processor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2",
    "@odata.type": "#Processor.v1_9_0.Processor",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "Description": "Represents the properties of a Processor attached to this System",
    "Id": "CPU.Socket.2",
    "InstructionSet": "x86-64",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        }
    },
    "Manufacturer": "Intel",
    "MaxSpeedMHz": 4000,
    "Model": "Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz",
    "Name": "CPU 2",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellAccelerators": null,
            "DellProcessor": {
                "@odata.context": "/redfish/v1/$metadata#DellProcessor.DellProcessor",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2/Oem/Dell/DellProcessors/CPU.Socket.2",
                "@odata.type": "#DellProcessor.v1_1_0.DellProcessor",
                "CPUFamily": "Intel(R)Xeon(TM)",
                "CPUStatus": "CPUEnabled",
                "Cache1Associativity": "12-WaySet-Associative",
                "Cache1ErrorMethodology": "Parity",
                "Cache1InstalledSizeKB": 2240,
                "Cache1Level": "L1",
                "Cache1Location": "Internal",
                "Cache1PrimaryStatus": "OK",
                "Cache1SRAMType": "Unknown",
                "Cache1SizeKB": 2240,
                "Cache1Type": "Unified",
                "Cache1WritePolicy": "WriteBack",
                "Cache2Associativity": "20-WaySet-Associative",
                "Cache2ErrorMethodology": "Single-bitECC",
                "Cache2InstalledSizeKB": 35840,
                "Cache2Level": "L2",
                "Cache2Location": "Internal",
                "Cache2PrimaryStatus": "OK",
                "Cache2SRAMType": "Unknown",
                "Cache2SizeKB": 35840,
                "Cache2Type": "Unified",
                "Cache2WritePolicy": "WriteBack",
                "Cache3Associativity": "12-WaySet-Associative",
                "Cache3ErrorMethodology": "Single-bitECC",
                "Cache3InstalledSizeKB": 43008,
                "Cache3Level": "L3",
                "Cache3Location": "Internal",
                "Cache3PrimaryStatus": "OK",
                "Cache3SRAMType": "Unknown",
                "Cache3SizeKB": 43008,
                "Cache3Type": "Unified",
                "Cache3WritePolicy": "WriteBack",
                "CurrentClockSpeedMhz": 2000,
                "ExternalBusClockSpeedMhz": 11200,
                "HyperThreadingCapable": "Yes",
                "HyperThreadingEnabled": "Yes",
                "Id": "CPU.Socket.2",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2021-07-02T21:31:25+00:00",
                "Name": "DellProcessor",
                "TurboModeCapable": "Yes",
                "TurboModeEnabled": "Yes",
                "VirtualizationTechnologyCapable": "Yes",
                "VirtualizationTechnologyEnabled": "Yes",
                "Volts": "1.6"
            },
            "PowerMetrics": null,
            "ThermalMetrics": null
        }
    },
    "OperatingSpeedMHz": 2000,
    "ProcessorArchitecture": "x86",
    "ProcessorId": {
        "EffectiveFamily": "6",
        "EffectiveModel": "106",
        "IdentificationRegisters": "0x000606A6",
        "MicrocodeInfo": "0xD0002B1",
        "Step": "6",
        "VendorId": "GenuineIntel"
    },
    "ProcessorType": "CPU",
    "Socket": "CPU.Socket.2",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TotalCores": 28,
    "TotalEnabledCores": 28,
    "TotalThreads": 56,
    "TurboState": "Enabled",
    "Version": "Model 106 Stepping 6"
}
```

## /redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2/Oem/Dell/DellProcessors/CPU.Socket.2

```{
    "@odata.context": "/redfish/v1/$metadata#DellProcessor.DellProcessor",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2/Oem/Dell/DellProcessors/CPU.Socket.2",
    "@odata.type": "#DellProcessor.v1_1_0.DellProcessor",
    "CPUFamily": "Intel(R)Xeon(TM)",
    "CPUStatus": "CPUEnabled",
    "Cache1Associativity": "12-WaySet-Associative",
    "Cache1ErrorMethodology": "Parity",
    "Cache1InstalledSizeKB": 2240,
    "Cache1Level": "L1",
    "Cache1Location": "Internal",
    "Cache1PrimaryStatus": "OK",
    "Cache1SRAMType": "Unknown",
    "Cache1SizeKB": 2240,
    "Cache1Type": "Unified",
    "Cache1WritePolicy": "WriteBack",
    "Cache2Associativity": "20-WaySet-Associative",
    "Cache2ErrorMethodology": "Single-bitECC",
    "Cache2InstalledSizeKB": 35840,
    "Cache2Level": "L2",
    "Cache2Location": "Internal",
    "Cache2PrimaryStatus": "OK",
    "Cache2SRAMType": "Unknown",
    "Cache2SizeKB": 35840,
    "Cache2Type": "Unified",
    "Cache2WritePolicy": "WriteBack",
    "Cache3Associativity": "12-WaySet-Associative",
    "Cache3ErrorMethodology": "Single-bitECC",
    "Cache3InstalledSizeKB": 43008,
    "Cache3Level": "L3",
    "Cache3Location": "Internal",
    "Cache3PrimaryStatus": "OK",
    "Cache3SRAMType": "Unknown",
    "Cache3SizeKB": 43008,
    "Cache3Type": "Unified",
    "Cache3WritePolicy": "WriteBack",
    "CurrentClockSpeedMhz": 2000,
    "Description": "An instance of DellProcessor will have CPU specific data.",
    "ExternalBusClockSpeedMhz": 11200,
    "HyperThreadingCapable": "Yes",
    "HyperThreadingEnabled": "Yes",
    "Id": "CPU.Socket.2",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2021-07-02T21:31:25+00:00",
    "Name": "DellProcessor",
    "TurboModeCapable": "Yes",
    "TurboModeEnabled": "Yes",
    "VirtualizationTechnologyCapable": "Yes",
    "VirtualizationTechnologyEnabled": "Yes",
    "Volts": "1.6"
}
```

## /redfish/v1/Systems/System.Embedded.1/SecureBoot

```{
    "@odata.context": "/redfish/v1/$metadata#SecureBoot.SecureBoot",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SecureBoot",
    "@odata.type": "#SecureBoot.v1_1_0.SecureBoot",
    "Actions": {
        "#SecureBoot.ResetKeys": {
            "ResetKeysType@Redfish.AllowableValues": [
                "ResetAllKeysToDefault",
                "DeleteAllKeys",
                "DeletePK",
                "ResetPK",
                "ResetKEK",
                "ResetDB",
                "ResetDBX"
            ],
            "target": "/redfish/v1/Systems/System.Embedded.1/SecureBoot/Actions/SecureBoot.ResetKeys"
        },
        "Oem": {}
    },
    "Description": "UEFI Secure Boot",
    "Id": "SecureBoot",
    "Name": "UEFI Secure Boot",
    "Oem": {
        "Dell": {
            "@odata.context": "/redfish/v1/$metadata#DellSecureBoot.DellSecureBoot",
            "@odata.type": "#DellSecureBoot.v1_0_0.DellSecureBoot",
            "Certificates": {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SecureBoot/Oem/Dell/Certificates"
            }
        }
    },
    "SecureBootCurrentBoot": "Disabled",
    "SecureBootDatabases": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases"
    },
    "SecureBootEnable": false,
    "SecureBootMode": "DeployedMode"
}
```

## /redfish/v1/Systems/System.Embedded.1/SecureBoot/Oem/Dell/Certificates

```
```

## /redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases

```
```

## /redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases/KEK/Certificates/StdSecbootpolicy.2

```
```

## /redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases/PK/Certificates/StdSecbootpolicy.1

```
```

## /redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases/db/Certificates/StdSecbootpolicy.3

```
```

## /redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases/db/Certificates/StdSecbootpolicy.4

```
```

## /redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases/db/Certificates/StdSecbootpolicy.5

```
```

## /redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases/db/Certificates/StdSecbootpolicy.6

```
```

## /redfish/v1/Systems/System.Embedded.1/SimpleStorage

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorageCollection.SimpleStorageCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SimpleStorage",
    "@odata.type": "#SimpleStorageCollection.SimpleStorageCollection",
    "Description": "Collection of Controllers for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SimpleStorage/RAID.SL.3-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SimpleStorage/CPU.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SimpleStorage/AHCI.Embedded.2-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SimpleStorage/AHCI.Embedded.1-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SimpleStorage/AHCI.SL.6-1"
        }
    ],
    "Members@odata.count": 5,
    "Name": "Simple Storage Collection"
}
```

## /redfish/v1/Systems/System.Embedded.1/SimpleStorage/AHCI.Embedded.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorage.SimpleStorage",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SimpleStorage/AHCI.Embedded.1-1",
    "@odata.type": "#SimpleStorage.v1_2_3.SimpleStorage",
    "Description": "Simple Storage Controller",
    "Devices": [],
    "Devices@odata.count": 0,
    "Id": "AHCI.Embedded.1-1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        }
    },
    "Name": "C620 Series Chipset Family SSATA Controller [AHCI mode]",
    "Status": {
        "Health": null,
        "HealthRollup": null,
        "State": "Enabled"
    },
    "UefiDevicePath": "PciRoot(0x0)/Pci(0x11,0x5)"
}
```

## /redfish/v1/Systems/System.Embedded.1/SimpleStorage/AHCI.Embedded.2-1

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorage.SimpleStorage",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SimpleStorage/AHCI.Embedded.2-1",
    "@odata.type": "#SimpleStorage.v1_2_3.SimpleStorage",
    "Description": "Simple Storage Controller",
    "Devices": [],
    "Devices@odata.count": 0,
    "Id": "AHCI.Embedded.2-1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        }
    },
    "Name": "C620 Series Chipset Family SATA Controller [AHCI mode]",
    "Status": {
        "Health": null,
        "HealthRollup": null,
        "State": "Enabled"
    },
    "UefiDevicePath": "PciRoot(0x0)/Pci(0x17,0x0)"
}
```

## /redfish/v1/Systems/System.Embedded.1/SimpleStorage/AHCI.SL.6-1

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorage.SimpleStorage",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SimpleStorage/AHCI.SL.6-1",
    "@odata.type": "#SimpleStorage.v1_2_3.SimpleStorage",
    "Description": "Simple Storage Controller",
    "Devices": [
        {
            "CapacityBytes": 480103981056,
            "Manufacturer": "INTEL",
            "Model": "SSDSCKKB480G8R",
            "Name": "SSD 0",
            "Status": {
                "Health": "OK",
                "HealthRollup": "OK",
                "State": "Enabled"
            }
        },
        {
            "CapacityBytes": 480103981056,
            "Manufacturer": "INTEL",
            "Model": "SSDSCKKB480G8R",
            "Name": "SSD 1",
            "Status": {
                "Health": "OK",
                "HealthRollup": "OK",
                "State": "Enabled"
            }
        }
    ],
    "Devices@odata.count": 2,
    "Id": "AHCI.SL.6-1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        }
    },
    "Name": "BOSS-S2",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "UefiDevicePath": "PciRoot(0x0)/Pci(0x1D,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/System.Embedded.1/SimpleStorage/CPU.1

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorage.SimpleStorage",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SimpleStorage/CPU.1",
    "@odata.type": "#SimpleStorage.v1_2_3.SimpleStorage",
    "Description": "Simple Storage Controller",
    "Devices": [
        {
            "CapacityBytes": 1600321314816,
            "Manufacturer": "Samsung Electronics Co Ltd ",
            "Model": "Dell Ent NVMe v2 AGN MU U.2 1.6TB      ",
            "Name": "PCIe SSD in Slot 8 in Bay 1",
            "Status": {
                "Health": "OK",
                "HealthRollup": "OK",
                "State": "Enabled"
            }
        },
        {
            "CapacityBytes": 1600321314816,
            "Manufacturer": "Samsung Electronics Co Ltd ",
            "Model": "Dell Ent NVMe v2 AGN MU U.2 1.6TB      ",
            "Name": "PCIe SSD in Slot 9 in Bay 1",
            "Status": {
                "Health": "OK",
                "HealthRollup": "OK",
                "State": "Enabled"
            }
        },
        {
            "CapacityBytes": null,
            "Manufacturer": "DELL",
            "Model": "PCIe SSD Backplane 1",
            "Name": "PCIe SSD Backplane 1",
            "Status": {
                "Health": "OK",
                "HealthRollup": "OK",
                "State": "Enabled"
            }
        }
    ],
    "Devices@odata.count": 3,
    "Id": "CPU.1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        }
    },
    "Name": "CPU.1",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "UefiDevicePath": "PciRoot(0x5)/Pci(0x2,0x0)/Pci(0x0,0x0)"
}
```

## /redfish/v1/Systems/System.Embedded.1/SimpleStorage/RAID.SL.3-1

```{
    "@odata.context": "/redfish/v1/$metadata#SimpleStorage.SimpleStorage",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/SimpleStorage/RAID.SL.3-1",
    "@odata.type": "#SimpleStorage.v1_2_3.SimpleStorage",
    "Description": "Simple Storage Controller",
    "Devices": [
        {
            "CapacityBytes": 479559942144,
            "Manufacturer": "SKhynix",
            "Model": "HFS480G32FEH BA1",
            "Name": "Solid State Disk 0:1:1",
            "Status": {
                "Health": "OK",
                "HealthRollup": "OK",
                "State": "Enabled"
            }
        },
        {
            "CapacityBytes": 479559942144,
            "Manufacturer": "SKhynix",
            "Model": "HFS480G32FEH BA1",
            "Name": "Solid State Disk 0:1:0",
            "Status": {
                "Health": "OK",
                "HealthRollup": "OK",
                "State": "Enabled"
            }
        },
        {
            "CapacityBytes": null,
            "Manufacturer": "DELL",
            "Model": "BP15G+ 0:1",
            "Name": "Backplane 1 on Connector 0 of RAID Controller in SL 3",
            "Status": {
                "Health": "OK",
                "HealthRollup": "OK",
                "State": "Enabled"
            }
        }
    ],
    "Devices@odata.count": 3,
    "Id": "RAID.SL.3-1",
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        }
    },
    "Name": "PERC H745 Front",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "UefiDevicePath": "PciRoot(0x5)/Pci(0x4,0x0)/Pci(0x0,0x0)/Ctrl(0x1)"
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage

```{
    "@odata.context": "/redfish/v1/$metadata#StorageCollection.StorageCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage",
    "@odata.type": "#StorageCollection.StorageCollection",
    "Description": "Collection Of Storage entities",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.2-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.1-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1"
        }
    ],
    "Members@odata.count": 5,
    "Name": "Storage Collection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#Storage.Storage",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.1-1",
    "@odata.type": "#Storage.v1_8_1.Storage",
    "Description": "Embedded AHCI 1",
    "Drives": [],
    "Drives@odata.count": 0,
    "Id": "AHCI.Embedded.1-1",
    "Links": {
        "Enclosures": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Enclosures@odata.count": 1,
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [],
                "CPUAffinity@odata.count": 0
            }
        }
    },
    "Name": "C620 Series Chipset Family SSATA Controller [AHCI mode]",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellController": {
                "@odata.context": "/redfish/v1/$metadata#DellController.DellController",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.1-1/Oem/Dell/DellControllers/AHCI.Embedded.1-1",
                "@odata.type": "#DellController.v1_3_0.DellController",
                "AlarmState": "AlarmNotPresent",
                "AutoConfigBehavior": "NotApplicable",
                "BootVirtualDiskFQDD": null,
                "CacheSizeInMB": 0,
                "CachecadeCapability": "NotSupported",
                "ConnectorCount": 0,
                "ControllerFirmwareVersion": null,
                "CurrentControllerMode": "NotSupported",
                "Description": "An instance of DellController will have RAID Controller specific data.",
                "Device": "0",
                "DeviceCardDataBusWidth": "Unknown",
                "DeviceCardSlotLength": "Unknown",
                "DeviceCardSlotType": "Unknown",
                "DriverVersion": null,
                "EncryptionCapability": "None",
                "EncryptionMode": "None",
                "Id": "AHCI.Embedded.1-1",
                "KeyID": null,
                "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
                "LastUpdateTime": "2022-04-06T08:56:37+00:00",
                "MaxAvailablePCILinkSpeed": null,
                "MaxPossiblePCILinkSpeed": null,
                "Name": "DellController",
                "PCISlot": null,
                "PatrolReadState": "Unknown",
                "PersistentHotspare": "NotApplicable",
                "RealtimeCapability": "Incapable",
                "RollupStatus": "Unknown",
                "SASAddress": "0",
                "SecurityStatus": "EncryptionNotCapable",
                "SharedSlotAssignmentAllowed": "NotApplicable",
                "SlicedVDCapability": "NotSupported",
                "SupportControllerBootMode": "NotSupported",
                "SupportEnhancedAutoForeignImport": "NotSupported",
                "SupportRAID10UnevenSpans": "NotSupported",
                "SupportsLKMtoSEKMTransition": "No",
                "T10PICapability": "NotSupported"
            }
        }
    },
    "Status": {
        "Health": null,
        "HealthRollup": null,
        "State": "Enabled"
    },
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.1-1#/StorageControllers/0",
            "@odata.type": "#Storage.v1_8_1.StorageController",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "CacheSummary": {
                "TotalCacheSizeMiB": 0
            },
            "ControllerRates": {
                "ConsistencyCheckRatePercent": null,
                "RebuildRatePercent": null
            },
            "FirmwareVersion": "",
            "Identifiers": [
                {
                    "DurableName": null,
                    "DurableNameFormat": null
                }
            ],
            "Identifiers@odata.count": 1,
            "Links": {
                "PCIeFunctions": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17/PCIeFunctions/0-17-5"
                    }
                ],
                "PCIeFunctions@odata.count": 1
            },
            "Manufacturer": "DELL",
            "MemberId": "0",
            "Model": "C620 Series Chipset Family SSATA Controller [AHCI mode]",
            "Name": "C620 Series Chipset Family SSATA Controller [AHCI mode]",
            "Status": {
                "Health": null,
                "HealthRollup": null,
                "State": "Enabled"
            },
            "SupportedControllerProtocols": [
                "PCIe"
            ],
            "SupportedControllerProtocols@odata.count": 1,
            "SupportedDeviceProtocols": [],
            "SupportedDeviceProtocols@odata.count": 0,
            "SupportedRAIDTypes": [],
            "SupportedRAIDTypes@odata.count": 0
        }
    ],
    "StorageControllers@odata.count": 1,
    "Volumes": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.1-1/Volumes"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.1-1/Oem/Dell/DellControllers/AHCI.Embedded.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellController.DellController",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.1-1/Oem/Dell/DellControllers/AHCI.Embedded.1-1",
    "@odata.type": "#DellController.v1_3_0.DellController",
    "AlarmState": "AlarmNotPresent",
    "AutoConfigBehavior": "NotApplicable",
    "BootVirtualDiskFQDD": null,
    "CacheSizeInMB": 0,
    "CachecadeCapability": "NotSupported",
    "ConnectorCount": 0,
    "ControllerFirmwareVersion": null,
    "CurrentControllerMode": "NotSupported",
    "Description": "An instance of DellController will have RAID Controller specific data.",
    "Device": "0",
    "DeviceCardDataBusWidth": "Unknown",
    "DeviceCardSlotLength": "Unknown",
    "DeviceCardSlotType": "Unknown",
    "DriverVersion": null,
    "EncryptionCapability": "None",
    "EncryptionMode": "None",
    "Id": "AHCI.Embedded.1-1",
    "KeyID": null,
    "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
    "LastUpdateTime": "2022-04-06T08:56:37+00:00",
    "MaxAvailablePCILinkSpeed": null,
    "MaxPossiblePCILinkSpeed": null,
    "Name": "DellController",
    "PCISlot": null,
    "PatrolReadState": "Unknown",
    "PersistentHotspare": "NotApplicable",
    "RealtimeCapability": "Incapable",
    "RollupStatus": "Unknown",
    "SASAddress": "0",
    "SecurityStatus": "EncryptionNotCapable",
    "SharedSlotAssignmentAllowed": "NotApplicable",
    "SlicedVDCapability": "NotSupported",
    "SupportControllerBootMode": "NotSupported",
    "SupportEnhancedAutoForeignImport": "NotSupported",
    "SupportRAID10UnevenSpans": "NotSupported",
    "SupportsLKMtoSEKMTransition": "No",
    "T10PICapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.1-1/Volumes

```{
    "@Redfish.OperationApplyTimeSupport": {
        "@odata.type": "#Settings.v1_3_1.OperationApplyTimeSupport",
        "SupportedValues": [
            "OnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#VolumeCollection.VolumeCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.1-1/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection Of Volume",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Volume Collection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.2-1

```{
    "@odata.context": "/redfish/v1/$metadata#Storage.Storage",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.2-1",
    "@odata.type": "#Storage.v1_8_1.Storage",
    "Description": "Embedded AHCI 2",
    "Drives": [],
    "Drives@odata.count": 0,
    "Id": "AHCI.Embedded.2-1",
    "Links": {
        "Enclosures": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Enclosures@odata.count": 1,
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [],
                "CPUAffinity@odata.count": 0
            }
        }
    },
    "Name": "C620 Series Chipset Family SATA Controller [AHCI mode]",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellController": {
                "@odata.context": "/redfish/v1/$metadata#DellController.DellController",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.2-1/Oem/Dell/DellControllers/AHCI.Embedded.2-1",
                "@odata.type": "#DellController.v1_3_0.DellController",
                "AlarmState": "AlarmNotPresent",
                "AutoConfigBehavior": "NotApplicable",
                "BootVirtualDiskFQDD": null,
                "CacheSizeInMB": 0,
                "CachecadeCapability": "NotSupported",
                "ConnectorCount": 0,
                "ControllerFirmwareVersion": null,
                "CurrentControllerMode": "NotSupported",
                "Description": "An instance of DellController will have RAID Controller specific data.",
                "Device": "0",
                "DeviceCardDataBusWidth": "Unknown",
                "DeviceCardSlotLength": "Unknown",
                "DeviceCardSlotType": "Unknown",
                "DriverVersion": null,
                "EncryptionCapability": "None",
                "EncryptionMode": "None",
                "Id": "AHCI.Embedded.2-1",
                "KeyID": null,
                "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
                "LastUpdateTime": "2022-04-06T08:56:37+00:00",
                "MaxAvailablePCILinkSpeed": null,
                "MaxPossiblePCILinkSpeed": null,
                "Name": "DellController",
                "PCISlot": null,
                "PatrolReadState": "Unknown",
                "PersistentHotspare": "NotApplicable",
                "RealtimeCapability": "Incapable",
                "RollupStatus": "Unknown",
                "SASAddress": "0",
                "SecurityStatus": "EncryptionNotCapable",
                "SharedSlotAssignmentAllowed": "NotApplicable",
                "SlicedVDCapability": "NotSupported",
                "SupportControllerBootMode": "NotSupported",
                "SupportEnhancedAutoForeignImport": "NotSupported",
                "SupportRAID10UnevenSpans": "NotSupported",
                "SupportsLKMtoSEKMTransition": "No",
                "T10PICapability": "NotSupported"
            }
        }
    },
    "Status": {
        "Health": null,
        "HealthRollup": null,
        "State": "Enabled"
    },
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.2-1#/StorageControllers/0",
            "@odata.type": "#Storage.v1_8_1.StorageController",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "CacheSummary": {
                "TotalCacheSizeMiB": 0
            },
            "ControllerRates": {
                "ConsistencyCheckRatePercent": null,
                "RebuildRatePercent": null
            },
            "FirmwareVersion": "",
            "Identifiers": [
                {
                    "DurableName": null,
                    "DurableNameFormat": null
                }
            ],
            "Identifiers@odata.count": 1,
            "Links": {
                "PCIeFunctions": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23/PCIeFunctions/0-23-0"
                    }
                ],
                "PCIeFunctions@odata.count": 1
            },
            "Manufacturer": "DELL",
            "MemberId": "0",
            "Model": "C620 Series Chipset Family SATA Controller [AHCI mode]",
            "Name": "C620 Series Chipset Family SATA Controller [AHCI mode]",
            "Status": {
                "Health": null,
                "HealthRollup": null,
                "State": "Enabled"
            },
            "SupportedControllerProtocols": [
                "PCIe"
            ],
            "SupportedControllerProtocols@odata.count": 1,
            "SupportedDeviceProtocols": [],
            "SupportedDeviceProtocols@odata.count": 0,
            "SupportedRAIDTypes": [],
            "SupportedRAIDTypes@odata.count": 0
        }
    ],
    "StorageControllers@odata.count": 1,
    "Volumes": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.2-1/Volumes"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.2-1/Oem/Dell/DellControllers/AHCI.Embedded.2-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellController.DellController",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.2-1/Oem/Dell/DellControllers/AHCI.Embedded.2-1",
    "@odata.type": "#DellController.v1_3_0.DellController",
    "AlarmState": "AlarmNotPresent",
    "AutoConfigBehavior": "NotApplicable",
    "BootVirtualDiskFQDD": null,
    "CacheSizeInMB": 0,
    "CachecadeCapability": "NotSupported",
    "ConnectorCount": 0,
    "ControllerFirmwareVersion": null,
    "CurrentControllerMode": "NotSupported",
    "Description": "An instance of DellController will have RAID Controller specific data.",
    "Device": "0",
    "DeviceCardDataBusWidth": "Unknown",
    "DeviceCardSlotLength": "Unknown",
    "DeviceCardSlotType": "Unknown",
    "DriverVersion": null,
    "EncryptionCapability": "None",
    "EncryptionMode": "None",
    "Id": "AHCI.Embedded.2-1",
    "KeyID": null,
    "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
    "LastUpdateTime": "2022-04-06T08:56:37+00:00",
    "MaxAvailablePCILinkSpeed": null,
    "MaxPossiblePCILinkSpeed": null,
    "Name": "DellController",
    "PCISlot": null,
    "PatrolReadState": "Unknown",
    "PersistentHotspare": "NotApplicable",
    "RealtimeCapability": "Incapable",
    "RollupStatus": "Unknown",
    "SASAddress": "0",
    "SecurityStatus": "EncryptionNotCapable",
    "SharedSlotAssignmentAllowed": "NotApplicable",
    "SlicedVDCapability": "NotSupported",
    "SupportControllerBootMode": "NotSupported",
    "SupportEnhancedAutoForeignImport": "NotSupported",
    "SupportRAID10UnevenSpans": "NotSupported",
    "SupportsLKMtoSEKMTransition": "No",
    "T10PICapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.2-1/Volumes

```{
    "@Redfish.OperationApplyTimeSupport": {
        "@odata.type": "#Settings.v1_3_1.OperationApplyTimeSupport",
        "SupportedValues": [
            "OnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#VolumeCollection.VolumeCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.2-1/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection Of Volume",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Volume Collection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1

```{
    "@odata.context": "/redfish/v1/$metadata#Storage.Storage",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1",
    "@odata.type": "#Storage.v1_8_1.Storage",
    "Description": "AHCI controller in SL 6",
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1/Drives/Disk.Direct.0-0:AHCI.SL.6-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1/Drives/Disk.Direct.1-1:AHCI.SL.6-1"
        }
    ],
    "Drives@odata.count": 2,
    "Id": "AHCI.SL.6-1",
    "Links": {
        "Enclosures": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Enclosures@odata.count": 1,
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [],
                "CPUAffinity@odata.count": 0
            }
        }
    },
    "Name": "BOSS-S2",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellController": {
                "@odata.context": "/redfish/v1/$metadata#DellController.DellController",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1/Oem/Dell/DellControllers/AHCI.SL.6-1",
                "@odata.type": "#DellController.v1_3_0.DellController",
                "AlarmState": "AlarmNotSupported",
                "AutoConfigBehavior": "NotApplicable",
                "BootVirtualDiskFQDD": null,
                "CacheSizeInMB": 0,
                "CachecadeCapability": "NotSupported",
                "ConnectorCount": 0,
                "ControllerFirmwareVersion": "2.5.13.4008",
                "CurrentControllerMode": "NotSupported",
                "Description": "An instance of DellController will have RAID Controller specific data.",
                "Device": "0",
                "DeviceCardDataBusWidth": "Unknown",
                "DeviceCardSlotLength": "Unknown",
                "DeviceCardSlotType": "Unknown",
                "DriverVersion": null,
                "EncryptionCapability": "None",
                "EncryptionMode": "None",
                "Id": "AHCI.SL.6-1",
                "KeyID": null,
                "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
                "LastUpdateTime": "2022-04-06T08:56:37+00:00",
                "MaxAvailablePCILinkSpeed": null,
                "MaxPossiblePCILinkSpeed": null,
                "Name": "DellController",
                "PCISlot": null,
                "PatrolReadState": "Unknown",
                "PersistentHotspare": "NotApplicable",
                "RealtimeCapability": "Incapable",
                "RollupStatus": "OK",
                "SASAddress": "0",
                "SecurityStatus": "EncryptionNotCapable",
                "SharedSlotAssignmentAllowed": "NotApplicable",
                "SlicedVDCapability": "NotSupported",
                "SupportControllerBootMode": "NotSupported",
                "SupportEnhancedAutoForeignImport": "NotSupported",
                "SupportRAID10UnevenSpans": "NotSupported",
                "SupportsLKMtoSEKMTransition": "No",
                "T10PICapability": "NotSupported"
            }
        }
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1#/StorageControllers/0",
            "@odata.type": "#Storage.v1_8_1.StorageController",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "CacheSummary": {
                "TotalCacheSizeMiB": 0
            },
            "ControllerRates": {
                "ConsistencyCheckRatePercent": null,
                "RebuildRatePercent": null
            },
            "FirmwareVersion": "2.5.13.4008",
            "Identifiers": [
                {
                    "DurableName": null,
                    "DurableNameFormat": null
                }
            ],
            "Identifiers@odata.count": 1,
            "Links": {
                "PCIeFunctions": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0/PCIeFunctions/5-0-0"
                    }
                ],
                "PCIeFunctions@odata.count": 1
            },
            "Manufacturer": "DELL",
            "MemberId": "0",
            "Model": "BOSS-S2",
            "Name": "BOSS-S2",
            "SpeedGbps": 6,
            "Status": {
                "Health": "OK",
                "HealthRollup": "OK",
                "State": "Enabled"
            },
            "SupportedControllerProtocols": [
                "PCIe"
            ],
            "SupportedControllerProtocols@odata.count": 1,
            "SupportedDeviceProtocols": [
                "SATA"
            ],
            "SupportedDeviceProtocols@odata.count": 1,
            "SupportedRAIDTypes": [
                "RAID1"
            ],
            "SupportedRAIDTypes@odata.count": 1
        }
    ],
    "StorageControllers@odata.count": 1,
    "Volumes": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1/Volumes"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1/Oem/Dell/DellControllers/AHCI.SL.6-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellController.DellController",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1/Oem/Dell/DellControllers/AHCI.SL.6-1",
    "@odata.type": "#DellController.v1_3_0.DellController",
    "AlarmState": "AlarmNotSupported",
    "AutoConfigBehavior": "NotApplicable",
    "BootVirtualDiskFQDD": null,
    "CacheSizeInMB": 0,
    "CachecadeCapability": "NotSupported",
    "ConnectorCount": 0,
    "ControllerFirmwareVersion": "2.5.13.4008",
    "CurrentControllerMode": "NotSupported",
    "Description": "An instance of DellController will have RAID Controller specific data.",
    "Device": "0",
    "DeviceCardDataBusWidth": "Unknown",
    "DeviceCardSlotLength": "Unknown",
    "DeviceCardSlotType": "Unknown",
    "DriverVersion": null,
    "EncryptionCapability": "None",
    "EncryptionMode": "None",
    "Id": "AHCI.SL.6-1",
    "KeyID": null,
    "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
    "LastUpdateTime": "2022-04-06T08:56:37+00:00",
    "MaxAvailablePCILinkSpeed": null,
    "MaxPossiblePCILinkSpeed": null,
    "Name": "DellController",
    "PCISlot": null,
    "PatrolReadState": "Unknown",
    "PersistentHotspare": "NotApplicable",
    "RealtimeCapability": "Incapable",
    "RollupStatus": "OK",
    "SASAddress": "0",
    "SecurityStatus": "EncryptionNotCapable",
    "SharedSlotAssignmentAllowed": "NotApplicable",
    "SlicedVDCapability": "NotSupported",
    "SupportControllerBootMode": "NotSupported",
    "SupportEnhancedAutoForeignImport": "NotSupported",
    "SupportRAID10UnevenSpans": "NotSupported",
    "SupportsLKMtoSEKMTransition": "No",
    "T10PICapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1/Volumes

```{
    "@Redfish.OperationApplyTimeSupport": {
        "@odata.type": "#Settings.v1_3_1.OperationApplyTimeSupport",
        "SupportedValues": [
            "OnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#VolumeCollection.VolumeCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection Of Volume",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1/Volumes/Disk.Virtual.0:AHCI.SL.6-1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Volume Collection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage/CPU.1

```{
    "@odata.context": "/redfish/v1/$metadata#Storage.Storage",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1",
    "@odata.type": "#Storage.v1_8_1.Storage",
    "Description": "CPU.1",
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1/Drives/Disk.Bay.8:Enclosure.Internal.0-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1/Drives/Disk.Bay.9:Enclosure.Internal.0-1"
        }
    ],
    "Drives@odata.count": 2,
    "Id": "CPU.1",
    "Links": {
        "Enclosures": [
            {
                "@odata.id": "/redfish/v1/Chassis/Enclosure.Internal.0-1"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Enclosures@odata.count": 2,
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [],
                "CPUAffinity@odata.count": 0
            }
        }
    },
    "Name": "CPU.1",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "Volumes": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1/Volumes"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage/CPU.1/Volumes

```{
    "@Redfish.OperationApplyTimeSupport": {
        "@odata.type": "#Settings.v1_3_1.OperationApplyTimeSupport",
        "SupportedValues": [
            "OnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#VolumeCollection.VolumeCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection Of Volume",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1/Volumes/Disk.Bay.8:Enclosure.Internal.0-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1/Volumes/Disk.Bay.9:Enclosure.Internal.0-1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Volume Collection"
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1

```{
    "@odata.context": "/redfish/v1/$metadata#Storage.Storage",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1",
    "@odata.type": "#Storage.v1_8_1.Storage",
    "Description": "RAID Controller in SL 3",
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1/Drives/Disk.Bay.1:Enclosure.Internal.0-1:RAID.SL.3-1"
        },
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1/Drives/Disk.Bay.0:Enclosure.Internal.0-1:RAID.SL.3-1"
        }
    ],
    "Drives@odata.count": 2,
    "Id": "RAID.SL.3-1",
    "Links": {
        "Enclosures": [
            {
                "@odata.id": "/redfish/v1/Chassis/Enclosure.Internal.0-1:RAID.SL.3-1"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "Enclosures@odata.count": 2,
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1
            }
        }
    },
    "Name": "PERC H745 Front",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellController": {
                "@odata.context": "/redfish/v1/$metadata#DellController.DellController",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1/Oem/Dell/DellControllers/RAID.SL.3-1",
                "@odata.type": "#DellController.v1_3_0.DellController",
                "AlarmState": "AlarmNotPresent",
                "AutoConfigBehavior": "Off",
                "BootVirtualDiskFQDD": null,
                "CacheSizeInMB": 4096,
                "CachecadeCapability": "NotSupported",
                "ConnectorCount": 4,
                "ControllerFirmwareVersion": "51.14.0-3900",
                "CurrentControllerMode": "RAID",
                "Description": "An instance of DellController will have RAID Controller specific data.",
                "Device": "0",
                "DeviceCardDataBusWidth": "Unknown",
                "DeviceCardSlotLength": "Unknown",
                "DeviceCardSlotType": "Unknown",
                "DriverVersion": "7.713.08.00",
                "EncryptionCapability": "LocalKeyManagementAndSecureEnterpriseKeyManagerCapable",
                "EncryptionMode": "None",
                "Id": "RAID.SL.3-1",
                "KeyID": null,
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-08-30T23:00:48+00:00",
                "MaxAvailablePCILinkSpeed": null,
                "MaxPossiblePCILinkSpeed": null,
                "Name": "DellController",
                "PCISlot": null,
                "PatrolReadState": "Stopped",
                "PersistentHotspare": "Disabled",
                "RealtimeCapability": "Capable",
                "RollupStatus": "OK",
                "SASAddress": "5B07B250D514E600",
                "SecurityStatus": "EncryptionCapable",
                "SharedSlotAssignmentAllowed": "NotApplicable",
                "SlicedVDCapability": "Supported",
                "SupportControllerBootMode": "NotSupported",
                "SupportEnhancedAutoForeignImport": "Supported",
                "SupportRAID10UnevenSpans": "Supported",
                "SupportsLKMtoSEKMTransition": "No",
                "T10PICapability": "NotSupported"
            },
            "DellControllerBattery": {
                "@odata.context": "/redfish/v1/$metadata#DellControllerBattery.DellControllerBattery",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1/Oem/Dell/DellControllerBattery/Battery.Integrated.1:RAID.SL.3-1",
                "@odata.type": "#DellControllerBattery.v1_0_0.DellControllerBattery",
                "Description": "An instance of DellController will have RAID Controller specific data.",
                "FQDD": "Battery.Integrated.1:RAID.SL.3-1",
                "Id": "Battery.Integrated.1:RAID.SL.3-1",
                "Name": "Battery on RAID Controller in SL 3",
                "PrimaryStatus": "OK",
                "RAIDState": "Ready"
            }
        }
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1#/StorageControllers/0",
            "@odata.type": "#Storage.v1_8_1.StorageController",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "CacheSummary": {
                "TotalCacheSizeMiB": 4096
            },
            "ControllerRates": {
                "ConsistencyCheckRatePercent": 30,
                "RebuildRatePercent": 30
            },
            "FirmwareVersion": "51.14.0-3900",
            "Identifiers": [
                {
                    "DurableName": "5b07b250d514e600",
                    "DurableNameFormat": "NAA"
                }
            ],
            "Identifiers@odata.count": 1,
            "Links": {
                "PCIeFunctions": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/103-0/PCIeFunctions/103-0-0"
                    }
                ],
                "PCIeFunctions@odata.count": 1
            },
            "Manufacturer": "DELL",
            "MemberId": "0",
            "Model": "PERC H745 Front",
            "Name": "PERC H745 Front",
            "SpeedGbps": 12,
            "Status": {
                "Health": "OK",
                "HealthRollup": "OK",
                "State": "Enabled"
            },
            "SupportedControllerProtocols": [
                "PCIe"
            ],
            "SupportedControllerProtocols@odata.count": 1,
            "SupportedDeviceProtocols": [
                "SAS",
                "SATA"
            ],
            "SupportedDeviceProtocols@odata.count": 2,
            "SupportedRAIDTypes": [
                "RAID0",
                "RAID1",
                "RAID5",
                "RAID6",
                "RAID10",
                "RAID50",
                "RAID60"
            ],
            "SupportedRAIDTypes@odata.count": 7
        }
    ],
    "StorageControllers@odata.count": 1,
    "Volumes": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1/Volumes"
    }
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1/Oem/Dell/DellControllers/RAID.SL.3-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellController.DellController",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1/Oem/Dell/DellControllers/RAID.SL.3-1",
    "@odata.type": "#DellController.v1_3_0.DellController",
    "AlarmState": "AlarmNotPresent",
    "AutoConfigBehavior": "Off",
    "BootVirtualDiskFQDD": null,
    "CacheSizeInMB": 4096,
    "CachecadeCapability": "NotSupported",
    "ConnectorCount": 4,
    "ControllerFirmwareVersion": "51.14.0-3900",
    "CurrentControllerMode": "RAID",
    "Description": "An instance of DellController will have RAID Controller specific data.",
    "Device": "0",
    "DeviceCardDataBusWidth": "Unknown",
    "DeviceCardSlotLength": "Unknown",
    "DeviceCardSlotType": "Unknown",
    "DriverVersion": "7.713.08.00",
    "EncryptionCapability": "LocalKeyManagementAndSecureEnterpriseKeyManagerCapable",
    "EncryptionMode": "None",
    "Id": "RAID.SL.3-1",
    "KeyID": null,
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2022-08-30T23:00:48+00:00",
    "MaxAvailablePCILinkSpeed": null,
    "MaxPossiblePCILinkSpeed": null,
    "Name": "DellController",
    "PCISlot": null,
    "PatrolReadState": "Stopped",
    "PersistentHotspare": "Disabled",
    "RealtimeCapability": "Capable",
    "RollupStatus": "OK",
    "SASAddress": "5B07B250D514E600",
    "SecurityStatus": "EncryptionCapable",
    "SharedSlotAssignmentAllowed": "NotApplicable",
    "SlicedVDCapability": "Supported",
    "SupportControllerBootMode": "NotSupported",
    "SupportEnhancedAutoForeignImport": "Supported",
    "SupportRAID10UnevenSpans": "Supported",
    "SupportsLKMtoSEKMTransition": "No",
    "T10PICapability": "NotSupported"
}
```

## /redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1/Volumes

```{
    "@Redfish.OperationApplyTimeSupport": {
        "@odata.type": "#Settings.v1_3_1.OperationApplyTimeSupport",
        "SupportedValues": [
            "Immediate",
            "OnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#VolumeCollection.VolumeCollection",
    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1/Volumes",
    "@odata.type": "#VolumeCollection.VolumeCollection",
    "Description": "Collection Of Volume",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Volume Collection"
}
```

