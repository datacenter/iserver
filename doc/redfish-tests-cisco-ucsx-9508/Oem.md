# Redfish Oem Resources

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
    --oem
    --deep
    --max 0

/api-explorer/resources/redfish/v1/
-----------------------------------
{
    "Oem": {
        "@odata.id": "/redfish/v1/Oem"
    }
}

/api-explorer/resources/redfish/v1/AccountService
-------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "AccountsCapabilities": [
                {
                    "AccountType": "Redfish",
                    "PasswordObfuscationCapabilities": [
                        "OriginalClear"
                    ]
                },
                {
                    "AccountType": "IPMI",
                    "PasswordObfuscationCapabilities": [
                        "OriginalClear"
                    ]
                },
                {
                    "AccountType": "SNMP",
                    "PasswordObfuscationCapabilities": [
                        "OriginalClear"
                    ]
                }
            ]
        }
    }
}

/api-explorer/resources/redfish/v1/Managers/CMC
-----------------------------------------------
{
    "Actions": {
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
    },
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "FanPolicy": "LowPower",
            "InventoryState": "FullInventoryReady"
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
    },
    "Oem": {
        "Cisco": {
            "SyslogConnectionInfo": [
                null,
                null
            ]
        }
    }
}

/api-explorer/resources/redfish/v1/UpdateService
------------------------------------------------
{
    "Actions": {
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

/api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/CMC
----------------------------------------------------------------------
{
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
    }
}

/api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/PSU1
-----------------------------------------------------------------------
{
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
    }
}

/api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/PSU2
-----------------------------------------------------------------------
{
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
    }
}

/api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/PSU3
-----------------------------------------------------------------------
{
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
    }
}

/api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/PSU4
-----------------------------------------------------------------------
{
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
    }
}

/api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/PSU5
-----------------------------------------------------------------------
{
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
    }
}

/api-explorer/resources/redfish/v1/UpdateService/FirmwareInventory/PSU6
-----------------------------------------------------------------------
{
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
    }
}
```