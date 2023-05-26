# Resource: /redfish/v1/Chassis

Vendor | Model
--- | ---
Cisco | UCSC-C240-M4SX

## /redfish/v1/Chassis

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis",
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
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/1",
    "@odata.type": "#Chassis.v1_10_0.Chassis",
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/1/Actions/Chassis.Reset"
        }
    },
    "ChassisType": "Rack",
    "DepthMm": 766,
    "Description": "It represents the properties for physical components for any system.  This one object is intended to represent racks, rackmount servers, blades, standalone, modular systems, enclosures, and all other containers.  The non-cpu/device centric parts of the schema are all accessed either directly or indirectly through this resource",
    "HeightMm": 87,
    "Id": "1",
    "IndicatorLED": "Off",
    "Links": {
        "ComputerSystems": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7"
            }
        ],
        "CooledBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/Thermal"
            }
        ],
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-7"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0/Drives/SLOT-2"
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
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/FlexFlash-0"
            }
        ]
    },
    "LogServices": {
        "@odata.id": "/redfish/v1/Chassis/1/LogServices"
    },
    "Manufacturer": "Cisco Systems Inc.",
    "Model": "UCS C240 M4SX",
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
    "SerialNumber": "FCH2017V1J7",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/1/Thermal"
    },
    "UUID": "BB16A414-DF14-47B4-8889-BAD3872F8926",
    "WeightKg": 28.4,
    "WidthMm": 482
}
```

## /redfish/v1/Chassis/1/LogServices

```
```

## /redfish/v1/Chassis/1/NetworkAdapters

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/NetworkAdapters",
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
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices",
    "@odata.type": "#PCIeDeviceCollection.PCIeDeviceCollection",
    "Description": "Collection of PCIeDevice resource instances for this system",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/5"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/HBA"
        }
    ],
    "Members@odata.count": 5,
    "Name": "PCIeDevice Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/3

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80009E63-1.823.2",
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
    "Name": "Cisco(R) Ethernet Converged NIC X710-DA4",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/3/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
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
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3/PCIeFunctions/3",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1572",
    "Id": "3",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/3.2"
            }
        ],
        "EthernetInterfaces@odata.count": 4,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Cisco(R) Ethernet Converged NIC X710-DA4",
    "SubsystemId": "0x013b",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/5

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/5",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x800008A4-1.812.1",
    "Id": "5",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/5/PCIeFunctions/5"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Intel X520-DA2 10 Gbps 2 port NIC",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/5/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/5/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/5/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/5/PCIeFunctions/5"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/5/PCIeFunctions/5

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/5/PCIeFunctions/5",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x10fb",
    "Id": "5",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/5.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/5.2"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/5"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel X520-DA2 10 Gbps 2 port NIC",
    "SubsystemId": "0x000c",
    "SubsystemVendorId": "0x8086",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/HBA

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/HBA",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "24.12.1-0456",
    "Id": "HBA",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/HBA/PCIeFunctions/HBA"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco 12G SAS Modular Raid Controller",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/HBA/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/HBA/PCIeFunctions

```null
```

## /redfish/v1/Chassis/1/PCIeDevices/HBA/PCIeFunctions/HBA

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/HBA/PCIeFunctions/HBA",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x005d",
    "Id": "HBA",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA/Drives/PD-7"
            }
        ],
        "Drives@odata.count": 7,
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/HBA"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/Storage/SLOT-HBA"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "Cisco 12G SAS Modular Raid Controller",
    "SubsystemId": "0x00db",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1000"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/L

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x80000E75-1.819.0",
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
    "Name": "Intel(R) I350 1 Gbps Network Controller",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/L/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
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
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L/PCIeFunctions/L",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1521",
    "Id": "L",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/L.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V1J7/EthernetInterfaces/L.2"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "Intel(R) I350 1 Gbps Network Controller",
    "SubsystemId": "0x00d6",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MLOM

```null
```

## /redfish/v1/Chassis/1/Power

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/Power",
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
            "PowerConsumedWatts": 0,
            "PowerLimit": {
                "LimitException": "NoAction"
            },
            "PowerMetrics": []
        }
    ],
    "PowerSupplies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/PSU1",
            "FirmwareVersion": "14031001",
            "InputRanges": [
                {
                    "InputType": "AC",
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 140,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 90,
                    "OutputWattage": 800
                },
                {
                    "InputType": "AC",
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 180,
                    "OutputWattage": 1200
                }
            ],
            "LastPowerOutputWatts": 0,
            "LineInputVoltage": 232,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "1",
            "Model": "DPST-1200CB B",
            "Name": "PSU1",
            "PartNumber": "341-0624-01",
            "PowerSupplyType": "AC",
            "SerialNumber": "DCH1815S0L1",
            "SparePartNumber": "341-0624-01",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/PSU2",
            "FirmwareVersion": "14031001",
            "InputRanges": [
                {
                    "InputType": "AC",
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 140,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 90,
                    "OutputWattage": 800
                },
                {
                    "InputType": "AC",
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 180,
                    "OutputWattage": 1200
                }
            ],
            "LastPowerOutputWatts": 0,
            "LineInputVoltage": 236,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "2",
            "Model": "DPST-1200CB B",
            "Name": "PSU2",
            "PartNumber": "341-0624-01",
            "PowerSupplyType": "AC",
            "SerialNumber": "DCH1815S0FC",
            "SparePartNumber": "341-0624-01",
            "Status": {
                "State": "Enabled"
            }
        }
    ],
    "Voltages": []
}
```

## /redfish/v1/Chassis/1/Thermal

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/Thermal",
    "@odata.id": "/redfish/v1/Chassis/1/Thermal",
    "@odata.type": "#Thermal.v1_5_0.Thermal",
    "Description": "Represents the properties for Temperature and Cooling",
    "Fans": [],
    "Fans@odata.count": 0,
    "Id": "Thermal",
    "Name": "Thermal",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Temperatures": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/MLOM_TMP",
            "MemberId": "1",
            "Name": "MLOM_TMP",
            "PhysicalContext": "NetworkingDevice",
            "ReadingCelsius": 24,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 52,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 90,
            "UpperThresholdNonCritical": 85
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/FP_TEMP_SENSOR",
            "MemberId": "2",
            "Name": "FP_TEMP_SENSOR",
            "PhysicalContext": "Front",
            "ReadingCelsius": 21,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 70,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 45,
            "UpperThresholdNonCritical": 40
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/PSU1_TEMP",
            "MemberId": "3",
            "Name": "PSU1_TEMP",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 28,
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
            "UpperThresholdCritical": 65,
            "UpperThresholdNonCritical": 60
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/PSU2_TEMP",
            "MemberId": "4",
            "Name": "PSU2_TEMP",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 27,
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
            "UpperThresholdCritical": 65,
            "UpperThresholdNonCritical": 60
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/RISER2_INLET_TMP",
            "MemberId": "5",
            "Name": "RISER2_INLET_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 27,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 232,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 70,
            "UpperThresholdNonCritical": 60
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/RISER1_INLET_TMP",
            "MemberId": "6",
            "Name": "RISER1_INLET_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 26,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 233,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 70,
            "UpperThresholdNonCritical": 60
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/RISER1_OUTLETTMP",
            "MemberId": "7",
            "Name": "RISER1_OUTLETTMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 32,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 234,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 70,
            "UpperThresholdNonCritical": 60
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/RISER2_OUTLETTMP",
            "MemberId": "8",
            "Name": "RISER2_OUTLETTMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 28,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 235,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 70,
            "UpperThresholdNonCritical": 60
        }
    ],
    "Temperatures@odata.count": 8
}
```

