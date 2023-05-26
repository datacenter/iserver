# Resource: /redfish/v1/Chassis

Vendor | Model
--- | ---
Cisco | UCSC-C220-M6N

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
    "AssetTag": "Unknown",
    "ChassisType": "Rack",
    "DepthMm": 762,
    "Description": "It represents the properties for physical components for any system.  This one object is intended to represent racks, rackmount servers, blades, standalone, modular systems, enclosures, and all other containers.  The non-cpu/device centric parts of the schema are all accessed either directly or indirectly through this resource",
    "HeightMm": 43.18,
    "Id": "1",
    "IndicatorLED": "Off",
    "Links": {
        "ComputerSystems": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0"
            }
        ],
        "CooledBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/Thermal"
            }
        ],
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/7"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/8"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/9"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/10"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Drives/253"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Drives/254"
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
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID"
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
    "Model": "UCS C225 M6S",
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
    "SerialNumber": "WZP262207W0",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/1/Thermal"
    },
    "UUID": "3FC6BE04-7B3E-4240-A269-D87F44A1F7DD",
    "WeightKg": 14.686,
    "WidthMm": 429.26
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
            "Model": "UCSC-C225-M6S",
            "PartNumber": "74-125841-01",
            "PhysicalContext": "Chassis",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "WZP262207W0",
            "Version": "V01"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Assembly#/Assemblies/1",
            "MemberId": "1",
            "Model": "UCSC-C225-M6S",
            "PartNumber": "74-125843-01",
            "PhysicalContext": "SystemBoard",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "WZP2620Z13G",
            "Version": "V01"
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
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-PCIE-C25Q-04_FCH26277TA5"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-M-V100-04_FCH26147UVK"
        }
    ],
    "Members@odata.count": 2,
    "Name": "NetworkAdapter Collection"
}
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-M-V100-04_FCH26147UVK

```null
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-M-V100-04_FCH26147UVK/NetworkDeviceFunctions

```null
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-M-V100-04_FCH26147UVK/NetworkPorts

```null
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-PCIE-C25Q-04_FCH26277TA5

```null
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-PCIE-C25Q-04_FCH26277TA5/NetworkDeviceFunctions

```null
```

## /redfish/v1/Chassis/1/NetworkAdapters/UCSC-PCIE-C25Q-04_FCH26277TA5/NetworkPorts

```null
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
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MSTOR-RAID"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3"
        }
    ],
    "Members@odata.count": 5,
    "Name": "PCIeDevice Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/1

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "5.2(2b)",
    "Id": "1",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1/PCIeFunctions/0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco UCS VIC 1455",
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
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1/PCIeFunctions/0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/1/PCIeFunctions/0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1/PCIeFunctions/0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0042",
    "Id": "1",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/1.0"
            }
        ],
        "EthernetInterfaces@odata.count": 4,
        "NetworkDeviceFunctions": [],
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/1"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "Cisco UCS VIC 1455",
    "SubsystemId": "0x0217",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1137"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/3

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "N/A",
    "Id": "3",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3/PCIeFunctions/0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "NVIDIA T4 PCIe 16GB 70W",
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
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3/PCIeFunctions/0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/3/PCIeFunctions/0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3/PCIeFunctions/0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x1eb8",
    "Id": "3",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions": [],
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "NVIDIA T4 PCIe 16GB 70W",
    "SubsystemId": "0x12a2",
    "SubsystemVendorId": "0x10de",
    "VendorId": "0x10de"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MLOM

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "5.2(2b)",
    "Id": "MLOM",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM/PCIeFunctions/0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco UCS VIC 1477 MLOM",
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
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM/PCIeFunctions/0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MLOM/PCIeFunctions/0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM/PCIeFunctions/0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x0042",
    "Id": "MLOM",
    "Links": {
        "Drives": [],
        "Drives@odata.count": 0,
        "EthernetInterfaces": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/MLOM.0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/EthernetInterfaces/MLOM.1"
            }
        ],
        "EthernetInterfaces@odata.count": 2,
        "NetworkDeviceFunctions": [],
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM"
        },
        "StorageControllers": [],
        "StorageControllers@odata.count": 0
    },
    "Name": "Cisco UCS VIC 1477 MLOM",
    "SubsystemId": "0x02b0",
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
    "FirmwareVersion": "52.20.0-4432",
    "Id": "MRAID",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID/PCIeFunctions/0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco 12G SAS RAID Controller with 4GB FBWC (16 Drives)",
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
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID/PCIeFunctions/0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MRAID/PCIeFunctions/0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID/PCIeFunctions/0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x10e2",
    "Id": "MRAID",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/2"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/3"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/4"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/5"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/6"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/7"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/8"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/9"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID/Drives/10"
            }
        ],
        "Drives@odata.count": 10,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions": [],
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MRAID"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "Cisco 12G SAS RAID Controller with 4GB FBWC (16 Drives)",
    "SubsystemId": "0x02a4",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1000"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MSTOR-RAID

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeDevice.PCIeDevice",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MSTOR-RAID",
    "@odata.type": "#PCIeDevice.v1_4_0.PCIeDevice",
    "Description": "This gives information of PCIeDevices on the system",
    "FirmwareVersion": "N/A",
    "Id": "MSTOR-RAID",
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
        "PCIeFunctions": [
            {
                "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MSTOR-RAID/PCIeFunctions/0"
            }
        ],
        "PCIeFunctions@odata.count": 1
    },
    "Name": "Cisco Boot optimized M.2 Raid controller",
    "PCIeFunctions": {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MSTOR-RAID/PCIeFunctions"
    }
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MSTOR-RAID/PCIeFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunctionCollection.PCIeFunctionCollection",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MSTOR-RAID/PCIeFunctions",
    "@odata.type": "#PCIeFunctionCollection.PCIeFunctionCollection",
    "Description": "Collection of PCIeFunction resource instances for this PCIeDevice",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MSTOR-RAID/PCIeFunctions/0"
        }
    ],
    "Members@odata.count": 1,
    "Name": "PCIeFunction Collection"
}
```

