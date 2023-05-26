# Resource: /redfish/v1/UpdateService

Vendor | Model
--- | ---
HPE | vServer

## /redfish/v1/UpdateService

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService.UpdateService",
    "@odata.etag": "W/\"15AD0341\"",
    "@odata.id": "/redfish/v1/UpdateService",
    "@odata.type": "#UpdateService.v1_1_1.UpdateService",
    "Actions": {
        "#UpdateService.SimpleUpdate": {
            "TransferProtocol@Redfish.AllowableValues": [
                "HTTP",
                "HTTPS"
            ],
            "target": "/redfish/v1/UpdateService/Actions/UpdateService.SimpleUpdate"
        }
    },
    "Description": "iLO Update Service",
    "FirmwareInventory": {
        "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory"
    },
    "HttpPushUri": "/cgi-bin/uploadFile",
    "Id": "UpdateService",
    "Name": "Update Service",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOUpdateServiceExt.HpeiLOUpdateServiceExt",
            "@odata.type": "#HpeiLOUpdateServiceExt.v2_1_4.HpeiLOUpdateServiceExt",
            "Accept3rdPartyFirmware": false,
            "Actions": {
                "#HpeiLOUpdateServiceExt.AddFromUri": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.AddFromUri"
                },
                "#HpeiLOUpdateServiceExt.DeleteInstallSets": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.DeleteInstallSets"
                },
                "#HpeiLOUpdateServiceExt.DeleteMaintenanceWindows": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.DeleteMaintenanceWindows"
                },
                "#HpeiLOUpdateServiceExt.DeleteUnlockedComponents": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.DeleteUnlockedComponents"
                },
                "#HpeiLOUpdateServiceExt.DeleteUpdateTaskQueueItems": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.DeleteUpdateTaskQueueItems"
                },
                "#HpeiLOUpdateServiceExt.RemoveLanguagePack": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.RemoveLanguagePack"
                },
                "#HpeiLOUpdateServiceExt.SetDefaultLanguage": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.SetDefaultLanguage"
                },
                "#HpeiLOUpdateServiceExt.StartFirmwareIntegrityCheck": {
                    "target": "/redfish/v1/UpdateService/Actions/Oem/Hpe/HpeiLOUpdateServiceExt.StartFirmwareIntegrityCheck"
                }
            },
            "Capabilities": {
                "PLDMFirmwareUpdate": true,
                "UpdateFWPKG": true
            },
            "ComponentRepository": {
                "@odata.id": "/redfish/v1/UpdateService/ComponentRepository"
            },
            "CurrentTime": "2022-08-03T17:14:57Z",
            "DowngradePolicy": "AllowDowngrade",
            "FirmwareIntegrity": {
                "EnableBackgroundScan": false,
                "LastScanResult": "OK",
                "LastScanTime": "1970-01-01T00:02:04Z",
                "OnIntegrityFailure": "LogOnly",
                "ScanEveryDays": 7
            },
            "InstallSets": {
                "@odata.id": "/redfish/v1/UpdateService/InstallSets"
            },
            "InvalidImageRepository": {
                "@odata.id": "/redfish/v1/UpdateService/InvalidImageRepository"
            },
            "MaintenanceWindows": {
                "@odata.id": "/redfish/v1/UpdateService/MaintenanceWindows"
            },
            "State": "Idle",
            "UpdateTaskQueue": {
                "@odata.id": "/redfish/v1/UpdateService/UpdateTaskQueue"
            }
        }
    },
    "ServiceEnabled": true,
    "SoftwareInventory": {
        "@odata.id": "/redfish/v1/UpdateService/SoftwareInventory"
    }
}
```

## /redfish/v1/UpdateService/ComponentRepository

```{
    "@odata.context": "/redfish/v1/$metadata#HpeComponentCollection.HpeComponentCollection",
    "@odata.etag": "W/\"C081AB46\"",
    "@odata.id": "/redfish/v1/UpdateService/ComponentRepository",
    "@odata.type": "#HpeComponentCollection.HpeComponentCollection",
    "Description": "Component Collection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/UpdateService/ComponentRepository/224c0cdf"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/ComponentRepository/7d70dc89"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/ComponentRepository/3e96efee"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/ComponentRepository/59018d2e"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/ComponentRepository/52a0a2f4"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/ComponentRepository/bebf97fe"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/ComponentRepository/6c508f1b"
        }
    ],
    "Members@odata.count": 7,
    "Name": "Component Collection",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeComponentRepositoryInformation.HpeComponentRepositoryInformation",
            "@odata.type": "#HpeComponentRepositoryInformation.v2_0_0.HpeComponentRepositoryInformation",
            "ComponentCount": 7,
            "FreeSizeBytes": 920829952,
            "TotalSizeBytes": 1073168384
        }
    }
}
```

## /redfish/v1/UpdateService/ComponentRepository/224c0cdf

```{
    "@odata.context": "/redfish/v1/$metadata#HpeComponent.HpeComponent",
    "@odata.etag": "W/\"CD21D410\"",
    "@odata.id": "/redfish/v1/UpdateService/ComponentRepository/224c0cdf",
    "@odata.type": "#HpeComponent.v1_0_1.HpeComponent",
    "Activates": "AfterDeviceReset",
    "ComponentUri": "/fwrepo/ilo5_244.bin",
    "Configuration": "",
    "Created": "2021-08-18T06:42:29Z",
    "Criticality": "Optional",
    "DeviceClass": "2f317b9d-c9e3-4d76-bff6-b9d0d085a952",
    "ExecutionParameters": "",
    "Filename": "ilo5_244.bin",
    "Filepath": "ilo5_244.bin",
    "Id": "224c0cdf",
    "Locked": true,
    "Name": "iLO 5",
    "SizeBytes": 33557060,
    "Targets": [
        "c0bcf2b9-1141-49af-aab8-c73791f0349c"
    ],
    "UpdatableBy": [
        "Bmc"
    ],
    "Version": "2.44"
}
```

## /redfish/v1/UpdateService/ComponentRepository/3e96efee

```{
    "@odata.context": "/redfish/v1/$metadata#HpeComponent.HpeComponent",
    "@odata.etag": "W/\"CD21D410\"",
    "@odata.id": "/redfish/v1/UpdateService/ComponentRepository/3e96efee",
    "@odata.type": "#HpeComponent.v1_0_1.HpeComponent",
    "Activates": "AfterHardPowerCycle",
    "ComponentUri": "/fwrepo/CPLD_DL360_DL380_Gen10Plus_v1515_signed.vme",
    "Configuration": "",
    "Created": "2021-08-18T06:44:42Z",
    "Criticality": "Optional",
    "DeviceClass": "b1ad439a-9dd1-41c1-a496-2da9313f1f07",
    "ExecutionParameters": "",
    "Filename": "CPLD_DL360_DL380_Gen10Plus_v1515_signed.vme",
    "Filepath": "CPLD_DL360_DL380_Gen10Plus_v1515_signed.vme",
    "Id": "3e96efee",
    "Locked": true,
    "Name": "System Programmable Logic Device",
    "SizeBytes": 925363,
    "Targets": [
        "00000000-0000-0000-0000-00000000022c",
        "00000000-0000-0000-0000-000000000226",
        "00000000-0000-0000-0000-000000000225"
    ],
    "UpdatableBy": [
        "Bmc"
    ],
    "Version": "15"
}
```

## /redfish/v1/UpdateService/ComponentRepository/52a0a2f4

```{
    "@odata.context": "/redfish/v1/$metadata#HpeComponent.HpeComponent",
    "@odata.etag": "W/\"CD21D410\"",
    "@odata.id": "/redfish/v1/UpdateService/ComponentRepository/52a0a2f4",
    "@odata.type": "#HpeComponent.v1_0_1.HpeComponent",
    "Activates": "AfterReboot",
    "ComponentUri": "/fwrepo/SPSGEN10PLUS_04.04.04.053.signed.bin",
    "Configuration": "",
    "Created": "2021-08-18T06:45:22Z",
    "Criticality": "Optional",
    "DeviceClass": "b34e5677-21dc-45d3-872b-42f76fee9053",
    "ExecutionParameters": "",
    "Filename": "SPSGEN10PLUS_04.04.04.053.signed.bin",
    "Filepath": "SPSGEN10PLUS_04.04.04.053.signed.bin",
    "Id": "52a0a2f4",
    "Locked": true,
    "Name": "Server Platform Services (SPS) Firmware",
    "SizeBytes": 8391535,
    "Targets": [
        "a6b1a447-382a-5a4f-3c10-87800a000101"
    ],
    "UpdatableBy": [
        "Bmc"
    ],
    "Version": "04.04.04.053"
}
```

## /redfish/v1/UpdateService/ComponentRepository/59018d2e

```{
    "@odata.context": "/redfish/v1/$metadata#HpeComponent.HpeComponent",
    "@odata.etag": "W/\"CD21D410\"",
    "@odata.id": "/redfish/v1/UpdateService/ComponentRepository/59018d2e",
    "@odata.type": "#HpeComponent.v1_0_1.HpeComponent",
    "Activates": "Immediately",
    "ComponentUri": "/fwrepo/IEGen10Plus_1.0.0.20.signed.bin",
    "Configuration": "",
    "Created": "2021-08-18T06:45:00Z",
    "Criticality": "Optional",
    "DeviceClass": "c734e171-8721-48c9-9ed6-d5bc7da5ef8d",
    "ExecutionParameters": "",
    "Filename": "IEGen10Plus_1.0.0.20.signed.bin",
    "Filepath": "IEGen10Plus_1.0.0.20.signed.bin",
    "Id": "59018d2e",
    "Locked": true,
    "Name": "Innovation Engine (IE) Universal Image",
    "SizeBytes": 8391545,
    "Targets": [
        "a6b1a447-382a-5a4f-3c10-87800a000303"
    ],
    "UpdatableBy": [
        "Bmc"
    ],
    "Version": "1.0.0.20"
}
```

## /redfish/v1/UpdateService/ComponentRepository/6c508f1b

```{
    "@odata.context": "/redfish/v1/$metadata#HpeComponent.HpeComponent",
    "@odata.etag": "W/\"CD21D410\"",
    "@odata.id": "/redfish/v1/UpdateService/ComponentRepository/6c508f1b",
    "@odata.type": "#HpeComponent.v1_0_1.HpeComponent",
    "Activates": "Immediately",
    "ComponentUri": "/fwrepo/ilo5_255.fwpkg",
    "Configuration": "",
    "Created": "2022-02-25T18:07:31Z",
    "Criticality": "Optional",
    "DeviceClass": "2f317b9d-c9e3-4d76-bff6-b9d0d085a952",
    "ExecutionParameters": "",
    "Filename": "ilo5_255.fwpkg",
    "Filepath": "ilo5_255.fwpkg",
    "Id": "6c508f1b",
    "Locked": false,
    "Name": "Online ROM Flash Firmware Package - HPE Integrated Lights-Out 5",
    "SizeBytes": 33604630,
    "Targets": [
        "c0bcf2b9-1141-49af-aab8-c73791f0349c"
    ],
    "UpdatableBy": [
        "Bmc"
    ],
    "Version": "2.55"
}
```

## /redfish/v1/UpdateService/ComponentRepository/7d70dc89

```{
    "@odata.context": "/redfish/v1/$metadata#HpeComponent.HpeComponent",
    "@odata.etag": "W/\"CD21D410\"",
    "@odata.id": "/redfish/v1/UpdateService/ComponentRepository/7d70dc89",
    "@odata.type": "#HpeComponent.v1_0_1.HpeComponent",
    "Activates": "AfterReboot",
    "ComponentUri": "/fwrepo/U46_1.42_05_26_2021.signed.flash",
    "Configuration": "",
    "Created": "2021-08-18T06:44:35Z",
    "Criticality": "Optional",
    "DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
    "ExecutionParameters": "",
    "Filename": "U46_1.42_05_26_2021.signed.flash",
    "Filepath": "U46_1.42_05_26_2021.signed.flash",
    "Id": "7d70dc89",
    "Locked": true,
    "Name": "System BIOS - U46",
    "SizeBytes": 33564540,
    "Targets": [
        "00000000-0000-0000-0000-000000000225",
        "00000000-0000-0000-0000-000000000226",
        "00000000-0000-0000-0000-00000000022c"
    ],
    "UpdatableBy": [
        "Bmc"
    ],
    "Version": "v1.42 (05/26/2021)"
}
```

## /redfish/v1/UpdateService/ComponentRepository/bebf97fe

```{
    "@odata.context": "/redfish/v1/$metadata#HpeComponent.HpeComponent",
    "@odata.etag": "W/\"CD21D410\"",
    "@odata.id": "/redfish/v1/UpdateService/ComponentRepository/bebf97fe",
    "@odata.type": "#HpeComponent.v1_0_1.HpeComponent",
    "Activates": "AfterReboot",
    "ComponentUri": "/fwrepo/U46_1.56_11_29_2021.fwpkg",
    "Configuration": "",
    "Created": "2022-02-25T17:29:29Z",
    "Criticality": "Optional",
    "DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
    "ExecutionParameters": "",
    "Filename": "U46_1.56_11_29_2021.fwpkg",
    "Filepath": "U46_1.56_11_29_2021.fwpkg",
    "Id": "bebf97fe",
    "Locked": false,
    "Name": "ROM Flash Universal Firmware Package - HPE ProLiant DL360/DL...",
    "SizeBytes": 33587844,
    "Targets": [
        "00000000-0000-0000-0000-000000000225",
        "00000000-0000-0000-0000-000000000226",
        "00000000-0000-0000-0000-00000000022c"
    ],
    "UpdatableBy": [
        "Bmc"
    ],
    "Version": "1.56_11-29-2021"
}
```

## /redfish/v1/UpdateService/FirmwareInventory

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventoryCollection.SoftwareInventoryCollection",
    "@odata.etag": "W/\"E5D4A4CF\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory",
    "@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
    "Description": "Firmware Inventory Collection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/1"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/2"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/3"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/4"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/5"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/6"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/7"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/8"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/9"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/10"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/11"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/12"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/13"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/14"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/15"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/16"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/17"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/18"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/19"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/20"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/21"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/22"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/23"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/24"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/25"
        }
    ],
    "Members@odata.count": 25,
    "Name": "Firmware Inventory Collection"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/1

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"918DA6A4\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/1",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "SystemBMC",
    "Id": "1",
    "Name": "iLO 5",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "2f317b9d-c9e3-4d76-bff6-b9d0d085a952",
            "DeviceContext": "System Board",
            "Targets": [
                "4764a662-b342-4fc7-9ce9-258c5d99e815",
                "c0bcf2b9-1141-49af-aab8-c73791f0349c"
            ]
        }
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Updateable": true,
    "Version": "2.55 Oct 01 2021"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/10

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"918DA6A4\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/10",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "SPSFirmwareDescriptor",
    "Id": "10",
    "Name": "Server Platform Services (SPS) Descriptor",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "3f30a329-d03c-46b8-8f0e-9567fad4ea9f",
            "DeviceContext": "System Board",
            "Targets": [
                "00000000-0000-0000-0000-000000000225"
            ]
        }
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Updateable": true,
    "Version": "1.2 0"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/11

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"1DF5B87E\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/11",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "SystemRomBackup",
    "Id": "11",
    "Name": "Redundant System ROM",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": null,
            "DeviceContext": "System Board"
        }
    },
    "Updateable": false,
    "Version": "U46 v1.42 (05/26/2021)"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/12

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"1DF5B87E\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/12",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "Intelligent Provisioning",
    "Id": "12",
    "Name": "Intelligent Provisioning",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "ac963eeb-ed78-4f36-c18c-29d85f34a0ac",
            "DeviceContext": "System Board"
        }
    },
    "Updateable": false,
    "Version": "3.64.2"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/13

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"1DF5B87E\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/13",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "PowerManagementControllerBootloader",
    "Id": "13",
    "Name": "Power Management Controller FW Bootloader",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": null,
            "DeviceContext": "System Board"
        }
    },
    "Updateable": false,
    "Version": "1.1"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/14

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"1DF5B87E\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/14",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "SmartStorageEnergyPack",
    "Id": "14",
    "Name": "HPE Smart Storage Energy Pack 1 Firmware",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": null,
            "DeviceContext": "Embedded Device"
        }
    },
    "Updateable": false,
    "Version": "0.70"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/15

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"0539D502\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/15",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "100010e215900293",
    "Id": "15",
    "Name": "HPE MR416i-p Gen10+",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": null,
            "DeviceContext": "PCI-E Slot 1",
            "DeviceInstance": "PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)",
            "Targets": [
                "a6b1a447-382a-5a4f-1000-10e215900293"
            ]
        }
    },
    "Updateable": true,
    "Version": "52.16.3-3913"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/16

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"0539D502\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/16",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "1b4b22411590030f",
    "Id": "16",
    "Name": "HPE NS204i-r Gen10+ Boot Controller",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": null,
            "DeviceContext": "PCI-E Slot 13",
            "DeviceInstance": "PciRoot(0x2)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "Targets": [
                "a6b1a447-382a-5a4f-1b4b-22411590030f"
            ]
        }
    },
    "Updateable": true,
    "Version": "1.0.14.1055"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/17

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"0539D502\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/17",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "80861521808600a3",
    "Id": "17",
    "Name": "Intel Eth Adptr I350T4 OCPv3",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": null,
            "DeviceContext": "OCP 3.0 Slot 10",
            "DeviceInstance": "PciRoot(0x4)/Pci(0x4,0x0)/Pci(0x0,0x0)",
            "Targets": [
                "a6b1a447-382a-5a4f-8086-1521808600a3"
            ]
        }
    },
    "Updateable": false,
    "Version": "1.2839.0"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/18

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"0539D502\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/18",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "102b0538159000e4",
    "Id": "18",
    "Name": "Embedded Video Controller",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": null,
            "DeviceContext": "Embedded Device",
            "DeviceInstance": "PciRoot(0x0)/Pci(0x1C,0x4)/Pci(0x0,0x1)",
            "Targets": [
                "a6b1a447-382a-5a4f-102b-0538159000e4"
            ]
        }
    },
    "Updateable": false,
    "Version": "2.5"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/19

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"0539D502\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/19",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "VO000960KXAVL",
    "Id": "19",
    "Name": "Drive",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "f6de0320-2e0f-489a-b238-6dd8ae7c3811",
            "DeviceContext": "Port 1I Box 1 Bay 1",
            "Targets": [
                "562340a5-304f-3030-3936-304b5841564c"
            ]
        }
    },
    "Updateable": false,
    "Version": "HPK3"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/2

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"918DA6A4\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/2",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "SystemRomActive",
    "Id": "2",
    "Name": "System ROM",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
            "DeviceContext": "System Board",
            "Targets": [
                "00000000-0000-0000-0000-000000000225",
                "00000000-0000-0000-0000-000001553436"
            ]
        }
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Updateable": true,
    "Version": "U46 v1.56 (11/29/2021)"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/20

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"0539D502\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/20",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "VO000960KXAVL",
    "Id": "20",
    "Name": "Drive",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "f6de0320-2e0f-489a-b238-6dd8ae7c3811",
            "DeviceContext": "Port 1I Box 1 Bay 3",
            "Targets": [
                "562340a5-304f-3030-3936-304b5841564c"
            ]
        }
    },
    "Updateable": false,
    "Version": "HPK3"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/21

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"542C1060\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/21",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "VS000480KXALB",
    "Id": "21",
    "Name": "480GB 16G NVMe SSD",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "f6de0320-2e0f-489a-b238-6dd8ae7c3811",
            "DeviceContext": "Slot=13:Bay=1",
            "Targets": [
                "562340a5-3053-3030-3438-304b58414c42"
            ]
        }
    },
    "RelatedItem": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000/Drives/1"
        }
    ],
    "SoftwareId": "f6de0320-2e0f-489a-b238-6dd8ae7c3811:562340a5-3053-3030-3438-304b58414c42",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Updateable": false,
    "Version": "85031G00"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/22

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"542C1060\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/22",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "VS000480KXALB",
    "Id": "22",
    "Name": "480GB 16G NVMe SSD",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "f6de0320-2e0f-489a-b238-6dd8ae7c3811",
            "DeviceContext": "Slot=13:Bay=2",
            "Targets": [
                "562340a5-3053-3030-3438-304b58414c42"
            ]
        }
    },
    "RelatedItem": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE009000/Drives/2"
        }
    ],
    "SoftwareId": "f6de0320-2e0f-489a-b238-6dd8ae7c3811:562340a5-3053-3030-3438-304b58414c42",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Updateable": false,
    "Version": "85031G00"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/23

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"542C1060\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/23",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "VO000960KXAVL",
    "Id": "23",
    "Name": "960GB 32G NVMe SSD",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "f6de0320-2e0f-489a-b238-6dd8ae7c3811",
            "DeviceContext": "Port=1I:Box=1:Bay=1",
            "Targets": [
                "562340a5-304f-3030-3936-304b5841564c"
            ]
        }
    },
    "RelatedItem": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/Drives/0"
        }
    ],
    "SoftwareId": "f6de0320-2e0f-489a-b238-6dd8ae7c3811:562340a5-304f-3030-3936-304b5841564c",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Updateable": false,
    "Version": "HPK3"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/24

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"542C1060\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/24",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "VO000960KXAVL",
    "Id": "24",
    "Name": "960GB 32G NVMe SSD",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "f6de0320-2e0f-489a-b238-6dd8ae7c3811",
            "DeviceContext": "Port=1I:Box=1:Bay=3",
            "Targets": [
                "562340a5-304f-3030-3936-304b5841564c"
            ]
        }
    },
    "RelatedItem": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/Drives/1"
        }
    ],
    "SoftwareId": "f6de0320-2e0f-489a-b238-6dd8ae7c3811:562340a5-304f-3030-3936-304b5841564c",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Updateable": false,
    "Version": "HPK3"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/25

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"542C1060\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/25",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "VO000960KXAVL",
    "Id": "25",
    "Name": "960GB 32G NVMe SSD",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "f6de0320-2e0f-489a-b238-6dd8ae7c3811",
            "DeviceContext": "Port=1I:Box=1:Bay=2",
            "Targets": [
                "562340a5-304f-3030-3936-304b5841564c"
            ]
        }
    },
    "RelatedItem": [
        {
            "@odata.id": "/redfish/v1/Systems/1/Storage/DE00A000/Drives/2"
        }
    ],
    "SoftwareId": "f6de0320-2e0f-489a-b238-6dd8ae7c3811:562340a5-304f-3030-3936-304b5841564c",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Updateable": false,
    "Version": "HPK3"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/3

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"0539D502\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/3",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "PlatformDefinitionTable",
    "Id": "3",
    "Name": "Intelligent Platform Abstraction Data",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "b8f46d06-85db-465c-94fb-d106e61378ed",
            "DeviceContext": "System Board",
            "Targets": [
                "00000000-0000-0000-0000-000000000225",
                "00000000-0000-0000-0000-000001553436"
            ]
        }
    },
    "Updateable": true,
    "Version": "9.2.0 Build 35"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/4

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"918DA6A4\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/4",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "SystemProgrammableLogicDevice",
    "Id": "4",
    "Name": "System Programmable Logic Device",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "b1ad439a-9dd1-41c1-a496-2da9313f1f07",
            "DeviceContext": "System Board",
            "Targets": [
                "00000000-0000-0000-0000-000000000225"
            ]
        }
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Updateable": true,
    "Version": "0x15"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/5

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"0539D502\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/5",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "PowerManagementController",
    "Id": "5",
    "Name": "Power Management Controller Firmware",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "9e48a28a-586c-4519-8405-a04f84e27f0f",
            "DeviceContext": "System Board",
            "Targets": [
                "00000000-0000-0000-0000-000000000225",
                "00000000-0000-0000-0000-000000504d05"
            ]
        }
    },
    "Updateable": true,
    "Version": "1.0.7"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/6

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"0539D502\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/6",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "PowerSupplies",
    "Id": "6",
    "Name": "Power Supply Firmware",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "6bb86077-0275-4614-aae1-86618e8b1c27",
            "DeviceContext": "Bay 1",
            "Targets": [
                "0102bd05-0001-0000-0000-0cf38db966ea"
            ]
        }
    },
    "Updateable": true,
    "Version": "1.00"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/7

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"0539D502\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/7",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "PowerSupplies",
    "Id": "7",
    "Name": "Power Supply Firmware",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "6bb86077-0275-4614-aae1-86618e8b1c27",
            "DeviceContext": "Bay 2",
            "Targets": [
                "0102bd05-0001-0000-0000-0cf38db966ea"
            ]
        }
    },
    "Updateable": true,
    "Version": "1.00"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/8

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"918DA6A4\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/8",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "InnovationEngineFirmware",
    "Id": "8",
    "Name": "Innovation Engine (IE) Firmware",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "c734e171-8721-48c9-9ed6-d5bc7da5ef8d",
            "DeviceContext": "System Board",
            "Targets": [
                "00000000-0000-0000-0000-000000000225",
                "a6b1a447-382a-5a4f-3c10-87800a000303"
            ]
        }
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Updateable": true,
    "Version": "1.0.0.20"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/9

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.etag": "W/\"918DA6A4\"",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/9",
    "@odata.type": "#SoftwareInventory.v1_2_0.SoftwareInventory",
    "Description": "SPSFirmwareVersionData",
    "Id": "9",
    "Name": "Server Platform Services (SPS) Firmware",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
            "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
            "DeviceClass": "b34e5677-21dc-45d3-872b-42f76fee9053",
            "DeviceContext": "System Board",
            "Targets": [
                "00000000-0000-0000-0000-000000000225",
                "a6b1a447-382a-5a4f-3c10-87800a000101"
            ]
        }
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Updateable": true,
    "Version": "4.4.4.53"
}
```

