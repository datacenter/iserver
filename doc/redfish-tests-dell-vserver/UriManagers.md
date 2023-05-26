# Resource: /redfish/v1/Managers

Vendor | Model
--- | ---
Dell | vServer

## /redfish/v1/Managers

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerCollection.ManagerCollection",
    "@odata.id": "/redfish/v1/Managers",
    "@odata.type": "#ManagerCollection.ManagerCollection",
    "Description": "BMC",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Manager"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1

```{
    "@odata.context": "/redfish/v1/$metadata#Manager.Manager",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1",
    "@odata.type": "#Manager.v1_9_0.Manager",
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "GracefulRestart"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Actions/Manager.Reset"
        },
        "Oem": {
            "#OemManager.v1_3_0.OemManager#OemManager.ExportSystemConfiguration": {
                "ExportFormat@Redfish.AllowableValues": [
                    "XML",
                    "JSON"
                ],
                "ExportUse@Redfish.AllowableValues": [
                    "Default",
                    "Clone",
                    "Replace"
                ],
                "ShareParameters": {
                    "IgnoreCertificateWarning@Redfish.AllowableValues": [
                        "Disabled",
                        "Enabled"
                    ],
                    "ProxySupport@Redfish.AllowableValues": [
                        "Disabled",
                        "EnabledProxyDefault",
                        "Enabled"
                    ],
                    "ProxyType@Redfish.AllowableValues": [
                        "HTTP",
                        "SOCKS4"
                    ],
                    "ShareType@Redfish.AllowableValues": [
                        "LOCAL",
                        "NFS",
                        "CIFS",
                        "HTTP",
                        "HTTPS"
                    ]
                },
                "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Actions/Oem/EID_674_Manager.ExportSystemConfiguration"
            },
            "#OemManager.v1_3_0.OemManager#OemManager.ImportSystemConfiguration": {
                "HostPowerState@Redfish.AllowableValues": [
                    "On",
                    "Off"
                ],
                "ImportSystemConfiguration@Redfish.AllowableValues": [
                    "TimeToWait",
                    "ImportBuffer"
                ],
                "ShareParameters": {
                    "IgnoreCertificateWarning@Redfish.AllowableValues": [
                        "Disabled",
                        "Enabled"
                    ],
                    "ProxySupport@Redfish.AllowableValues": [
                        "Disabled",
                        "EnabledProxyDefault",
                        "Enabled"
                    ],
                    "ProxyType@Redfish.AllowableValues": [
                        "HTTP",
                        "SOCKS4"
                    ],
                    "ShareType@Redfish.AllowableValues": [
                        "LOCAL",
                        "NFS",
                        "CIFS",
                        "HTTP",
                        "HTTPS"
                    ]
                },
                "ShutdownType@Redfish.AllowableValues": [
                    "Graceful",
                    "Forced",
                    "NoReboot"
                ],
                "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Actions/Oem/EID_674_Manager.ImportSystemConfiguration"
            },
            "#OemManager.v1_3_0.OemManager#OemManager.ImportSystemConfigurationPreview": {
                "ImportSystemConfigurationPreview@Redfish.AllowableValues": [
                    "ImportBuffer"
                ],
                "ShareParameters": {
                    "IgnoreCertificateWarning@Redfish.AllowableValues": [
                        "Disabled",
                        "Enabled"
                    ],
                    "ProxySupport@Redfish.AllowableValues": [
                        "Disabled",
                        "EnabledProxyDefault",
                        "Enabled"
                    ],
                    "ProxyType@Redfish.AllowableValues": [
                        "HTTP",
                        "SOCKS4"
                    ],
                    "ShareType@Redfish.AllowableValues": [
                        "LOCAL",
                        "NFS",
                        "CIFS",
                        "HTTP",
                        "HTTPS"
                    ]
                },
                "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Actions/Oem/EID_674_Manager.ImportSystemConfigurationPreview"
            },
            "DellManager.v1_0_0#DellManager.ResetToDefaults": {
                "ResetType@Redfish.AllowableValues": [
                    "All",
                    "ResetAllWithRootDefaults",
                    "Default"
                ],
                "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Actions/Oem/DellManager.ResetToDefaults"
            }
        }
    },
    "CommandShell": {
        "ConnectTypesSupported": [
            "SSH",
            "IPMI"
        ],
        "ConnectTypesSupported@odata.count": 2,
        "MaxConcurrentSessions": 5,
        "ServiceEnabled": true
    },
    "DateTime": "2022-10-26T15:21:38-05:00",
    "DateTimeLocalOffset": "-05:00",
    "Description": "BMC",
    "EthernetInterfaces": {
        "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/EthernetInterfaces"
    },
    "FirmwareVersion": "5.10.00.00",
    "GraphicalConsole": {
        "ConnectTypesSupported": [
            "KVMIP"
        ],
        "ConnectTypesSupported@odata.count": 1,
        "MaxConcurrentSessions": 6,
        "ServiceEnabled": true
    },
    "HostInterfaces": {
        "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/HostInterfaces"
    },
    "Id": "iDRAC.Embedded.1",
    "Links": {
        "ActiveSoftwareImage": {
            "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Installed-25227-5.10.00.00__iDRAC.Embedded.1-1"
        },
        "ManagerForChassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
            }
        ],
        "ManagerForChassis@odata.count": 1,
        "ManagerForServers": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
            }
        ],
        "ManagerForServers@odata.count": 1,
        "ManagerInChassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "DellAttributes": [
                    {
                        "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/iDRAC.Embedded.1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/System.Embedded.1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/LifecycleController.Embedded.1"
                    }
                ],
                "DellAttributes@odata.count": 3,
                "DellJobService": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellJobService"
                },
                "DellLCService": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService"
                },
                "DellLicensableDeviceCollection": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicensableDevices"
                },
                "DellLicenseCollection": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenses"
                },
                "DellLicenseManagementService": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService"
                },
                "DellOpaqueManagementDataCollection": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellOpaqueManagementData"
                },
                "DellPersistentStorageService": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService"
                },
                "DellSwitchConnectionCollection": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkPorts/Oem/Dell/DellSwitchConnections"
                },
                "DellSwitchConnectionService": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSwitchConnectionService"
                },
                "DellSystemManagementService": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellSystemManagementService"
                },
                "DellSystemQuickSyncCollection": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellSystemQuickSync"
                },
                "DellTimeService": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellTimeService"
                },
                "DellUSBDeviceCollection": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellUSBDevices"
                },
                "DelliDRACCardService": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService"
                },
                "DellvFlashCollection": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellvFlash"
                },
                "Jobs": {
                    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/Jobs"
                }
            }
        },
        "SoftwareImages": [
            {
                "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Previous-25227-5.00.20.10__iDRAC.Embedded.1-1"
            },
            {
                "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/Installed-25227-5.10.00.00__iDRAC.Embedded.1-1"
            }
        ],
        "SoftwareImages@odata.count": 2
    },
    "LogServices": {
        "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/LogServices"
    },
    "ManagerType": "BMC",
    "Model": "15G Monolithic",
    "Name": "Manager",
    "NetworkProtocol": {
        "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/NetworkProtocol"
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DelliDRACCard": {
                "@odata.context": "/redfish/v1/$metadata#DelliDRACCard.DelliDRACCard",
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCard/iDRAC.Embedded.1-1_0x23_IDRACinfo",
                "@odata.type": "#DelliDRACCard.v1_1_0.DelliDRACCard",
                "Description": "An instance of DelliDRACCard will have data specific to the Integrated Dell Remote Access Controller (iDRAC) in the managed system.",
                "IPMIVersion": "2.0",
                "Id": "iDRAC.Embedded.1-1_0x23_IDRACinfo",
                "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                "LastUpdateTime": "2022-10-26T20:21:26+00:00",
                "Name": "DelliDRACCard",
                "URLString": "https://10.44.182.90:443"
            }
        }
    },
    "PowerState": "On",
    "Redundancy": [],
    "Redundancy@odata.count": 0,
    "SerialConsole": {
        "ConnectTypesSupported": [],
        "ConnectTypesSupported@odata.count": 0,
        "MaxConcurrentSessions": 0,
        "ServiceEnabled": false
    },
    "SerialInterfaces": {
        "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/SerialInterfaces"
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "UUID": "3346464f-c0b1-3880-4410-00344c4c4544",
    "VirtualMedia": {
        "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia"
    }
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Description": "Collection of EthernetInterfaces for this Manager",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/EthernetInterfaces/NIC.1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Ethernet Network Interface Collection"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/EthernetInterfaces/NIC.1

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterface.EthernetInterface",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/EthernetInterfaces/NIC.1",
    "@odata.type": "#EthernetInterface.v1_6_1.EthernetInterface",
    "AutoNeg": true,
    "Description": "Management Network Interface",
    "EthernetInterfaceType": "Physical",
    "FQDN": "",
    "FullDuplex": true,
    "HostName": "idrac-U8OIL5X",
    "IPv4Addresses": [
        {
            "Address": "10.44.182.90",
            "AddressOrigin": "Static",
            "Gateway": "10.29.152.1",
            "SubnetMask": "255.255.255.0"
        }
    ],
    "IPv4Addresses@odata.count": 1,
    "IPv6AddressPolicyTable": [],
    "IPv6AddressPolicyTable@odata.count": 0,
    "IPv6Addresses": [
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": "Preferred",
            "PrefixLength": 64
        },
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": "Preferred",
            "PrefixLength": 64
        },
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": null,
            "PrefixLength": 64
        },
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": null,
            "PrefixLength": 64
        },
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": null,
            "PrefixLength": 64
        },
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": null,
            "PrefixLength": 64
        },
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": null,
            "PrefixLength": 64
        },
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": null,
            "PrefixLength": 64
        },
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": null,
            "PrefixLength": 64
        },
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": null,
            "PrefixLength": 64
        },
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": null,
            "PrefixLength": 64
        },
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": null,
            "PrefixLength": 64
        },
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": null,
            "PrefixLength": 64
        },
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": null,
            "PrefixLength": 64
        },
        {
            "Address": "::",
            "AddressOrigin": null,
            "AddressState": null,
            "PrefixLength": 64
        },
        {
            "Address": "fe80::b29e:904d:cfe8:a0de",
            "AddressOrigin": null,
            "AddressState": "Preferred",
            "PrefixLength": 64
        }
    ],
    "IPv6Addresses@odata.count": 16,
    "IPv6DefaultGateway": "::",
    "IPv6StaticAddresses": [
        {
            "Address": "::",
            "PrefixLength": 64
        }
    ],
    "IPv6StaticAddresses@odata.count": 1,
    "Id": "NIC.1",
    "InterfaceEnabled": true,
    "Links": {
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        }
    },
    "MACAddress": "b0:7b:25:d1:5a:5a",
    "MTUSize": 1500,
    "MaxIPv6StaticAddresses": 1,
    "Name": "Manager Ethernet Interface",
    "NameServers": [
        "0.0.0.0",
        "0.0.0.0",
        "::",
        "::"
    ],
    "NameServers@odata.count": 4,
    "PermanentMACAddress": "b0:7b:25:d1:5a:5a",
    "SpeedMbps": 10000,
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "VLAN": {
        "VLANEnable": false,
        "VLANId": 1
    }
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/HostInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#HostInterfaceCollection.HostInterfaceCollection",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/HostInterfaces",
    "@odata.type": "#HostInterfaceCollection.HostInterfaceCollection",
    "Description": "Collection of Host Interfaces for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/HostInterfaces/Host.1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Host Interface Collection"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/HostInterfaces/Host.1

```{
    "@odata.context": "/redfish/v1/$metadata#HostInterface.HostInterface",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/HostInterfaces/Host.1",
    "@odata.type": "#HostInterface.v1_2_2.HostInterface",
    "Description": "Management for Host Interface",
    "ExternallyAccessible": false,
    "HostInterfaceType": "NetworkHostInterface",
    "Id": "Host.1",
    "InterfaceEnabled": false,
    "Name": "Managed Host Interface 1"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/LogServices

```
```

## /redfish/v1/Managers/iDRAC.Embedded.1/LogServices/Lclog

```
```

## /redfish/v1/Managers/iDRAC.Embedded.1/NetworkProtocol

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerNetworkProtocol.ManagerNetworkProtocol",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/NetworkProtocol",
    "@odata.type": "#ManagerNetworkProtocol.v1_6_0.ManagerNetworkProtocol",
    "DHCP": {
        "ProtocolEnabled": true
    },
    "DHCPv6": {
        "ProtocolEnabled": true
    },
    "Description": "Manager Network Service Status",
    "FQDN": "",
    "HTTP": {
        "Port": 80,
        "ProtocolEnabled": true
    },
    "HTTPS": {
        "Certificates": {
            "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/NetworkProtocol/HTTPS/Certificates"
        },
        "Port": 443,
        "ProtocolEnabled": true
    },
    "HostName": "idrac-U8OIL5X",
    "IPMI": {
        "ProtocolEnabled": true
    },
    "Id": "NetworkProtocol",
    "KVMIP": {
        "Port": 5900,
        "ProtocolEnabled": true
    },
    "NTP": {
        "NTPServers": [
            "",
            "",
            ""
        ],
        "NTPServers@odata.count": 3,
        "ProtocolEnabled": false
    },
    "Name": "Manager Network Protocol",
    "RFB": {
        "Port": 5901,
        "ProtocolEnabled": false
    },
    "SNMP": {
        "Port": 161,
        "ProtocolEnabled": true
    },
    "SSH": {
        "Port": 22,
        "ProtocolEnabled": true
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "Telnet": {
        "Port": 23,
        "ProtocolEnabled": false
    },
    "VirtualMedia": {
        "ProtocolEnabled": true
    }
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/NetworkProtocol/HTTPS/Certificates

```{
    "@odata.context": "/redfish/v1/$metadata#CertificateCollection.CertificateCollection",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/NetworkProtocol/HTTPS/Certificates",
    "@odata.type": "#CertificateCollection.CertificateCollection",
    "Description": "A Collection of Webserver SSL  Certificate resource instances.",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/NetworkProtocol/HTTPS/Certificates/SecurityCertificate.1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Certificate Collection"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/NetworkProtocol/HTTPS/Certificates/SecurityCertificate.1

```{
    "@odata.context": "/redfish/v1/$metadata#Certificate.Certificate",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/NetworkProtocol/HTTPS/Certificates/SecurityCertificate.1",
    "@odata.type": "#Certificate.v1_2_1.Certificate",
    "Description": "IDRAC Web server SSL digital certificate",
    "Id": "SecurityCertificate.1",
    "Issuer": {
        "City": "Round Rock",
        "CommonName": "idrac-SVCTAG",
        "Country": "US",
        "Email": null,
        "Organization": "Dell Inc.",
        "OrganizationalUnit": "Remote Access Group",
        "State": "Texas"
    },
    "Name": "Server Certificates",
    "Subject": {
        "City": "Round Rock",
        "CommonName": "idrac-SVCTAG",
        "Country": "US",
        "Email": null,
        "Organization": "Dell Inc.",
        "OrganizationalUnit": "Remote Access Group",
        "State": "Texas"
    },
    "ValidNotAfter": "2031-1-21T05:38:00+00:00",
    "ValidNotBefore": "2021-1-20T05:38:00+00:00"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/LifecycleController.Embedded.1

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/LifecycleController.Embedded.1/Settings"
        },
        "SupportedApplyTimes": [
            "Immediate",
            "AtMaintenanceWindowStart"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/LifecycleController.Embedded.1",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "AttributeRegistry": "ManagerAttributeRegistry.v1_0_0",
    "Attributes": {
        "LCAttributes.1.AutoDiscovery": "Off",
        "LCAttributes.1.AutoUpdate": "Disabled",
        "LCAttributes.1.BIOSRTDRequested": "False",
        "LCAttributes.1.CollectSystemInventoryOnRestart": "Enabled",
        "LCAttributes.1.DiscoveryFactoryDefaults": "Off",
        "LCAttributes.1.IPAddress": "",
        "LCAttributes.1.IPChangeNotifyPS": "Off",
        "LCAttributes.1.IgnoreCertWarning": "On",
        "LCAttributes.1.Licensed": "No",
        "LCAttributes.1.LifecycleControllerState": "Enabled",
        "LCAttributes.1.PartConfigurationUpdate": "Apply Always",
        "LCAttributes.1.PartFirmwareUpdate": "Match firmware of replaced part",
        "LCAttributes.1.ProvisioningServer": "",
        "LCAttributes.1.StorageHealthRollupStatus": 2,
        "LCAttributes.1.SystemID": "0912",
        "LCAttributes.1.UserProxyPassword": null,
        "LCAttributes.1.UserProxyPort": "80",
        "LCAttributes.1.UserProxyServer": "",
        "LCAttributes.1.UserProxyType": "HTTP",
        "LCAttributes.1.UserProxyUserName": "",
        "LCAttributes.1.VirtualAddressManagementApplication": "",
        "OSD.1.SupportedOSList": ""
    },
    "Description": "This schema provides the oem attributes",
    "Id": "LCAttributes",
    "Name": "OEMAttributeRegistry"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/LifecycleController.Embedded.1/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/LifecycleController.Embedded.1/Settings",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/LifecycleController.Embedded.1/Settings/Actions/DellManager.ClearPending"
        }
    },
    "AttributeRegistry": "ManagerAttributeRegistry.v1_0_0",
    "Attributes": {},
    "Description": "This schema provides settings of the oem attributes",
    "Id": "LCSettings",
    "Name": "OemAttributeRegistrySettings",
    "Oem": {
        "Dell": {
            "@odata.context": "/redfish/v1/$metadata#DellManager.DellManager",
            "@odata.type": "#DellManager.v1_1_0.DellManager",
            "Jobs": {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/Jobs"
            }
        }
    }
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/System.Embedded.1

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/System.Embedded.1/Settings"
        },
        "SupportedApplyTimes": [
            "Immediate",
            "AtMaintenanceWindowStart"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/System.Embedded.1",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "AttributeRegistry": "ManagerAttributeRegistry.v1_0_0",
    "Attributes": {
        "AcquisitionInfo.1.CostCenter": "",
        "AcquisitionInfo.1.Expensed": "No",
        "AcquisitionInfo.1.InstallDate": "",
        "AcquisitionInfo.1.PONumber": "0",
        "AcquisitionInfo.1.PurchaseCost": "0",
        "AcquisitionInfo.1.PurchaseDate": "",
        "AcquisitionInfo.1.Vendor": "Dell",
        "AcquisitionInfo.1.WayBill": "0",
        "AcquisitionInfo.1.WhoSigned": "",
        "Backplane.1.BackplaneBusMode": "I2C",
        "Backplane.1.BackplaneSplitMode": 0,
        "CustomAsset.1.Label": "",
        "CustomAsset.1.Value": "",
        "CustomAsset.10.Label": "",
        "CustomAsset.10.Value": "",
        "CustomAsset.11.Label": "",
        "CustomAsset.11.Value": "",
        "CustomAsset.12.Label": "",
        "CustomAsset.12.Value": "",
        "CustomAsset.13.Label": "",
        "CustomAsset.13.Value": "",
        "CustomAsset.14.Label": "",
        "CustomAsset.14.Value": "",
        "CustomAsset.15.Label": "",
        "CustomAsset.15.Value": "",
        "CustomAsset.16.Label": "",
        "CustomAsset.16.Value": "",
        "CustomAsset.17.Label": "",
        "CustomAsset.17.Value": "",
        "CustomAsset.18.Label": "",
        "CustomAsset.18.Value": "",
        "CustomAsset.19.Label": "",
        "CustomAsset.19.Value": "",
        "CustomAsset.2.Label": "",
        "CustomAsset.2.Value": "",
        "CustomAsset.20.Label": "",
        "CustomAsset.20.Value": "",
        "CustomAsset.21.Label": "",
        "CustomAsset.21.Value": "",
        "CustomAsset.22.Label": "",
        "CustomAsset.22.Value": "",
        "CustomAsset.23.Label": "",
        "CustomAsset.23.Value": "",
        "CustomAsset.24.Label": "",
        "CustomAsset.24.Value": "",
        "CustomAsset.25.Label": "",
        "CustomAsset.25.Value": "",
        "CustomAsset.26.Label": "",
        "CustomAsset.26.Value": "",
        "CustomAsset.27.Label": "",
        "CustomAsset.27.Value": "",
        "CustomAsset.28.Label": "",
        "CustomAsset.28.Value": "",
        "CustomAsset.29.Label": "",
        "CustomAsset.29.Value": "",
        "CustomAsset.3.Label": "",
        "CustomAsset.3.Value": "",
        "CustomAsset.30.Label": "",
        "CustomAsset.30.Value": "",
        "CustomAsset.31.Label": "",
        "CustomAsset.31.Value": "",
        "CustomAsset.32.Label": "",
        "CustomAsset.32.Value": "",
        "CustomAsset.4.Label": "",
        "CustomAsset.4.Value": "",
        "CustomAsset.5.Label": "",
        "CustomAsset.5.Value": "",
        "CustomAsset.6.Label": "",
        "CustomAsset.6.Value": "",
        "CustomAsset.7.Label": "",
        "CustomAsset.7.Value": "",
        "CustomAsset.8.Label": "",
        "CustomAsset.8.Value": "",
        "CustomAsset.9.Label": "",
        "CustomAsset.9.Value": "",
        "DepreciationInfo.1.Duration": "0",
        "DepreciationInfo.1.DurationUnit": "Months",
        "DepreciationInfo.1.Method": "",
        "DepreciationInfo.1.Percentage": "0",
        "Diagnostics.1.OSAppCollectionTime": "N/A",
        "ExtWarrantyInfo.1.Cost": "0",
        "ExtWarrantyInfo.1.EndDate": "",
        "ExtWarrantyInfo.1.Provider": "",
        "ExtWarrantyInfo.1.StartDate": "",
        "LCD.1.ChassisIdentifyDuration": -1,
        "LCD.1.Configuration": "Service Tag",
        "LCD.1.CurrentDisplay": "ST: U8OIL5X",
        "LCD.1.ErrorDisplayMode": "SEL",
        "LCD.1.FrontPanelLocking": "Full-Access",
        "LCD.1.HideErrs": "unhide",
        "LCD.1.LicenseMsgEnable": "No-License-Msg",
        "LCD.1.NMIResetOverride": "DIsabled",
        "LCD.1.NumberErrsHidden": 0,
        "LCD.1.NumberErrsVisible": 0,
        "LCD.1.QualifierTemp": "C",
        "LCD.1.QualifierWatt": "Watts",
        "LCD.1.UserDefinedString": "",
        "LCD.1.vConsoleIndication": "Enabled",
        "LeaseInfo.1.Buyout": "0",
        "LeaseInfo.1.EndDate": "",
        "LeaseInfo.1.FairValue": "0",
        "LeaseInfo.1.Lessor": "",
        "LeaseInfo.1.MultiSched": "No",
        "LeaseInfo.1.RateFactor": "0",
        "MaintenanceInfo.1.EndDate": "",
        "MaintenanceInfo.1.Provider": "",
        "MaintenanceInfo.1.Restrictions": "",
        "MaintenanceInfo.1.StartDate": "",
        "OpenIDConnectServer.1.DiscoveryURL": "",
        "OpenIDConnectServer.1.Enabled": "Disabled",
        "OpenIDConnectServer.1.Name": "",
        "OpenIDConnectServer.1.RegistrationDetails": null,
        "OpenIDConnectServer.1.RegistrationStatus": "",
        "OpenIDConnectServer.10.DiscoveryURL": "",
        "OpenIDConnectServer.10.Enabled": "Disabled",
        "OpenIDConnectServer.10.Name": "",
        "OpenIDConnectServer.10.RegistrationDetails": null,
        "OpenIDConnectServer.10.RegistrationStatus": "",
        "OpenIDConnectServer.11.DiscoveryURL": "",
        "OpenIDConnectServer.11.Enabled": "Disabled",
        "OpenIDConnectServer.11.Name": "",
        "OpenIDConnectServer.11.RegistrationDetails": null,
        "OpenIDConnectServer.11.RegistrationStatus": "",
        "OpenIDConnectServer.12.DiscoveryURL": "",
        "OpenIDConnectServer.12.Enabled": "Disabled",
        "OpenIDConnectServer.12.Name": "",
        "OpenIDConnectServer.12.RegistrationDetails": null,
        "OpenIDConnectServer.12.RegistrationStatus": "",
        "OpenIDConnectServer.13.DiscoveryURL": "",
        "OpenIDConnectServer.13.Enabled": "Disabled",
        "OpenIDConnectServer.13.Name": "",
        "OpenIDConnectServer.13.RegistrationDetails": null,
        "OpenIDConnectServer.13.RegistrationStatus": "",
        "OpenIDConnectServer.14.DiscoveryURL": "",
        "OpenIDConnectServer.14.Enabled": "Disabled",
        "OpenIDConnectServer.14.Name": "",
        "OpenIDConnectServer.14.RegistrationDetails": null,
        "OpenIDConnectServer.14.RegistrationStatus": "",
        "OpenIDConnectServer.15.DiscoveryURL": "",
        "OpenIDConnectServer.15.Enabled": "Disabled",
        "OpenIDConnectServer.15.Name": "",
        "OpenIDConnectServer.15.RegistrationDetails": null,
        "OpenIDConnectServer.15.RegistrationStatus": "",
        "OpenIDConnectServer.16.DiscoveryURL": "",
        "OpenIDConnectServer.16.Enabled": "Disabled",
        "OpenIDConnectServer.16.Name": "",
        "OpenIDConnectServer.16.RegistrationDetails": null,
        "OpenIDConnectServer.16.RegistrationStatus": "",
        "OpenIDConnectServer.2.DiscoveryURL": "",
        "OpenIDConnectServer.2.Enabled": "Disabled",
        "OpenIDConnectServer.2.Name": "",
        "OpenIDConnectServer.2.RegistrationDetails": null,
        "OpenIDConnectServer.2.RegistrationStatus": "",
        "OpenIDConnectServer.3.DiscoveryURL": "",
        "OpenIDConnectServer.3.Enabled": "Disabled",
        "OpenIDConnectServer.3.Name": "",
        "OpenIDConnectServer.3.RegistrationDetails": null,
        "OpenIDConnectServer.3.RegistrationStatus": "",
        "OpenIDConnectServer.4.DiscoveryURL": "",
        "OpenIDConnectServer.4.Enabled": "Disabled",
        "OpenIDConnectServer.4.Name": "",
        "OpenIDConnectServer.4.RegistrationDetails": null,
        "OpenIDConnectServer.4.RegistrationStatus": "",
        "OpenIDConnectServer.5.DiscoveryURL": "",
        "OpenIDConnectServer.5.Enabled": "Disabled",
        "OpenIDConnectServer.5.Name": "",
        "OpenIDConnectServer.5.RegistrationDetails": null,
        "OpenIDConnectServer.5.RegistrationStatus": "",
        "OpenIDConnectServer.6.DiscoveryURL": "",
        "OpenIDConnectServer.6.Enabled": "Disabled",
        "OpenIDConnectServer.6.Name": "",
        "OpenIDConnectServer.6.RegistrationDetails": null,
        "OpenIDConnectServer.6.RegistrationStatus": "",
        "OpenIDConnectServer.7.DiscoveryURL": "",
        "OpenIDConnectServer.7.Enabled": "Disabled",
        "OpenIDConnectServer.7.Name": "",
        "OpenIDConnectServer.7.RegistrationDetails": null,
        "OpenIDConnectServer.7.RegistrationStatus": "",
        "OpenIDConnectServer.8.DiscoveryURL": "",
        "OpenIDConnectServer.8.Enabled": "Disabled",
        "OpenIDConnectServer.8.Name": "",
        "OpenIDConnectServer.8.RegistrationDetails": null,
        "OpenIDConnectServer.8.RegistrationStatus": "",
        "OpenIDConnectServer.9.DiscoveryURL": "",
        "OpenIDConnectServer.9.Enabled": "Disabled",
        "OpenIDConnectServer.9.Name": "",
        "OpenIDConnectServer.9.RegistrationDetails": null,
        "OpenIDConnectServer.9.RegistrationStatus": "",
        "OutsourceInfo.1.ProbComp": "",
        "OutsourceInfo.1.ProviderFee": "0",
        "OutsourceInfo.1.SLALevel": "",
        "OutsourceInfo.1.ServiceFee": "0",
        "OutsourceInfo.1.SignedFor": "",
        "OwnerInfo.1.InsComp": "",
        "OwnerInfo.1.OwnerName": "",
        "OwnerInfo.1.Type": "Owned",
        "PCIeSlotLFM.1.3rdPartyCard": "No",
        "PCIeSlotLFM.1.CardType": "FC",
        "PCIeSlotLFM.1.LFMMode": "Automatic",
        "PCIeSlotLFM.1.MaxLFM": 1170,
        "PCIeSlotLFM.1.PCIeInletTemperature": 31,
        "PCIeSlotLFM.1.SlotState": "Defined",
        "PCIeSlotLFM.1.TargetLFM": "Temperature Controlled",
        "PCIeSlotLFM.10.3rdPartyCard": "N/A",
        "PCIeSlotLFM.10.CardType": "Empty",
        "PCIeSlotLFM.10.LFMMode": "Automatic",
        "PCIeSlotLFM.10.MaxLFM": 0,
        "PCIeSlotLFM.10.PCIeInletTemperature": 0,
        "PCIeSlotLFM.10.SlotState": "Not-Defined",
        "PCIeSlotLFM.10.TargetLFM": "-",
        "PCIeSlotLFM.11.3rdPartyCard": "N/A",
        "PCIeSlotLFM.11.CardType": "Empty",
        "PCIeSlotLFM.11.LFMMode": "Automatic",
        "PCIeSlotLFM.11.MaxLFM": 0,
        "PCIeSlotLFM.11.PCIeInletTemperature": 0,
        "PCIeSlotLFM.11.SlotState": "Not-Defined",
        "PCIeSlotLFM.11.TargetLFM": "-",
        "PCIeSlotLFM.12.3rdPartyCard": "N/A",
        "PCIeSlotLFM.12.CardType": "Empty",
        "PCIeSlotLFM.12.LFMMode": "Automatic",
        "PCIeSlotLFM.12.MaxLFM": 0,
        "PCIeSlotLFM.12.PCIeInletTemperature": 0,
        "PCIeSlotLFM.12.SlotState": "Not-Defined",
        "PCIeSlotLFM.12.TargetLFM": "-",
        "PCIeSlotLFM.13.3rdPartyCard": "N/A",
        "PCIeSlotLFM.13.CardType": "Empty",
        "PCIeSlotLFM.13.LFMMode": "Automatic",
        "PCIeSlotLFM.13.MaxLFM": 0,
        "PCIeSlotLFM.13.PCIeInletTemperature": 0,
        "PCIeSlotLFM.13.SlotState": "Not-Defined",
        "PCIeSlotLFM.13.TargetLFM": "-",
        "PCIeSlotLFM.14.3rdPartyCard": "N/A",
        "PCIeSlotLFM.14.CardType": "Empty",
        "PCIeSlotLFM.14.LFMMode": "Automatic",
        "PCIeSlotLFM.14.MaxLFM": 0,
        "PCIeSlotLFM.14.PCIeInletTemperature": 0,
        "PCIeSlotLFM.14.SlotState": "Not-Defined",
        "PCIeSlotLFM.14.TargetLFM": "-",
        "PCIeSlotLFM.15.3rdPartyCard": "N/A",
        "PCIeSlotLFM.15.CardType": "Empty",
        "PCIeSlotLFM.15.LFMMode": "Automatic",
        "PCIeSlotLFM.15.MaxLFM": 0,
        "PCIeSlotLFM.15.PCIeInletTemperature": 0,
        "PCIeSlotLFM.15.SlotState": "Not-Defined",
        "PCIeSlotLFM.15.TargetLFM": "-",
        "PCIeSlotLFM.16.3rdPartyCard": "N/A",
        "PCIeSlotLFM.16.CardType": "Empty",
        "PCIeSlotLFM.16.LFMMode": "Automatic",
        "PCIeSlotLFM.16.MaxLFM": 0,
        "PCIeSlotLFM.16.PCIeInletTemperature": 0,
        "PCIeSlotLFM.16.SlotState": "Not-Defined",
        "PCIeSlotLFM.16.TargetLFM": "-",
        "PCIeSlotLFM.17.3rdPartyCard": "N/A",
        "PCIeSlotLFM.17.CardType": "Empty",
        "PCIeSlotLFM.17.LFMMode": "Automatic",
        "PCIeSlotLFM.17.MaxLFM": 0,
        "PCIeSlotLFM.17.PCIeInletTemperature": 0,
        "PCIeSlotLFM.17.SlotState": "Not-Defined",
        "PCIeSlotLFM.17.TargetLFM": "-",
        "PCIeSlotLFM.18.3rdPartyCard": "N/A",
        "PCIeSlotLFM.18.CardType": "Empty",
        "PCIeSlotLFM.18.LFMMode": "Automatic",
        "PCIeSlotLFM.18.MaxLFM": 0,
        "PCIeSlotLFM.18.PCIeInletTemperature": 0,
        "PCIeSlotLFM.18.SlotState": "Not-Defined",
        "PCIeSlotLFM.18.TargetLFM": "-",
        "PCIeSlotLFM.19.3rdPartyCard": "N/A",
        "PCIeSlotLFM.19.CardType": "Empty",
        "PCIeSlotLFM.19.LFMMode": "Automatic",
        "PCIeSlotLFM.19.MaxLFM": 0,
        "PCIeSlotLFM.19.PCIeInletTemperature": 0,
        "PCIeSlotLFM.19.SlotState": "Not-Defined",
        "PCIeSlotLFM.19.TargetLFM": "-",
        "PCIeSlotLFM.2.3rdPartyCard": "N/A",
        "PCIeSlotLFM.2.CardType": "Empty",
        "PCIeSlotLFM.2.LFMMode": "Automatic",
        "PCIeSlotLFM.2.MaxLFM": 1320,
        "PCIeSlotLFM.2.PCIeInletTemperature": 30,
        "PCIeSlotLFM.2.SlotState": "Defined",
        "PCIeSlotLFM.2.TargetLFM": "-",
        "PCIeSlotLFM.20.3rdPartyCard": "N/A",
        "PCIeSlotLFM.20.CardType": "Empty",
        "PCIeSlotLFM.20.LFMMode": "Automatic",
        "PCIeSlotLFM.20.MaxLFM": 0,
        "PCIeSlotLFM.20.PCIeInletTemperature": 0,
        "PCIeSlotLFM.20.SlotState": "Not-Defined",
        "PCIeSlotLFM.20.TargetLFM": "-",
        "PCIeSlotLFM.21.3rdPartyCard": "N/A",
        "PCIeSlotLFM.21.CardType": "Empty",
        "PCIeSlotLFM.21.LFMMode": "Automatic",
        "PCIeSlotLFM.21.MaxLFM": 0,
        "PCIeSlotLFM.21.PCIeInletTemperature": 0,
        "PCIeSlotLFM.21.SlotState": "Not-Defined",
        "PCIeSlotLFM.21.TargetLFM": "-",
        "PCIeSlotLFM.22.3rdPartyCard": "N/A",
        "PCIeSlotLFM.22.CardType": "Empty",
        "PCIeSlotLFM.22.LFMMode": "Automatic",
        "PCIeSlotLFM.22.MaxLFM": 0,
        "PCIeSlotLFM.22.PCIeInletTemperature": 0,
        "PCIeSlotLFM.22.SlotState": "Not-Defined",
        "PCIeSlotLFM.22.TargetLFM": "-",
        "PCIeSlotLFM.23.3rdPartyCard": "N/A",
        "PCIeSlotLFM.23.CardType": "Empty",
        "PCIeSlotLFM.23.LFMMode": "Automatic",
        "PCIeSlotLFM.23.MaxLFM": 0,
        "PCIeSlotLFM.23.PCIeInletTemperature": 0,
        "PCIeSlotLFM.23.SlotState": "Not-Defined",
        "PCIeSlotLFM.23.TargetLFM": "-",
        "PCIeSlotLFM.24.3rdPartyCard": "N/A",
        "PCIeSlotLFM.24.CardType": "Empty",
        "PCIeSlotLFM.24.LFMMode": "Automatic",
        "PCIeSlotLFM.24.MaxLFM": 0,
        "PCIeSlotLFM.24.PCIeInletTemperature": 0,
        "PCIeSlotLFM.24.SlotState": "Not-Defined",
        "PCIeSlotLFM.24.TargetLFM": "-",
        "PCIeSlotLFM.25.3rdPartyCard": "N/A",
        "PCIeSlotLFM.25.CardType": "Empty",
        "PCIeSlotLFM.25.LFMMode": "Automatic",
        "PCIeSlotLFM.25.MaxLFM": 0,
        "PCIeSlotLFM.25.PCIeInletTemperature": 0,
        "PCIeSlotLFM.25.SlotState": "Not-Defined",
        "PCIeSlotLFM.25.TargetLFM": "-",
        "PCIeSlotLFM.26.3rdPartyCard": "N/A",
        "PCIeSlotLFM.26.CardType": "Empty",
        "PCIeSlotLFM.26.LFMMode": "Automatic",
        "PCIeSlotLFM.26.MaxLFM": 0,
        "PCIeSlotLFM.26.PCIeInletTemperature": 0,
        "PCIeSlotLFM.26.SlotState": "Not-Defined",
        "PCIeSlotLFM.26.TargetLFM": "-",
        "PCIeSlotLFM.27.3rdPartyCard": "N/A",
        "PCIeSlotLFM.27.CardType": "Empty",
        "PCIeSlotLFM.27.LFMMode": "Automatic",
        "PCIeSlotLFM.27.MaxLFM": 0,
        "PCIeSlotLFM.27.PCIeInletTemperature": 0,
        "PCIeSlotLFM.27.SlotState": "Not-Defined",
        "PCIeSlotLFM.27.TargetLFM": "-",
        "PCIeSlotLFM.28.3rdPartyCard": "N/A",
        "PCIeSlotLFM.28.CardType": "Empty",
        "PCIeSlotLFM.28.LFMMode": "Automatic",
        "PCIeSlotLFM.28.MaxLFM": 0,
        "PCIeSlotLFM.28.PCIeInletTemperature": 0,
        "PCIeSlotLFM.28.SlotState": "Not-Defined",
        "PCIeSlotLFM.28.TargetLFM": "-",
        "PCIeSlotLFM.29.3rdPartyCard": "N/A",
        "PCIeSlotLFM.29.CardType": "Empty",
        "PCIeSlotLFM.29.LFMMode": "Automatic",
        "PCIeSlotLFM.29.MaxLFM": 0,
        "PCIeSlotLFM.29.PCIeInletTemperature": 0,
        "PCIeSlotLFM.29.SlotState": "Not-Defined",
        "PCIeSlotLFM.29.TargetLFM": "-",
        "PCIeSlotLFM.3.3rdPartyCard": "N/A",
        "PCIeSlotLFM.3.CardType": "Empty",
        "PCIeSlotLFM.3.LFMMode": "Automatic",
        "PCIeSlotLFM.3.MaxLFM": 1130,
        "PCIeSlotLFM.3.PCIeInletTemperature": 33,
        "PCIeSlotLFM.3.SlotState": "Not-Defined",
        "PCIeSlotLFM.3.TargetLFM": "-",
        "PCIeSlotLFM.30.3rdPartyCard": "N/A",
        "PCIeSlotLFM.30.CardType": "Empty",
        "PCIeSlotLFM.30.LFMMode": "Automatic",
        "PCIeSlotLFM.30.MaxLFM": 0,
        "PCIeSlotLFM.30.PCIeInletTemperature": 0,
        "PCIeSlotLFM.30.SlotState": "Not-Defined",
        "PCIeSlotLFM.30.TargetLFM": "-",
        "PCIeSlotLFM.31.3rdPartyCard": "N/A",
        "PCIeSlotLFM.31.CardType": "Empty",
        "PCIeSlotLFM.31.LFMMode": "Automatic",
        "PCIeSlotLFM.31.MaxLFM": 0,
        "PCIeSlotLFM.31.PCIeInletTemperature": 0,
        "PCIeSlotLFM.31.SlotState": "Not-Defined",
        "PCIeSlotLFM.31.TargetLFM": "-",
        "PCIeSlotLFM.32.3rdPartyCard": "N/A",
        "PCIeSlotLFM.32.CardType": "Empty",
        "PCIeSlotLFM.32.LFMMode": "Automatic",
        "PCIeSlotLFM.32.MaxLFM": 0,
        "PCIeSlotLFM.32.PCIeInletTemperature": 0,
        "PCIeSlotLFM.32.SlotState": "Not-Defined",
        "PCIeSlotLFM.32.TargetLFM": "-",
        "PCIeSlotLFM.33.3rdPartyCard": "N/A",
        "PCIeSlotLFM.33.CardType": "Empty",
        "PCIeSlotLFM.33.LFMMode": "Automatic",
        "PCIeSlotLFM.33.MaxLFM": 0,
        "PCIeSlotLFM.33.PCIeInletTemperature": 0,
        "PCIeSlotLFM.33.SlotState": "Not-Defined",
        "PCIeSlotLFM.33.TargetLFM": "-",
        "PCIeSlotLFM.34.3rdPartyCard": "N/A",
        "PCIeSlotLFM.34.CardType": "Empty",
        "PCIeSlotLFM.34.LFMMode": "Automatic",
        "PCIeSlotLFM.34.MaxLFM": 0,
        "PCIeSlotLFM.34.PCIeInletTemperature": 0,
        "PCIeSlotLFM.34.SlotState": "Not-Defined",
        "PCIeSlotLFM.34.TargetLFM": "-",
        "PCIeSlotLFM.4.3rdPartyCard": "N/A",
        "PCIeSlotLFM.4.CardType": "Empty",
        "PCIeSlotLFM.4.LFMMode": "Automatic",
        "PCIeSlotLFM.4.MaxLFM": 0,
        "PCIeSlotLFM.4.PCIeInletTemperature": 0,
        "PCIeSlotLFM.4.SlotState": "Not-Defined",
        "PCIeSlotLFM.4.TargetLFM": "-",
        "PCIeSlotLFM.5.3rdPartyCard": "N/A",
        "PCIeSlotLFM.5.CardType": "Empty",
        "PCIeSlotLFM.5.LFMMode": "Automatic",
        "PCIeSlotLFM.5.MaxLFM": 0,
        "PCIeSlotLFM.5.PCIeInletTemperature": 0,
        "PCIeSlotLFM.5.SlotState": "Not-Defined",
        "PCIeSlotLFM.5.TargetLFM": "-",
        "PCIeSlotLFM.6.3rdPartyCard": "N/A",
        "PCIeSlotLFM.6.CardType": "Empty",
        "PCIeSlotLFM.6.LFMMode": "Automatic",
        "PCIeSlotLFM.6.MaxLFM": 0,
        "PCIeSlotLFM.6.PCIeInletTemperature": 0,
        "PCIeSlotLFM.6.SlotState": "Not-Defined",
        "PCIeSlotLFM.6.TargetLFM": "-",
        "PCIeSlotLFM.7.3rdPartyCard": "N/A",
        "PCIeSlotLFM.7.CardType": "Empty",
        "PCIeSlotLFM.7.LFMMode": "Automatic",
        "PCIeSlotLFM.7.MaxLFM": 0,
        "PCIeSlotLFM.7.PCIeInletTemperature": 0,
        "PCIeSlotLFM.7.SlotState": "Not-Defined",
        "PCIeSlotLFM.7.TargetLFM": "-",
        "PCIeSlotLFM.8.3rdPartyCard": "N/A",
        "PCIeSlotLFM.8.CardType": "Empty",
        "PCIeSlotLFM.8.LFMMode": "Automatic",
        "PCIeSlotLFM.8.MaxLFM": 0,
        "PCIeSlotLFM.8.PCIeInletTemperature": 0,
        "PCIeSlotLFM.8.SlotState": "Not-Defined",
        "PCIeSlotLFM.8.TargetLFM": "-",
        "PCIeSlotLFM.9.3rdPartyCard": "N/A",
        "PCIeSlotLFM.9.CardType": "Empty",
        "PCIeSlotLFM.9.LFMMode": "Automatic",
        "PCIeSlotLFM.9.MaxLFM": 0,
        "PCIeSlotLFM.9.PCIeInletTemperature": 0,
        "PCIeSlotLFM.9.SlotState": "Not-Defined",
        "PCIeSlotLFM.9.TargetLFM": "-",
        "QuickSync.1.Access": "Read-write",
        "QuickSync.1.InactivityTimeout": 120,
        "QuickSync.1.InactivityTimerEnable": "Enabled",
        "QuickSync.1.Presence": "Absent",
        "QuickSync.1.ReadAuthentication": "Enabled",
        "QuickSync.1.WifiEnable": "Enabled",
        "SC-BMC.1.PowerMonitoring": 0,
        "ServerInfo.1.NodeID": "U8OIL5X",
        "ServerInfo.1.RChassisServiceTag": "",
        "ServerInfo.1.ServerType": "Rack",
        "ServerInfo.1.ServiceTag": "U8OIL5X",
        "ServerOS.1.HostName": "",
        "ServerOS.1.OEMOSVersion": "",
        "ServerOS.1.OSName": "DellEMC-VMware ESXi",
        "ServerOS.1.OSVersion": "7.0 Update 1 Build-17551050 (A05)",
        "ServerOS.1.ProductKey": "",
        "ServerOS.1.ServerPoweredOnTime": 4918850,
        "ServerPwr.1.ActivePolicyName": "",
        "ServerPwr.1.ActivePowerCapVal": 278,
        "ServerPwr.1.PSRapidOn": "Enabled",
        "ServerPwr.1.PSRedPolicy": "A/B Grid Redundant",
        "ServerPwr.1.PowerCapMaxThres": 836,
        "ServerPwr.1.PowerCapMinThres": 501,
        "ServerPwr.1.PowerCapSetting": "Disabled",
        "ServerPwr.1.PowerCapValue": 278,
        "ServerPwr.1.RapidOnPrimaryPSU": "PSU1",
        "ServerPwrMon.1.AccumulativePower": 3982394,
        "ServerPwrMon.1.CumulativePowerStartTime": 1625257740,
        "ServerPwrMon.1.CumulativePowerStartTimeStr": "2021-07-02T20:29:00Z",
        "ServerPwrMon.1.MinPowerTime": 1649239599,
        "ServerPwrMon.1.MinPowerTimeStr": "2022-04-06T10:06:39Z",
        "ServerPwrMon.1.MinPowerWatts": 22,
        "ServerPwrMon.1.PeakCurrentTime": 1625263702,
        "ServerPwrMon.1.PeakCurrentTimeStr": "2021-07-02T22:08:22Z",
        "ServerPwrMon.1.PeakPowerStartTime": 1625257741,
        "ServerPwrMon.1.PeakPowerStartTimeStr": "2021-07-02T20:29:01Z",
        "ServerPwrMon.1.PeakPowerTime": 1625257827,
        "ServerPwrMon.1.PeakPowerTimeStr": "2021-07-02T20:30:27Z",
        "ServerPwrMon.1.PeakPowerWatts": 612,
        "ServerPwrMon.1.PowerConfigReset": "None",
        "ServerTopology.1.AisleName": "",
        "ServerTopology.1.DataCenterName": "",
        "ServerTopology.1.ManagedSystemSizeInU": "1",
        "ServerTopology.1.RackName": "",
        "ServerTopology.1.RackSlot": 1,
        "ServerTopology.1.RoomName": "",
        "ServerTopology.1.SizeOfManagedSystemInU": 1,
        "ServiceContract.1.Renewed": "No",
        "ServiceContract.1.Type": "",
        "ServiceContract.1.Vendor": "",
        "Storage.1.AvailableSpareAlertThreshold": 10,
        "Storage.1.RemainingRatedWriteEnduranceAlertThreshold": 10,
        "SupportInfo.1.AutoFix": "",
        "SupportInfo.1.HelpDesk": "",
        "SupportInfo.1.Outsourced": "No",
        "SupportInfo.1.Type": "Network",
        "SystemInfo.1.BootTime": "Tue Aug 30 17:00:48 2022",
        "SystemInfo.1.PrimaryTelephone": "",
        "SystemInfo.1.PrimaryUser": "",
        "SystemInfo.1.SysLocation": "",
        "SystemInfo.1.SysTime": "Wed Oct 26 15:21:38 2022",
        "ThermalConfig.1.ASHRAEEnvironmentalClass": "A2",
        "ThermalConfig.1.CriticalEventGenerationInterval": 30,
        "ThermalConfig.1.EventGenerationInterval": 30,
        "ThermalConfig.1.FreshAirCompliantConfiguration": "No",
        "ThermalConfig.1.MaxCFM": 0,
        "ThermalConfig.1.ValidFanConfiguration": "Yes",
        "ThermalHistorical.1.IntervalInSeconds": 0,
        "ThermalSettings.1.AirExhaustTempSupport": "Not Supported",
        "ThermalSettings.1.AirTemperatureRiseLimitSupport": "Not Supported",
        "ThermalSettings.1.CurrentSystemProfileValue": "Maximum Performance",
        "ThermalSettings.1.DriveTemperaturePolling": "Default",
        "ThermalSettings.1.FanSpeedHighOffsetVal": 75,
        "ThermalSettings.1.FanSpeedLowOffsetVal": 25,
        "ThermalSettings.1.FanSpeedMaxOffsetVal": 100,
        "ThermalSettings.1.FanSpeedMediumOffsetVal": 50,
        "ThermalSettings.1.FanSpeedOffset": "Off",
        "ThermalSettings.1.MFSMaximumLimit": 100,
        "ThermalSettings.1.MFSMinimumLimit": 32,
        "ThermalSettings.1.MaximumPCIeInletTemperatureLimitSupport": "Not Supported",
        "ThermalSettings.1.MinimumFanSpeed": 255,
        "ThermalSettings.1.PCIeSlotLFMSupport": "Not Supported",
        "ThermalSettings.1.SystemCFMSupport": "Not Supported",
        "ThermalSettings.1.SystemExhaustTemperature": 35,
        "ThermalSettings.1.SystemInletTemperature": 18,
        "ThermalSettings.1.SystemInletTemperatureSupportLimitPerConfiguration": 35,
        "ThermalSettings.1.TargetExhaustTemperatureLimit": 70,
        "ThermalSettings.1.ThermalProfile": "Default Thermal Profile Settings",
        "USBFront.1.Enable": "Not Applicable",
        "WarrantyInfo.1.Cost": "0",
        "WarrantyInfo.1.Duration": "0",
        "WarrantyInfo.1.EndDate": "",
        "WarrantyInfo.1.UnitType": "Days"
    },
    "Description": "This schema provides the oem attributes",
    "Id": "SystemAttributes",
    "Name": "OEMAttributeRegistry"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/System.Embedded.1/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/System.Embedded.1/Settings",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/System.Embedded.1/Settings/Actions/DellManager.ClearPending"
        }
    },
    "AttributeRegistry": "ManagerAttributeRegistry.v1_0_0",
    "Attributes": {},
    "Description": "This schema provides settings of the oem attributes",
    "Id": "SystemSettings",
    "Name": "OemAttributeRegistrySettings",
    "Oem": {
        "Dell": {
            "@odata.context": "/redfish/v1/$metadata#DellManager.DellManager",
            "@odata.type": "#DellManager.v1_1_0.DellManager",
            "Jobs": {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/Jobs"
            }
        }
    }
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/iDRAC.Embedded.1

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/iDRAC.Embedded.1/Settings"
        },
        "SupportedApplyTimes": [
            "Immediate",
            "AtMaintenanceWindowStart"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/iDRAC.Embedded.1",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "AttributeRegistry": "ManagerAttributeRegistry.v1_0_0",
    "Attributes": {
        "ADGroup.1.Domain": "",
        "ADGroup.1.Name": "",
        "ADGroup.1.Privilege": 0,
        "ADGroup.10.Domain": "",
        "ADGroup.10.Name": "",
        "ADGroup.10.Privilege": 0,
        "ADGroup.11.Domain": "",
        "ADGroup.11.Name": "",
        "ADGroup.11.Privilege": 0,
        "ADGroup.12.Domain": "",
        "ADGroup.12.Name": "",
        "ADGroup.12.Privilege": 0,
        "ADGroup.13.Domain": "",
        "ADGroup.13.Name": "",
        "ADGroup.13.Privilege": 0,
        "ADGroup.14.Domain": "",
        "ADGroup.14.Name": "",
        "ADGroup.14.Privilege": 0,
        "ADGroup.15.Domain": "",
        "ADGroup.15.Name": "",
        "ADGroup.15.Privilege": 0,
        "ADGroup.2.Domain": "",
        "ADGroup.2.Name": "",
        "ADGroup.2.Privilege": 0,
        "ADGroup.3.Domain": "",
        "ADGroup.3.Name": "",
        "ADGroup.3.Privilege": 0,
        "ADGroup.4.Domain": "",
        "ADGroup.4.Name": "",
        "ADGroup.4.Privilege": 0,
        "ADGroup.5.Domain": "",
        "ADGroup.5.Name": "",
        "ADGroup.5.Privilege": 0,
        "ADGroup.6.Domain": "",
        "ADGroup.6.Name": "",
        "ADGroup.6.Privilege": 0,
        "ADGroup.7.Domain": "",
        "ADGroup.7.Name": "",
        "ADGroup.7.Privilege": 0,
        "ADGroup.8.Domain": "",
        "ADGroup.8.Name": "",
        "ADGroup.8.Privilege": 0,
        "ADGroup.9.Domain": "",
        "ADGroup.9.Name": "",
        "ADGroup.9.Privilege": 0,
        "ASRConfig.1.Enable": "Enabled",
        "ActiveDirectory.1.AuthTimeout": 120,
        "ActiveDirectory.1.CertValidationEnable": "Disabled",
        "ActiveDirectory.1.DCLookupByUserDomain": "Enabled",
        "ActiveDirectory.1.DCLookupDomainName": "",
        "ActiveDirectory.1.DCLookupEnable": "Disabled",
        "ActiveDirectory.1.DomainController1": "",
        "ActiveDirectory.1.DomainController2": "",
        "ActiveDirectory.1.DomainController3": "",
        "ActiveDirectory.1.Enable": "Disabled",
        "ActiveDirectory.1.GCLookupEnable": "Disabled",
        "ActiveDirectory.1.GCRootDomain": "",
        "ActiveDirectory.1.GlobalCatalog1": "",
        "ActiveDirectory.1.GlobalCatalog2": "",
        "ActiveDirectory.1.GlobalCatalog3": "",
        "ActiveDirectory.1.RacDomain": "",
        "ActiveDirectory.1.RacName": "",
        "ActiveDirectory.1.SSOEnable": "Disabled",
        "ActiveDirectory.1.Schema": "Extended Schema",
        "AutoOSLockGroup.1.AutoOSLockState": "Enabled",
        "Autodiscovery.1.EnableIPChangeAnnounce": "Enabled",
        "Autodiscovery.1.EnableIPChangeAnnounceFromDHCP": "Enabled",
        "Autodiscovery.1.EnableIPChangeAnnounceFromUnicastDNS": "Enabled",
        "Autodiscovery.1.EnableIPChangeAnnounceFrommDNS": "Enabled",
        "Autodiscovery.1.SendTestAnnouncement": "Disabled",
        "Autodiscovery.1.UnsolicitedIPChangeAnnounceRate": "1 day",
        "CurrentIPv4.1.Address": "10.44.182.90",
        "CurrentIPv4.1.DHCPEnable": "Disabled",
        "CurrentIPv4.1.DNS1": "0.0.0.0",
        "CurrentIPv4.1.DNS2": "0.0.0.0",
        "CurrentIPv4.1.DNSFromDHCP": "Disabled",
        "CurrentIPv4.1.DupAddrDetected": "0.0.0.0",
        "CurrentIPv4.1.Enable": "Enabled",
        "CurrentIPv4.1.Gateway": "10.29.152.1",
        "CurrentIPv4.1.Netmask": "255.255.255.0",
        "CurrentIPv6.1.Address1": "::",
        "CurrentIPv6.1.Address10": "::",
        "CurrentIPv6.1.Address11": "::",
        "CurrentIPv6.1.Address12": "::",
        "CurrentIPv6.1.Address13": "::",
        "CurrentIPv6.1.Address14": "::",
        "CurrentIPv6.1.Address15": "::",
        "CurrentIPv6.1.Address2": "::",
        "CurrentIPv6.1.Address3": "::",
        "CurrentIPv6.1.Address4": "::",
        "CurrentIPv6.1.Address5": "::",
        "CurrentIPv6.1.Address6": "::",
        "CurrentIPv6.1.Address7": "::",
        "CurrentIPv6.1.Address8": "::",
        "CurrentIPv6.1.Address9": "::",
        "CurrentIPv6.1.AddressGenerationMode": "StablePrivacy",
        "CurrentIPv6.1.AutoConfig": "Enabled",
        "CurrentIPv6.1.DHCPv6Address": "::",
        "CurrentIPv6.1.DNS1": "::",
        "CurrentIPv6.1.DNS2": "::",
        "CurrentIPv6.1.DNSFromDHCP6": "Disabled",
        "CurrentIPv6.1.DUID": "00:01:00:01:27:9b:cf:b4:b0:7b:25:d1:5a:5a",
        "CurrentIPv6.1.Enable": "Enabled",
        "CurrentIPv6.1.Gateway": "::",
        "CurrentIPv6.1.IPV6NumOfExtAddress": 0,
        "CurrentIPv6.1.LinkLocalAddress": "fe80::b29e:904d:cfe8:a0de",
        "CurrentIPv6.1.PrefixLength": 64,
        "CurrentNIC.1.ActiveNIC": "LOM3",
        "CurrentNIC.1.ActiveSharedLOM": "LOM3",
        "CurrentNIC.1.AutoDetect": "Disabled",
        "CurrentNIC.1.Autoneg": "Enabled",
        "CurrentNIC.1.DNSDomainFromDHCP": "Disabled",
        "CurrentNIC.1.DNSDomainName": "",
        "CurrentNIC.1.DNSRacName": "idrac-U8OIL5X",
        "CurrentNIC.1.DNSRegister": "Disabled",
        "CurrentNIC.1.DedicatedNICScanTime": 5,
        "CurrentNIC.1.Duplex": "Full",
        "CurrentNIC.1.Enable": "Enabled",
        "CurrentNIC.1.Failover": "LOM4",
        "CurrentNIC.1.LinkStatus": "Yes",
        "CurrentNIC.1.MACAddress": "b0:7b:25:d1:5a:5a",
        "CurrentNIC.1.MACAddress2": "b0:7b:25:d1:5a:5b",
        "CurrentNIC.1.MTU": 1500,
        "CurrentNIC.1.MgmtIfaceName": "bond0",
        "CurrentNIC.1.NumberOfLOM": 4,
        "CurrentNIC.1.PingEnable": "Enabled",
        "CurrentNIC.1.Selection": "LOM3",
        "CurrentNIC.1.SharedNICScanTime": 30,
        "CurrentNIC.1.Speed": "10000",
        "CurrentNIC.1.VLanEnable": "Disabled",
        "CurrentNIC.1.VLanID": 1,
        "CurrentNIC.1.VLanPriority": 0,
        "CurrentNIC.1.VLanSetting": "Both Enable",
        "DefaultCredentialMitigationConfigGroup.1.DefaultCredentialMitigation": "Disabled",
        "EmailAlert.1.Address": "",
        "EmailAlert.1.CustomMsg": "",
        "EmailAlert.1.Enable": "Disabled",
        "EmailAlert.2.Address": "",
        "EmailAlert.2.CustomMsg": "",
        "EmailAlert.2.Enable": "Disabled",
        "EmailAlert.3.Address": "",
        "EmailAlert.3.CustomMsg": "",
        "EmailAlert.3.Enable": "Disabled",
        "EmailAlert.4.Address": "",
        "EmailAlert.4.CustomMsg": "",
        "EmailAlert.4.Enable": "Disabled",
        "GUI.1.SecurityPolicyMessage": "By accessing this computer, you confirm that such access complies with your organization's security policy.",
        "GroupManager.1.GroupName": "",
        "GroupManager.1.GroupUUID": "",
        "GroupManager.1.Status": "Disabled",
        "IOIDOpt.1.IOIDOptEnable": "Disabled",
        "IOIDOpt.1.InitiatorPersistencePolicy": "WarmReset, ColdReset, ACPowerLoss",
        "IOIDOpt.1.PersistencePolicyOnPartReplacement": "Enabled",
        "IOIDOpt.1.StorageTargetPersistencePolicy": "WarmReset, ColdReset, ACPowerLoss",
        "IOIDOpt.1.VirtualAddressPersistencePolicyAuxPwrd": "WarmReset, ColdReset",
        "IOIDOpt.1.VirtualAddressPersistencePolicyNonAuxPwrd": "WarmReset",
        "IPBlocking.1.BlockEnable": "Enabled",
        "IPBlocking.1.FailCount": 3,
        "IPBlocking.1.FailWindow": 60,
        "IPBlocking.1.PenaltyTime": 60,
        "IPBlocking.1.RangeAddr": "192.168.1.1",
        "IPBlocking.1.RangeAddr2": "192.168.1.1",
        "IPBlocking.1.RangeAddr3": "192.168.1.1",
        "IPBlocking.1.RangeAddr4": "192.168.1.1",
        "IPBlocking.1.RangeAddr5": "192.168.1.1",
        "IPBlocking.1.RangeEnable": "Disabled",
        "IPBlocking.1.RangeEnable2": "Disabled",
        "IPBlocking.1.RangeEnable3": "Disabled",
        "IPBlocking.1.RangeEnable4": "Disabled",
        "IPBlocking.1.RangeEnable5": "Disabled",
        "IPBlocking.1.RangeMask": "255.255.255.0",
        "IPBlocking.1.RangeMask2": "255.255.255.0",
        "IPBlocking.1.RangeMask3": "255.255.255.0",
        "IPBlocking.1.RangeMask4": "255.255.255.0",
        "IPBlocking.1.RangeMask5": "255.255.255.0",
        "IPMILan.1.AlertEnable": "Disabled",
        "IPMILan.1.CommunityName": "public",
        "IPMILan.1.Enable": "Enabled",
        "IPMILan.1.EncryptionKey": "0000000000000000000000000000000000000000",
        "IPMILan.1.PrivLimit": "Administrator",
        "IPMISOL.1.AccumulateInterval": 10,
        "IPMISOL.1.BaudRate": "115200",
        "IPMISOL.1.Enable": "Enabled",
        "IPMISOL.1.MinPrivilege": "Administrator",
        "IPMISOL.1.SendThreshold": 255,
        "IPMISerial.1.BaudRate": "57600",
        "IPMISerial.1.ChanPrivLimit": "Administrator",
        "IPMISerial.1.ConnectionMode": "Basic",
        "IPMISerial.1.DeleteControl": "Disabled",
        "IPMISerial.1.EchoControl": "Enabled",
        "IPMISerial.1.FlowControl": "RTS/CTS",
        "IPMISerial.1.HandshakeControl": "Enabled",
        "IPMISerial.1.InputNewLineSeq": "Enter",
        "IPMISerial.1.LineEdit": "Enabled",
        "IPMISerial.1.NewLineSeq": "CR-LF",
        "IPv4.1.Address": "10.44.182.90",
        "IPv4.1.DHCPEnable": "Disabled",
        "IPv4.1.DNS1": "0.0.0.0",
        "IPv4.1.DNS2": "0.0.0.0",
        "IPv4.1.DNSFromDHCP": "Disabled",
        "IPv4.1.Enable": "Enabled",
        "IPv4.1.Gateway": "10.29.152.1",
        "IPv4.1.Netmask": "255.255.255.0",
        "IPv4Static.1.Address": "10.44.182.90",
        "IPv4Static.1.DNS1": "0.0.0.0",
        "IPv4Static.1.DNS2": "0.0.0.0",
        "IPv4Static.1.DNSFromDHCP": "Disabled",
        "IPv4Static.1.Gateway": "10.29.152.1",
        "IPv4Static.1.Netmask": "255.255.255.0",
        "IPv6.1.Address1": "::",
        "IPv6.1.Address10": "::",
        "IPv6.1.Address11": "::",
        "IPv6.1.Address12": "::",
        "IPv6.1.Address13": "::",
        "IPv6.1.Address14": "::",
        "IPv6.1.Address15": "::",
        "IPv6.1.Address2": "::",
        "IPv6.1.Address3": "::",
        "IPv6.1.Address4": "::",
        "IPv6.1.Address5": "::",
        "IPv6.1.Address6": "::",
        "IPv6.1.Address7": "::",
        "IPv6.1.Address8": "::",
        "IPv6.1.Address9": "::",
        "IPv6.1.AddressGenerationMode": "StablePrivacy",
        "IPv6.1.AddressState": "Active",
        "IPv6.1.AutoConfig": "Enabled",
        "IPv6.1.DNS1": "::",
        "IPv6.1.DNS2": "::",
        "IPv6.1.DNSFromDHCP6": "Disabled",
        "IPv6.1.DUID": "00:01:00:01:27:9b:cf:b4:b0:7b:25:d1:5a:5a",
        "IPv6.1.Enable": "Enabled",
        "IPv6.1.Gateway": "::",
        "IPv6.1.LinkLocalAddress": "fe80::b29e:904d:cfe8:a0de",
        "IPv6.1.PrefixLength": 64,
        "IPv6Static.1.Address1": "::",
        "IPv6Static.1.DNS1": "::",
        "IPv6Static.1.DNS2": "::",
        "IPv6Static.1.DNSFromDHCP6": "Disabled",
        "IPv6Static.1.Gateway": "::",
        "IPv6Static.1.PrefixLength": 64,
        "IPv6URL.1.URL": "",
        "Info.1.Build": "57",
        "Info.1.CPLDVersion": "1.0.5",
        "Info.1.Description": "This system component provides a complete set of remote management functions for Dell PowerEdge Servers",
        "Info.1.HWRev": "0.01",
        "Info.1.IPMIVersion": "2.0",
        "Info.1.Name": "iDRAC",
        "Info.1.Product": "Integrated Dell Remote Access Controller",
        "Info.1.RollbackBuild": "04",
        "Info.1.RollbackVersion": "5.00.20.10",
        "Info.1.ServerGen": "15G",
        "Info.1.Type": "15G Monolithic",
        "Info.1.Version": "5.10.00.00",
        "IntegratedDatacenter.1.DiscoveryEnable": "Disabled",
        "InventoryHash.1.HashCalculationInterval": 15,
        "InventoryHash.1.SystemConfigHash": "f9b98fde62b656e1f620a0309d04cd9192c27d192b42ad77701576dd28c87d7f",
        "LDAP.1.BaseDN": "",
        "LDAP.1.BindDN": "",
        "LDAP.1.BindPassword": null,
        "LDAP.1.CertValidationEnable": "Enabled",
        "LDAP.1.Enable": "Disabled",
        "LDAP.1.GroupAttribute": "",
        "LDAP.1.GroupAttributeIsDN": "Enabled",
        "LDAP.1.Port": 636,
        "LDAP.1.SearchFilter": "",
        "LDAP.1.Server": "",
        "LDAP.1.UserAttribute": "",
        "LDAPRoleGroup.1.DN": "",
        "LDAPRoleGroup.1.Privilege": 0,
        "LDAPRoleGroup.10.DN": "",
        "LDAPRoleGroup.10.Privilege": 0,
        "LDAPRoleGroup.11.DN": "",
        "LDAPRoleGroup.11.Privilege": 0,
        "LDAPRoleGroup.12.DN": "",
        "LDAPRoleGroup.12.Privilege": 0,
        "LDAPRoleGroup.13.DN": "",
        "LDAPRoleGroup.13.Privilege": 0,
        "LDAPRoleGroup.14.DN": "",
        "LDAPRoleGroup.14.Privilege": 0,
        "LDAPRoleGroup.15.DN": "",
        "LDAPRoleGroup.15.Privilege": 0,
        "LDAPRoleGroup.2.DN": "",
        "LDAPRoleGroup.2.Privilege": 0,
        "LDAPRoleGroup.3.DN": "",
        "LDAPRoleGroup.3.Privilege": 0,
        "LDAPRoleGroup.4.DN": "",
        "LDAPRoleGroup.4.Privilege": 0,
        "LDAPRoleGroup.5.DN": "",
        "LDAPRoleGroup.5.Privilege": 0,
        "LDAPRoleGroup.6.DN": "",
        "LDAPRoleGroup.6.Privilege": 0,
        "LDAPRoleGroup.7.DN": "",
        "LDAPRoleGroup.7.Privilege": 0,
        "LDAPRoleGroup.8.DN": "",
        "LDAPRoleGroup.8.Privilege": 0,
        "LDAPRoleGroup.9.DN": "",
        "LDAPRoleGroup.9.Privilege": 0,
        "LocalSecurity.1.LocalConfig": "Disabled",
        "LocalSecurity.1.PrebootConfig": "Disabled",
        "Lockdown.1.SystemLockdown": "Disabled",
        "Logging.1.SELBufferType": "Circular",
        "Logging.1.SELOEMEventFilterEnable": "Disabled",
        "NIC.1.AutoConfig": "Disabled",
        "NIC.1.AutoDetect": "Disabled",
        "NIC.1.Autoneg": "Enabled",
        "NIC.1.DNSDomainFromDHCP": "Disabled",
        "NIC.1.DNSDomainName": "",
        "NIC.1.DNSDomainNameFromDHCP": "Disabled",
        "NIC.1.DNSRacName": "idrac-U8OIL5X",
        "NIC.1.DNSRegister": "Disabled",
        "NIC.1.DNSRegisterInterval": 0,
        "NIC.1.DedicatedNICScanTime": 5,
        "NIC.1.DiscoveryLLDP": "Disabled",
        "NIC.1.Duplex": "Full",
        "NIC.1.Enable": "Enabled",
        "NIC.1.Failover": "LOM4",
        "NIC.1.MACAddress": "b0:7b:25:d1:5a:5a",
        "NIC.1.MTU": 1500,
        "NIC.1.PingEnable": "Enabled",
        "NIC.1.PowerOnOCPSlot1InS5": "Off",
        "NIC.1.Selection": "LOM3",
        "NIC.1.SharedNICScanTime": 30,
        "NIC.1.Speed": "10000",
        "NIC.1.SwitchConnection": "bc:26:c7:cf:ae:94",
        "NIC.1.SwitchPortConnection": "Ethernet1/23",
        "NIC.1.TopologyLldp": "Disabled",
        "NIC.1.VLanEnable": "Disabled",
        "NIC.1.VLanID": 1,
        "NIC.1.VLanPort": "Both",
        "NIC.1.VLanPriority": 0,
        "NICStatic.1.DNSDomainFromDHCP": "Disabled",
        "NICStatic.1.DNSDomainName": "",
        "NTPConfigGroup.1.NTP1": "",
        "NTPConfigGroup.1.NTP1SecurityKey": null,
        "NTPConfigGroup.1.NTP1SecurityKeyNumber": 1,
        "NTPConfigGroup.1.NTP1SecurityType": "Disabled",
        "NTPConfigGroup.1.NTP2": "",
        "NTPConfigGroup.1.NTP2SecurityKey": null,
        "NTPConfigGroup.1.NTP2SecurityKeyNumber": 1,
        "NTPConfigGroup.1.NTP2SecurityType": "Disabled",
        "NTPConfigGroup.1.NTP3": "",
        "NTPConfigGroup.1.NTP3SecurityKey": null,
        "NTPConfigGroup.1.NTP3SecurityKeyNumber": 1,
        "NTPConfigGroup.1.NTP3SecurityType": "Disabled",
        "NTPConfigGroup.1.NTPEnable": "Disabled",
        "NTPConfigGroup.1.NTPMaxDist": 16,
        "OS-BMC.1.AdminState": "Disabled",
        "OS-BMC.1.OsIpAddress": "0.0.0.0",
        "OS-BMC.1.PTCapability": "Capable",
        "OS-BMC.1.PTMode": "usb-p2p",
        "OS-BMC.1.UsbNicIpAddress": "169.254.1.1",
        "OS-BMC.1.UsbNicIpV6Address": "::",
        "OS-BMC.1.UsbNicIpv4AddressSupport": "Enabled",
        "OS-BMC.1.UsbNicULA": "fde1:53ba:e9a0:de11::1",
        "PCIeVDM.1.Enable": "Enabled",
        "PlatformCapability.1.ASHRAECapable": "Enabled",
        "PlatformCapability.1.BackupRestoreCapable": "Disabled",
        "PlatformCapability.1.CUPSCapable": "Enabled",
        "PlatformCapability.1.FrontPanelCapable": "Enabled",
        "PlatformCapability.1.FrontPanelUSBCapable": "Enabled",
        "PlatformCapability.1.FrontPortUSBConfiguration": "Disabled",
        "PlatformCapability.1.GridCurrentCapCapable": "Enabled",
        "PlatformCapability.1.LCDCapable": "Enabled",
        "PlatformCapability.1.LiveScanCapable": "Enabled",
        "PlatformCapability.1.NicVLANCapable": "Both",
        "PlatformCapability.1.PMBUSCapablePSU": "Enabled",
        "PlatformCapability.1.PowerBudgetCapable": "Enabled",
        "PlatformCapability.1.PowerMonitoringCapable": "Enabled",
        "PlatformCapability.1.SerialDB9PCapable": "Disabled",
        "PlatformCapability.1.ServerAllocationCapable": "Disabled",
        "PlatformCapability.1.SystemCurrentCapCapable": "Enabled",
        "PlatformCapability.1.UserPowerCapBoundCapable": "Enabled",
        "PlatformCapability.1.UserPowerCapCapable": "Enabled",
        "PlatformCapability.1.WiFiCapable": "Enabled",
        "PlatformCapability.1.vFlashCapable": "Disabled",
        "RFS.1.AttachMode": "Auto Attach",
        "RFS.1.Enable": "Disabled",
        "RFS.1.IgnoreCertWarning": "Yes",
        "RFS.1.Image": "",
        "RFS.1.MediaAttachState": "Detached",
        "RFS.1.Password": null,
        "RFS.1.Status": "Done",
        "RFS.1.User": "",
        "RFS.1.WriteProtected": "Read Only",
        "Racadm.1.Enable": "Enabled",
        "Racadm.1.MaxSessions": 2,
        "Racadm.1.Timeout": 60,
        "Redfish.1.Enable": "Enabled",
        "RedfishEventing.1.DeliveryRetryAttempts": 5,
        "RedfishEventing.1.DeliveryRetryIntervalInSeconds": 60,
        "RedfishEventing.1.IgnoreCertificateErrors": "Yes",
        "RemoteHosts.1.ConnectionEncryption": "STARTTLS",
        "RemoteHosts.1.MessageSubjectPrefix": "",
        "RemoteHosts.1.SMTPAuthentication": "Disabled",
        "RemoteHosts.1.SMTPPassword": null,
        "RemoteHosts.1.SMTPPort": 25,
        "RemoteHosts.1.SMTPServerIPAddress": "0.0.0.0",
        "RemoteHosts.1.SMTPUserName": "",
        "RemoteHosts.1.SenderEmail": "",
        "SEKM.1.SupportStatus": "NotInstalled",
        "SNMP.1.AgentCommunity": "public",
        "SNMP.1.AgentEnable": "Enabled",
        "SNMP.1.AlertPort": 162,
        "SNMP.1.DiscoveryPort": 161,
        "SNMP.1.EngineID": "0x80001f880431344438464633",
        "SNMP.1.SNMPProtocol": "All",
        "SNMP.1.TrapFormat": "SNMPv1",
        "SNMPAlert.1.Destination": "",
        "SNMPAlert.1.SNMPv3UserID": 0,
        "SNMPAlert.1.SNMPv3Username": "",
        "SNMPAlert.1.State": "Disabled",
        "SNMPAlert.2.Destination": "",
        "SNMPAlert.2.SNMPv3UserID": 0,
        "SNMPAlert.2.SNMPv3Username": "",
        "SNMPAlert.2.State": "Disabled",
        "SNMPAlert.3.Destination": "",
        "SNMPAlert.3.SNMPv3UserID": 0,
        "SNMPAlert.3.SNMPv3Username": "",
        "SNMPAlert.3.State": "Disabled",
        "SNMPAlert.4.Destination": "",
        "SNMPAlert.4.SNMPv3UserID": 0,
        "SNMPAlert.4.SNMPv3Username": "",
        "SNMPAlert.4.State": "Disabled",
        "SNMPAlert.5.Destination": "",
        "SNMPAlert.5.SNMPv3UserID": 0,
        "SNMPAlert.5.SNMPv3Username": "",
        "SNMPAlert.5.State": "Disabled",
        "SNMPAlert.6.Destination": "",
        "SNMPAlert.6.SNMPv3UserID": 0,
        "SNMPAlert.6.SNMPv3Username": "",
        "SNMPAlert.6.State": "Disabled",
        "SNMPAlert.7.Destination": "",
        "SNMPAlert.7.SNMPv3UserID": 0,
        "SNMPAlert.7.SNMPv3Username": "",
        "SNMPAlert.7.State": "Disabled",
        "SNMPAlert.8.Destination": "",
        "SNMPAlert.8.SNMPv3UserID": 0,
        "SNMPAlert.8.SNMPv3Username": "",
        "SNMPAlert.8.State": "Disabled",
        "SNMPTrapIPv4.1.DestIPv4Addr": "0.0.0.0",
        "SNMPTrapIPv4.1.DestinationNum": 1,
        "SNMPTrapIPv4.1.State": "Disabled",
        "SNMPTrapIPv4.2.DestIPv4Addr": "0.0.0.0",
        "SNMPTrapIPv4.2.DestinationNum": 1,
        "SNMPTrapIPv4.2.State": "Disabled",
        "SNMPTrapIPv4.3.DestIPv4Addr": "0.0.0.0",
        "SNMPTrapIPv4.3.DestinationNum": 1,
        "SNMPTrapIPv4.3.State": "Disabled",
        "SNMPTrapIPv4.4.DestIPv4Addr": "0.0.0.0",
        "SNMPTrapIPv4.4.DestinationNum": 1,
        "SNMPTrapIPv4.4.State": "Disabled",
        "SNMPTrapIPv6.1.DestIPv6Addr": "::",
        "SNMPTrapIPv6.1.DestinationNum": 1,
        "SNMPTrapIPv6.1.State": "Disabled",
        "SNMPTrapIPv6.2.DestIPv6Addr": "::",
        "SNMPTrapIPv6.2.DestinationNum": 1,
        "SNMPTrapIPv6.2.State": "Disabled",
        "SNMPTrapIPv6.3.DestIPv6Addr": "::",
        "SNMPTrapIPv6.3.DestinationNum": 1,
        "SNMPTrapIPv6.3.State": "Disabled",
        "SSH.1.Banner": "",
        "SSH.1.Enable": "Enabled",
        "SSH.1.MaxSessions": 4,
        "SSH.1.Port": 22,
        "SSH.1.Timeout": 1800,
        "SSHCrypto.1.Ciphers": "chacha20-poly1305@openssh.com,aes128-ctr,aes192-ctr,aes256-ctr,aes128-gcm@openssh.com,aes256-gcm@openssh.com",
        "SSHCrypto.1.HostKeyAlgorithms": "ssh-rsa,rsa-sha2-512,rsa-sha2-256,ecdsa-sha2-nistp256,ssh-ed25519",
        "SSHCrypto.1.KexAlgorithms": "curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group14-sha256",
        "SSHCrypto.1.MACs": "umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,umac-128@openssh.com,hmac-sha2-256,hmac-sha2-512",
        "SecureDefaultPassword.1.ForceChangePassword": "False",
        "Security.1.CsrCommonName": "",
        "Security.1.CsrCountryCode": "US",
        "Security.1.CsrEmailAddr": "",
        "Security.1.CsrKeySize": "2048",
        "Security.1.CsrLocalityName": "",
        "Security.1.CsrOrganizationName": "",
        "Security.1.CsrOrganizationUnit": "",
        "Security.1.CsrStateName": "",
        "Security.1.CsrSubjectAltName": "",
        "Security.1.FIPSMode": "Disabled",
        "Security.1.FIPSVersion": "DELL OpenSSL FIPS Crypto Module v2.6",
        "Security.1.MinimumPasswordScore": "Weak Protection",
        "Security.1.PasswordMinimumLength": 0,
        "Security.1.PasswordRequireNumbers": "Disabled",
        "Security.1.PasswordRequireRegex": "",
        "Security.1.PasswordRequireSymbols": "Disabled",
        "Security.1.PasswordRequireUpperCase": "Disabled",
        "SecurityCertificate.1.CertValidFrom": "Jan 20 05:38:00 2021 GMT",
        "SecurityCertificate.1.CertValidTo": "Jan 21 05:38:00 2031 GMT",
        "SecurityCertificate.1.CertificateInstance": 1,
        "SecurityCertificate.1.CertificateType": "WEBSERVER_SSL",
        "SecurityCertificate.1.IssuerCommonName": "idrac-SVCTAG",
        "SecurityCertificate.1.IssuerCountryCode": "US",
        "SecurityCertificate.1.IssuerLocality": "Round Rock",
        "SecurityCertificate.1.IssuerOrganization": "Dell Inc.",
        "SecurityCertificate.1.IssuerOrganizationalUnit": "Remote Access Group",
        "SecurityCertificate.1.IssuerState": "Texas",
        "SecurityCertificate.1.SerialNumber": "821EF8AFC0CD599E",
        "SecurityCertificate.1.SubjectCommonName": "idrac-SVCTAG",
        "SecurityCertificate.1.SubjectCountryCode": "US",
        "SecurityCertificate.1.SubjectLocality": "Round Rock",
        "SecurityCertificate.1.SubjectOrganization": "Dell Inc.",
        "SecurityCertificate.1.SubjectOrganizationalUnit": "Remote Access Group",
        "SecurityCertificate.1.SubjectState": "Texas",
        "SecurityCertificate.2.CertValidFrom": "Apr  1 05:20:12 2021 GMT",
        "SecurityCertificate.2.CertValidTo": "May 31 05:20:12 2040 GMT",
        "SecurityCertificate.2.CertificateInstance": 1,
        "SecurityCertificate.2.CertificateType": "FACTORY_IDENTITY_CERT",
        "SecurityCertificate.2.IssuerCommonName": "0IVC00-CE0C-105E-6826",
        "SecurityCertificate.2.IssuerCountryCode": "CN",
        "SecurityCertificate.2.IssuerLocality": "Shanghai",
        "SecurityCertificate.2.IssuerOrganization": "Inventec",
        "SecurityCertificate.2.IssuerOrganizationalUnit": "PROD",
        "SecurityCertificate.2.IssuerState": "Shanghai",
        "SecurityCertificate.2.SerialNumber": "03000000002328E5",
        "SecurityCertificate.2.SubjectCommonName": "b0:7b:25:d1:5a:5a",
        "SecurityCertificate.2.SubjectCountryCode": "US",
        "SecurityCertificate.2.SubjectLocality": "Round Rock",
        "SecurityCertificate.2.SubjectOrganization": "Dell EMC",
        "SecurityCertificate.2.SubjectOrganizationalUnit": "IDRAC",
        "SecurityCertificate.2.SubjectState": "Texas",
        "Serial.1.BaudRate": "57600",
        "Serial.1.Command": "",
        "Serial.1.Enable": "Enabled",
        "Serial.1.FlowControl": "None",
        "Serial.1.HistorySize": 8192,
        "Serial.1.IdleTimeout": 300,
        "Serial.1.NoAuth": "Disabled",
        "SerialRedirection.1.Enable": "Enabled",
        "SerialRedirection.1.QuitKey": "^\\",
        "ServerBoot.1.BootOnce": "Enabled",
        "ServerBoot.1.FirstBootDevice": "Normal",
        "ServiceModule.1.ChipsetSATASupported": "Enabled",
        "ServiceModule.1.HostSNMPAlert": "Disabled",
        "ServiceModule.1.HostSNMPGet": "Disabled",
        "ServiceModule.1.HostSNMPOMSAAlert": "Disabled",
        "ServiceModule.1.LCLReplication": "Disabled",
        "ServiceModule.1.OMSAPresence": "NA",
        "ServiceModule.1.OSInfo": "Enabled",
        "ServiceModule.1.SSEventCorrelation": "Enabled",
        "ServiceModule.1.ServiceModuleEnable": "Enabled",
        "ServiceModule.1.ServiceModuleState": "Not Running",
        "ServiceModule.1.ServiceModuleVersion": "NA",
        "ServiceModule.1.WMIInfo": "Disabled",
        "ServiceModule.1.WatchdogRecoveryAction": "None",
        "ServiceModule.1.WatchdogResetTime": 480,
        "ServiceModule.1.WatchdogState": "Disabled",
        "ServiceModule.1.iDRACHardReset": "Enabled",
        "ServiceModule.1.iDRACSSOLauncher": "Enabled",
        "SmartCard.1.SmartCardCRLEnable": "Disabled",
        "SmartCard.1.SmartCardLogonEnable": "Disabled",
        "SupportAssist.1.DefaultIPAddress": "",
        "SupportAssist.1.DefaultPassword": null,
        "SupportAssist.1.DefaultProtocol": "CIFS",
        "SupportAssist.1.DefaultProtocolPort": 0,
        "SupportAssist.1.DefaultShareName": "",
        "SupportAssist.1.DefaultUserName": "",
        "SupportAssist.1.DefaultWorkgroupName": "",
        "SupportAssist.1.EmailOptIn": "Yes",
        "SupportAssist.1.EventBasedAutoCollection": "Disabled",
        "SupportAssist.1.FilterAutoCollections": "No",
        "SupportAssist.1.HostOSProxyAddress": "",
        "SupportAssist.1.HostOSProxyConfigured": "No",
        "SupportAssist.1.HostOSProxyPassword": null,
        "SupportAssist.1.HostOSProxyPort": 1,
        "SupportAssist.1.HostOSProxyUserName": "",
        "SupportAssist.1.NativeOSLogsCollectionSupported": "None",
        "SupportAssist.1.PreferredLanguage": "English",
        "SupportAssist.1.ProSupportPlusRecommendationsReport": "Disabled",
        "SupportAssist.1.RegistrationID": "",
        "SupportAssist.1.RequestTechnicianForPartsDispatch": "No",
        "SupportAssist.1.SupportAssistEnableState": "Disabled",
        "SupportAssist.1.iDRACFirstPowerUpDateTime": "Thu Jul 15 01:52:17 GMT 2021",
        "SwitchConnectionView.1.Enable": "Enabled",
        "SysInfo.1.LocalConsoleLockOut": 1,
        "SysInfo.1.POSTCode": 126,
        "SysInfo.1.SystemRev": 0,
        "SysLog.1.Port": 514,
        "SysLog.1.PowerLogEnable": "Disabled",
        "SysLog.1.PowerLogInterval": 5,
        "SysLog.1.Server1": "",
        "SysLog.1.Server2": "",
        "SysLog.1.Server3": "",
        "SysLog.1.SysLogEnable": "Disabled",
        "Telemetry.1.EnableTelemetry": "Enabled",
        "Time.1.DayLightOffset": 0,
        "Time.1.TimeZoneOffset": 0,
        "Time.1.Timezone": "CST6CDT",
        "USB.1.ConfigurationXML": "Enabled while server has default credential settings only",
        "USB.1.ManagementPortMode": "iDRAC Direct Only",
        "USB.1.PortStatus": "Enabled",
        "USB.1.ZipPassword": null,
        "Update.1.FwUpdateIPAddr": "0.0.0.0",
        "Update.1.FwUpdatePath": "",
        "Update.1.FwUpdateTFTPEnable": "Enabled",
        "UserDomain.1.Name": "",
        "UserDomain.10.Name": "",
        "UserDomain.11.Name": "",
        "UserDomain.12.Name": "",
        "UserDomain.13.Name": "",
        "UserDomain.14.Name": "",
        "UserDomain.15.Name": "",
        "UserDomain.16.Name": "",
        "UserDomain.17.Name": "",
        "UserDomain.18.Name": "",
        "UserDomain.19.Name": "",
        "UserDomain.2.Name": "",
        "UserDomain.20.Name": "",
        "UserDomain.21.Name": "",
        "UserDomain.22.Name": "",
        "UserDomain.23.Name": "",
        "UserDomain.24.Name": "",
        "UserDomain.25.Name": "",
        "UserDomain.26.Name": "",
        "UserDomain.27.Name": "",
        "UserDomain.28.Name": "",
        "UserDomain.29.Name": "",
        "UserDomain.3.Name": "",
        "UserDomain.30.Name": "",
        "UserDomain.31.Name": "",
        "UserDomain.32.Name": "",
        "UserDomain.33.Name": "",
        "UserDomain.34.Name": "",
        "UserDomain.35.Name": "",
        "UserDomain.36.Name": "",
        "UserDomain.37.Name": "",
        "UserDomain.38.Name": "",
        "UserDomain.39.Name": "",
        "UserDomain.4.Name": "",
        "UserDomain.40.Name": "",
        "UserDomain.5.Name": "",
        "UserDomain.6.Name": "",
        "UserDomain.7.Name": "",
        "UserDomain.8.Name": "",
        "UserDomain.9.Name": "",
        "Users.1.AuthenticationProtocol": "SHA",
        "Users.1.EmailAddress": "",
        "Users.1.Enable": "Disabled",
        "Users.1.IpmiLanPrivilege": "No Access",
        "Users.1.IpmiSerialPrivilege": "No Access",
        "Users.1.Password": null,
        "Users.1.PrivacyProtocol": "AES",
        "Users.1.Privilege": 0,
        "Users.1.ProtocolEnable": "Disabled",
        "Users.1.SMSNumber": "",
        "Users.1.Simple2FA": "Disabled",
        "Users.1.SolEnable": "Disabled",
        "Users.1.UseEmail": "Disabled",
        "Users.1.UseSMS": "Disabled",
        "Users.1.UserName": "",
        "Users.10.AuthenticationProtocol": "SHA",
        "Users.10.EmailAddress": "",
        "Users.10.Enable": "Disabled",
        "Users.10.IpmiLanPrivilege": "No Access",
        "Users.10.IpmiSerialPrivilege": "No Access",
        "Users.10.Password": null,
        "Users.10.PrivacyProtocol": "AES",
        "Users.10.Privilege": 0,
        "Users.10.ProtocolEnable": "Disabled",
        "Users.10.SMSNumber": "",
        "Users.10.Simple2FA": "Disabled",
        "Users.10.SolEnable": "Disabled",
        "Users.10.UseEmail": "Disabled",
        "Users.10.UseSMS": "Disabled",
        "Users.10.UserName": "",
        "Users.11.AuthenticationProtocol": "SHA",
        "Users.11.EmailAddress": "",
        "Users.11.Enable": "Disabled",
        "Users.11.IpmiLanPrivilege": "No Access",
        "Users.11.IpmiSerialPrivilege": "No Access",
        "Users.11.Password": null,
        "Users.11.PrivacyProtocol": "AES",
        "Users.11.Privilege": 0,
        "Users.11.ProtocolEnable": "Disabled",
        "Users.11.SMSNumber": "",
        "Users.11.Simple2FA": "Disabled",
        "Users.11.SolEnable": "Disabled",
        "Users.11.UseEmail": "Disabled",
        "Users.11.UseSMS": "Disabled",
        "Users.11.UserName": "",
        "Users.12.AuthenticationProtocol": "SHA",
        "Users.12.EmailAddress": "",
        "Users.12.Enable": "Disabled",
        "Users.12.IpmiLanPrivilege": "No Access",
        "Users.12.IpmiSerialPrivilege": "No Access",
        "Users.12.Password": null,
        "Users.12.PrivacyProtocol": "AES",
        "Users.12.Privilege": 0,
        "Users.12.ProtocolEnable": "Disabled",
        "Users.12.SMSNumber": "",
        "Users.12.Simple2FA": "Disabled",
        "Users.12.SolEnable": "Disabled",
        "Users.12.UseEmail": "Disabled",
        "Users.12.UseSMS": "Disabled",
        "Users.12.UserName": "",
        "Users.13.AuthenticationProtocol": "SHA",
        "Users.13.EmailAddress": "",
        "Users.13.Enable": "Disabled",
        "Users.13.IpmiLanPrivilege": "No Access",
        "Users.13.IpmiSerialPrivilege": "No Access",
        "Users.13.Password": null,
        "Users.13.PrivacyProtocol": "AES",
        "Users.13.Privilege": 0,
        "Users.13.ProtocolEnable": "Disabled",
        "Users.13.SMSNumber": "",
        "Users.13.Simple2FA": "Disabled",
        "Users.13.SolEnable": "Disabled",
        "Users.13.UseEmail": "Disabled",
        "Users.13.UseSMS": "Disabled",
        "Users.13.UserName": "",
        "Users.14.AuthenticationProtocol": "SHA",
        "Users.14.EmailAddress": "",
        "Users.14.Enable": "Disabled",
        "Users.14.IpmiLanPrivilege": "No Access",
        "Users.14.IpmiSerialPrivilege": "No Access",
        "Users.14.Password": null,
        "Users.14.PrivacyProtocol": "AES",
        "Users.14.Privilege": 0,
        "Users.14.ProtocolEnable": "Disabled",
        "Users.14.SMSNumber": "",
        "Users.14.Simple2FA": "Disabled",
        "Users.14.SolEnable": "Disabled",
        "Users.14.UseEmail": "Disabled",
        "Users.14.UseSMS": "Disabled",
        "Users.14.UserName": "",
        "Users.15.AuthenticationProtocol": "SHA",
        "Users.15.EmailAddress": "",
        "Users.15.Enable": "Disabled",
        "Users.15.IpmiLanPrivilege": "No Access",
        "Users.15.IpmiSerialPrivilege": "No Access",
        "Users.15.Password": null,
        "Users.15.PrivacyProtocol": "AES",
        "Users.15.Privilege": 0,
        "Users.15.ProtocolEnable": "Disabled",
        "Users.15.SMSNumber": "",
        "Users.15.Simple2FA": "Disabled",
        "Users.15.SolEnable": "Disabled",
        "Users.15.UseEmail": "Disabled",
        "Users.15.UseSMS": "Disabled",
        "Users.15.UserName": "",
        "Users.16.AuthenticationProtocol": "SHA",
        "Users.16.EmailAddress": "",
        "Users.16.Enable": "Disabled",
        "Users.16.IpmiLanPrivilege": "No Access",
        "Users.16.IpmiSerialPrivilege": "No Access",
        "Users.16.Password": null,
        "Users.16.PrivacyProtocol": "AES",
        "Users.16.Privilege": 0,
        "Users.16.ProtocolEnable": "Disabled",
        "Users.16.SMSNumber": "",
        "Users.16.Simple2FA": "Disabled",
        "Users.16.SolEnable": "Disabled",
        "Users.16.UseEmail": "Disabled",
        "Users.16.UseSMS": "Disabled",
        "Users.16.UserName": "",
        "Users.2.AuthenticationProtocol": "SHA",
        "Users.2.EmailAddress": "",
        "Users.2.Enable": "Enabled",
        "Users.2.IpmiLanPrivilege": "Administrator",
        "Users.2.IpmiSerialPrivilege": "Administrator",
        "Users.2.Password": null,
        "Users.2.PrivacyProtocol": "AES",
        "Users.2.Privilege": 511,
        "Users.2.ProtocolEnable": "Disabled",
        "Users.2.SMSNumber": "",
        "Users.2.Simple2FA": "Disabled",
        "Users.2.SolEnable": "Enabled",
        "Users.2.UseEmail": "Disabled",
        "Users.2.UseSMS": "Disabled",
        "Users.2.UserName": "root",
        "Users.3.AuthenticationProtocol": "SHA",
        "Users.3.EmailAddress": "",
        "Users.3.Enable": "Enabled",
        "Users.3.IpmiLanPrivilege": "No Access",
        "Users.3.IpmiSerialPrivilege": "No Access",
        "Users.3.Password": null,
        "Users.3.PrivacyProtocol": "AES",
        "Users.3.Privilege": 511,
        "Users.3.ProtocolEnable": "Disabled",
        "Users.3.SMSNumber": "",
        "Users.3.Simple2FA": "Disabled",
        "Users.3.SolEnable": "Disabled",
        "Users.3.UseEmail": "Disabled",
        "Users.3.UseSMS": "Disabled",
        "Users.3.UserName": "complab",
        "Users.4.AuthenticationProtocol": "SHA",
        "Users.4.EmailAddress": "",
        "Users.4.Enable": "Enabled",
        "Users.4.IpmiLanPrivilege": "No Access",
        "Users.4.IpmiSerialPrivilege": "No Access",
        "Users.4.Password": null,
        "Users.4.PrivacyProtocol": "AES",
        "Users.4.Privilege": 1,
        "Users.4.ProtocolEnable": "Disabled",
        "Users.4.SMSNumber": "",
        "Users.4.Simple2FA": "Disabled",
        "Users.4.SolEnable": "Disabled",
        "Users.4.UseEmail": "Disabled",
        "Users.4.UseSMS": "Disabled",
        "Users.4.UserName": "engineer",
        "Users.5.AuthenticationProtocol": "SHA",
        "Users.5.EmailAddress": "",
        "Users.5.Enable": "Disabled",
        "Users.5.IpmiLanPrivilege": "No Access",
        "Users.5.IpmiSerialPrivilege": "No Access",
        "Users.5.Password": null,
        "Users.5.PrivacyProtocol": "AES",
        "Users.5.Privilege": 0,
        "Users.5.ProtocolEnable": "Disabled",
        "Users.5.SMSNumber": "",
        "Users.5.Simple2FA": "Disabled",
        "Users.5.SolEnable": "Disabled",
        "Users.5.UseEmail": "Disabled",
        "Users.5.UseSMS": "Disabled",
        "Users.5.UserName": "",
        "Users.6.AuthenticationProtocol": "SHA",
        "Users.6.EmailAddress": "",
        "Users.6.Enable": "Disabled",
        "Users.6.IpmiLanPrivilege": "No Access",
        "Users.6.IpmiSerialPrivilege": "No Access",
        "Users.6.Password": null,
        "Users.6.PrivacyProtocol": "AES",
        "Users.6.Privilege": 0,
        "Users.6.ProtocolEnable": "Disabled",
        "Users.6.SMSNumber": "",
        "Users.6.Simple2FA": "Disabled",
        "Users.6.SolEnable": "Disabled",
        "Users.6.UseEmail": "Disabled",
        "Users.6.UseSMS": "Disabled",
        "Users.6.UserName": "",
        "Users.7.AuthenticationProtocol": "SHA",
        "Users.7.EmailAddress": "",
        "Users.7.Enable": "Disabled",
        "Users.7.IpmiLanPrivilege": "No Access",
        "Users.7.IpmiSerialPrivilege": "No Access",
        "Users.7.Password": null,
        "Users.7.PrivacyProtocol": "AES",
        "Users.7.Privilege": 0,
        "Users.7.ProtocolEnable": "Disabled",
        "Users.7.SMSNumber": "",
        "Users.7.Simple2FA": "Disabled",
        "Users.7.SolEnable": "Disabled",
        "Users.7.UseEmail": "Disabled",
        "Users.7.UseSMS": "Disabled",
        "Users.7.UserName": "",
        "Users.8.AuthenticationProtocol": "SHA",
        "Users.8.EmailAddress": "",
        "Users.8.Enable": "Disabled",
        "Users.8.IpmiLanPrivilege": "No Access",
        "Users.8.IpmiSerialPrivilege": "No Access",
        "Users.8.Password": null,
        "Users.8.PrivacyProtocol": "AES",
        "Users.8.Privilege": 0,
        "Users.8.ProtocolEnable": "Disabled",
        "Users.8.SMSNumber": "",
        "Users.8.Simple2FA": "Disabled",
        "Users.8.SolEnable": "Disabled",
        "Users.8.UseEmail": "Disabled",
        "Users.8.UseSMS": "Disabled",
        "Users.8.UserName": "",
        "Users.9.AuthenticationProtocol": "SHA",
        "Users.9.EmailAddress": "",
        "Users.9.Enable": "Disabled",
        "Users.9.IpmiLanPrivilege": "No Access",
        "Users.9.IpmiSerialPrivilege": "No Access",
        "Users.9.Password": null,
        "Users.9.PrivacyProtocol": "AES",
        "Users.9.Privilege": 0,
        "Users.9.ProtocolEnable": "Disabled",
        "Users.9.SMSNumber": "",
        "Users.9.Simple2FA": "Disabled",
        "Users.9.SolEnable": "Disabled",
        "Users.9.UseEmail": "Disabled",
        "Users.9.UseSMS": "Disabled",
        "Users.9.UserName": "",
        "VNCServer.1.ActiveSessions": 0,
        "VNCServer.1.Enable": "Disabled",
        "VNCServer.1.LowerEncryptionBitLength": "Disabled",
        "VNCServer.1.MaxSessions": 2,
        "VNCServer.1.Password": null,
        "VNCServer.1.Port": 5901,
        "VNCServer.1.SSLEncryptionBitLength": "Disabled",
        "VNCServer.1.Timeout": 300,
        "VirtualConsole.1.AccessPrivilege": "Full Access",
        "VirtualConsole.1.ActiveSessions": 0,
        "VirtualConsole.1.AttachState": "Auto-attach",
        "VirtualConsole.1.CloseUnusedPort": "Disabled",
        "VirtualConsole.1.Enable": "Enabled",
        "VirtualConsole.1.EncryptEnable": "Enabled",
        "VirtualConsole.1.LocalDisable": "Disabled",
        "VirtualConsole.1.LocalVideo": "Enabled",
        "VirtualConsole.1.MaxSessions": 6,
        "VirtualConsole.1.PluginType": "HTML5",
        "VirtualConsole.1.Port": 5900,
        "VirtualConsole.1.Timeout": 1800,
        "VirtualConsole.1.TimeoutEnable": "Disabled",
        "VirtualConsole.1.WebRedirect": "Disabled",
        "VirtualMedia.1.Enable": "Enabled",
        "WebServer.1.BlockHTTPPort": "Disabled",
        "WebServer.1.CustomCipherString": "",
        "WebServer.1.Enable": "Enabled",
        "WebServer.1.HostHeaderCheck": "Enabled",
        "WebServer.1.Http2Enable": "Disabled",
        "WebServer.1.HttpPort": 80,
        "WebServer.1.HttpsPort": 443,
        "WebServer.1.HttpsRedirection": "Enabled",
        "WebServer.1.LowerEncryptionBitLength": "Enabled",
        "WebServer.1.ManualDNSEntry": "",
        "WebServer.1.MaxNumberOfSessions": 8,
        "WebServer.1.SSLEncryptionBitLength": "128-Bit or higher",
        "WebServer.1.TLSProtocol": "TLS 1.1 and Higher",
        "WebServer.1.Timeout": 300,
        "WebServer.1.TitleBarOption": "Auto",
        "WebServer.1.TitleBarOptionCustom": ""
    },
    "Description": "This schema provides the oem attributes",
    "Id": "iDRACAttributes",
    "Name": "OEMAttributeRegistry"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/iDRAC.Embedded.1/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/iDRAC.Embedded.1/Settings",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/iDRAC.Embedded.1/Settings/Actions/DellManager.ClearPending"
        }
    },
    "AttributeRegistry": "ManagerAttributeRegistry.v1_0_0",
    "Attributes": {},
    "Description": "This schema provides settings of the oem attributes",
    "Id": "iDRACSettings",
    "Name": "OemAttributeRegistrySettings",
    "Oem": {
        "Dell": {
            "@odata.context": "/redfish/v1/$metadata#DellManager.DellManager",
            "@odata.type": "#DellManager.v1_1_0.DellManager",
            "Jobs": {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/Jobs"
            }
        }
    }
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellJobService

