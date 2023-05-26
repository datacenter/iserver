# Resource: /redfish/v1/Chassis

Vendor | Model
--- | ---
Cisco | UCSS-S3260

## /redfish/v1/Chassis

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis",
    "@odata.id": "/redfish/v1/Chassis",
    "@odata.type": "#ChassisCollection.ChassisCollection",
    "Description": "Collection of Chassis",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/CMC"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Chassis Collection"
}
```

## /redfish/v1/Chassis/CMC

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/CMC",
    "@odata.type": "#Chassis.v1_10_0.Chassis",
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/CMC/Actions/Chassis.Reset"
        }
    },
    "AssetTag": "022C221",
    "ChassisType": "Enclosure",
    "DepthMm": 813,
    "Description": "It represents the properties for physical components for any system.  This one object is intended to represent racks, rackmount servers, blades, standalone, modular systems, enclosures, and all other containers.  The non-cpu/device centric parts of the schema are all accessed either directly or indirectly through this resource",
    "HeightMm": 174,
    "Id": "CMC",
    "IndicatorLED": "Off",
    "Links": {
        "CooledBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/CMC/Thermal"
            }
        ],
        "ManagedBy": [
            {
                "@odata.id": "/redfish/v1/Managers/CIMC"
            }
        ],
        "ManagersInChassis": [
            {
                "@odata.id": "/redfish/v1/Managers/BMC1"
            }
        ],
        "PoweredBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/CMC/Power"
            }
        ]
    },
    "LogServices": {
        "@odata.id": "/redfish/v1/Chassis/CMC/LogServices"
    },
    "Manufacturer": "Cisco Systems Inc.",
    "Model": "UCS S3260",
    "Name": "CMC",
    "NetworkAdapters": {
        "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters"
    },
    "PCIeDevices": {
        "@odata.id": "/redfish/v1/Chassis/CMC/PCIeDevices"
    },
    "Power": {
        "@odata.id": "/redfish/v1/Chassis/CMC/Power"
    },
    "PowerState": "On",
    "SerialNumber": "FOX2034GCLV",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/CMC/Thermal"
    },
    "WeightKg": 88.45,
    "WidthMm": 444
}
```

## /redfish/v1/Chassis/CMC/LogServices

```
```

## /redfish/v1/Chassis/CMC/NetworkAdapters

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters",
    "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters",
    "@odata.type": "#NetworkAdapterCollection.NetworkAdapterCollection",
    "Description": "Collection of NetworkAdapter resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "NetworkAdapter Collection"
}
```

## /redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1",
    "@odata.type": "#NetworkAdapter.v1_2_0.NetworkAdapter",
    "Actions": {
        "#NetworkAdapter.ResetSettingsToDefault": {
            "target": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/Actions/NetworkAdapter.ResetSettingsToDefault"
        }
    },
    "Controllers": [
        {
            "ControllerCapabilities": {
                "NetworkDeviceFunctionCount": 4,
                "NetworkPortCount": 2
            },
            "FirmwarePackageVersion": "4.4(3a)",
            "Links": {
                "NetworkDeviceFunctions": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth0"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc0"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc1"
                    }
                ],
                "NetworkDeviceFunctions@odata.count": 4,
                "NetworkPorts": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts/Port-0"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts/Port-1"
                    }
                ],
                "NetworkPorts@odata.count": 2
            }
        }
    ],
    "Id": "UCSC-C3260-SIOC",
    "Manufacturer": "Cisco Systems Inc",
    "Model": "UCSS-S3260-SIOC",
    "Name": "Adapter Card SIOC1",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts"
    },
    "PartNumber": "73-16644-04",
    "SerialNumber": "FCH20487P5X"
}
```

## /redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkDeviceFunctions",
    "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions",
    "@odata.type": "#NetworkDeviceFunctionCollection.NetworkDeviceFunctionCollection",
    "Description": "Collection of NetworkDeviceFunction resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth0"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc0"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc1"
        }
    ],
    "Members@odata.count": 4,
    "Name": "NetworkDeviceFunction Collection"
}
```

## /redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth0

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkDeviceFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth0",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "2C:5A:0F:6F:6C:00",
        "MTUSize": 9000,
        "VLAN": {
            "VLANEnable": true
        }
    },
    "Id": "eth0",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts/Port-0"
        }
    },
    "Name": "eth0"
}
```

## /redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkDeviceFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth1",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "2C:5A:0F:6F:6C:01",
        "MTUSize": 9000,
        "VLAN": {
            "VLANEnable": true
        }
    },
    "Id": "eth1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts/Port-1"
        }
    },
    "Name": "eth1"
}
```

## /redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc0

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkDeviceFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc0",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "2C:5A:0F:6F:6C:02"
    },
    "FibreChannel": {
        "BootTargets": [],
        "WWNN": "10:00:2C:5A:0F:6F:6C:02",
        "WWNSource": "ConfiguredLocally",
        "WWPN": "20:00:2C:5A:0F:6F:6C:02"
    },
    "Id": "fc0",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts/Port-0"
        }
    },
    "Name": "fc0"
}
```

