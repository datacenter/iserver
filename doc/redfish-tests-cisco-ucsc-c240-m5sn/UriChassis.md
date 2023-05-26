# Resource: /redfish/v1/Chassis

Vendor | Model
--- | ---
Cisco | UCSC-C240-M5SN

## /redfish/v1/Chassis

```{
    "@odata.context": "/redfish/v1/$metadata#ChassisCollection.ChassisCollection",
    "@odata.id": "/redfish/v1/Chassis",
    "@odata.type": "#ChassisCollection.ChassisCollection",
    "Description": "Collection of Chassis",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Chassis Collection"
}
```

## /redfish/v1/Chassis/1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/1",
    "@odata.type": "#Chassis.v1_10_0.Chassis",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/1/Assembly"
    },
    "AssetTag": "022C2F7",
    "ChassisType": "Rack",
    "DepthMm": 766,
    "Description": "It represents the properties for physical components for any system.  This one object is intended to represent racks, rackmount servers, blades, standalone, modular systems, enclosures, and all other containers.  The non-cpu/device centric parts of the schema are all accessed either directly or indirectly through this resource",
    "HeightMm": 87,
    "Id": "1",
    "IndicatorLED": "Off",
    "Links": {
        "ComputerSystems": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4"
            }
        ],
        "CooledBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/Thermal"
            }
        ],
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12"
            },
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
        "ManagedBy": [
            {
                "@odata.id": "/redfish/v1/Managers/CIMC"
            }
        ],
        "PoweredBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/Power"
            }
        ],
        "Storage": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID"
            }
        ]
    },
    "Location": {
        "Contacts": [],
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
    "LogServices": {
        "@odata.id": "/redfish/v1/Chassis/1/LogServices"
    },
    "Manufacturer": "Cisco Systems Inc.",
    "Model": "UCS C240 M5SN",
    "Name": "Computer System Chassis",
    "NetworkAdapters": {
        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters"
    },
    "PCIeDevices": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices"
    },
    "Power": {
        "@odata.id": "/redfish/v1/Chassis/1/Power"
    },
    "PowerState": "On",
    "SerialNumber": "WZP23400AK4",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/1/Thermal"
    },
    "UUID": "B813910F-BFD2-439F-9C3B-75B376C5B160",
    "WidthMm": 482
}
```

## /redfish/v1/Chassis/1/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSC-C240-M5SN",
            "PartNumber": "74-106032-02",
            "PhysicalContext": "Chassis",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "WZP23400AK4",
            "Version": "V02"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Assembly#/Assemblies/1",
            "MemberId": "1",
            "Model": "UCSC-C240-M5SN",
            "PartNumber": "74-105773-01",
            "PhysicalContext": "SystemBoard",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "WZP2339Z335",
            "Version": "V02"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /redfish/v1/Chassis/1/LogServices

```
```

## /redfish/v1/Chassis/1/NetworkAdapters

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkAdapterCollection.NetworkAdapterCollection",
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters",
    "@odata.type": "#NetworkAdapterCollection.NetworkAdapterCollection",
    "Description": "Collection of NetworkAdapter resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "NetworkAdapter Collection"
}
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkAdapter.NetworkAdapter",
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1",
    "@odata.type": "#NetworkAdapter.v1_2_0.NetworkAdapter",
    "Actions": {
        "#NetworkAdapter.ResetSettingsToDefault": {
            "target": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/Actions/NetworkAdapter.ResetSettingsToDefault"
        }
    },
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/Assembly"
    },
    "Controllers": [
        {
            "ControllerCapabilities": {
                "NetworkDeviceFunctionCount": 4,
                "NetworkPortCount": 4
            },
            "FirmwarePackageVersion": "5.1(3d)",
            "Links": {
                "NetworkDeviceFunctions": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/eth0"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/eth1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/fc0"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/fc1"
                    }
                ],
                "NetworkDeviceFunctions@odata.count": 4,
                "NetworkPorts": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-2"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-3"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-4"
                    }
                ],
                "NetworkPorts@odata.count": 4
            },
            "Location": {
                "PartLocation": {
                    "LocationType": "Slot",
                    "ServiceLabel": "SlotID:MLOM"
                }
            }
        }
    ],
    "Id": "UCSC-MLOM-C25Q-04_FCH24157DE1",
    "Manufacturer": "Cisco Systems Inc",
    "Model": "UCSC-MLOM-C25Q-04",
    "Name": "UCS VIC 1457",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts"
    },
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
    },
    "PartNumber": "73-19238-03",
    "SerialNumber": "FCH24157DE1",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/Assembly#/Assemblies/10",
            "MemberId": "10",
            "Model": "UCSC-MLOM-C25Q-04",
            "PartNumber": "73-19238-03",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FCH24157DE1",
            "Version": "V05"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunctionCollection.NetworkDeviceFunctionCollection",
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions",
    "@odata.type": "#NetworkDeviceFunctionCollection.NetworkDeviceFunctionCollection",
    "Description": "Collection of NetworkDeviceFunction resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/eth0"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/eth1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/fc0"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/fc1"
        }
    ],
    "Members@odata.count": 4,
    "Name": "NetworkDeviceFunction Collection"
}
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/eth0

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/eth0",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-3"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 2,
    "BootMode": "Disabled",
    "Ethernet": {
        "MACAddress": "3C:57:31:CC:14:0A",
        "MTUSize": 1500,
        "VLAN": {
            "VLANEnable": false
        }
    },
    "Id": "eth0",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-1"
        }
    },
    "Name": "eth0",
    "NetDevFuncCapabilities": [
        "Ethernet",
        "iSCSI"
    ],
    "NetDevFuncType": "Ethernet",
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
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/eth1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/eth1",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-3"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 2,
    "BootMode": "Disabled",
    "Ethernet": {
        "MACAddress": "3C:57:31:CC:14:0B",
        "MTUSize": 1500,
        "VLAN": {
            "VLANEnable": false
        }
    },
    "Id": "eth1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-3"
        }
    },
    "Name": "eth1",
    "NetDevFuncCapabilities": [
        "Ethernet",
        "iSCSI"
    ],
    "NetDevFuncType": "Ethernet",
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
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/fc0

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/fc0",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-3"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 2,
    "BootMode": "Disabled",
    "Ethernet": {
        "MACAddress": "3C:57:31:CC:14:0C",
        "VLAN": {
            "VLANEnable": false
        }
    },
    "FibreChannel": {
        "WWNN": "10:00:3C:57:31:CC:14:0C",
        "WWNSource": "ConfiguredLocally",
        "WWPN": "20:00:3C:57:31:CC:14:0C"
    },
    "Id": "fc0",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-1"
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
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/fc1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/fc1",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-3"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 2,
    "BootMode": "Disabled",
    "Ethernet": {
        "MACAddress": "3C:57:31:CC:14:0D",
        "VLAN": {
            "VLANEnable": false
        }
    },
    "FibreChannel": {
        "WWNN": "10:00:3C:57:31:CC:14:0D",
        "WWNSource": "ConfiguredLocally",
        "WWPN": "20:00:3C:57:31:CC:14:0D"
    },
    "Id": "fc1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-3"
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
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPortCollection.NetworkPortCollection",
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts",
    "@odata.type": "#NetworkPortCollection.NetworkPortCollection",
    "Description": "Collection of NetworkPort resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-2"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-3"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-4"
        }
    ],
    "Members@odata.count": 4,
    "Name": "NetworkPort Collection"
}
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPort.NetworkPort",
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-1",
    "@odata.type": "#NetworkPort.v1_2_0.NetworkPort",
    "AssociatedNetworkAddresses": [
        "3C:57:31:CC:14:02"
    ],
    "CurrentLinkSpeedMbps": 10000,
    "Id": "Port-1",
    "LinkStatus": "Up",
    "Name": "Port-1",
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
    },
    "PhysicalPortNumber": "1",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-2

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPort.NetworkPort",
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-2",
    "@odata.type": "#NetworkPort.v1_2_0.NetworkPort",
    "AssociatedNetworkAddresses": [
        "3C:57:31:CC:14:04"
    ],
    "Id": "Port-2",
    "LinkStatus": "Down",
    "Name": "Port-2",
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
    },
    "PhysicalPortNumber": "2",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-3

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPort.NetworkPort",
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-3",
    "@odata.type": "#NetworkPort.v1_2_0.NetworkPort",
    "AssociatedNetworkAddresses": [
        "3C:57:31:CC:14:03"
    ],
    "CurrentLinkSpeedMbps": 10000,
    "Id": "Port-3",
    "LinkStatus": "Up",
    "Name": "Port-3",
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
    },
    "PhysicalPortNumber": "3",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-4

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPort.NetworkPort",
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkPorts/Port-4",
    "@odata.type": "#NetworkPort.v1_2_0.NetworkPort",
    "AssociatedNetworkAddresses": [
        "3C:57:31:CC:14:05"
    ],
    "Id": "Port-4",
    "LinkStatus": "Down",
    "Name": "Port-4",
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
    },
    "PhysicalPortNumber": "4",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDeviceCollection.PCIeDeviceCollection",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices",
    "@odata.type": "#PCIeDeviceCollection.PCIeDeviceCollection",
    "Description": "Collection of PCIeDevice resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/6"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L"
        }
    ],
    "Members@odata.count": 5,
    "Name": "PCIeDevice Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/3

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80009E5D-1.823.2",
    "Id": "3",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3/PCIeFunctions/3"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/3/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3/PCIeFunctions/3"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/3/PCIeFunctions/3

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3/PCIeFunctions/3",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x158b",
    "Id": "3",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/3.2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/3.1"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
    "SubsystemId": "0x0225",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/6

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/6",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80009E5D-1.823.2",
    "Id": "6",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/6/PCIeFunctions/6"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/6/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/6/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/6/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/6/PCIeFunctions/6"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/6/PCIeFunctions/6

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/6/PCIeFunctions/6",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x158b",
    "Id": "6",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/6.2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/6.1"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/6"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
    "SubsystemId": "0x0225",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/L

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80001516-1.823.2",
    "Id": "L",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L/PCIeFunctions/L"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel X550 LOM",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/L/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L/PCIeFunctions/L"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/L/PCIeFunctions/L

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L/PCIeFunctions/L",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1563",
    "Id": "L",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/L.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces/L.2"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel X550 LOM",
    "SubsystemId": "0x01a4",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "N/A",
    "Id": "MLOM",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM/PCIeFunctions/MLOM"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco UCS VIC 1457 MLOM",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MLOM/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM/PCIeFunctions/MLOM"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MLOM/PCIeFunctions/MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM/PCIeFunctions/MLOM",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0042",
    "Id": "MLOM",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/eth0"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/eth1"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/fc0"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FCH24157DE1/NetworkDeviceFunctions/fc1"
            }
        ],
        "NetworkDeviceFunctions@odata.count": 4,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Cisco UCS VIC 1457 MLOM",
    "SubsystemId": "0x0218",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1137"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "51.10.0-3612",
    "Id": "MRAID",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID/PCIeFunctions/MRAID"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MRAID/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID/PCIeFunctions/MRAID"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MRAID/PCIeFunctions/MRAID

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID/PCIeFunctions/MRAID",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0014",
    "Id": "MRAID",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/7"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/8"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/9"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/10"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/11"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/12"
            },
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
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/19"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/20"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/21"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/22"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/23"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/24"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/25"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID/Drives/26"
            }
        ],
        "Drives@odata.count": 26,
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP23400AK4/Storage/MRAID"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
    "SubsystemId": "0x020e",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1000"
}
```

