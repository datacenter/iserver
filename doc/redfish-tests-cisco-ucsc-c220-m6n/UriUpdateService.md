# Resource: /redfish/v1/UpdateService

Vendor | Model
--- | ---
Cisco | UCSC-C220-M6N

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
                    "This object specifies details required to access OS Answer file. This object shall have properties ImageRepository, TransferProtocol [SCP and TFTP], Username and Password."
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
                    "This parameter specifies the disk where OS is to be installed. For local disks use @odataid to specify storage URI URI and for remote disks, use TargetUri to specify the SAN LUN URI."
                ],
                "TargetOS@Redfish.AllowableValues": [
                    "This object specifies details of OS to be installed. This object shall have properties OSName and OSEdition."
                ],
                "TargetUri@Redfish.AllowableValues": [
                    "URI of SAN LUN - cisco-ucs-fc:<HostWWPN>:<LUNID>:<TargetWWPN> or cisco-ucs-iscsi:<HostMACAdress>:<TargetLUNID>:<TargetIQN>"
                ],
                "TransferProtocol@Redfish.AllowableValues": [
                    "CIFS",
                    "HTTPS",
                    "NFS",
                    "VMEDIA-CIFS",
                    "VMEDIA-HTTPS",
                    "VMEDIA-NFS",
                    "SCP",
                    "TFTP",
                    "LOCAL-HOST"
                ],
                "Username@Redfish.AllowableValues": [
                    "The username to be used while accessing shared location specified by the ImageRepository parameter."
                ],
                "target": "/redfish/v1/UpdateService/Actions/Oem/CiscoUCSExtensions.PrepareOSInstall"
            },
            "#CiscoUCSExtensions.UCSUpdate": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UCSUpdate",
                "AdaptorDowngradeSecurityLevel@Redfish.AllowableValues": [
                    true,
                    false
                ],
                "AdaptorSecureUpdate@Redfish.AllowableValues": [
                    true,
                    false
                ],
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
                    "This parameter shall specify the directory path of extracted HSU bundle or the string URI of the remote HUU ISO file. Standard mount options can be specified as query parameter to the URI."
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
                    "VMEDIA-NFS",
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
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCSC-M-V100-04-slot-MLOM"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCSC-GPU-T4-16-slot-3"
        }
    ],
    "Members@odata.count": 5,
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
    "RelatedItem": [
        {
            "@odata.id": "/redfish/v1/Systems/WZP262207W0"
        }
    ],
    "Updateable": true,
    "Version": "C225M6.4.2.2b.0.0509222122"
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
    "Version": "23.0"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/CIMC

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/CIMC",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "CIMC",
    "Name": "CIMC",
    "RelatedItem": [
        {
            "@odata.id": "/redfish/v1/Managers/CIMC"
        }
    ],
    "Updateable": true,
    "Version": "4.2(2a)"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/UCSC-GPU-T4-16-slot-3

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCSC-GPU-T4-16-slot-3",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "UCSC-GPU-T4-16-slot-3",
    "Name": "UCSC-GPU-T4-16-slot-3",
    "Updateable": true
}
```

## /redfish/v1/UpdateService/FirmwareInventory/UCSC-M-V100-04-slot-MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/UCSC-M-V100-04-slot-MLOM",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "UCSC-M-V100-04-slot-MLOM",
    "Name": "UCSC-M-V100-04-slot-MLOM",
    "Updateable": true,
    "Version": "5.2(2b)"
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

