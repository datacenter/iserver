# Get Oem properties

Resources in Redfish can have optional Oem extensions with vendor specific extensions.

iserver makes it every easy to find Oem properties for single URI defined resource as well as searching recursively for all Oem properties.

## Get system oem properties

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --oem

/redfish/v1/Systems/WZP23400AK4
-------------------------------
{
    "Oem": {
        "Cisco": {
            "DimmBlacklistingEnabled": true,
            "SystemEffectiveMemory": 384,
            "SystemEffectiveSpeed": 2933,
            "PostCompletionStatus": true,
            "FrontPanelButtonsLocked": false
        }
    },
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.ResetBIOSCMOS": {
                "target": "/redfish/v1/Systems/WZP23400AK4/Actions/Oem/ComputerSystem.ResetBIOSCMOS",
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetBIOSCMOS"
            }
        }
    }
}
```

## Get all oem properties

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --oem
    --deep

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
            "StrongPasswordPolicyEnabled": false
        }
    }
}

/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1
-------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "BaseMac": "3C:57:31:CC:13:FE",
            "VicConfiguration": {
                "AzureQosEnabled": false,
                "ConfigurationPending": false,
                "FipEnabled": false,
                "LldpEnabled": false,
                "NivEnabled": false,
                "PhysicalNicModeEnabled": false,
                "PortChannelEnabled": true
            }
        }
    }
}

/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/eth0
-----------------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VnicConfiguration": {
                "EthConfiguration": {
                    "Cdn": "VIC-MLOM-eth0",
                    "CompQueueCount": 5,
                    "Features": {
                        "AdvancedFilterEnabled": false,
                        "ArfsEnabled": false,
                        "GeneveEnabled": false,
                        "GroupInterruptEnabled": false,
                        "MultiQueueEnabled": false,
                        "NvgreEnabled": false,
                        "Rocev2Enabled": false,
                        "VmqEnabled": false,
                        "VxlanEnabled": false
                    },
                    "InterruptProfile": {
                        "CoalescingTime": 125,
                        "CoalescingType": "Min",
                        "Count": 8
                    },
                    "OffloadProfile": {
                        "TcpLargeReceiveEnabled": true,
                        "TcpRxChecksumEnabled": true,
                        "TcpSegmentEnabled": true,
                        "TcpTxChecksumEnabled": true
                    },
                    "RecvQueue": {
                        "Count": 4,
                        "RingSize": 512
                    },
                    "RssProfile": {
                        "RssEnabled": true,
                        "RssIpv4HashEnabled": true,
                        "RssIpv6ExHashEnabled": false,
                        "RssIpv6HashEnabled": true,
                        "RssTcpIpv4HashEnabled": true,
                        "RssTcpIpv6ExHashEnabled": false,
                        "RssTcpIpv6HashEnabled": true,
                        "RssUdpIpv4HashEnabled": false,
                        "RssUdpIpv6HashEnabled": false
                    },
                    "StandByRecoveryDly": 5,
                    "StandByVif": {
                        "VifCookie": 0,
                        "VifId": 0
                    },
                    "TrustedClassOfServiceEnabled": false,
                    "WorkQueue": {
                        "Count": 1,
                        "RingSize": 256
                    }
                },
                "InterruptMode": "Any",
                "PCIOrder": "0.0",
                "UplinkPort": 0,
                "Vif": {
                    "VifCookie": 0,
                    "VifId": 0
                },
                "VlanMode": "Trunk"
            }
        }
    }
}

/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/eth1
-----------------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VnicConfiguration": {
                "EthConfiguration": {
                    "Cdn": "VIC-MLOM-eth1",
                    "CompQueueCount": 5,
                    "Features": {
                        "AdvancedFilterEnabled": false,
                        "ArfsEnabled": false,
                        "GeneveEnabled": false,
                        "GroupInterruptEnabled": false,
                        "MultiQueueEnabled": false,
                        "NvgreEnabled": false,
                        "Rocev2Enabled": false,
                        "VmqEnabled": false,
                        "VxlanEnabled": false
                    },
                    "InterruptProfile": {
                        "CoalescingTime": 125,
                        "CoalescingType": "Min",
                        "Count": 8
                    },
                    "OffloadProfile": {
                        "TcpLargeReceiveEnabled": true,
                        "TcpRxChecksumEnabled": true,
                        "TcpSegmentEnabled": true,
                        "TcpTxChecksumEnabled": true
                    },
                    "RecvQueue": {
                        "Count": 4,
                        "RingSize": 512
                    },
                    "RssProfile": {
                        "RssEnabled": true,
                        "RssIpv4HashEnabled": true,
                        "RssIpv6ExHashEnabled": false,
                        "RssIpv6HashEnabled": true,
                        "RssTcpIpv4HashEnabled": true,
                        "RssTcpIpv6ExHashEnabled": false,
                        "RssTcpIpv6HashEnabled": true,
                        "RssUdpIpv4HashEnabled": false,
                        "RssUdpIpv6HashEnabled": false
                    },
                    "StandByRecoveryDly": 5,
                    "StandByVif": {
                        "VifCookie": 0,
                        "VifId": 0
                    },
                    "TrustedClassOfServiceEnabled": false,
                    "WorkQueue": {
                        "Count": 1,
                        "RingSize": 256
                    }
                },
                "InterruptMode": "Any",
                "PCIOrder": "0.1",
                "UplinkPort": 1,
                "Vif": {
                    "VifCookie": 0,
                    "VifId": 0
                },
                "VlanMode": "Trunk"
            }
        }
    }
}

/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/fc0
----------------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VnicConfiguration": {
                "ClassOfService": 3,
                "InterruptMode": "Any",
                "PCIOrder": "0.2",
                "UplinkPort": 0,
                "VHBAConfiguration": {
                    "BootTable": [],
                    "CdbWorkQueue": {
                        "Count": 1,
                        "RingSize": 512
                    },
                    "ErrorRecoveryProfile": {
                        "ErrorDetectTimeout": 2000,
                        "FcpErrorRecoveryEnabled": false,
                        "IoTimeoutRetry": 5,
                        "LinkDownTimeout": 30000,
                        "PortDownIoRetryCount": 8,
                        "PortDownTimeout": 10000,
                        "ResourceAllocationTimeout": 10000
                    },
                    "FcPortProfile": {
                        "IoThrottleCount": 512,
                        "LunQueueDepth": 20,
                        "LunsPerTarget": 256
                    },
                    "FcRecvQueueRingSize": 64,
                    "FcWorkQueueRingSize": 64,
                    "MaxDataFieldSize": 2112,
                    "PersistentLunBindEnabled": false,
                    "PortFLogi": {
                        "RetryCount": -1,
                        "Timeout": 2000
                    },
                    "PortPLogi": {
                        "RetryCount": 8,
                        "Timeout": 2000
                    },
                    "VHBAType": [
                        "FcInitiator"
                    ]
                },
                "Vif": {
                    "VifCookie": 0,
                    "VifId": 0
                }
            }
        }
    }
}

/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/fc1
----------------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VnicConfiguration": {
                "ClassOfService": 3,
                "InterruptMode": "Any",
                "PCIOrder": "0.3",
                "UplinkPort": 1,
                "VHBAConfiguration": {
                    "BootTable": [],
                    "CdbWorkQueue": {
                        "Count": 1,
                        "RingSize": 512
                    },
                    "ErrorRecoveryProfile": {
                        "ErrorDetectTimeout": 2000,
                        "FcpErrorRecoveryEnabled": false,
                        "IoTimeoutRetry": 5,
                        "LinkDownTimeout": 30000,
                        "PortDownIoRetryCount": 8,
                        "PortDownTimeout": 10000,
                        "ResourceAllocationTimeout": 10000
                    },
                    "FcPortProfile": {
                        "IoThrottleCount": 512,
                        "LunQueueDepth": 20,
                        "LunsPerTarget": 256
                    },
                    "FcRecvQueueRingSize": 64,
                    "FcWorkQueueRingSize": 64,
                    "MaxDataFieldSize": 2112,
                    "PersistentLunBindEnabled": false,
                    "PortFLogi": {
                        "RetryCount": -1,
                        "Timeout": 2000
                    },
                    "PortPLogi": {
                        "RetryCount": 8,
                        "Timeout": 2000
                    },
                    "VHBAType": [
                        "FcInitiator"
                    ]
                },
                "Vif": {
                    "VifCookie": 0,
                    "VifId": 0
                }
            }
        }
    }
}

/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-1
---------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VicPort": {
                "AdminFecMode": "Off",
                "ConnectorPartNumber": "AFBR-7IER03Z-CS2",
                "ConnectorPartRevision": "01",
                "ConnectorPresent": true,
                "ConnectorType": "QSFP-4X10G-AOC3M",
                "ConnectorVendorName": "CISCO-AVAGO",
                "ConnectorVendorPid": "AVE2314300W-CH2",
                "OperFecMode": "Off"
            }
        }
    }
}

/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-2
---------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VicPort": {
                "AdminFecMode": "Off",
                "ConnectorPartNumber": "N/A",
                "ConnectorPartRevision": "N/A",
                "ConnectorPresent": false,
                "ConnectorType": "N/A",
                "ConnectorVendorName": "N/A",
                "ConnectorVendorPid": "N/A",
                "OperFecMode": "Off"
            }
        }
    }
}

/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-3
---------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VicPort": {
                "AdminFecMode": "Off",
                "ConnectorPartNumber": "AFBR-7IER03Z-CS2",
                "ConnectorPartRevision": "01",
                "ConnectorPresent": true,
                "ConnectorType": "QSFP-4X10G-AOC3M",
                "ConnectorVendorName": "CISCO-AVAGO",
                "ConnectorVendorPid": "AVE2432301M-CH2",
                "OperFecMode": "Off"
            }
        }
    }
}

/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-4
---------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VicPort": {
                "AdminFecMode": "Off",
                "ConnectorPartNumber": "N/A",
                "ConnectorPartRevision": "N/A",
                "ConnectorPresent": false,
                "ConnectorType": "N/A",
                "ConnectorVendorName": "N/A",
                "ConnectorVendorPid": "N/A",
                "OperFecMode": "Off"
            }
        }
    }
}

/redfish/v1/Fabrics/PCIeFabric/Switches/PCIe-Switch
---------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "ActiveFirmwareRevision": "1.8.0.58-24b3",
            "ComponentId": "8533",
            "LinkStatus": "Optimal",
            "P2PDeviceId": "efbe",
            "P2PVendorId": "f811",
            "ProductId": "PFX 48XG3",
            "ProductRevision": "RevB",
            "ShutdownTemperatureInCel": "105 degrees C",
            "SwitchTemperatureInCel": "47 degrees C"
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
                    "The directory path of the extracted HSU bundle."
                ],
                "Mode@Redfish.AllowableValues": [
                    "Discovery"
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
                    "VMEDIA-NFS"
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
            }
        }
    },
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
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
            "EncryptionStatus": false,
            "FanPolicy": "LowPower",
            "HardwareX509Identity": {
                "Certificate": "-----BEGIN CERTIFICATE-----\nMIICIzCCAamgAwIBAgIEAQOqlTAKBggqhkjOPQQDAjArMQ4wDAYDVQQKEwVDaXNj\nbzEZMBcGA1UEAxMQQUNUMiBFQ0MgU1VESSBDQTAgFw0xOTEwMDcwNzE5MDBaGA8y\nMDUzMDQwNDA4MTU0MlowdTEqMCgGA1UEBRMhUElEOlVDU0MtQzI0MC1NNVNOIFNO\nOldaUDIzNDAwQUs0MQ4wDAYDVQQKEwVDaXNjbzEYMBYGA1UECxMPQUNULTIgTGl0\nZSBTVURJMR0wGwYDVQQDExRVQ1MgTS1TZXJpZXMgU2VydmVyczBZMBMGByqGSM49\nAgEGCCqGSM49AwEHA0IABHzcgTt0LbaZDPeLcyVKFJYSmIVY+O6flI2rWjI1Zjbv\nq+I5XNRAbCiwqeE8Bkryp1x1LWPi7JhZke5hgF54fSCjbzBtMA4GA1UdDwEB/wQE\nAwIF4DAMBgNVHRMBAf8EAjAAME0GA1UdEQRGMESgQgYJKwYBBAEJFQIDoDUTM0No\naXBJRD13REdDTUFNSzdrRTJJRVFFQUFNQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB\nPTAKBggqhkjOPQQDAgNoADBlAjEA7tOlnvFRuR3najGQIEs2XDSfmvQtFnZgbxPb\nvil9m+KpPmzM5sr+nuggXW2ueJbPAjAD9Ta4A+xMA0trGb4ooyrJooGUF4nS12xN\nEX1lOXiXINcOn1/yBAg3WnWR6hdkMQ0=\n-----END CERTIFICATE-----\n",
                "CertificateFormat": "PEM"
            },
            "InventoryState": "OobInventoryReady",
            "SignatureInfo": {
                "RequestID": "e0c2bfb298644827c926e80f96b2fc94",
                "Signature": "MEUCIFMlzqFOXz1ihcjaLv/Ja5Kx1Y/T6uYEmaoWbLufMJmNAiEAv0KpR61jZbenEL3X/Vu4\njnzWLvW+WWIRm8Y4Ny9Jm8A=\n",
                "SignatureStatus": "Completed"
            },
            "UserLabel": "aio-2-p2b-eu-spdc-WZP23400AK4"
        }
    }
}

/redfish/v1/Managers/CIMC/NetworkProtocol
-----------------------------------------
{
    "Oem": {
        "Cisco": {
            "KVMConfiguration": {
                "LocalServerVideo": "Enabled",
                "MaxConcurrentSessions": 4,
                "VideoEncryption": "Enabled"
            }
        }
    }
}

/redfish/v1/Managers/UCSC-MLOM-C25Q-04_FCH24157DE1
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
                "target": "/redfish/v1/Managers/UCSC-MLOM-C25Q-04_FCH24157DE1/Actions/Oem/CiscoUCSExtensions.ExportTechSupport"
            }
        }
    }
}

/redfish/v1/SessionService/Sessions/533
---------------------------------------
{
    "Oem": {
        "Cisco": {
            "RemoteIP": "10.61.108.138",
            "SessionType": "redfish"
        }
    }
}

/redfish/v1/Systems/WZP23400AK4
-------------------------------
{
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.ResetBIOSCMOS": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetBIOSCMOS",
                "target": "/redfish/v1/Systems/WZP23400AK4/Actions/Oem/ComputerSystem.ResetBIOSCMOS"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "DimmBlacklistingEnabled": true,
            "FrontPanelButtonsLocked": false,
            "PostCompletionStatus": true,
            "SystemEffectiveMemory": 384,
            "SystemEffectiveSpeed": 2933
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID
---------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.BbuStartLearnCycle": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.BbuStartLearnCycle",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.BbuStartLearnCycle"
            },
            "#Cisco.ClearConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ClearConfig",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.ClearConfig"
            },
            "#Cisco.DoForeignConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.DoForeignConfig",
                "ForeignCfgOp@Redfish.AllowableValues": [
                    "Clear",
                    "Import"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.DoForeignConfig"
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
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.EncryptionOp"
            },
            "#Cisco.GetLogs": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.GetLogs",
                "OutputFile@Redfish.AllowableValues": [
                    "A string of length between 1-64 alpha numeric characters for output file name"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.GetLogs"
            },
            "#Cisco.ResetToFactoryDefaults": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetToFactoryDefaults",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.ResetToFactoryDefaults"
            },
            "#Cisco.UnpinCache": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UnpinCache",
                "DiscardType@Redfish.AllowableValues": [
                    "all",
                    "missing"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Actions/Oem/Cisco.UnpinCache"
            }
        }
    },
    "Links": {
        "Oem": {
            "Cisco": {
                "PCIeInfo": [
                    {
                        "@odata.id": "/redfish/v1/Systems/WZP23400AK4/PCIeFunctions/MRAID"
                    }
                ]
            }
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10
-------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 958999298048,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 959659900928,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "PercentLifeLeft": 99,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 98,
                "PowerOnHours": 15660,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1806
            },
            "StorageInstanceId": 10
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11
-------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 958999298048,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "UnConfiguredGood",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 959659900928,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 89,
                "PowerOnHours": 15645,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 11
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12
-------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 958999298048,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "UnConfiguredGood",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 959659900928,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 90,
                "PowerOnHours": 15645,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 12
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13
-------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 60
            },
            "StorageInstanceId": 13
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14
-------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 60
            },
            "StorageInstanceId": 14
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15
-------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 60
            },
            "StorageInstanceId": 15
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16
-------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 60
            },
            "StorageInstanceId": 16
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17
-------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 60
            },
            "StorageInstanceId": 17
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18
-------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.AddHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.AddHotSpare",
                "HotSpareType@Redfish.AllowableValues": [
                    "Global",
                    "Dedicated"
                ],
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 1198999470080,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 1199706210304,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "ThresholdOperatingTemperatureInCel": 60
            },
            "StorageInstanceId": 18
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9
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
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9/Actions/Oem/Cisco.AddHotspare"
            },
            "#Cisco.CancelDiag": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.CancelDiag",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9/Actions/Oem/Cisco.CancelDiag"
            },
            "#Cisco.PrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.PrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9/Actions/Oem/Cisco.PrepareForRemoval"
            },
            "#Cisco.RemoveHotspare": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.RemoveHotSpare",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9/Actions/Oem/Cisco.RemoveHotspare"
            },
            "#Cisco.StartDiagnostics": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartDiagnostics",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9/Actions/Oem/Cisco.StartDiagnostics"
            },
            "#Cisco.UndoPrepareForRemoval": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UndoPrepareForRemoval",
                "target": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9/Actions/Oem/Cisco.UndoPrepareForRemoval"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "Bootable": false,
            "CoercedSizeBytes": 958999298048,
            "DisabledForRemoval": false,
            "DrivePowerState": "Active",
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 959659900928,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "PercentLifeLeft": 99,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 100,
                "PowerOnHours": 15660,
                "ThresholdOperatingTemperatureInCel": 70,
                "WearStatusInDays": 1806
            },
            "StorageInstanceId": 9
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/0
-------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Cisco": {
                "Spans": [
                    {
                        "DrivesList": [
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10"
                            }
                        ],
                        "DrivesList@odata.count": 2,
                        "SpanId": 0
                    }
                ],
                "Spans@odata.count": 1
            }
        }
    },
    "Oem": {
        "Cisco": {
            "AvailableSizeMiBytes": 0,
            "Bootable": true,
            "ConfiguredWriteCachePolicy": "WriteThrough",
            "FullDiskEncryptionCapable": false,
            "RequestedWriteCachePolicy": "WriteThrough",
            "VolumeAccessPolicy": "ReadWrite",
            "VolumeDriveCachePolicy": "NoChange",
            "VolumeIoPolicy": "DirectIo",
            "VolumeReadAheadPolicy": "NoReadAhead",
            "VolumeState": "Optimal"
        }
    }
}

/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Volumes/1
-------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Cisco": {
                "Spans": [
                    {
                        "DrivesList": [
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/13"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/14"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/15"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/16"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/17"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/18"
                            }
                        ],
                        "DrivesList@odata.count": 6,
                        "SpanId": 0
                    }
                ],
                "Spans@odata.count": 1
            }
        }
    },
    "Oem": {
        "Cisco": {
            "AvailableSizeMiBytes": 0,
            "Bootable": false,
            "ConfiguredWriteCachePolicy": "WriteThrough",
            "FullDiskEncryptionCapable": false,
            "RequestedWriteCachePolicy": "WriteThrough",
            "VolumeAccessPolicy": "ReadWrite",
            "VolumeDriveCachePolicy": "NoChange",
            "VolumeIoPolicy": "DirectIo",
            "VolumeReadAheadPolicy": "NoReadAhead",
            "VolumeState": "Optimal"
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
                    "This object specifies details required to access OS Answer file. This object shall have properties ImageRepository, TransferProtocol, Username and Password."
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
                    "This parameter specifies the Storage URI to indicate the disk where OS is to be installed."
                ],
                "TargetOS@Redfish.AllowableValues": [
                    "This object specifies details of OS to be installed. This object shall have properties OSName and OSEdition."
                ],
                "TransferProtocol@Redfish.AllowableValues": [
                    "CIFS",
                    "HTTPS",
                    "NFS",
                    "VMEDIA-CIFS",
                    "VMEDIA-HTTPS",
                    "VMEDIA-NFS"
                ],
                "Username@Redfish.AllowableValues": [
                    "The username to be used while accessing shared location specified by the ImageRepository parameter."
                ],
                "target": "/redfish/v1/UpdateService/Actions/Oem/CiscoUCSExtensions.PrepareOSInstall"
            },
            "#CiscoUCSExtensions.UCSUpdate": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.UCSUpdate",
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
                    "The directory path of the extracted HSU bundle."
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
                    "VMEDIA-NFS"
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