## /redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkDeviceFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc1",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "2C:5A:0F:6F:6C:03"
    },
    "FibreChannel": {
        "BootTargets": [],
        "WWNN": "10:00:2C:5A:0F:6F:6C:03",
        "WWNSource": "ConfiguredLocally",
        "WWPN": "20:00:2C:5A:0F:6F:6C:03"
    },
    "Id": "fc1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts/Port-1"
        }
    },
    "Name": "fc1"
}
```

## /redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkPorts",
    "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts",
    "@odata.type": "#NetworkPortCollection.NetworkPortCollection",
    "Description": "Collection of NetworkPort resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts/Port-0"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts/Port-1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "NetworkPort Collection"
}
```

## /redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts/Port-0

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkPorts/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts/Port-0",
    "@odata.type": "#NetworkPort.v1_2_0.NetworkPort",
    "AssociatedNetworkAddresses": [
        "2C:5A:0F:6F:6B:F4"
    ],
    "Id": "0",
    "LinkStatus": "Up",
    "Name": "Port-0",
    "PhysicalPortNumber": "0",
    "SupportedLinkCapabilities": [
        {
            "LinkNetworkTechnology": "Ethernet"
        }
    ]
}
```

## /redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts/Port-1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkPorts/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/CMC/NetworkAdapters/SIOC1/NetworkPorts/Port-1",
    "@odata.type": "#NetworkPort.v1_2_0.NetworkPort",
    "AssociatedNetworkAddresses": [
        "2C:5A:0F:6F:6B:F5"
    ],
    "Id": "1",
    "LinkStatus": "Up",
    "Name": "Port-1",
    "PhysicalPortNumber": "1",
    "SupportedLinkCapabilities": [
        {
            "LinkNetworkTechnology": "Ethernet"
        }
    ]
}
```

