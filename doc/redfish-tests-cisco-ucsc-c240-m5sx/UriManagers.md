# Resource: /redfish/v1/Managers

Vendor | Model
--- | ---
Cisco | UCSC-C240-M5SX

## /redfish/v1/Managers

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerCollection.ManagerCollection",
    "@odata.id": "/redfish/v1/Managers",
    "@odata.type": "#ManagerCollection.ManagerCollection",
    "Description": "Collection of Managers",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/CIMC"
        },
        {
            "@odata.id": "/redfish/v1/Managers/UCSC-MLOM-C40Q-03_FCH23507ASW"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Manager Collection"
}
```

## /redfish/v1/Managers/CIMC

```{
    "@odata.context": "/redfish/v1/$metadata#Manager.Manager",
    "@odata.id": "/redfish/v1/Managers/CIMC",
    "@odata.type": "#Manager.v1_5_0.Manager",
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "ForceRestart"
            ],
            "target": "/redfish/v1/Managers/CIMC/Actions/Manager.Reset"
        },
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
    "AutoDSTEnabled": true,
    "CommandShell": {
        "ConnectTypesSupported": [
            "SSH",
            "IPMI",
            "Oem"
        ],
        "MaxConcurrentSessions": 4,
        "ServiceEnabled": true
    },
    "DateTime": "2022-11-27T18:04:28+01:00",
    "DateTimeLocalOffset": "+01:00",
    "Description": "Cisco Integrated Management Controller",
    "EthernetInterfaces": {
        "@odata.id": "/redfish/v1/Managers/CIMC/EthernetInterfaces"
    },
    "FirmwareVersion": "4.1(3d)",
    "GraphicalConsole": {
        "ConnectTypesSupported": [
            "KVMIP",
            "Oem"
        ],
        "MaxConcurrentSessions": 4,
        "ServiceEnabled": true
    },
    "Id": "CIMC",
    "Links": {
        "ManagerForChassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "ManagerForServers": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23450C8K"
            }
        ],
        "ManagerInChassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "LogServices": {
        "@odata.id": "/redfish/v1/Managers/CIMC/LogServices"
    },
    "ManagerType": "BMC",
    "Model": "UCSC-C240-M5SX",
    "Name": "Cisco Integrated Management Controller",
    "NetworkProtocol": {
        "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol"
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
                "Certificate": "-----BEGIN CERTIFICATE-----\nMIICIzCCAamgAwIBAgIEAQ4C2zAKBggqhkjOPQQDAjArMQ4wDAYDVQQKEwVDaXNj\nbzEZMBcGA1UEAxMQQUNUMiBFQ0MgU1VESSBDQTAgFw0xOTExMDcxNDI3NDdaGA8y\nMDUzMDQwNDA4MTU0MlowdTEqMCgGA1UEBRMhUElEOlVDU0MtQzI0MC1NNVNYIFNO\nOldaUDIzNDUwQzhLMQ4wDAYDVQQKEwVDaXNjbzEYMBYGA1UECxMPQUNULTIgTGl0\nZSBTVURJMR0wGwYDVQQDExRVQ1MgTS1TZXJpZXMgU2VydmVyczBZMBMGByqGSM49\nAgEGCCqGSM49AwEHA0IABHO//TG0oOwcVrjpY3WZBQjlDGFMPzxj2lFerrNYO7oj\n08wOeihUleNBSXhlG/YWPHiZ9wGv+Q02aQsm/Tu27sejbzBtMA4GA1UdDwEB/wQE\nAwIF4DAMBgNVHRMBAf8EAjAAME0GA1UdEQRGMESgQgYJKwYBBAEJFQIDoDUTM0No\naXBJRD1VRWlSTXhFVmVVRTJJRVFFQUFjQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB\nPTAKBggqhkjOPQQDAgNoADBlAjEA4WjMT/mqCD3ba3Shr2xEoLpBeT/8SSTBo+Qa\nQNlvplM+tCCIiLLoJ5020E++MWB8AjAA4CIQOjhGOvmRDuQjP+kjM92gleZu84BJ\nJRsZh7JId+1STjpFFbsKMX1eKcIooqk=\n-----END CERTIFICATE-----\n",
                "CertificateFormat": "PEM"
            },
            "InventoryState": "PartialInventoryReady",
            "SignatureInfo": {
                "RequestID": "3b9a5d9ae1ac45f14d29a351317428e8",
                "Signature": "MEUCIQDStMhxZmA7Amfy/J/VAWGcPKYuHXQoXhbNl+32aeGErgIgWRQZ0ZE1sfSfEKroFM4M\nEDCC7bO3em//ZwT1WvJWhOo=\n",
                "SignatureStatus": "Completed"
            },
            "UserLabel": "aio3-p5g-eu-spdc-WZP23450C8K"
        }
    },
    "RemoteAccountService": {
        "@odata.id": "/redfish/v1/AccountService"
    },
    "RemoteRedfishServiceUri": "/redfish/v1",
    "SerialInterfaces": {
        "@odata.id": "/redfish/v1/Managers/CIMC/SerialInterfaces"
    },
    "ServiceEntryPointUUID": "9A6D909E-F7C5-4481-BF21-424340DA652C",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "UUID": "9A6D909E-F7C5-4481-BF21-424340DA652C",
    "VirtualMedia": {
        "@odata.id": "/redfish/v1/Managers/CIMC/VirtualMedia"
    }
}
```

## /redfish/v1/Managers/CIMC/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "@odata.id": "/redfish/v1/Managers/CIMC/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Description": "Collection of EthernetInterfaces for this Manager",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/CIMC/EthernetInterfaces/NICs"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Ethernet Interfaces Collection"
}
```