## /redfish/v1/UpdateService/InstallSets

```{
    "@odata.context": "/redfish/v1/$metadata#HpeComponentInstallSetCollection.HpeComponentInstallSetCollection",
    "@odata.etag": "W/\"AA6D42B0\"",
    "@odata.id": "/redfish/v1/UpdateService/InstallSets",
    "@odata.type": "#HpeComponentInstallSetCollection.HpeComponentInstallSetCollection",
    "Description": "Component Install Set Collection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/UpdateService/InstallSets/a74b22b6"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Component Install Set Collection"
}
```

## /redfish/v1/UpdateService/InstallSets/a74b22b6

```{
    "@odata.context": "/redfish/v1/$metadata#HpeComponentInstallSet.HpeComponentInstallSet",
    "@odata.etag": "W/\"298E1A70\"",
    "@odata.id": "/redfish/v1/UpdateService/InstallSets/a74b22b6",
    "@odata.type": "#HpeComponentInstallSet.v1_1_0.HpeComponentInstallSet",
    "Actions": {
        "#HpeComponentInstallSet.Invoke": {
            "target": "/redfish/v1/UpdateService/InstallSets/a74b22b6/Actions/HpeComponentInstallSet.Invoke"
        }
    },
    "Created": "2021-08-18T06:45:40Z",
    "Description": "Essential System Firmware Components",
    "Id": "a74b22b6",
    "IsRecovery": true,
    "Modified": "2021-08-18T06:45:40Z",
    "Name": "System Recovery Set",
    "Sequence": [
        {
            "Command": "ApplyUpdate",
            "Component": "/redfish/v1/UpdateService/ComponentRepository/224c0cdf",
            "ExecutionTimeoutMinutes": 0,
            "Filename": "ilo5_244.bin",
            "Name": "iLO 5",
            "UpdatableBy": [
                "Bmc"
            ]
        },
        {
            "Command": "ApplyUpdate",
            "Component": "/redfish/v1/UpdateService/ComponentRepository/59018d2e",
            "ExecutionTimeoutMinutes": 0,
            "Filename": "IEGen10Plus_1.0.0.20.signed.bin",
            "Name": "Innovation Engine (IE) Universal Image",
            "UpdatableBy": [
                "Bmc"
            ]
        },
        {
            "Command": "ApplyUpdate",
            "Component": "/redfish/v1/UpdateService/ComponentRepository/52a0a2f4",
            "ExecutionTimeoutMinutes": 0,
            "Filename": "SPSGEN10PLUS_04.04.04.053.signed.bin",
            "Name": "Server Platform Services (SPS) Firmware",
            "UpdatableBy": [
                "Bmc"
            ]
        },
        {
            "Command": "ApplyUpdate",
            "Component": "/redfish/v1/UpdateService/ComponentRepository/3e96efee",
            "ExecutionTimeoutMinutes": 0,
            "Filename": "CPLD_DL360_DL380_Gen10Plus_v1515_signed.vme",
            "Name": "System Programmable Logic Device",
            "UpdatableBy": [
                "Bmc"
            ]
        },
        {
            "Command": "ApplyUpdate",
            "Component": "/redfish/v1/UpdateService/ComponentRepository/7d70dc89",
            "ExecutionTimeoutMinutes": 0,
            "Filename": "U46_1.42_05_26_2021.signed.flash",
            "Name": "System BIOS - U46",
            "UpdatableBy": [
                "Bmc"
            ]
        }
    ]
}
```