## /redfish/v1/Chassis/CMC/PCIeDevices

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices",
    "@odata.id": "/redfish/v1/Chassis/CMC/PCIeDevices",
    "@odata.type": "#PCIeDeviceCollection.PCIeDeviceCollection",
    "Description": "Collection of PCIeDevice resource instances for this system",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "PCIeDevice Collection"
}
```

## /redfish/v1/Chassis/CMC/Power

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/Power",
    "@odata.id": "/redfish/v1/Chassis/CMC/Power",
    "@odata.type": "#Power.v1_5_1.Power",
    "Description": "Power",
    "Id": "Power",
    "Name": "Power",
    "PowerControl": [
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/PowerControl/1",
            "MemberId": "1",
            "PhysicalContext": "PowerSupply",
            "PowerConsumedWatts": 392,
            "PowerLimit": {
                "LimitInWatts": 931
            },
            "PowerMetrics": {
                "AverageConsumedWatts": 361,
                "MaxConsumedWatts": 642,
                "MinConsumedWatts": 249
            }
        }
    ],
    "PowerSupplies": [
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/PowerSupplies/PSU1",
            "FirmwareVersion": "10062019",
            "InputRanges": [
                {
                    "InputType": "AC",
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 180,
                    "OutputWattage": 1050
                }
            ],
            "LastPowerOutputWatts": 96,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "1",
            "Model": "PS-2112-9S-LF",
            "Name": "PSU1",
            "PowerInputWatts": 103,
            "PowerOutputWatts": 96,
            "PowerSupplyType": "AC",
            "SerialNumber": "LIT20422447",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/PowerSupplies/PSU2",
            "FirmwareVersion": "10062019",
            "InputRanges": [
                {
                    "InputType": "AC",
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 180,
                    "OutputWattage": 1050
                }
            ],
            "LastPowerOutputWatts": 82,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "2",
            "Model": "PS-2112-9S-LF",
            "Name": "PSU2",
            "PowerInputWatts": 95,
            "PowerOutputWatts": 82,
            "PowerSupplyType": "AC",
            "SerialNumber": "LIT2042245H",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/PowerSupplies/PSU3",
            "FirmwareVersion": "10062019",
            "InputRanges": [
                {
                    "InputType": "AC",
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 180,
                    "OutputWattage": 1050
                }
            ],
            "LastPowerOutputWatts": 89,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "3",
            "Model": "PS-2112-9S-LF",
            "Name": "PSU3",
            "PowerInputWatts": 109,
            "PowerOutputWatts": 89,
            "PowerSupplyType": "AC",
            "SerialNumber": "LIT204224DH",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/PowerSupplies/PSU4",
            "FirmwareVersion": "10062019",
            "InputRanges": [
                {
                    "InputType": "AC",
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 180,
                    "OutputWattage": 1050
                }
            ],
            "LastPowerOutputWatts": 101,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "4",
            "Model": "PS-2112-9S-LF",
            "Name": "PSU4",
            "PowerInputWatts": 118,
            "PowerOutputWatts": 101,
            "PowerSupplyType": "AC",
            "SerialNumber": "LIT2042243U",
            "Status": {
                "State": "Enabled"
            }
        }
    ],
    "Voltages": [
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/SIOC1_P12V",
            "LowerThresholdCritical": 11.22,
            "MemberId": "1",
            "Name": "SIOC1_P12V",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 12,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 12.72
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/SIOC1_P1V0",
            "LowerThresholdCritical": 0.944,
            "MemberId": "2",
            "Name": "SIOC1_P1V0",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.064
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/SIOC1_P1V2",
            "LowerThresholdCritical": 1.128,
            "MemberId": "3",
            "Name": "SIOC1_P1V2",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1.2,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.272
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/SIOC1_P1V5",
            "LowerThresholdCritical": 1.41,
            "MemberId": "4",
            "Name": "SIOC1_P1V5",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1.5,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.59
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/SIOC1_P2V5",
            "LowerThresholdCritical": 2.338,
            "MemberId": "5",
            "Name": "SIOC1_P2V5",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 2.492,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 2.646
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/SIOC1_P3V3",
            "LowerThresholdCritical": 3.1,
            "MemberId": "6",
            "Name": "SIOC1_P3V3",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 3.34,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 3.5
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/SIOC1_P12V_STBY",
            "LowerThresholdCritical": 11.28,
            "MemberId": "7",
            "Name": "SIOC1_P12V_STBY",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 12.12,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 12.72
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/SIOC1_P3V3_STBY",
            "LowerThresholdCritical": 3.14,
            "MemberId": "8",
            "Name": "SIOC1_P3V3_STBY",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 3.36,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 3.46
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/PSU1_VIN",
            "MemberId": "9",
            "Name": "PSU1_VIN",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 236,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 264
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/PSU2_VIN",
            "MemberId": "10",
            "Name": "PSU2_VIN",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 238,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 264
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/PSU3_VIN",
            "MemberId": "11",
            "Name": "PSU3_VIN",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 242,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 264
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/PSU4_VIN",
            "MemberId": "12",
            "Name": "PSU4_VIN",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 244,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 264
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/P5V_1",
            "LowerThresholdCritical": 4.5,
            "MemberId": "13",
            "Name": "P5V_1",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 5.01,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 5.64
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/P5V_2",
            "LowerThresholdCritical": 4.5,
            "MemberId": "14",
            "Name": "P5V_2",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 5.01,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 5.64
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/P5V_3",
            "LowerThresholdCritical": 4.5,
            "MemberId": "15",
            "Name": "P5V_3",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 5.01,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 5.64
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/P5V_4",
            "LowerThresholdCritical": 4.5,
            "MemberId": "16",
            "Name": "P5V_4",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 5.01,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 5.64
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/P0V9_EXP1_VCORE",
            "LowerThresholdCritical": 0.836,
            "MemberId": "17",
            "Name": "P0V9_EXP1_VCORE",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0.92,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 0.976
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/P0V9_EXP2_VCORE",
            "LowerThresholdCritical": 0.836,
            "MemberId": "18",
            "Name": "P0V9_EXP2_VCORE",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0.92,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 0.976
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/P0V9_EXP1_AVD",
            "LowerThresholdCritical": 0.836,
            "MemberId": "19",
            "Name": "P0V9_EXP1_AVD",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0.92,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 0.976
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/P0V9_EXP2_AVD",
            "LowerThresholdCritical": 0.836,
            "MemberId": "20",
            "Name": "P0V9_EXP2_AVD",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0.936,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 0.976
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/PSU1_VOUT",
            "MemberId": "21",
            "Name": "PSU1_VOUT",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 12.2,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 14
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/PSU2_VOUT",
            "MemberId": "22",
            "Name": "PSU2_VOUT",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 12.1,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 14
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/PSU3_VOUT",
            "MemberId": "23",
            "Name": "PSU3_VOUT",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 12.1,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 14
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/PSU4_VOUT",
            "MemberId": "24",
            "Name": "PSU4_VOUT",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 12.1,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 14
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Power#/Voltages/SIOC1_RTC_BAT",
            "LowerThresholdCritical": 2.14,
            "MemberId": "25",
            "Name": "SIOC1_RTC_BAT",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 3.14,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 3.42
        }
    ]
}
```

