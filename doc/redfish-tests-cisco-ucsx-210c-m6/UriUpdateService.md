# Resource: /api-explorer/resources/redfish/v1/UpdateService

Vendor | Model
--- | ---
Cisco | UCSX-210C-M6

## /api-explorer/resources/redfish/v1/UpdateService

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService.UpdateService",
    "@odata.id": "/redfish/v1/UpdateService",
    "@odata.type": "#UpdateService.v1_8_2.UpdateService",
    "Actions": {
        "#UpdateService.SimpleUpdate": {
            "ImageURI@Redfish.AllowableValues": [
                "URI to Image File"
            ],
            "Password@Redfish.AllowableValues": [
                "Server Password"
            ],
            "Target@Redfish.AllowableValues": [
                "/redfish/v1/UpdateService/FirmwareInventory/CIMC",
                "/redfish/v1/UpdateService/FirmwareInventory/BIOS"
            ],
            "TransferProtocol@Redfish.AllowableValues": [
                "OEM",
                "TFTP",
                "SCP",
                "SFTP",
                "FTP",
                "HTTP",
                "HTTPS"
            ],
            "Username@Redfish.AllowableValues": [
                "Server Username"
            ],
            "target": "/redfish/v1/UpdateService/Actions/UpdateService.SimpleUpdate"
        },
        "Oem": {
            "#CiscoUCSExtensions.PrepareOSInstall": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareOSInstall",
                "ApplyTime@Redfish.AllowableValues": [
                    "Immediate",
                    "OnNextBoot"
                ],
                "BaseISORepoDetails@Redfish.AllowableValues": [
                    "This object specifies details required to access SCU ISO image. This object shall have properties ImageRepository, TransferProtocol, Username and Password."
                ],
                "ImageRepository@Redfish.AllowableValues": [
                    "The shared repository path of ISO image."
                ],
                "MountOption@Redfish.AllowableValues": [
                    "Mount option is optional and shall be used for accessing CIFS shared location specified by the ImageRepository parameter."
                ],
                "OSAnswerFileRepoDetails@Redfish.AllowableValues": [
                    "This object specifies details required to access OS Answer file. This object shall have properties ImageRepository, TransferProtocol, Username and Password."
                ],
                "OSEdition@Redfish.AllowableValues": [
                    "None",
                    "STANDARD",
                    "DATACENTER",
                    "CORE",
                    "STANDARDCORE",
                    "DATACENTERCORE"
                ],
                "OSISORepoDetails@Redfish.AllowableValues": [
                    "This object specifies details required to access OS ISO image. This object shall have properties ImageRepository, TransferProtocol, Username and Password."
                ],
                "OSName@Redfish.AllowableValues": [
                    "Unique name of the OS, as given in SCU Release Note."
                ],
                "Password@Redfish.AllowableValues": [
                    "The password to be used while accessing shared location specified by the ImageRepository parameter."
                ],
                "TargetDisk@Redfish.AllowableValues": [
                    "This parameter specifies the Storage URI to indicate the disk where OS is to be installed."
                ],
                "TargetOS@Redfish.AllowableValues": [
                    "This object specifies details of OS to be installed. This object shall have properties OSName and OSEdition."
                ],
                "TransferProtocol@Redfish.AllowableValues": [
                    "CIFS",
                    "HTTPS",
                    "NFS",
                    "VMEDIA-CIFS",
                    "VMEDIA-HTTPS",
                    "VMEDIA-NFS",
                    "LOCAL-HOST"
                ],
                "Username@Redfish.AllowableValues": [
                    "The username to be used while accessing shared location specified by the ImageRepository parameter."
                ],
                "target": "/redfish/v1/UpdateService/Actions/Oem/CiscoUCSExtensions.PrepareOSInstall"
            },
            "#CiscoUCSExtensions.SetStartImageVersion": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.SetStartImageVersion",
                "ImageVersion@Redfish.AllowableValues": [
                    "Image Version"
                ],
                "Target@Redfish.AllowableValues": [
                    "/redfish/v1/UpdateService/FirmwareInventory/CIMC"
                ],
                "target": "/redfish/v1/UpdateService/Actions/Oem/CiscoUpdateService.SetStartImageVersion"
            },
            "#CiscoUCSExtensions.UCSUpdate": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UCSUpdate",
                "ApplyTime@Redfish.AllowableValues": [
                    "Immediate",
                    "OnNextBoot"
                ],
                "ExcludeTargets@Redfish.AllowableValues": [
                    "Array of Redfish Odata Types indicating types of components to be excluded."
                ],
                "ForceUpdate@Redfish.AllowableValues": [
                    true,
                    false
                ],
                "ImageRepository@Redfish.AllowableValues": [
                    "The directory path of the extracted HSU bundle."
                ],
                "Password@Redfish.AllowableValues": [
                    "The password to be used when accessing the URI specified by the ImageRepository parameter."
                ],
                "Targets@Redfish.AllowableValues": [
                    "Array of Software/Firmware Inventory URIs indicating where the image is to be applied."
                ],
                "TransferProtocol@Redfish.AllowableValues": [
                    "VMEDIA-CIFS",
                    "VMEDIA-NFS",
                    "VMEDIA-HTTPS",
                    "LOCAL-HOST"
                ],
                "Username@Redfish.AllowableValues": [
                    "The username to be used when accessing the URI specified by the ImageRepository parameter."
                ],
                "target": "/redfish/v1/UpdateService/Actions/Oem/CiscoUCSExtensions.UCSUpdate"
            }
        }
    },
    "Description": "Update Service",
    "FirmwareInventory": {
        "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory"
    },
    "HttpPushUriTargetsBusy": false,
    "Id": "UpdateService",
    "Name": "Update Service",
    "ServiceEnabled": true,
    "SoftwareInventory": {
        "@odata.id": "/redfish/v1/UpdateService/SoftwareInventory"
    }
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventoryCollection.SoftwareInventoryCollection",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory",
    "@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
    "Description": "Inventory of Firmware components",
    "Members": [
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/BIOS"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/CIMC"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Board_Controller"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCSX-V4-Q25GML_FCH25337EE9"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCS-M2-HWRAID-slot-MSTOR-RAID"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-MTFDDAV240TCB-serial-MSA25230BH0"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-MTFDDAV240TCB-serial-MSA25230BH7"
        }
    ],
    "Members@odata.count": 7,
    "Name": "Firmware Inventory"
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/BIOS

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/BIOS",
    "@odata.type": "#SoftwareInventory.v1_3_0.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "BIOS",
    "Name": "BIOS",
    "RelatedItem": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM"
        }
    ],
    "Updateable": true,
    "Version": "X210M6.5.0.1i.0.0709221354"
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/Board_Controller

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Board_Controller",
    "@odata.type": "#SoftwareInventory.v1_3_0.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "Board_Controller",
    "Name": "Board_Controller",
    "Updateable": true,
    "Version": "18.0"
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/CIMC

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/CIMC",
    "@odata.type": "#SoftwareInventory.v1_3_0.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "CIMC",
    "Name": "CIMC",
    "RelatedItem": [
        {
            "@odata.id": "/redfish/v1/Managers/CIMC"
        }
    ],
    "Updateable": true,
    "Version": "5.0(1f)"
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/HDD-model-MTFDDAV240TCB-serial-MSA25230BH0

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-MTFDDAV240TCB-serial-MSA25230BH0",
    "@odata.type": "#SoftwareInventory.v1_3_0.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "HDD-model-MTFDDAV240TCB-serial-MSA25230BH0",
    "Name": "HDD-model-MTFDDAV240TCB-serial-MSA25230BH0",
    "RelatedItem": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/253"
        }
    ],
    "Updateable": true,
    "Version": "D0MH077"
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/HDD-model-MTFDDAV240TCB-serial-MSA25230BH7

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-MTFDDAV240TCB-serial-MSA25230BH7",
    "@odata.type": "#SoftwareInventory.v1_3_0.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "HDD-model-MTFDDAV240TCB-serial-MSA25230BH7",
    "Name": "HDD-model-MTFDDAV240TCB-serial-MSA25230BH7",
    "RelatedItem": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/254"
        }
    ],
    "Updateable": true,
    "Version": "D0MH077"
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/UCS-M2-HWRAID-slot-MSTOR-RAID

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCS-M2-HWRAID-slot-MSTOR-RAID",
    "@odata.type": "#SoftwareInventory.v1_3_0.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "UCS-M2-HWRAID-slot-MSTOR-RAID",
    "Name": "UCS-M2-HWRAID-slot-MSTOR-RAID",
    "RelatedItem": [
        {
            "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID"
        }
    ],
    "Updateable": true,
    "Version": "2.3.17.1014"
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/UCSX-V4-Q25GML_FCH25337EE9

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCSX-V4-Q25GML_FCH25337EE9",
    "@odata.type": "#SoftwareInventory.v1_3_0.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "UCSX-V4-Q25GML_FCH25337EE9",
    "Name": "UCSX-V4-Q25GML_FCH25337EE9",
    "Updateable": true,
    "Version": "5.2(1c)"
}
```

## /api-explorer/resources/redfish/v1/UpdateService/SoftwareInventory

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventoryCollection.SoftwareInventoryCollection",
    "@odata.id": "/redfish/v1/UpdateService/SoftwareInventory",
    "@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
    "Description": "Inventory of Software components",
    "Members": [
        {
            "@odata.id": "/redfish/v1/UpdateService/SoftwareInventory/DeviceConnector"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Software Inventory"
}
```

## /api-explorer/resources/redfish/v1/UpdateService/SoftwareInventory/DeviceConnector

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/SoftwareInventory/DeviceConnector",
    "@odata.type": "#SoftwareInventory.v1_3_0.SoftwareInventory",
    "Description": "Software Inventory",
    "Id": "DeviceConnector",
    "Manufacturer": "Cisco Systems Inc",
    "Name": "DeviceConnector",
    "Updateable": true,
    "Version": "1.0.11-2316"
}
```