## /redfish/v1/Chassis/1/Power

```{
    "@odata.context": "/redfish/v1/$metadata#Power.Power",
    "@odata.id": "/redfish/v1/Chassis/1/Power",
    "@odata.type": "#Power.v1_5_1.Power",
    "Description": "Power",
    "Id": "Power",
    "Name": "Power",
    "PowerControl": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/1",
            "MemberId": "1",
            "PhysicalContext": "PowerSupply",
            "PowerConsumedWatts": 324,
            "PowerLimit": {
                "LimitException": "NoAction"
            },
            "PowerMetrics": {
                "AverageConsumedWatts": 349,
                "MaxConsumedWatts": 495,
                "MinConsumedWatts": 186
            }
        }
    ],
    "PowerSupplies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/PSU1",
            "FirmwareVersion": "10062019",
            "InputRanges": [
                {
                    "InputType": "AC",
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 90,
                    "OutputWattage": 1050
                }
            ],
            "LastPowerOutputWatts": 155,
            "LineInputVoltage": 231,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "1",
            "Model": "PS-2112-9S-LF",
            "Name": "PSU1",
            "PartNumber": "341-0638-03",
            "PowerInputWatts": 173,
            "PowerOutputWatts": 155,
            "PowerSupplyType": "AC",
            "SerialNumber": "LIT241244RQ",
            "SparePartNumber": "341-0638-03",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/PSU2",
            "FirmwareVersion": "10062019",
            "InputRanges": [
                {
                    "InputType": "AC",
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 90,
                    "OutputWattage": 1050
                }
            ],
            "LastPowerOutputWatts": 152,
            "LineInputVoltage": 229,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "2",
            "Model": "PS-2112-9S-LF",
            "Name": "PSU2",
            "PartNumber": "341-0638-03",
            "PowerInputWatts": 176,
            "PowerOutputWatts": 152,
            "PowerSupplyType": "AC",
            "SerialNumber": "LIT241242TS",
            "SparePartNumber": "341-0638-03",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ],
    "Voltages": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/Voltages/PSU1_VOUT",
            "MemberId": "1",
            "Name": "PSU1_VOUT",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 12.2,
            "SensorNumber": 48,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 14
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/Voltages/PSU2_VOUT",
            "MemberId": "2",
            "Name": "PSU2_VOUT",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 12.2,
            "SensorNumber": 54,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 14
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/Voltages/P12V",
            "LowerThresholdCritical": 10.788,
            "MemberId": "3",
            "Name": "P12V",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 11.89,
            "SensorNumber": 210,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 13.166
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/Voltages/P3V_BAT_SCALED",
            "LowerThresholdCritical": 2.543,
            "MemberId": "4",
            "Name": "P3V_BAT_SCALED",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 3.026,
            "SensorNumber": 211,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 3.588
        }
    ]
}
```