## /redfish/v1/Chassis/CMC/Thermal

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/Thermal",
    "@odata.id": "/redfish/v1/Chassis/CMC/Thermal",
    "@odata.type": "#Thermal.v1_5_0.Thermal",
    "Description": "Represents the properties for Temperature and Cooling",
    "Fans": [
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Fans/FAN1",
            "LowerThresholdCritical": 1800,
            "LowerThresholdNonCritical": 2040,
            "MemberId": "1",
            "Name": "FAN1_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7920,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Fans/FAN2",
            "LowerThresholdCritical": 1800,
            "LowerThresholdNonCritical": 2040,
            "MemberId": "2",
            "Name": "FAN2_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7920,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Fans/FAN3",
            "LowerThresholdCritical": 1800,
            "LowerThresholdNonCritical": 2040,
            "MemberId": "3",
            "Name": "FAN3_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7920,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Fans/FAN4",
            "LowerThresholdCritical": 1800,
            "LowerThresholdNonCritical": 2040,
            "MemberId": "4",
            "Name": "FAN4_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7980,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Fans/FAN5",
            "LowerThresholdCritical": 1800,
            "LowerThresholdNonCritical": 2040,
            "MemberId": "5",
            "Name": "FAN5_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7920,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Fans/FAN6",
            "LowerThresholdCritical": 1800,
            "LowerThresholdNonCritical": 2040,
            "MemberId": "6",
            "Name": "FAN6_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7920,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Fans/FAN7",
            "LowerThresholdCritical": 1800,
            "LowerThresholdNonCritical": 2040,
            "MemberId": "7",
            "Name": "FAN7_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 7920,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Fans/FAN8",
            "LowerThresholdCritical": 1800,
            "LowerThresholdNonCritical": 2040,
            "MemberId": "8",
            "Name": "FAN8_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 8040,
            "ReadingUnits": "RPM",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ],
    "Fans@odata.count": 8,
    "Id": "Thermal",
    "Name": "Thermal",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Temperatures": [
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/SIOC1_BACK_TEMP",
            "MemberId": "1",
            "Name": "SIOC1_BACK_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 29,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/SIOC1_FRONT_TEMP",
            "MemberId": "2",
            "Name": "SIOC1_FRONT_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 33,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/SIOC1_MID_TEMP",
            "MemberId": "3",
            "Name": "SIOC1_MID_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 32,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/SIOC1_VIC_TEMP",
            "MemberId": "4",
            "Name": "SIOC1_VIC_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 34,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/MOBO_R_BOT_TEMP",
            "MemberId": "5",
            "Name": "MOBO_R_BOT_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 25,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/MOBO_L_BOT_TEMP",
            "MemberId": "6",
            "Name": "MOBO_L_BOT_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 25,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/MOBO_R_MID_TEMP",
            "MemberId": "7",
            "Name": "MOBO_R_MID_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 22,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 60
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/MOBO_R_IN_TEMP",
            "MemberId": "8",
            "Name": "MOBO_R_IN_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 22,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 45
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/MOBO_L_IN_TEMP",
            "MemberId": "9",
            "Name": "MOBO_L_IN_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 21,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 45
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/MOBO_L_MID_TEMP",
            "MemberId": "10",
            "Name": "MOBO_L_MID_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 22,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 60
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/MOBO_R_OUT_TEMP",
            "MemberId": "11",
            "Name": "MOBO_R_OUT_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 26,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 65
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/MOBO_L_OUT_TEMP",
            "MemberId": "12",
            "Name": "MOBO_L_OUT_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 23,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 65
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/PSU1_TEMP",
            "MemberId": "13",
            "Name": "PSU1_TEMP",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 18,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 55
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/PSU2_TEMP",
            "MemberId": "14",
            "Name": "PSU2_TEMP",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 20,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 55
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/PSU3_TEMP",
            "MemberId": "15",
            "Name": "PSU3_TEMP",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 19,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 55
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/PSU4_TEMP",
            "MemberId": "16",
            "Name": "PSU4_TEMP",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 17,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 55
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/SIOC1_CMC_TEMP",
            "MemberId": "17",
            "Name": "SIOC1_CMC_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 42,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/MOBO_R_EXP_TEMP",
            "MemberId": "18",
            "Name": "MOBO_R_EXP_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 33,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 90
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Temperatures/MOBO_L_EXP_TEMP",
            "MemberId": "19",
            "Name": "MOBO_L_EXP_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 34,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/CMC"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 90
        }
    ],
    "Temperatures@odata.count": 19
}
```

## /redfish/v1/Chassis/Server1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/Server1",
    "@odata.type": "#Chassis.v1_10_0.Chassis",
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Server1/Actions/Chassis.Reset"
        }
    },
    "ChassisType": "Enclosure",
    "DepthMm": 813,
    "Description": "It represents the properties for physical components for any system.  This one object is intended to represent racks, rackmount servers, blades, standalone, modular systems, enclosures, and all other containers.  The non-cpu/device centric parts of the schema are all accessed either directly or indirectly through this resource",
    "HeightMm": 174,
    "Id": "Server1",
    "IndicatorLED": "Off",
    "Links": {
        "ComputerSystems": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808"
            }
        ],
        "CooledBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/CMC/Thermal"
            }
        ],
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-7"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-8"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-9"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-10"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-11"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-12"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-13"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-14"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-15"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-55"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-56"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-201"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-202"
            }
        ],
        "ManagedBy": [
            {
                "@odata.id": "/redfish/v1/Managers/CIMC"
            },
            {
                "@odata.id": "/redfish/v1/Managers/BMC1"
            }
        ],
        "PoweredBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/CMC/Power"
            }
        ],
        "Storage": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1"
            }
        ]
    },
    "LogServices": {
        "@odata.id": "/redfish/v1/Chassis/Server1/LogServices"
    },
    "Manufacturer": "Cisco Systems Inc.",
    "Model": "UCS S3260M4",
    "Name": "BMC",
    "NetworkAdapters": {
        "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters"
    },
    "PCIeDevices": {
        "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices"
    },
    "Power": {
        "@odata.id": "/redfish/v1/Chassis/Server1/Power"
    },
    "PowerState": "On",
    "SerialNumber": "FCH21067808",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/Server1/Thermal"
    },
    "UUID": "937E6EE7-0EA5-42CE-9EAE-A960BF1F0BAD",
    "WeightKg": 88.45,
    "WidthMm": 444
}
```