## /redfish/v1/Chassis/1/PCIeDevices/MSTOR-RAID/PCIeFunctions/0

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeFunction.PCIeFunction",
    "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MSTOR-RAID/PCIeFunctions/0",
    "@odata.type": "#PCIeFunction.v1_2_3.PCIeFunction",
    "Description": "This gives information of PCIeFunctions on the system",
    "DeviceId": "0x9230",
    "Id": "MSTOR-RAID",
    "Links": {
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Drives/253"
            },
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID/Drives/254"
            }
        ],
        "Drives@odata.count": 2,
        "EthernetInterfaces": [],
        "EthernetInterfaces@odata.count": 0,
        "NetworkDeviceFunctions": [],
        "NetworkDeviceFunctions@odata.count": 0,
        "PCIeDevice": {
            "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MSTOR-RAID"
        },
        "StorageControllers": [
            {
                "@odata.id": "/redfish/v1/Systems/WZP262207W0/Storage/MSTOR-RAID"
            }
        ],
        "StorageControllers@odata.count": 1
    },
    "Name": "Cisco Boot optimized M.2 Raid controller",
    "SubsystemId": "0x0251",
    "SubsystemVendorId": "0x1137",
    "VendorId": "0x1b4b"
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
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/0",
            "MemberId": "1",
            "PowerConsumedWatts": 0
        }
    ],
    "PowerSupplies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/0",
            "FirmwareVersion": "10062019",
            "InputRanges": [
                {
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 140,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 90,
                    "OutputWattage": 800
                },
                {
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 180,
                    "OutputWattage": 1050
                }
            ],
            "LastPowerOutputWatts": 0,
            "LineInputVoltage": 227,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "1",
            "Model": "PS-2112-9S-LF",
            "Name": "PSU1",
            "PartNumber": "341-0638-03",
            "PowerInputWatts": 16,
            "PowerOutputWatts": 0,
            "PowerSupplyType": "AC",
            "SerialNumber": "LIT2625AHL5",
            "SparePartNumber": "341-0638-03",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/1",
            "FirmwareVersion": "10062019",
            "InputRanges": [
                {
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 140,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 90,
                    "OutputWattage": 800
                },
                {
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47,
                    "MinimumVoltage": 180,
                    "OutputWattage": 1050
                }
            ],
            "LastPowerOutputWatts": 0,
            "LineInputVoltage": 224,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "2",
            "Model": "PS-2112-9S-LF",
            "Name": "PSU2",
            "PartNumber": "341-0638-03",
            "PowerInputWatts": 16,
            "PowerOutputWatts": 0,
            "PowerSupplyType": "AC",
            "SerialNumber": "LIT2625AHEQ",
            "SparePartNumber": "341-0638-03",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ],
    "Voltages": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/Voltages/0",
            "MemberId": "1",
            "Name": "PSU1_VOUT",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0,
            "SensorNumber": 57,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 14
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/Voltages/1",
            "MemberId": "2",
            "Name": "PSU2_VOUT",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 0,
            "SensorNumber": 61,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 14
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/Voltages/2",
            "LowerThresholdCritical": 2.543,
            "MemberId": "3",
            "Name": "P3V_BAT_SCALED",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 3.167,
            "SensorNumber": 202,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/0",
            "MemberId": "1",
            "Name": "PSU1_TEMP",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 26,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 198,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 65
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/1",
            "MemberId": "2",
            "Name": "PSU2_TEMP",
            "PhysicalContext": "PowerSupply",
            "ReadingCelsius": 24,
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
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/2",
            "MemberId": "3",
            "Name": "TEMP_SENS_FRONT",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 22,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1"
                }
            ],
            "SensorNumber": 240,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 45
        }
    ],
    "Temperatures@odata.count": 3
}
```

