# Redfish Oem Resources

Vendor | Model
--- | ---
Cisco | UCSS-S3260

```
# iserver get redfish endpoint
    --cache ucsc-ucs-s3260-fch21067808--on
    --type ucsc
    --ip 10.58.50.34
    --username admin
    --password ******
    --oem
    --deep
    --max 0

/redfish/v1/Managers/BMC1
-------------------------
{
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.BiosFwActivate": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "target": "/redfish/v1/Managers/BMC1/Actions/Oem/CiscoUCSExtensions.BiosFwActivate"
            },
            "#CiscoUCSExtensions.ExportConfig": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "Protocol@Redfish.AllowableValues": [
                    "TFTP",
                    "SCP",
                    "SFTP",
                    "FTP",
                    "HTTP"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "Valid Hostname/IP Address"
                ],
                "RemotePassword@Redfish.AllowableValues": [
                    "Remote Server Password"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "Valid Remote Share Path"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/BMC1/Actions/Oem/CiscoUCSExtensions.ExportConfig"
            },
            "#CiscoUCSExtensions.FwActivate": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "target": "/redfish/v1/Managers/BMC1/Actions/Oem/CiscoUCSExtensions.FwActivate"
            },
            "#CiscoUCSExtensions.ImportConfig": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "Protocol@Redfish.AllowableValues": [
                    "TFTP",
                    "SCP",
                    "SFTP",
                    "FTP",
                    "HTTP"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "Valid Hostname/IP Address"
                ],
                "RemotePassword@Redfish.AllowableValues": [
                    "Remote Server Password"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "Valid Remote Share Path"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/BMC1/Actions/Oem/CiscoUCSExtensions.ImportConfig"
            },
            "#CiscoUCSExtensions.TechSupportExport": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "Protocol@Redfish.AllowableValues": [
                    "TFTP",
                    "SCP",
                    "SFTP",
                    "FTP",
                    "HTTP"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "Valid Hostname/IP Address"
                ],
                "RemotePassword@Redfish.AllowableValues": [
                    "Remote Server Password"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "Valid Remote Share Path"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/BMC1/Actions/Oem/CiscoUCSExtensions.TechSupportExport"
            }
        }
    }
}

/redfish/v1/Managers/CIMC
-------------------------
{
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.ExportConfig": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "Passphrase@Redfish.AllowableValues": [
                    "Passphrase"
                ],
                "Protocol@Redfish.AllowableValues": [
                    "TFTP",
                    "SCP",
                    "SFTP",
                    "FTP",
                    "HTTP"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "Valid Hostname/IP Address"
                ],
                "RemotePassword@Redfish.AllowableValues": [
                    "Remote Server Password"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "Valid Remote Share Path"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.ExportConfig"
            },
            "#CiscoUCSExtensions.FwActivate": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.FwActivate"
            },
            "#CiscoUCSExtensions.ImportConfig": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "Passphrase@Redfish.AllowableValues": [
                    "Passphrase"
                ],
                "Protocol@Redfish.AllowableValues": [
                    "TFTP",
                    "SCP",
                    "SFTP",
                    "FTP",
                    "HTTP"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "Valid Hostname/IP Address"
                ],
                "RemotePassword@Redfish.AllowableValues": [
                    "Remote Server Password"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "Valid Remote Share Path"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.ImportConfig"
            },
            "#CiscoUCSExtensions.TechSupportExport": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "Protocol@Redfish.AllowableValues": [
                    "TFTP",
                    "SCP",
                    "SFTP",
                    "FTP",
                    "HTTP"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "Valid Hostname/IP Address"
                ],
                "RemotePassword@Redfish.AllowableValues": [
                    "Remote Server Password"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "Valid Remote Share Path"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.TechSupportExport"
            }
        }
    }
}

/redfish/v1/TaskService/Tasks/BMC1ExportConfig
----------------------------------------------
{
    "Oem": {
        "Cisco": {
            "ExportStatus": "None"
        }
    }
}

/redfish/v1/TaskService/Tasks/BMC1FwUpdate
------------------------------------------
{
    "Oem": {
        "Cisco": {
            "FWVersion": "4.1(1f)",
            "UpdateStatus": "Success (100%)"
        }
    }
}

/redfish/v1/TaskService/Tasks/BMC1ImportConfig
----------------------------------------------
{
    "Oem": {
        "Cisco": {
            "ImportStatus": "Completed Successfully"
        }
    }
}

/redfish/v1/TaskService/Tasks/BMC1TechSupportExport
---------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "ExportStatus": "NA",
            "Protocol": "NA",
            "RemoteHostName": "NA",
            "RemotePath": "NA",
            "RemoteUsername": "NA"
        }
    }
}

/redfish/v1/TaskService/Tasks/Bios1FwUpdate
-------------------------------------------
{
    "Oem": {
        "Cisco": {
            "FWVersion": "C3X60M4.4.1.2c.0.0202211901",
            "UpdateStatus": "None, OK"
        }
    }
}

/redfish/v1/TaskService/Tasks/CIMCExportConfig
----------------------------------------------
{
    "Oem": {
        "Cisco": {
            "ExportStatus": "None"
        }
    }
}

/redfish/v1/TaskService/Tasks/CIMCFwUpdate
------------------------------------------
{
    "Oem": {
        "Cisco": {
            "FWVersion": "4.1(1f)",
            "UpdateStatus": "Success (100%)"
        }
    }
}

/redfish/v1/TaskService/Tasks/CIMCImportConfig
----------------------------------------------
{
    "Oem": {
        "Cisco": {
            "ImportStatus": "Completed Successfully"
        }
    }
}

/redfish/v1/TaskService/Tasks/CIMCTechSupportExport
---------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "ExportStatus": "NA",
            "Protocol": "NA",
            "RemoteHostName": "NA",
            "RemotePath": "NA",
            "RemoteUsername": "NA"
        }
    }
}

/redfish/v1/TaskService/Tasks/PeerCMCFwUpdate
---------------------------------------------
{
    "Oem": {
        "Cisco": {
            "FWVersion": "N/A",
            "UpdateStatus": "Starting (0%)"
        }
    }
}
```