## /redfish/v1/Chassis/Server1/LogServices

```
```

## /redfish/v1/Chassis/Server1/NetworkAdapters

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters",
    "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters",
    "@odata.type": "#NetworkAdapterCollection.NetworkAdapterCollection",
    "Description": "Collection of NetworkAdapter resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "NetworkAdapter Collection"
}
```

## /redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1",
    "@odata.type": "#NetworkAdapter.v1_2_0.NetworkAdapter",
    "Actions": {
        "#NetworkAdapter.ResetSettingsToDefault": {
            "target": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/Actions/NetworkAdapter.ResetSettingsToDefault"
        }
    },
    "Controllers": [
        {
            "ControllerCapabilities": {
                "NetworkDeviceFunctionCount": 4,
                "NetworkPortCount": 2
            },
            "FirmwarePackageVersion": "4.4(3a)",
            "Links": {
                "NetworkDeviceFunctions": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth0"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc0"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc1"
                    }
                ],
                "NetworkDeviceFunctions@odata.count": 4,
                "NetworkPorts": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkPorts/Port-0"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkPorts/Port-1"
                    }
                ],
                "NetworkPorts@odata.count": 2
            }
        }
    ],
    "Id": "UCSC-C3260-SIOC",
    "Manufacturer": "Cisco Systems Inc",
    "Model": "UCSS-S3260-SIOC",
    "Name": "Adapter Card SIOC1",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkPorts"
    },
    "PartNumber": "73-16644-04",
    "SerialNumber": "FCH20487P5X"
}
```

## /redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkDeviceFunctions",
    "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions",
    "@odata.type": "#NetworkDeviceFunctionCollection.NetworkDeviceFunctionCollection",
    "Description": "Collection of NetworkDeviceFunction resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth0"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc0"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc1"
        }
    ],
    "Members@odata.count": 4,
    "Name": "NetworkDeviceFunction Collection"
}
```

## /redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth0

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkDeviceFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth0",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "2C:5A:0F:6F:6C:00",
        "MTUSize": 9000,
        "VLAN": {
            "VLANEnable": true
        }
    },
    "Id": "eth0",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Systems/Server1/NetworkInterfaces/SIOC1/NetworkPorts/Port-0"
        }
    },
    "Name": "eth0"
}
```

## /redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkDeviceFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/eth1",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "2C:5A:0F:6F:6C:01",
        "MTUSize": 9000,
        "VLAN": {
            "VLANEnable": true
        }
    },
    "Id": "eth1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Systems/Server1/NetworkInterfaces/SIOC1/NetworkPorts/Port-1"
        }
    },
    "Name": "eth1"
}
```

## /redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc0

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkDeviceFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc0",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "2C:5A:0F:6F:6C:02"
    },
    "FibreChannel": {
        "BootTargets": [],
        "WWNN": "10:00:2C:5A:0F:6F:6C:02",
        "WWNSource": "ConfiguredLocally",
        "WWPN": "20:00:2C:5A:0F:6F:6C:02"
    },
    "Id": "fc0",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Systems/Server1/NetworkInterfaces/SIOC1/NetworkPorts/Port-0"
        }
    },
    "Name": "fc0"
}
```

## /redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkDeviceFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkDeviceFunctions/fc1",
    "@odata.type": "#NetworkDeviceFunction.v1_3_0.NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "2C:5A:0F:6F:6C:03"
    },
    "FibreChannel": {
        "BootTargets": [],
        "WWNN": "10:00:2C:5A:0F:6F:6C:03",
        "WWNSource": "ConfiguredLocally",
        "WWPN": "20:00:2C:5A:0F:6F:6C:03"
    },
    "Id": "fc1",
    "Links": {
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Systems/Server1/NetworkInterfaces/SIOC1/NetworkPorts/Port-1"
        }
    },
    "Name": "fc1"
}
```

## /redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkPorts

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkPorts",
    "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkPorts",
    "@odata.type": "#NetworkPortCollection.NetworkPortCollection",
    "Description": "Collection of NetworkPort resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkPorts/Port-0"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkPorts/Port-1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "NetworkPort Collection"
}
```

