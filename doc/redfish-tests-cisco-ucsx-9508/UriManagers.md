# Resource: /api-explorer/resources/redfish/v1/Managers

Vendor | Model
--- | ---
Cisco | UCSX-9508

## /api-explorer/resources/redfish/v1/Managers

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerCollection.ManagerCollection",
    "@odata.id": "/redfish/v1/Managers",
    "@odata.type": "#ManagerCollection.ManagerCollection",
    "Description": "Collection of Managers",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/CMC"
        },
        {
            "@odata.id": "/redfish/v1/Managers/PeerCMC"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Manager Collection"
}
```

## /api-explorer/resources/redfish/v1/Managers/CMC

```{
    "@odata.context": "/redfish/v1/$metadata#Manager.Manager",
    "@odata.id": "/redfish/v1/Managers/CMC",
    "@odata.type": "#Manager.v1_5_0.Manager",
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "ForceRestart"
            ],
            "target": "/redfish/v1/Managers/CMC/Actions/Manager.Reset"
        },
        "Oem": {
            "#Cisco.ExportTechSupport": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ExportTechSupport",
                "Protocol@Redfish.AllowableValues": [
                    "TFTP"
                ],
                "RemoteFilename@Redfish.AllowableValues": [
                    "Tech support filename on remote machine"
                ],
                "RemoteHostname@Redfish.AllowableValues": [
                    "IP Address String"
                ],
                "RemotePath@Redfish.AllowableValues": [
                    "Directory path of tech support file on remote machine"
                ],
                "target": "/redfish/v1/Managers/CMC/Actions/Oem/Cisco.ExportTechSupport"
            },
            "#Cisco.ResetToFactoryDefaults": {
                "@odata.type": "#CiscoUCSExtensions.v1_0_0.ResetToFactoryDefaults",
                "target": "/redfish/v1/Managers/CMC/Actions/Oem/Cisco.ResetToFactoryDefaults"
            }
        }
    },
    "DateTime": "Tue Nov 29 08:35:41 2022",
    "DateTimeLocalOffset": "+00:00",
    "Description": "Cisco Chassis Management Controller",
    "EthernetInterfaces": {
        "@odata.id": "/redfish/v1/Managers/CMC/EthernetInterfaces"
    },
    "FirmwareVersion": "4.2(2c)",
    "Id": "CMC",
    "LogServices": {
        "@odata.id": "/redfish/v1/Managers/CMC/LogServices"
    },
    "ManagerType": "EnclosureManager",
    "Model": "UCSX-I-9108-25G",
    "Name": "Cisco Chassis Management Controller",
    "NetworkProtocol": {
        "@odata.id": "/redfish/v1/Managers/CMC/NetworkProtocol"
    },
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "FanPolicy": "LowPower",
            "InventoryState": "FullInventoryReady"
        }
    },
    "ServiceEntryPointUUID": "8b5e20ee-1acd-4c9b-9f90-e42b4d81a15a",
    "Status": {
        "State": "StandbySpare"
    },
    "UUID": "8b5e20ee-1acd-4c9b-9f90-e42b4d81a15a"
}
```

## /api-explorer/resources/redfish/v1/Managers/CMC/EthernetInterfaces

```{
    "@odata.context": "/redfish/v1/$metadata#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "@odata.id": "/redfish/v1/Managers/CMC/EthernetInterfaces",
    "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/CMC/EthernetInterfaces/CMS"
        },
        {
            "@odata.id": "/redfish/v1/Managers/CMC/EthernetInterfaces/Inband"
        }
    ],
    "Members@odata.count": 2,
    "Name": "EthernetInterfaces"
}
```

## /api-explorer/resources/redfish/v1/Managers/CMC/EthernetInterfaces/CMS

```{
    "@odata.id": "/redfish/v1/Managers/CMC/EthernetInterfaces/CMS",
    "@odata.type": "#EthernetInterface.v1_5_0.EthernetInterface",
    "Id": "CMS",
    "Name": "CMS VLAN ID entries",
    "VLANs": {
        "@odata.id": "/redfish/v1/Managers/CMC/EthernetInterfaces/CMS/VLANs"
    }
}
```

## /api-explorer/resources/redfish/v1/Managers/CMC/EthernetInterfaces/CMS/VLANs

```{
    "@odata.id": "/redfish/v1/Managers/CMC/EthernetInterfaces/CMS/VLANs",
    "@odata.type": "#VLanNetworkInterfaceCollection.VLanNetworkInterfaceCollection",
    "Description": "Inband VLAN Network Interfaces",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/CMC/EthernetInterfaces/CMS/VLANs/10"
        },
        {
            "@odata.id": "/redfish/v1/Managers/CMC/EthernetInterfaces/CMS/VLANs/89"
        }
    ],
    "Members@odata.count": 2,
    "Name": "System Inband VLAN"
}
```

## /api-explorer/resources/redfish/v1/Managers/CMC/EthernetInterfaces/CMS/VLANs/10

```{
    "@odata.id": "/redfish/v1/Managers/CMC/EthernetInterfaces/CMS/VLANs/10",
    "@odata.type": "#VLanNetworkInterface.v1_1_3.VLanNetworkInterface",
    "Description": "Inband VLAN Network Interface",
    "Id": "10",
    "Name": "System Inband VLAN Collection",
    "VLANEnable": true,
    "VLANId": 10
}
```

## /api-explorer/resources/redfish/v1/Managers/CMC/EthernetInterfaces/CMS/VLANs/89

```{
    "@odata.id": "/redfish/v1/Managers/CMC/EthernetInterfaces/CMS/VLANs/89",
    "@odata.type": "#VLanNetworkInterface.v1_1_3.VLanNetworkInterface",
    "Description": "Inband VLAN Network Interface",
    "Id": "89",
    "Name": "System Inband VLAN Collection",
    "VLANEnable": true,
    "VLANId": 89
}
```

## /api-explorer/resources/redfish/v1/Managers/CMC/EthernetInterfaces/Inband

```{
    "@odata.id": "/redfish/v1/Managers/CMC/EthernetInterfaces/Inband",
    "@odata.type": "#EthernetInterface.v1_5_0.EthernetInterface",
    "IPv4StaticAddresses": [
        {
            "Address": "",
            "Gateway": "",
            "SubnetMask": ""
        }
    ],
    "IPv6StaticAddresses": [
        {}
    ],
    "IPv6StaticDefaultGateways": [
        {}
    ],
    "Id": "Inband",
    "Name": "Inband Interface",
    "VLAN": {
        "VLANEnable": false,
        "VlanId": -1
    }
}
```

## /api-explorer/resources/redfish/v1/Managers/CMC/LogServices

```{
    "@odata.context": "/redfish/v1/$metadata#LogServiceCollection.LogServiceCollection",
    "@odata.id": "/redfish/v1/Managers/CMC/LogServices",
    "@odata.type": "#LogServiceCollection.LogServiceCollection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Managers/CMC/LogServices/CMC"
        }
    ],
    "Members@odata.count": 1,
    "Name": "LogServices"
}
```

## /api-explorer/resources/redfish/v1/Managers/CMC/LogServices/CMC

```{
    "@odata.id": "/redfish/v1/Managers/CMC/LogServices/CMC",
    "@odata.type": "#LogService.v1_1_1.LogService",
    "Actions": {
        "Oem": {
            "#CiscoUCSExtensions.TestRemoteSyslogCfg": {
                "target": "/redfish/v1/Managers/CMC/LogServices/CMC/Actions/Oem/CiscoUCSExtensions.TestRemoteSyslogCfg"
            }
        }
    },
    "Oem": {
        "Cisco": {
            "SyslogConnectionInfo": [
                null,
                null
            ]
        }
    }
}
```

## /api-explorer/resources/redfish/v1/Managers/CMC/NetworkProtocol

```{
    "@odata.context": "/redfish/v1/$metadata#ManagerNetworkProtocol.ManagerNetworkProtocol",
    "@odata.id": "/redfish/v1/Managers/CMC/NetworkProtocol",
    "@odata.type": "#ManagerNetworkProtocol.v1_6_1.ManagerNetworkProtocol",
    "Description": "Manager Network Service",
    "FQDN": "TiltonRiver-0",
    "HostName": "TiltonRiver-0",
    "Id": "ManagerNetworkProtocol",
    "Name": "Manager Network Protocol",
    "SNMP": {
        "ProtocolEnabled": null
    }
}
```

## /api-explorer/resources/redfish/v1/Managers/PeerCMC

```{
    "@odata.context": "/redfish/v1/$metadata#Manager.Manager",
    "@odata.id": "/redfish/v1/Managers/PeerCMC",
    "@odata.type": "#Manager.v1_5_0.Manager",
    "Actions": {
        "#Manager.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "ForceRestart"
            ],
            "target": "/redfish/v1/Managers/PeerCMC/Actions/Manager.Reset"
        }
    },
    "Description": "Cisco Chassis Management Controller",
    "Id": "PeerCMC",
    "ManagerType": "EnclosureManager",
    "Name": "Cisco Chassis Management Controller",
    "Status": {
        "State": "Enabled"
    }
}
```

