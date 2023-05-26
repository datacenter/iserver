# Redfish Action Resources

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
    --action
    --deep
    --max 0

/redfish/v1/CertificateService
------------------------------
{
    "Actions": {
        "#CertificateService.GenerateCSR": {
            "CertificateCollection@Redfish.AllowableValues": [
                "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates/1"
            ],
            "KeyPairAlgorithm@Redfish.AllowableValues": [
                "TPM_ALG_SHA512",
                "TPM_ALG_SHA384",
                "TPM_ALG_SHA1",
                "TPM_ALG_SHA256"
            ],
            "target": "/redfish/v1/CertificateService/Actions/CertificateService.GenerateCSR"
        },
        "#CertificateService.ReplaceCertificate": {
            "CertificateType@Redfish.AllowableValues": [
                "PEM"
            ],
            "CertificateUri@Redfish.AllowableValues": [
                "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates/1",
                "/redfish/v1/AccountService/LDAP/Certificates/1"
            ],
            "target": "/redfish/v1/CertificateService/Actions/CertificateService.ReplaceCertificate"
        }
    }
}

/redfish/v1/Chassis/CMC
-----------------------
{
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/CMC/Actions/Chassis.Reset"
        }
    }
}

/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1
---------------------------------------------
{
    "Actions": {
        "#NetworkAdapter.ResetSettingsToDefault": {
            "target": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/Actions/NetworkAdapter.ResetSettingsToDefault"
        }
    }
}

/redfish/v1/Chassis/Server1
---------------------------
{
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Server1/Actions/Chassis.Reset"
        }
    }
}

/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1
-------------------------------------------------
{
    "Actions": {
        "#NetworkAdapter.ResetSettingsToDefault": {
            "target": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/Actions/NetworkAdapter.ResetSettingsToDefault"
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

/redfish/v1/Managers/BMC1
-------------------------
{
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "ForceRestart"
            ],
            "target": "/redfish/v1/Managers/BMC1/Actions/Manager.Reset"
        },
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

/redfish/v1/Managers/BMC1/LogServices/SEL
-----------------------------------------
{
    "Actions": {
        "#LogService.ClearLog": {
            "target": "/redfish/v1/Managers/BMC1/LogServices/SEL/Actions/LogService.ClearLog"
        }
    }
}

/redfish/v1/Managers/BMC1/VirtualMedia/0
----------------------------------------
{
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/BMC1/VirtualMedia/0/Actions/VirtualMedia.EjectMedia"
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
            "target": "/redfish/v1/Managers/BMC1/VirtualMedia/0/Actions/VirtualMedia.InsertMedia"
        }
    }
}

/redfish/v1/Managers/BMC1/VirtualMedia/1
----------------------------------------
{
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/BMC1/VirtualMedia/1/Actions/VirtualMedia.EjectMedia"
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
            "target": "/redfish/v1/Managers/BMC1/VirtualMedia/1/Actions/VirtualMedia.InsertMedia"
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

/redfish/v1/Systems/FCH21067808
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
            "target": "/redfish/v1/Systems/FCH21067808/Actions/ComputerSystem.Reset"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Bios
------------------------------------
{
    "Actions": {
        "#Bios.ResetBios": {
            "target": "/redfish/v1/Systems/FCH21067808/Bios/Actions/Bios.ResetBios"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1
-----------------------------------------------
{
    "Actions": {
        "#Storage.SetEncryptionKey": {
            "SecurityKey@Redfish.AllowableValues": [
                "Security Key"
            ],
            "SecurityKeyId@Redfish.AllowableValues": [
                "Security Key Identifier"
            ],
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Actions/Storage.SetEncryptionKey"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-1
-----------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-1/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-10
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-10/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-11
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-11/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-12
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-12/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-13
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-13/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-14
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-14/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-15
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-15/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-2
-----------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-2/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-201
-------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-201/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-202
-------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-202/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-3
-----------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-3/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-4
-----------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-4/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-5
-----------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-5/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-55
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-55/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-56
------------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-56/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-6
-----------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-6/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-7
-----------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-7/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-8
-----------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-8/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-9
-----------------------------------------------------------
{
    "Actions": {
        "#Drive.SecureErase": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-9/Actions/Drive.SecureErase"
        }
    }
}

/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Volumes/VD-0
------------------------------------------------------------
{
    "Actions": {
        "#Volume.Initialize": {
            "target": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Volumes/VD-0/Actions/Volume.Initialize"
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
    }
}
```