## /redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkPorts/Port-0

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkPorts/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkPorts/Port-0",
    "@odata.type": "#NetworkPort.v1_2_0.NetworkPort",
    "AssociatedNetworkAddresses": [
        "2C:5A:0F:6F:6B:F4"
    ],
    "Id": "0",
    "LinkStatus": "Up",
    "Name": "Port-0",
    "PhysicalPortNumber": "0",
    "SupportedLinkCapabilities": [
        {
            "LinkNetworkTechnology": "Ethernet"
        }
    ]
}
```

## /redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkPorts/Port-1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters/Members/$entity/NetworkPorts/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/Server1/NetworkAdapters/SIOC1/NetworkPorts/Port-1",
    "@odata.type": "#NetworkPort.v1_2_0.NetworkPort",
    "AssociatedNetworkAddresses": [
        "2C:5A:0F:6F:6B:F5"
    ],
    "Id": "1",
    "LinkStatus": "Up",
    "Name": "Port-1",
    "PhysicalPortNumber": "1",
    "SupportedLinkCapabilities": [
        {
            "LinkNetworkTechnology": "Ethernet"
        }
    ]
}
```

## /redfish/v1/Chassis/Server1/PCIeDevices

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices",
    "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices",
    "@odata.type": "#PCIeDeviceCollection.PCIeDeviceCollection",
    "Description": "Collection of PCIeDevice resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SIOC1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SBMezz1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "PCIeDevice Collection"
}
```

## /redfish/v1/Chassis/Server1/PCIeDevices/SBMezz1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SBMezz1",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "29.00.1-0360",
    "Id": "SBMezz1",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/Server1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SBMezz1/PCIeFunctions/SBMezz1"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco UCS C3000 RAID Controller for M4 Server",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SBMezz1/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/Server1/PCIeDevices/SBMezz1/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SBMezz1/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SBMezz1/PCIeFunctions/SBMezz1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/Server1/PCIeDevices/SBMezz1/PCIeFunctions/SBMezz1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SBMezz1/PCIeFunctions/SBMezz1",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x00ce",
    "Id": "SBMezz1",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-7"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-8"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-9"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-10"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-11"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-12"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-13"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-14"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-15"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-55"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-56"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-201"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1/Drives/PD-202"
            }
        ],
        "Drives@odata.count": 19,
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SBMezz1"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/Storage/SBMezz1"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "Cisco UCS C3000 RAID Controller for M4 Server",
    "SubsystemId": "0x0197",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1000"
}
```

