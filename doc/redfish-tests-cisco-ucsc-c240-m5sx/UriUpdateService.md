# Resource: /redfish/v1/UpdateService

Vendor | Model
--- | ---
Cisco | UCSC-C240-M5SX

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
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCS_VIC_1387-slot-MLOM"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCSC-RAID-M5HD-slot-MRAID"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/SasExpM5"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00LTSMF"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00VTSMF"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00CTSMF"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00NTSMF"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00STSMF"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/XL710-slot-4"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/XL710-slot-6"
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
    "RelatedItem": "/redfish/v1/Systems/WZP23450C8K",
    "Updateable": true,
    "Version": "C240M5.4.1.3i.0.0713210713"
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
    "Version": "61.0"
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

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00CTSMF

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00CTSMF",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-KPM51VUG800G-serial-Y9B0A00CTSMF",
    "Name": "HDD-model-KPM51VUG800G-serial-Y9B0A00CTSMF",
    "RelatedItem": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/22",
    "Updateable": true,
    "Version": "0108"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00LTSMF

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00LTSMF",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-KPM51VUG800G-serial-Y9B0A00LTSMF",
    "Name": "HDD-model-KPM51VUG800G-serial-Y9B0A00LTSMF",
    "RelatedItem": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/1",
    "Updateable": true,
    "Version": "0108"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00NTSMF

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00NTSMF",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-KPM51VUG800G-serial-Y9B0A00NTSMF",
    "Name": "HDD-model-KPM51VUG800G-serial-Y9B0A00NTSMF",
    "RelatedItem": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/23",
    "Updateable": true,
    "Version": "0108"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00STSMF

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00STSMF",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-KPM51VUG800G-serial-Y9B0A00STSMF",
    "Name": "HDD-model-KPM51VUG800G-serial-Y9B0A00STSMF",
    "RelatedItem": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/24",
    "Updateable": true,
    "Version": "0108"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00VTSMF

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-KPM51VUG800G-serial-Y9B0A00VTSMF",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-KPM51VUG800G-serial-Y9B0A00VTSMF",
    "Name": "HDD-model-KPM51VUG800G-serial-Y9B0A00VTSMF",
    "RelatedItem": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID/Drives/2",
    "Updateable": true,
    "Version": "0108"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/SasExpM5

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/SasExpM5",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "SasExpM5",
    "Name": "SasExpM5",
    "Updateable": true,
    "Version": "65.11.20.00"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/UCSC-RAID-M5HD-slot-MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCSC-RAID-M5HD-slot-MRAID",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "UCSC-RAID-M5HD-slot-MRAID",
    "Name": "UCSC-RAID-M5HD-slot-MRAID",
    "RelatedItem": "/redfish/v1/Systems/WZP23450C8K/Storage/MRAID",
    "Updateable": true,
    "Version": "51.10.0-3612"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/UCS_VIC_1387-slot-MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCS_VIC_1387-slot-MLOM",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "UCS_VIC_1387-slot-MLOM",
    "Name": "UCS_VIC_1387-slot-MLOM",
    "Updateable": true,
    "Version": "4.4(3a)"
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
    "Version": "0x80001516-1.823.2"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/XL710-slot-4

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/XL710-slot-4",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "XL710-slot-4",
    "Name": "XL710-slot-4",
    "Updateable": true,
    "Version": "0x80009E5A-1.823.2"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/XL710-slot-6

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/XL710-slot-6",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "XL710-slot-6",
    "Name": "XL710-slot-6",
    "Updateable": true,
    "Version": "0x80009E5A-1.823.2"
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

