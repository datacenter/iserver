# Redfish Action Resources

Vendor | Model
--- | ---
Cisco | UCSC-C240-M4SX

```
# iserver get redfish endpoint
    --cache ucsc-ucs-c240-m4sx-fch2017v1j7-4.1.2g-off
    --type ucsc
    --ip 10.58.50.48
    --username admin
    --password ******
    --action
    --deep
    --max 0

/redfish/v1/CertificateService
------------------------------
{
    "Actions": {
        "#CertificateService.GenerateCSR": {
            "target": "/redfish/v1/CertificateService/Actions/CertificateService.GenerateCSR"
        },
        "#CertificateService.ReplaceCertificate": {
            "target": "/redfish/v1/CertificateService/Actions/CertificateService.ReplaceCertificate"
        }
    }
}

/redfish/v1/Chassis/1
---------------------
{
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/1/Actions/Chassis.Reset"
        }
    }
}

/redfish/v1/EventService
------------------------
{
    "Actions": {
        "#EventService.SubmitTestEvent": {
            "target": "/redfish/v1/EventService/Actions/EventService.SubmitTestEvent"
        }
    }
}

/redfish/v1/Managers/CIMC
-------------------------
{
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "ForceRestart"
            ],
            "target": "/redfish/v1/Managers/CIMC/Actions/Manager.Reset"
        },
        "Oem": {
            "#CiscoUCSExtensions.BiosFwActivate": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.BiosFwActivate"
            },
            "#CiscoUCSExtensions.BmcFwActivate": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.BmcFwActivate"
            },
            "#CiscoUCSExtensions.BmcTechSupportExport": {
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
                    "Valid Remote Share Path and filename with valid extension (tar.gz)"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.BmcTechSupportExport"
            },
            "#CiscoUCSExtensions.ExportBmcConfig": {
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
                    "Valid Remote Share Path and filename with valid extension (.xml)"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.ExportBmcConfig"
            },
            "#CiscoUCSExtensions.ImportBmcConfig": {
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
                    "Valid Remote Share Path and filename with valid extension (.xml)"
                ],
                "RemoteUsername@Redfish.AllowableValues": [
                    "Remote Server Username"
                ],
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.ImportBmcConfig"
            },
            "#CiscoUCSExtensions.SigningRequest": {
                "@odata.type": "CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "HashToSign@Redfish.AllowableValues": [
                    "SHA-256 hash encoded in base64"
                ],
                "RequestID@Redfish.AllowableValues": [
                    "A unique string generated by the requester to match response, min is 1 and max is 128"
                ],
                "RequestedSignatureAlgorithm@Redfish.AllowableValues": [
                    "Signing algorithm to be used, currently supported algorithm is ECCsecp256r1"
                ],
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.SigningRequest"
            }
        }
    }
}

/redfish/v1/Managers/CIMC/VirtualMedia/0
----------------------------------------
{
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/CIMC/VirtualMedia/0/Actions/VirtualMedia.EjectMedia"
        },
        "#VirtualMedia.InsertMedia": {
            "Image@Redfish.AllowableValues": [
                "This parameter shall specify the string URI of the remote media to be attached to the virtual media. (Required)"
            ],
            "Inserted@Redfish.AllowableValues": [
                "true"
            ],
            "Password@Redfish.AllowableValues": [
                "This parameter shall contain a string representing the password to be used when accessing the URI specified by the Image parameter."
            ],
            "TransferMethod@Redfish.AllowableValues": [
                "Stream"
            ],
            "TransferProtocolType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "NFS"
            ],
            "UserName@Redfish.AllowableValues": [
                "This parameter shall contain a string representing the username to be used when accessing the URI specified by the Image parameter."
            ],
            "WriteProtected@Redfish.AllowableValues": [
                "true"
            ],
            "target": "/redfish/v1/Managers/CIMC/VirtualMedia/0/Actions/VirtualMedia.InsertMedia"
        }
    }
}

/redfish/v1/Managers/CIMC/VirtualMedia/1
----------------------------------------
{
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/CIMC/VirtualMedia/1/Actions/VirtualMedia.EjectMedia"
        },
        "#VirtualMedia.InsertMedia": {
            "Image@Redfish.AllowableValues": [
                "This parameter shall specify the string URI of the remote media to be attached to the virtual media. (Required)"
            ],
            "Inserted@Redfish.AllowableValues": [
                "true"
            ],
            "Password@Redfish.AllowableValues": [
                "This parameter shall contain a string representing the password to be used when accessing the URI specified by the Image parameter."
            ],
            "TransferMethod@Redfish.AllowableValues": [
                "Stream"
            ],
            "TransferProtocolType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "NFS"
            ],
            "UserName@Redfish.AllowableValues": [
                "This parameter shall contain a string representing the username to be used when accessing the URI specified by the Image parameter."
            ],
            "WriteProtected@Redfish.AllowableValues": [
                "true"
            ],
            "target": "/redfish/v1/Managers/CIMC/VirtualMedia/1/Actions/VirtualMedia.InsertMedia"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7
-------------------------------
{
    "Actions": {
        "#ComputerSystem.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff",
                "GracefulShutdown",
                "ForceRestart",
                "Nmi",
                "PowerCycle"
            ],
            "target": "/redfish/v1/Systems/FCH2017V1J7/Actions/ComputerSystem.Reset"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7/Bios
------------------------------------
{
    "Actions": {
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Bios/Actions/Bios.ResetBios"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0
---------------------------------------------------
{
    "Actions": {
        "#Storage.SetEncryptionKey": {
            "SecurityKey@Redfish.AllowableValues": [
                "Security Key"
            ],
            "SecurityKeyId@Redfish.AllowableValues": [
                "Security Key Identifier"
            ],
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Actions/Storage.SetEncryptionKey"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-1
-----------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-1/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-2
-----------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-2/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Volumes/Hypervisor
----------------------------------------------------------------------
{
    "Actions": {
        "#Volume.Initialize": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Volumes/Hypervisor/Actions/Volume.Initialize"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA
------------------------------------------------
{
    "Actions": {
        "#Storage.SetEncryptionKey": {
            "SecurityKey@Redfish.AllowableValues": [
                "Security Key"
            ],
            "SecurityKeyId@Redfish.AllowableValues": [
                "Security Key Identifier"
            ],
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Actions/Storage.SetEncryptionKey"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-1
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-1/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-2
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-2/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-3
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-3/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-4
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-4/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-5
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-5/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-6
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-6/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-7
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-7/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes/VD-0
-------------------------------------------------------------
{
    "Actions": {
        "#Volume.Initialize": {
            "target": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Volumes/VD-0/Actions/Volume.Initialize"
        }
    }
}

/redfish/v1/UpdateService
-------------------------
{
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
    }
}
```