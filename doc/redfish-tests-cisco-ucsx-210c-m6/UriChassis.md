# Resource: /api-explorer/resources/redfish/v1/Chassis

Vendor | Model
--- | ---
Cisco | UCSX-210C-M6

## /api-explorer/resources/redfish/v1/Chassis

```{
    "@odata.context": "/redfish/v1/$metadata#ChassisCollection.ChassisCollection",
    "@odata.id": "/redfish/v1/Chassis",
    "@odata.type": "#ChassisCollection.ChassisCollection",
    "Description": "Collection of Chassis",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Chassis Collection"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/1",
    "@odata.type": "#Chassis.v1_14_0.Chassis",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/1/Assembly"
    },
    "ChassisType": "Enclosure",
    "Description": "It represents the properties for physical components for any system.  This one object is intended to represent racks, rackmount servers, blades, standalone, modular systems, enclosures, and all other containers.  The non-cpu/device centric parts of the schema are all accessed either directly or indirectly through this resource",
    "Id": "1",
    "Manufacturer": "Cisco Systems Inc",
    "Name": "BladeEnclosure."
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Assembly",
    "@odata.type": "#Assembly.v1_3_0.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-210C-M6",
            "PartNumber": "68-7387-01 ",
            "PhysicalContext": "Chassis",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FCH25337EHM",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/FCH25337EHM

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/FCH25337EHM",
    "@odata.type": "#Chassis.v1_14_0.Chassis",
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/FCH25337EHM/Actions/Chassis.Reset"
        }
    },
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Assembly"
    },
    "AssetTag": null,
    "ChassisType": "Blade",
    "Description": "It represents the properties for physical components for any system.  This one object is intended to represent racks, rackmount servers, blades, standalone, modular systems, enclosures, and all other containers.  The non-cpu/device centric parts of the schema are all accessed either directly or indirectly through this resource",
    "Id": "FCH25337EHM",
    "Links": {
        "ComputerSystems": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH25337EHM"
            }
        ],
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/253"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID/Drives/254"
            }
        ],
        "ManagedBy": [
            {
                "@odata.id": "/redfish/v1/Managers/CIMC"
            }
        ],
        "Storage": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH25337EHM/Storage/MSTOR-RAID"
            }
        ]
    },
    "Location": {
        "Contacts": [],
        "PartLocation": {
            "LocationOrdinalValue": 1,
            "LocationType": "Slot"
        },
        "Placement": {
            "Rack": null,
            "RackOffset": null,
            "RackOffsetUnits": null,
            "Row": null
        },
        "PostalAddress": {
            "AdditionalInfo": null,
            "Building": null,
            "City": null,
            "Country": null,
            "District": null,
            "Floor": null,
            "Name": null,
            "PostalCode": null,
            "Room": null,
            "Street": null,
            "Territory": null
        }
    },
    "LocationIndicatorActive": false,
    "Manufacturer": "Cisco Systems Inc",
    "Model": "UCSX-210C-M6",
    "Name": "Computer System Blade.",
    "NetworkAdapters": {
        "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters"
    },
    "Power": {
        "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Power"
    },
    "SerialNumber": "FCH25337EHM",
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Assembly",
    "@odata.type": "#Assembly.v1_3_0.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-210C-M6",
            "PartNumber": "73-20511-01 ",
            "PhysicalContext": "SystemBoard",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FCH25337EHM",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkAdapterCollection.NetworkAdapterCollection",
    "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters",
    "@odata.type": "#NetworkAdapterCollection.NetworkAdapterCollection",
    "Description": "Collection of NetworkAdapter resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9"
        }
    ],
    "Members@odata.count": 1,
    "Name": "NetworkAdapter Collection"
}
```

