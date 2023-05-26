# Resource: /redfish/v1/UpdateService

Vendor | Model
--- | ---
Cisco | UCSC-C220-M4S

## /redfish/v1/UpdateService

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService",
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
                "SCP",
                "SFTP",
                "TFTP",
                "FTP",
                "HTTP"
            ],
            "Username@Redfish.AllowableValues": [
                "Server Username"
            ],
            "target": "/redfish/v1/UpdateService/Actions/UpdateService.SimpleUpdate"
        }
    },
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
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory",
    "@odata.type": "#SoftwareInventoryCollection.SoftwareInventoryCollection",
    "Description": "Inventory of Firmware components",
    "Members": [
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/slot-L"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/slot-1"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/slot-2"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/slot-MLOM"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/slot-HBA"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/CIMC"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/BIOS"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/FlexFlash-0"
        }
    ],
    "Members@odata.count": 8,
    "Name": "Firmware Inventory"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/BIOS

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/BIOS",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "BIOS",
    "Name": "BIOS",
    "Updateable": true,
    "Version": "C220M4.4.1.2c.0.0202211901"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/CIMC

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/CIMC",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "CIMC",
    "Name": "CIMC",
    "Updateable": true,
    "Version": "4.1(2g)"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/FlexFlash-0

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/FlexFlash-0",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "FlexFlash-0",
    "Name": "FlexFlash-0",
    "Updateable": false,
    "Version": "1.3.2 build 176"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/slot-1

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/slot-1",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "slot-1",
    "Name": "slot-1",
    "Updateable": true,
    "Version": "0x80009E63-1.823.2"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/slot-2

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/slot-2",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "slot-2",
    "Name": "slot-2",
    "Updateable": true,
    "Version": "0x800008A4-1.819.0"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/slot-HBA

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/slot-HBA",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "slot-HBA",
    "Name": "slot-HBA",
    "Updateable": true,
    "Version": "24.12.1-0456"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/slot-L

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/slot-L",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "slot-L",
    "Name": "slot-L",
    "Updateable": true,
    "Version": "0x80000E74-1.819.0"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/slot-MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/slot-MLOM",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "slot-MLOM",
    "Name": "slot-MLOM",
    "Updateable": true,
    "Version": "N/A"
}
```

## /redfish/v1/UpdateService/SoftwareInventory

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/SoftwareInventory",
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
    "@odata.context": "/redfish/v1/$metadata#UpdateService/SoftwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/SoftwareInventory/DeviceConnector",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "DeviceConnector",
    "Manufacturer": "Cisco Systems Inc.",
    "Name": "DeviceConnector",
    "Updateable": true,
    "Version": "1.0.11-2209"
}
```