## /redfish/v1/Managers/CIMC/EthernetInterfaces/NICs

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Managers/CIMC/EthernetInterfaces/NICs",
    "@odata.type": "#EthernetInterface.v1_4_1.EthernetInterface",
    "AutoNeg": true,
    "DHCPv4": {
        "DHCPEnabled": false,
        "UseDNSServers": false,
        "UseDomainName": false,
        "UseGateway": false,
        "UseNTPServers": false,
        "UseStaticRoutes": false
    },
    "DHCPv6": {
        "OperatingMode": "Disabled",
        "UseDNSServers": false,
        "UseDomainName": false,
        "UseNTPServers": false
    },
    "Description": "Manager Network Interface",
    "FullDuplex": false,
    "HostName": "aio3-p5g-eu-spdc-WZP23450C8K",
    "IPv4Addresses": [
        {
            "Address": "10.58.50.51",
            "AddressOrigin": "Static",
            "Gateway": "10.58.50.62",
            "SubnetMask": "255.255.255.224"
        }
    ],
    "IPv6Addresses": [
        {
            "Address": "::",
            "AddressOrigin": "Static",
            "PrefixLength": 64
        }
    ],
    "IPv6DefaultGateway": "::",
    "IPv6StaticDefaultGateways": [
        {
            "Address": "::"
        }
    ],
    "Id": "NICs",
    "InterfaceEnabled": true,
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "5C:71:0D:C6:91:50",
    "MTUSize": 1500,
    "MaxIPv6StaticAddresses": 1,
    "Name": "Manager Ethernet Interface",
    "NameServers": [
        "173.38.200.100",
        "144.254.71.184"
    ],
    "PermanentMACAddress": "5C:71:0D:C6:91:50",
    "StatelessAddressAutoConfig": {
        "IPv4AutoConfigEnabled": false,
        "IPv6AutoConfigEnabled": false
    },
    "StaticNameServers": [
        "173.38.200.100",
        "144.254.71.184"
    ],
    "VLAN": {
        "VLANEnable": false,
        "VLANId": 1
    }
}
```

## /redfish/v1/Managers/CIMC/LogServices

```
```

## /redfish/v1/Managers/CIMC/NetworkProtocol

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerNetworkProtocol.ManagerNetworkProtocol",
    "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol",
    "@odata.type": "#ManagerNetworkProtocol.v1_5_0.ManagerNetworkProtocol",
    "DHCP": {
        "Port": null,
        "ProtocolEnabled": false
    },
    "DHCPv6": {
        "Port": null,
        "ProtocolEnabled": false
    },
    "Description": "Manager Network Service",
    "HTTP": {
        "Port": 80,
        "ProtocolEnabled": true
    },
    "HTTPS": {
        "Certificates": {
            "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates"
        },
        "Port": 443,
        "ProtocolEnabled": true
    },
    "HostName": "aio3-p5g-eu-spdc-WZP23450C8K",
    "IPMI": {
        "Port": 623,
        "ProtocolEnabled": false
    },
    "Id": "ManagerNetworkProtocol",
    "KVMIP": {
        "Port": 2068,
        "ProtocolEnabled": true
    },
    "NTP": {
        "NTPServers": [
            "ntp.esl.cisco.com"
        ],
        "Port": 123,
        "ProtocolEnabled": true
    },
    "Name": "Manager Network Protocol",
    "Oem": {
        "Cisco": {
            "KVMConfiguration": {
                "LocalServerVideo": "Enabled",
                "MaxConcurrentSessions": 4,
                "VideoEncryption": "Enabled"
            }
        }
    },
    "SNMP": {
        "CommunityStrings": [
            {
                "AccessMode": null,
                "CommunityString": ""
            }
        ],
        "EnableSNMPv1": true,
        "EnableSNMPv2c": true,
        "EnableSNMPv3": true,
        "HideCommunityStrings": false,
        "Port": 161,
        "ProtocolEnabled": false
    },
    "SSH": {
        "Port": 22,
        "ProtocolEnabled": true
    },
    "VirtualMedia": {
        "Port": 2068,
        "ProtocolEnabled": true
    }
}
```