## /redfish/v1/UpdateService/InvalidImageRepository

```{
    "@odata.context": "/redfish/v1/$metadata#HpeInvalidImageCollection.HpeInvalidImageCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/UpdateService/InvalidImageRepository",
    "@odata.type": "#HpeInvalidImageCollection.HpeInvalidImageCollection",
    "Description": "Invalid Image Collection",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Invalid Image Collection"
}
```

## /redfish/v1/UpdateService/MaintenanceWindows

```{
    "@odata.context": "/redfish/v1/$metadata#HpeMaintenanceWindowCollection.HpeMaintenanceWindowCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/UpdateService/MaintenanceWindows",
    "@odata.type": "#HpeMaintenanceWindowCollection.HpeMaintenanceWindowCollection",
    "Description": "Maintenance Window Collection",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Maintenance Window Collection"
}
```

## /redfish/v1/UpdateService/SoftwareInventory

```
```

## /redfish/v1/UpdateService/SoftwareInventory/1

```
```

## /redfish/v1/UpdateService/SoftwareInventory/10

```
```

## /redfish/v1/UpdateService/SoftwareInventory/11

```
```

## /redfish/v1/UpdateService/SoftwareInventory/12

```
```

## /redfish/v1/UpdateService/SoftwareInventory/13

```
```