```{
    "@odata.context": "/redfish/v1/$metadata#DellJobService.DellJobService",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellJobService",
    "@odata.type": "#DellJobService.v1_2_0.DellJobService",
    "Actions": {
        "#DellJobService.CreateRebootJob": {
            "RebootJobType@Redfish.AllowableValues": [
                "GracefulRebootWithForcedShutdown",
                "GracefulRebootWithoutForcedShutdown",
                "PowerCycle"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellJobService/Actions/DellJobService.CreateRebootJob"
        },
        "#DellJobService.DeleteJobQueue": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellJobService/Actions/DellJobService.DeleteJobQueue"
        },
        "#DellJobService.SetDeleteOnCompletionTimeout": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellJobService/Actions/DellJobService.SetDeleteOnCompletionTimeout"
        },
        "#DellJobService.SetupJobQueue": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellJobService/Actions/DellJobService.SetupJobQueue"
        }
    },
    "CurrentNumberOfJobs": 14,
    "DeleteOnCompletionTimeoutMinutes": 2880,
    "Description": "The DellJobService resource provides some actions to support Job management functionality.",
    "Id": "Job Service",
    "MaximumNumberOfJobs": 256,
    "Name": "DellJobService",
    "StartAutoDeleteAtThreshold": 128
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService

```{
    "@odata.context": "/redfish/v1/$metadata#DellLCService.DellLCService",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService",
    "@odata.type": "#DellLCService.v1_3_0.DellLCService",
    "Actions": {
        "#DellLCService.ClearProvisioningServer": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ClearProvisioningServer"
        },
        "#DellLCService.DeleteAutoDiscoveryClientCerts": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.DeleteAutoDiscoveryClientCerts"
        },
        "#DellLCService.DeleteAutoDiscoveryServerPublicKey": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.DeleteAutoDiscoveryServerPublicKey"
        },
        "#DellLCService.DownloadClientCerts": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.DownloadClientCerts"
        },
        "#DellLCService.ExportCompleteLCLog": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "Local",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportCompleteLCLog"
        },
        "#DellLCService.ExportFactoryConfiguration": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "Local",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportFactoryConfiguration"
        },
        "#DellLCService.ExportHWInventory": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "Local",
                "NFS"
            ],
            "XMLSchema@Redfish.AllowableValues": [
                "CIM-XML",
                "JSON",
                "Simple"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportHWInventory"
        },
        "#DellLCService.ExportLCLog": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "Local",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportLCLog"
        },
        "#DellLCService.ExportSVGFile": {
            "ShareType@Redfish.AllowableValues": [
                "Local"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportSVGFile"
        },
        "#DellLCService.ExportServerScreenShot": {
            "FileType@Redfish.AllowableValues": [
                "LastCrashScreenShot",
                "Preview",
                "ServerScreenShot"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportServerScreenShot"
        },
        "#DellLCService.ExportTechSupportReport": {
            "DataSelectorArrayIn@Redfish.AllowableValues": [
                "HWData",
                "OSAppData",
                "OSAppDataWithoutPII",
                "TTYLogs"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportTechSupportReport"
        },
        "#DellLCService.ExportVideoLog": {
            "FileType@Redfish.AllowableValues": [
                "BootCaptureVideo",
                "CrashCaptureVideo"
            ],
            "ShareType@Redfish.AllowableValues": [
                "Local"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportVideoLog"
        },
        "#DellLCService.ExportePSADiagnosticsResult": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "Local",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExportePSADiagnosticsResult"
        },
        "#DellLCService.ExposeiSMInstallerToHostOS": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ExposeiSMInstallerToHostOS"
        },
        "#DellLCService.GetRSStatus": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.GetRSStatus"
        },
        "#DellLCService.GetRemoteServicesAPIStatus": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.GetRemoteServicesAPIStatus"
        },
        "#DellLCService.InsertCommentInLCLog": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.InsertCommentInLCLog"
        },
        "#DellLCService.LCWipe": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.LCWipe"
        },
        "#DellLCService.ReInitiateAutoDiscovery": {
            "PerformAutoDiscovery@Redfish.AllowableValues": [
                "NextBoot",
                "Now",
                "Off"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ReInitiateAutoDiscovery"
        },
        "#DellLCService.ReInitiateDHS": {
            "PerformAutoDiscovery@Redfish.AllowableValues": [
                "NextBoot",
                "Now",
                "Off"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.ReInitiateDHS"
        },
        "#DellLCService.RunePSADiagnostics": {
            "RebootJobType@Redfish.AllowableValues": [
                "GracefulRebootWithForcedShutdown",
                "GracefulRebootWithoutForcedShutdown",
                "PowerCycle"
            ],
            "RunMode@Redfish.AllowableValues": [
                "Express",
                "ExpressAndExtended",
                "Extended"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.RunePSADiagnostics"
        },
        "#DellLCService.SupportAssistAcceptEULA": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistAcceptEULA"
        },
        "#DellLCService.SupportAssistClearAutoCollectSchedule": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistClearAutoCollectSchedule"
        },
        "#DellLCService.SupportAssistCollection": {
            "DataSelectorArrayIn@Redfish.AllowableValues": [
                "DebugLogs",
                "HWData",
                "OSAppData",
                "TTYLogs",
                "TelemetryReports"
            ],
            "Filter@Redfish.AllowableValues": [
                "No",
                "Yes"
            ],
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "FTP",
                "HTTP",
                "HTTPS",
                "Local",
                "NFS",
                "TFTP"
            ],
            "Transmit@Redfish.AllowableValues": [
                "No",
                "Yes"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistCollection"
        },
        "#DellLCService.SupportAssistExportLastCollection": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "FTP",
                "HTTP",
                "HTTPS",
                "NFS",
                "TFTP"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistExportLastCollection"
        },
        "#DellLCService.SupportAssistGetAutoCollectSchedule": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistGetAutoCollectSchedule"
        },
        "#DellLCService.SupportAssistGetEULAStatus": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistGetEULAStatus"
        },
        "#DellLCService.SupportAssistRegister": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistRegister"
        },
        "#DellLCService.SupportAssistSetAutoCollectSchedule": {
            "Recurrence@Redfish.AllowableValues": [
                "Monthly",
                "Quarterly",
                "Weekly"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistSetAutoCollectSchedule"
        },
        "#DellLCService.SupportAssistUploadLastCollection": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SupportAssistUploadLastCollection"
        },
        "#DellLCService.SystemErase": {
            "Component@Redfish.AllowableValues": [
                "AllApps",
                "BIOS",
                "CryptographicErasePD",
                "DIAG",
                "DrvPack",
                "IDRAC",
                "LCData",
                "NonVolatileMemory",
                "OverwritePD",
                "PERCNVCache",
                "vFlash"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.SystemErase"
        },
        "#DellLCService.TestNetworkShare": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "FTP",
                "HTTP",
                "HTTPS",
                "NFS",
                "TFTP"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.TestNetworkShare"
        },
        "#DellLCService.UpdateOSAppHealthData": {
            "UpdateType@Redfish.AllowableValues": [
                "Automatic"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLCService/Actions/DellLCService.UpdateOSAppHealthData"
        }
    },
    "Description": "The DellLCService resource provides some actions to support Lifecycle Controller functionality.",
    "Id": "DellLCService",
    "Name": "DellLCService"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicensableDevices

