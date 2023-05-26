# Resource: /redfish/v1/UpdateService

Vendor | Model
--- | ---
Cisco | UCSC-C240-M5SN

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
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-SSDSC2KB960G7K-serial-PHYS746100ZW960CGN"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-SSDSC2KB960G7K-serial-PHYS746002M1960CGN"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-SSDSC2KB960G7K-serial-PHYS746002ME960CGN"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-SSDSC2KB960G7K-serial-PHYS746003DM960CGN"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK65JQF0000C0259760"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK65LZ70000C02597DN"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK65LD10000C024KKJM"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK64DPD0000C0244K8B"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK64DX60000C025BW6X"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0088-serial-Z4000FFD0000R616HPN9"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/mswitchp"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/XXV710-DA2-slot-3"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/XXV710-DA2-slot-6"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/X550-LOM-slot-L"
        }
    ],
    "Members@odata.count": 18,
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
    "RelatedItem": "/redfish/v1/Systems/WZP23400AK4",
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
    "Version": "52.0"
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

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-SSDSC2KB960G7K-serial-PHYS746002M1960CGN

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-SSDSC2KB960G7K-serial-PHYS746002M1960CGN",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-SSDSC2KB960G7K-serial-PHYS746002M1960CGN",
    "Name": "HDD-model-SSDSC2KB960G7K-serial-PHYS746002M1960CGN",
    "RelatedItem": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10",
    "Updateable": true,
    "Version": "SCV1CS08"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-SSDSC2KB960G7K-serial-PHYS746002ME960CGN

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-SSDSC2KB960G7K-serial-PHYS746002ME960CGN",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-SSDSC2KB960G7K-serial-PHYS746002ME960CGN",
    "Name": "HDD-model-SSDSC2KB960G7K-serial-PHYS746002ME960CGN",
    "RelatedItem": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11",
    "Updateable": true,
    "Version": "SCV1CS08"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-SSDSC2KB960G7K-serial-PHYS746003DM960CGN

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-SSDSC2KB960G7K-serial-PHYS746003DM960CGN",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-SSDSC2KB960G7K-serial-PHYS746003DM960CGN",
    "Name": "HDD-model-SSDSC2KB960G7K-serial-PHYS746003DM960CGN",
    "RelatedItem": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12",
    "Updateable": true,
    "Version": "SCV1CS08"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-SSDSC2KB960G7K-serial-PHYS746100ZW960CGN

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-SSDSC2KB960G7K-serial-PHYS746100ZW960CGN",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-SSDSC2KB960G7K-serial-PHYS746100ZW960CGN",
    "Name": "HDD-model-SSDSC2KB960G7K-serial-PHYS746100ZW960CGN",
    "RelatedItem": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9",
    "Updateable": true,
    "Version": "SCV1CS08"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK64DPD0000C0244K8B

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK64DPD0000C0244K8B",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-ST1200MM0009-serial-WFK64DPD0000C0244K8B",
    "Name": "HDD-model-ST1200MM0009-serial-WFK64DPD0000C0244K8B",
    "RelatedItem": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16",
    "Updateable": true,
    "Version": "CN03"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK64DX60000C025BW6X

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK64DX60000C025BW6X",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-ST1200MM0009-serial-WFK64DX60000C025BW6X",
    "Name": "HDD-model-ST1200MM0009-serial-WFK64DX60000C025BW6X",
    "RelatedItem": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17",
    "Updateable": true,
    "Version": "CN03"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK65JQF0000C0259760

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK65JQF0000C0259760",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-ST1200MM0009-serial-WFK65JQF0000C0259760",
    "Name": "HDD-model-ST1200MM0009-serial-WFK65JQF0000C0259760",
    "RelatedItem": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13",
    "Updateable": true,
    "Version": "CN03"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK65LD10000C024KKJM

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK65LD10000C024KKJM",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-ST1200MM0009-serial-WFK65LD10000C024KKJM",
    "Name": "HDD-model-ST1200MM0009-serial-WFK65LD10000C024KKJM",
    "RelatedItem": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15",
    "Updateable": true,
    "Version": "CN03"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK65LZ70000C02597DN

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0009-serial-WFK65LZ70000C02597DN",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-ST1200MM0009-serial-WFK65LZ70000C02597DN",
    "Name": "HDD-model-ST1200MM0009-serial-WFK65LZ70000C02597DN",
    "RelatedItem": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14",
    "Updateable": true,
    "Version": "CN03"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0088-serial-Z4000FFD0000R616HPN9

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-model-ST1200MM0088-serial-Z4000FFD0000R616HPN9",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-model-ST1200MM0088-serial-Z4000FFD0000R616HPN9",
    "Name": "HDD-model-ST1200MM0088-serial-Z4000FFD0000R616HPN9",
    "RelatedItem": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18",
    "Updateable": true,
    "Version": "N0A4"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/UCSC-RAID-M5-slot-MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCSC-RAID-M5-slot-MRAID",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "UCSC-RAID-M5-slot-MRAID",
    "Name": "UCSC-RAID-M5-slot-MRAID",
    "RelatedItem": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID",
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
    "Version": "0x80001516-1.823.2"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/XXV710-DA2-slot-3

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/XXV710-DA2-slot-3",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "XXV710-DA2-slot-3",
    "Name": "XXV710-DA2-slot-3",
    "Updateable": true,
    "Version": "0x80009E5D-1.823.2"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/XXV710-DA2-slot-6

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/XXV710-DA2-slot-6",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "XXV710-DA2-slot-6",
    "Name": "XXV710-DA2-slot-6",
    "Updateable": true,
    "Version": "0x80009E5D-1.823.2"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/mswitchp

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/mswitchp",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "mswitchp",
    "Name": "mswitchp",
    "Updateable": true,
    "Version": "1.8.0.58-24b3"
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