## /api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkAdapter.NetworkAdapter",
    "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9",
    "@odata.type": "#NetworkAdapter.v1_5_0.NetworkAdapter",
    "Actions": {
        "#NetworkAdapter.ResetSettingsToDefault": {
            "target": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/Actions/NetworkAdapter.ResetSettingsToDefault"
        }
    },
    "Controllers": [
        {
            "ControllerCapabilities": {
                "NetworkDeviceFunctionCount": 4,
                "NetworkPortCount": 2
            },
            "FirmwarePackageVersion": "5.2(1c)",
            "Links": {
                "NetworkDeviceFunctions": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/esxi-trunk-2"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/esxi-trunk-1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/fc0"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/fc1"
                    }
                ],
                "NetworkDeviceFunctions@odata.count": 4,
                "NetworkPorts": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-2"
                    }
                ],
                "NetworkPorts@odata.count": 2
            },
            "Location": {
                "PartLocation": {
                    "LocationType": "Slot",
                    "ServiceLabel": "SlotID:0-MLOM"
                }
            }
        }
    ],
    "Id": "UCSX-V4-Q25GML_FCH25337EE9",
    "Manufacturer": "Cisco Systems Inc",
    "Model": "UCSX-V4-Q25GML",
    "Name": "UCS VIC 14425",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts"
    },
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "BaseMac": "D4:77:98:A8:D0:E8",
            "VicConfiguration": {
                "AzureQosEnabled": false,
                "ConfigurationPending": true
            }
        }
    },
    "PartNumber": "73-20185-03",
    "SerialNumber": "FCH25337EE9",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunctionCollection.NetworkDeviceFunctionCollection",
    "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions",
    "@odata.type": "#NetworkDeviceFunctionCollection.NetworkDeviceFunctionCollection",
    "Description": "Collection of NetworkDeviceFunction resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/esxi-trunk-2"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/esxi-trunk-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/fc0"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/fc1"
        }
    ],
    "Members@odata.count": 4,
    "Name": "NetworkDeviceFunction Collection"
}
```

## /api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/esxi-trunk-1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/esxi-trunk-1",
    "@odata.type": "#NetworkDeviceFunction.v1_5_0.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-2"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 2,
    "BootMode": "Disabled",
    "Ethernet": {
        "MACAddress": "00:25:B5:CD:32:0D",
        "MTUSize": 9000,
        "VLAN": {
            "VLANEnable": false
        }
    },
    "Id": "esxi-trunk-1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-2"
        }
    },
    "Name": "esxi-trunk-1",
    "NetDevFuncCapabilities": [
        "Ethernet",
        "iSCSI"
    ],
    "NetDevFuncType": "Ethernet",
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
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/esxi-trunk-2

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/esxi-trunk-2",
    "@odata.type": "#NetworkDeviceFunction.v1_5_0.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-2"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 2,
    "BootMode": "Disabled",
    "Ethernet": {
        "MACAddress": "00:25:B5:CD:32:0C",
        "MTUSize": 9000,
        "VLAN": {
            "VLANEnable": false
        }
    },
    "Id": "esxi-trunk-2",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-1"
        }
    },
    "Name": "esxi-trunk-2",
    "NetDevFuncCapabilities": [
        "Ethernet",
        "iSCSI"
    ],
    "NetDevFuncType": "Ethernet",
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
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/fc0

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/fc0",
    "@odata.type": "#NetworkDeviceFunction.v1_5_0.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-2"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 2,
    "BootMode": "Disabled",
    "Ethernet": {
        "MACAddress": "00:25:B5:CC:AA:03",
        "VLAN": {
            "VLANEnable": false
        }
    },
    "FibreChannel": {
        "WWNN": "20:00:00:25:B5:CC:CC:03",
        "WWNSource": "ConfiguredLocally",
        "WWPN": "20:00:00:25:B5:CC:AA:03"
    },
    "Id": "fc0",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-2"
        }
    },
    "Name": "fc0",
    "NetDevFuncCapabilities": [
        "FibreChannelOverEthernet"
    ],
    "NetDevFuncType": "FibreChannelOverEthernet",
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
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/fc1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkDeviceFunctions/fc1",
    "@odata.type": "#NetworkDeviceFunction.v1_5_0.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-2"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 2,
    "BootMode": "Disabled",
    "Ethernet": {
        "MACAddress": "00:25:B5:CC:BB:03",
        "VLAN": {
            "VLANEnable": false
        }
    },
    "FibreChannel": {
        "WWNN": "20:00:00:25:B5:CC:CC:03",
        "WWNSource": "ConfiguredLocally",
        "WWPN": "20:00:00:25:B5:CC:BB:03"
    },
    "Id": "fc1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-1"
        }
    },
    "Name": "fc1",
    "NetDevFuncCapabilities": [
        "FibreChannelOverEthernet"
    ],
    "NetDevFuncType": "FibreChannelOverEthernet",
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
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPortCollection.NetworkPortCollection",
    "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts",
    "@odata.type": "#NetworkPortCollection.NetworkPortCollection",
    "Description": "Collection of NetworkPort resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-2"
        }
    ],
    "Members@odata.count": 2,
    "Name": "NetworkPort Collection"
}
```

## /api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPort.NetworkPort",
    "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-1",
    "@odata.type": "#NetworkPort.v1_3_0.NetworkPort",
    "AssociatedNetworkAddresses": [
        "D4:77:98:A8:D0:E8"
    ],
    "CurrentLinkSpeedMbps": 25000,
    "Id": "Port-1",
    "LinkStatus": "Up",
    "Name": "Port-1",
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VicPort": {
                "AdminLinkSpeed": "Auto"
            }
        }
    },
    "PhysicalPortNumber": "1",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-2

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPort.NetworkPort",
    "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/NetworkAdapters/UCSX-V4-Q25GML_FCH25337EE9/NetworkPorts/Port-2",
    "@odata.type": "#NetworkPort.v1_3_0.NetworkPort",
    "AssociatedNetworkAddresses": [
        "D4:77:98:A8:D0:E9"
    ],
    "CurrentLinkSpeedMbps": 25000,
    "Id": "Port-2",
    "LinkStatus": "Up",
    "Name": "Port-2",
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "VicPort": {
                "AdminLinkSpeed": "Auto"
            }
        }
    },
    "PhysicalPortNumber": "2",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/Power