## /redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateCollection.CertificateCollection",
    "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates",
    "@odata.type": "#CertificateCollection.CertificateCollection",
    "Description": "A Collection of Certificate resource instances.",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Certificate Collection"
}
```

## /redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates/1

```{
    "@odata.context": "/redfish/v1/$metadata#Certificate.Certificate",
    "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates/1",
    "@odata.type": "#Certificate.v1_0_1.Certificate",
    "CertificateString": "-----BEGIN CERTIFICATE-----\nMIID+jCCAuKgAwIBAgIJAMQTu4D+J4d5MA0GCSqGSIb3DQEBDQUAMIGgMQswCQYD\nVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTERMA8GA1UEBwwIU2FuIEpvc2Ux\nGjAYBgNVBAoMEUNpc2NvIFNlbGYgU2lnbmVkMQwwCgYDVQQLDANQSUQxJTAjBgNV\nBAMMHGFpbzMtcDVnLWV1LXNwZGMtV1pQMjM0NTBDOEsxGDAWBgkqhkiG9w0BCQEW\nCW51bGxAbnVsbDAeFw0yMTA5MTcwOTM5MDRaFw0yNjA5MTYwOTM5MDRaMIGgMQsw\nCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTERMA8GA1UEBwwIU2FuIEpv\nc2UxGjAYBgNVBAoMEUNpc2NvIFNlbGYgU2lnbmVkMQwwCgYDVQQLDANQSUQxJTAj\nBgNVBAMMHGFpbzMtcDVnLWV1LXNwZGMtV1pQMjM0NTBDOEsxGDAWBgkqhkiG9w0B\nCQEWCW51bGxAbnVsbDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKpo\nfhR2WcRT1JQKifpHcTWB2b/i/mL1x+c7G4mEfVGGvDvcMoNeAwNGB2o4Z1HHmAr7\naGe3I3xtuyf/PXD/kBDcGZuw1HRQOnapqxFEcKTmy94ngKRMNhveyZJi3MaMIDoQ\nl3Xlj7UXrStuWzQpZXlUA024l86MosFa8H2uVQZsKI8+eDEXA0Gvg0Z6SSD0HqvJ\no0qgxODam1P9c9T1uxGhlHXRh1kRV4hs/rvCxqzLAoaoMm4TLVrZyuB/6j6Ty+KP\niInWCWVQYOHreVk5JkPuSGPCUR+rIulwOvZaIzIpAbqw9A0g0y0JNnHI08SQkpcV\nXGerU7/xtgdX64fpjWkCAwEAAaM1MDMwCQYDVR0TBAIwADATBgNVHSUEDDAKBggr\nBgEFBQcDATARBglghkgBhvhCAQEEBAMCBkAwDQYJKoZIhvcNAQENBQADggEBAEGr\nPiwWtgKAjyA4OqD9hSqoLHU2pNbP9TnccuuRws5qUkVnXBzKc/l11Nfscg7VQz5k\nuH0vc2w8k4qSuJXWdB3TMcaEoBU7iG0RWgSOcBRvd6E1xegyzqNF/ixNyH8NZ4N7\nXOvDPC61kYBS1Bj4c3zTktMJjQxwg9tE6sVv0j4v+XajsVPfOHWLk2eHsIBQ+IFu\nRAgQDiUk9aRjzGrsHtn510/hR7m/sv8igzpuAdH/XSMMow26V1iacxTzdoWELLBk\nz4sV7VK1bmCkPmXW0AZUEorA1EjE4kvslK3X7p3su8Nrbq0Es6KVw7L8EXy5MOJf\nFfY5RkpVcZpBCgGXDSM=\n-----END CERTIFICATE-----\n",
    "CertificateType": "PEM",
    "Description": "The Certificate resource describes a certificate used to prove the identify of a component, account, or service.",
    "Id": "Certificate",
    "Issuer": {
        "City": " San Jose",
        "CommonName": " aio3-p5g-eu-spdc-WZP23450C8K",
        "Country": " US",
        "Organization": " Cisco Self Signed",
        "OrganizationalUnit": " PID",
        "State": " California"
    },
    "KeyUsage": [
        "ServerAuthentication"
    ],
    "Name": "Certificate",
    "Subject": {
        "City": " San Jose",
        "CommonName": " aio3-p5g-eu-spdc-WZP23450C8K",
        "Country": " US",
        "Organization": " Cisco Self Signed",
        "OrganizationalUnit": " PID",
        "State": " California"
    },
    "ValidNotAfter": "Sep 16 09:39:04 2026 GMT",
    "ValidNotBefore": "Sep 17 09:39:04 2021 GMT"
}
```

## /redfish/v1/Managers/CIMC/Oem/Cisco/CiscoKMIPClient/Certificates

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateCollection.CertificateCollection",
    "@odata.id": "/redfish/v1/Managers/CIMC/Oem/Cisco/CiscoKMIPClient/Certificates",
    "@odata.type": "#CertificateCollection.CertificateCollection",
    "Description": "A Collection of Certificate resource instances.",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Certificate Collection"
}
```

