# Resource: /redfish/v1/Managers

Vendor | Model
--- | ---
Cisco | UCSC-C225-M6S

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
            "@odata.id": "/redfish/v1/Managers/UCSC-PCIE-C25Q-04_FCH26277TA5"
        },
        {
            "@odata.id": "/redfish/v1/Managers/UCSC-M-V100-04_FCH26147UVK"
        }
    ],
    "Members@odata.count": 3,
    "Name": "Manager Collection"
}
```

## /redfish/v1/Managers/CIMC

```{
    "@Redfish.Settings": {
        "@odata.type": "#Settings.v1_3_0.Settings",
        "Messages": [
            {
                "Message": "In order to apply the configured 'FanPolicy', host needs to be powered on. Current fan policy status: PENDING - Host powered off",
                "MessageId": "Base.1.4.GeneralError",
                "Resolution": "Power on the host and wait for POST complete",
                "Severity": "Warning"
            }
        ]
    },
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
    "DateTime": "2022-11-29T12:40:09+00:00",
    "DateTimeLocalOffset": "+00:00",
    "Description": "Cisco Integrated Management Controller",
    "EthernetInterfaces": {
        "@odata.id": "/redfish/v1/Managers/CIMC/EthernetInterfaces"
    },
    "FirmwareVersion": "4.2(2a)",
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
                "@odata.id": "/redfish/v1/Systems/WZP262207W0"
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
    "Model": "UCSC-C225-M6S",
    "Name": "Cisco Integrated Management Controller",
    "NetworkProtocol": {
        "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol"
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
    },
    "RemoteAccountService": {
        "@odata.id": "/redfish/v1/AccountService"
    },
    "RemoteRedfishServiceUri": "/redfish/v1",
    "SerialInterfaces": {
        "@odata.id": "/redfish/v1/Managers/CIMC/SerialInterfaces"
    },
    "ServiceEntryPointUUID": "3FC6BE04-7B3E-4240-A269-D87F44A1F7DD",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "UUID": "3FC6BE04-7B3E-4240-A269-D87F44A1F7DD",
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
        "OperatingMode": "Stateful",
        "UseDNSServers": true,
        "UseDomainName": false,
        "UseNTPServers": false
    },
    "Description": "Manager Network Interface",
    "FullDuplex": true,
    "HostName": "C225-WZP262207W0",
    "IPv4Addresses": [
        {
            "Address": "10.90.90.133",
            "AddressOrigin": "Static",
            "Gateway": "10.90.90.1",
            "SubnetMask": "255.255.255.0"
        }
    ],
    "IPv6Addresses": [
        {
            "Address": "::",
            "AddressOrigin": "DHCPv6",
            "PrefixLength": 64
        }
    ],
    "IPv6DefaultGateway": "::",
    "Id": "NICs",
    "InterfaceEnabled": true,
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    },
    "MACAddress": "EC:F4:0C:1B:26:D8",
    "MTUSize": 1500,
    "MaxIPv6StaticAddresses": 1,
    "Name": "Manager Ethernet Interface",
    "NameServers": [
        "10.90.89.19"
    ],
    "PermanentMACAddress": "EC:F4:0C:1B:26:D8",
    "SpeedMbps": 1024,
    "StatelessAddressAutoConfig": {
        "IPv4AutoConfigEnabled": false,
        "IPv6AutoConfigEnabled": true
    },
    "StaticNameServers": [
        "10.90.89.19"
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
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.ResetKVM": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetKVM",
                "target": "/redfish/v1/Managers/CIMC/NetworkProtocol/Actions/Oem/CiscoUCSExtensions.ResetKVM"
            }
        }
    },
    "DHCP": {
        "Port": null,
        "ProtocolEnabled": false
    },
    "DHCPv6": {
        "Port": null,
        "ProtocolEnabled": true
    },
    "Description": "Manager Network Service",
    "HTTP": {
        "Port": 80,
        "ProtocolEnabled": false
    },
    "HTTPS": {
        "Certificates": {
            "@odata.id": "/redfish/v1/Managers/CIMC/NetworkProtocol/HTTPS/Certificates"
        },
        "Port": 443,
        "ProtocolEnabled": true
    },
    "HostName": "C225-WZP262207W0",
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
        "NTPServers": [],
        "Port": 123,
        "ProtocolEnabled": false
    },
    "Name": "Manager Network Protocol",
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
    },
    "SNMP": {
        "CommunityStrings": [
            {
                "AccessMode": null,
                "CommunityString": ""
            }
        ],
        "EnableSNMPv1": false,
        "EnableSNMPv2c": false,
        "EnableSNMPv3": false,
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
    "@odata.type": "#Certificate.v1_3_0.Certificate",
    "CertificateString": "-----BEGIN CERTIFICATE-----\nMIIEJjCCAw6gAwIBAgIUd6379y3ca8DEjG3xsQ7D2WjPHbcwDQYJKoZIhvcNAQEN\nBQAwgZgxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMREwDwYDVQQH\nDAhTYW4gSm9zZTEWMBQGA1UEAwwNQy1zZXJpZXMgQ0lNQzEaMBgGA1UECgwRQ2lz\nY28gU2VsZiBTaWduZWQxLTArBgNVBAsMJFBJRDpVQ1NDLUMyMjUtTTZTIFNFUklB\nTDpXWlAyNjIwWjEzRzAeFw0yMjA5MDgxOTU2MDdaFw0yNDEyMTExOTU2MDdaMIGY\nMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTERMA8GA1UEBwwIU2Fu\nIEpvc2UxFjAUBgNVBAMMDUMtc2VyaWVzIENJTUMxGjAYBgNVBAoMEUNpc2NvIFNl\nbGYgU2lnbmVkMS0wKwYDVQQLDCRQSUQ6VUNTQy1DMjI1LU02UyBTRVJJQUw6V1pQ\nMjYyMFoxM0cwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDZBe37ddKA\nSe+IGKkd5JwCu5x5hzsrdIoTalkyg5aUu8QkJYQXfLVtUNlRNkRp+Ux/VbhaAsL5\niLD+daA4W8VV4h70Y6JOIw6dBpLevHh960+/zO0DMdI0sdV8MFa40O/o4ckk8Wur\nUxJTUegbvV6Ki21JknlBVlp8fJqmT+se6GmuI+kQR5bXFqvpgueFgwBnHjCU5JIt\ntsuTZ2795yw1bvcIF9kzDW2XgdrAexsLlykpudY9pO1FUJ2PueoymgUae0aIUiFz\n3A8hTGGOMwcjza1tlQ865P9sAqJxOFZUJUQRxTbsn7a4SeRuUjqnpibozXZmDBP1\nSuk6tJfvD41tAgMBAAGjZjBkMB0GA1UdDgQWBBSu0qjhLonKJuU4D7BilZ3Dc32b\nljAfBgNVHSMEGDAWgBSu0qjhLonKJuU4D7BilZ3Dc32bljAPBgNVHRMBAf8EBTAD\nAQH/MBEGCWCGSAGG+EIBAQQEAwIGQDANBgkqhkiG9w0BAQ0FAAOCAQEAmZpOSq3g\n5ubGSS5p0HJfPsRIilihBgJiYjVwP3HFNaTtI+b7upkX8SPZqz2Drmpflw40vTFB\n4KauvYnQTD8Ua5jMbcJKddhN0fEwyL8uj1MI95EA0PRuw3S+waBLKiRZckYisZb+\nQHrNoV9JRdrvA87ToxeDIEVe/5E7Na1CjKZYNieWlahWMERyRgsBtBoxMcllgP3K\nR3CRn3w0fj/Cn1qlM/DNfCUxMkK01aCaTG+r4lZMlJCe9Jgq/DA7NF+vXmNh26uD\n6r6IAIdYar9ktfWgy5QstyeMaGTbXRvHmINKJbSwXAaW9zKQYEVpevLdE3h9eX8O\nHXb1O0T4DgV5KA==\n-----END CERTIFICATE-----\n",
    "CertificateType": "PEM",
    "Description": "The Certificate resource describes a certificate used to prove the identify of a component, account, or service.",
    "Id": "Certificate",
    "Issuer": {
        "City": "San Jose",
        "CommonName": "C-series CIMC",
        "Country": "US",
        "Organization": "Cisco Self Signed",
        "OrganizationalUnit": "PID:UCSC-C225-M6S SERIAL:WZP2620Z13G",
        "State": "California"
    },
    "KeyUsage": [
        "ServerAuthentication"
    ],
    "Name": "Certificate",
    "SerialNumber": "77:AD:FB:F7:2D:DC:6B:C0:C4:8C:6D:F1:B1:0E:C3:D9:68:CF:1D:B7",
    "Subject": {
        "City": "San Jose",
        "CommonName": "C-series CIMC",
        "Country": "US",
        "Organization": "Cisco Self Signed",
        "OrganizationalUnit": "PID:UCSC-C225-M6S SERIAL:WZP2620Z13G",
        "State": "California"
    },
    "ValidNotAfter": "2024-12-11T19:56:07Z",
    "ValidNotBefore": "2022-09-08T19:56:07Z"
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
    "@odata.type": "#Certificate.v1_3_0.Certificate",
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
    "@odata.type": "#Certificate.v1_3_0.Certificate",
    "CertificateString": "",
    "Description": "The Certificate resource describes a certificate used to prove the identify of a component, account, or service.",
    "Id": "Certificate",
    "KeyUsage": [
        "ServerAuthentication"
    ],
    "Name": "Certificate"
}
```

## /redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage

```{
    "@odata.context": "/redfish/v1/$metadata#CiscoInternalStorageCollection.CiscoInternalStorageCollection",
    "@odata.id": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage",
    "@odata.type": "#CiscoInternalStorageCollection.CiscoInternalStorageCollection",
    "Description": "Collection of Cisco Internal Storge resources",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Cisco Internal Storage Collections"
}
```

## /redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC

```{
    "@odata.context": "/redfish/v1/$metadata#CiscoInternalStorage.CiscoInternalStorage",
    "@odata.id": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC",
    "@odata.type": "#CiscoInternalStorage.v1_0_0.CiscoInternalStorage",
    "Actions": {
        "#CiscoInternalStorage.ResetToDefault": {
            "target": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/Actions/CiscoInternalStorage.ResetToDefault"
        }
    },
    "Description": "FlexMMC Details",
    "Id": "FlexMMC",
    "Name": "FlexMMC",
    "Partitions": [
        {
            "@odata.id": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/CiscoPartition/IMCImages"
        },
        {
            "@odata.id": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/CiscoPartition/UserFiles"
        }
    ],
    "Partitions@odata.count": 2
}
```

## /redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/CiscoPartition/IMCImages

```{
    "@odata.context": "/redfish/v1/$metadata#CiscoPartition.CiscoPartition",
    "@odata.id": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/CiscoPartition/IMCImages",
    "@odata.type": "#CiscoPartition.v1_0_0.CiscoPartition",
    "Actions": {
        "#CiscoPartition.UploadFile": {
            "target": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/CiscoPartition/IMCImages/Actions/CiscoPartition.UploadFile"
        }
    },
    "AvailableSpaceMiB": 1536,
    "CiscoFile": {
        "@odata.id": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/CiscoPartition/IMCImages/CiscoFile"
    },
    "Description": "Cisco IMC Images",
    "Id": "IMCImages",
    "Name": "IMCImages",
    "TotalSpaceMiB": 1536
}
```

## /redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/CiscoPartition/IMCImages/CiscoFile

```{
    "@odata.context": "/redfish/v1/$metadata#CiscoFileCollection.CiscoFileCollection",
    "@odata.id": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/CiscoPartition/IMCImages/CiscoFile",
    "@odata.type": "#CiscoFileCollection.CiscoFileCollection",
    "Description": "Collection of Cisco Internal Storge Partition resources",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Cisco Internal Storage Partition Collections"
}
```

## /redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/CiscoPartition/UserFiles

```{
    "@odata.context": "/redfish/v1/$metadata#CiscoPartition.CiscoPartition",
    "@odata.id": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/CiscoPartition/UserFiles",
    "@odata.type": "#CiscoPartition.v1_0_0.CiscoPartition",
    "Actions": {
        "#CiscoPartition.UploadFile": {
            "target": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/CiscoPartition/UserFiles/Actions/CiscoPartition.UploadFile"
        }
    },
    "AvailableSpaceMiB": 6656,
    "CiscoFile": {
        "@odata.id": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/CiscoPartition/UserFiles/CiscoFile"
    },
    "Description": "User Uploaded Files",
    "Id": "UserFiles",
    "Name": "UserFiles",
    "TotalSpaceMiB": 6656
}
```

## /redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/CiscoPartition/UserFiles/CiscoFile

```{
    "@odata.context": "/redfish/v1/$metadata#CiscoFileCollection.CiscoFileCollection",
    "@odata.id": "/redfish/v1/Managers/CIMC/Oem/CiscoInternalStorage/FlexMMC/CiscoPartition/UserFiles/CiscoFile",
    "@odata.type": "#CiscoFileCollection.CiscoFileCollection",
    "Description": "Collection of Cisco Internal Storge Partition resources",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Cisco Internal Storage Partition Collections"
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
    "@odata.type": "#VirtualMedia.v1_4_0.VirtualMedia",
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
    "Status": {
        "Health": "OK",
        "State": "Disabled"
    },
    "TransferMethod": "Stream",
    "WriteProtected": true
}
```

## /redfish/v1/Managers/CIMC/VirtualMedia/1

```{
    "@odata.context": "/redfish/v1/$metadata#VirtualMedia.VirtualMedia",
    "@odata.id": "/redfish/v1/Managers/CIMC/VirtualMedia/1",
    "@odata.type": "#VirtualMedia.v1_4_0.VirtualMedia",
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
    "Status": {
        "Health": "OK",
        "State": "Disabled"
    },
    "TransferMethod": "Stream",
    "WriteProtected": true
}
```

## /redfish/v1/Managers/UCSC-M-V100-04_FCH26147UVK

```{
    "@odata.context": "/redfish/v1/$metadata#Manager.Manager",
    "@odata.id": "/redfish/v1/Managers/UCSC-M-V100-04_FCH26147UVK",
    "@odata.type": "#Manager.v1_5_0.Manager",
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [],
            "target": "/redfish/v1/Managers/UCSC-M-V100-04_FCH26147UVK/Actions/Manager.Reset"
        },
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
    },
    "Description": "Cisco Integrated Management Controller",
    "Id": "UCSC-M-V100-04_FCH26147UVK",
    "Name": "Cisco Integrated Management Controller",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Managers/UCSC-PCIE-C25Q-04_FCH26277TA5

```{
    "@odata.context": "/redfish/v1/$metadata#Manager.Manager",
    "@odata.id": "/redfish/v1/Managers/UCSC-PCIE-C25Q-04_FCH26277TA5",
    "@odata.type": "#Manager.v1_5_0.Manager",
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [],
            "target": "/redfish/v1/Managers/UCSC-PCIE-C25Q-04_FCH26277TA5/Actions/Manager.Reset"
        },
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
    },
    "Description": "Cisco Integrated Management Controller",
    "Id": "UCSC-PCIE-C25Q-04_FCH26277TA5",
    "Name": "Cisco Integrated Management Controller",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