```{
    "@odata.context": "/redfish/v1/$metadata#Power.Power",
    "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Power",
    "@odata.type": "#Power.v1_6_1.Power",
    "Description": "Host Power Information",
    "Id": "Power",
    "Name": "Power",
    "PowerControl": [
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Power#/PowerControl/0",
            "MemberId": "0",
            "Name": "POWER_USAGE",
            "PowerConsumedWatts": 259
        }
    ],
    "PowerControl@odata.count": 1,
    "Voltages": [
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Power#/Voltages/0",
            "LowerThresholdCritical": 11.269000053405762,
            "LowerThresholdFatal": 10.79699993133545,
            "MemberId": "0",
            "Name": "P12V",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 12.095000267028809,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 12.6850004196167,
            "UpperThresholdFatal": 13.156999588012695
        }
    ],
    "Voltages@odata.count": 1
}
```

## /api-explorer/resources/redfish/v1/Chassis/FCH25337EHM/Thermal

```{
    "@odata.context": "/redfish/v1/$metadata#Thermal.Thermal",
    "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal",
    "@odata.type": "#Thermal.v1_6_2.Thermal",
    "Description": "Represents the properties for Temperature",
    "Id": "Thermal",
    "Name": "Thermal",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Temperatures": [
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/0",
            "MemberId": "0",
            "Name": "TEMP_FRONT",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 15,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 45,
            "UpperThresholdFatal": 50
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/1",
            "MemberId": "1",
            "Name": "TEMP_REAR_TOP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 25,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/2",
            "MemberId": "2",
            "Name": "TEMP_REAR_MID",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 33,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/3",
            "MemberId": "3",
            "Name": "TEMP_REAR_BOT",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 21,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/4",
            "MemberId": "4",
            "Name": "P1_TEMP_SENS",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 43.5,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 101,
            "UpperThresholdFatal": 102
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/5",
            "MemberId": "5",
            "Name": "P2_TEMP_SENS",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 53,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 101,
            "UpperThresholdFatal": 102
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/6",
            "MemberId": "6",
            "Name": "DDR4_P1_A1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 26,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/7",
            "MemberId": "7",
            "Name": "DDR4_P1_A2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/8",
            "MemberId": "8",
            "Name": "DDR4_P1_B1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/9",
            "MemberId": "9",
            "Name": "DDR4_P1_B2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/10",
            "MemberId": "10",
            "Name": "DDR4_P1_C1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/11",
            "MemberId": "11",
            "Name": "DDR4_P1_C2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/12",
            "MemberId": "12",
            "Name": "DDR4_P1_D1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/13",
            "MemberId": "13",
            "Name": "DDR4_P1_D2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/14",
            "MemberId": "14",
            "Name": "DDR4_P1_E1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/15",
            "MemberId": "15",
            "Name": "DDR4_P1_E2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/16",
            "MemberId": "16",
            "Name": "DDR4_P1_F1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/17",
            "MemberId": "17",
            "Name": "DDR4_P1_F2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/18",
            "MemberId": "18",
            "Name": "DDR4_P1_G1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/19",
            "MemberId": "19",
            "Name": "DDR4_P1_G2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/20",
            "MemberId": "20",
            "Name": "DDR4_P1_H1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/21",
            "MemberId": "21",
            "Name": "DDR4_P1_H2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/22",
            "MemberId": "22",
            "Name": "DDR4_P2_A1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 27,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/23",
            "MemberId": "23",
            "Name": "DDR4_P2_A2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/24",
            "MemberId": "24",
            "Name": "DDR4_P2_B1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/25",
            "MemberId": "25",
            "Name": "DDR4_P2_B2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/26",
            "MemberId": "26",
            "Name": "DDR4_P2_C1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/27",
            "MemberId": "27",
            "Name": "DDR4_P2_C2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/28",
            "MemberId": "28",
            "Name": "DDR4_P2_D1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/29",
            "MemberId": "29",
            "Name": "DDR4_P2_D2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/30",
            "MemberId": "30",
            "Name": "DDR4_P2_E1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/31",
            "MemberId": "31",
            "Name": "DDR4_P2_E2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/32",
            "MemberId": "32",
            "Name": "DDR4_P2_F1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/33",
            "MemberId": "33",
            "Name": "DDR4_P2_F2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/34",
            "MemberId": "34",
            "Name": "DDR4_P2_G1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/35",
            "MemberId": "35",
            "Name": "DDR4_P2_G2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/36",
            "MemberId": "36",
            "Name": "DDR4_P2_H1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/37",
            "MemberId": "37",
            "Name": "DDR4_P2_H2_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdFatal": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/38",
            "MemberId": "38",
            "Name": "PWR_BRICK_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 52,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/39",
            "MemberId": "39",
            "Name": "NOEVALLEY_PD0_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 38,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/40",
            "MemberId": "40",
            "Name": "NOEVALLEY_PD1_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 37,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ],
    "Temperatures@odata.count": 41
}
```

