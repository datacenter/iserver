# Get resource

Resources in Redfish are defined with URI (link) typically starting with /redfish/v1/.

iserver supports full uri syntax e.g. /redfish/v1/Chassis/1/NetworkAdapters as well as shortened syntax e.g. Chassis/1/NetworkAdapters.

All properties of the requested resource are shown in JSON format.

Note: Resource properties can be fetched recursively when --deep option is defined. Check [here](./ResourceDeep.md) for more details.

## Get network adapters resource

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Chassis/1/NetworkAdapters

/redfish/v1/Chassis/1/NetworkAdapters
-------------------------------------
{
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters",
    "@odata.type": "#NetworkAdapterCollection.NetworkAdapterCollection",
    "@odata.context": "/redfish/v1/$metadata#NetworkAdapterCollection.NetworkAdapterCollection",
    "Description": "Collection of NetworkAdapter resource instances for this system",
    "Name": "NetworkAdapter Collection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1"
        }
    ],
    "Members@odata.count": 1
}
```

## Get storage controller resource

Depending on endpoint type, URI may contain system identifier value that is device specific. iserver supports uri syntax with SYSTEM_ID value that will be automatically replaced with proper system identifier.

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID/Storage/MRAID

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID
---------------------------------------------
{
    "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID",
    "@odata.type": "#Storage.v1_8_0.Storage",
    "@odata.context": "/redfish/v1/$metadata#Storage.Storage",
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
    "Volumes": {
        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes"
    },
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
    "Id": "MRAID",
    "Name": "MRAID",
    "StorageControllers": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID",
            "SupportedControllerProtocols": [
                "PCIe"
            ],
            "SupportedDeviceProtocols": [
                "SATA",
                "SAS"
            ],
            "MemberId": "MRAID",
            "Model": "UCSC-RAID-M5",
            "Name": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
            "FirmwareVersion": "51.10.0-3612",
            "Manufacturer": "Cisco Systems Inc",
            "SupportedRAIDTypes": [
                "RAID0",
                "RAID1",
                "RAID5",
                "RAID6",
                "RAID10",
                "RAID50",
                "RAID60"
            ],
            "SerialNumber": "SK00481450",
            "CacheSummary": {
                "PersistentCacheSizeMiB": 1332,
                "TotalCacheSizeMiB": 2048
            },
            "Oem": {
                "Cisco": {
                    "StorageControllerBiosVersion": "7.10.03.1_0x070A0402",
                    "PCIeSlot": "MRAID",
                    "ChipRevision": "08004",
                    "StorageInstanceId": 8,
                    "ControllerInterfaceType": "Sas",
                    "ControllerStatus": "Optimal",
                    "StorageControllerDefaultDriveMode": "UnConfiguredGood",
                    "HasForeignConfig": false,
                    "DefaultStripeSizeKiBytes": 64,
                    "SupportedStripeSizesKiBytes": [
                        64,
                        128,
                        256,
                        512,
                        1024
                    ],
                    "JbodMode": true,
                    "MaximumVolumesPerController": 64,
                    "ControllerType": "Raid",
                    "FullDiskEncryptionCapable": true,
                    "ControllerEncryptionEnabled": false,
                    "EccBucketLeakRate": 1440,
                    "ConnectedSasExpander": true,
                    "MemoryCorrectableErrors": 0,
                    "PinnedCacheState": 0,
                    "RebuildRatePercent": 30,
                    "SubOEMId": 3,
                    "BootDevices": [
                        "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/0"
                    ],
                    "Bbu": {
                        "BbuDeviceName": "CVPM05",
                        "BbuVendor": "LSI",
                        "BbuManufacturingDate": "2019-12-26",
                        "BbuModuleVersion": "05668-01",
                        "BbuSerialNumber": 22303,
                        "BbuType": "TMMC",
                        "BbuStatus": "Optimal",
                        "BbuChargingState": "Unknown",
                        "IsCapacitor": true,
                        "BbuDesignVoltageInVolts": 9.5,
                        "BbuVoltageInVolts": 12.497,
                        "BbuCurrentInAmps": 0,
                        "BbuTemperatureInCel": 22,
                        "IsVoltageLow": false,
                        "IsTemperatureHigh": false,
                        "IsBatteryPresent": true,
                        "IsLearnCycleTransparent": true,
                        "LearnMode": "Auto",
                        "LearnCycleProgressStatus": "Success",
                        "LearnCycleProgressStartTimeStamp": "1668451804",
                        "LearnCycleProgressEndTimeStamp": "1668451929",
                        "NextLearnCycleTimeStamp": "2022-12-12 17:51",
                        "IsLearnCycleRequested": false,
                        "CapacitanceInPercent": 100,
                        "DesignCapacityInJoules": 306,
                        "PackEnergyInJoules": 616,
                        "RemainingPoolSpaceInPercent": 0
                    }
                }
            },
            "Status": {
                "State": "Enabled",
                "Health": "OK",
                "HealthRollup": "OK"
            },
            "Location": {
                "PartLocation": {
                    "LocationType": "Slot",
                    "ServiceLabel": "MRAID"
                }
            }
        }
    ],
    "Actions": {
        "Oem": {
            "#Cisco.EncryptionOp": {
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.EncryptionOp",
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.EncryptionOp",
                "EnOpName@Redfish.AllowableValues": [
                    "Enable",
                    "Disable",
                    "Migrate",
                    "Modify",
                    "Unlock"
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
                "EncryptionKey@Redfish.AllowableValues": [
                    "A unique string generated by requester, min is 1 and max is 32"
                ],
                "DriveEncryptionModeRemote@Redfish.AllowableValues": [
                    true,
                    false
                ]
            },
            "#Cisco.ClearConfig": {
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.ClearConfig",
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ClearConfig"
            },
            "#Cisco.DoForeignConfig": {
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.DoForeignConfig",
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.DoForeignConfig",
                "ForeignCfgOp@Redfish.AllowableValues": [
                    "Clear",
                    "Import"
                ]
            },
            "#Cisco.ResetToFactoryDefaults": {
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.ResetToFactoryDefaults",
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetToFactoryDefaults"
            },
            "#Cisco.UnpinCache": {
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.UnpinCache",
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UnpinCache",
                "DiscardType@Redfish.AllowableValues": [
                    "all",
                    "missing"
                ]
            },
            "#Cisco.GetLogs": {
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.GetLogs",
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.GetLogs",
                "OutputFile@Redfish.AllowableValues": [
                    "A string of length between 1-64 alpha numeric characters for output file name"
                ]
            },
            "#Cisco.BbuStartLearnCycle": {
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.BbuStartLearnCycle",
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.BbuStartLearnCycle"
            }
        }
    }
}
```