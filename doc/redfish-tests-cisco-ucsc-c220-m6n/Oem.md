# Redfish Oem Resources

Vendor | Model
--- | ---
Cisco | UCSC-C220-M6N

```
# iserver get redfish endpoint
    --cache ucsc-c225-m6s-wzp262207w0-4.2.2a-off
    --type ucsc
    --ip 10.90.90.113
    --username admin
    --password ******
    --oem
    --deep
    --max 0

/redfish/v1/AccountService
--------------------------
{
    "LDAP": {
        "LDAPService": {
            "Oem": {
                "Cisco": {
                    "LDAPGroupAuthorizationEnabled": false
                }
            }
        }
    },
    "Oem": {
        "Cisco": {
            "PasswordExpiry": {
                "Enabled": false,
                "ExpiryDuration": 0,
                "GracePeriod": 0,
                "NotificationPeriod": 15
            },
            "PasswordHistory": 0,
            "StrongPasswordPolicyEnabled": true
        }
    }
}

/redfish/v1/Managers/CIMC
-------------------------
{
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.BiosFwActivate": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.BiosFwActivate"
            },
            "#CiscoUCSExtensions.BmcFwActivate": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.BmcFwActivate",
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.BmcFwActivate"
            },
            "#CiscoUCSExtensions.BmcTechSupportExport": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ExportTechSupport",
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
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ExportBmcConfig",
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
            "#CiscoUCSExtensions.HostOSBootManagement": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.HostOSBootManagement",
                "BootOption@Redfish.AllowableValues": [
                    "Immediate",
                    "OnNextBoot"
                ],
                "ImageRepository@Redfish.AllowableValues": [
                    "This parameter shall specify the directory path of extracted HSU bundle or the string URI of the remote HUU ISO file. Standard mount options can be specified as query parameter to the URI."
                ],
                "Mode@Redfish.AllowableValues": [
                    "Discovery",
                    "StartConfigure",
                    "EndConfigure"
                ],
                "Password@Redfish.AllowableValues": [
                    "The password to be used when accessing the URI specified by the ImageRepository parameter."
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
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.HostOSBootManagement"
            },
            "#CiscoUCSExtensions.ImportBmcConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ImportBmcConfig",
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
            "#CiscoUCSExtensions.ResetToFactoryDefaults": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetToFactoryDefaults",
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.ResetToFactoryDefaults"
            },
            "#CiscoUCSExtensions.SigningRequest": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.SigningRequest",
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
            },
            "#CiscoUCSExtenstions.KmipTestConnection": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.KmipTestConnection",
                "KMIPServer@Redfish.AllowableValues": [
                    "Primary",
                    "Secondary"
                ],
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.KmipTestConnection"
            },
            "#CiscoUCSExtenstions.ResetMemoryErrors": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetMemoryErrors",
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.ResetMemoryErrors"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "AggressiveCoolingEnabled": false,
            "CiscoInternalStorage": {
                "@odata.id": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage"
            },
            "CiscoKMIPClient": {
                "Certificates": {
                    "@odata.id": "/redfish/v1/Managers/CIMC/Oem/Cisco/CiscoKMIPClient/Certificates"
                },
                "KMIPServerSettings": {
                    "Enabled": false,
                    "KMIPServerPublicKey": false,
                    "KMIPServers": [],
                    "Password": null,
                    "UseKMIPLogin": false,
                    "UserName": null
                }
            },
            "EnableLowPowerUsb": true,
            "FanPolicy": "Acoustic",
            "HardwareX509Identity": {
                "Certificate": "-----BEGIN CERTIFICATE-----\nMIICazCCAfCgAwIBAgIKCQdXWJlhYISSCDAKBggqhkjOPQQDAjArMQ4wDAYDVQQK\nEwVDaXNjbzEZMBcGA1UEAxMQQUNUMiBFQ0MgU1VESSBDQTAgFw0yMjA2MDIwMzI1\nMTVaGA8yMDUzMDQwNDA4MTU0MlowdDEpMCcGA1UEBRMgUElEOlVDU0MtQzIyNS1N\nNlMgU046V1pQMjYyMjA3VzAxDjAMBgNVBAoTBUNpc2NvMRgwFgYDVQQLEw9BQ1Qt\nMiBMaXRlIFNVREkxHTAbBgNVBAMTFFVDUyBDLVNlcmllcyBTZXJ2ZXJzMFkwEwYH\nKoZIzj0CAQYIKoZIzj0DAQcDQgAEJt8J+tOb/1lpSMXCLlPiRjWytbR61NEN3X8U\nSR6CTEJN+6o1hpkNzvhDzx3wE6+Jmckk6OtGN588nvXnmZ/x3KOBsDCBrTAOBgNV\nHQ8BAf8EBAMCBeAwDAYDVR0TAQH/BAIwADAfBgNVHSMEGDAWgBSWhzrYiYGRQRUz\nv+A0jyCPwrvDljBNBgNVHREERjBEoEIGCSsGAQQBCRUCA6A1EzNDaGlwSUQ9Y1Rj\nU053a0FOVUUySUVRRUFBa0FBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQT0wHQYDVR0O\nBBYEFP3BUGkdbDrXOGVFoEDtl7EciB9zMAoGCCqGSM49BAMCA2kAMGYCMQC11eAd\nWA5CD7Y8s0B+9XeSytPGXRff2lOjfKBVMUF+8xOABeEjQIg+7HCNxpqSX60CMQCD\nR4AsHxwxB1Hw+FNYPl5FCmuT3oYoSAH1ybuTUUvzo1TWpHRyTaUT7GqLWYFXjh8=\n-----END CERTIFICATE-----\n",
                "CertificateFormat": "PEM"
            },
            "InventoryState": "OobInventoryReady",
            "ManagerMode": "IntersightManagedStandalone",
            "SignatureInfo": {
                "RequestID": "e07efcc14dd099778fcda3340b7630ba",
                "Signature": "MEUCIETg6P8YZ5uouBX7Xsh8UB0mz6MnNCgOlC0M5oFp+CB1AiEA03FbG7OELeCBRCtzmQUD\nLLgonQa/5pO/ZrBUeuU+ixA=\n",
                "SignatureStatus": "Completed"
            },
            "UserLabel": ""
        }
    }
}

/redfish/v1/Managers/CIMC/NetworkProtocol
-----------------------------------------
{
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.ResetKVM": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetKVM",
                "target": "/redfish/v1/Managers/CIMC/NetworkProtocol/Actions/Oem/CiscoUCSExtensions.ResetKVM"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "KVMConfiguration": {
                "LocalServerVideo": "Enabled",
                "MaxConcurrentSessions": 4
            },
            "KVMVendor": {
                "Vendor": "Cisco"
            }
        }
    }
}

/redfish/v1/Managers/UCSC-M-V100-04_FCH26147UVK
-----------------------------------------------
{
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.ExportTechSupport": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ExportTechSupport",
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
                "target": "/redfish/v1/Managers/UCSC-M-V100-04_FCH26147UVK/Actions/Oem/CiscoUCSExtensions.ExportTechSupport"
            }
        }
    }
}

/redfish/v1/Managers/UCSC-PCIE-C25Q-04_FCH26277TA5
--------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.ExportTechSupport": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ExportTechSupport",
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
                "target": "/redfish/v1/Managers/UCSC-PCIE-C25Q-04_FCH26277TA5/Actions/Oem/CiscoUCSExtensions.ExportTechSupport"
            }
        }
    }
}

/redfish/v1/Systems/WZP262207W0
-------------------------------
{
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.ResetBIOSCMOS": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetBIOSCMOS",
                "target": "/redfish/v1/Systems/WZP262207W0/Actions/Oem/ComputerSystem.ResetBIOSCMOS"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "FrontPanelButtonsLocked": false,
            "PostCompletionStatus": false,
            "SystemEffectiveMemory": 512,
            "SystemEffectiveSpeed": 3200
        }
    }
}

/redfish/v1/Systems/WZP262207W0/Storage/MRAID
---------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.BbuStartLearnCycle": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.BbuStartLearnCycle",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Actions/Oem/Cisco.BbuStartLearnCycle"
            },
            "#Cisco.ClearConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ClearConfig",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Actions/Oem/Cisco.ClearConfig"
            },
            "#Cisco.DoForeignConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.DoForeignConfig",
                "ForeignCfgOp@Redfish.AllowableValues": [
                    "Clear",
                    "Import"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Actions/Oem/Cisco.DoForeignConfig"
            },
            "#Cisco.EncryptionOp": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.EncryptionOp",
                "DriveEncryptionModeRemote@Redfish.AllowableValues": [
                    true,
                    false
                ],
                "EnOpName@Redfish.AllowableValues": [
                    "Enable",
                    "Disable",
                    "Migrate",
                    "Modify",
                    "Unlock"
                ],
                "EncryptionKey@Redfish.AllowableValues": [
                    "A unique string generated by requester, min is 1 and max is 32"
                ],
                "KeyId@Redfish.AllowableValues": [
                    "A unique string generated by requester, min is 1 and max is 255"
                ],
                "NewEncryptionKey@Redfish.AllowableValues": [
                    "A unique string generated by requester, min is 1 and max is 32"
                ],
                "Remote@Redfish.AllowableValues": [
                    true,
                    false
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Actions/Oem/Cisco.EncryptionOp"
            },
            "#Cisco.GetLogs": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.GetLogs",
                "OutputFile@Redfish.AllowableValues": [
                    "A string of length between 1-64 alpha numeric characters for output file name"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Actions/Oem/Cisco.GetLogs"
            },
            "#Cisco.ResetToFactoryDefaults": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetToFactoryDefaults",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Actions/Oem/Cisco.ResetToFactoryDefaults"
            },
            "#Cisco.UnpinCache": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UnpinCache",
                "DiscardType@Redfish.AllowableValues": [
                    "all",
                    "missing"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Actions/Oem/Cisco.UnpinCache"
            }
        }
    },
    "Links": {
        "Oem": {
            "Cisco": {
                "PCIeInfo": [
                    {
                        "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MRAID/PCIeFunctions/0"
                    }
                ]
            }
        }
    }
}

/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1
------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.Spindown": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spindown",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.Spindown"
            },
            "#Cisco.Spinup": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spinup",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.Spinup"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1918999986176,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "UnConfiguredGood",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1919846187008,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 70,
                "OperatingTemperatureInCel": 23,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 41,
                "PowerOnHours": 27,
                "PowerOnHoursPercentage": 0,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 1
        }
    }
}

/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2
------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.Spindown": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spindown",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.Spindown"
            },
            "#Cisco.Spinup": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spinup",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.Spinup"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1918999986176,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "UnConfiguredGood",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1919846187008,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 70,
                "OperatingTemperatureInCel": 23,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 41,
                "PowerOnHours": 27,
                "PowerOnHoursPercentage": 0,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 2
        }
    }
}

/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3
------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.Spindown": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spindown",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.Spindown"
            },
            "#Cisco.Spinup": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spinup",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.Spinup"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1918999986176,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "UnConfiguredGood",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1919846187008,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 70,
                "OperatingTemperatureInCel": 23,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 41,
                "PowerOnHours": 27,
                "PowerOnHoursPercentage": 0,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 3
        }
    }
}

/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4
------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.Spindown": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spindown",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.Spindown"
            },
            "#Cisco.Spinup": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.Spinup",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.Spinup"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1918999986176,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "UnConfiguredGood",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1919846187008,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 70,
                "OperatingTemperatureInCel": 23,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 41,
                "PowerOnHours": 27,
                "PowerOnHoursPercentage": 0,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 4
        }
    }
}

/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID
--------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.DoForeignConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.DoForeignConfig",
                "ForeignCfgOp@Redfish.AllowableValues": [
                    "Clear",
                    "Import"
                ],
                "target": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Actions/Oem/Cisco.DoForeignConfig"
            }
        }
    },
    "Links": {
        "Oem": {
            "Cisco": {
                "PCIeInfo": [
                    {
                        "@odata.id": "/redfish/v1/Systems/WZP262207W0/PCIeDevices/MSTOR-RAID/PCIeFunctions/0"
                    }
                ]
            }
        }
    }
}

/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Drives/253
-------------------------------------------------------------
{
    "Actions": {
        "Oem": {}
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 240056795136,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Jbod",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 240056795136,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 75,
                "OperatingTemperatureInCel": 42,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 20,
                "PowerOnHours": 62,
                "PowerOnHoursPercentage": 0,
                "ThresholdOperatingTemperatureInCel": 75,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 253
        }
    }
}

/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Drives/254
-------------------------------------------------------------
{
    "Actions": {
        "Oem": {}
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 240056795136,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Jbod",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 240056795136,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 75,
                "OperatingTemperatureInCel": 44,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 20,
                "PowerOnHours": 62,
                "PowerOnHoursPercentage": 0,
                "ThresholdOperatingTemperatureInCel": 75,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 254
        }
    }
}

/redfish/v1/UpdateService
-------------------------
{
    "Actions": {
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
    }
}
```