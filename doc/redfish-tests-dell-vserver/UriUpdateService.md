# Resource: /redfish/v1/UpdateService

Vendor | Model
--- | ---
Dell | vServer

## /redfish/v1/UpdateService

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService.UpdateService",
    "@odata.id": "/redfish/v1/UpdateService",
    "@odata.type": "#UpdateService.v1_8_1.UpdateService",
    "Actions": {
        "#UpdateService.SimpleUpdate": {
            "@Redfish.OperationApplyTimeSupport": {
                "@odata.type": "#Settings.v1_3_1.OperationApplyTimeSupport",
                "SupportedValues": [
                    "Immediate",
                    "OnReset",
                    "OnStartUpdateRequest"
                ]
            },
            "TransferProtocol@Redfish.AllowableValues": [
                "HTTP",
                "NFS",
                "CIFS",
                "TFTP",
                "HTTPS"
            ],
            "target": "/redfish/v1/UpdateService/Actions/UpdateService.SimpleUpdate"
        },
        "#UpdateService.StartUpdate": {
            "target": "/redfish/v1/UpdateService/Actions/UpdateService.StartUpdate"
        },
        "Oem": {
            "DellUpdateService.v1_1_0#DellUpdateService.Install": {
                "InstallUpon@Redfish.AllowableValues": [
                    "Now",
                    "NowAndReboot",
                    "NextReboot"
                ],
                "target": "/redfish/v1/UpdateService/Actions/Oem/DellUpdateService.Install"
            }
        }
    },
    "Description": "Represents the properties for the Update Service",
    "FirmwareInventory": {
        "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory"
    },
    "HttpPushUri": "/redfish/v1/UpdateService/FirmwareInventory",
    "Id": "UpdateService",
    "MaxImageSizeBytes": null,
    "MultipartHttpPushUri": "/redfish/v1/UpdateService/MultipartUpload",
    "Name": "Update Service",
    "ServiceEnabled": true,
    "SoftwareInventory": {
        "@odata.id": "/redfish/v1/UpdateService/SoftwareInventory"
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/UpdateService/FirmwareInventory

```
```

## /redfish/v1/UpdateService/FirmwareInventory/Current-159-1.2.4__BIOS.Setup.1-1

```
```

## /redfish/v1/UpdateService/FirmwareInventory/Installed-159-1.2.4__BIOS.Setup.1-1

```
```

## /redfish/v1/UpdateService/FirmwareInventory/Installed-25227-5.10.00.00__iDRAC.Embedded.1-1

```
```

## /redfish/v1/UpdateService/FirmwareInventory/Previous-25227-5.00.20.10__iDRAC.Embedded.1-1

```
```

## /redfish/v1/UpdateService/SoftwareInventory

```
```