## /redfish/v1/UpdateService/SoftwareInventory/14

```
```

## /redfish/v1/UpdateService/SoftwareInventory/15

```
```

## /redfish/v1/UpdateService/SoftwareInventory/16

```
```

## /redfish/v1/UpdateService/SoftwareInventory/17

```
```

## /redfish/v1/UpdateService/SoftwareInventory/18

```
```

## /redfish/v1/UpdateService/SoftwareInventory/19

```
```

## /redfish/v1/UpdateService/SoftwareInventory/2

```
```

## /redfish/v1/UpdateService/SoftwareInventory/20

```
```

## /redfish/v1/UpdateService/SoftwareInventory/21

```
```

## /redfish/v1/UpdateService/SoftwareInventory/22

```
```

## /redfish/v1/UpdateService/SoftwareInventory/23

```
```

## /redfish/v1/UpdateService/SoftwareInventory/24

```
```

## /redfish/v1/UpdateService/SoftwareInventory/25

```
```

## /redfish/v1/UpdateService/SoftwareInventory/26

```
```

## /redfish/v1/UpdateService/SoftwareInventory/27

```
```

## /redfish/v1/UpdateService/SoftwareInventory/28

```
```

## /redfish/v1/UpdateService/SoftwareInventory/29

```
```

## /redfish/v1/UpdateService/SoftwareInventory/3

