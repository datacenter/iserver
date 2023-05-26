# Resource: /redfish/v1/Chassis

Vendor | Model
--- | ---
Dell | vServer

## /redfish/v1/Chassis

```{
    "@odata.context": "/redfish/v1/$metadata#ChassisCollection.ChassisCollection",
    "@odata.id": "/redfish/v1/Chassis",
    "@odata.type": "#ChassisCollection.ChassisCollection",
    "Description": "Collection of Chassis",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Enclosure.Internal.0-1:RAID.SL.3-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Enclosure.Internal.0-1"
        }
    ],
    "Members@odata.count": 3,
    "Name": "Chassis Collection"
}
```

## /redfish/v1/Chassis/Enclosure.Internal.0-1

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Chassis/Enclosure.Internal.0-1/Settings"
        },
        "SupportedApplyTimes": [
            "Immediate",
            "OnReset",
            "AtMaintenanceWindowStart",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/Enclosure.Internal.0-1",
    "@odata.type": "#Chassis.v1_13_0.Chassis",
    "Actions": {},
    "AssetTag": "",
    "ChassisType": "StorageEnclosure",
    "Description": "PCIe SSD Backplane 1",
    "Id": "Enclosure.Internal.0-1",
    "Links": {
        "ContainedBy": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Contains": [],
        "Contains@odata.count": 0,
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1/Drives/Disk.Bay.8:Enclosure.Internal.0-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1/Drives/Disk.Bay.9:Enclosure.Internal.0-1"
            }
        ],
        "Drives@odata.count": 2,
        "ManagedBy": [
            {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1"
            }
        ],
        "ManagedBy@odata.count": 1,
        "PCIeDevices": [],
        "PCIeDevices@odata.count": 0,
        "Storage": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1"
            }
        ],
        "Storage@odata.count": 1
    },
    "Manufacturer": null,
    "Model": "PCIe SSD Backplane 1",
    "Name": "PCIe SSD Backplane 1",
    "PartNumber": null,
    "PowerState": "On",
    "SKU": "",
    "SerialNumber": null,
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Chassis/Enclosure.Internal.0-1/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/Enclosure.Internal.0-1/Settings",
    "@odata.type": "#Chassis.v1_13_0.Chassis",
    "Actions": {},
    "AssetTag": "",
    "ChassisType": "StorageEnclosure",
    "Description": "PCIe SSD Backplane 1",
    "Id": "Enclosure.Internal.0-1",
    "Links": {
        "ContainedBy": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
        },
        "Contains": [],
        "Contains@odata.count": 0,
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1/Drives/Disk.Bay.8:Enclosure.Internal.0-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1/Drives/Disk.Bay.9:Enclosure.Internal.0-1"
            }
        ],
        "Drives@odata.count": 2,
        "ManagedBy": [
            {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1"
            }
        ],
        "ManagedBy@odata.count": 1,
        "PCIeDevices": [],
        "PCIeDevices@odata.count": 0,
        "Storage": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1"
            }
        ],
        "Storage@odata.count": 1
    },
    "Manufacturer": null,
    "Model": "PCIe SSD Backplane 1",
    "Name": "PCIe SSD Backplane 1",
    "PartNumber": null,
    "PowerState": "On",
    "SKU": "",
    "SerialNumber": null,
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1",
    "@odata.type": "#Chassis.v1_13_0.Chassis",
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/System.Embedded.1/Actions/Chassis.Reset"
        }
    },
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "AssetTag": "testdell",
    "ChassisType": "RackMount",
    "Description": "It represents the properties for physical components for any system.It represent racks, rackmount servers, blades, standalone, modular systems,enclosures, and all other containers.The non-cpu/device centric parts of the schema are all accessed either directly or indirectly through this resource.",
    "EnvironmentalClass": "A2",
    "Id": "System.Embedded.1",
    "IndicatorLED": "Blinking",
    "Links": {
        "ComputerSystems": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
            }
        ],
        "ComputerSystems@odata.count": 1,
        "Contains": [
            {
                "@odata.id": "/redfish/v1/Chassis/Enclosure.Internal.0-1:RAID.SL.3-1"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/Enclosure.Internal.0-1"
            }
        ],
        "Contains@odata.count": 2,
        "CooledBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/0"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/1"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/2"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/3"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/4"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/5"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/6"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/7"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/8"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/9"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/10"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/11"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/12"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/13"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/14"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/15"
            }
        ],
        "CooledBy@odata.count": 16,
        "Drives": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1/Drives/Disk.Direct.0-0:AHCI.SL.6-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1/Drives/Disk.Direct.1-1:AHCI.SL.6-1"
            }
        ],
        "Drives@odata.count": 2,
        "ManagedBy": [
            {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1"
            }
        ],
        "ManagedBy@odata.count": 1,
        "ManagersInChassis": [
            {
                "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1"
            }
        ],
        "ManagersInChassis@odata.count": 1,
        "PCIeDevices": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-23"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-28"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/4-0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-31"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/0-17"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/3-0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/102-0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/101-0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/49-0"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/5-0"
            }
        ],
        "PCIeDevices@odata.count": 11,
        "PoweredBy": [
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerSupplies/0"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerSupplies/1"
            }
        ],
        "PoweredBy@odata.count": 2,
        "Processors": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
            }
        ],
        "Processors@odata.count": 2,
        "Storage": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/RAID.SL.3-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/CPU.1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.2-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.Embedded.1-1"
            },
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Storage/AHCI.SL.6-1"
            }
        ],
        "Storage@odata.count": 5
    },
    "Location": {
        "Info": ";;;;1",
        "InfoFormat": "DataCenter;RoomName;Aisle;RackName;RackSlot",
        "Placement": {
            "Rack": "",
            "Row": ""
        },
        "PostalAddress": {
            "Building": "",
            "Room": ""
        }
    },
    "Manufacturer": "Dell Inc.",
    "Memory": {
        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Memory"
    },
    "Model": "PowerEdge R650",
    "Name": "Computer System Chassis",
    "NetworkAdapters": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters"
    },
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellChassis": {
                "@odata.context": "/redfish/v1/$metadata#DellChassis.DellChassis",
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellChassis/mainsystemchassis",
                "@odata.type": "#DellChassis.v1_0_0.DellChassis",
                "CanBeFRUed": true,
                "Description": "This resource shall provide information about the enclosure or chassis the system is in.",
                "Id": "mainsystemchassis",
                "Links": {
                    "ComputerSystem": {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                    }
                },
                "Name": "DellChassis",
                "SystemID": 2322
            }
        }
    },
    "PCIeSlots": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/PCIeSlots"
    },
    "PartNumber": "0JDN4VA00",
    "PhysicalSecurity": {
        "IntrusionSensor": "Normal",
        "IntrusionSensorNumber": 115,
        "IntrusionSensorReArm": "Manual"
    },
    "Power": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power"
    },
    "PowerState": "On",
    "SKU": "U8OIL5X",
    "Sensors": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors"
    },
    "SerialNumber": "YGFCBTJSO8WOMR",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal"
    },
    "UUID": "4c4c4544-0034-4410-8038-b1c04f464633"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896869",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "0",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B6#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B6_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.B6",
                        "Id": "DIMM.Socket.B6_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "1994CC0E"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896869",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/1",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "1",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B3#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B3_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.B3",
                        "Id": "DIMM.Socket.B3_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "1994CC0F"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896869",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/2",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "2",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A3#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A3_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.A3",
                        "Id": "DIMM.Socket.A3_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A27"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896869",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/3",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "3",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B1#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B1_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.B1",
                        "Id": "DIMM.Socket.B1_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A25"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896869",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/4",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "4",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A7#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A7_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.A7",
                        "Id": "DIMM.Socket.A7_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A67"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896869",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/5",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "5",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B5#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B5_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.B5",
                        "Id": "DIMM.Socket.B5_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A52"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896869",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/6",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "6",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A4#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A4_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.A4",
                        "Id": "DIMM.Socket.A4_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A29"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896870",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/7",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "7",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A1#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A1_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.A1",
                        "Id": "DIMM.Socket.A1_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A6B"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896870",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/8",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "8",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A8#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A8_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.A8",
                        "Id": "DIMM.Socket.A8_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A1F"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896870",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/9",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "9",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A5#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A5_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.A5",
                        "Id": "DIMM.Socket.A5_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A26"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896870",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/10",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "10",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A2#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A2_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.A2",
                        "Id": "DIMM.Socket.A2_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A55"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896870",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/11",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "11",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.A6#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A6_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.A6",
                        "Id": "DIMM.Socket.A6_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A56"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896870",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/12",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "12",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B8#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B8_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.B8",
                        "Id": "DIMM.Socket.B8_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A8A"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896870",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/13",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "13",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B7#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B7_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.B7",
                        "Id": "DIMM.Socket.B7_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "1994BEBD"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896870",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/14",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "14",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B4#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B4_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.B4",
                        "Id": "DIMM.Socket.B4_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A66"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896870",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/15",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DDR4 DIMM",
            "EngineeringChangeLevel": null,
            "MemberId": "15",
            "Model": "DDR4 DIMM",
            "Name": "DIMM.Socket.B2#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B2_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "DIMM.Socket.B2",
                        "Id": "DIMM.Socket.B2_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Memory",
                        "SerialNumber": "19949A23"
                    }
                }
            },
            "PartNumber": "M393A1K43DB2-CWE",
            "Producer": "Samsung",
            "ProductionDate": "2021-04-26T07:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1659740309",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/16",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "SystemPlanar",
            "EngineeringChangeLevel": "A00",
            "MemberId": "16",
            "Model": "SystemPlanar",
            "Name": "System.Embedded.1#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/System.Embedded.1_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "System.Embedded.1",
                        "Id": "System.Embedded.1_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Module/Card",
                        "SerialNumber": "YGFCBTJSO8WOMR"
                    }
                }
            },
            "PartNumber": "0JDN4V",
            "Producer": "Dell Inc.",
            "ProductionDate": "2021-04-01T11:55:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1659740309",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/17",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "MLNX 25GbE 2P ConnectX5 OCP3 NIC",
            "EngineeringChangeLevel": "A03",
            "MemberId": "17",
            "Model": "MLNX 25GbE 2P ConnectX5 OCP3 NIC",
            "Name": "NIC.Integrated.1#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/NIC.Integrated.1_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "NIC.Integrated.1",
                        "Id": "NIC.Integrated.1_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Module/Card",
                        "SerialNumber": "INJBNM414TJ0AL"
                    }
                }
            },
            "PartNumber": "04TRD3",
            "Producer": "Dell",
            "ProductionDate": "2021-04-30T10:54:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1659740309",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/18",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "Dell Storage Cntlr. H745 Front",
            "EngineeringChangeLevel": "A00",
            "MemberId": "18",
            "Model": "Dell Storage Cntlr. H745 Front",
            "Name": "RAID.SL.3-1#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/RAID.SL.3-1_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "RAID.SL.3-1",
                        "Id": "RAID.SL.3-1_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Module/Card",
                        "SerialNumber": "CNIVC0013I0887"
                    }
                }
            },
            "PartNumber": "0JT47Y",
            "Producer": "Dell",
            "ProductionDate": "2021-03-25T08:27:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1659740309",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/19",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "BOSS-S2",
            "EngineeringChangeLevel": "A00",
            "MemberId": "19",
            "Model": "BOSS-S2",
            "Name": "AHCI.SL.6-1#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/AHCI.SL.6-1_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "AHCI.SL.6-1",
                        "Id": "AHCI.SL.6-1_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Module/Card",
                        "SerialNumber": "CNIVC0015I0958"
                    }
                }
            },
            "PartNumber": "0FGNRW",
            "Producer": "Dell",
            "ProductionDate": "2021-05-22T10:53:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1659740309",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/20",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "ELX FC32 LPe32002-M2 Adapter",
            "EngineeringChangeLevel": "A00",
            "MemberId": "20",
            "Model": "ELX FC32 LPe32002-M2 Adapter",
            "Name": "FC.Slot.1#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/FC.Slot.1_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "FC.Slot.1",
                        "Id": "FC.Slot.1_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Module/Card",
                        "SerialNumber": "MYFLPB38BTM033"
                    }
                }
            },
            "PartNumber": "0MHFHK",
            "Producer": "Dell",
            "ProductionDate": "2018-11-28T20:09:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896873",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/21",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "DRIVE BACKPLANE",
            "EngineeringChangeLevel": "A02",
            "MemberId": "21",
            "Model": "DRIVE BACKPLANE",
            "Name": "Enclosure.Internal.0-1#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/Enclosure.Internal.0-1_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "Enclosure.Internal.0-1",
                        "Id": "Enclosure.Internal.0-1_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "CrossConnect/Backplane",
                        "SerialNumber": "CNIVC0013U0560"
                    }
                }
            },
            "PartNumber": "07JJY5",
            "Producer": "Dell",
            "ProductionDate": "2021-04-08T08:59:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896952",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/22",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "Dell Ent NVMe v2 AGN MU U.2 1.6TB",
            "EngineeringChangeLevel": "A00",
            "MemberId": "22",
            "Model": "Dell Ent NVMe v2 AGN MU U.2 1.6TB",
            "Name": "Disk.Bay.8:Enclosure.Internal.0-1#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/Disk.Bay.8:Enclosure.Internal.0-1_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "Disk.Bay.8:Enclosure.Internal.0-1",
                        "Id": "Disk.Bay.8:Enclosure.Internal.0-1_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "StorageMediaPackage(E.GDiskOrTapeDrive)",
                        "SerialNumber": "KRSSK0015M010C"
                    }
                }
            },
            "PartNumber": "00MNMV",
            "Producer": "Dell",
            "ProductionDate": "2021-05-22T00:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
            "@odata.etag": "1661896952",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly#/Assemblies/23",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "Dell Ent NVMe v2 AGN MU U.2 1.6TB",
            "EngineeringChangeLevel": "A00",
            "MemberId": "23",
            "Model": "Dell Ent NVMe v2 AGN MU U.2 1.6TB",
            "Name": "Disk.Bay.9:Enclosure.Internal.0-1#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/Disk.Bay.9:Enclosure.Internal.0-1_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "Description": "This resource shall be used to represent an assembly information.",
                        "DeviceFQDD": "Disk.Bay.9:Enclosure.Internal.0-1",
                        "Id": "Disk.Bay.9:Enclosure.Internal.0-1_0x23_FRU",
                        "Name": "DellAssembly",
                        "PackageType": "StorageMediaPackage(E.GDiskOrTapeDrive)",
                        "SerialNumber": "KRSSK0015M00ZR"
                    }
                }
            },
            "PartNumber": "00MNMV",
            "Producer": "Dell",
            "ProductionDate": "2021-05-22T00:00:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 24,
    "Id": "PCIE Assembly",
    "Name": "Assembly"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkAdapterCollection.NetworkAdapterCollection",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters",
    "@odata.type": "#NetworkAdapterCollection.NetworkAdapterCollection",
    "Description": "Collection Of Network Adapter",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1"
        }
    ],
    "Members@odata.count": 3,
    "Name": "Network Adapter Collection"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkAdapter.NetworkAdapter",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1",
    "@odata.type": "#NetworkAdapter.v1_4_0.NetworkAdapter",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/Assembly"
    },
    "Controllers": [
        {
            "ControllerCapabilities": {
                "DataCenterBridging": {
                    "Capable": false
                },
                "NPAR": {
                    "NparCapable": false,
                    "NparEnabled": false
                },
                "NPIV": {
                    "MaxDeviceLogins": 12288,
                    "MaxPortLogins": 6144
                },
                "NetworkDeviceFunctionCount": 2,
                "NetworkPortCount": 2,
                "VirtualizationOffload": {
                    "SRIOV": {
                        "SRIOVVEPACapable": false
                    },
                    "VirtualFunction": {
                        "DeviceMaxCount": null,
                        "MinAssignmentGroupSize": null,
                        "NetworkPortMaxCount": null
                    }
                }
            },
            "FirmwarePackageVersion": "03.00.14",
            "Links": {
                "NetworkDeviceFunctions": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1"
                    }
                ],
                "NetworkDeviceFunctions@odata.count": 2,
                "NetworkPorts": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-2"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-1"
                    }
                ],
                "NetworkPorts@odata.count": 2,
                "Oem": {
                    "Dell": {
                        "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                        "CPUAffinity": [
                            {
                                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                            }
                        ],
                        "CPUAffinity@odata.count": 1
                    }
                }
            }
        }
    ],
    "Controllers@odata.count": 1,
    "Description": "Network Adapter View",
    "Id": "FC.Slot.1",
    "Manufacturer": "Emulex Corporation",
    "Model": "ELX FC32 LPe32002-M2 Adapter",
    "Name": "Network Adapter View",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts"
    },
    "PartNumber": "0MHFHK",
    "SerialNumber": "MYFLPB38BTM033",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "ELX FC32 LPe32002-M2 Adapter",
            "EngineeringChangeLevel": "A00",
            "MemberId": "0",
            "Model": "ELX FC32 LPe32002-M2 Adapter",
            "Name": "FC.Slot.1#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/FC.Slot.1_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "FC.Slot.1",
                        "Id": "FC.Slot.1#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Module/Card",
                        "SerialNumber": "MYFLPB38BTM033"
                    }
                }
            },
            "PartNumber": "0MHFHK",
            "Producer": "Dell",
            "ProductionDate": "2018-11-28T20:09:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "FC.Slot.1#FRU"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunctionCollection.NetworkDeviceFunctionCollection",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions",
    "@odata.type": "#NetworkDeviceFunctionCollection.NetworkDeviceFunctionCollection",
    "Description": "Collection Of Network Device Function entities",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Network Device Function Collection"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Settings"
        },
        "SupportedApplyTimes": [
            "OnReset",
            "AtMaintenanceWindowStart",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1",
    "@odata.type": "#NetworkDeviceFunction.v1_5_1.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-1"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 1,
    "Description": "NetworkDeviceFunction",
    "Ethernet": {},
    "FibreChannel": {
        "BootTargets": [
            {
                "LUNID": "0",
                "WWPN": "00:00:00:00:00:00:00:00"
            }
        ],
        "BootTargets@odata.count": 1,
        "FCoEActiveVLANId": null,
        "FCoELocalVLANId": null,
        "PermanentWWNN": "20:00:00:10:9B:5A:4A:58",
        "PermanentWWPN": "10:00:00:10:9B:5A:4A:58",
        "WWNN": "20:00:00:10:9B:5A:4A:58",
        "WWNSource": "ProvidedByFabric",
        "WWPN": "10:00:00:10:9B:5A:4A:58"
    },
    "Id": "FC.Slot.1-1",
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1,
                "DellNetworkAttributes": {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellNetworkAttributes/FC.Slot.1-1"
                }
            }
        },
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-1"
        }
    },
    "MaxVirtualFunctions": null,
    "Name": "NetworkDeviceFunction",
    "NetDevFuncCapabilities": [
        "Disabled",
        "FibreChannel"
    ],
    "NetDevFuncCapabilities@odata.count": 2,
    "NetDevFuncType": "FibreChannel",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellFC": {
                "@odata.context": "/redfish/v1/$metadata#DellFC.DellFC",
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellFC/FC.Slot.1-1",
                "@odata.type": "#DellFC.v1_3_0.DellFC",
                "Bus": 23,
                "CableLengthMetres": null,
                "ChipType": null,
                "Device": 0,
                "DeviceDescription": "Fibre Channel in Slot 1 Port 1",
                "DeviceName": "Port 0: Emulex LightPulse LPe32002-M2-D 2-Port 32Gb Fibre  - FC ",
                "EFIVersion": "12.0.257.5",
                "FCTapeEnable": "Disabled",
                "FabricLoginRetryCount": 0,
                "FabricLoginTimeout": 0,
                "FamilyVersion": "03.00.14",
                "FramePayloadSize": null,
                "Function": 0,
                "HardZoneAddress": 0,
                "HardZoneEnable": "Disabled",
                "Id": "FC.Slot.1-1",
                "IdentifierType": null,
                "LinkDownTimeout": 0,
                "LoopResetDelay": 0,
                "Name": "DellFC",
                "PartNumber": "0MHFHK",
                "PortDownRetryCount": 0,
                "PortDownTimeout": 0,
                "PortLoginRetryCount": 0,
                "PortLoginTimeout": 1,
                "Revision": null,
                "SecondFCTargetLUN": 0,
                "SecondFCTargetWWPN": "00:00:00:00:00:00:00:00",
                "SerialNumber": "MYFLPB38BTM033",
                "TransceiverPartNumber": null,
                "TransceiverSerialNumber": null,
                "TransceiverVendorName": null
            },
            "DellFCCapabilities": {
                "@odata.context": "/redfish/v1/$metadata#DellFCCapabilities.DellFCCapabilities",
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellFCCapabilities/FC.Slot.1-1",
                "@odata.type": "#DellFCCapabilities.v1_0_0.DellFCCapabilities",
                "FCMaxNumberExchanges": 6144,
                "FCMaxNumberOutStandingCommands": 12289,
                "FeatureLicensingSupport": "NotSupported",
                "FlexAddressingSupport": "Supported",
                "Id": "FC.Slot.1-1",
                "Name": "DellFCCapabilities",
                "OnChipThermalSensor": "Supported",
                "PersistencePolicySupport": "Supported",
                "uEFISupport": "Supported"
            },
            "DellFCPortMetrics": {
                "@odata.context": "/redfish/v1/$metadata#DellFCPortMetrics.DellFCPortMetrics",
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellFCPortMetrics/FC.Slot.1-1",
                "@odata.type": "#DellFCPortMetrics.v1_1_1.DellFCPortMetrics",
                "FCInvalidCRCs": 0,
                "FCLinkFailures": 0,
                "FCLossOfSignals": 0,
                "FCRxKBCount": 0,
                "FCRxSequences": null,
                "FCRxTotalFrames": 0,
                "FCTxKBCount": 0,
                "FCTxSequences": null,
                "FCTxTotalFrames": 0,
                "Id": "FC.Slot.1-1",
                "Name": "DellFCPortMetrics",
                "OSDriverState": "Operational",
                "PortStatus": "Down"
            },
            "DellInfiniBand": null,
            "DellInfiniBandCapabilities": null,
            "DellInfiniBandPortMetrics": null,
            "DellNIC": null,
            "DellNICCapabilities": null,
            "DellNICPortMetrics": null
        }
    },
    "PhysicalPortAssignment": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-1"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "iSCSIBoot": {}
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellFC/FC.Slot.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellFC.DellFC",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellFC/FC.Slot.1-1",
    "@odata.type": "#DellFC.v1_3_0.DellFC",
    "Bus": 23,
    "CableLengthMetres": null,
    "ChipType": null,
    "Description": "An instance of DellFC will have Fiber Channel device specific data.",
    "Device": 0,
    "DeviceDescription": "Fibre Channel in Slot 1 Port 1",
    "DeviceName": "Port 0: Emulex LightPulse LPe32002-M2-D 2-Port 32Gb Fibre  - FC ",
    "EFIVersion": "12.0.257.5",
    "FCTapeEnable": "Disabled",
    "FabricLoginRetryCount": 0,
    "FabricLoginTimeout": 0,
    "FamilyVersion": "03.00.14",
    "FramePayloadSize": null,
    "Function": 0,
    "HardZoneAddress": 0,
    "HardZoneEnable": "Disabled",
    "Id": "FC.Slot.1-1",
    "IdentifierType": null,
    "LinkDownTimeout": 0,
    "LoopResetDelay": 0,
    "Name": "DellFC",
    "PartNumber": "0MHFHK",
    "PortDownRetryCount": 0,
    "PortDownTimeout": 0,
    "PortLoginRetryCount": 0,
    "PortLoginTimeout": 1,
    "Revision": null,
    "SecondFCTargetLUN": 0,
    "SecondFCTargetWWPN": "00:00:00:00:00:00:00:00",
    "SerialNumber": "MYFLPB38BTM033",
    "TransceiverPartNumber": null,
    "TransceiverSerialNumber": null,
    "TransceiverVendorName": null
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellFCCapabilities/FC.Slot.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellFCCapabilities.DellFCCapabilities",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellFCCapabilities/FC.Slot.1-1",
    "@odata.type": "#DellFCCapabilities.v1_0_0.DellFCCapabilities",
    "Description": "This resource shall represents Fibre Channel HBA capabilities in the managed system.",
    "FCMaxNumberExchanges": 6144,
    "FCMaxNumberOutStandingCommands": 12289,
    "FeatureLicensingSupport": "NotSupported",
    "FlexAddressingSupport": "Supported",
    "Id": "FC.Slot.1-1",
    "Name": "DellFCCapabilities",
    "OnChipThermalSensor": "Supported",
    "PersistencePolicySupport": "Supported",
    "uEFISupport": "Supported"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellFCPortMetrics/FC.Slot.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#DellFCPortMetrics.DellFCPortMetrics",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellFCPortMetrics/FC.Slot.1-1",
    "@odata.type": "#DellFCPortMetrics.v1_1_1.DellFCPortMetrics",
    "Description": "This resource shall represents the statistics of the Fibre Channel HBA port.",
    "FCInvalidCRCs": 0,
    "FCLinkFailures": 0,
    "FCLossOfSignals": 0,
    "FCRxKBCount": 0,
    "FCRxSequences": null,
    "FCRxTotalFrames": 0,
    "FCTxKBCount": 0,
    "FCTxSequences": null,
    "FCTxTotalFrames": 0,
    "Id": "FC.Slot.1-1",
    "Name": "DellFCPortMetrics",
    "OSDriverState": "Operational",
    "PortStatus": "Down"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellNetworkAttributes/FC.Slot.1-1

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellNetworkAttributes/FC.Slot.1-1/Settings"
        },
        "SupportedApplyTimes": [
            "Immediate",
            "AtMaintenanceWindowStart",
            "OnReset",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellNetworkAttributes/FC.Slot.1-1",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "AttributeRegistry": "NetworkAttributeRegistry",
    "Attributes": {
        "BootScanSelection": "Disabled",
        "BusDeviceFunction": "17:00:00",
        "DeviceName": "LPe32002-M2-D",
        "EFIVersion": "12.0.257.5",
        "ELX_BootTargetScanMethod": "NVRAM_BOOTSCAN",
        "ELX_EighthFCBootDeviceOrder": 0,
        "ELX_EighthFCTargetLUN": 0,
        "ELX_EighthFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "ELX_FABLSupport": "Disabled",
        "ELX_FaPWWNSupport": "Disabled",
        "ELX_FifthFCBootDeviceOrder": 0,
        "ELX_FifthFCTargetLUN": 0,
        "ELX_FifthFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "ELX_FirstFCBootDeviceOrder": 0,
        "ELX_FourthFCBootDeviceOrder": 0,
        "ELX_FourthFCTargetLUN": 0,
        "ELX_FourthFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "ELX_LegacyAutoBoot": "Disabled",
        "ELX_LegacyAutoScan": "DISABLE_AUTOSCAN",
        "ELX_LegacyEDD": "EDD30_ENABLED",
        "ELX_LegacyEnvVar": "Disabled",
        "ELX_LegacySpin": "Disabled",
        "ELX_LegacyStartUnit": "Disabled",
        "ELX_MaxLUNSPerTarget": 256,
        "ELX_SecondFCBootDeviceOrder": 0,
        "ELX_SeventhFCBootDeviceOrder": 0,
        "ELX_SeventhFCTargetLUN": 0,
        "ELX_SeventhFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "ELX_SixthFCBootDeviceOrder": 0,
        "ELX_SixthFCTargetLUN": 0,
        "ELX_SixthFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "ELX_ThirdFCBootDeviceOrder": 0,
        "ELX_ThirdFCTargetLUN": 0,
        "ELX_ThirdFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "FamilyVersion": "03.00.14",
        "FirstFCTargetLUN": 0,
        "FirstFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "PCIDeviceID": "E300",
        "PortLoginTimeout": 1,
        "PortNumber": 0,
        "PortSpeed": "Auto",
        "SecondFCTargetLUN": 0,
        "SecondFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "VirtualWWN": "20:00:00:10:9B:5A:4A:58",
        "VirtualWWPN": "10:00:00:10:9B:5A:4A:58",
        "WWN": "20:00:00:10:9B:5A:4A:58",
        "WWPN": "10:00:00:10:9B:5A:4A:58"
    },
    "Description": "DellNetworkAttributes represents the Network device attribute details.",
    "Id": "FC.Slot.1-1",
    "Name": "DellNetworkAttributes"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellNetworkAttributes/FC.Slot.1-1/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellNetworkAttributes/FC.Slot.1-1/Settings",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1/Oem/Dell/DellNetworkAttributes/FC.Slot.1-1/Settings/Actions/DellManager.ClearPending"
        }
    },
    "AttributeRegistry": "NetworkAttributeRegistry",
    "Attributes": {},
    "Description": "This schema provides settings of the oem attributes",
    "Id": "FC.Slot.1-1",
    "Name": "DellNetworkAttributes"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Settings"
        },
        "SupportedApplyTimes": [
            "OnReset",
            "AtMaintenanceWindowStart",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2",
    "@odata.type": "#NetworkDeviceFunction.v1_5_1.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-2"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 1,
    "Description": "NetworkDeviceFunction",
    "Ethernet": {},
    "FibreChannel": {
        "BootTargets": [
            {
                "LUNID": "0",
                "WWPN": "00:00:00:00:00:00:00:00"
            }
        ],
        "BootTargets@odata.count": 1,
        "FCoEActiveVLANId": null,
        "FCoELocalVLANId": null,
        "PermanentWWNN": "20:00:00:10:9B:5A:4A:59",
        "PermanentWWPN": "10:00:00:10:9B:5A:4A:59",
        "WWNN": "20:00:00:10:9B:5A:4A:59",
        "WWNSource": "ProvidedByFabric",
        "WWPN": "10:00:00:10:9B:5A:4A:59"
    },
    "Id": "FC.Slot.1-2",
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1,
                "DellNetworkAttributes": {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellNetworkAttributes/FC.Slot.1-2"
                }
            }
        },
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-2"
        }
    },
    "MaxVirtualFunctions": null,
    "Name": "NetworkDeviceFunction",
    "NetDevFuncCapabilities": [
        "Disabled",
        "FibreChannel"
    ],
    "NetDevFuncCapabilities@odata.count": 2,
    "NetDevFuncType": "FibreChannel",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellFC": {
                "@odata.context": "/redfish/v1/$metadata#DellFC.DellFC",
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellFC/FC.Slot.1-2",
                "@odata.type": "#DellFC.v1_3_0.DellFC",
                "Bus": 23,
                "CableLengthMetres": null,
                "ChipType": null,
                "Device": 0,
                "DeviceDescription": "Fibre Channel in Slot 1 Port 2",
                "DeviceName": "Port 1: Emulex LightPulse LPe32002-M2-D 2-Port 32Gb Fibre  - FC ",
                "EFIVersion": "12.0.257.5",
                "FCTapeEnable": "Disabled",
                "FabricLoginRetryCount": 0,
                "FabricLoginTimeout": 0,
                "FamilyVersion": "03.00.14",
                "FramePayloadSize": null,
                "Function": 1,
                "HardZoneAddress": 0,
                "HardZoneEnable": "Disabled",
                "Id": "FC.Slot.1-2",
                "IdentifierType": null,
                "LinkDownTimeout": 0,
                "LoopResetDelay": 0,
                "Name": "DellFC",
                "PartNumber": "0MHFHK",
                "PortDownRetryCount": 0,
                "PortDownTimeout": 0,
                "PortLoginRetryCount": 0,
                "PortLoginTimeout": 1,
                "Revision": null,
                "SecondFCTargetLUN": 0,
                "SecondFCTargetWWPN": "00:00:00:00:00:00:00:00",
                "SerialNumber": "MYFLPB38BTM033",
                "TransceiverPartNumber": null,
                "TransceiverSerialNumber": null,
                "TransceiverVendorName": null
            },
            "DellFCCapabilities": {
                "@odata.context": "/redfish/v1/$metadata#DellFCCapabilities.DellFCCapabilities",
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellFCCapabilities/FC.Slot.1-2",
                "@odata.type": "#DellFCCapabilities.v1_0_0.DellFCCapabilities",
                "FCMaxNumberExchanges": 6144,
                "FCMaxNumberOutStandingCommands": 12289,
                "FeatureLicensingSupport": "NotSupported",
                "FlexAddressingSupport": "Supported",
                "Id": "FC.Slot.1-2",
                "Name": "DellFCCapabilities",
                "OnChipThermalSensor": "Supported",
                "PersistencePolicySupport": "Supported",
                "uEFISupport": "Supported"
            },
            "DellFCPortMetrics": {
                "@odata.context": "/redfish/v1/$metadata#DellFCPortMetrics.DellFCPortMetrics",
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellFCPortMetrics/FC.Slot.1-2",
                "@odata.type": "#DellFCPortMetrics.v1_1_1.DellFCPortMetrics",
                "FCInvalidCRCs": 0,
                "FCLinkFailures": 0,
                "FCLossOfSignals": 0,
                "FCRxKBCount": 0,
                "FCRxSequences": null,
                "FCRxTotalFrames": 0,
                "FCTxKBCount": 0,
                "FCTxSequences": null,
                "FCTxTotalFrames": 0,
                "Id": "FC.Slot.1-2",
                "Name": "DellFCPortMetrics",
                "OSDriverState": "Operational",
                "PortStatus": "Down"
            },
            "DellInfiniBand": null,
            "DellInfiniBandCapabilities": null,
            "DellInfiniBandPortMetrics": null,
            "DellNIC": null,
            "DellNICCapabilities": null,
            "DellNICPortMetrics": null
        }
    },
    "PhysicalPortAssignment": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-2"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "iSCSIBoot": {}
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellFC/FC.Slot.1-2

