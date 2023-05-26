# Resource: /redfish/v1/Chassis

Vendor | Model
--- | ---
Cisco | UCSC-C220-M5SX

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
    "AssetTag": "029056F",
    "ChassisType": "Rack",
    "DepthMm": 787,
    "Description": "It represents the properties for physical components for any system.  This one object is intended to represent racks, rackmount servers, blades, standalone, modular systems, enclosures, and all other containers.  The non-cpu/device centric parts of the schema are all accessed either directly or indirectly through this resource",
    "HeightMm": 43.2,
    "Id": "1",
    "IndicatorLED": "Off",
    "Links": {
        "ComputerSystems": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU"
            }
        ],
        "CooledBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/Thermal"
            }
        ],
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/7"
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
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID"
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
    "Model": "UCS C220 M5SX",
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
    "SerialNumber": "WZP22490ZCU",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/1/Thermal"
    },
    "UUID": "B16A1200-1CCF-42EA-8B33-6C4D50110704",
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
            "Model": "UCSC-C220-M5SX",
            "PartNumber": "74-105774-02",
            "PhysicalContext": "Chassis",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "WZP22490ZCU",
            "Version": "V02"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Assembly#/Assemblies/1",
            "MemberId": "1",
            "Model": "UCSC-C220-M5SX",
            "PartNumber": "74-105772-01",
            "PhysicalContext": "SystemBoard",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "WZP2249Z09V",
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
    "Members": [],
    "Members@odata.count": 0,
    "Name": "NetworkAdapter Collection"
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
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/2"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID"
        }
    ],
    "Members@odata.count": 4,
    "Name": "PCIeDevice Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/1

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80009E63-1.823.2",
    "Id": "1",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1/PCIeFunctions/1"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/1/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1/PCIeFunctions/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/1/PCIeFunctions/1

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1/PCIeFunctions/1",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1572",
    "Id": "1",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/1.2"
            }
        ],
        "EthernetInterfaces@odata.count": 4,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC",
    "SubsystemId": "0x013b",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/2

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/2",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80009E63-1.823.2",
    "Id": "2",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/2/PCIeFunctions/2"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/2/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/2/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/2/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/2/PCIeFunctions/2"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/2/PCIeFunctions/2

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/2/PCIeFunctions/2",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1572",
    "Id": "2",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/2.1"
            }
        ],
        "EthernetInterfaces@odata.count": 4,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/2"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC",
    "SubsystemId": "0x013b",
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
    "FirmwareVersion": "0x80001514-1.823.2",
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
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/L.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/EthernetInterfaces/L.2"
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
    "SubsystemId": "0x01a3",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
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
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/7"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/8"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/9"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID/Drives/10"
            }
        ],
        "Drives@odata.count": 10,
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP22490ZCU/Storage/MRAID"
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
            "PowerConsumedWatts": 252,
            "PowerLimit": {
                "LimitException": "NoAction"
            },
            "PowerMetrics": {
                "AverageConsumedWatts": 268,
                "MaxConsumedWatts": 366,
                "MinConsumedWatts": 172
            }
        }
    ],
    "PowerSupplies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/PSU1",
            "FirmwareVersion": "12002217",
            "InputRanges": [
                {
                    "InputType": "AC",
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 90,
                    "OutputWattage": 770
                }
            ],
            "LastPowerOutputWatts": 112,
            "LineInputVoltage": 229,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "1",
            "Model": "700-014160-0000",
            "Name": "PSU1",
            "PartNumber": "341-0591-04",
            "PowerInputWatts": 126,
            "PowerOutputWatts": 112,
            "PowerSupplyType": "AC",
            "SerialNumber": "ART2302FHS5",
            "SparePartNumber": "341-0591-04",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/PSU2",
            "FirmwareVersion": "12002217",
            "InputRanges": [
                {
                    "InputType": "AC",
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 90,
                    "OutputWattage": 770
                }
            ],
            "LastPowerOutputWatts": 121,
            "LineInputVoltage": 232,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "2",
            "Model": "700-014160-0000",
            "Name": "PSU2",
            "PartNumber": "341-0591-04",
            "PowerInputWatts": 136,
            "PowerOutputWatts": 121,
            "PowerSupplyType": "AC",
            "SerialNumber": "ART2302FHS2",
            "SparePartNumber": "341-0591-04",
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
            "ReadingVolts": 12.1,
            "SensorNumber": 45,
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
            "ReadingVolts": 12.1,
            "SensorNumber": 51,
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
            "ReadingVolts": 11.774,
            "SensorNumber": 213,
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
            "ReadingVolts": 2.933,
            "SensorNumber": 209,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD1_FAN1_SPEED",
            "MemberId": "1",
            "Name": "MOD1_FAN1_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 4725,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD1_FAN2_SPEED",
            "MemberId": "2",
            "Name": "MOD1_FAN2_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 4841,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD2_FAN1_SPEED",
            "MemberId": "3",
            "Name": "MOD2_FAN1_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 4725,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD2_FAN2_SPEED",
            "MemberId": "4",
            "Name": "MOD2_FAN2_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 4841,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD3_FAN1_SPEED",
            "MemberId": "5",
            "Name": "MOD3_FAN1_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 4830,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD3_FAN2_SPEED",
            "MemberId": "6",
            "Name": "MOD3_FAN2_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 4738,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD4_FAN1_SPEED",
            "MemberId": "7",
            "Name": "MOD4_FAN1_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 4935,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD4_FAN2_SPEED",
            "MemberId": "8",
            "Name": "MOD4_FAN2_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 4738,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD5_FAN1_SPEED",
            "MemberId": "9",
            "Name": "MOD5_FAN1_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 4620,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD5_FAN2_SPEED",
            "MemberId": "10",
            "Name": "MOD5_FAN2_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 4738,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD6_FAN1_SPEED",
            "MemberId": "11",
            "Name": "MOD6_FAN1_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 4830,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD6_FAN2_SPEED",
            "MemberId": "12",
            "Name": "MOD6_FAN2_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 4841,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD7_FAN1_SPEED",
            "MemberId": "13",
            "Name": "MOD7_FAN1_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 4725,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD7_FAN2_SPEED",
            "MemberId": "14",
            "Name": "MOD7_FAN2_SPEED",
            "PhysicalContext": "Fan",
            "Reading": 4738,
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
        }
    ],
    "Fans@odata.count": 14,
    "Id": "Thermal",
    "Name": "Thermal",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Temperatures": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/TEMP_SENS_FRONT",
            "MemberId": "1",
            "Name": "TEMP_SENS_FRONT",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 24,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 68,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 45
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P1_A1_TMP",
            "MemberId": "2",
            "Name": "DDR4_P1_A1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 46,
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
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P1_B1_TMP",
            "MemberId": "3",
            "Name": "DDR4_P1_B1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 44,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 90,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P1_D1_TMP",
            "MemberId": "4",
            "Name": "DDR4_P1_D1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 45,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 102,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P1_E1_TMP",
            "MemberId": "5",
            "Name": "DDR4_P1_E1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 43,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 108,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P2_G1_TMP",
            "MemberId": "6",
            "Name": "DDR4_P2_G1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 42,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P2_H1_TMP",
            "MemberId": "7",
            "Name": "DDR4_P2_H1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 41,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P2_K1_TMP",
            "MemberId": "8",
            "Name": "DDR4_P2_K1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 40,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/DDR4_P2_L1_TMP",
            "MemberId": "9",
            "Name": "DDR4_P2_L1_TMP",
            "PhysicalContext": "Memory",
            "ReadingCelsius": 39,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/P1_TEMP_SENS",
            "MemberId": "10",
            "Name": "P1_TEMP_SENS",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 77.5,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 164,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 98
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/P2_TEMP_SENS",
            "MemberId": "11",
            "Name": "P2_TEMP_SENS",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 67,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 165,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 98
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/PSU1_TEMP",
            "MemberId": "12",
            "Name": "PSU1_TEMP",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 40,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 199,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 65
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/PSU2_TEMP",
            "MemberId": "13",
            "Name": "PSU2_TEMP",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 34,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 200,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 65
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/PCH_TEMP_SENS",
            "MemberId": "14",
            "Name": "PCH_TEMP_SENS",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 58,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 201,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/RISER2_INLET_TMP",
            "MemberId": "15",
            "Name": "RISER2_INLET_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 54,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 241,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 70
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/RISER1_INLET_TMP",
            "MemberId": "16",
            "Name": "RISER1_INLET_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 47,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 242,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 70
        }
    ],
    "Temperatures@odata.count": 16
}
```

