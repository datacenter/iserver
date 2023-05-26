# Resource: /redfish/v1/Managers

Vendor | Model
--- | ---
Cisco | UCSC-C240-M5SN

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
            "@odata.id": "/redfish/v1/Managers/UCSC-MLOM-C25Q-04_FCH24157DE1"
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
    "DateTime": "2022-11-29T12:05:44+01:00",
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
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4"
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
    "Model": "UCSC-C240-M5SN",
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
                "Certificate": "-----BEGIN CERTIFICATE-----\nMIICIzCCAamgAwIBAgIEAQOqlTAKBggqhkjOPQQDAjArMQ4wDAYDVQQKEwVDaXNj\nbzEZMBcGA1UEAxMQQUNUMiBFQ0MgU1VESSBDQTAgFw0xOTEwMDcwNzE5MDBaGA8y\nMDUzMDQwNDA4MTU0MlowdTEqMCgGA1UEBRMhUElEOlVDU0MtQzI0MC1NNVNOIFNO\nOldaUDIzNDAwQUs0MQ4wDAYDVQQKEwVDaXNjbzEYMBYGA1UECxMPQUNULTIgTGl0\nZSBTVURJMR0wGwYDVQQDExRVQ1MgTS1TZXJpZXMgU2VydmVyczBZMBMGByqGSM49\nAgEGCCqGSM49AwEHA0IABHzcgTt0LbaZDPeLcyVKFJYSmIVY+O6flI2rWjI1Zjbv\nq+I5XNRAbCiwqeE8Bkryp1x1LWPi7JhZke5hgF54fSCjbzBtMA4GA1UdDwEB/wQE\nAwIF4DAMBgNVHRMBAf8EAjAAME0GA1UdEQRGMESgQgYJKwYBBAEJFQIDoDUTM0No\naXBJRD13REdDTUFNSzdrRTJJRVFFQUFNQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB\nPTAKBggqhkjOPQQDAgNoADBlAjEA7tOlnvFRuR3najGQIEs2XDSfmvQtFnZgbxPb\nvil9m+KpPmzM5sr+nuggXW2ueJbPAjAD9Ta4A+xMA0trGb4ooyrJooGUF4nS12xN\nEX1lOXiXINcOn1/yBAg3WnWR6hdkMQ0=\n-----END CERTIFICATE-----\n",
                "CertificateFormat": "PEM"
            },
            "InventoryState": "OobInventoryReady",
            "SignatureInfo": {
                "RequestID": "e0c2bfb298644827c926e80f96b2fc94",
                "Signature": "MEUCIFMlzqFOXz1ihcjaLv/Ja5Kx1Y/T6uYEmaoWbLufMJmNAiEAv0KpR61jZbenEL3X/Vu4\njnzWLvW+WWIRm8Y4Ny9Jm8A=\n",
                "SignatureStatus": "Completed"
            },
            "UserLabel": "comp-2-p2b-eu-spdc-WZP23400AK4"
        }
    },
    "RemoteAccountService": {
        "@odata.id": "/redfish/v1/AccountService"
    },
    "RemoteRedfishServiceUri": "/redfish/v1",
    "SerialInterfaces": {
        "@odata.id": "/redfish/v1/Managers/CIMC/SerialInterfaces"
    },
    "ServiceEntryPointUUID": "B813910F-BFD2-439F-9C3B-75B376C5B160",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "UUID": "B813910F-BFD2-439F-9C3B-75B376C5B160",
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
    "HostName": "comp-2-p2b-eu-spdc-WZP23400AK4",
    "IPv4Addresses": [
        {
            "Address": "10.58.50.42",
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
    "MACAddress": "5C:71:0D:26:2B:CC",
    "MTUSize": 1500,
    "MaxIPv6StaticAddresses": 1,
    "Name": "Manager Ethernet Interface",
    "NameServers": [
        "173.38.200.100",
        "144.254.71.184"
    ],
    "PermanentMACAddress": "5C:71:0D:26:2B:CC",
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
    "HostName": "comp-2-p2b-eu-spdc-WZP23400AK4",
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
                "AccessMode": "Full",
                "CommunityString": "cimcpublic"
            }
        ],
        "EnableSNMPv1": true,
        "EnableSNMPv2c": true,
        "EnableSNMPv3": true,
        "HideCommunityStrings": false,
        "Port": 161,
        "ProtocolEnabled": true
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
    "CertificateString": "-----BEGIN CERTIFICATE-----\nMIID3TCCAsWgAwIBAgIUQ8opXs+e1Wyt2lijTGK/BdImtKAwDQYJKoZIhvcNAQEN\nBQAwgYwxCzAJBgNVBAYTAlVTMQ0wCwYDVQQIDARudWxsMQ0wCwYDVQQHDARudWxs\nMQ0wCwYDVQQKDARudWxsMQ0wCwYDVQQLDARudWxsMScwJQYDVQQDDB5jb21wLTIt\ncDJiLWV1LXNwZGMtV1pQMjM0MDBBSzQxGDAWBgkqhkiG9w0BCQEWCW51bGxAbnVs\nbDAeFw0yMjExMjMxODQxMjhaFw0yNTAyMjUxODQxMjhaMIGMMQswCQYDVQQGEwJV\nUzENMAsGA1UECAwEbnVsbDENMAsGA1UEBwwEbnVsbDENMAsGA1UECgwEbnVsbDEN\nMAsGA1UECwwEbnVsbDEnMCUGA1UEAwweY29tcC0yLXAyYi1ldS1zcGRjLVdaUDIz\nNDAwQUs0MRgwFgYJKoZIhvcNAQkBFgludWxsQG51bGwwggEiMA0GCSqGSIb3DQEB\nAQUAA4IBDwAwggEKAoIBAQDsbnI/vPcdn4P6i4f/n1BAJqu1AGqaM27Io8pgb6a6\nh4LAOD0+/FjhZ+oYOzbqUoLm17qJkJ/XvhZbEpfKoO8dpDw6goZ7pva+IjsRCfiU\nLphI9oUJAxfWnXBwmQLd5v1T8bxgu/CsyRU2p9hwiz7C2vwvY68aRdY1/E31eBON\nRqZAV+8xFnXr+imnVdd3eoL8cDQl2admGvvr+psjJzesvplsESgiCs9DdDT6GkS4\nNxem/gnGDucpG3WaCy0cicZUl6esIcGImR+XP1bPbMnE6nw4YN25HCAro/pjwBRn\nw20nxmemPwlLm0I9Z0qAUWPHABikysDrrA27AR+CWlRRAgMBAAGjNTAzMAkGA1Ud\nEwQCMAAwEwYDVR0lBAwwCgYIKwYBBQUHAwEwEQYJYIZIAYb4QgEBBAQDAgZAMA0G\nCSqGSIb3DQEBDQUAA4IBAQCsls8ydxn7VbjDFX77GnP6ByvCBUgkg4pS4qnDGDOU\nvdYIWeCvbVUcByDjrumXua1ygzuQyHxCs2EcYo8sjD83j02g9I8tVFnD3jhecxkx\n8TYCaQ/IMjnrB6oYaCpcA3b0ofb+TAxzuOvUmDdAUU6QP76cuolpHJ0C/QZD7Rzs\nuLPPRaJI8lr/spwX78pTCnbVIA+c2w3wSG6PeLBI59VfeSGC4u+u1MtPmnnEcSja\n9Ha7Z2eydgJJTYeNEzrT8+0byyyYujIlnhz0NNpZKCZgbx6VFsWovvJwn2WCcyNC\nmmmDh3X2UlwUDwgvTmXizt//B5jzfRzBNBtW9b54Ff4W\n-----END CERTIFICATE-----\n",
    "CertificateType": "PEM",
    "Description": "The Certificate resource describes a certificate used to prove the identify of a component, account, or service.",
    "Id": "Certificate",
    "Issuer": {
        "City": " null",
        "CommonName": " comp-2-p2b-eu-spdc-WZP23400AK4",
        "Country": " US",
        "Organization": " null",
        "OrganizationalUnit": " null",
        "State": " null"
    },
    "KeyUsage": [
        "ServerAuthentication"
    ],
    "Name": "Certificate",
    "Subject": {
        "City": " null",
        "CommonName": " comp-2-p2b-eu-spdc-WZP23400AK4",
        "Country": " US",
        "Organization": " null",
        "OrganizationalUnit": " null",
        "State": " null"
    },
    "ValidNotAfter": "Feb 25 18:41:28 2025 GMT",
    "ValidNotBefore": "Nov 23 18:41:28 2022 GMT"
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
    "InterfaceEnabled": true,
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

## /redfish/v1/Managers/UCSC-MLOM-C25Q-04_FCH24157DE1

```{
    "@odata.context": "/redfish/v1/$metadata#Manager.Manager",
    "@odata.id": "/redfish/v1/Managers/UCSC-MLOM-C25Q-04_FCH24157DE1",
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
                "target": "/redfish/v1/Managers/UCSC-MLOM-C25Q-04_FCH24157DE1/Actions/Oem/CiscoUCSExtensions.ExportTechSupport"
            }
        }
    },
    "Description": "Cisco Integrated Management Controller",
    "Id": "UCSC-MLOM-C25Q-04_FCH24157DE1",
    "Name": "Cisco Integrated Management Controller"
}
```