```
```

## /redfish/v1/UpdateService/SoftwareInventory/30

```
```

## /redfish/v1/UpdateService/SoftwareInventory/31

```
```

## /redfish/v1/UpdateService/SoftwareInventory/32

```
```

## /redfish/v1/UpdateService/SoftwareInventory/33

```
```

## /redfish/v1/UpdateService/SoftwareInventory/34

```
```

## /redfish/v1/UpdateService/SoftwareInventory/35

```
```

## /redfish/v1/UpdateService/SoftwareInventory/36

```
```

## /redfish/v1/UpdateService/SoftwareInventory/37

```
```

## /redfish/v1/UpdateService/SoftwareInventory/38

```
```

## /redfish/v1/UpdateService/SoftwareInventory/39

```
```

## /redfish/v1/UpdateService/SoftwareInventory/4

```
```

## /redfish/v1/UpdateService/SoftwareInventory/40

```
```

## /redfish/v1/UpdateService/SoftwareInventory/41

```
```

## /redfish/v1/UpdateService/SoftwareInventory/42

```
```

## /redfish/v1/UpdateService/SoftwareInventory/43

```
```

## /redfish/v1/UpdateService/SoftwareInventory/44

```
```

## /redfish/v1/UpdateService/SoftwareInventory/45

```
```

