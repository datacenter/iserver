# Resource: /redfish/v1/Chassis

Vendor | Model
--- | ---
Cisco | UCSC-C220-M4S

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
    "DepthMm": 787,
    "Description": "It represents the properties for physical components for any system.  This one object is intended to represent racks, rackmount servers, blades, standalone, modular systems, enclosures, and all other containers.  The non-cpu/device centric parts of the schema are all accessed either directly or indirectly through this resource",
    "HeightMm": 43.2,
    "Id": "1",
    "IndicatorLED": "Off",
    "Links": {
        "ComputerSystems": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J"
            }
        ],
        "CooledBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/Thermal"
            }
        ],
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Drives/SLOT-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0/Drives/SLOT-2"
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
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/FlexFlash-0"
            }
        ]
    },
    "LogServices": {
        "@odata.id": "/redfish/v1/Chassis/1/LogServices"
    },
    "Manufacturer": "Cisco Systems Inc.",
    "Model": "UCS C220 M4S",
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
    "SerialNumber": "FCH2017V24J",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/1/Thermal"
    },
    "UUID": "48753718-3DB4-4502-B2A0-58BC21922BA3",
    "WeightKg": 17.2,
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
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/2"
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

## /redfish/v1/Chassis/1/PCIeDevices/1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity",
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
    "Name": "Cisco(R) Ethernet Converged NIC X710-DA4",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/1/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
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

```null
```

## /redfish/v1/Chassis/1/PCIeDevices/2

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/2",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "0x800008A4-1.819.0",
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
    "Name": "Intel X520-DA2 10 Gbps 2 port NIC",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/2/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/2/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
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
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/2/PCIeFunctions/2",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x10fb",
    "Id": "2",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/2.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/2.2"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/2"
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

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/HBA/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/HBA/PCIeFunctions/HBA"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
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
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA/Drives/PD-2"
            }
        ],
        "Drives@odata.count": 2,
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/HBA"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/Storage/SLOT-HBA"
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
    "FirmwareVersion": "0x80000E74-1.819.0",
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
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/L.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/L.2"
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
    "SubsystemId": "0x00d5",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x8086"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity",
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
    "Name": "UCS VIC 1227 10Gbps 2 port CNA SFP+",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MLOM/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions",
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
    "@odata.context": "/redfish/v1/$metadata#Chassis/Members/$entity/PCIeDevices/Members/$entity/PCIeFunctions/Members/$entity",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM/PCIeFunctions/MLOM",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0042",
    "Id": "MLOM",
    "Links": {
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/MLOM.0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/EthernetInterfaces/MLOM.1"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions": [
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/eth0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/eth1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/vs0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/vs1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/i0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/i1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/fc0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/FCH2017V24J/NetworkInterfaces/MLOM/NetworkDeviceFunctions/fc1"
            }
        ],
        "NetworkDeviceFunctions@odata.count": 8,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM"
        },
        "StorageControllers@odata.count": 0
    },
    "Name": "UCS VIC 1227 10Gbps 2 port CNA SFP+",
    "SubsystemId": "0x012e",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1137"
}
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
            "FirmwareVersion": "10052023",
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
            "LastPowerOutputWatts": 0,
            "LineInputVoltage": 232,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "1",
            "Model": "PS-2771-1S-LF",
            "Name": "PSU1",
            "PartNumber": "341-0591-01",
            "PowerInputWatts": 13,
            "PowerOutputWatts": 0,
            "PowerSupplyType": "AC",
            "SerialNumber": "LIT20100SXH",
            "SparePartNumber": "341-0591-01",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/PSU2",
            "FirmwareVersion": "10052023",
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
            "LastPowerOutputWatts": 0,
            "LineInputVoltage": 237,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "2",
            "Model": "PS-2771-1S-LF",
            "Name": "PSU2",
            "PartNumber": "341-0591-01",
            "PowerInputWatts": 14,
            "PowerOutputWatts": 0,
            "PowerSupplyType": "AC",
            "SerialNumber": "LIT20100SU6",
            "SparePartNumber": "341-0591-01",
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
            "ReadingCelsius": 27,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 64,
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
            "ReadingCelsius": 19,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 67,
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
            "ReadingCelsius": 33,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 177,
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
            "ReadingCelsius": 32,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 178,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 65,
            "UpperThresholdNonCritical": 60
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/RISER1_INLET_TMP",
            "MemberId": "5",
            "Name": "RISER1_INLET_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 29,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 211,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 70,
            "UpperThresholdNonCritical": 60
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/RISER1_OUTLETTMP",
            "MemberId": "6",
            "Name": "RISER1_OUTLETTMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 33,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 212,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 70,
            "UpperThresholdNonCritical": 60
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/RISER2_INLET_TMP",
            "MemberId": "7",
            "Name": "RISER2_INLET_TMP",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 32,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 213,
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
            "ReadingCelsius": 36,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 214,
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

