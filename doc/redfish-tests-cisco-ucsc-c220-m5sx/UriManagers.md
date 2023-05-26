# Resource: /redfish/v1/Managers

Vendor | Model
--- | ---
Cisco | UCSC-C220-M5SX

## /redfish/v1/Managers

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerCollection.ManagerCollection",
    "@odata.id": "/redfish/v1/Managers",
    "@odata.type": "#ManagerCollection.ManagerCollection",
    "Description": "Collection of Managers",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/CIMC"
        }
    ],
    "Members@odata.count": 1,
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
    "DateTime": "2022-11-29T10:14:35+01:00",
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
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU"
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
    "Model": "UCSC-C220-M5SX",
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
                "Certificate": "-----BEGIN CERTIFICATE-----\nMIICIzCCAamgAwIBAgIEAMO9DTAKBggqhkjOPQQDAjArMQ4wDAYDVQQKEwVDaXNj\nbzEZMBcGA1UEAxMQQUNUMiBFQ0MgU1VESSBDQTAgFw0xOTAyMjAwNTUyMzlaGA8y\nMDUzMDQwNDA4MTU0MlowdTEqMCgGA1UEBRMhUElEOlVDU0MtQzIyMC1NNVNYIFNO\nOldaUDIyNDkwWkNVMQ4wDAYDVQQKEwVDaXNjbzEYMBYGA1UECxMPQUNULTIgTGl0\nZSBTVURJMR0wGwYDVQQDExRVQ1MgTS1TZXJpZXMgU2VydmVyczBZMBMGByqGSM49\nAgEGCCqGSM49AwEHA0IABFaisKrrag7KGNhBYz4sw+7KnRAMLrqq/On+lLkeojOY\nucwMObvGq8KnlOmPHfrux3b4/TdteKsdBMNLjwFfgzGjbzBtMA4GA1UdDwEB/wQE\nAwIF4DAMBgNVHRMBAf8EAjAAME0GA1UdEQRGMESgQgYJKwYBBAEJFQIDoDUTM0No\naXBJRD1jRFp5T0JJTTZFRTJJRVFFQUFjQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB\nPTAKBggqhkjOPQQDAgNoADBlAjARaY1+mcM9GTY6mCD9as8cbfbmWhBPTezN/nGt\nXFFumlC68Ub3fvWRjngE6HBQ7V8CMQC0copEaEWfVD5kQiqUdtmK/PdJBYgRBbBF\nNCUTiyD4FSOWx/9Es1YrTgz3Z3od1RE=\n-----END CERTIFICATE-----\n",
                "CertificateFormat": "PEM"
            },
            "InventoryState": "OobInventoryReady",
            "SignatureInfo": {
                "RequestID": "70d3121a6b35d070255d6be59eaa5141",
                "Signature": "MEUCIQDkw48fRF+QvNgcfD43mUpksJFmnalhaaaXqyq4xrp16AIgf9XI0+ou3W6Ab+e6+Y34\nYkEwvLCO+5MWzyTe0tluzWE=\n",
                "SignatureStatus": "Completed"
            },
            "UserLabel": "aio-1-p1-eu-spdc"
        }
    },
    "RemoteAccountService": {
        "@odata.id": "/redfish/v1/AccountService"
    },
    "RemoteRedfishServiceUri": "/redfish/v1",
    "SerialInterfaces": {
        "@odata.id": "/redfish/v1/Managers/CIMC/SerialInterfaces"
    },
    "ServiceEntryPointUUID": "B16A1200-1CCF-42EA-8B33-6C4D50110704",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "UUID": "B16A1200-1CCF-42EA-8B33-6C4D50110704",
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
    "HostName": "aio-1-p1-eu-spdc-WZP22490ZCU",
    "IPv4Addresses": [
        {
            "Address": "10.58.28.41",
            "AddressOrigin": "Static",
            "Gateway": "10.58.28.62",
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
    "MACAddress": "70:EA:1A:59:C9:9C",
    "MTUSize": 1500,
    "MaxIPv6StaticAddresses": 1,
    "Name": "Manager Ethernet Interface",
    "NameServers": [
        "173.38.200.100",
        "144.254.71.184"
    ],
    "PermanentMACAddress": "70:EA:1A:59:C9:9C",
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
    "HostName": "aio-1-p1-eu-spdc-WZP22490ZCU",
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
            "10.58.228.2",
            "10.58.228.3"
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
    "CertificateString": "-----BEGIN CERTIFICATE-----\nMIIEDDCCAvSgAwIBAgIJAN7K7Vt5OYiKMA0GCSqGSIb3DQEBDQUAMIGZMQswCQYD\nVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTERMA8GA1UEBwwIU2FuIEpvc2Ux\nFjAUBgNVBAMMDUMtc2VyaWVzIENJTUMxGjAYBgNVBAoMEUNpc2NvIFNlbGYgU2ln\nbmVkMS4wLAYDVQQLDCVQSUQ6VUNTQy1DMjIwLU01U1ggU0VSSUFMOldaUDIyNDla\nMDlWMB4XDTE5MDIyMDA5NDQyOFoXDTI0MDIxOTA5NDQyOFowgZkxCzAJBgNVBAYT\nAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMREwDwYDVQQHDAhTYW4gSm9zZTEWMBQG\nA1UEAwwNQy1zZXJpZXMgQ0lNQzEaMBgGA1UECgwRQ2lzY28gU2VsZiBTaWduZWQx\nLjAsBgNVBAsMJVBJRDpVQ1NDLUMyMjAtTTVTWCBTRVJJQUw6V1pQMjI0OVowOVYw\nggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDBXP4AFHvTenNJfDD0CGe+\nHwjvPoYSJdsEcCPO6fLnHDvKrGNFMfG5wXzBByntVtNJ75bgJ2BjcUcphwUeX1p2\nuwmlOW/WXU//urYzWEow4q+PfltpfvQCyf+V0xPIC2ixYuyrnF8kUnhJ6Jzeoh17\nMv8wsDDNNUyvlAGtLdyd6AdVTYow5pMmfHeogS1rduWTle8XMHHU95jXsI/uvTXV\njpfXhFq/77iHR0KDy6G/tOaG9TckvDy0LCcoo4WQDm1gRK9wK/y7hIcwH+1CWL8r\nzYuDTsoOeEjOSCIJ9xrqnnGXP5pXRQeTJ91gEdoKCIQ7FKRKL+PQuHxyWxi0gj7P\nAgMBAAGjVTBTMB0GA1UdDgQWBBTiQ5IknLjo3qOGSfuX3krAsoxzmjAfBgNVHSME\nGDAWgBTiQ5IknLjo3qOGSfuX3krAsoxzmjARBglghkgBhvhCAQEEBAMCBkAwDQYJ\nKoZIhvcNAQENBQADggEBACJ54Wg5QwQipzC5JGhPdOyiaWnOFlwf4Z/pxzdb0cOw\nuSpZ0Idcy5bHCBPKsFnKwor/u6sO6URu3Slc1lkxu23jCTOcrqArMG3baKrZuAD4\nvzgYf9fCZPHWa6vnxnPEtfNOS1PL1d3N0ss0Tu1XNEeoNQ9YEZVq/jtL5GXvafSe\nvdSAL3lrqSNk/cS4Une2ftynAJhS0Ho7oPdEGUQvc+/jZW29sudDDtDkOofEvEJ7\n7TSh5yoYqWtXjwRQZZSWFVZXjaFLXxLTXGLRPi9OslG6RspOTa58hCYygM+y9Q0K\nZ50/sdyjPM2GpM22yKeMHg7pGiEiHjR8a5BdDJ0Q7zw=\n-----END CERTIFICATE-----\n",
    "CertificateType": "PEM",
    "Description": "The Certificate resource describes a certificate used to prove the identify of a component, account, or service.",
    "Id": "Certificate",
    "Issuer": {
        "City": " San Jose",
        "CommonName": " C-series CIMC",
        "Country": " US",
        "Organization": " Cisco Self Signed",
        "OrganizationalUnit": " PID:UCSC-C220-M5SX SERIAL:WZP2249Z09V",
        "State": " California"
    },
    "KeyUsage": [
        "ServerAuthentication"
    ],
    "Name": "Certificate",
    "Subject": {
        "City": " San Jose",
        "CommonName": " C-series CIMC",
        "Country": " US",
        "Organization": " Cisco Self Signed",
        "OrganizationalUnit": " PID:UCSC-C220-M5SX SERIAL:WZP2249Z09V",
        "State": " California"
    },
    "ValidNotAfter": "Feb 19 09:44:28 2024 GMT",
    "ValidNotBefore": "Feb 20 09:44:28 2019 GMT"
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

