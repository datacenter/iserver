# Resource: /redfish/v1/UpdateService

Vendor | Model
--- | ---
Cisco | UCSC-C220-M5SX

## /redfish/v1/UpdateService

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService.UpdateService",
    "@odata.id": "/redfish/v1/UpdateService",
    "@odata.type": "#UpdateService.v1_5_0.UpdateService",
    "Actions": {
        "#UpdateService.SimpleUpdate": {
            "ImageURI@Redfish.AllowableValues": [
                "Path to Image File : Format - IP:/PATH - where IP can be IPv4, IPv6 or Hostname and PATH should start with a forward slash and should contain the appropriate file extension."
            ],
            "Password@Redfish.AllowableValues": [
                "Server Password"
            ],
            "Targets@Redfish.AllowableValues": [
                "Array of Software/Firmware Inventory URI of either /redfish/v1/UpdateService/FirmwareInventory/CIMC or /redfish/v1/UpdateService/FirmwareInventory/BIOS indicating where the image is to be applied."
            ],
            "TransferProtocol@Redfish.AllowableValues": [
                "TFTP",
                "SCP",
                "SFTP",
                "FTP",
                "HTTP"
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
                    "VMEDIA-NFS"
                ],
                "Username@Redfish.AllowableValues": [
                    "The username to be used while accessing shared location specified by the ImageRepository parameter."
                ],
                "target": "/redfish/v1/UpdateService/Actions/Oem/CiscoUCSExtensions.PrepareOSInstall"
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
                    "CIFS",
                    "HTTPS",
                    "NFS",
                    "VMEDIA-CIFS",
                    "VMEDIA-HTTPS",
                    "VMEDIA-NFS"
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
    "Id": "UpdateService",
    "MaxImageSizeBytes": 60000000,
    "Name": "Update Service",
    "ServiceEnabled": true,
    "SoftwareInventory": {
        "@odata.id": "/redfish/v1/UpdateService/SoftwareInventory"
    }
}
```

## /redfish/v1/UpdateService/FirmwareInventory

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
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCSC-RAID-M5-slot-MRAID"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-MZ7LM240HMHQ-00003-serial-S3LKNX0K800827"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A00MFJRG"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z820A07VFJRG"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A01YFJRG"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A02JFJRG"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A02DFJRG"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A003FJRG"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/X710DA4-slot-1"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/X710DA4-slot-2"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/X550-LOM-slot-L"
        }
    ],
    "Members@odata.count": 14,
    "Name": "Firmware Inventory"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/BIOS

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/BIOS",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "BIOS",
    "Name": "BIOS",
    "RelatedItem": "/redfish/v1/Systems/WZP22490ZCU",
    "Updateable": true,
    "Version": "C220M5.4.1.3i.0.0713210713"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/Board_Controller

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Board_Controller",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "Board_Controller",
    "Name": "Board_Controller",
    "Updateable": true,
    "Version": "59.0"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/CIMC

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/CIMC",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "CIMC",
    "Name": "CIMC",
    "RelatedItem": "/redfish/v1/Managers/CIMC",
    "Updateable": true,
    "Version": "4.1(3d)"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z820A07VFJRG

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z820A07VFJRG",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-AL15SEB120N-serial-Z820A07VFJRG",
    "Name": "HDD-model-AL15SEB120N-serial-Z820A07VFJRG",
    "RelatedItem": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3",
    "Updateable": true,
    "Version": "5703"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A003FJRG

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A003FJRG",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-AL15SEB120N-serial-Z830A003FJRG",
    "Name": "HDD-model-AL15SEB120N-serial-Z830A003FJRG",
    "RelatedItem": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/7",
    "Updateable": true,
    "Version": "5703"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A00MFJRG

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A00MFJRG",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-AL15SEB120N-serial-Z830A00MFJRG",
    "Name": "HDD-model-AL15SEB120N-serial-Z830A00MFJRG",
    "RelatedItem": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2",
    "Updateable": true,
    "Version": "5703"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A01YFJRG

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A01YFJRG",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-AL15SEB120N-serial-Z830A01YFJRG",
    "Name": "HDD-model-AL15SEB120N-serial-Z830A01YFJRG",
    "RelatedItem": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/4",
    "Updateable": true,
    "Version": "5703"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A02DFJRG

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A02DFJRG",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-AL15SEB120N-serial-Z830A02DFJRG",
    "Name": "HDD-model-AL15SEB120N-serial-Z830A02DFJRG",
    "RelatedItem": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/6",
    "Updateable": true,
    "Version": "5703"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A02JFJRG

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-AL15SEB120N-serial-Z830A02JFJRG",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-AL15SEB120N-serial-Z830A02JFJRG",
    "Name": "HDD-model-AL15SEB120N-serial-Z830A02JFJRG",
    "RelatedItem": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/5",
    "Updateable": true,
    "Version": "5703"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-MZ7LM240HMHQ-00003-serial-S3LKNX0K800827

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-MZ7LM240HMHQ-00003-serial-S3LKNX0K800827",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-MZ7LM240HMHQ-00003-serial-S3LKNX0K800827",
    "Name": "HDD-model-MZ7LM240HMHQ-00003-serial-S3LKNX0K800827",
    "RelatedItem": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/1",
    "Updateable": true,
    "Version": "GXT51F3Q"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/UCSC-RAID-M5-slot-MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCSC-RAID-M5-slot-MRAID",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "UCSC-RAID-M5-slot-MRAID",
    "Name": "UCSC-RAID-M5-slot-MRAID",
    "RelatedItem": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID",
    "Updateable": true,
    "Version": "51.10.0-3612"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/X550-LOM-slot-L

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/X550-LOM-slot-L",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "X550-LOM-slot-L",
    "Name": "X550-LOM-slot-L",
    "Updateable": true,
    "Version": "0x80001514-1.823.2"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/X710DA4-slot-1

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/X710DA4-slot-1",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "X710DA4-slot-1",
    "Name": "X710DA4-slot-1",
    "Updateable": true,
    "Version": "0x80009E63-1.823.2"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/X710DA4-slot-2

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/X710DA4-slot-2",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "X710DA4-slot-2",
    "Name": "X710DA4-slot-2",
    "Updateable": true,
    "Version": "0x80009E63-1.823.2"
}
```

## /redfish/v1/UpdateService/SoftwareInventory

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

## /redfish/v1/UpdateService/SoftwareInventory/DeviceConnector

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/SoftwareInventory/DeviceConnector",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "DeviceConnector",
    "Manufacturer": "Cisco Systems Inc.",
    "Name": "DeviceConnector",
    "Updateable": true,
    "Version": "1.0.11-2316"
}
```