## /redfish/v1/Chassis/Server1/PCIeDevices/SIOC1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SIOC1",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "4.4(3a)",
    "Id": "SIOC1",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/Server1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SIOC1/PCIeFunctions/SIOC1"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "UCSC-C3260-SIOC",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SIOC1/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/Server1/PCIeDevices/SIOC1/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SIOC1/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SIOC1/PCIeFunctions/SIOC1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/Server1/PCIeDevices/SIOC1/PCIeFunctions/SIOC1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SIOC1/PCIeFunctions/SIOC1",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0042",
    "Id": "SIOC1",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/EthernetInterfaces/SIOC1.0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/EthernetInterfaces/SIOC1.1"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/eth0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/eth1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/fc0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH21067808/NetworkInterfaces/SIOC1/NetworkDeviceFunctions/fc1"
            }
        ],
        "NetworkDeviceFunctions@odata.count": 4,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/Server1/PCIeDevices/SIOC1"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "UCSC-C3260-SIOC",
    "SubsystemId": "0x0157",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1137"
}
```

## /redfish/v1/Chassis/Server1/Power

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/Power",
    "@odata.id": "/redfish/v1/Chassis/Server1/Power",
    "@odata.type": "#Power.v1_5_1.Power",
    "Description": "Power",
    "Id": "Power",
    "Name": "Power",
    "PowerControl": [
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/PowerControl/1",
            "MemberId": "1",
            "PhysicalContext": "PowerSupply",
            "PowerLimit": {
                "LimitException": "NoAction"
            },
            "PowerMetrics": {
                "AverageConsumedWatts": 76,
                "MaxConsumedWatts": 195,
                "MinConsumedWatts": 62
            }
        }
    ],
    "Voltages": [
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P3V_BAT_SCALED",
            "LowerThresholdCritical": 2.158,
            "MemberId": "1",
            "Name": "P3V_BAT_SCALED",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 3.107,
            "SensorNumber": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P5V_STBY",
            "LowerThresholdCritical": 4.555,
            "MemberId": "2",
            "Name": "P5V_STBY",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 5.013,
            "SensorNumber": 1,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 5.471
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P3V3_STBY",
            "LowerThresholdCritical": 3.018,
            "MemberId": "3",
            "Name": "P3V3_STBY",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 3.286,
            "SensorNumber": 2,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 3.602
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P1V05_PCH_STBY",
            "LowerThresholdCritical": 0.96,
            "MemberId": "4",
            "Name": "P1V05_PCH_STBY",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1.029,
            "SensorNumber": 3,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.147
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P1V8_STBY",
            "LowerThresholdCritical": 1.637,
            "MemberId": "5",
            "Name": "P1V8_STBY",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1.774,
            "SensorNumber": 4,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.98
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P1V0_STBY",
            "LowerThresholdCritical": 0.911,
            "MemberId": "6",
            "Name": "P1V0_STBY",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0.98,
            "SensorNumber": 5,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.088
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P1V5_STBY",
            "LowerThresholdCritical": 1.372,
            "MemberId": "7",
            "Name": "P1V5_STBY",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1.48,
            "SensorNumber": 6,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.646
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P0V75_STBY",
            "LowerThresholdCritical": 0.686,
            "MemberId": "8",
            "Name": "P0V75_STBY",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0.725,
            "SensorNumber": 7,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 0.823
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P2V5_STBY",
            "LowerThresholdCritical": 2.279,
            "MemberId": "9",
            "Name": "P2V5_STBY",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 2.44,
            "SensorNumber": 8,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 2.734
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P2V625_STBY",
            "LowerThresholdCritical": 2.275,
            "MemberId": "10",
            "Name": "P2V625_STBY",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 2.591,
            "SensorNumber": 9,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 2.702
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P12V",
            "LowerThresholdCritical": 11.21,
            "MemberId": "11",
            "Name": "P12V",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 12.154,
            "SensorNumber": 10,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 12.803
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P5V",
            "LowerThresholdCritical": 4.677,
            "MemberId": "12",
            "Name": "P5V",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 5.006,
            "SensorNumber": 11,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 5.335
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P1V05_PCH",
            "LowerThresholdCritical": 0.983,
            "MemberId": "13",
            "Name": "P1V05_PCH",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1.045,
            "SensorNumber": 12,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.115
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P3V3",
            "LowerThresholdCritical": 3.089,
            "MemberId": "14",
            "Name": "P3V3",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 3.292,
            "SensorNumber": 13,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 3.526
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P1V5_PCH",
            "LowerThresholdCritical": 1.412,
            "MemberId": "15",
            "Name": "P1V5_PCH",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1.498,
            "SensorNumber": 14,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.607
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVCCIO_CPU",
            "LowerThresholdCritical": 0.905,
            "MemberId": "16",
            "Name": "PVCCIO_CPU",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0.944,
            "SensorNumber": 15,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 0.991
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVPP_AB",
            "LowerThresholdCritical": 2.375,
            "MemberId": "17",
            "Name": "PVPP_AB",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 2.609,
            "SensorNumber": 16,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 2.796
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVPP_CD",
            "LowerThresholdCritical": 2.375,
            "MemberId": "18",
            "Name": "PVPP_CD",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 2.621,
            "SensorNumber": 17,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 2.796
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVPP_EF",
            "LowerThresholdCritical": 2.375,
            "MemberId": "19",
            "Name": "PVPP_EF",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 2.621,
            "SensorNumber": 18,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 2.796
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVPP_GH",
            "LowerThresholdCritical": 2.375,
            "MemberId": "20",
            "Name": "PVPP_GH",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 2.609,
            "SensorNumber": 19,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 2.796
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVDDQ_AB",
            "LowerThresholdCritical": 1.135,
            "MemberId": "21",
            "Name": "PVDDQ_AB",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1.205,
            "SensorNumber": 20,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.275
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVDDQ_CD",
            "LowerThresholdCritical": 1.135,
            "MemberId": "22",
            "Name": "PVDDQ_CD",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1.205,
            "SensorNumber": 21,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.275
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVDDQ_EF",
            "LowerThresholdCritical": 1.135,
            "MemberId": "23",
            "Name": "PVDDQ_EF",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1.205,
            "SensorNumber": 22,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.275
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVDDQ_GH",
            "LowerThresholdCritical": 1.135,
            "MemberId": "24",
            "Name": "PVDDQ_GH",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1.205,
            "SensorNumber": 23,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.275
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVTT_AB",
            "LowerThresholdCritical": 0.546,
            "MemberId": "25",
            "Name": "PVTT_AB",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0.593,
            "SensorNumber": 24,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 0.655
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVTT_CD",
            "LowerThresholdCritical": 0.546,
            "MemberId": "26",
            "Name": "PVTT_CD",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0.593,
            "SensorNumber": 25,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 0.655
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVTT_EF",
            "LowerThresholdCritical": 0.546,
            "MemberId": "27",
            "Name": "PVTT_EF",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0.593,
            "SensorNumber": 26,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 0.655
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVTT_GH",
            "LowerThresholdCritical": 0.546,
            "MemberId": "28",
            "Name": "PVTT_GH",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0.593,
            "SensorNumber": 27,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 0.655
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVCCIN_P1",
            "LowerThresholdCritical": 1.782,
            "MemberId": "29",
            "Name": "PVCCIN_P1",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 2.348,
            "SensorNumber": 28,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 2.482
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/PVCCIN_P2",
            "LowerThresholdCritical": 1.782,
            "MemberId": "30",
            "Name": "PVCCIN_P2",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 2.359,
            "SensorNumber": 29,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 2.482
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P12V_MR_SAS",
            "LowerThresholdCritical": 11.172,
            "MemberId": "31",
            "Name": "P12V_MR_SAS",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 11.928,
            "SensorNumber": 149,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 12.768
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P1V8_SAS_STBY",
            "LowerThresholdCritical": 1.636,
            "MemberId": "32",
            "Name": "P1V8_SAS_STBY",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1.792,
            "SensorNumber": 150,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.897
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P1V8_SAS",
            "LowerThresholdCritical": 1.636,
            "MemberId": "33",
            "Name": "P1V8_SAS",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1.775,
            "SensorNumber": 151,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.897
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P1V5_SAS",
            "LowerThresholdCritical": 1.418,
            "MemberId": "34",
            "Name": "P1V5_SAS",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 1.488,
            "SensorNumber": 152,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 2.59
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P0V75_SAS",
            "LowerThresholdCritical": 0.688,
            "MemberId": "35",
            "Name": "P0V75_SAS",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0.744,
            "SensorNumber": 155,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 0.792
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P0V9_SAS_STBY",
            "LowerThresholdCritical": 0.819,
            "MemberId": "36",
            "Name": "P0V9_SAS_STBY",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0.944,
            "SensorNumber": 156,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.03
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Power#/Voltages/P0V9_SAS",
            "LowerThresholdCritical": 0.819,
            "MemberId": "37",
            "Name": "P0V9_SAS",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0.967,
            "SensorNumber": 157,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 1.03
        }
    ]
}
```

