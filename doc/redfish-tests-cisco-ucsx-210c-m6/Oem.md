# Redfish Oem Resources

Vendor | Model
--- | ---
Cisco | UCSX-210C-M6

```
# iserver get redfish endpoint
    --cache ucsc-ucsx-210c-m6-fch25337ehm-5.0.1f-on
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Server
    --inventory-id FI4-1-1
    --oem
    --deep
    --max 0

/api-explorer/resources/redfish/v1/AccountService
-------------------------------------------------
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

/api-explorer/resources/redfish/v1/AccountService/Accounts/1
------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "IPMI": {
                "Password": null,
                "UID": 1
            }
        }
    }
}

/api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9
-------------------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "BaseMac": "D4:77:98:A8:D0:E8",
            "VicConfiguration": {
                "AzureQosEnabled": false,
                "ConfigurationPending": true
            }
        }
    }
}

/api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/esxi-trunk-1
-------------------------------------------------------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VnicConfiguration": {
                "ClassOfService": 0,
                "EthConfiguration": {
                    "Cdn": "esxi-trunk-1",
                    "CompQueueCount": 5,
                    "Features": {
                        "AdvancedFilterEnabled": false,
                        "ArfsEnabled": false,
                        "GeneveEnabled": false,
                        "GroupInterruptEnabled": false,
                        "MultiQueueEnabled": false,
                        "NvgreEnabled": false,
                        "Rocev2Enabled": false,
                        "UplinkFailOverEnabled": false,
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
                "UplinkPort": 1,
                "Vif": {
                    "VifCookie": 807,
                    "VifId": 807,
                    "VifState": "Error"
                },
                "VlanMode": "Trunk"
            }
        }
    }
}

/api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/esxi-trunk-2
-------------------------------------------------------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VnicConfiguration": {
                "ClassOfService": 0,
                "EthConfiguration": {
                    "Cdn": "esxi-trunk-2",
                    "CompQueueCount": 5,
                    "Features": {
                        "AdvancedFilterEnabled": false,
                        "ArfsEnabled": false,
                        "GeneveEnabled": false,
                        "GroupInterruptEnabled": false,
                        "MultiQueueEnabled": false,
                        "NvgreEnabled": false,
                        "Rocev2Enabled": false,
                        "UplinkFailOverEnabled": false,
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
                "UplinkPort": 0,
                "Vif": {
                    "VifCookie": 806,
                    "VifId": 806,
                    "VifState": "Error"
                },
                "VlanMode": "Trunk"
            }
        }
    }
}

/api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/fc0
----------------------------------------------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VnicConfiguration": {
                "ClassOfService": 3,
                "InterruptMode": "Any",
                "PCIOrder": "0.2",
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
                        "PortDownIoRetryCount": 30,
                        "PortDownTimeout": 10000,
                        "ResourceAllocationTimeout": 10000
                    },
                    "FcPortProfile": {
                        "IoThrottleCount": 256,
                        "LunQueueDepth": 20,
                        "LunsPerTarget": 1024
                    },
                    "FcRecvQueueRingSize": 64,
                    "FcWorkQueueRingSize": 64,
                    "MaxDataFieldSize": 2112,
                    "PersistentLunBindEnabled": false,
                    "PortFLogi": {
                        "RetryCount": 8,
                        "Timeout": 4000
                    },
                    "PortPLogi": {
                        "RetryCount": 8,
                        "Timeout": 20000
                    },
                    "VHBAType": [
                        "FcInitiator"
                    ]
                },
                "Vif": {
                    "VifCookie": 814,
                    "VifId": 814,
                    "VifState": "Down"
                }
            }
        }
    }
}

/api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/fc1
----------------------------------------------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VnicConfiguration": {
                "ClassOfService": 3,
                "InterruptMode": "Any",
                "PCIOrder": "0.3",
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
                        "PortDownIoRetryCount": 30,
                        "PortDownTimeout": 10000,
                        "ResourceAllocationTimeout": 10000
                    },
                    "FcPortProfile": {
                        "IoThrottleCount": 256,
                        "LunQueueDepth": 20,
                        "LunsPerTarget": 1024
                    },
                    "FcRecvQueueRingSize": 64,
                    "FcWorkQueueRingSize": 64,
                    "MaxDataFieldSize": 2112,
                    "PersistentLunBindEnabled": false,
                    "PortFLogi": {
                        "RetryCount": 8,
                        "Timeout": 4000
                    },
                    "PortPLogi": {
                        "RetryCount": 8,
                        "Timeout": 20000
                    },
                    "VHBAType": [
                        "FcInitiator"
                    ]
                },
                "Vif": {
                    "VifCookie": 815,
                    "VifId": 815,
                    "VifState": "Up"
                }
            }
        }
    }
}

/api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-1
---------------------------------------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VicPort": {
                "AdminLinkSpeed": "Auto"
            }
        }
    }
}

/api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-2
---------------------------------------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VicPort": {
                "AdminLinkSpeed": "Auto"
            }
        }
    }
}

/api-explorer/resources/redfish/v1/Managers/CIMC
------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.ExportTechSupport": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ExportTechSupport",
                "Protocol@Redfish.AllowableValues": [
                    "DeviceConnector",
                    "TFTP"
                ],
                "RemoteFilename@Redfish.AllowableValues": [
                    "The name of the exported tech support file"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "The remote location to where the tech support file needs to be exported"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "The directory path to where the tech support file needs to be exported"
                ],
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.ExportTechSupport"
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
                    "VMEDIA-CIFS",
                    "VMEDIA-NFS",
                    "VMEDIA-HTTPS",
                    "LOCAL-HOST"
                ],
                "Username@Redfish.AllowableValues": [
                    "The username to be used when accessing the URI specified by the ImageRepository parameter."
                ],
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.HostOSBootManagement"
            },
            "#CiscoUCSExtensions.ResetToFactoryDefaults": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetToFactoryDefaults",
                "target": "/redfish/v1/Managers/CIMC/Actions/Oem/CiscoUCSExtensions.ResetToFactoryDefaults"
            },
            "#CiscoUCSExtensions.SigningRequest": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.SigningRequest",
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
    "Links": {
        "Oem": {
            "Cisco": {
                "SPDMTrustStoreCertificateCollection": {
                    "@odata.id": "/redfish/v1/Managers/CIMC/Oem/Cisco/SPDMTrustStore/Certificates"
                }
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
            "CoreFilesTransferSettings": {
                "Enabled": false,
                "Path": null,
                "Port": null,
                "Prefix": null,
                "Protocol": null
            },
            "EnableLowPowerUsb": true,
            "EncryptionStatus": true,
            "HardwareX509Identity": {
                "Certificate": "-----BEGIN CERTIFICATE-----\nMIICaDCCAe+gAwIBAgIKBySHURRIEzKRtTAKBggqhkjOPQQDAjArMQ4wDAYDVQQK\nEwVDaXNjbzEZMBcGA1UEAxMQQUNUMiBFQ0MgU1VESSBDQTAgFw0yMTA4MjcxOTM2\nMDRaGA8yMDUzMDQwNDA4MTU0MlowczEoMCYGA1UEBRMfUElEOlVDU1gtMjEwQy1N\nNiBTTjpGQ0gyNTMzN0VITTEOMAwGA1UEChMFQ2lzY28xGDAWBgNVBAsTD0FDVC0y\nIExpdGUgU1VESTEdMBsGA1UEAxMUVUNTIEItU2VyaWVzIFNlcnZlcnMwWTATBgcq\nhkjOPQIBBggqhkjOPQMBBwNCAASU8QCrzd1IYNblRmMsIOHaA81PrhvIQD+9UwpX\n7vlpbZM7csNnMSZqPNMmKlYrTAMjISp2FozV+77J98mscfnlo4GwMIGtMA4GA1Ud\nDwEB/wQEAwIF4DAMBgNVHRMBAf8EAjAAMB8GA1UdIwQYMBaAFJaHOtiJgZFBFTO/\n4DSPII/Cu8OWME0GA1UdEQRGMESgQgYJKwYBBAEJFQIDoDUTM0NoaXBJRD1VWUpU\nTVZSUUJBUkNWR2gxSUUxaGNpQXlOU0F4TlRvME1EbzFNU0FOeGNNPTAdBgNVHQ4E\nFgQUXigBnXlQ90iOidWlw0OqTtrGuikwCgYIKoZIzj0EAwIDZwAwZAIwLUfLodAX\n2NMcfViJNk4DxKs86titKhQ52kkCNz1R6+/ko16ttJRwgnsOvjqCG0PBAjAQYgxA\nXXC/cVr8oGKrs66eM/JAnE0UbEjoYKE5batBF/AK49SnckingHzwRSSymS4=\n-----END CERTIFICATE-----\n",
                "CertificateFormat": "PEM"
            },
            "InventoryState": "PartialInventoryReady",
            "SignatureInfo": {
                "RequestID": "bd4d2b98d51b7b36b24295e3a7982628",
                "Signature": "MEUCIQDvIrUdTLQ7jliM/D8utXir0kYuEi2Xwie9gqsEr9azKQIgRzXqlkz6t6oBzsM8A8JS\ne52UDSPYjG+49Pb1KkKMTwI=\n",
                "SignatureStatus": "Completed"
            },
            "UserLabel": null
        }
    }
}

/api-explorer/resources/redfish/v1/Managers/CIMC/LogServices/CIMC
-----------------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.TestRemoteSyslogCfg": {
                "target": "/redfish/v1/Managers/CIMC/LogServices/CIMC/Actions/Oem/CiscoUCSExtensions.TestRemoteSyslogCfg"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "MinimumSeverityLevel": "Warning",
            "SyslogConnectionInfo": [
                {
                    "DestinationServer": "0.0.0.0",
                    "Enabled": false,
                    "Port": 514,
                    "Protocol": "UDP"
                },
                {
                    "DestinationServer": "0.0.0.0",
                    "Enabled": false,
                    "Port": 514,
                    "Protocol": "UDP"
                }
            ]
        }
    }
}

/api-explorer/resources/redfish/v1/Managers/CIMC/NetworkProtocol
----------------------------------------------------------------
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
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
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

/api-explorer/resources/redfish/v1/Managers/CIMC/Oem/Cisco/SPDMTrustStore/Certificates/1
----------------------------------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "CertificateSerialNumber": "0A:62:A4:1D:B6:03:0D:94:36:00:1C:CE:7B:37:3E:93:90:9C:24:36"
        }
    }
}

/api-explorer/resources/redfish/v1/Managers/CIMC/VirtualMedia/0
---------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "ImageNameVariable": null,
            "RemapOnEject": null
        }
    }
}

/api-explorer/resources/redfish/v1/Managers/CIMC/VirtualMedia/1
---------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "ImageNameVariable": null,
            "RemapOnEject": null
        }
    }
}

/api-explorer/resources/redfish/v1/Managers/CIMC/VirtualMedia/2
---------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "ImageNameVariable": null,
            "RemapOnEject": null
        }
    }
}

/api-explorer/resources/redfish/v1/Managers/CIMC/VirtualMedia/3
---------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "ImageNameVariable": "VMware-ESXi-6.7.0-17700523-Custom-Cisco-6.7.3.1.iso",
            "RemapOnEject": null
        }
    }
}

/api-explorer/resources/redfish/v1/Managers/CIMC/VirtualMedia/4
---------------------------------------------------------------
{
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "ImageNameVariable": null,
            "RemapOnEject": null
        }
    }
}

/api-explorer/resources/redfish/v1/Systems/FCH25337EHM
------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.ResetBIOSCMOS": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetBIOSCMOS",
                "target": "/redfish/v1/Systems/FCH25337EHM/Actions/Oem/ComputerSystem.ResetBIOSCMOS"
            },
            "#CiscoUCSExtensions.TPMClear": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.TPMClear",
                "target": "/redfish/v1/Systems/FCH25337EHM/Actions/Oem/ComputerSystem.TPMClear"
            }
        }
    },
    "Links": {
        "Oem": {
            "Cisco": {
                "SPDMDeviceCertificates": {
                    "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Oem/Cisco/SPDMDevice/Certificates"
                },
                "SPDMTrustStoreCertificateCollection": {
                    "@odata.id": "/redfish/v1/Managers/CIMC/Oem/Cisco/SPDMTrustStore/Certificates"
                }
            }
        }
    },
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "DimmBlacklistingEnabled": true,
            "FrontPanelButtonsLocked": true,
            "MCTP": {
                "FaultAlertSetting": "Partial",
                "SPDMHandShakeStatus": "Completed"
            },
            "PostCompletionStatus": true,
            "PowerProfilingEnabled": true,
            "SystemEffectiveMemory": 128,
            "SystemEffectiveSpeed": 3200
        }
    }
}

/api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID
-------------------------------------------------------------------------
{
    "Actions": {
        "Oem": {
            "#Cisco.DoForeignConfig": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.DoForeignConfig",
                "ForeignCfgOp@Redfish.AllowableValues": [
                    "Clear",
                    "Import"
                ],
                "target": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Actions/Oem/Cisco.DoForeignConfig"
            }
        }
    },
    "Links": {
        "Oem": {
            "Cisco": {
                "PCIeInfo": [
                    {
                        "@odata.id": "/redfish/v1/Systems/FCH25337EHM/PCIeDevices/MSTOR-RAID/PCIeFunctions/0"
                    }
                ]
            }
        }
    }
}

/api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/253
------------------------------------------------------------------------------------
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
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 240056795136,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 68,
                "OperatingTemperatureInCel": 38,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 25,
                "PowerOnHours": 3734,
                "ThresholdOperatingTemperatureInCel": 75,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 253
        }
    }
}

/api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/254
------------------------------------------------------------------------------------
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
            "DriveState": "Online",
            "MediaErrorCount": 0,
            "NonCoercedSizeBytes": 240056795136,
            "PredictiveFailureCount": 0,
            "SmartData": {
                "MaximumOperatingTemperatureInCel": 68,
                "OperatingTemperatureInCel": 37,
                "PercentLifeLeft": 100,
                "PercentReservedCapacityConsumed": 0,
                "PowerCycleCount": 25,
                "PowerOnHours": 3734,
                "ThresholdOperatingTemperatureInCel": 75,
                "WearStatusInDays": 1825
            },
            "StorageInstanceId": 254
        }
    }
}

/api-explorer/resources/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Volumes/0
-----------------------------------------------------------------------------------
{
    "Links": {
        "Oem": {
            "Cisco": {
                "Spans": [
                    {
                        "DrivesList": [
                            {
                                "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/253"
                            },
                            {
                                "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/254"
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

/api-explorer/resources/redfish/v1/UpdateService
------------------------------------------------
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
                    "VMEDIA-NFS",
                    "LOCAL-HOST"
                ],
                "Username@Redfish.AllowableValues": [
                    "The username to be used while accessing shared location specified by the ImageRepository parameter."
                ],
                "target": "/redfish/v1/UpdateService/Actions/Oem/CiscoUCSExtensions.PrepareOSInstall"
            },
            "#CiscoUCSExtensions.SetStartImageVersion": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.SetStartImageVersion",
                "ImageVersion@Redfish.AllowableValues": [
                    "Image Version"
                ],
                "Target@Redfish.AllowableValues": [
                    "/redfish/v1/UpdateService/FirmwareInventory/CIMC"
                ],
                "target": "/redfish/v1/UpdateService/Actions/Oem/CiscoUpdateService.SetStartImageVersion"
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
                    "VMEDIA-CIFS",
                    "VMEDIA-NFS",
                    "VMEDIA-HTTPS",
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