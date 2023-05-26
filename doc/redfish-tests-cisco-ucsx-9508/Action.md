# Redfish Action Resources

Vendor | Model
--- | ---
Cisco | UCSX-9508

```
# iserver get redfish endpoint
    --cache chassis-UCSX-9508-fox2521p34m
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Chassis
    --inventory-id IoCard-1-1
    --action
    --deep
    --max 0

/api-explorer/resources/redfish/v1/Chassis/Blade1
-------------------------------------------------
{
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade1/Actions/Chassis.Reset"
        }
    }
}

/api-explorer/resources/redfish/v1/Chassis/Blade2
-------------------------------------------------
{
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade2/Actions/Chassis.Reset"
        }
    }
}

/api-explorer/resources/redfish/v1/Chassis/Blade3
-------------------------------------------------
{
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade3/Actions/Chassis.Reset"
        }
    }
}

/api-explorer/resources/redfish/v1/Chassis/Blade4
-------------------------------------------------
{
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade4/Actions/Chassis.Reset"
        }
    }
}

/api-explorer/resources/redfish/v1/Chassis/Blade5
-------------------------------------------------
{
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade5/Actions/Chassis.Reset"
        }
    }
}

/api-explorer/resources/redfish/v1/Chassis/Blade6
-------------------------------------------------
{
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade6/Actions/Chassis.Reset"
        }
    }
}

/api-explorer/resources/redfish/v1/Chassis/Blade7
-------------------------------------------------
{
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade7/Actions/Chassis.Reset"
        }
    }
}

/api-explorer/resources/redfish/v1/Chassis/Blade8
-------------------------------------------------
{
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade8/Actions/Chassis.Reset"
        }
    }
}

/api-explorer/resources/redfish/v1/Managers/CMC
-----------------------------------------------
{
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "ForceRestart"
            ],
            "target": "/redfish/v1/Managers/CMC/Actions/Manager.Reset"
        },
        "Oem": {
            "#Cisco.ExportTechSupport": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ExportTechSupport",
                "Protocol@Redfish.AllowableValues": [
                    "TFTP"
                ],
                "RemoteFilename@Redfish.AllowableValues": [
                    "Tech support filename on remote machine"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "IP Address String"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "Directory path of tech support file on remote machine"
                ],
                "target": "/redfish/v1/Managers/CMC/Actions/Oem/Cisco.ExportTechSupport"
            },
            "#Cisco.ResetToFactoryDefaults": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetToFactoryDefaults",
                "target": "/redfish/v1/Managers/CMC/Actions/Oem/Cisco.ResetToFactoryDefaults"
            }
        }
    }
}

/api-explorer/resources/redfish/v1/Managers/CMC/LogServices/CMC
---------------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.TestRemoteSyslogCfg": {
                "target": "/redfish/v1/Managers/CMC/LogServices/CMC/Actions/Oem/CiscoUCSExtensions.TestRemoteSyslogCfg"
            }
        }
    }
}

/api-explorer/resources/redfish/v1/Managers/PeerCMC
---------------------------------------------------
{
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "ForceRestart"
            ],
            "target": "/redfish/v1/Managers/PeerCMC/Actions/Manager.Reset"
        }
    }
}

/api-explorer/resources/redfish/v1/UpdateService
------------------------------------------------
{
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
    }
}
```