# Resource: /redfish/v1/UpdateService

Vendor | Model
--- | ---
Cisco | UCSS-S3260

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
                "Array of Software/Firmware Inventory URI of /redfish/v1/UpdateService/FirmwareInventory/BMC1 or /redfish/v1/UpdateService/FirmwareInventory/BMC2 or /redfish/v1/UpdateService/FirmwareInventory/CMC1 or /redfish/v1/UpdateService/FirmwareInventory/CMC2 or /redfish/v1/UpdateService/FirmwareInventory/BIOS1 or /redfish/v1/UpdateService/FirmwareInventory/BIOS2 indicating where the image is to be applied."
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
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/SASEXP1"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/SASEXP2"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/BMC1"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/BIOS1"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/S1_slot-SIOC1"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/S1_slot-SBMezz1"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/CMC1"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/CMC2"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-1"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-2"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-3"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-4"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-5"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-6"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-7"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-8"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-9"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-10"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-11"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-12"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-13"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-14"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-15"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-55"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-56"
        }
    ],
    "Members@odata.count": 25,
    "Name": "Firmware Inventory"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/BIOS1

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/BIOS1",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "BIOS1",
    "Name": "BIOS1",
    "Updateable": true,
    "Version": "C3X60M4.4.1.2c.0.0202211901\n"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/BMC1

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/BMC1",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "BMC1",
    "Name": "BMC1",
    "Updateable": true,
    "Version": "4.1(3d)"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/CMC1

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/CMC1",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "CMC1",
    "Name": "CMC1",
    "Updateable": true,
    "Version": "4.1(3d)"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/CMC2

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/CMC2",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "CMC2",
    "Name": "CMC2",
    "Updateable": true,
    "Version": "N/A"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-1

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-1",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-1",
    "Name": "HDD-1",
    "Updateable": true,
    "Version": "A320"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-10

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-10",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-10",
    "Name": "HDD-10",
    "Updateable": true,
    "Version": "5705"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-11

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-11",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-11",
    "Name": "HDD-11",
    "Updateable": true,
    "Version": "A320"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-12

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-12",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-12",
    "Name": "HDD-12",
    "Updateable": true,
    "Version": "A320"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-13

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-13",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-13",
    "Name": "HDD-13",
    "Updateable": true,
    "Version": "A320"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-14

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-14",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-14",
    "Name": "HDD-14",
    "Updateable": true,
    "Version": "A320"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-15

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-15",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-15",
    "Name": "HDD-15",
    "Updateable": true,
    "Version": "5705"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-2

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-2",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-2",
    "Name": "HDD-2",
    "Updateable": true,
    "Version": "A320"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-3

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-3",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-3",
    "Name": "HDD-3",
    "Updateable": true,
    "Version": "A320"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-4

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-4",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-4",
    "Name": "HDD-4",
    "Updateable": true,
    "Version": "A320"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-5

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-5",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-5",
    "Name": "HDD-5",
    "Updateable": true,
    "Version": "A320"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-55

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-55",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-55",
    "Name": "HDD-55",
    "Updateable": true,
    "Version": "0104"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-56

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-56",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-56",
    "Name": "HDD-56",
    "Updateable": true,
    "Version": "0104"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-6

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-6",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-6",
    "Name": "HDD-6",
    "Updateable": true,
    "Version": "A320"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-7

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-7",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-7",
    "Name": "HDD-7",
    "Updateable": true,
    "Version": "A320"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-8

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-8",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-8",
    "Name": "HDD-8",
    "Updateable": true,
    "Version": "A320"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/HDD-9

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/HDD-9",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "HDD-9",
    "Name": "HDD-9",
    "Updateable": true,
    "Version": "A320"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/S1_slot-SBMezz1

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/S1_slot-SBMezz1",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "S1_slot-SBMezz1",
    "Name": "S1_slot-SBMezz1",
    "Updateable": true,
    "Version": "29.00.1-0360"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/S1_slot-SIOC1

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/S1_slot-SIOC1",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "S1_slot-SIOC1",
    "Name": "S1_slot-SIOC1",
    "Updateable": true,
    "Version": "4.4(3a)"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/SASEXP1

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/SASEXP1",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "SASEXP1",
    "Name": "SASEXP1",
    "Updateable": true,
    "Version": "04.08.01_B083"
}
```

## /redfish/v1/UpdateService/FirmwareInventory/SASEXP2

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService/FirmwareInventory/Members/$entity",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/SASEXP2",
    "@odata.type": "#SoftwareInventory.v1_2_1.SoftwareInventory",
    "Id": "SASEXP2",
    "Name": "SASEXP2",
    "Updateable": true,
    "Version": "04.08.01_B083"
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
    "Name": "DeviceConnector",
    "Updateable": true,
    "Version": "1.0.11-2209"
}
```