## /redfish/v1/UpdateService/SoftwareInventory/46

```
```

## /redfish/v1/UpdateService/SoftwareInventory/47

```
```

## /redfish/v1/UpdateService/SoftwareInventory/48

```
```

## /redfish/v1/UpdateService/SoftwareInventory/49

```
```

## /redfish/v1/UpdateService/SoftwareInventory/5

```
```

## /redfish/v1/UpdateService/SoftwareInventory/50

```
```

## /redfish/v1/UpdateService/SoftwareInventory/51

```
```

## /redfish/v1/UpdateService/SoftwareInventory/52

```
```

## /redfish/v1/UpdateService/SoftwareInventory/53

```
```

## /redfish/v1/UpdateService/SoftwareInventory/54

```
```

## /redfish/v1/UpdateService/SoftwareInventory/55

```
```

## /redfish/v1/UpdateService/SoftwareInventory/56

```
```

## /redfish/v1/UpdateService/SoftwareInventory/57

```
```

## /redfish/v1/UpdateService/SoftwareInventory/58

```
```

## /redfish/v1/UpdateService/SoftwareInventory/59

```
```

## /redfish/v1/UpdateService/SoftwareInventory/6

```
```

## /redfish/v1/UpdateService/SoftwareInventory/60

```
```

## /redfish/v1/UpdateService/SoftwareInventory/61

```
```

## /redfish/v1/UpdateService/SoftwareInventory/62

```
```

## /redfish/v1/UpdateService/SoftwareInventory/63

```
```

## /redfish/v1/UpdateService/SoftwareInventory/64

```
```

## /redfish/v1/UpdateService/SoftwareInventory/65

```
```

## /redfish/v1/UpdateService/SoftwareInventory/7

```
```

## /redfish/v1/UpdateService/SoftwareInventory/8

```
```

## /redfish/v1/UpdateService/SoftwareInventory/9

```
```

## /redfish/v1/UpdateService/UpdateTaskQueue

```{
    "@odata.context": "/redfish/v1/$metadata#HpeComponentUpdateTaskQueueCollection.HpeComponentUpdateTaskQueueCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/UpdateService/UpdateTaskQueue",
    "@odata.type": "#HpeComponentUpdateTaskQueueCollection.HpeComponentUpdateTaskQueueCollection",
    "Description": "Component Update Task Queue",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Component Update Task Queue"
}
```