## /redfish/v1/Managers/CIMC/Oem/Cisco/CiscoKMIPClient/Certificates/KMIPClient

```{
    "@odata.context": "/redfish/v1/$metadata#Certificate.Certificate",
    "@odata.id": "/redfish/v1/Managers/CIMC/Oem/Cisco/CiscoKMIPClient/Certificates/KMIPClient",
    "@odata.type": "#Certificate.v1_0_1.Certificate",
    "CertificateString": "",
    "Description": "The Certificate resource describes a certificate used to prove the identify of a component, account, or service.",
    "Id": "Certificate",
    "KeyUsage": [
        "ServerAuthentication"
    ],
    "Name": "Certificate"
}
```

## /redfish/v1/Managers/CIMC/Oem/Cisco/CiscoKMIPClient/Certificates/KMIPServer

```{
    "@odata.context": "/redfish/v1/$metadata#Certificate.Certificate",
    "@odata.id": "/redfish/v1/Managers/CIMC/Oem/Cisco/CiscoKMIPClient/Certificates/KMIPServer",
    "@odata.type": "#Certificate.v1_0_1.Certificate",
    "CertificateString": "",
    "Description": "The Certificate resource describes a certificate used to prove the identify of a component, account, or service.",
    "Id": "Certificate",
    "KeyUsage": [
        "ServerAuthentication"
    ],
    "Name": "Certificate"
}
```