```{
    "@odata.context": "/redfish/v1/$metadata#DellLicensableDeviceCollection.DellLicensableDeviceCollection",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicensableDevices",
    "@odata.type": "#DellLicensableDeviceCollection.DellLicensableDeviceCollection",
    "Description": "A collection of DellLicensableDevice resource",
    "Members": [
        {
            "@odata.context": "/redfish/v1/$metadata#DellLicensableDevice.DellLicensableDevice",
            "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicensableDevices/iDRAC.Embedded.1",
            "@odata.type": "#DellLicensableDevice.v1_0_0.DellLicensableDevice",
            "Description": "DellLicensableDevice represents a device in the system that has registered with the License Manager.",
            "DeviceID": "11",
            "DevicePrimaryStatus": "OK",
            "DeviceState": "DevicePresent",
            "DeviceStatusMessage": null,
            "DeviceStatusMessageID": null,
            "DeviceType": "Internal",
            "FQDD": "iDRAC.Embedded.1",
            "Id": "iDRAC.Embedded.1",
            "LicenseList": [
                "FD00000021768845",
                "FD00000021768846"
            ],
            "LicenseList@odata.count": 2,
            "Model": "iDRAC9",
            "Name": "DellLicensableDevice",
            "RollupStatus": "OK",
            "SubsystemID": "4",
            "SubsystemVendorID": "1028",
            "UniqueID": "U8OIL5X",
            "VendorID": "1912"
        }
    ],
    "Members@odata.count": 1,
    "Name": "DellLicensableDeviceCollection"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicensableDevices/iDRAC.Embedded.1

```{
    "@odata.context": "/redfish/v1/$metadata#DellLicensableDevice.DellLicensableDevice",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicensableDevices/iDRAC.Embedded.1",
    "@odata.type": "#DellLicensableDevice.v1_0_0.DellLicensableDevice",
    "Description": "DellLicensableDevice represents a device in the system that has registered with the License Manager.",
    "DeviceID": "11",
    "DevicePrimaryStatus": "OK",
    "DeviceState": "DevicePresent",
    "DeviceStatusMessage": null,
    "DeviceStatusMessageID": null,
    "DeviceType": "Internal",
    "FQDD": "iDRAC.Embedded.1",
    "Id": "iDRAC.Embedded.1",
    "LicenseList": [
        "FD00000021768845",
        "FD00000021768846"
    ],
    "LicenseList@odata.count": 2,
    "Model": "iDRAC9",
    "Name": "DellLicensableDevice",
    "RollupStatus": "OK",
    "SubsystemID": "4",
    "SubsystemVendorID": "1028",
    "UniqueID": "U8OIL5X",
    "VendorID": "1912"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService

```{
    "@odata.context": "/redfish/v1/$metadata#DellLicenseManagementService.DellLicenseManagementService",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService",
    "@odata.type": "#DellLicenseManagementService.v1_1_0.DellLicenseManagementService",
    "Actions": {
        "#DellLicenseManagementService.DeleteLicense": {
            "DeleteOptions@Redfish.AllowableValues": [
                "All",
                "Force",
                "NoOption"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.DeleteLicense"
        },
        "#DellLicenseManagementService.ExportLicense": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ExportLicense"
        },
        "#DellLicenseManagementService.ExportLicenseByDevice": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ExportLicenseByDevice"
        },
        "#DellLicenseManagementService.ExportLicenseByDeviceToNetworkShare": {
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ExportLicenseByDeviceToNetworkShare"
        },
        "#DellLicenseManagementService.ExportLicenseToNetworkShare": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ExportLicenseToNetworkShare"
        },
        "#DellLicenseManagementService.ImportLicense": {
            "ImportOptions@Redfish.AllowableValues": [
                "All",
                "Force",
                "NoOption"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ImportLicense"
        },
        "#DellLicenseManagementService.ImportLicenseFromNetworkShare": {
            "IgnoreCertWarning@Redfish.AllowableValues": [
                "Off",
                "On"
            ],
            "ImportOptions@Redfish.AllowableValues": [
                "All",
                "Force",
                "NoOption"
            ],
            "ProxySupport@Redfish.AllowableValues": [
                "DefaultProxy",
                "Off",
                "ParametersProxy"
            ],
            "ProxyType@Redfish.AllowableValues": [
                "HTTP",
                "SOCKS"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "NFS"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ImportLicenseFromNetworkShare"
        },
        "#DellLicenseManagementService.ShowLicenseBits": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenseManagementService/Actions/DellLicenseManagementService.ShowLicenseBits"
        }
    },
    "Description": "The DellLicenseManagementService resource provides some actions to support License Management functionality.",
    "Id": "DellLicenseManagementService",
    "Name": "DellLicenseManagementService"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenses

```{
    "@odata.context": "/redfish/v1/$metadata#DellLicenseCollection.DellLicenseCollection",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenses",
    "@odata.type": "#DellLicenseCollection.DellLicenseCollection",
    "Description": "A collection of DellLicense resource",
    "Members": [
        {
            "@odata.context": "/redfish/v1/$metadata#DellLicense.DellLicense",
            "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenses/FD00000021768845",
            "@odata.type": "#DellLicense.v1_2_0.DellLicense",
            "AssignedDevices": [
                "iDRAC.Embedded.1"
            ],
            "AssignedDevices@odata.count": 1,
            "Description": "An instance of DellLicense represents a feature license installed on a system.",
            "DeviceFamilyDeviceID": [
                "11",
                "11"
            ],
            "DeviceFamilyDeviceID@odata.count": 2,
            "DeviceFamilySubsystemID": [
                "3",
                "4"
            ],
            "DeviceFamilySubsystemID@odata.count": 2,
            "DeviceFamilySubsystemVendorID": [
                "3",
                "4"
            ],
            "DeviceFamilySubsystemVendorID@odata.count": 2,
            "DeviceFamilyVendorID": [
                "1912",
                "1912"
            ],
            "DeviceFamilyVendorID@odata.count": 2,
            "EntitlementID": "FD00000021768845",
            "EvalLicenseTimeRemainingDays": null,
            "Id": "FD00000021768845",
            "InstanceID": "FD00000021768845",
            "LicenseAttributes": "ValidSubcomponent",
            "LicenseDescription": [
                "OpenManage Enterprise Advanced"
            ],
            "LicenseDescription@odata.count": 1,
            "LicenseDurationDays": 0,
            "LicenseEndDate": null,
            "LicenseInstallDate": "2021-07-02T13:02:10-05:00",
            "LicensePrimaryStatus": "OK",
            "LicenseSoldDate": "2021-06-03T19:26:08-05:00",
            "LicenseStartDate": null,
            "LicenseStatusMessage": null,
            "LicenseStatusMessageID": null,
            "LicenseType": "Perpetual",
            "Name": "DellLicense"
        },
        {
            "@odata.context": "/redfish/v1/$metadata#DellLicense.DellLicense",
            "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenses/FD00000021768846",
            "@odata.type": "#DellLicense.v1_2_0.DellLicense",
            "AssignedDevices": [
                "iDRAC.Embedded.1"
            ],
            "AssignedDevices@odata.count": 1,
            "Description": "An instance of DellLicense represents a feature license installed on a system.",
            "DeviceFamilyDeviceID": [
                "11",
                "11"
            ],
            "DeviceFamilyDeviceID@odata.count": 1,
            "DeviceFamilySubsystemID": [
                "4",
                "4"
            ],
            "DeviceFamilySubsystemID@odata.count": 1,
            "DeviceFamilySubsystemVendorID": [
                "4",
                "4"
            ],
            "DeviceFamilySubsystemVendorID@odata.count": 1,
            "DeviceFamilyVendorID": [
                "1912",
                "1912"
            ],
            "DeviceFamilyVendorID@odata.count": 1,
            "EntitlementID": "FD00000021768846",
            "EvalLicenseTimeRemainingDays": null,
            "Id": "FD00000021768846",
            "InstanceID": "FD00000021768846",
            "LicenseAttributes": "ValidSubcomponent",
            "LicenseDescription": [
                "iDRAC9 15g Enterprise License"
            ],
            "LicenseDescription@odata.count": 1,
            "LicenseDurationDays": 0,
            "LicenseEndDate": null,
            "LicenseInstallDate": "2021-07-02T13:02:22-05:00",
            "LicensePrimaryStatus": "OK",
            "LicenseSoldDate": "2021-06-03T19:26:08-05:00",
            "LicenseStartDate": null,
            "LicenseStatusMessage": null,
            "LicenseStatusMessageID": null,
            "LicenseType": "Perpetual",
            "Name": "DellLicense"
        }
    ],
    "Members@odata.count": 2,
    "Name": "DellLicenseCollection"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenses/FD00000021768845

```{
    "@odata.context": "/redfish/v1/$metadata#DellLicense.DellLicense",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenses/FD00000021768845",
    "@odata.type": "#DellLicense.v1_2_0.DellLicense",
    "AssignedDevices": [
        "iDRAC.Embedded.1"
    ],
    "AssignedDevices@odata.count": 1,
    "Description": "An instance of DellLicense represents a feature license installed on a system.",
    "DeviceFamilyDeviceID": [
        "11",
        "11"
    ],
    "DeviceFamilyDeviceID@odata.count": 2,
    "DeviceFamilySubsystemID": [
        "3",
        "4"
    ],
    "DeviceFamilySubsystemID@odata.count": 2,
    "DeviceFamilySubsystemVendorID": [
        "3",
        "4"
    ],
    "DeviceFamilySubsystemVendorID@odata.count": 2,
    "DeviceFamilyVendorID": [
        "1912",
        "1912"
    ],
    "DeviceFamilyVendorID@odata.count": 2,
    "EntitlementID": "FD00000021768845",
    "EvalLicenseTimeRemainingDays": null,
    "Id": "FD00000021768845",
    "InstanceID": "FD00000021768845",
    "LicenseAttributes": "ValidSubcomponent",
    "LicenseDescription": [
        "OpenManage Enterprise Advanced"
    ],
    "LicenseDescription@odata.count": 1,
    "LicenseDurationDays": 0,
    "LicenseEndDate": null,
    "LicenseInstallDate": "2021-07-02T13:02:10-05:00",
    "LicensePrimaryStatus": "OK",
    "LicenseSoldDate": "2021-06-03T19:26:08-05:00",
    "LicenseStartDate": null,
    "LicenseStatusMessage": null,
    "LicenseStatusMessageID": null,
    "LicenseType": "Perpetual",
    "Name": "DellLicense"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenses/FD00000021768846

```{
    "@odata.context": "/redfish/v1/$metadata#DellLicense.DellLicense",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellLicenses/FD00000021768846",
    "@odata.type": "#DellLicense.v1_2_0.DellLicense",
    "AssignedDevices": [
        "iDRAC.Embedded.1"
    ],
    "AssignedDevices@odata.count": 1,
    "Description": "An instance of DellLicense represents a feature license installed on a system.",
    "DeviceFamilyDeviceID": [
        "11"
    ],
    "DeviceFamilyDeviceID@odata.count": 1,
    "DeviceFamilySubsystemID": [
        "4"
    ],
    "DeviceFamilySubsystemID@odata.count": 1,
    "DeviceFamilySubsystemVendorID": [
        "4"
    ],
    "DeviceFamilySubsystemVendorID@odata.count": 1,
    "DeviceFamilyVendorID": [
        "1912"
    ],
    "DeviceFamilyVendorID@odata.count": 1,
    "EntitlementID": "FD00000021768846",
    "EvalLicenseTimeRemainingDays": null,
    "Id": "FD00000021768846",
    "InstanceID": "FD00000021768846",
    "LicenseAttributes": "ValidSubcomponent",
    "LicenseDescription": [
        "iDRAC9 15g Enterprise License"
    ],
    "LicenseDescription@odata.count": 1,
    "LicenseDurationDays": 0,
    "LicenseEndDate": null,
    "LicenseInstallDate": "2021-07-02T13:02:22-05:00",
    "LicensePrimaryStatus": "OK",
    "LicenseSoldDate": "2021-06-03T19:26:08-05:00",
    "LicenseStartDate": null,
    "LicenseStatusMessage": null,
    "LicenseStatusMessageID": null,
    "LicenseType": "Perpetual",
    "Name": "DellLicense"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellOpaqueManagementData

```{
    "@odata.context": "/redfish/v1/$metadata#DellOpaqueManagementDataCollection.DellOpaqueManagementDataCollection",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellOpaqueManagementData",
    "@odata.type": "#DellOpaqueManagementDataCollection.DellOpaqueManagementDataCollection",
    "Description": "A collection of DellOpaqueManagementData resource",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "DellOpaqueManagementDataCollection"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService

```{
    "@odata.context": "/redfish/v1/$metadata#DellPersistentStorageService.DellPersistentStorageService",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService",
    "@odata.type": "#DellPersistentStorageService.v1_1_0.DellPersistentStorageService",
    "Actions": {
        "#DellPersistentStorageService.AttachPartition": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.AttachPartition"
        },
        "#DellPersistentStorageService.CreatePartition": {
            "PartitionType@Redfish.AllowableValues": [
                "Floppy",
                "HardDisk"
            ],
            "SizeUnit@Redfish.AllowableValues": [
                "GB",
                "MB"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.CreatePartition"
        },
        "#DellPersistentStorageService.CreatePartitionUsingImage": {
            "HashType@Redfish.AllowableValues": [
                "MD5",
                "SHA1"
            ],
            "PartitionType@Redfish.AllowableValues": [
                "CDROM",
                "Floppy",
                "HardDisk"
            ],
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "FTP",
                "HTTP",
                "NFS",
                "TFTP"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.CreatePartitionUsingImage"
        },
        "#DellPersistentStorageService.DeletePartition": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.DeletePartition"
        },
        "#DellPersistentStorageService.DetachPartition": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.DetachPartition"
        },
        "#DellPersistentStorageService.ExportDataFromPartition": {
            "ShareType@Redfish.AllowableValues": [
                "CIFS",
                "NFS",
                "TFTP"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.ExportDataFromPartition"
        },
        "#DellPersistentStorageService.FormatPartition": {
            "FormatType@Redfish.AllowableValues": [
                "EXT2",
                "EXT3",
                "FAT16",
                "FAT32"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.FormatPartition"
        },
        "#DellPersistentStorageService.InitializeMedia": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.InitializeMedia"
        },
        "#DellPersistentStorageService.ModifyPartition": {
            "AccessType@Redfish.AllowableValues": [
                "Read-Only",
                "Read-Write"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.ModifyPartition"
        },
        "#DellPersistentStorageService.VFlashStateChange": {
            "RequestedState@Redfish.AllowableValues": [
                "Disable",
                "Enable"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellPersistentStorageService/Actions/DellPersistentStorageService.VFlashStateChange"
        }
    },
    "Description": "The DellPersistentStorageService resource provides some actions to support VFlash functionality.",
    "Id": "DellPersistentStorageService",
    "Name": "DellPersistentStorageService"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellSystemQuickSync

```{
    "@odata.context": "/redfish/v1/$metadata#DellSystemQuickSyncCollection.DellSystemQuickSyncCollection",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellSystemQuickSync",
    "@odata.type": "#DellSystemQuickSyncCollection.DellSystemQuickSyncCollection",
    "Description": "A collection of DellSystemQuickSync resource",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "DellSystemQuickSyncCollection"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellTimeService

```{
    "@odata.context": "/redfish/v1/$metadata#DellTimeService.DellTimeService",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellTimeService",
    "@odata.type": "#DellTimeService.v1_0_1.DellTimeService",
    "Actions": {
        "#DellTimeService.ManageTime": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellTimeService/Actions/DellTimeService.ManageTime"
        }
    },
    "Description": "DellTimeService provides actions to manage time (retrieve or set time) for the service processor.",
    "Id": "DellTimeService",
    "Name": "DellTimeService"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellUSBDevices

```{
    "@odata.context": "/redfish/v1/$metadata#DellUSBDeviceCollection.DellUSBDeviceCollection",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellUSBDevices",
    "@odata.type": "#DellUSBDeviceCollection.DellUSBDeviceCollection",
    "Description": "A collection of DellUSBDevice resource",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "DellUSBDeviceCollection"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCard/iDRAC.Embedded.1-1_0x23_IDRACinfo

```{
    "@odata.context": "/redfish/v1/$metadata#DelliDRACCard.DelliDRACCard",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCard/iDRAC.Embedded.1-1_0x23_IDRACinfo",
    "@odata.type": "#DelliDRACCard.v1_1_0.DelliDRACCard",
    "Description": "An instance of DelliDRACCard will have data specific to the Integrated Dell Remote Access Controller (iDRAC) in the managed system.",
    "IPMIVersion": "2.0",
    "Id": "iDRAC.Embedded.1-1_0x23_IDRACinfo",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2022-10-26T20:48:25+00:00",
    "Name": "DelliDRACCard",
    "URLString": "https://10.44.182.90:443"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService

```{
    "@odata.context": "/redfish/v1/$metadata#DelliDRACCardService.DelliDRACCardService",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService",
    "@odata.type": "#DelliDRACCardService.v1_4_0.DelliDRACCardService",
    "Actions": {
        "#DelliDRACCardService.DeleteCertificate": {
            "CertificateType@Redfish.AllowableValues": [
                "KMS_SERVER_CA",
                "SEKM_SSL_CERT"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.DeleteCertificate"
        },
        "#DelliDRACCardService.DeleteGroup": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.DeleteGroup"
        },
        "#DelliDRACCardService.DisableSEKM": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.DisableSEKM"
        },
        "#DelliDRACCardService.DisableiLKM": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.DisableiLKM"
        },
        "#DelliDRACCardService.EnableSEKM": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.EnableSEKM"
        },
        "#DelliDRACCardService.EnableiLKM": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.EnableiLKM"
        },
        "#DelliDRACCardService.ExportCertificate": {
            "CertificateType@Redfish.AllowableValues": [
                "KMS_SERVER_CA",
                "SEKM_SSL_CERT"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.ExportCertificate"
        },
        "#DelliDRACCardService.ExportSSLCertificate": {
            "SSLCertType@Redfish.AllowableValues": [
                "CA",
                "CSC",
                "ClientTrustCertificate",
                "Server"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.ExportSSLCertificate"
        },
        "#DelliDRACCardService.FactoryIdentityCertificateGenerateCSR": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.FactoryIdentityCertificateGenerateCSR"
        },
        "#DelliDRACCardService.FactoryIdentityExportCertificate": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.FactoryIdentityExportCertificate"
        },
        "#DelliDRACCardService.FactoryIdentityImportCertificate": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.FactoryIdentityImportCertificate"
        },
        "#DelliDRACCardService.GenerateSEKMCSR": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.GenerateSEKMCSR"
        },
        "#DelliDRACCardService.GetKVMSession": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.GetKVMSession"
        },
        "#DelliDRACCardService.ImportCertificate": {
            "CertificateType@Redfish.AllowableValues": [
                "KMS_SERVER_CA",
                "RSYSLOG_SERVER_CA",
                "SEKM_SSL_CERT"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.ImportCertificate"
        },
        "#DelliDRACCardService.ImportSSLCertificate": {
            "CertificateType@Redfish.AllowableValues": [
                "CA",
                "CSC",
                "ClientTrustCertificate",
                "Server"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.ImportSSLCertificate"
        },
        "#DelliDRACCardService.JoinGroup": {
            "CloneConfiguration@Redfish.AllowableValues": [
                "Disable",
                "Enable"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.JoinGroup"
        },
        "#DelliDRACCardService.Rekey": {
            "Mode@Redfish.AllowableValues": [
                "SEKM",
                "iLKM"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.Rekey"
        },
        "#DelliDRACCardService.RemoveSelf": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.RemoveSelf"
        },
        "#DelliDRACCardService.SSLResetCfg": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.SSLResetCfg"
        },
        "#DelliDRACCardService.SendTestEmailAlert": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.SendTestEmailAlert"
        },
        "#DelliDRACCardService.SendTestSNMPTrap": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.SendTestSNMPTrap"
        },
        "#DelliDRACCardService.TestRsyslogServerConnection": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.TestRsyslogServerConnection"
        },
        "#DelliDRACCardService.TestSEKMServerConnection": {
            "ServerType@Redfish.AllowableValues": [
                "Primary",
                "Secondary"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.TestSEKMServerConnection"
        },
        "#DelliDRACCardService.VerifyHWProofOfPossession": {
            "Algorithm@Redfish.AllowableValues": [
                "AES128CBC"
            ],
            "KeyDerivationFunction@Redfish.AllowableValues": [
                "DellSHA256"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.VerifyHWProofOfPossession"
        },
        "#DelliDRACCardService.iDRACReset": {
            "Force@Redfish.AllowableValues": [
                "Force",
                "Graceful"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.iDRACReset"
        },
        "#DelliDRACCardService.iDRACResetCfg": {
            "Force@Redfish.AllowableValues": [
                "Force",
                "Graceful"
            ],
            "Preserve@Redfish.AllowableValues": [
                "All",
                "Default",
                "ResetAllWithRootDefaults"
            ],
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.iDRACResetCfg"
        },
        "#DelliDRACCardService.iLKMToSEKMTransition": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DelliDRACCardService/Actions/DelliDRACCardService.iLKMToSEKMTransition"
        }
    },
    "Description": "The DelliDRACCardService resource provides some actions to support iDRAC configurations.",
    "Id": "DelliDRACCardService",
    "Name": "DelliDRACCardService"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellvFlash

```{
    "@odata.context": "/redfish/v1/$metadata#DellvFlashCollection.DellvFlashCollection",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellvFlash",
    "@odata.type": "#DellvFlashCollection.DellvFlashCollection",
    "Description": "A collection of DellvFlash resource",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "DellvFlashCollection"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/HWCertificates/SecurityCertificate.2

```{
    "@odata.context": "/redfish/v1/$metadata#DellCertificate.DellCertificate",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/HWCertificates/SecurityCertificate.2",
    "@odata.type": "#DellCertificate.v1_0_1.DellCertificate",
    "CertificateType": "FACTORY_IDENTITY_CERT",
    "Description": "Factory Identity Certificate",
    "Id": "SecurityCertificate.2",
    "IssuerCommonName_CN": "0IVC00-CE0C-105E-6826",
    "IssuerCountryCode_CC": "CN",
    "IssuerLocality_L": "Shanghai",
    "IssuerOrganization_O": "Inventec",
    "IssuerState_S": "Shanghai",
    "Name": "FactoryIdentity Certificate",
    "SerialNumber": "03000000002328E5",
    "SubjectCommonName_CN": "b0:7b:25:d1:5a:5a",
    "SubjectCountryCode_CC": "US",
    "SubjectLocality_L": "Round Rock",
    "SubjectOrganization_O": "Dell EMC",
    "SubjectState_S": "Texas",
    "ValidFrom": "Apr  1 05:20:12 2021 GMT",
    "ValidTo": "May 31 05:20:12 2040 GMT"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/Jobs

```
```

## /redfish/v1/Managers/iDRAC.Embedded.1/SerialInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#SerialInterfaceCollection.SerialInterfaceCollection",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/SerialInterfaces",
    "@odata.type": "#SerialInterfaceCollection.SerialInterfaceCollection",
    "Description": "Collection of Serial Interfaces for this System",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/SerialInterfaces/Serial.1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Serial Interface Collection"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/SerialInterfaces/Serial.1

```{
    "@odata.context": "/redfish/v1/$metadata#SerialInterface.SerialInterface",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/SerialInterfaces/Serial.1",
    "@odata.type": "#SerialInterface.v1_1_7.SerialInterface",
    "Actions": {
        "Oem": {
            "#DellSerialInterface.SerialDataClear": {
                "target": "/redfish/v1/Managers/iDRAC.Embedded.1/SerialInterfaces/Serial.1/Actions/Oem/DellSerialInterface.SerialDataClear"
            },
            "#DellSerialInterface.SerialDataExport": {
                "target": "/redfish/v1/Managers/iDRAC.Embedded.1/SerialInterfaces/Serial.1/Actions/Oem/DellSerialInterface.SerialDataExport"
            }
        }
    },
    "Description": "Management for Serial Interface",
    "Id": "Serial.1",
    "Name": "Managed Serial Interface 1"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia

```{
    "@odata.context": "/redfish/v1/$metadata#VirtualMediaCollection.VirtualMediaCollection",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia",
    "@odata.type": "#VirtualMediaCollection.VirtualMediaCollection",
    "Description": "iDRAC Virtual Media Services Settings",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/RemovableDisk"
        },
        {
            "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/CD"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Virtual Media Services"
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/CD

```{
    "@odata.context": "/redfish/v1/$metadata#VirtualMedia.VirtualMedia",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/CD",
    "@odata.type": "#VirtualMedia.v1_3_2.VirtualMedia",
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/CD/Actions/VirtualMedia.EjectMedia"
        },
        "#VirtualMedia.InsertMedia": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/CD/Actions/VirtualMedia.InsertMedia"
        }
    },
    "ConnectedVia": "NotConnected",
    "Description": "iDRAC Virtual Media Services Settings",
    "Id": "CD",
    "Image": null,
    "ImageName": null,
    "Inserted": false,
    "MediaTypes": [
        "CD",
        "DVD"
    ],
    "MediaTypes@odata.count": 2,
    "Name": "Virtual CD",
    "Password": null,
    "TransferMethod": null,
    "TransferProtocolType": null,
    "UserName": null,
    "WriteProtected": null
}
```

## /redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/RemovableDisk

```{
    "@odata.context": "/redfish/v1/$metadata#VirtualMedia.VirtualMedia",
    "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/RemovableDisk",
    "@odata.type": "#VirtualMedia.v1_3_2.VirtualMedia",
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/RemovableDisk/Actions/VirtualMedia.EjectMedia"
        },
        "#VirtualMedia.InsertMedia": {
            "target": "/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/RemovableDisk/Actions/VirtualMedia.InsertMedia"
        }
    },
    "ConnectedVia": "NotConnected",
    "Description": "iDRAC Virtual Media Services Settings",
    "Id": "RemovableDisk",
    "Image": null,
    "ImageName": null,
    "Inserted": false,
    "MediaTypes": [
        "USBStick"
    ],
    "MediaTypes@odata.count": 1,
    "Name": "Virtual Removable Disk",
    "Password": null,
    "TransferMethod": null,
    "TransferProtocolType": null,
    "UserName": null,
    "WriteProtected": null
}
```