```{
    "@odata.context": "/redfish/v1/$metadata#DellFC.DellFC",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellFC/FC.Slot.1-2",
    "@odata.type": "#DellFC.v1_3_0.DellFC",
    "Bus": 23,
    "CableLengthMetres": null,
    "ChipType": null,
    "Description": "An instance of DellFC will have Fiber Channel device specific data.",
    "Device": 0,
    "DeviceDescription": "Fibre Channel in Slot 1 Port 2",
    "DeviceName": "Port 1: Emulex LightPulse LPe32002-M2-D 2-Port 32Gb Fibre  - FC ",
    "EFIVersion": "12.0.257.5",
    "FCTapeEnable": "Disabled",
    "FabricLoginRetryCount": 0,
    "FabricLoginTimeout": 0,
    "FamilyVersion": "03.00.14",
    "FramePayloadSize": null,
    "Function": 1,
    "HardZoneAddress": 0,
    "HardZoneEnable": "Disabled",
    "Id": "FC.Slot.1-2",
    "IdentifierType": null,
    "LinkDownTimeout": 0,
    "LoopResetDelay": 0,
    "Name": "DellFC",
    "PartNumber": "0MHFHK",
    "PortDownRetryCount": 0,
    "PortDownTimeout": 0,
    "PortLoginRetryCount": 0,
    "PortLoginTimeout": 1,
    "Revision": null,
    "SecondFCTargetLUN": 0,
    "SecondFCTargetWWPN": "00:00:00:00:00:00:00:00",
    "SerialNumber": "MYFLPB38BTM033",
    "TransceiverPartNumber": null,
    "TransceiverSerialNumber": null,
    "TransceiverVendorName": null
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellFCCapabilities/FC.Slot.1-2

```{
    "@odata.context": "/redfish/v1/$metadata#DellFCCapabilities.DellFCCapabilities",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellFCCapabilities/FC.Slot.1-2",
    "@odata.type": "#DellFCCapabilities.v1_0_0.DellFCCapabilities",
    "Description": "This resource shall represents Fibre Channel HBA capabilities in the managed system.",
    "FCMaxNumberExchanges": 6144,
    "FCMaxNumberOutStandingCommands": 12289,
    "FeatureLicensingSupport": "NotSupported",
    "FlexAddressingSupport": "Supported",
    "Id": "FC.Slot.1-2",
    "Name": "DellFCCapabilities",
    "OnChipThermalSensor": "Supported",
    "PersistencePolicySupport": "Supported",
    "uEFISupport": "Supported"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellFCPortMetrics/FC.Slot.1-2

```{
    "@odata.context": "/redfish/v1/$metadata#DellFCPortMetrics.DellFCPortMetrics",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellFCPortMetrics/FC.Slot.1-2",
    "@odata.type": "#DellFCPortMetrics.v1_1_1.DellFCPortMetrics",
    "Description": "This resource shall represents the statistics of the Fibre Channel HBA port.",
    "FCInvalidCRCs": 0,
    "FCLinkFailures": 0,
    "FCLossOfSignals": 0,
    "FCRxKBCount": 0,
    "FCRxSequences": null,
    "FCRxTotalFrames": 0,
    "FCTxKBCount": 0,
    "FCTxSequences": null,
    "FCTxTotalFrames": 0,
    "Id": "FC.Slot.1-2",
    "Name": "DellFCPortMetrics",
    "OSDriverState": "Operational",
    "PortStatus": "Down"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellNetworkAttributes/FC.Slot.1-2

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellNetworkAttributes/FC.Slot.1-2/Settings"
        },
        "SupportedApplyTimes": [
            "Immediate",
            "AtMaintenanceWindowStart",
            "OnReset",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellNetworkAttributes/FC.Slot.1-2",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "AttributeRegistry": "NetworkAttributeRegistry",
    "Attributes": {
        "BootScanSelection": "Disabled",
        "BusDeviceFunction": "17:00:01",
        "DeviceName": "LPe32002-M2-D",
        "EFIVersion": "12.0.257.5",
        "ELX_BootTargetScanMethod": "NVRAM_BOOTSCAN",
        "ELX_EighthFCBootDeviceOrder": 0,
        "ELX_EighthFCTargetLUN": 0,
        "ELX_EighthFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "ELX_FABLSupport": "Disabled",
        "ELX_FaPWWNSupport": "Disabled",
        "ELX_FifthFCBootDeviceOrder": 0,
        "ELX_FifthFCTargetLUN": 0,
        "ELX_FifthFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "ELX_FirstFCBootDeviceOrder": 0,
        "ELX_FourthFCBootDeviceOrder": 0,
        "ELX_FourthFCTargetLUN": 0,
        "ELX_FourthFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "ELX_LegacyAutoBoot": "Disabled",
        "ELX_LegacyAutoScan": "DISABLE_AUTOSCAN",
        "ELX_LegacyEDD": "EDD30_ENABLED",
        "ELX_LegacyEnvVar": "Disabled",
        "ELX_LegacySpin": "Disabled",
        "ELX_LegacyStartUnit": "Disabled",
        "ELX_MaxLUNSPerTarget": 256,
        "ELX_SecondFCBootDeviceOrder": 0,
        "ELX_SeventhFCBootDeviceOrder": 0,
        "ELX_SeventhFCTargetLUN": 0,
        "ELX_SeventhFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "ELX_SixthFCBootDeviceOrder": 0,
        "ELX_SixthFCTargetLUN": 0,
        "ELX_SixthFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "ELX_ThirdFCBootDeviceOrder": 0,
        "ELX_ThirdFCTargetLUN": 0,
        "ELX_ThirdFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "FamilyVersion": "03.00.14",
        "FirstFCTargetLUN": 0,
        "FirstFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "PCIDeviceID": "E300",
        "PortLoginTimeout": 1,
        "PortNumber": 1,
        "PortSpeed": "Auto",
        "SecondFCTargetLUN": 0,
        "SecondFCTargetWWPN": "00:00:00:00:00:00:00:00",
        "VirtualWWN": "20:00:00:10:9B:5A:4A:59",
        "VirtualWWPN": "10:00:00:10:9B:5A:4A:59",
        "WWN": "20:00:00:10:9B:5A:4A:59",
        "WWPN": "10:00:00:10:9B:5A:4A:59"
    },
    "Description": "DellNetworkAttributes represents the Network device attribute details.",
    "Id": "FC.Slot.1-2",
    "Name": "DellNetworkAttributes"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellNetworkAttributes/FC.Slot.1-2/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellNetworkAttributes/FC.Slot.1-2/Settings",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2/Oem/Dell/DellNetworkAttributes/FC.Slot.1-2/Settings/Actions/DellManager.ClearPending"
        }
    },
    "AttributeRegistry": "NetworkAttributeRegistry",
    "Attributes": {},
    "Description": "This schema provides settings of the oem attributes",
    "Id": "FC.Slot.1-2",
    "Name": "DellNetworkAttributes"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPortCollection.NetworkPortCollection",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts",
    "@odata.type": "#NetworkPortCollection.NetworkPortCollection",
    "Description": "Collection Of Network Port entities",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-2"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Network Port Collection"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPort.NetworkPort",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-1",
    "@odata.type": "#NetworkPort.v1_2_5.NetworkPort",
    "ActiveLinkTechnology": "FibreChannel",
    "AssociatedNetworkAddresses": [
        "20:00:00:10:9B:5A:4A:58"
    ],
    "CurrentLinkSpeedMbps": null,
    "Description": "Network Port View",
    "EEEEnabled": null,
    "FlowControlConfiguration": "None",
    "FlowControlStatus": "None",
    "Id": "FC.Slot.1-1",
    "LinkStatus": "Down",
    "Name": "Network Port View",
    "NetDevFuncMaxBWAlloc": [
        {
            "MaxBWAllocPercent": null,
            "NetworkDeviceFunction": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1"
            }
        }
    ],
    "NetDevFuncMaxBWAlloc@odata.count": 1,
    "NetDevFuncMinBWAlloc": [
        {
            "MinBWAllocPercent": null,
            "NetworkDeviceFunction": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-1"
            }
        }
    ],
    "NetDevFuncMinBWAlloc@odata.count": 1,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellNetworkTransceiver": {
                "@odata.context": "/redfish/v1/$metadata#DellNetworkTransceiver.DellNetworkTransceiver",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-1/Oem/Dell/DellNetworkTransceivers/NetworkTransceiver.Integrated.1:FC.Slot.1-1",
                "@odata.type": "#DellNetworkTransceiver.v1_0_0.DellNetworkTransceiver",
                "DeviceDescription": "Network Transceiver in Fibre Channel in Slot 1 Port 1",
                "FQDD": "NetworkTransceiver.Integrated.1:FC.Slot.1-1",
                "Id": "NetworkTransceiver.Integrated.1:FC.Slot.1-1",
                "IdentifierType": "SFP/SFP+/SFP28",
                "InterfaceType": "OpticalFiber",
                "Name": "DellNetworkTransceiver",
                "PartNumber": "AFBR-57G5MZ-ELX",
                "Revision": " ",
                "SerialNumber": "AD1827G03D5",
                "VendorName": "AVAGO"
            }
        }
    },
    "PhysicalPortNumber": "1",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SupportedEthernetCapabilities": [],
    "SupportedEthernetCapabilities@odata.count": 0,
    "SupportedLinkCapabilities": [
        {
            "LinkNetworkTechnology": "FibreChannel",
            "LinkSpeedMbps": 0
        }
    ],
    "SupportedLinkCapabilities@odata.count": 1,
    "VendorId": "10df"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-2

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPort.NetworkPort",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-2",
    "@odata.type": "#NetworkPort.v1_2_5.NetworkPort",
    "ActiveLinkTechnology": "FibreChannel",
    "AssociatedNetworkAddresses": [
        "20:00:00:10:9B:5A:4A:59"
    ],
    "CurrentLinkSpeedMbps": null,
    "Description": "Network Port View",
    "EEEEnabled": null,
    "FlowControlConfiguration": "None",
    "FlowControlStatus": "None",
    "Id": "FC.Slot.1-2",
    "LinkStatus": "Down",
    "Name": "Network Port View",
    "NetDevFuncMaxBWAlloc": [
        {
            "MaxBWAllocPercent": null,
            "NetworkDeviceFunction": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2"
            }
        }
    ],
    "NetDevFuncMaxBWAlloc@odata.count": 1,
    "NetDevFuncMinBWAlloc": [
        {
            "MinBWAllocPercent": null,
            "NetworkDeviceFunction": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkDeviceFunctions/FC.Slot.1-2"
            }
        }
    ],
    "NetDevFuncMinBWAlloc@odata.count": 1,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellNetworkTransceiver": {
                "@odata.context": "/redfish/v1/$metadata#DellNetworkTransceiver.DellNetworkTransceiver",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/FC.Slot.1/NetworkPorts/FC.Slot.1-2/Oem/Dell/DellNetworkTransceivers/NetworkTransceiver.Integrated.1:FC.Slot.1-2",
                "@odata.type": "#DellNetworkTransceiver.v1_0_0.DellNetworkTransceiver",
                "DeviceDescription": "Network Transceiver in Fibre Channel in Slot 1 Port 2",
                "FQDD": "NetworkTransceiver.Integrated.1:FC.Slot.1-2",
                "Id": "NetworkTransceiver.Integrated.1:FC.Slot.1-2",
                "IdentifierType": "SFP/SFP+/SFP28",
                "InterfaceType": "OpticalFiber",
                "Name": "DellNetworkTransceiver",
                "PartNumber": "AFBR-57G5MZ-ELX",
                "Revision": " ",
                "SerialNumber": "AD1827G03R3",
                "VendorName": "AVAGO"
            }
        }
    },
    "PhysicalPortNumber": "2",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SupportedEthernetCapabilities": [],
    "SupportedEthernetCapabilities@odata.count": 0,
    "SupportedLinkCapabilities": [
        {
            "LinkNetworkTechnology": "FibreChannel",
            "LinkSpeedMbps": 0
        }
    ],
    "SupportedLinkCapabilities@odata.count": 1,
    "VendorId": "10df"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkAdapter.NetworkAdapter",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1",
    "@odata.type": "#NetworkAdapter.v1_4_0.NetworkAdapter",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
    },
    "Controllers": [
        {
            "ControllerCapabilities": {
                "DataCenterBridging": {
                    "Capable": false
                },
                "NPAR": {
                    "NparCapable": false,
                    "NparEnabled": false
                },
                "NPIV": {
                    "MaxDeviceLogins": 0,
                    "MaxPortLogins": 0
                },
                "NetworkDeviceFunctionCount": 2,
                "NetworkPortCount": 2,
                "VirtualizationOffload": {
                    "SRIOV": {
                        "SRIOVVEPACapable": false
                    },
                    "VirtualFunction": {
                        "DeviceMaxCount": null,
                        "MinAssignmentGroupSize": null,
                        "NetworkPortMaxCount": null
                    }
                }
            },
            "FirmwarePackageVersion": "21.80.8",
            "Links": {
                "NetworkDeviceFunctions": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1"
                    }
                ],
                "NetworkDeviceFunctions@odata.count": 2,
                "NetworkPorts": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.2-1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.1-1"
                    }
                ],
                "NetworkPorts@odata.count": 2,
                "Oem": {
                    "Dell": {
                        "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                        "CPUAffinity": [],
                        "CPUAffinity@odata.count": 0
                    }
                }
            }
        }
    ],
    "Controllers@odata.count": 1,
    "Description": "Network Adapter View",
    "Id": "NIC.Embedded.1",
    "Manufacturer": "Broadcom Inc. and subsidiaries",
    "Model": null,
    "Name": "Network Adapter View",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts"
    },
    "PartNumber": null,
    "SerialNumber": null,
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunctionCollection.NetworkDeviceFunctionCollection",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions",
    "@odata.type": "#NetworkDeviceFunctionCollection.NetworkDeviceFunctionCollection",
    "Description": "Collection Of Network Device Function entities",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Network Device Function Collection"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Settings"
        },
        "SupportedApplyTimes": [
            "OnReset",
            "AtMaintenanceWindowStart",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1",
    "@odata.type": "#NetworkDeviceFunction.v1_5_1.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.1-1"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 1,
    "Description": "NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "70:B5:E8:F0:25:52",
        "MTUSize": null,
        "PermanentMACAddress": "70:B5:E8:F0:25:52",
        "VLAN": {
            "VLANEnable": false,
            "VLANId": 1
        }
    },
    "FibreChannel": {
        "BootTargets": [
            {
                "LUNID": null,
                "WWPN": null
            }
        ],
        "BootTargets@odata.count": 1,
        "FCoEActiveVLANId": null,
        "FCoELocalVLANId": null,
        "PermanentWWNN": null,
        "PermanentWWPN": null,
        "WWNN": null,
        "WWNSource": null,
        "WWPN": null
    },
    "Id": "NIC.Embedded.1-1-1",
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [],
                "CPUAffinity@odata.count": 0,
                "DellNetworkAttributes": {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.1-1-1"
                }
            }
        },
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.1-1"
        }
    },
    "MaxVirtualFunctions": null,
    "Name": "NetworkDeviceFunction",
    "NetDevFuncCapabilities": [
        "Disabled",
        "Ethernet"
    ],
    "NetDevFuncCapabilities@odata.count": 2,
    "NetDevFuncType": "Ethernet",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellFC": null,
            "DellFCCapabilities": null,
            "DellFCPortMetrics": null,
            "DellInfiniBand": null,
            "DellInfiniBandCapabilities": null,
            "DellInfiniBandPortMetrics": null,
            "DellNIC": {
                "@odata.context": "/redfish/v1/$metadata#DellNIC.DellNIC",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNIC/NIC.Embedded.1-1-1",
                "@odata.type": "#DellNIC.v1_4_0.DellNIC",
                "BusNumber": 4,
                "CableLengthMetres": null,
                "ControllerBIOSVersion": "1.39",
                "DataBusWidth": "Unknown",
                "DeviceDescription": "Embedded NIC 1 Port 1 Partition 1",
                "EFIVersion": "21.6.12",
                "FCoEOffloadMode": "Unknown",
                "FQDD": "NIC.Embedded.1-1-1",
                "FamilyVersion": "21.80.8",
                "Id": "NIC.Embedded.1-1-1",
                "IdentifierType": null,
                "InstanceID": "NIC.Embedded.1-1-1",
                "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
                "LastUpdateTime": "2021-07-14T03:23:00+00:00",
                "LinkDuplex": "Unknown",
                "MediaType": "Base T",
                "Name": "DellNIC",
                "NicMode": "Unknown",
                "PCIDeviceID": "165f",
                "PCISubDeviceID": "08ff",
                "PCISubVendorID": "1028",
                "PCIVendorID": "14e4",
                "PartNumber": null,
                "PermanentFCOEMACAddress": null,
                "PermanentiSCSIMACAddress": null,
                "ProductName": "Broadcom Gigabit Ethernet BCM5720 - 70:B5:E8:F0:25:52",
                "Protocol": "NIC",
                "Revision": null,
                "SNAPIState": "Disabled",
                "SNAPISupport": "NotAvailable",
                "SerialNumber": null,
                "SlotLength": "Unknown",
                "SlotType": "Unknown",
                "TransceiverPartNumber": null,
                "TransceiverSerialNumber": null,
                "TransceiverVendorName": null,
                "VPISupport": "NotAvailable",
                "VendorName": "Broadcom Corp",
                "iScsiOffloadMode": "Unknown"
            },
            "DellNICCapabilities": {
                "@odata.context": "/redfish/v1/$metadata#DellNICCapabilities.DellNICCapabilities",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNICCapabilities/NIC.Embedded.1-1-1",
                "@odata.type": "#DellNICCapabilities.v1_1_0.DellNICCapabilities",
                "BPESupport": "NotSupported",
                "CongestionNotification": "NotSupported",
                "ETS": "NotSupported",
                "EVBModesSupport": "NotSupported",
                "FCoEBootSupport": "NotSupported",
                "FCoEMaxIOsPerSession": 0,
                "FCoEMaxNPIVPerPort": 0,
                "FCoEMaxNumberExchanges": 0,
                "FCoEMaxNumberLogins": 0,
                "FCoEMaxNumberOfFCTargets": 0,
                "FCoEMaxNumberOutStandingCommands": 0,
                "FCoEOffloadSupport": "NotSupported",
                "FeatureLicensingSupport": "NotSupported",
                "FlexAddressingSupport": "Supported",
                "IPSecOffloadSupport": "NotSupported",
                "Id": "NIC.Embedded.1-1-1",
                "MACSecSupport": "NotSupported",
                "NWManagementPassThrough": "Supported",
                "Name": "DellNICCapabilities",
                "OSBMCManagementPassThrough": "Supported",
                "OnChipThermalSensor": "Supported",
                "OpenFlowSupport": "NotSupported",
                "PXEBootSupport": "Supported",
                "PartitionWOLSupport": "NotSupported",
                "PersistencePolicySupport": "Supported",
                "PriorityFlowControl": "NotSupported",
                "RDMASupport": "NotSupported",
                "RemotePHY": "NotSupported",
                "TCPChimneySupport": "NotSupported",
                "VEB": "NotSupported",
                "VEBVEPAMultiChannel": "NotSupported",
                "VEBVEPASingleChannel": "NotSupported",
                "VirtualLinkControl": "NotSupported",
                "iSCSIBootSupport": "NotSupported",
                "iSCSIOffloadSupport": "NotSupported",
                "uEFISupport": "Supported"
            },
            "DellNICPortMetrics": {
                "@odata.context": "/redfish/v1/$metadata#DellNICPortMetrics.DellNICPortMetrics",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNICPortMetrics/NIC.Embedded.1-1-1",
                "@odata.type": "#DellNICPortMetrics.v1_1_1.DellNICPortMetrics",
                "DiscardedPkts": 0,
                "FCCRCErrorCount": null,
                "FCOELinkFailures": null,
                "FCOEPktRxCount": null,
                "FCOEPktTxCount": null,
                "FCOERxPktDroppedCount": null,
                "FQDD": "NIC.Embedded.1-1-1",
                "LanFCSRxErrors": null,
                "LanUnicastPktRXCount": null,
                "LanUnicastPktTXCount": null,
                "OSDriverState": "Operational",
                "PartitionLinkStatus": null,
                "PartitionOSDriverState": null,
                "RDMARxTotalBytes": null,
                "RDMARxTotalPackets": null,
                "RDMATotalProtectionErrors": null,
                "RDMATotalProtocolErrors": null,
                "RDMATxTotalBytes": null,
                "RDMATxTotalPackets": null,
                "RDMATxTotalReadReqPkts": null,
                "RDMATxTotalSendPkts": null,
                "RDMATxTotalWritePkts": null,
                "RxBroadcast": 0,
                "RxBytes": 0,
                "RxErrorPktAlignmentErrors": 0,
                "RxErrorPktFCSErrors": 0,
                "RxFalseCarrierDetection": null,
                "RxJabberPkt": 0,
                "RxMutlicastPackets": 0,
                "RxPauseXOFFFrames": 0,
                "RxPauseXONFrames": 0,
                "RxRuntPkt": 0,
                "RxUnicastPackets": 0,
                "StartStatisticTime": "2022-08-30T17:01:47-05:00",
                "StatisticTime": "2022-10-26T15:50:35-05:00",
                "TxBroadcast": 0,
                "TxBytes": 0,
                "TxErrorPktExcessiveCollision": 0,
                "TxErrorPktLateCollision": 0,
                "TxErrorPktMultipleCollision": 0,
                "TxErrorPktSingleCollision": 0,
                "TxMutlicastPackets": 0,
                "TxPauseXOFFFrames": 0,
                "TxPauseXONFrames": 0,
                "TxUnicastPackets": 0
            }
        }
    },
    "PhysicalPortAssignment": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.1-1"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "iSCSIBoot": {}
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.1-1-1

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.1-1-1/Settings"
        },
        "SupportedApplyTimes": [
            "Immediate",
            "AtMaintenanceWindowStart",
            "OnReset",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.1-1-1",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "AttributeRegistry": "NetworkAttributeRegistry",
    "Attributes": {
        "BannerMessageTimeout": 5,
        "BlnkLeds": 0,
        "BootOptionROM": "Enabled",
        "BootStrapType": "AutoDetect",
        "BusDeviceFunction": "04:00:00",
        "ChipMdl": "BCM5720 A0",
        "ControllerBIOSVersion": "1.39",
        "EEEControl": "Enabled",
        "EFIVersion": "21.6.12",
        "EnergyEfficientEthernet": "Available",
        "FCoEBootSupport": "Unavailable",
        "FCoEOffloadSupport": "Unavailable",
        "FamilyVersion": "21.80.8",
        "FlexAddressing": "Unavailable",
        "HideSetupPrompt": "Disabled",
        "LegacyBootProto": "PXE",
        "LinkStatus": "Disconnected",
        "LnkSpeed": "AutoNeg",
        "MacAddr": "70:B5:E8:F0:25:52",
        "NicPartitioningSupport": "Unavailable",
        "PCIDeviceID": "165F",
        "PXEBootSupport": "Available",
        "PermitTotalPortShutdown": "Disabled",
        "TXBandwidthControlMaximum": "Unavailable",
        "TXBandwidthControlMinimum": "Unavailable",
        "VLanId": 1,
        "VLanMode": "Disabled",
        "VirtMacAddr": "70:B5:E8:F0:25:52",
        "WakeOnLan": "Disabled",
        "iSCSIBootSupport": "Unavailable",
        "iSCSIOffloadSupport": "Unavailable"
    },
    "Description": "DellNetworkAttributes represents the Network device attribute details.",
    "Id": "NIC.Embedded.1-1-1",
    "Name": "DellNetworkAttributes"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.1-1-1/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.1-1-1/Settings",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.1-1-1/Settings/Actions/DellManager.ClearPending"
        }
    },
    "AttributeRegistry": "NetworkAttributeRegistry",
    "Attributes": {},
    "Description": "This schema provides settings of the oem attributes",
    "Id": "NIC.Embedded.1-1-1",
    "Name": "DellNetworkAttributes"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Settings"
        },
        "SupportedApplyTimes": [
            "OnReset",
            "AtMaintenanceWindowStart",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1",
    "@odata.type": "#NetworkDeviceFunction.v1_5_1.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.2-1"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 1,
    "Description": "NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "70:B5:E8:F0:25:53",
        "MTUSize": null,
        "PermanentMACAddress": "70:B5:E8:F0:25:53",
        "VLAN": {
            "VLANEnable": false,
            "VLANId": 1
        }
    },
    "FibreChannel": {
        "BootTargets": [
            {
                "LUNID": null,
                "WWPN": null
            }
        ],
        "BootTargets@odata.count": 1,
        "FCoEActiveVLANId": null,
        "FCoELocalVLANId": null,
        "PermanentWWNN": null,
        "PermanentWWPN": null,
        "WWNN": null,
        "WWNSource": null,
        "WWPN": null
    },
    "Id": "NIC.Embedded.2-1-1",
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [],
                "CPUAffinity@odata.count": 0,
                "DellNetworkAttributes": {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.2-1-1"
                }
            }
        },
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.2-1"
        }
    },
    "MaxVirtualFunctions": null,
    "Name": "NetworkDeviceFunction",
    "NetDevFuncCapabilities": [
        "Disabled",
        "Ethernet"
    ],
    "NetDevFuncCapabilities@odata.count": 2,
    "NetDevFuncType": "Ethernet",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellFC": null,
            "DellFCCapabilities": null,
            "DellFCPortMetrics": null,
            "DellInfiniBand": null,
            "DellInfiniBandCapabilities": null,
            "DellInfiniBandPortMetrics": null,
            "DellNIC": {
                "@odata.context": "/redfish/v1/$metadata#DellNIC.DellNIC",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.2/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNIC/NIC.Embedded.2-1-1",
                "@odata.type": "#DellNIC.v1_4_0.DellNIC",
                "BusNumber": 4,
                "CableLengthMetres": null,
                "ControllerBIOSVersion": "1.39",
                "DataBusWidth": "Unknown",
                "DeviceDescription": "Embedded NIC 1 Port 2 Partition 1",
                "EFIVersion": "21.6.12",
                "FCoEOffloadMode": "Unknown",
                "FQDD": "NIC.Embedded.2-1-1",
                "FamilyVersion": "21.80.8",
                "Id": "NIC.Embedded.2-1-1",
                "IdentifierType": null,
                "InstanceID": "NIC.Embedded.2-1-1",
                "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
                "LastUpdateTime": "2021-07-02T22:29:07+00:00",
                "LinkDuplex": "Unknown",
                "MediaType": "Base T",
                "Name": "DellNIC",
                "NicMode": "Unknown",
                "PCIDeviceID": "165f",
                "PCISubDeviceID": "08ff",
                "PCISubVendorID": "1028",
                "PCIVendorID": "14e4",
                "PartNumber": null,
                "PermanentFCOEMACAddress": null,
                "PermanentiSCSIMACAddress": null,
                "ProductName": "Broadcom Gigabit Ethernet BCM5720 - 70:B5:E8:F0:25:53",
                "Protocol": "NIC",
                "Revision": null,
                "SNAPIState": "Disabled",
                "SNAPISupport": "NotAvailable",
                "SerialNumber": null,
                "SlotLength": "Unknown",
                "SlotType": "Unknown",
                "TransceiverPartNumber": null,
                "TransceiverSerialNumber": null,
                "TransceiverVendorName": null,
                "VPISupport": "NotAvailable",
                "VendorName": "Broadcom Corp",
                "iScsiOffloadMode": "Unknown"
            },
            "DellNICCapabilities": {
                "@odata.context": "/redfish/v1/$metadata#DellNICCapabilities.DellNICCapabilities",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.2/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNICCapabilities/NIC.Embedded.2-1-1",
                "@odata.type": "#DellNICCapabilities.v1_1_0.DellNICCapabilities",
                "BPESupport": "NotSupported",
                "CongestionNotification": "NotSupported",
                "ETS": "NotSupported",
                "EVBModesSupport": "NotSupported",
                "FCoEBootSupport": "NotSupported",
                "FCoEMaxIOsPerSession": 0,
                "FCoEMaxNPIVPerPort": 0,
                "FCoEMaxNumberExchanges": 0,
                "FCoEMaxNumberLogins": 0,
                "FCoEMaxNumberOfFCTargets": 0,
                "FCoEMaxNumberOutStandingCommands": 0,
                "FCoEOffloadSupport": "NotSupported",
                "FeatureLicensingSupport": "NotSupported",
                "FlexAddressingSupport": "Supported",
                "IPSecOffloadSupport": "NotSupported",
                "Id": "NIC.Embedded.2-1-1",
                "MACSecSupport": "NotSupported",
                "NWManagementPassThrough": "Supported",
                "Name": "DellNICCapabilities",
                "OSBMCManagementPassThrough": "Supported",
                "OnChipThermalSensor": "Supported",
                "OpenFlowSupport": "NotSupported",
                "PXEBootSupport": "Supported",
                "PartitionWOLSupport": "NotSupported",
                "PersistencePolicySupport": "Supported",
                "PriorityFlowControl": "NotSupported",
                "RDMASupport": "NotSupported",
                "RemotePHY": "NotSupported",
                "TCPChimneySupport": "NotSupported",
                "VEB": "NotSupported",
                "VEBVEPAMultiChannel": "NotSupported",
                "VEBVEPASingleChannel": "NotSupported",
                "VirtualLinkControl": "NotSupported",
                "iSCSIBootSupport": "NotSupported",
                "iSCSIOffloadSupport": "NotSupported",
                "uEFISupport": "Supported"
            },
            "DellNICPortMetrics": {
                "@odata.context": "/redfish/v1/$metadata#DellNICPortMetrics.DellNICPortMetrics",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Embedded.2/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNICPortMetrics/NIC.Embedded.2-1-1",
                "@odata.type": "#DellNICPortMetrics.v1_1_1.DellNICPortMetrics",
                "DiscardedPkts": 0,
                "FCCRCErrorCount": null,
                "FCOELinkFailures": null,
                "FCOEPktRxCount": null,
                "FCOEPktTxCount": null,
                "FCOERxPktDroppedCount": null,
                "FQDD": "NIC.Embedded.2-1-1",
                "LanFCSRxErrors": null,
                "LanUnicastPktRXCount": null,
                "LanUnicastPktTXCount": null,
                "OSDriverState": "Operational",
                "PartitionLinkStatus": null,
                "PartitionOSDriverState": null,
                "RDMARxTotalBytes": null,
                "RDMARxTotalPackets": null,
                "RDMATotalProtectionErrors": null,
                "RDMATotalProtocolErrors": null,
                "RDMATxTotalBytes": null,
                "RDMATxTotalPackets": null,
                "RDMATxTotalReadReqPkts": null,
                "RDMATxTotalSendPkts": null,
                "RDMATxTotalWritePkts": null,
                "RxBroadcast": 0,
                "RxBytes": 0,
                "RxErrorPktAlignmentErrors": 0,
                "RxErrorPktFCSErrors": 0,
                "RxFalseCarrierDetection": null,
                "RxJabberPkt": 0,
                "RxMutlicastPackets": 0,
                "RxPauseXOFFFrames": 0,
                "RxPauseXONFrames": 0,
                "RxRuntPkt": 0,
                "RxUnicastPackets": 0,
                "StartStatisticTime": "2022-08-30T17:01:47-05:00",
                "StatisticTime": "2022-10-26T15:50:30-05:00",
                "TxBroadcast": 0,
                "TxBytes": 0,
                "TxErrorPktExcessiveCollision": 0,
                "TxErrorPktLateCollision": 0,
                "TxErrorPktMultipleCollision": 0,
                "TxErrorPktSingleCollision": 0,
                "TxMutlicastPackets": 0,
                "TxPauseXOFFFrames": 0,
                "TxPauseXONFrames": 0,
                "TxUnicastPackets": 0
            }
        }
    },
    "PhysicalPortAssignment": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.2-1"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "iSCSIBoot": {}
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.2-1-1

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.2-1-1/Settings"
        },
        "SupportedApplyTimes": [
            "Immediate",
            "AtMaintenanceWindowStart",
            "OnReset",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.2-1-1",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "AttributeRegistry": "NetworkAttributeRegistry",
    "Attributes": {
        "BannerMessageTimeout": 5,
        "BlnkLeds": 0,
        "BootOptionROM": "Enabled",
        "BootStrapType": "AutoDetect",
        "BusDeviceFunction": "04:00:01",
        "ChipMdl": "BCM5720 A0",
        "ControllerBIOSVersion": "1.39",
        "EEEControl": "Enabled",
        "EFIVersion": "21.6.12",
        "EnergyEfficientEthernet": "Available",
        "FCoEBootSupport": "Unavailable",
        "FCoEOffloadSupport": "Unavailable",
        "FamilyVersion": "21.80.8",
        "FlexAddressing": "Unavailable",
        "HideSetupPrompt": "Disabled",
        "LegacyBootProto": "NONE",
        "LinkStatus": "Disconnected",
        "LnkSpeed": "AutoNeg",
        "MacAddr": "70:B5:E8:F0:25:53",
        "NicPartitioningSupport": "Unavailable",
        "PCIDeviceID": "165F",
        "PXEBootSupport": "Available",
        "PermitTotalPortShutdown": "Disabled",
        "TXBandwidthControlMaximum": "Unavailable",
        "TXBandwidthControlMinimum": "Unavailable",
        "VLanId": 1,
        "VLanMode": "Disabled",
        "VirtMacAddr": "70:B5:E8:F0:25:53",
        "WakeOnLan": "Disabled",
        "iSCSIBootSupport": "Unavailable",
        "iSCSIOffloadSupport": "Unavailable"
    },
    "Description": "DellNetworkAttributes represents the Network device attribute details.",
    "Id": "NIC.Embedded.2-1-1",
    "Name": "DellNetworkAttributes"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.2-1-1/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.2-1-1/Settings",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1/Oem/Dell/DellNetworkAttributes/NIC.Embedded.2-1-1/Settings/Actions/DellManager.ClearPending"
        }
    },
    "AttributeRegistry": "NetworkAttributeRegistry",
    "Attributes": {},
    "Description": "This schema provides settings of the oem attributes",
    "Id": "NIC.Embedded.2-1-1",
    "Name": "DellNetworkAttributes"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPortCollection.NetworkPortCollection",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts",
    "@odata.type": "#NetworkPortCollection.NetworkPortCollection",
    "Description": "Collection Of Network Port entities",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.1-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.2-1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Network Port Collection"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPort.NetworkPort",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.1-1",
    "@odata.type": "#NetworkPort.v1_2_5.NetworkPort",
    "ActiveLinkTechnology": "Ethernet",
    "AssociatedNetworkAddresses": [
        "70:B5:E8:F0:25:52"
    ],
    "CurrentLinkSpeedMbps": 0,
    "Description": "Network Port View",
    "EEEEnabled": true,
    "FlowControlConfiguration": "TX_RX",
    "FlowControlStatus": "TX_RX",
    "Id": "NIC.Embedded.1-1",
    "LinkStatus": "Down",
    "Name": "Network Port View",
    "NetDevFuncMaxBWAlloc": [
        {
            "MaxBWAllocPercent": null,
            "NetworkDeviceFunction": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1"
            }
        }
    ],
    "NetDevFuncMaxBWAlloc@odata.count": 1,
    "NetDevFuncMinBWAlloc": [
        {
            "MinBWAllocPercent": null,
            "NetworkDeviceFunction": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.1-1-1"
            }
        }
    ],
    "NetDevFuncMinBWAlloc@odata.count": 1,
    "Oem": {},
    "PhysicalPortNumber": "1",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SupportedEthernetCapabilities": [
        "WakeOnLAN",
        "EEE"
    ],
    "SupportedEthernetCapabilities@odata.count": 2,
    "SupportedLinkCapabilities": [
        {
            "AutoSpeedNegotiation": false,
            "LinkNetworkTechnology": "Ethernet",
            "LinkSpeedMbps": 0
        }
    ],
    "SupportedLinkCapabilities@odata.count": 1,
    "VendorId": "14e4",
    "WakeOnLANEnabled": false
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.2-1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPort.NetworkPort",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkPorts/NIC.Embedded.2-1",
    "@odata.type": "#NetworkPort.v1_2_5.NetworkPort",
    "ActiveLinkTechnology": "Ethernet",
    "AssociatedNetworkAddresses": [
        "70:B5:E8:F0:25:53"
    ],
    "CurrentLinkSpeedMbps": 0,
    "Description": "Network Port View",
    "EEEEnabled": true,
    "FlowControlConfiguration": "TX_RX",
    "FlowControlStatus": "TX_RX",
    "Id": "NIC.Embedded.2-1",
    "LinkStatus": "Down",
    "Name": "Network Port View",
    "NetDevFuncMaxBWAlloc": [
        {
            "MaxBWAllocPercent": null,
            "NetworkDeviceFunction": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1"
            }
        }
    ],
    "NetDevFuncMaxBWAlloc@odata.count": 1,
    "NetDevFuncMinBWAlloc": [
        {
            "MinBWAllocPercent": null,
            "NetworkDeviceFunction": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Embedded.1/NetworkDeviceFunctions/NIC.Embedded.2-1-1"
            }
        }
    ],
    "NetDevFuncMinBWAlloc@odata.count": 1,
    "Oem": {},
    "PhysicalPortNumber": "2",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SupportedEthernetCapabilities": [
        "WakeOnLAN",
        "EEE"
    ],
    "SupportedEthernetCapabilities@odata.count": 2,
    "SupportedLinkCapabilities": [
        {
            "AutoSpeedNegotiation": false,
            "LinkNetworkTechnology": "Ethernet",
            "LinkSpeedMbps": 0
        }
    ],
    "SupportedLinkCapabilities@odata.count": 1,
    "VendorId": "14e4",
    "WakeOnLANEnabled": false
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkAdapter.NetworkAdapter",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1",
    "@odata.type": "#NetworkAdapter.v1_4_0.NetworkAdapter",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/Assembly"
    },
    "Controllers": [
        {
            "ControllerCapabilities": {
                "DataCenterBridging": {
                    "Capable": true
                },
                "NPAR": {
                    "NparCapable": false,
                    "NparEnabled": false
                },
                "NPIV": {
                    "MaxDeviceLogins": 0,
                    "MaxPortLogins": 0
                },
                "NetworkDeviceFunctionCount": 2,
                "NetworkPortCount": 2,
                "VirtualizationOffload": {
                    "SRIOV": {
                        "SRIOVVEPACapable": true
                    },
                    "VirtualFunction": {
                        "DeviceMaxCount": 254,
                        "MinAssignmentGroupSize": 8,
                        "NetworkPortMaxCount": 127
                    }
                }
            },
            "FirmwarePackageVersion": "16.28.45.12",
            "Links": {
                "NetworkDeviceFunctions": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1"
                    }
                ],
                "NetworkDeviceFunctions@odata.count": 2,
                "NetworkPorts": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-2"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-1"
                    }
                ],
                "NetworkPorts@odata.count": 2,
                "Oem": {
                    "Dell": {
                        "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                        "CPUAffinity": [
                            {
                                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                            }
                        ],
                        "CPUAffinity@odata.count": 1
                    }
                }
            }
        }
    ],
    "Controllers@odata.count": 1,
    "Description": "Network Adapter View",
    "Id": "NIC.Integrated.1",
    "Manufacturer": "Mellanox Technologies",
    "Model": "MLNX 25GbE 2P ConnectX5 OCP3 NIC",
    "Name": "Network Adapter View",
    "NetworkDeviceFunctions": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions"
    },
    "NetworkPorts": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts"
    },
    "PartNumber": "04TRD3",
    "SerialNumber": "INJBNM414TJ0AL",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/Assembly",
    "@odata.type": "#Assembly.v1_2_3.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/Assembly#/Assemblies/0",
            "@odata.type": "#Assembly.v1_2_3.AssemblyData",
            "BinaryDataURI": null,
            "Description": "MLNX 25GbE 2P ConnectX5 OCP3 NIC",
            "EngineeringChangeLevel": "A03",
            "MemberId": "0",
            "Model": "MLNX 25GbE 2P ConnectX5 OCP3 NIC",
            "Name": "NIC.Integrated.1#FRU",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellAssembly": {
                        "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/NIC.Integrated.1_0x23_FRU",
                        "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
                        "DeviceFQDD": "NIC.Integrated.1",
                        "Id": "NIC.Integrated.1#FRU",
                        "Name": "DellAssembly",
                        "PackageType": "Module/Card",
                        "SerialNumber": "INJBNM414TJ0AL"
                    }
                }
            },
            "PartNumber": "04TRD3",
            "Producer": "Dell",
            "ProductionDate": "2021-04-30T10:54:00Z",
            "SKU": null,
            "SparePartNumber": null,
            "Vendor": "DELL",
            "Version": null
        }
    ],
    "Assemblies@odata.count": 1,
    "Id": "PCIE Assembly",
    "Name": "NIC.Integrated.1#FRU"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunctionCollection.NetworkDeviceFunctionCollection",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions",
    "@odata.type": "#NetworkDeviceFunctionCollection.NetworkDeviceFunctionCollection",
    "Description": "Collection Of Network Device Function entities",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Network Device Function Collection"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Settings"
        },
        "SupportedApplyTimes": [
            "OnReset",
            "AtMaintenanceWindowStart",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1",
    "@odata.type": "#NetworkDeviceFunction.v1_5_1.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-1"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 1,
    "Description": "NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "B8:CE:F6:94:F0:B8",
        "MTUSize": null,
        "PermanentMACAddress": "B8:CE:F6:94:F0:B8",
        "VLAN": {
            "VLANEnable": false,
            "VLANId": 1
        }
    },
    "FibreChannel": {
        "BootTargets": [
            {
                "LUNID": null,
                "WWPN": null
            }
        ],
        "BootTargets@odata.count": 1,
        "FCoEActiveVLANId": null,
        "FCoELocalVLANId": null,
        "PermanentWWNN": null,
        "PermanentWWPN": null,
        "WWNN": null,
        "WWNSource": null,
        "WWPN": null
    },
    "Id": "NIC.Integrated.1-1-1",
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1,
                "DellNetworkAttributes": {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-1-1"
                }
            }
        },
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-1"
        }
    },
    "MaxVirtualFunctions": 127,
    "Name": "NetworkDeviceFunction",
    "NetDevFuncCapabilities": [
        "Disabled",
        "Ethernet",
        "iSCSI"
    ],
    "NetDevFuncCapabilities@odata.count": 3,
    "NetDevFuncType": "Ethernet",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellFC": null,
            "DellFCCapabilities": null,
            "DellFCPortMetrics": null,
            "DellInfiniBand": null,
            "DellInfiniBandCapabilities": null,
            "DellInfiniBandPortMetrics": null,
            "DellNIC": {
                "@odata.context": "/redfish/v1/$metadata#DellNIC.DellNIC",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNIC/NIC.Integrated.1-1-1",
                "@odata.type": "#DellNIC.v1_4_0.DellNIC",
                "BusNumber": 49,
                "CableLengthMetres": null,
                "ControllerBIOSVersion": null,
                "DataBusWidth": "Unknown",
                "DeviceDescription": "Integrated NIC 1 Port 1 Partition 1",
                "EFIVersion": "14.22.15",
                "FCoEOffloadMode": "Unknown",
                "FQDD": "NIC.Integrated.1-1-1",
                "FamilyVersion": "16.28.45.12",
                "Id": "NIC.Integrated.1-1-1",
                "IdentifierType": null,
                "InstanceID": "NIC.Integrated.1-1-1",
                "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
                "LastUpdateTime": "2022-08-04T16:53:47+00:00",
                "LinkDuplex": "FullDuplex",
                "MediaType": "SFF_CAGE",
                "Name": "DellNIC",
                "NicMode": "Enabled",
                "PCIDeviceID": "1017",
                "PCISubDeviceID": "0097",
                "PCISubVendorID": "15b3",
                "PCIVendorID": "15b3",
                "PartNumber": "04TRD3",
                "PermanentFCOEMACAddress": null,
                "PermanentiSCSIMACAddress": null,
                "ProductName": "Mellanox ConnectX-5 EN 25GbE Dual-port SFP28 Adapter - B8:CE:F6:94:F0:B8",
                "Protocol": "NIC,RDMA",
                "Revision": null,
                "SNAPIState": "Disabled",
                "SNAPISupport": "NotAvailable",
                "SerialNumber": "INJBNM414TJ0AL",
                "SlotLength": "Unknown",
                "SlotType": "Unknown",
                "TransceiverPartNumber": null,
                "TransceiverSerialNumber": null,
                "TransceiverVendorName": null,
                "VPISupport": "NotAvailable",
                "VendorName": "Mellanox Technologies, Inc.",
                "iScsiOffloadMode": "Unknown"
            },
            "DellNICCapabilities": {
                "@odata.context": "/redfish/v1/$metadata#DellNICCapabilities.DellNICCapabilities",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNICCapabilities/NIC.Integrated.1-1-1",
                "@odata.type": "#DellNICCapabilities.v1_1_0.DellNICCapabilities",
                "BPESupport": "NotSupported",
                "CongestionNotification": "Supported",
                "ETS": "Supported",
                "EVBModesSupport": "NotSupported",
                "FCoEBootSupport": "NotSupported",
                "FCoEMaxIOsPerSession": 0,
                "FCoEMaxNPIVPerPort": 0,
                "FCoEMaxNumberExchanges": 0,
                "FCoEMaxNumberLogins": 0,
                "FCoEMaxNumberOfFCTargets": 0,
                "FCoEMaxNumberOutStandingCommands": 0,
                "FCoEOffloadSupport": "NotSupported",
                "FeatureLicensingSupport": "NotSupported",
                "FlexAddressingSupport": "Supported",
                "IPSecOffloadSupport": "NotSupported",
                "Id": "NIC.Integrated.1-1-1",
                "MACSecSupport": "NotSupported",
                "NWManagementPassThrough": "Supported",
                "Name": "DellNICCapabilities",
                "OSBMCManagementPassThrough": "Supported",
                "OnChipThermalSensor": "Supported",
                "OpenFlowSupport": "NotSupported",
                "PXEBootSupport": "Supported",
                "PartitionWOLSupport": "NotSupported",
                "PersistencePolicySupport": "Supported",
                "PriorityFlowControl": "Supported",
                "RDMASupport": "Supported",
                "RemotePHY": "NotSupported",
                "TCPChimneySupport": "NotSupported",
                "VEB": "NotSupported",
                "VEBVEPAMultiChannel": "NotSupported",
                "VEBVEPASingleChannel": "NotSupported",
                "VirtualLinkControl": "NotSupported",
                "iSCSIBootSupport": "Supported",
                "iSCSIOffloadSupport": "NotSupported",
                "uEFISupport": "Supported"
            },
            "DellNICPortMetrics": {
                "@odata.context": "/redfish/v1/$metadata#DellNICPortMetrics.DellNICPortMetrics",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNICPortMetrics/NIC.Integrated.1-1-1",
                "@odata.type": "#DellNICPortMetrics.v1_1_1.DellNICPortMetrics",
                "DiscardedPkts": 0,
                "FCCRCErrorCount": null,
                "FCOELinkFailures": null,
                "FCOEPktRxCount": null,
                "FCOEPktTxCount": null,
                "FCOERxPktDroppedCount": null,
                "FQDD": "NIC.Integrated.1-1-1",
                "LanFCSRxErrors": null,
                "LanUnicastPktRXCount": null,
                "LanUnicastPktTXCount": null,
                "OSDriverState": "Operational",
                "PartitionLinkStatus": null,
                "PartitionOSDriverState": null,
                "RDMARxTotalBytes": 0,
                "RDMARxTotalPackets": 0,
                "RDMATotalProtectionErrors": null,
                "RDMATotalProtocolErrors": null,
                "RDMATxTotalBytes": 0,
                "RDMATxTotalPackets": 0,
                "RDMATxTotalReadReqPkts": null,
                "RDMATxTotalSendPkts": null,
                "RDMATxTotalWritePkts": null,
                "RxBroadcast": 4304449747,
                "RxBytes": 828323997018,
                "RxErrorPktAlignmentErrors": 0,
                "RxErrorPktFCSErrors": 0,
                "RxFalseCarrierDetection": 0,
                "RxJabberPkt": 0,
                "RxMutlicastPackets": 963469206,
                "RxPauseXOFFFrames": 0,
                "RxPauseXONFrames": 0,
                "RxRuntPkt": 0,
                "RxUnicastPackets": 969898405,
                "StartStatisticTime": "2022-08-30T17:01:47-05:00",
                "StatisticTime": "2022-10-26T15:50:40-05:00",
                "TxBroadcast": 82721,
                "TxBytes": 15381706231,
                "TxErrorPktExcessiveCollision": 0,
                "TxErrorPktLateCollision": 0,
                "TxErrorPktMultipleCollision": 0,
                "TxErrorPktSingleCollision": 0,
                "TxMutlicastPackets": 545996,
                "TxPauseXOFFFrames": 0,
                "TxPauseXONFrames": 0,
                "TxUnicastPackets": 25776787
            }
        }
    },
    "PhysicalPortAssignment": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-1"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "iSCSIBoot": {
        "AuthenticationMethod": "None",
        "CHAPSecret": null,
        "CHAPUsername": null,
        "IPAddressType": "IPv4",
        "IPMaskDNSViaDHCP": false,
        "InitiatorDefaultGateway": "0.0.0.0",
        "InitiatorIPAddress": "0.0.0.0",
        "InitiatorName": null,
        "InitiatorNetmask": "0.0.0.0",
        "PrimaryDNS": "0.0.0.0",
        "PrimaryLUN": 0,
        "PrimaryTargetIPAddress": "0.0.0.0",
        "PrimaryTargetName": null,
        "PrimaryTargetTCPPort": 3260,
        "PrimaryVLANEnable": null,
        "PrimaryVLANId": null,
        "SecondaryDNS": null,
        "SecondaryLUN": null,
        "SecondaryTargetIPAddress": null,
        "SecondaryTargetName": null,
        "SecondaryTargetTCPPort": null,
        "SecondaryVLANEnable": null,
        "SecondaryVLANId": null,
        "TargetInfoViaDHCP": false
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-1-1

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-1-1/Settings"
        },
        "SupportedApplyTimes": [
            "Immediate",
            "AtMaintenanceWindowStart",
            "OnReset",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-1-1",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "AttributeRegistry": "NetworkAttributeRegistry",
    "Attributes": {
        "BannerMessageTimeout": 4,
        "BlnkLeds": 15,
        "BootRetryCnt": "NoRetry",
        "BootStrapType": "Int19h",
        "BusDeviceFunction": "31:00:00",
        "ChapAuthEnable": "Disabled",
        "ChapMutualAuth": "Disabled",
        "ChipMdl": "ConnectX-5",
        "CongestionNotification": "Available",
        "ConnectFirstTgt": "Disabled",
        "DCBXSupport": "Available",
        "DeviceName": "Mellanox ConnectX-5 EN 25GbE Dual-port SFP28 Adapter",
        "EFIVersion": "14.22.15",
        "EVBModesSupport": "VEB",
        "EnergyEfficientEthernet": "Unavailable",
        "EnhancedTransmissionSelection": "Available",
        "FCoEBootSupport": "Unavailable",
        "FCoEOffloadSupport": "Unavailable",
        "FamilyVersion": "16.28.45.12",
        "FeatureLicensingSupport": "Unavailable",
        "FirstTgtBootLun": 0,
        "FirstTgtChapId": null,
        "FirstTgtChapPwd": null,
        "FirstTgtIpAddress": "0.0.0.0",
        "FirstTgtIscsiName": null,
        "FirstTgtTcpPort": 3260,
        "FlexAddressing": "Available",
        "ForwardErrorCorrection": "Disabled",
        "InfiniBand": "Unavailable",
        "IpVer": "IPv4",
        "IscsiInitiatorChapId": null,
        "IscsiInitiatorChapPwd": null,
        "IscsiInitiatorGateway": "0.0.0.0",
        "IscsiInitiatorIpAddr": "0.0.0.0",
        "IscsiInitiatorName": null,
        "IscsiInitiatorPrimDns": "0.0.0.0",
        "IscsiInitiatorSubnet": "0.0.0.0",
        "IscsiTgtBoot": "Disabled",
        "IscsiViaDHCP": "Disabled",
        "LegacyBootProto": "PXE",
        "LinkStatus": "Connected",
        "LnkSpeed": "AutoNeg",
        "MacAddr": "B8:CE:F6:94:F0:B8",
        "NWManagementPassThrough": "Available",
        "NicMode": "Enabled",
        "NicPartitioningSupport": "Unavailable",
        "NumberPCIFunctionsEnabled": 1,
        "NumberPCIFunctionsSupported": 1,
        "NumberVFAdvertised": 8,
        "NumberVFSupported": 127,
        "OSBMCManagementPassThrough": "Available",
        "OnChipThermalSensor": "Available",
        "PCIDeviceID": "1017",
        "PXEBootSupport": "Available",
        "PartitionStateInterpretation": "Fixed",
        "PermitTotalPortShutdown": "Disabled",
        "PriorityFlowControl": "Available",
        "RDMANICModeOnPort": "Enabled",
        "RDMAProtocolSupport": "RoCE",
        "RDMASupport": "Available",
        "RXFlowControl": "Available",
        "RemotePHY": "Unavailable",
        "SNAPI": "Unavailable",
        "SNAPIState": "Disabled",
        "SRIOVSupport": "Available",
        "TOESupport": "Unavailable",
        "TXBandwidthControlMaximum": "Available",
        "TXBandwidthControlMinimum": "Available",
        "TXFlowControl": "Available",
        "TcpIpViaDHCP": "Disabled",
        "VFAllocBasis": "Device",
        "VFAllocMult": 1,
        "VFDistribution": "8",
        "VLanId": 1,
        "VLanMode": "Disabled",
        "VPI": "Unavailable",
        "VirtMacAddr": "00:00:00:00:00:00",
        "VirtualizationMode": "NONE",
        "WakeOnLan": "Enabled",
        "WakeOnLanLnkSpeed": "1Gbps",
        "iSCSIBootSupport": "Available",
        "iSCSIDualIPVersionSupport": "Unavailable",
        "iSCSIOffloadSupport": "Unavailable"
    },
    "Description": "DellNetworkAttributes represents the Network device attribute details.",
    "Id": "NIC.Integrated.1-1-1",
    "Name": "DellNetworkAttributes"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-1-1/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-1-1/Settings",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-1-1/Settings/Actions/DellManager.ClearPending"
        }
    },
    "AttributeRegistry": "NetworkAttributeRegistry",
    "Attributes": {},
    "Description": "This schema provides settings of the oem attributes",
    "Id": "NIC.Integrated.1-1-1",
    "Name": "DellNetworkAttributes"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Settings"
        },
        "SupportedApplyTimes": [
            "OnReset",
            "AtMaintenanceWindowStart",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#NetworkDeviceFunction.NetworkDeviceFunction",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1",
    "@odata.type": "#NetworkDeviceFunction.v1_5_1.NetworkDeviceFunction",
    "AssignablePhysicalPorts": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-2"
        }
    ],
    "AssignablePhysicalPorts@odata.count": 1,
    "Description": "NetworkDeviceFunction",
    "Ethernet": {
        "MACAddress": "B8:CE:F6:94:F0:B9",
        "MTUSize": null,
        "PermanentMACAddress": "B8:CE:F6:94:F0:B9",
        "VLAN": {
            "VLANEnable": false,
            "VLANId": 1
        }
    },
    "FibreChannel": {
        "BootTargets": [
            {
                "LUNID": null,
                "WWPN": null
            }
        ],
        "BootTargets@odata.count": 1,
        "FCoEActiveVLANId": null,
        "FCoELocalVLANId": null,
        "PermanentWWNN": null,
        "PermanentWWPN": null,
        "WWNN": null,
        "WWNSource": null,
        "WWPN": null
    },
    "Id": "NIC.Integrated.1-2-1",
    "Links": {
        "Oem": {
            "Dell": {
                "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                "CPUAffinity": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                    }
                ],
                "CPUAffinity@odata.count": 1,
                "DellNetworkAttributes": {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-2-1"
                }
            }
        },
        "PhysicalPortAssignment": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-2"
        }
    },
    "MaxVirtualFunctions": 127,
    "Name": "NetworkDeviceFunction",
    "NetDevFuncCapabilities": [
        "Disabled",
        "Ethernet",
        "iSCSI"
    ],
    "NetDevFuncCapabilities@odata.count": 3,
    "NetDevFuncType": "Ethernet",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellFC": null,
            "DellFCCapabilities": null,
            "DellFCPortMetrics": null,
            "DellInfiniBand": null,
            "DellInfiniBandCapabilities": null,
            "DellInfiniBandPortMetrics": null,
            "DellNIC": {
                "@odata.context": "/redfish/v1/$metadata#DellNIC.DellNIC",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNIC/NIC.Integrated.1-2-1",
                "@odata.type": "#DellNIC.v1_4_0.DellNIC",
                "BusNumber": 49,
                "CableLengthMetres": null,
                "ControllerBIOSVersion": null,
                "DataBusWidth": "Unknown",
                "DeviceDescription": "Integrated NIC 1 Port 2 Partition 1",
                "EFIVersion": "14.22.15",
                "FCoEOffloadMode": "Unknown",
                "FQDD": "NIC.Integrated.1-2-1",
                "FamilyVersion": "16.28.45.12",
                "Id": "NIC.Integrated.1-2-1",
                "IdentifierType": null,
                "InstanceID": "NIC.Integrated.1-2-1",
                "LastSystemInventoryTime": "2022-08-04T15:53:48+00:00",
                "LastUpdateTime": "2022-08-04T16:53:47+00:00",
                "LinkDuplex": "FullDuplex",
                "MediaType": "SFF_CAGE",
                "Name": "DellNIC",
                "NicMode": "Enabled",
                "PCIDeviceID": "1017",
                "PCISubDeviceID": "0097",
                "PCISubVendorID": "15b3",
                "PCIVendorID": "15b3",
                "PartNumber": "04TRD3",
                "PermanentFCOEMACAddress": null,
                "PermanentiSCSIMACAddress": null,
                "ProductName": "Mellanox ConnectX-5 EN 25GbE Dual-port SFP28 Adapter - B8:CE:F6:94:F0:B9",
                "Protocol": "NIC,RDMA",
                "Revision": null,
                "SNAPIState": "Disabled",
                "SNAPISupport": "NotAvailable",
                "SerialNumber": "INJBNM414TJ0AL",
                "SlotLength": "Unknown",
                "SlotType": "Unknown",
                "TransceiverPartNumber": null,
                "TransceiverSerialNumber": null,
                "TransceiverVendorName": null,
                "VPISupport": "NotAvailable",
                "VendorName": "Mellanox Technologies, Inc.",
                "iScsiOffloadMode": "Unknown"
            },
            "DellNICCapabilities": {
                "@odata.context": "/redfish/v1/$metadata#DellNICCapabilities.DellNICCapabilities",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNICCapabilities/NIC.Integrated.1-2-1",
                "@odata.type": "#DellNICCapabilities.v1_1_0.DellNICCapabilities",
                "BPESupport": "NotSupported",
                "CongestionNotification": "Supported",
                "ETS": "Supported",
                "EVBModesSupport": "NotSupported",
                "FCoEBootSupport": "NotSupported",
                "FCoEMaxIOsPerSession": 0,
                "FCoEMaxNPIVPerPort": 0,
                "FCoEMaxNumberExchanges": 0,
                "FCoEMaxNumberLogins": 0,
                "FCoEMaxNumberOfFCTargets": 0,
                "FCoEMaxNumberOutStandingCommands": 0,
                "FCoEOffloadSupport": "NotSupported",
                "FeatureLicensingSupport": "NotSupported",
                "FlexAddressingSupport": "Supported",
                "IPSecOffloadSupport": "NotSupported",
                "Id": "NIC.Integrated.1-2-1",
                "MACSecSupport": "NotSupported",
                "NWManagementPassThrough": "Supported",
                "Name": "DellNICCapabilities",
                "OSBMCManagementPassThrough": "Supported",
                "OnChipThermalSensor": "Supported",
                "OpenFlowSupport": "NotSupported",
                "PXEBootSupport": "Supported",
                "PartitionWOLSupport": "NotSupported",
                "PersistencePolicySupport": "Supported",
                "PriorityFlowControl": "Supported",
                "RDMASupport": "Supported",
                "RemotePHY": "NotSupported",
                "TCPChimneySupport": "NotSupported",
                "VEB": "NotSupported",
                "VEBVEPAMultiChannel": "NotSupported",
                "VEBVEPASingleChannel": "NotSupported",
                "VirtualLinkControl": "NotSupported",
                "iSCSIBootSupport": "Supported",
                "iSCSIOffloadSupport": "NotSupported",
                "uEFISupport": "Supported"
            },
            "DellNICPortMetrics": {
                "@odata.context": "/redfish/v1/$metadata#DellNICPortMetrics.DellNICPortMetrics",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNICPortMetrics/NIC.Integrated.1-2-1",
                "@odata.type": "#DellNICPortMetrics.v1_1_1.DellNICPortMetrics",
                "DiscardedPkts": 0,
                "FCCRCErrorCount": null,
                "FCOELinkFailures": null,
                "FCOEPktRxCount": null,
                "FCOEPktTxCount": null,
                "FCOERxPktDroppedCount": null,
                "FQDD": "NIC.Integrated.1-2-1",
                "LanFCSRxErrors": null,
                "LanUnicastPktRXCount": null,
                "LanUnicastPktTXCount": null,
                "OSDriverState": "Operational",
                "PartitionLinkStatus": null,
                "PartitionOSDriverState": null,
                "RDMARxTotalBytes": 0,
                "RDMARxTotalPackets": 0,
                "RDMATotalProtectionErrors": null,
                "RDMATotalProtocolErrors": null,
                "RDMATxTotalBytes": 0,
                "RDMATxTotalPackets": 0,
                "RDMATxTotalReadReqPkts": null,
                "RDMATxTotalSendPkts": null,
                "RDMATxTotalWritePkts": null,
                "RxBroadcast": 3865711632,
                "RxBytes": 720933706011,
                "RxErrorPktAlignmentErrors": 0,
                "RxErrorPktFCSErrors": 0,
                "RxFalseCarrierDetection": 0,
                "RxJabberPkt": 0,
                "RxMutlicastPackets": 831027785,
                "RxPauseXOFFFrames": 0,
                "RxPauseXONFrames": 0,
                "RxRuntPkt": 0,
                "RxUnicastPackets": 855696971,
                "StartStatisticTime": "2022-08-30T17:01:47-05:00",
                "StatisticTime": "2022-10-26T15:50:40-05:00",
                "TxBroadcast": 1,
                "TxBytes": 14852656,
                "TxErrorPktExcessiveCollision": 0,
                "TxErrorPktLateCollision": 0,
                "TxErrorPktMultipleCollision": 0,
                "TxErrorPktSingleCollision": 0,
                "TxMutlicastPackets": 206286,
                "TxPauseXOFFFrames": 0,
                "TxPauseXONFrames": 0,
                "TxUnicastPackets": 0
            }
        }
    },
    "PhysicalPortAssignment": {
        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-2"
    },
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "iSCSIBoot": {
        "AuthenticationMethod": "None",
        "CHAPSecret": null,
        "CHAPUsername": null,
        "IPAddressType": "IPv4",
        "IPMaskDNSViaDHCP": false,
        "InitiatorDefaultGateway": "0.0.0.0",
        "InitiatorIPAddress": "0.0.0.0",
        "InitiatorName": null,
        "InitiatorNetmask": "0.0.0.0",
        "PrimaryDNS": "0.0.0.0",
        "PrimaryLUN": 0,
        "PrimaryTargetIPAddress": "0.0.0.0",
        "PrimaryTargetName": null,
        "PrimaryTargetTCPPort": 3260,
        "PrimaryVLANEnable": null,
        "PrimaryVLANId": null,
        "SecondaryDNS": null,
        "SecondaryLUN": null,
        "SecondaryTargetIPAddress": null,
        "SecondaryTargetName": null,
        "SecondaryTargetTCPPort": null,
        "SecondaryVLANEnable": null,
        "SecondaryVLANId": null,
        "TargetInfoViaDHCP": false
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-2-1

```{
    "@Redfish.Settings": {
        "@odata.context": "/redfish/v1/$metadata#Settings.Settings",
        "@odata.type": "#Settings.v1_3_1.Settings",
        "SettingsObject": {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-2-1/Settings"
        },
        "SupportedApplyTimes": [
            "Immediate",
            "AtMaintenanceWindowStart",
            "OnReset",
            "InMaintenanceWindowOnReset"
        ]
    },
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-2-1",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "AttributeRegistry": "NetworkAttributeRegistry",
    "Attributes": {
        "BannerMessageTimeout": 4,
        "BlnkLeds": 15,
        "BootRetryCnt": "NoRetry",
        "BootStrapType": "Int19h",
        "BusDeviceFunction": "31:00:01",
        "ChapAuthEnable": "Disabled",
        "ChapMutualAuth": "Disabled",
        "ChipMdl": "ConnectX-5",
        "CongestionNotification": "Available",
        "ConnectFirstTgt": "Disabled",
        "DCBXSupport": "Available",
        "DeviceName": "Mellanox ConnectX-5 EN 25GbE Dual-port SFP28 Adapter",
        "EFIVersion": "14.22.15",
        "EVBModesSupport": "VEB",
        "EnergyEfficientEthernet": "Unavailable",
        "EnhancedTransmissionSelection": "Available",
        "FCoEBootSupport": "Unavailable",
        "FCoEOffloadSupport": "Unavailable",
        "FamilyVersion": "16.28.45.12",
        "FeatureLicensingSupport": "Unavailable",
        "FirstTgtBootLun": 0,
        "FirstTgtChapId": null,
        "FirstTgtChapPwd": null,
        "FirstTgtIpAddress": "0.0.0.0",
        "FirstTgtIscsiName": null,
        "FirstTgtTcpPort": 3260,
        "FlexAddressing": "Available",
        "ForwardErrorCorrection": "Disabled",
        "InfiniBand": "Unavailable",
        "IpVer": "IPv4",
        "IscsiInitiatorChapId": null,
        "IscsiInitiatorChapPwd": null,
        "IscsiInitiatorGateway": "0.0.0.0",
        "IscsiInitiatorIpAddr": "0.0.0.0",
        "IscsiInitiatorName": null,
        "IscsiInitiatorPrimDns": "0.0.0.0",
        "IscsiInitiatorSubnet": "0.0.0.0",
        "IscsiTgtBoot": "Disabled",
        "IscsiViaDHCP": "Disabled",
        "LegacyBootProto": "NONE",
        "LinkStatus": "Connected",
        "LnkSpeed": "AutoNeg",
        "MacAddr": "B8:CE:F6:94:F0:B9",
        "NWManagementPassThrough": "Available",
        "NicMode": "Enabled",
        "NicPartitioningSupport": "Unavailable",
        "NumberPCIFunctionsEnabled": 1,
        "NumberPCIFunctionsSupported": 1,
        "NumberVFAdvertised": 8,
        "NumberVFSupported": 127,
        "OSBMCManagementPassThrough": "Available",
        "OnChipThermalSensor": "Available",
        "PCIDeviceID": "1017",
        "PXEBootSupport": "Available",
        "PartitionStateInterpretation": "Fixed",
        "PermitTotalPortShutdown": "Disabled",
        "PriorityFlowControl": "Available",
        "RDMANICModeOnPort": "Enabled",
        "RDMAProtocolSupport": "RoCE",
        "RDMASupport": "Available",
        "RXFlowControl": "Available",
        "RemotePHY": "Unavailable",
        "SNAPI": "Unavailable",
        "SNAPIState": "Disabled",
        "SRIOVSupport": "Available",
        "TOESupport": "Unavailable",
        "TXBandwidthControlMaximum": "Available",
        "TXBandwidthControlMinimum": "Available",
        "TXFlowControl": "Available",
        "TcpIpViaDHCP": "Disabled",
        "VFAllocBasis": "Device",
        "VFAllocMult": 1,
        "VFDistribution": "8",
        "VLanId": 1,
        "VLanMode": "Disabled",
        "VPI": "Unavailable",
        "VirtMacAddr": "00:00:00:00:00:00",
        "VirtualizationMode": "NONE",
        "WakeOnLan": "Enabled",
        "WakeOnLanLnkSpeed": "1Gbps",
        "iSCSIBootSupport": "Available",
        "iSCSIDualIPVersionSupport": "Unavailable",
        "iSCSIOffloadSupport": "Unavailable"
    },
    "Description": "DellNetworkAttributes represents the Network device attribute details.",
    "Id": "NIC.Integrated.1-2-1",
    "Name": "DellNetworkAttributes"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-2-1/Settings

```{
    "@odata.context": "/redfish/v1/$metadata#DellAttributes.DellAttributes",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-2-1/Settings",
    "@odata.type": "#DellAttributes.v1_0_0.DellAttributes",
    "Actions": {
        "#DellManager.ClearPending": {
            "target": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1/Oem/Dell/DellNetworkAttributes/NIC.Integrated.1-2-1/Settings/Actions/DellManager.ClearPending"
        }
    },
    "AttributeRegistry": "NetworkAttributeRegistry",
    "Attributes": {},
    "Description": "This schema provides settings of the oem attributes",
    "Id": "NIC.Integrated.1-2-1",
    "Name": "DellNetworkAttributes"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPortCollection.NetworkPortCollection",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts",
    "@odata.type": "#NetworkPortCollection.NetworkPortCollection",
    "Description": "Collection Of Network Port entities",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-2"
        }
    ],
    "Members@odata.count": 2,
    "Name": "Network Port Collection"
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-1

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPort.NetworkPort",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-1",
    "@odata.type": "#NetworkPort.v1_2_5.NetworkPort",
    "ActiveLinkTechnology": "Ethernet",
    "AssociatedNetworkAddresses": [
        "B8:CE:F6:94:F0:B8"
    ],
    "CurrentLinkSpeedMbps": 10000,
    "Description": "Network Port View",
    "EEEEnabled": null,
    "FlowControlConfiguration": "None",
    "FlowControlStatus": "None",
    "Id": "NIC.Integrated.1-1",
    "LinkStatus": "Up",
    "Name": "Network Port View",
    "NetDevFuncMaxBWAlloc": [
        {
            "MaxBWAllocPercent": null,
            "NetworkDeviceFunction": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1"
            }
        }
    ],
    "NetDevFuncMaxBWAlloc@odata.count": 1,
    "NetDevFuncMinBWAlloc": [
        {
            "MinBWAllocPercent": null,
            "NetworkDeviceFunction": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-1-1"
            }
        }
    ],
    "NetDevFuncMinBWAlloc@odata.count": 1,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellNetworkTransceiver": {
                "@odata.context": "/redfish/v1/$metadata#DellNetworkTransceiver.DellNetworkTransceiver",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-1/Oem/Dell/DellNetworkTransceivers/NetworkTransceiver.Integrated.1:NIC.Integrated.1-1",
                "@odata.type": "#DellNetworkTransceiver.v1_0_0.DellNetworkTransceiver",
                "DeviceDescription": "Network Transceiver in Integrated NIC 1 Port 1",
                "FQDD": "NetworkTransceiver.Integrated.1:NIC.Integrated.1-1",
                "Id": "NetworkTransceiver.Integrated.1:NIC.Integrated.1-1",
                "IdentifierType": "SFP/SFP+/SFP28",
                "InterfaceType": "OpticalFiber",
                "Name": "DellNetworkTransceiver",
                "PartNumber": "FTLX8571D3BCL-C2",
                "Revision": "A",
                "SerialNumber": "FNS1651019S",
                "VendorName": "CISCO-FINISAR"
            }
        }
    },
    "PhysicalPortNumber": "1",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SupportedEthernetCapabilities": [
        "WakeOnLAN"
    ],
    "SupportedEthernetCapabilities@odata.count": 1,
    "SupportedLinkCapabilities": [
        {
            "AutoSpeedNegotiation": true,
            "LinkNetworkTechnology": "Ethernet",
            "LinkSpeedMbps": 10000
        }
    ],
    "SupportedLinkCapabilities@odata.count": 1,
    "VendorId": "15b3",
    "WakeOnLANEnabled": true
}
```

## /redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-2

```{
    "@odata.context": "/redfish/v1/$metadata#NetworkPort.NetworkPort",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-2",
    "@odata.type": "#NetworkPort.v1_2_5.NetworkPort",
    "ActiveLinkTechnology": "Ethernet",
    "AssociatedNetworkAddresses": [
        "B8:CE:F6:94:F0:B9"
    ],
    "CurrentLinkSpeedMbps": 10000,
    "Description": "Network Port View",
    "EEEEnabled": null,
    "FlowControlConfiguration": "None",
    "FlowControlStatus": "None",
    "Id": "NIC.Integrated.1-2",
    "LinkStatus": "Up",
    "Name": "Network Port View",
    "NetDevFuncMaxBWAlloc": [
        {
            "MaxBWAllocPercent": null,
            "NetworkDeviceFunction": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1"
            }
        }
    ],
    "NetDevFuncMaxBWAlloc@odata.count": 1,
    "NetDevFuncMinBWAlloc": [
        {
            "MinBWAllocPercent": null,
            "NetworkDeviceFunction": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkDeviceFunctions/NIC.Integrated.1-2-1"
            }
        }
    ],
    "NetDevFuncMinBWAlloc@odata.count": 1,
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOem.v1_2_0.DellOemResources",
            "DellNetworkTransceiver": {
                "@odata.context": "/redfish/v1/$metadata#DellNetworkTransceiver.DellNetworkTransceiver",
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/NetworkAdapters/NIC.Integrated.1/NetworkPorts/NIC.Integrated.1-2/Oem/Dell/DellNetworkTransceivers/NetworkTransceiver.Integrated.1:NIC.Integrated.1-2",
                "@odata.type": "#DellNetworkTransceiver.v1_0_0.DellNetworkTransceiver",
                "DeviceDescription": "Network Transceiver in Integrated NIC 1 Port 2",
                "FQDD": "NetworkTransceiver.Integrated.1:NIC.Integrated.1-2",
                "Id": "NetworkTransceiver.Integrated.1:NIC.Integrated.1-2",
                "IdentifierType": "SFP/SFP+/SFP28",
                "InterfaceType": "OpticalFiber",
                "Name": "DellNetworkTransceiver",
                "PartNumber": "FTLX8571D3BCL-C2",
                "Revision": "A",
                "SerialNumber": "FNS18270TMW",
                "VendorName": "CISCO-FINISAR"
            }
        }
    },
    "PhysicalPortNumber": "2",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "SupportedEthernetCapabilities": [
        "WakeOnLAN"
    ],
    "SupportedEthernetCapabilities@odata.count": 1,
    "SupportedLinkCapabilities": [
        {
            "AutoSpeedNegotiation": true,
            "LinkNetworkTechnology": "Ethernet",
            "LinkSpeedMbps": 10000
        }
    ],
    "SupportedLinkCapabilities@odata.count": 1,
    "VendorId": "15b3",
    "WakeOnLANEnabled": true
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/AHCI.SL.6-1_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/AHCI.SL.6-1_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "AHCI.SL.6-1",
    "Id": "AHCI.SL.6-1_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Module/Card",
    "SerialNumber": "CNIVC0015I0958"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A1_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A1_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.A1",
    "Id": "DIMM.Socket.A1_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "19949A6B"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A2_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A2_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.A2",
    "Id": "DIMM.Socket.A2_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "19949A55"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A3_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A3_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.A3",
    "Id": "DIMM.Socket.A3_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "19949A27"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A4_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A4_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.A4",
    "Id": "DIMM.Socket.A4_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "19949A29"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A5_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A5_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.A5",
    "Id": "DIMM.Socket.A5_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "19949A26"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A6_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A6_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.A6",
    "Id": "DIMM.Socket.A6_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "19949A56"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A7_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A7_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.A7",
    "Id": "DIMM.Socket.A7_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "19949A67"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A8_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.A8_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.A8",
    "Id": "DIMM.Socket.A8_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "19949A1F"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B1_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B1_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.B1",
    "Id": "DIMM.Socket.B1_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "19949A25"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B2_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B2_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.B2",
    "Id": "DIMM.Socket.B2_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "19949A23"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B3_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B3_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.B3",
    "Id": "DIMM.Socket.B3_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "1994CC0F"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B4_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B4_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.B4",
    "Id": "DIMM.Socket.B4_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "19949A66"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B5_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B5_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.B5",
    "Id": "DIMM.Socket.B5_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "19949A52"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B6_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B6_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.B6",
    "Id": "DIMM.Socket.B6_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "1994CC0E"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B7_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B7_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.B7",
    "Id": "DIMM.Socket.B7_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "1994BEBD"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B8_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/DIMM.Socket.B8_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "DIMM.Socket.B8",
    "Id": "DIMM.Socket.B8_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Memory",
    "SerialNumber": "19949A8A"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/Enclosure.Internal.0-1_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/Enclosure.Internal.0-1_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "Enclosure.Internal.0-1",
    "Id": "Enclosure.Internal.0-1_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "CrossConnect/Backplane",
    "SerialNumber": "CNIVC0013U0560"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/FC.Slot.1_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/FC.Slot.1_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "FC.Slot.1",
    "Id": "FC.Slot.1_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Module/Card",
    "SerialNumber": "MYFLPB38BTM033"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/NIC.Integrated.1_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/NIC.Integrated.1_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "NIC.Integrated.1",
    "Id": "NIC.Integrated.1_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Module/Card",
    "SerialNumber": "INJBNM414TJ0AL"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/RAID.SL.3-1_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/RAID.SL.3-1_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "RAID.SL.3-1",
    "Id": "RAID.SL.3-1_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Module/Card",
    "SerialNumber": "CNIVC0013I0887"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/System.Embedded.1_0x23_FRU

```{
    "@odata.context": "/redfish/v1/$metadata#DellAssembly.DellAssembly",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellAssembly/System.Embedded.1_0x23_FRU",
    "@odata.type": "#DellAssembly.v1_0_0.DellAssembly",
    "Description": "This resource shall be used to represent an assembly information.",
    "DeviceFQDD": "System.Embedded.1",
    "Id": "System.Embedded.1_0x23_FRU",
    "Name": "DellAssembly",
    "PackageType": "Module/Card",
    "SerialNumber": "YGFCBTJSO8WOMR"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellChassis

```{
    "@odata.context": "/redfish/v1/$metadata#DellChassisCollection.DellChassisCollection",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellChassis",
    "@odata.type": "#DellChassisCollection.DellChassisCollection",
    "Description": "A collection of DellChassis resource",
    "Members": [
        {
            "@odata.context": "/redfish/v1/$metadata#DellChassis.DellChassis",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellChassis/mainsystemchassis",
            "@odata.type": "#DellChassis.v1_0_0.DellChassis",
            "CanBeFRUed": true,
            "Description": "This resource shall provide information about the enclosure or chassis the system is in.",
            "Id": "mainsystemchassis",
            "Links": {
                "ComputerSystem": {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            },
            "Name": "DellChassis",
            "SystemID": 2322
        }
    ],
    "Members@odata.count": 1,
    "Name": "DellChassisCollection"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellChassis/mainsystemchassis

```{
    "@odata.context": "/redfish/v1/$metadata#DellChassis.DellChassis",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Oem/Dell/DellChassis/mainsystemchassis",
    "@odata.type": "#DellChassis.v1_0_0.DellChassis",
    "CanBeFRUed": true,
    "Description": "This resource shall provide information about the enclosure or chassis the system is in.",
    "Id": "mainsystemchassis",
    "Links": {
        "ComputerSystem": {
            "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
        }
    },
    "Name": "DellChassis",
    "SystemID": 2322
}
```

## /redfish/v1/Chassis/System.Embedded.1/PCIeSlots

```{
    "@odata.context": "/redfish/v1/$metadata#PCIeSlots.PCIeSlots",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/PCIeSlots",
    "@odata.type": "#PCIeSlots.v1_3_0.PCIeSlots",
    "Description": "This Resource shall represent a set of PCIe slot information.",
    "Id": "PCIeSlots",
    "Name": "PCIeSlots",
    "Slots": [
        {
            "HotPluggable": false,
            "Lanes": 16,
            "Links": {
                "Oem": {
                    "Dell": {
                        "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                        "CPUAffinity": [
                            {
                                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                            }
                        ],
                        "CPUAffinity@odata.count": 1
                    }
                },
                "PCIeDevice": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/23-0"
                    }
                ],
                "PCIeDevice@odata.count": 1
            },
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 1,
                    "LocationType": "Slot"
                }
            },
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellPCIeSlots.v1_0_0.DellPCIeSlots",
                    "SlotKey": "PCIe.Slot.1"
                }
            },
            "PCIeType": "Gen4",
            "SlotType": "FullLength",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "HotPluggable": true,
            "Lanes": 4,
            "Links": {
                "Oem": {
                    "Dell": {
                        "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                        "CPUAffinity": [
                            {
                                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                            }
                        ],
                        "CPUAffinity@odata.count": 1
                    }
                },
                "PCIeDevice": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/102-0"
                    }
                ],
                "PCIeDevice@odata.count": 1
            },
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 8,
                    "LocationType": "Slot"
                }
            },
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellPCIeSlots.v1_0_0.DellPCIeSlots",
                    "SlotKey": "PCIeSSD.BaySlot.8:1"
                }
            },
            "PCIeType": null,
            "SlotType": "U2",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "HotPluggable": true,
            "Lanes": 4,
            "Links": {
                "Oem": {
                    "Dell": {
                        "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                        "CPUAffinity": [
                            {
                                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                            }
                        ],
                        "CPUAffinity@odata.count": 1
                    }
                },
                "PCIeDevice": [
                    {
                        "@odata.id": "/redfish/v1/Systems/System.Embedded.1/PCIeDevices/101-0"
                    }
                ],
                "PCIeDevice@odata.count": 1
            },
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 9,
                    "LocationType": "Slot"
                }
            },
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellPCIeSlots.v1_0_0.DellPCIeSlots",
                    "SlotKey": "PCIeSSD.BaySlot.9:1"
                }
            },
            "PCIeType": null,
            "SlotType": "U2",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "HotPluggable": false,
            "Lanes": 16,
            "Links": {
                "Oem": {
                    "Dell": {
                        "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                        "CPUAffinity": [
                            {
                                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                            }
                        ],
                        "CPUAffinity@odata.count": 1
                    }
                },
                "PCIeDevice": [],
                "PCIeDevice@odata.count": 0
            },
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 2,
                    "LocationType": "Slot"
                }
            },
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellPCIeSlots.v1_0_0.DellPCIeSlots",
                    "SlotKey": "PCIe.Slot.2"
                }
            },
            "PCIeType": "Gen4",
            "SlotType": "FullLength",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "HotPluggable": true,
            "Lanes": 4,
            "Links": {
                "Oem": {
                    "Dell": {
                        "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                        "CPUAffinity": [],
                        "CPUAffinity@odata.count": 0
                    }
                },
                "PCIeDevice": [],
                "PCIeDevice@odata.count": 0
            },
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 7,
                    "LocationType": "Slot"
                }
            },
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellPCIeSlots.v1_0_0.DellPCIeSlots",
                    "SlotKey": "PCIeSSD.BaySlot.7:1"
                }
            },
            "PCIeType": null,
            "SlotType": "U2",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "HotPluggable": true,
            "Lanes": 4,
            "Links": {
                "Oem": {
                    "Dell": {
                        "@odata.type": "#DellOem.v1_2_0.DellOemLinks",
                        "CPUAffinity": [],
                        "CPUAffinity@odata.count": 0
                    }
                },
                "PCIeDevice": [],
                "PCIeDevice@odata.count": 0
            },
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 6,
                    "LocationType": "Slot"
                }
            },
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellPCIeSlots.v1_0_0.DellPCIeSlots",
                    "SlotKey": "PCIeSSD.BaySlot.6:1"
                }
            },
            "PCIeType": null,
            "SlotType": "U2",
            "Status": {
                "State": "Enabled"
            }
        }
    ],
    "Slots@odata.count": 6
}
```

## /redfish/v1/Chassis/System.Embedded.1/Power

```{
    "@odata.context": "/redfish/v1/$metadata#Power.Power",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power",
    "@odata.type": "#Power.v1_6_1.Power",
    "Description": "Power",
    "Id": "Power",
    "Name": "Power",
    "PowerControl": [
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerControl/0",
            "@odata.type": "#Power.v1_6_1.PowerControl",
            "MemberId": "0",
            "Name": "System Power Control",
            "PowerAllocatedWatts": 1512,
            "PowerAvailableWatts": 0,
            "PowerCapacityWatts": 1512,
            "PowerConsumedWatts": 396,
            "PowerLimit": {
                "CorrectionInMs": 0,
                "LimitException": "HardPowerOff",
                "LimitInWatts": 278
            },
            "PowerMetrics": {
                "AverageConsumedWatts": 395,
                "IntervalInMin": 1,
                "MaxConsumedWatts": 399,
                "MinConsumedWatts": 393
            },
            "PowerRequestedWatts": 836,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                },
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1"
                }
            ]
        }
    ],
    "PowerControl@odata.count": 1,
    "PowerSupplies": [
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerSupplies/0",
            "@odata.type": "#Power.v1_6_1.PowerSupply",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power/PowerSupplies/PSU.Slot.1/Assembly"
            },
            "EfficiencyPercent": 92.0000016689301,
            "FirmwareVersion": "00.17.28",
            "HotPluggable": true,
            "InputRanges": [
                {
                    "InputType": "AC",
                    "MaximumFrequencyHz": 35,
                    "MaximumVoltage": 14,
                    "MinimumFrequencyHz": 40,
                    "MinimumVoltage": 132,
                    "OutputWattage": 1400
                }
            ],
            "LastPowerOutputWatts": null,
            "LineInputVoltage": 208,
            "LineInputVoltageType": "AC240V",
            "Manufacturer": "DELL",
            "MemberId": "0",
            "Model": "PWR SPLY,1400W,RDNT,LTON",
            "Name": "PS1 Status",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellPowerSupply": {
                        "@odata.context": "/redfish/v1/$metadata#DellPowerSupply.DellPowerSupply",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupply/PSU.Slot.1",
                        "@odata.type": "#DellPowerSupply.v1_1_0.DellPowerSupply",
                        "ActiveInputVoltage": "Unknown",
                        "Id": "PSU.Slot.1",
                        "IsSwitchingSupply": true,
                        "Links": {
                            "DellPSNumericSensorCollection": [
                                {
                                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors/iDRAC.Embedded.1_0x23_PS1Current1"
                                }
                            ],
                            "DellPSNumericSensorCollection@odata.count": 1
                        },
                        "Name": "DellPowerSupply",
                        "OperationalStatus": [
                            "OK"
                        ],
                        "OperationalStatus@odata.count": 1,
                        "RequestedState": "NotApplicable"
                    },
                    "DellPowerSupplyView": {
                        "@odata.context": "/redfish/v1/$metadata#DellPowerSupplyView.DellPowerSupplyView",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupplyInventory/PSU.Slot.1",
                        "@odata.type": "#DellPowerSupplyView.v1_3_0.DellPowerSupplyView",
                        "DetailedState": "Presence Detected",
                        "DeviceDescription": "Power Supply 1",
                        "Id": "PSU.Slot.1",
                        "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                        "LastUpdateTime": "2022-10-26T20:52:37+00:00",
                        "Name": "DellPowerSupplyView",
                        "PMBusMonitoring": "Capable",
                        "Range1MaxInputPowerWatts": 1568,
                        "RedMinNumberNeeded": 1,
                        "RedTypeOfSet": [
                            "N+1",
                            "InputPowerRedundancy",
                            "Sparing"
                        ],
                        "RedTypeOfSet@odata.count": 3,
                        "RedundancyStatus": "FullyRedundant"
                    }
                }
            },
            "PartNumber": "01CW9GA03",
            "PowerCapacityWatts": 1400,
            "PowerInputWatts": 393.0,
            "PowerOutputWatts": 363.0,
            "PowerSupplyType": "AC",
            "Redundancy": [
                {
                    "@odata.context": "/redfish/v1/$metadata#Redundancy.Redundancy",
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Redundancy/0",
                    "@odata.type": "#Redundancy.v1_3_5.Redundancy",
                    "MaxNumSupported": 4,
                    "MemberId": "0",
                    "MinNumNeeded": 2,
                    "Mode": "N+m",
                    "Name": "System Board PS Redundancy",
                    "RedundancySet": [
                        {
                            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerSupplies/0"
                        },
                        {
                            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerSupplies/1"
                        }
                    ],
                    "RedundancySet@odata.count": 2,
                    "Status": {
                        "Health": "OK",
                        "State": "Enabled"
                    }
                }
            ],
            "Redundancy@odata.count": 1,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SerialNumber": "CNLOD001262D5D",
            "SparePartNumber": "01CW9GA03",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerSupplies/1",
            "@odata.type": "#Power.v1_6_1.PowerSupply",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power/PowerSupplies/PSU.Slot.2/Assembly"
            },
            "EfficiencyPercent": 92.0000016689301,
            "FirmwareVersion": "00.17.28",
            "HotPluggable": true,
            "InputRanges": [
                {
                    "InputType": "AC",
                    "MaximumFrequencyHz": 35,
                    "MaximumVoltage": 14,
                    "MinimumFrequencyHz": 40,
                    "MinimumVoltage": 132,
                    "OutputWattage": 1400
                }
            ],
            "LastPowerOutputWatts": null,
            "LineInputVoltage": 208,
            "LineInputVoltageType": "AC240V",
            "Manufacturer": "DELL",
            "MemberId": "1",
            "Model": "PWR SPLY,1400W,RDNT,LTON",
            "Name": "PS2 Status",
            "Oem": {
                "Dell": {
                    "@odata.type": "#DellOem.v1_2_0.DellOemResources",
                    "DellPowerSupply": {
                        "@odata.context": "/redfish/v1/$metadata#DellPowerSupply.DellPowerSupply",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupply/PSU.Slot.2",
                        "@odata.type": "#DellPowerSupply.v1_1_0.DellPowerSupply",
                        "ActiveInputVoltage": "Unknown",
                        "Id": "PSU.Slot.2",
                        "IsSwitchingSupply": true,
                        "Links": {
                            "DellPSNumericSensorCollection": [
                                {
                                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors/iDRAC.Embedded.1_0x23_PS2Current2"
                                }
                            ],
                            "DellPSNumericSensorCollection@odata.count": 1
                        },
                        "Name": "DellPowerSupply",
                        "OperationalStatus": [
                            "OK"
                        ],
                        "OperationalStatus@odata.count": 1,
                        "RequestedState": "NotApplicable"
                    },
                    "DellPowerSupplyView": {
                        "@odata.context": "/redfish/v1/$metadata#DellPowerSupplyView.DellPowerSupplyView",
                        "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupplyInventory/PSU.Slot.2",
                        "@odata.type": "#DellPowerSupplyView.v1_3_0.DellPowerSupplyView",
                        "DetailedState": "Presence Detected",
                        "DeviceDescription": "Power Supply 2",
                        "Id": "PSU.Slot.2",
                        "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
                        "LastUpdateTime": "2022-10-26T20:52:37+00:00",
                        "Name": "DellPowerSupplyView",
                        "PMBusMonitoring": "Capable",
                        "Range1MaxInputPowerWatts": 1568,
                        "RedMinNumberNeeded": 1,
                        "RedTypeOfSet": [
                            "N+1",
                            "InputPowerRedundancy",
                            "Sparing"
                        ],
                        "RedTypeOfSet@odata.count": 3,
                        "RedundancyStatus": "FullyRedundant"
                    }
                }
            },
            "PartNumber": "01CW9GA03",
            "PowerCapacityWatts": 1400,
            "PowerInputWatts": 5.0,
            "PowerOutputWatts": 0.0,
            "PowerSupplyType": "AC",
            "Redundancy": [
                {
                    "@odata.context": "/redfish/v1/$metadata#Redundancy.Redundancy",
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Redundancy/0",
                    "@odata.type": "#Redundancy.v1_3_5.Redundancy",
                    "MaxNumSupported": 4,
                    "MemberId": "0",
                    "MinNumNeeded": 2,
                    "Mode": "N+m",
                    "Name": "System Board PS Redundancy",
                    "RedundancySet": [
                        {
                            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerSupplies/0"
                        },
                        {
                            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerSupplies/1"
                        }
                    ],
                    "RedundancySet@odata.count": 2,
                    "Status": {
                        "Health": "OK",
                        "State": "Enabled"
                    }
                }
            ],
            "Redundancy@odata.count": 1,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SerialNumber": "CNLOD001262DF2",
            "SparePartNumber": "01CW9GA03",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ],
    "PowerSupplies@odata.count": 2,
    "Redundancy": [
        {
            "@odata.context": "/redfish/v1/$metadata#Redundancy.Redundancy",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Redundancy/0",
            "@odata.type": "#Redundancy.v1_3_5.Redundancy",
            "MaxNumSupported": 4,
            "MemberId": "0",
            "MinNumNeeded": 2,
            "Mode": "N+m",
            "Name": "System Board PS Redundancy",
            "RedundancySet": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerSupplies/0"
                },
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerSupplies/1"
                }
            ],
            "RedundancySet@odata.count": 2,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ],
    "Redundancy@odata.count": 1,
    "Voltages": [
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/0",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "0",
            "Name": "PS1 Voltage 1",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 208.0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerSupplies/0"
                }
            ],
            "SensorNumber": 109,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/1",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "1",
            "Name": "PS2 Voltage 2",
            "PhysicalContext": "PowerSupply",
            "ReadingVolts": 208.0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/PowerSupplies/1"
                }
            ],
            "SensorNumber": 110,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/2",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "2",
            "Name": "System Board Pfault Fail Safe",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 116,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/3",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "3",
            "Name": "System Board DIMM VSHORT",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 7,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/4",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "4",
            "Name": "System Board PS1 PG FAIL",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 8,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/5",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "5",
            "Name": "System Board PS2 PG FAIL",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 9,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/6",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "6",
            "Name": "CPU1 MEMABCD VDD PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 10,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/7",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "7",
            "Name": "CPU1 MEMABCD VPP PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 11,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/8",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "8",
            "Name": "CPU1 MEMABCD VTT PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 12,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/9",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "9",
            "Name": "CPU1 MEMEFGH VDD PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 13,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/10",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "10",
            "Name": "CPU1 MEMEFGH VPP PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 14,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/11",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "11",
            "Name": "CPU1 MEMEFGH VTT PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 15,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/12",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "12",
            "Name": "CPU1 1P8 PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 16,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/13",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "13",
            "Name": "CPU1 ANA PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 17,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/14",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "14",
            "Name": "CPU1 VCCIN PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 18,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/15",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "15",
            "Name": "CPU1 VCCIO PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 19,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/16",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "16",
            "Name": "CPU1 VSA PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 20,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/17",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "17",
            "Name": "CPU1 FIVR PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 21,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/18",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "18",
            "Name": "CPU2 MEMABCD VDD PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 22,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/19",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "19",
            "Name": "CPU2 MEMABCD VPP PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 23,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/20",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "20",
            "Name": "CPU2 MEMABCD VTT PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 24,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/21",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "21",
            "Name": "CPU2 MEMEFGH VDD PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 25,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/22",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "22",
            "Name": "CPU2 MEMEFGH VPP PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 26,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/23",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "23",
            "Name": "CPU2 MEMEFGH VTT PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 27,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/24",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "24",
            "Name": "CPU2 1P8 PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 28,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/25",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "25",
            "Name": "CPU2 ANA PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 29,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/26",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "26",
            "Name": "CPU2 VCCIN PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 30,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/27",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "27",
            "Name": "CPU2 VCCIO PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 31,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/28",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "28",
            "Name": "CPU2 VSA PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 32,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/29",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "29",
            "Name": "CPU2 FIVR PG",
            "PhysicalContext": "CPU",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 33,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/30",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "30",
            "Name": "System Board BP0 PG",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 34,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/31",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "31",
            "Name": "System Board BP1 PG",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 35,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/32",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "32",
            "Name": "System Board BP3 PG",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 36,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/33",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "33",
            "Name": "System Board BP4 PG",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 37,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/34",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "34",
            "Name": "System Board 1V05 SW PG",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 38,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/35",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "35",
            "Name": "System Board 3.3V A PG",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 39,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/36",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "36",
            "Name": "System Board 5V SW PG",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 40,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/37",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "37",
            "Name": "System Board BMC SW PG",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 41,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/38",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "38",
            "Name": "System Board OCP1 PG",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 42,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/39",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "39",
            "Name": "System Board OCP1 HP SW PG",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 43,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/40",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "40",
            "Name": "System Board BATT PG",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 44,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/41",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "41",
            "Name": "System Board PVNN SW PG",
            "PhysicalContext": "SystemBoard",
            "ReadingVolts": null,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "SensorNumber": 45,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/42",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "42",
            "Name": "CPU1 VCORE VR",
            "PhysicalContext": "CPU",
            "ReadingVolts": 1.79,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 50,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/43",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "43",
            "Name": "CPU2 VCORE VR",
            "PhysicalContext": "CPU",
            "ReadingVolts": 1.79,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 51,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/44",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "44",
            "Name": "CPU1 MEM0123 VR",
            "PhysicalContext": "CPU",
            "ReadingVolts": 1.22,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 52,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/45",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "45",
            "Name": "CPU1 MEM4567 VR",
            "PhysicalContext": "CPU",
            "ReadingVolts": 1.22,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "SensorNumber": 53,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/46",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "46",
            "Name": "CPU2 MEM0123 VR",
            "PhysicalContext": "CPU",
            "ReadingVolts": 1.22,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 54,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Power.Power",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power#/Voltages/47",
            "@odata.type": "#Power.v1_6_1.Voltage",
            "LowerThresholdCritical": null,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MemberId": "47",
            "Name": "CPU2 MEM4567 VR",
            "PhysicalContext": "CPU",
            "ReadingVolts": 1.22,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "SensorNumber": 55,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        }
    ],
    "Voltages@odata.count": 48
}
```

## /redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupply/PSU.Slot.1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPowerSupply.DellPowerSupply",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupply/PSU.Slot.1",
    "@odata.type": "#DellPowerSupply.v1_1_0.DellPowerSupply",
    "ActiveInputVoltage": "Unknown",
    "Description": "An instance of DellPowerSupply will have data specific to the Power Supply devices in the managed system.",
    "Id": "PSU.Slot.1",
    "IsSwitchingSupply": true,
    "Links": {
        "DellPSNumericSensorCollection": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors/iDRAC.Embedded.1_0x23_PS1Current1"
            }
        ],
        "DellPSNumericSensorCollection@odata.count": 1
    },
    "Name": "DellPowerSupply",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "RequestedState": "NotApplicable"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupply/PSU.Slot.2

```{
    "@odata.context": "/redfish/v1/$metadata#DellPowerSupply.DellPowerSupply",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupply/PSU.Slot.2",
    "@odata.type": "#DellPowerSupply.v1_1_0.DellPowerSupply",
    "ActiveInputVoltage": "Unknown",
    "Description": "An instance of DellPowerSupply will have data specific to the Power Supply devices in the managed system.",
    "Id": "PSU.Slot.2",
    "IsSwitchingSupply": true,
    "Links": {
        "DellPSNumericSensorCollection": [
            {
                "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Oem/Dell/DellPSNumericSensors/iDRAC.Embedded.1_0x23_PS2Current2"
            }
        ],
        "DellPSNumericSensorCollection@odata.count": 1
    },
    "Name": "DellPowerSupply",
    "OperationalStatus": [
        "OK"
    ],
    "OperationalStatus@odata.count": 1,
    "RequestedState": "NotApplicable"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupplyInventory/PSU.Slot.1

```{
    "@odata.context": "/redfish/v1/$metadata#DellPowerSupplyView.DellPowerSupplyView",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupplyInventory/PSU.Slot.1",
    "@odata.type": "#DellPowerSupplyView.v1_3_0.DellPowerSupplyView",
    "Description": "An instance of DellPowerSupplyView will have data specific to the Power Supply devices in the managed system.",
    "DetailedState": "Presence Detected",
    "DeviceDescription": "Power Supply 1",
    "Id": "PSU.Slot.1",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2022-10-26T20:52:37+00:00",
    "Name": "DellPowerSupplyView",
    "PMBusMonitoring": "Capable",
    "Range1MaxInputPowerWatts": 1568,
    "RedMinNumberNeeded": 1,
    "RedTypeOfSet": [
        "N+1",
        "InputPowerRedundancy",
        "Sparing"
    ],
    "RedTypeOfSet@odata.count": 3,
    "RedundancyStatus": "FullyRedundant"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupplyInventory/PSU.Slot.2

```{
    "@odata.context": "/redfish/v1/$metadata#DellPowerSupplyView.DellPowerSupplyView",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Power/Oem/Dell/DellPowerSupplyInventory/PSU.Slot.2",
    "@odata.type": "#DellPowerSupplyView.v1_3_0.DellPowerSupplyView",
    "Description": "An instance of DellPowerSupplyView will have data specific to the Power Supply devices in the managed system.",
    "DetailedState": "Presence Detected",
    "DeviceDescription": "Power Supply 2",
    "Id": "PSU.Slot.2",
    "LastSystemInventoryTime": "2022-08-30T22:00:48+00:00",
    "LastUpdateTime": "2022-10-26T20:52:37+00:00",
    "Name": "DellPowerSupplyView",
    "PMBusMonitoring": "Capable",
    "Range1MaxInputPowerWatts": 1568,
    "RedMinNumberNeeded": 1,
    "RedTypeOfSet": [
        "N+1",
        "InputPowerRedundancy",
        "Sparing"
    ],
    "RedTypeOfSet@odata.count": 3,
    "RedundancyStatus": "FullyRedundant"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Power/PowerSupplies/PSU.Slot.1/Assembly

```{
    "error": {
        "@Message.ExtendedInfo": [
            {
                "Message": "Unable to complete the operation because the resource /redfish/v1/Chassis/System.Embedded.1/Power/PowerSupplies/PSU.Slot.1/Assembly entered is not found.",
                "MessageArgs": [
                    "/redfish/v1/Chassis/System.Embedded.1/Power/PowerSupplies/PSU.Slot.1/Assembly"
                ],
                "MessageArgs@odata.count": 1,
                "MessageId": "IDRAC.2.5.SYS403",
                "RelatedProperties": [],
                "RelatedProperties@odata.count": 0,
                "Resolution": "Enter the correct resource and retry the operation. For information about valid resource, see the Redfish Users Guide available on the support site.",
                "Severity": "Critical"
            },
            {
                "Message": "The resource at the URI /redfish/v1/Chassis/System.Embedded.1/Power/PowerSupplies/PSU.Slot.1/Assembly was not found.",
                "MessageArgs": [
                    "/redfish/v1/Chassis/System.Embedded.1/Power/PowerSupplies/PSU.Slot.1/Assembly"
                ],
                "MessageArgs@odata.count": 1,
                "MessageId": "Base.1.8.ResourceMissingAtURI",
                "RelatedProperties": [],
                "RelatedProperties@odata.count": 0,
                "Resolution": "Place a valid resource at the URI or correct the URI and resubmit the request.",
                "Severity": "Critical"
            }
        ],
        "code": "Base.1.8.GeneralError",
        "message": "A general error has occurred. See ExtendedInfo for more information"
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Power/PowerSupplies/PSU.Slot.2/Assembly

```{
    "error": {
        "@Message.ExtendedInfo": [
            {
                "Message": "Unable to complete the operation because the resource /redfish/v1/Chassis/System.Embedded.1/Power/PowerSupplies/PSU.Slot.2/Assembly entered is not found.",
                "MessageArgs": [
                    "/redfish/v1/Chassis/System.Embedded.1/Power/PowerSupplies/PSU.Slot.2/Assembly"
                ],
                "MessageArgs@odata.count": 1,
                "MessageId": "IDRAC.2.5.SYS403",
                "RelatedProperties": [],
                "RelatedProperties@odata.count": 0,
                "Resolution": "Enter the correct resource and retry the operation. For information about valid resource, see the Redfish Users Guide available on the support site.",
                "Severity": "Critical"
            },
            {
                "Message": "The resource at the URI /redfish/v1/Chassis/System.Embedded.1/Power/PowerSupplies/PSU.Slot.2/Assembly was not found.",
                "MessageArgs": [
                    "/redfish/v1/Chassis/System.Embedded.1/Power/PowerSupplies/PSU.Slot.2/Assembly"
                ],
                "MessageArgs@odata.count": 1,
                "MessageId": "Base.1.8.ResourceMissingAtURI",
                "RelatedProperties": [],
                "RelatedProperties@odata.count": 0,
                "Resolution": "Place a valid resource at the URI or correct the URI and resubmit the request.",
                "Severity": "Critical"
            }
        ],
        "code": "Base.1.8.GeneralError",
        "message": "A general error has occurred. See ExtendedInfo for more information"
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors

```{
    "@odata.context": "/redfish/v1/$metadata#SensorCollection.SensorCollection",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors",
    "@odata.type": "#SensorCollection.SensorCollection",
    "Description": "Collection of Sensors",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/PS1Current1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/PS2Current2"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/PS1Voltage"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/PS2Voltage"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/SystemBoardPwrConsumption"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1VCOREVR"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2VCOREVR"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1MEM0123VR"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1MEM4567VR"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2MEM0123VR"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2MEM4567VR"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1A"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2A"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3A"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4A"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1B"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2B"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3B"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4B"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1C"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2C"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3C"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4C"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1D"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2D"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3D"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4D"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1Temp"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2Temp"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/SystemBoardInletTemp"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/SystemBoardExhaustTemp"
        }
    ],
    "Members@odata.count": 31,
    "Name": "SensorCollection"
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1MEM0123VR

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1MEM0123VR",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "CPU1MEM0123VR",
    "Name": "CPU1 MEM0123 VR",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU1MEM0123VR",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "CPU",
    "Reading": 1.22,
    "ReadingType": "Voltage",
    "ReadingUnits": "V",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": null
        },
        "LowerCritical": {
            "Reading": null
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1MEM4567VR

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1MEM4567VR",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "CPU1MEM4567VR",
    "Name": "CPU1 MEM4567 VR",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU1MEM4567VR",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "CPU",
    "Reading": 1.22,
    "ReadingType": "Voltage",
    "ReadingUnits": "V",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": null
        },
        "LowerCritical": {
            "Reading": null
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1Temp

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1Temp",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "CPU1Temp",
    "Name": "CPU1 Temp",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU1Temp",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "CPU",
    "Reading": 57.0,
    "ReadingType": "Temperature",
    "ReadingUnits": "Cel",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": null
        },
        "LowerCritical": {
            "Reading": 3
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": 98
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1VCOREVR

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU1VCOREVR",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "CPU1VCOREVR",
    "Name": "CPU1 VCORE VR",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU1VCOREVR",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "CPU",
    "Reading": 1.79,
    "ReadingType": "Voltage",
    "ReadingUnits": "V",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": null
        },
        "LowerCritical": {
            "Reading": null
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2MEM0123VR

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2MEM0123VR",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "CPU2MEM0123VR",
    "Name": "CPU2 MEM0123 VR",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU2MEM0123VR",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "CPU",
    "Reading": 1.22,
    "ReadingType": "Voltage",
    "ReadingUnits": "V",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": null
        },
        "LowerCritical": {
            "Reading": null
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2MEM4567VR

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2MEM4567VR",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "CPU2MEM4567VR",
    "Name": "CPU2 MEM4567 VR",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU2MEM4567VR",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "CPU",
    "Reading": 1.22,
    "ReadingType": "Voltage",
    "ReadingUnits": "V",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": null
        },
        "LowerCritical": {
            "Reading": null
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2Temp

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2Temp",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "CPU2Temp",
    "Name": "CPU2 Temp",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU2Temp",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "CPU",
    "Reading": 54.0,
    "ReadingType": "Temperature",
    "ReadingUnits": "Cel",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": null
        },
        "LowerCritical": {
            "Reading": 3
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": 98
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2VCOREVR

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/CPU2VCOREVR",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "CPU2VCOREVR",
    "Name": "CPU2 VCORE VR",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#CPU2VCOREVR",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "CPU",
    "Reading": 1.79,
    "ReadingType": "Voltage",
    "ReadingUnits": "V",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": null
        },
        "LowerCritical": {
            "Reading": null
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1A

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1A",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.1A",
    "Name": "System Board Fan1A",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.1A",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 9000.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1B

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1B",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.1B",
    "Name": "System Board Fan1B",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.1B",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 5400.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1C

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1C",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.1C",
    "Name": "System Board Fan1C",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.1C",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 9240.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1D

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.1D",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.1D",
    "Name": "System Board Fan1D",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.1D",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 5400.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2A

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2A",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.2A",
    "Name": "System Board Fan2A",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.2A",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 9120.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2B

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2B",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.2B",
    "Name": "System Board Fan2B",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.2B",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 5520.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2C

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2C",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.2C",
    "Name": "System Board Fan2C",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.2C",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 9240.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2D

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.2D",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.2D",
    "Name": "System Board Fan2D",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.2D",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 5400.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3A

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3A",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.3A",
    "Name": "System Board Fan3A",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.3A",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 9240.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3B

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3B",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.3B",
    "Name": "System Board Fan3B",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.3B",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 5520.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3C

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3C",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.3C",
    "Name": "System Board Fan3C",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.3C",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 9120.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3D

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.3D",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.3D",
    "Name": "System Board Fan3D",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.3D",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 5400.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4A

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4A",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.4A",
    "Name": "System Board Fan4A",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.4A",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 9000.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4B

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4B",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.4B",
    "Name": "System Board Fan4B",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.4B",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 5400.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4C

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4C",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.4C",
    "Name": "System Board Fan4C",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.4C",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 9120.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4D

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/Fan.Embedded.4D",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "Fan.Embedded.4D",
    "Name": "System Board Fan4D",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "0x17||Fan.Embedded.4D",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 5400.0,
    "ReadingType": "Rotational",
    "ReadingUnits": "RPM",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 840
        },
        "LowerCritical": {
            "Reading": 480
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/PS1Current1

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/PS1Current1",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "PS1Current1",
    "Name": "PS1 Current 1",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#PS1Current1",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "PowerSupply",
    "Reading": 1.8,
    "ReadingType": "Current",
    "ReadingUnits": "A",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": null
        },
        "LowerCritical": {
            "Reading": null
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/PS1Voltage

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/PS1Voltage",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "PS1Voltage",
    "Name": "PS1 Voltage 1",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#PS1Voltage",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "PowerSupply",
    "Reading": 208.0,
    "ReadingType": "Voltage",
    "ReadingUnits": "V",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": null
        },
        "LowerCritical": {
            "Reading": null
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/PS2Current2

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/PS2Current2",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "PS2Current2",
    "Name": "PS2 Current 2",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#PS2Current2",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "PowerSupply",
    "Reading": 0.2,
    "ReadingType": "Current",
    "ReadingUnits": "A",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": null
        },
        "LowerCritical": {
            "Reading": null
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/PS2Voltage

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/PS2Voltage",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "PS2Voltage",
    "Name": "PS2 Voltage 2",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#PS2Voltage",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "PowerSupply",
    "Reading": 208.0,
    "ReadingType": "Voltage",
    "ReadingUnits": "V",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": null
        },
        "LowerCritical": {
            "Reading": null
        },
        "UpperCaution": {
            "Reading": null
        },
        "UpperCritical": {
            "Reading": null
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/SystemBoardExhaustTemp

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/SystemBoardExhaustTemp",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "SystemBoardExhaustTemp",
    "Name": "System Board Exhaust Temp",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#SystemBoardExhaustTemp",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 34.0,
    "ReadingType": "Temperature",
    "ReadingUnits": "Cel",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 8
        },
        "LowerCritical": {
            "Reading": 3
        },
        "UpperCaution": {
            "Reading": 75
        },
        "UpperCritical": {
            "Reading": 80
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/SystemBoardInletTemp

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/SystemBoardInletTemp",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "SystemBoardInletTemp",
    "Name": "System Board Inlet Temp",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#SystemBoardInletTemp",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 18.0,
    "ReadingType": "Temperature",
    "ReadingUnits": "Cel",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": 3
        },
        "LowerCritical": {
            "Reading": -7
        },
        "UpperCaution": {
            "Reading": 38
        },
        "UpperCritical": {
            "Reading": 42
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Sensors/SystemBoardPwrConsumption

```{
    "@odata.context": "/redfish/v1/$metadata#Sensor.Sensor",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Sensors/SystemBoardPwrConsumption",
    "@odata.type": "#Sensor.v1_1_1.Sensor",
    "Description": "Instance of Sensor Id",
    "Id": "SystemBoardPwrConsumption",
    "Name": "System Board Pwr Consumption",
    "Oem": {
        "Dell": {
            "@odata.type": "#DellOemSensor.v1_0_0.DellOemSensor",
            "CurrentState": "Normal",
            "DeviceID": "iDRAC.Embedded.1#SystemBoardPwrConsumption",
            "PossibleStates": [
                "Unknown",
                "Fatal",
                "Normal",
                "Upper Fatal",
                "Upper Critical",
                "Upper Non-Critical",
                "Lower Non-Critical",
                "Lower Critical",
                "Lower Fatal"
            ],
            "PossibleStates@odata.count": 9,
            "RequestedState": "NotApplicable"
        }
    },
    "PhysicalContext": "SystemBoard",
    "Reading": 384.0,
    "ReadingType": "Power",
    "ReadingUnits": "W",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thresholds": {
        "LowerCaution": {
            "Reading": null
        },
        "LowerCritical": {
            "Reading": null
        },
        "UpperCaution": {
            "Reading": 1512
        },
        "UpperCritical": {
            "Reading": 1656
        }
    }
}
```

## /redfish/v1/Chassis/System.Embedded.1/Thermal

```{
    "@odata.context": "/redfish/v1/$metadata#Thermal.Thermal",
    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal",
    "@odata.type": "#Thermal.v1_6_2.Thermal",
    "Description": "Represents the properties for Temperature and Cooling",
    "Fans": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/0",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan1A",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "0",
            "MinReadingRange": null,
            "Name": "System Board Fan1A",
            "PhysicalContext": "SystemBoard",
            "Reading": 9000,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 56,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/1",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan1B",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "1",
            "MinReadingRange": null,
            "Name": "System Board Fan1B",
            "PhysicalContext": "SystemBoard",
            "Reading": 5400,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 57,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/2",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan1C",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "2",
            "MinReadingRange": null,
            "Name": "System Board Fan1C",
            "PhysicalContext": "SystemBoard",
            "Reading": 9240,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 58,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/3",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan1D",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "3",
            "MinReadingRange": null,
            "Name": "System Board Fan1D",
            "PhysicalContext": "SystemBoard",
            "Reading": 5400,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 59,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/4",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan2A",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "4",
            "MinReadingRange": null,
            "Name": "System Board Fan2A",
            "PhysicalContext": "SystemBoard",
            "Reading": 9120,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 60,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/5",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan2B",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "5",
            "MinReadingRange": null,
            "Name": "System Board Fan2B",
            "PhysicalContext": "SystemBoard",
            "Reading": 5520,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 61,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/6",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan2C",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "6",
            "MinReadingRange": null,
            "Name": "System Board Fan2C",
            "PhysicalContext": "SystemBoard",
            "Reading": 9240,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 62,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/7",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan2D",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "7",
            "MinReadingRange": null,
            "Name": "System Board Fan2D",
            "PhysicalContext": "SystemBoard",
            "Reading": 5400,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 63,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/8",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan3A",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "8",
            "MinReadingRange": null,
            "Name": "System Board Fan3A",
            "PhysicalContext": "SystemBoard",
            "Reading": 9240,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 64,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/9",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan3B",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "9",
            "MinReadingRange": null,
            "Name": "System Board Fan3B",
            "PhysicalContext": "SystemBoard",
            "Reading": 5520,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 65,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/10",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan3C",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "10",
            "MinReadingRange": null,
            "Name": "System Board Fan3C",
            "PhysicalContext": "SystemBoard",
            "Reading": 9120,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 66,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/11",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan3D",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "11",
            "MinReadingRange": null,
            "Name": "System Board Fan3D",
            "PhysicalContext": "SystemBoard",
            "Reading": 5400,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 67,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/12",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan4A",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "12",
            "MinReadingRange": null,
            "Name": "System Board Fan4A",
            "PhysicalContext": "SystemBoard",
            "Reading": 9000,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 68,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/13",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan4B",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "13",
            "MinReadingRange": null,
            "Name": "System Board Fan4B",
            "PhysicalContext": "SystemBoard",
            "Reading": 5400,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 69,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/14",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan4C",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "14",
            "MinReadingRange": null,
            "Name": "System Board Fan4C",
            "PhysicalContext": "SystemBoard",
            "Reading": 9120,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 70,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Fans/15",
            "@odata.type": "#Thermal.v1_6_2.Fan",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Assembly"
            },
            "FanName": "System Board Fan4D",
            "HotPluggable": false,
            "LowerThresholdCritical": 480,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 840,
            "MaxReadingRange": null,
            "MemberId": "15",
            "MinReadingRange": null,
            "Name": "System Board Fan4D",
            "PhysicalContext": "SystemBoard",
            "Reading": 5400,
            "ReadingUnits": "RPM",
            "Redundancy": [],
            "Redundancy@odata.count": 0,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 71,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": null,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        }
    ],
    "Fans@odata.count": 16,
    "Id": "Thermal",
    "Name": "Thermal",
    "Redundancy": [
        {
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Redundancy/0",
            "@odata.type": "#Redundancy.v1_3_5.Redundancy",
            "MaxNumSupported": null,
            "MemberId": "0",
            "MinNumNeeded": null,
            "Mode": "N+m",
            "Name": "System Board Fan Redundancy",
            "RedundancyEnabled": true,
            "RedundancySet": [],
            "RedundancySet@odata.count": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ],
    "Redundancy@odata.count": 1,
    "Temperatures": [
        {
            "@odata.context": "/redfish/v1/$metadata#Thermal.Thermal",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Temperatures/0",
            "@odata.type": "#Thermal.v1_6_2.Temperature",
            "LowerThresholdCritical": 3,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MaxReadingRangeTemp": null,
            "MemberId": "0",
            "MinReadingRangeTemp": null,
            "Name": "CPU1 Temp",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 57,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 1,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 98,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Thermal.Thermal",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Temperatures/1",
            "@odata.type": "#Thermal.v1_6_2.Temperature",
            "LowerThresholdCritical": 3,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": null,
            "MaxReadingRangeTemp": null,
            "MemberId": "1",
            "MinReadingRangeTemp": null,
            "Name": "CPU2 Temp",
            "PhysicalContext": "CPU",
            "ReadingCelsius": 54,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/System.Embedded.1/Processors/CPU.Socket.2"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 2,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 98,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": null
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Thermal.Thermal",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Temperatures/2",
            "@odata.type": "#Thermal.v1_6_2.Temperature",
            "LowerThresholdCritical": -7,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 3,
            "MaxReadingRangeTemp": null,
            "MemberId": "2",
            "MinReadingRangeTemp": null,
            "Name": "System Board Inlet Temp",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 18,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 5,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 42,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": 38
        },
        {
            "@odata.context": "/redfish/v1/$metadata#Thermal.Thermal",
            "@odata.id": "/redfish/v1/Chassis/System.Embedded.1/Thermal#/Temperatures/3",
            "@odata.type": "#Thermal.v1_6_2.Temperature",
            "LowerThresholdCritical": 3,
            "LowerThresholdFatal": null,
            "LowerThresholdNonCritical": 8,
            "MaxReadingRangeTemp": null,
            "MemberId": "3",
            "MinReadingRangeTemp": null,
            "Name": "System Board Exhaust Temp",
            "PhysicalContext": "SystemBoard",
            "ReadingCelsius": 34,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/System.Embedded.1"
                }
            ],
            "RelatedItem@odata.count": 1,
            "SensorNumber": 6,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 80,
            "UpperThresholdFatal": null,
            "UpperThresholdNonCritical": 75
        }
    ],
    "Temperatures@odata.count": 4
}
```