## /redfish/v1/Chassis/Server1/Thermal

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/Thermal",
    "@odata.id": "/redfish/v1/Chassis/Server1/Thermal",
    "@odata.type": "#Thermal.v1_5_0.Thermal",
    "Description": "Represents the properties for Temperature and Cooling",
    "Id": "Thermal",
    "Name": "Thermal",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Temperatures": [
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/TEMP_SENS_FRONT",
            "MemberId": "1",
            "Name": "TEMP_SENS_FRONT",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 24,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 55,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 70,
            "UpperThresholdNonCritical": 60
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/TEMP_SENS_REAR",
            "MemberId": "2",
            "Name": "TEMP_SENS_REAR",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 28,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 56,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdNonCritical": 80
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/P1_TEMP_SENS",
            "MemberId": "3",
            "Name": "P1_TEMP_SENS",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 28.5,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 57,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 90,
            "UpperThresholdNonCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/P2_TEMP_SENS",
            "MemberId": "4",
            "Name": "P2_TEMP_SENS",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 28,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 58,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 90,
            "UpperThresholdNonCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/DDR4_P1_A1_TMP",
            "MemberId": "5",
            "Name": "DDR4_P1_A1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 25,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 59,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80,
            "UpperThresholdNonCritical": 70
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/DDR4_P1_B1_TMP",
            "MemberId": "6",
            "Name": "DDR4_P1_B1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 25,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 61,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80,
            "UpperThresholdNonCritical": 70
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/DDR4_P1_C1_TMP",
            "MemberId": "7",
            "Name": "DDR4_P1_C1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 26,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 63,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80,
            "UpperThresholdNonCritical": 70
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/DDR4_P1_D1_TMP",
            "MemberId": "8",
            "Name": "DDR4_P1_D1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 26,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 65,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80,
            "UpperThresholdNonCritical": 70
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/DDR4_P2_E1_TMP",
            "MemberId": "9",
            "Name": "DDR4_P2_E1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 24,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 67,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80,
            "UpperThresholdNonCritical": 70
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/DDR4_P2_F1_TMP",
            "MemberId": "10",
            "Name": "DDR4_P2_F1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 25,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 69,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80,
            "UpperThresholdNonCritical": 70
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/DDR4_P2_G1_TMP",
            "MemberId": "11",
            "Name": "DDR4_P2_G1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 25,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 71,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80,
            "UpperThresholdNonCritical": 70
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/DDR4_P2_H1_TMP",
            "MemberId": "12",
            "Name": "DDR4_P2_H1_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 25,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 73,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80,
            "UpperThresholdNonCritical": 70
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/PCH_TEMP_SENS",
            "MemberId": "13",
            "Name": "PCH_TEMP_SENS",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 27,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 108,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85,
            "UpperThresholdNonCritical": 80
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/SB_MEZZ1_TEMP",
            "MemberId": "14",
            "Name": "SB_MEZZ1_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 26,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 109,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 72,
            "UpperThresholdNonCritical": 62
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Server1/Thermal#/Temperatures/SB_MEZZ1ROC_TEMP",
            "MemberId": "15",
            "Name": "SB_MEZZ1ROC_TEMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 41,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/Server1"
                }
            ],
            "SensorNumber": 110,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 100,
            "UpperThresholdNonCritical": 90
        }
    ],
    "Temperatures@odata.count": 15
}
```