## /redfish/v1/Managers/CIMC/SerialInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#SerialInterfaceCollection.SerialInterfaceCollection",
    "@odata.id": "/redfish/v1/Managers/CIMC/SerialInterfaces",
    "@odata.type": "#SerialInterfaceCollection.SerialInterfaceCollection",
    "Description": "Collection of Serial Interfaces for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/CIMC/SerialInterfaces/TTY0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Serial Interface Collection"
}
```

## /redfish/v1/Managers/CIMC/SerialInterfaces/TTY0

```{
    "@odata.context": "/redfish/v1/$metadata#SerialInterface.SerialInterface",
    "@odata.id": "/redfish/v1/Managers/CIMC/SerialInterfaces/TTY0",
    "@odata.type": "#SerialInterface.v1_1_3.SerialInterface",
    "BitRate": "115200",
    "ConnectorType": "DB9 Female",
    "DataBits": "8",
    "Description": "Management for Serial Interface",
    "FlowControl": "None",
    "Id": "TTY0",
    "InterfaceEnabled": false,
    "Name": "Manager Serial Interface 1",
    "Parity": "None",
    "PinOut": "Cisco",
    "SignalType": "Rs232",
    "StopBits": "1"
}
```

## /redfish/v1/Managers/CIMC/VirtualMedia

```{
    "@odata.context": "/redfish/v1/$metadata#VirtualMediaCollection.VirtualMediaCollection",
    "@odata.id": "/redfish/v1/Managers/CIMC/VirtualMedia",
    "@odata.type": "#VirtualMediaCollection.VirtualMediaCollection",
    "Description": "Redfish-BMC Virtual Media Service Settings",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/CIMC/VirtualMedia/1"
        },
        {
            "@odata.id": "/redfish/v1/Managers/CIMC/VirtualMedia/0"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Virtual Media Services"
}
```

## /redfish/v1/Managers/CIMC/VirtualMedia/0

```{
    "@odata.context": "/redfish/v1/$metadata#VirtualMedia.VirtualMedia",
    "@odata.id": "/redfish/v1/Managers/CIMC/VirtualMedia/0",
    "@odata.type": "#VirtualMedia.v1_3_0.VirtualMedia",
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
    },
    "ConnectedVia": "NotConnected",
    "Description": "Virtual Media Settings",
    "Id": "0",
    "Inserted": false,
    "MediaTypes": [
        "CD",
        "DVD"
    ],
    "Name": "Virtual CD",
    "WriteProtected": true
}
```

## /redfish/v1/Managers/CIMC/VirtualMedia/1

```{
    "@odata.context": "/redfish/v1/$metadata#VirtualMedia.VirtualMedia",
    "@odata.id": "/redfish/v1/Managers/CIMC/VirtualMedia/1",
    "@odata.type": "#VirtualMedia.v1_3_0.VirtualMedia",
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
    },
    "ConnectedVia": "NotConnected",
    "Description": "Virtual Media Settings",
    "Id": "1",
    "Inserted": false,
    "MediaTypes": [
        "Floppy",
        "USBStick"
    ],
    "Name": "Virtual HDD",
    "WriteProtected": true
}
```

## /redfish/v1/Managers/UCSC-MLOM-C40Q-03_FCH23507ASW

```{
    "@odata.context": "/redfish/v1/$metadata#Manager.Manager",
    "@odata.id": "/redfish/v1/Managers/UCSC-MLOM-C40Q-03_FCH23507ASW",
    "@odata.type": "#Manager.v1_5_0.Manager",
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
                "target": "/redfish/v1/Managers/UCSC-MLOM-C40Q-03_FCH23507ASW/Actions/Oem/CiscoUCSExtensions.ExportTechSupport"
            }
        }
    },
    "Description": "Cisco Integrated Management Controller",
    "Id": "UCSC-MLOM-C40Q-03_FCH23507ASW",
    "Name": "Cisco Integrated Management Controller"
}
```