## /redfish/v1/Chassis/1/Thermal

```{
    "@odata.context": "/redfish/v1/$metadata#Thermal.Thermal",
    "@odata.id": "/redfish/v1/Chassis/1/Thermal",
    "@odata.type": "#Thermal.v1_5_0.Thermal",
    "Description": "Represents the properties for Temperature and Cooling",
    "Fans": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD1_FAN1",
            "MemberId": "1",
            "Name": "MOD1_FAN1_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7070,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD1_FAN2",
            "MemberId": "2",
            "Name": "MOD1_FAN2_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7350,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD2_FAN1",
            "MemberId": "3",
            "Name": "MOD2_FAN1_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 6868,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD2_FAN2",
            "MemberId": "4",
            "Name": "MOD2_FAN2_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7056,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD3_FAN1",
            "MemberId": "5",
            "Name": "MOD3_FAN1_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 6868,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD3_FAN2",
            "MemberId": "6",
            "Name": "MOD3_FAN2_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7056,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD4_FAN1",
            "MemberId": "7",
            "Name": "MOD4_FAN1_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7070,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD4_FAN2",
            "MemberId": "8",
            "Name": "MOD4_FAN2_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7056,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD5_FAN1",
            "MemberId": "9",
            "Name": "MOD5_FAN1_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 6868,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD5_FAN2",
            "MemberId": "10",
            "Name": "MOD5_FAN2_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7056,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD6_FAN1",
            "MemberId": "11",
            "Name": "MOD6_FAN1_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7070,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD6_FAN2",
            "MemberId": "12",
            "Name": "MOD6_FAN2_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7056,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD7_FAN1",
            "MemberId": "13",
            "Name": "MOD7_FAN1_SPEED",
            "Status": {
                "State": "Absent"
            }
        }
    ],
    "Fans@odata.count": 13,
    "Id": "Thermal",
    "Name": "Thermal",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Temperatures": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/MLOM_TEMP",
            "MemberId": "1",
            "Name": "MLOM_TEMP",
            "PhysicalContext": "NetworkingDevice",
            "ReadingCelsius": 54,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 60,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/TEMP_SENS_FRONT",
            "MemberId": "2",
            "Name": "TEMP_SENS_FRONT",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 26,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 84,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 45
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P1_A1_TMP",
            "MemberId": "3",
            "Name": "DDR4_P1_A1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 30,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 114,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P1_B1_TMP",
            "MemberId": "4",
            "Name": "DDR4_P1_B1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 29,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 120,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P1_C1_TMP",
            "MemberId": "5",
            "Name": "DDR4_P1_C1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 29,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 126,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P1_D1_TMP",
            "MemberId": "6",
            "Name": "DDR4_P1_D1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 29,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 132,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P1_E1_TMP",
            "MemberId": "7",
            "Name": "DDR4_P1_E1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 29,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 138,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P1_F1_TMP",
            "MemberId": "8",
            "Name": "DDR4_P1_F1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 29,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 144,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P2_G1_TMP",
            "MemberId": "9",
            "Name": "DDR4_P2_G1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 28,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 150,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P2_H1_TMP",
            "MemberId": "10",
            "Name": "DDR4_P2_H1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 28,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 156,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P2_J1_TMP",
            "MemberId": "11",
            "Name": "DDR4_P2_J1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 29,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 162,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P2_K1_TMP",
            "MemberId": "12",
            "Name": "DDR4_P2_K1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 29,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 168,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P2_L1_TMP",
            "MemberId": "13",
            "Name": "DDR4_P2_L1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 28,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 174,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P2_M1_TMP",
            "MemberId": "14",
            "Name": "DDR4_P2_M1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 29,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 180,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/P1_TEMP_SENS",
            "MemberId": "15",
            "Name": "P1_TEMP_SENS",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 40,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 196,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 100
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/P2_TEMP_SENS",
            "MemberId": "16",
            "Name": "P2_TEMP_SENS",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 43,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 197,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 100
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/PSU1_TEMP",
            "MemberId": "17",
            "Name": "PSU1_TEMP",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 24,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 207,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 65
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/PSU2_TEMP",
            "MemberId": "18",
            "Name": "PSU2_TEMP",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 21,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 208,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 65
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/PCH_TEMP_SENS",
            "MemberId": "19",
            "Name": "PCH_TEMP_SENS",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 34,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 209,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/PCIE_SWITCH_TMP",
            "MemberId": "20",
            "Name": "PCIE_SWITCH_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 40,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 239,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 100
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/RISER1_TEMP",
            "MemberId": "21",
            "Name": "RISER1_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 24,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 245,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 70
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/RISER2_TEMP",
            "MemberId": "22",
            "Name": "RISER2_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 29,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 246,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 70
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/RISER2_INLET_TMP",
            "MemberId": "23",
            "Name": "RISER2_INLET_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 33,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 249,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 70
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/RISER1_INLET_TMP",
            "MemberId": "24",
            "Name": "RISER1_INLET_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 33,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 250,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 70
        }
    ],
    "Temperatures@odata.count": 24
}
```

