# Resource: /api-explorer/resources/redfish/v1/UpdateService

Vendor | Model
--- | ---
Cisco | UCSX-9508

## /api-explorer/resources/redfish/v1/UpdateService

```{
    "@odata.context": "/redfish/v1/$metadata#UpdateService.UpdateService",
    "@odata.id": "/redfish/v1/UpdateService",
    "@odata.type": "#UpdateService.v1_5_0.UpdateService",
    "Actions": {
        "#UpdateService.SimpleUpdate": {
            "ImageURI@Redfish.AllowableValues": [
                "Path to Image File"
            ],
            "Targets@Redfish.AllowableValues": [
                "/redfish/v1/UpdateService/FirmwareInventory/CMC"
            ],
            "TransferProtocol@Redfish.AllowableValues": [
                "TFTP"
            ],
            "target": "/redfish/v1/UpdateService/Actions/UpdateService.SimpleUpdate"
        },
        "Oem": {
            "#Cisco.ActivatePsuFirmware": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ActivatePsuFirmware",
                "Target@Redfish.AllowableValues": [
                    "/redfish/v1/UpdateService/FirmwareInventory/PSU1",
                    "/redfish/v1/UpdateService/FirmwareInventory/PSU2",
                    "/redfish/v1/UpdateService/FirmwareInventory/PSU3",
                    "/redfish/v1/UpdateService/FirmwareInventory/PSU4",
                    "/redfish/v1/UpdateService/FirmwareInventory/PSU5",
                    "/redfish/v1/UpdateService/FirmwareInventory/PSU6"
                ],
                "UpdateType@Redfish.AllowableValues": [
                    "Primary",
                    "Secondary"
                ],
                "target": "/redfish/v1/UpdateService/Actions/Oem/Cisco.ActivatePsuFirmware"
            },
            "#Cisco.SetStartImageVersion": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.SetStartImageVersion",
                "ImageVersion@Redfish.AllowableValues": [
                    "Image Version"
                ],
                "Target@Redfish.AllowableValues": [
                    "/redfish/v1/UpdateService/FirmwareInventory/CMC"
                ],
                "target": "/redfish/v1/UpdateService/Actions/Oem/Cisco.SetStartImageVersion"
            },
            "#Cisco.UpdatePsuFirmware": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UpdatePsuFirmware",
                "ImageURI@Redfish.AllowableValues": [
                    "Path to Image File"
                ],
                "Target@Redfish.AllowableValues": [
                    "/redfish/v1/UpdateService/FirmwareInventory/PSU1",
                    "/redfish/v1/UpdateService/FirmwareInventory/PSU2",
                    "/redfish/v1/UpdateService/FirmwareInventory/PSU3",
                    "/redfish/v1/UpdateService/FirmwareInventory/PSU4",
                    "/redfish/v1/UpdateService/FirmwareInventory/PSU5",
                    "/redfish/v1/UpdateService/FirmwareInventory/PSU6"
                ],
                "TransferProtocol@Redfish.AllowableValues": [
                    "TFTP"
                ],
                "UpdateType@Redfish.AllowableValues": [
                    "Primary",
                    "Secondary"
                ],
                "target": "/redfish/v1/UpdateService/Actions/Oem/Cisco.UpdatePsuFirmware"
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
    "ServiceEnabled": true
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
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/FPGA"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/BIOS"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/CMC"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/PSU1"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/PSU2"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/PSU3"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/PSU4"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/PSU5"
        },
        {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/PSU6"
        }
    ],
    "Members@odata.count": 9,
    "Name": "Firmware Inventory"
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/BIOS

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/BIOS",
    "@odata.type": "#SoftwareInventory.v1_2_2.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "BIOS",
    "Name": "BIOS",
    "Updateable": true,
    "Version": "3.2.36"
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/CMC

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/CMC",
    "@odata.type": "#SoftwareInventory.v1_2_2.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "CMC",
    "Name": "CMC",
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "StartImage": "4.2(2c)",
            "UpdateStatus": "idle",
            "UpdateStatusDetailed": "Update Status Undefined",
            "Versions": [
                {
                    "Status": "OK",
                    "Version": "4.2(2c)"
                },
                {
                    "Status": "OK",
                    "Version": "4.2(2.220322)"
                }
            ]
        }
    },
    "Updateable": true,
    "Version": "4.2(2c)"
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/FPGA

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/FPGA",
    "@odata.type": "#SoftwareInventory.v1_2_2.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "FPGA",
    "Name": "FPGA",
    "Updateable": true,
    "Version": "0x208"
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/PSU1

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/PSU1",
    "@odata.type": "#SoftwareInventory.v1_2_2.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "PSU1",
    "Name": "PSU1",
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "Primary": {
                "StagingVersion": "/./././",
                "UpdateStatus": "idle",
                "UpdateStatusDetailed": "Update Status Undefined",
                "Version": "1.1.2.0"
            },
            "Secondary": {
                "StagingVersion": "2.0.0.0",
                "UpdateStatus": "idle",
                "UpdateStatusDetailed": "Update Status Undefined",
                "Version": "2.2.0.0"
            }
        }
    },
    "Updateable": true
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/PSU2

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/PSU2",
    "@odata.type": "#SoftwareInventory.v1_2_2.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "PSU2",
    "Name": "PSU2",
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "Primary": {
                "StagingVersion": "",
                "UpdateStatus": "idle",
                "UpdateStatusDetailed": "Update Status Undefined",
                "Version": ""
            },
            "Secondary": {
                "StagingVersion": "",
                "UpdateStatus": "idle",
                "UpdateStatusDetailed": "Update Status Undefined",
                "Version": ""
            }
        }
    },
    "Updateable": true
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/PSU3

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/PSU3",
    "@odata.type": "#SoftwareInventory.v1_2_2.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "PSU3",
    "Name": "PSU3",
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "Primary": {
                "StagingVersion": "",
                "UpdateStatus": "idle",
                "UpdateStatusDetailed": "Update Status Undefined",
                "Version": ""
            },
            "Secondary": {
                "StagingVersion": "",
                "UpdateStatus": "idle",
                "UpdateStatusDetailed": "Update Status Undefined",
                "Version": ""
            }
        }
    },
    "Updateable": true
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/PSU4

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/PSU4",
    "@odata.type": "#SoftwareInventory.v1_2_2.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "PSU4",
    "Name": "PSU4",
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "Primary": {
                "StagingVersion": "/./././",
                "UpdateStatus": "idle",
                "UpdateStatusDetailed": "Update Status Undefined",
                "Version": "1.1.2.0"
            },
            "Secondary": {
                "StagingVersion": "2.0.0.0",
                "UpdateStatus": "idle",
                "UpdateStatusDetailed": "Update Status Undefined",
                "Version": "2.2.0.0"
            }
        }
    },
    "Updateable": true
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/PSU5

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/PSU5",
    "@odata.type": "#SoftwareInventory.v1_2_2.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "PSU5",
    "Name": "PSU5",
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "Primary": {
                "StagingVersion": "",
                "UpdateStatus": "idle",
                "UpdateStatusDetailed": "Update Status Undefined",
                "Version": ""
            },
            "Secondary": {
                "StagingVersion": "",
                "UpdateStatus": "idle",
                "UpdateStatusDetailed": "Update Status Undefined",
                "Version": ""
            }
        }
    },
    "Updateable": true
}
```

## /api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/PSU6

```{
    "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
    "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/PSU6",
    "@odata.type": "#SoftwareInventory.v1_2_2.SoftwareInventory",
    "Description": "Firmware Inventory",
    "Id": "PSU6",
    "Name": "PSU6",
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "Primary": {
                "StagingVersion": "",
                "UpdateStatus": "idle",
                "UpdateStatusDetailed": "Update Status Undefined",
                "Version": ""
            },
            "Secondary": {
                "StagingVersion": "",
                "UpdateStatus": "idle",
                "UpdateStatusDetailed": "Update Status Undefined",
                "Version": ""
            }
        }
    },
    "Updateable": true
}
```

