# Resource: /api-explorer/resources/redfish/v1/Chassis

Vendor | Model
--- | ---
Cisco | UCSX-9508

## /api-explorer/resources/redfish/v1/Chassis

```{
    "@odata.context": "/redfish/v1/$metadata#ChassisCollection.ChassisCollection",
    "@odata.id": "/redfish/v1/Chassis",
    "@odata.type": "#ChassisCollection.ChassisCollection",
    "Description": "Collection of Chassis",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/PeerCMC"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FEM1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FEM2"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Blade1"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Blade2"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Blade3"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Blade4"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Blade5"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Blade6"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Blade7"
        },
        {
            "@odata.id": "/redfish/v1/Chassis/Blade8"
        }
    ],
    "Members@odata.count": 13,
    "Name": "Chassis Collection"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/1",
    "@odata.type": "#Chassis.v1_9_1.Chassis",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/1/Assembly"
    },
    "ChassisType": "Enclosure",
    "Id": "1",
    "IndicatorLED": "Off",
    "Manufacturer": "Cisco Systems Inc",
    "Model": "UCSX-9508",
    "Name": "Blade Server Chassis",
    "PartNumber": "68-6847-03  ",
    "Power": {
        "@odata.id": "/redfish/v1/Chassis/1/Power"
    },
    "SerialNumber": "FOX2521P34M",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/1/Thermal"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508",
            "PartNumber": "68-6847-03  ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FOX2521P34M",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Power

```{
    "@odata.context": "/redfish/v1/$metadata#Power.Power",
    "@odata.id": "/redfish/v1/Chassis/1/Power",
    "@odata.type": "#Power.v1_5_3.Power",
    "Description": "Chassis Power Information",
    "Id": "Power",
    "Name": "Power",
    "PowerControl": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/Chassis",
            "MemberId": "Chassis",
            "Name": "Chassis Power Control",
            "Oem": {
                "Cisco": {
                    "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                    "PowerExtendedEnabled": false,
                    "PowerGridMaxWatts": 3044,
                    "PowerN+1MaxWatts": 3044,
                    "PowerN+2MaxWatts": 3044,
                    "PowerNotRedundantMaxWatts": 6087,
                    "PowerProfileMaxWatts": 6641,
                    "PowerProfileMinWatts": 3632,
                    "PowerRebalanceEnabled": true,
                    "PowerSaveEnabled": false
                }
            },
            "PowerLimit": {
                "LimitInWatts": null
            },
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/Blade1",
            "MemberId": "Blade1",
            "Name": "Blade 1 Power Control",
            "Oem": {
                "Cisco": {
                    "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                    "InitialPowerLimit": {
                        "LimitInWatts": 1135
                    },
                    "PowerAllocationPriority": 3,
                    "PowerCharacteristics": {
                        "MaxPowerWatts": 1414,
                        "MinPowerWatts": 381,
                        "PowerProfileMaxWatts": 734,
                        "PowerProfileMinWatts": 448
                    },
                    "PowerMetrics": {
                        "AverageConsumedWatts": 259,
                        "CurrentConsumedWatts": 255,
                        "IntervalInMsec": 1000,
                        "MaxConsumedWatts": 288,
                        "MinConsumedWatts": 175
                    }
                }
            },
            "PowerLimit": {
                "LimitInWatts": 1135
            },
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/Blade2",
            "MemberId": "Blade2",
            "Name": "Blade 2 Power Control",
            "Oem": {
                "Cisco": {
                    "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                    "InitialPowerLimit": {
                        "LimitInWatts": 0
                    },
                    "PowerAllocationPriority": 3,
                    "PowerCharacteristics": {
                        "MaxPowerWatts": 0,
                        "MinPowerWatts": 0,
                        "PowerProfileMaxWatts": 0,
                        "PowerProfileMinWatts": 0
                    },
                    "PowerMetrics": {
                        "AverageConsumedWatts": 0,
                        "CurrentConsumedWatts": 0,
                        "IntervalInMsec": 1000,
                        "MaxConsumedWatts": 0,
                        "MinConsumedWatts": 0
                    }
                }
            },
            "PowerLimit": {
                "LimitInWatts": 0
            },
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/Blade3",
            "MemberId": "Blade3",
            "Name": "Blade 3 Power Control",
            "Oem": {
                "Cisco": {
                    "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                    "InitialPowerLimit": {
                        "LimitInWatts": 0
                    },
                    "PowerAllocationPriority": 3,
                    "PowerCharacteristics": {
                        "MaxPowerWatts": 0,
                        "MinPowerWatts": 0,
                        "PowerProfileMaxWatts": 0,
                        "PowerProfileMinWatts": 0
                    },
                    "PowerMetrics": {
                        "AverageConsumedWatts": 0,
                        "CurrentConsumedWatts": 0,
                        "IntervalInMsec": 1000,
                        "MaxConsumedWatts": 0,
                        "MinConsumedWatts": 0
                    }
                }
            },
            "PowerLimit": {
                "LimitInWatts": 0
            },
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/Blade4",
            "MemberId": "Blade4",
            "Name": "Blade 4 Power Control",
            "Oem": {
                "Cisco": {
                    "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                    "InitialPowerLimit": {
                        "LimitInWatts": 0
                    },
                    "PowerAllocationPriority": 3,
                    "PowerCharacteristics": {
                        "MaxPowerWatts": 0,
                        "MinPowerWatts": 0,
                        "PowerProfileMaxWatts": 0,
                        "PowerProfileMinWatts": 0
                    },
                    "PowerMetrics": {
                        "AverageConsumedWatts": 0,
                        "CurrentConsumedWatts": 0,
                        "IntervalInMsec": 1000,
                        "MaxConsumedWatts": 0,
                        "MinConsumedWatts": 0
                    }
                }
            },
            "PowerLimit": {
                "LimitInWatts": 0
            },
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/Blade5",
            "MemberId": "Blade5",
            "Name": "Blade 5 Power Control",
            "Oem": {
                "Cisco": {
                    "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                    "InitialPowerLimit": {
                        "LimitInWatts": 1119
                    },
                    "PowerAllocationPriority": 3,
                    "PowerCharacteristics": {
                        "MaxPowerWatts": 1414,
                        "MinPowerWatts": 381,
                        "PowerProfileMaxWatts": 670,
                        "PowerProfileMinWatts": 348
                    },
                    "PowerMetrics": {
                        "AverageConsumedWatts": 263,
                        "CurrentConsumedWatts": 260,
                        "IntervalInMsec": 1000,
                        "MaxConsumedWatts": 288,
                        "MinConsumedWatts": 13
                    }
                }
            },
            "PowerLimit": {
                "LimitInWatts": 1119
            },
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/Blade6",
            "MemberId": "Blade6",
            "Name": "Blade 6 Power Control",
            "Oem": {
                "Cisco": {
                    "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                    "InitialPowerLimit": {
                        "LimitInWatts": 0
                    },
                    "PowerAllocationPriority": 3,
                    "PowerCharacteristics": {
                        "MaxPowerWatts": 0,
                        "MinPowerWatts": 0,
                        "PowerProfileMaxWatts": 0,
                        "PowerProfileMinWatts": 0
                    },
                    "PowerMetrics": {
                        "AverageConsumedWatts": 0,
                        "CurrentConsumedWatts": 0,
                        "IntervalInMsec": 1000,
                        "MaxConsumedWatts": 0,
                        "MinConsumedWatts": 0
                    }
                }
            },
            "PowerLimit": {
                "LimitInWatts": 0
            },
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/Blade7",
            "MemberId": "Blade7",
            "Name": "Blade 7 Power Control",
            "Oem": {
                "Cisco": {
                    "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                    "InitialPowerLimit": {
                        "LimitInWatts": 1137
                    },
                    "PowerAllocationPriority": 3,
                    "PowerCharacteristics": {
                        "MaxPowerWatts": 1414,
                        "MinPowerWatts": 381,
                        "PowerProfileMaxWatts": 740,
                        "PowerProfileMinWatts": 435
                    },
                    "PowerMetrics": {
                        "AverageConsumedWatts": 143,
                        "CurrentConsumedWatts": 144,
                        "IntervalInMsec": 1000,
                        "MaxConsumedWatts": 171,
                        "MinConsumedWatts": 13
                    }
                }
            },
            "PowerLimit": {
                "LimitInWatts": 1137
            },
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/Blade8",
            "MemberId": "Blade8",
            "Name": "Blade 8 Power Control",
            "Oem": {
                "Cisco": {
                    "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                    "InitialPowerLimit": {
                        "LimitInWatts": 0
                    },
                    "PowerAllocationPriority": 3,
                    "PowerCharacteristics": {
                        "MaxPowerWatts": 0,
                        "MinPowerWatts": 0,
                        "PowerProfileMaxWatts": 0,
                        "PowerProfileMinWatts": 0
                    },
                    "PowerMetrics": {
                        "AverageConsumedWatts": 0,
                        "CurrentConsumedWatts": 0,
                        "IntervalInMsec": 1000,
                        "MaxConsumedWatts": 0,
                        "MinConsumedWatts": 0
                    }
                }
            },
            "PowerLimit": {
                "LimitInWatts": 0
            },
            "Status": {
                "Health": "OK",
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/ChassisOutput",
            "MemberId": "ChassisOutput",
            "Name": "CHS_OUTPUT_POWER",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/ChassisInput",
            "MemberId": "ChassisInput",
            "Name": "CHS_INPUT_POWER",
            "Status": {
                "State": "Absent"
            }
        }
    ],
    "PowerControl@odata.count": 11,
    "PowerSupplies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/1",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/1/Assembly"
            },
            "HotPluggable": true,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "1",
            "Model": "UCSX-PSU-2800AC",
            "Name": "Power Supply 1",
            "PartNumber": "341-0772-01 ",
            "SerialNumber": "ART2510F5AT",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/2",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/2/Assembly"
            },
            "HotPluggable": true,
            "MemberId": "2",
            "Name": "Power Supply 2",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/3",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/3/Assembly"
            },
            "HotPluggable": true,
            "MemberId": "3",
            "Name": "Power Supply 3",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/4",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/4/Assembly"
            },
            "HotPluggable": true,
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "4",
            "Model": "UCSX-PSU-2800AC",
            "Name": "Power Supply 4",
            "PartNumber": "341-0772-01 ",
            "SerialNumber": "ART2510F5AD",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/5",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/5/Assembly"
            },
            "HotPluggable": true,
            "MemberId": "5",
            "Name": "Power Supply 5",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/6",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/6/Assembly"
            },
            "HotPluggable": true,
            "MemberId": "6",
            "Name": "Power Supply 6",
            "Status": {
                "State": "Absent"
            }
        }
    ],
    "PowerSupplies@odata.count": 6,
    "Redundancy": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/Redundancy/PowerSupplies",
            "MaxNumSupported": 6,
            "MemberId": "PowerSupplies",
            "MinNumNeeded": 1,
            "Name": "Chassis Power Supply Redundancy",
            "Oem": {
                "Cisco": {
                    "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                    "RedundancyPolicy": "NotRedundant"
                }
            },
            "RedundancyEnabled": true,
            "RedundancySet": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/1"
                },
                {
                    "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/4"
                }
            ],
            "RedundancySet@odata.count": 2,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power#/Redundancy/SparePowerSupplies",
            "MaxNumSupported": null,
            "MemberId": "SparePowerSupplies",
            "MinNumNeeded": null,
            "Mode": "Sparing",
            "Name": "Chassis Power Supply Redundancy",
            "RedundancySet": [],
            "RedundancySet@odata.count": 0,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ]
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Power/PowerSupplies/1/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/1/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/1/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-PSU-2800AC",
            "PartNumber": "341-0772-01 ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "ART2510F5AT",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Power/PowerSupplies/2/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/2/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/2/Assembly#/Assemblies/0",
            "MemberId": "0"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Power/PowerSupplies/3/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/3/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/3/Assembly#/Assemblies/0",
            "MemberId": "0"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Power/PowerSupplies/4/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/4/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/4/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-PSU-2800AC",
            "PartNumber": "341-0772-01 ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "ART2510F5AD",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Power/PowerSupplies/5/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/5/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/5/Assembly#/Assemblies/0",
            "MemberId": "0"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Power/PowerSupplies/6/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/6/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Power/PowerSupplies/6/Assembly#/Assemblies/0",
            "MemberId": "0"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Thermal

```{
    "@odata.context": "/redfish/v1/$metadata#Thermal.Thermal",
    "@odata.id": "/redfish/v1/Chassis/1/Thermal",
    "@odata.type": "#Thermal.v1_5_2.Thermal",
    "Description": "Represents the properties for Temperature",
    "Fans": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/1",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/1/Assembly"
            },
            "HotPluggable": true,
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 1,
                    "LocationType": "Slot"
                }
            },
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "1",
            "Model": "UCSX-9508-FAN",
            "Name": "Fan Module 1 Fan 1",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517709V",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/2",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/2/Assembly"
            },
            "HotPluggable": true,
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 1,
                    "LocationType": "Slot"
                }
            },
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "2",
            "Model": "UCSX-9508-FAN",
            "Name": "Fan Module 1 Fan 2",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517709V",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/3",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/3/Assembly"
            },
            "HotPluggable": true,
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 2,
                    "LocationType": "Slot"
                }
            },
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "3",
            "Model": "UCSX-9508-FAN",
            "Name": "Fan Module 2 Fan 1",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517701J",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/4",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/4/Assembly"
            },
            "HotPluggable": true,
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 2,
                    "LocationType": "Slot"
                }
            },
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "4",
            "Model": "UCSX-9508-FAN",
            "Name": "Fan Module 2 Fan 2",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517701J",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/5",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/5/Assembly"
            },
            "HotPluggable": true,
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 3,
                    "LocationType": "Slot"
                }
            },
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "5",
            "Model": "UCSX-9508-FAN",
            "Name": "Fan Module 3 Fan 1",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517704C",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/6",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/6/Assembly"
            },
            "HotPluggable": true,
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 3,
                    "LocationType": "Slot"
                }
            },
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "6",
            "Model": "UCSX-9508-FAN",
            "Name": "Fan Module 3 Fan 2",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517704C",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/7",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/7/Assembly"
            },
            "HotPluggable": true,
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 4,
                    "LocationType": "Slot"
                }
            },
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "7",
            "Model": "UCSX-9508-FAN",
            "Name": "Fan Module 4 Fan 1",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517701L",
            "Status": {
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/8",
            "Assembly": {
                "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/8/Assembly"
            },
            "HotPluggable": true,
            "Location": {
                "PartLocation": {
                    "LocationOrdinalValue": 4,
                    "LocationType": "Slot"
                }
            },
            "Manufacturer": "Cisco Systems Inc",
            "MemberId": "8",
            "Model": "UCSX-9508-FAN",
            "Name": "Fan Module 4 Fan 2",
            "PartNumber": "73-19422-04 ",
            "SerialNumber": "FCH2517701L",
            "Status": {
                "State": "Enabled"
            }
        }
    ],
    "Fans@odata.count": 8,
    "Id": "Thermal",
    "Name": "Thermal",
    "Temperatures": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/1",
            "MemberId": "1",
            "Name": "ASIC_TEMP_A",
            "ReadingCelsius": 50,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/2",
            "MemberId": "2",
            "Name": "ASIC_TEMP_B",
            "ReadingCelsius": 50,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/3",
            "MemberId": "3",
            "Name": "ASIC_INLET_TEMP",
            "ReadingCelsius": 27,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/4",
            "MemberId": "4",
            "Name": "ASIC_OUTLET_TEMP",
            "ReadingCelsius": 42,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/5",
            "MemberId": "5",
            "Name": "P1_TEMP",
            "ReadingCelsius": 26,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/6",
            "MemberId": "6",
            "Name": "IFM_INLET_TEMP",
            "ReadingCelsius": 20,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/7",
            "MemberId": "7",
            "Name": "IFM_OUTLET_TEMP",
            "ReadingCelsius": 44,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/8",
            "MemberId": "8",
            "Name": "IFM_HOTSWAP_TEMP",
            "ReadingCelsius": 18,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/9",
            "MemberId": "9",
            "Name": "PWR_BRICK_TEMP1",
            "ReadingCelsius": 40,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/10",
            "MemberId": "10",
            "Name": "PWR_BRICK_TEMP2",
            "ReadingCelsius": 40,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/11",
            "MemberId": "11",
            "Name": "PEER_SLOT_FEM_INLET_TEMP",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/12",
            "MemberId": "12",
            "Name": "PEER_SLOT_FEM_HOTSWAP_TEMP",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/13",
            "MemberId": "13",
            "Name": "FEM1_INLET_TEMP",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/14",
            "MemberId": "14",
            "Name": "FEM2_INLET_TEMP",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/15",
            "MemberId": "15",
            "Name": "FEM1_HOTSWAP_TEMP",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/16",
            "MemberId": "16",
            "Name": "FEM2_HOTSWAP_TEMP",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/17",
            "MemberId": "17",
            "Name": "FAN1_HOTSWAP_TEMP",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/18",
            "MemberId": "18",
            "Name": "FAN2_HOTSWAP_TEMP",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/19",
            "MemberId": "19",
            "Name": "FAN3_HOTSWAP_TEMP",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/20",
            "MemberId": "20",
            "Name": "FAN4_HOTSWAP_TEMP",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/21",
            "MemberId": "21",
            "Name": "PS1_TEMP1",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/22",
            "MemberId": "22",
            "Name": "PS1_TEMP2",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/23",
            "MemberId": "23",
            "Name": "PS1_TEMP3",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/24",
            "MemberId": "24",
            "Name": "PS2_TEMP1",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/25",
            "MemberId": "25",
            "Name": "PS2_TEMP2",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/26",
            "MemberId": "26",
            "Name": "PS2_TEMP3",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/27",
            "MemberId": "27",
            "Name": "PS3_TEMP1",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/28",
            "MemberId": "28",
            "Name": "PS3_TEMP2",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/29",
            "MemberId": "29",
            "Name": "PS3_TEMP3",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/30",
            "MemberId": "30",
            "Name": "PS4_TEMP1",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/31",
            "MemberId": "31",
            "Name": "PS4_TEMP2",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/32",
            "MemberId": "32",
            "Name": "PS4_TEMP3",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/33",
            "MemberId": "33",
            "Name": "PS5_TEMP1",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/34",
            "MemberId": "34",
            "Name": "PS5_TEMP2",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/35",
            "MemberId": "35",
            "Name": "PS5_TEMP3",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/36",
            "MemberId": "36",
            "Name": "PS6_TEMP1",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/37",
            "MemberId": "37",
            "Name": "PS6_TEMP2",
            "Status": {
                "State": "Absent"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/38",
            "MemberId": "38",
            "Name": "PS6_TEMP3",
            "Status": {
                "State": "Absent"
            }
        }
    ],
    "Temperatures@odata.count": 38
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Thermal/Fans/1/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/1/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/1/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508-FAN",
            "PartNumber": "73-19422-04 ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FCH2517709V",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Thermal/Fans/2/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/2/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/2/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508-FAN",
            "PartNumber": "73-19422-04 ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FCH2517709V",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Thermal/Fans/3/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/3/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/3/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508-FAN",
            "PartNumber": "73-19422-04 ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FCH2517701J",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Thermal/Fans/4/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/4/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/4/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508-FAN",
            "PartNumber": "73-19422-04 ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FCH2517701J",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Thermal/Fans/5/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/5/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/5/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508-FAN",
            "PartNumber": "73-19422-04 ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FCH2517704C",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Thermal/Fans/6/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/6/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/6/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508-FAN",
            "PartNumber": "73-19422-04 ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FCH2517704C",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Thermal/Fans/7/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/7/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/7/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508-FAN",
            "PartNumber": "73-19422-04 ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FCH2517701L",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/1/Thermal/Fans/8/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/8/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Thermal/Fans/8/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508-FAN",
            "PartNumber": "73-19422-04 ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FCH2517701L",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/Blade1",
    "@odata.type": "#Chassis.v1_9_1.Chassis",
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade1/Actions/Chassis.Reset"
        }
    },
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/Blade1/Assembly"
    },
    "ChassisType": "Blade",
    "Id": "Blade1",
    "Location": {
        "PartLocation": {
            "LocationOrdinalValue": 1,
            "LocationType": "Slot"
        }
    },
    "ManagedBy": [
        "/redfish/v1/Managers/CIMC1"
    ],
    "ManagedBy@odata.count": 1,
    "ManagersInChassis": [
        "/redfish/v1/Managers/CIMC1"
    ],
    "ManagersInChassis@odata.count": 1,
    "Manufacturer": "Cisco Systems Inc",
    "Model": "UCSX-210C-M6",
    "Name": "Server Blade 1",
    "PowerSubsystem": {
        "@odata.id": "/redfish/v1/Chassis/Blade1/PowerSubsystem"
    },
    "SerialNumber": "FCH25337EHM",
    "Status": {
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/Blade1/Thermal"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade1/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/Blade1/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508",
            "PartNumber": "68-6847-03  ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FOX2521P34M",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade1/PowerSubsystem

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade1/Thermal

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade2

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/Blade2",
    "@odata.type": "#Chassis.v1_9_1.Chassis",
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade2/Actions/Chassis.Reset"
        }
    },
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/Blade2/Assembly"
    },
    "ChassisType": "Blade",
    "Id": "Blade2",
    "Location": {
        "PartLocation": {
            "LocationOrdinalValue": 2,
            "LocationType": "Slot"
        }
    },
    "Name": "Server Blade 2",
    "PowerSubsystem": {
        "@odata.id": "/redfish/v1/Chassis/Blade2/PowerSubsystem"
    },
    "Status": {
        "State": "Absent"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/Blade2/Thermal"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade2/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/Blade2/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508",
            "PartNumber": "68-6847-03  ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FOX2521P34M",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade2/PowerSubsystem

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade2/Thermal

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade3

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/Blade3",
    "@odata.type": "#Chassis.v1_9_1.Chassis",
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade3/Actions/Chassis.Reset"
        }
    },
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/Blade3/Assembly"
    },
    "ChassisType": "Blade",
    "Id": "Blade3",
    "Location": {
        "PartLocation": {
            "LocationOrdinalValue": 3,
            "LocationType": "Slot"
        }
    },
    "Name": "Server Blade 3",
    "PowerSubsystem": {
        "@odata.id": "/redfish/v1/Chassis/Blade3/PowerSubsystem"
    },
    "Status": {
        "State": "Absent"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/Blade3/Thermal"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade3/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/Blade3/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508",
            "PartNumber": "68-6847-03  ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FOX2521P34M",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade3/PowerSubsystem

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade3/Thermal

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade4

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/Blade4",
    "@odata.type": "#Chassis.v1_9_1.Chassis",
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade4/Actions/Chassis.Reset"
        }
    },
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/Blade4/Assembly"
    },
    "ChassisType": "Blade",
    "Id": "Blade4",
    "Location": {
        "PartLocation": {
            "LocationOrdinalValue": 4,
            "LocationType": "Slot"
        }
    },
    "Name": "Server Blade 4",
    "PowerSubsystem": {
        "@odata.id": "/redfish/v1/Chassis/Blade4/PowerSubsystem"
    },
    "Status": {
        "State": "Absent"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/Blade4/Thermal"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade4/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/Blade4/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508",
            "PartNumber": "68-6847-03  ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FOX2521P34M",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade4/PowerSubsystem

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade4/Thermal

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade5

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/Blade5",
    "@odata.type": "#Chassis.v1_9_1.Chassis",
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade5/Actions/Chassis.Reset"
        }
    },
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/Blade5/Assembly"
    },
    "ChassisType": "Blade",
    "Id": "Blade5",
    "Location": {
        "PartLocation": {
            "LocationOrdinalValue": 5,
            "LocationType": "Slot"
        }
    },
    "ManagedBy": [
        "/redfish/v1/Managers/CIMC5"
    ],
    "ManagedBy@odata.count": 1,
    "ManagersInChassis": [
        "/redfish/v1/Managers/CIMC5"
    ],
    "ManagersInChassis@odata.count": 1,
    "Manufacturer": "Cisco Systems Inc",
    "Model": "UCSX-210C-M6",
    "Name": "Server Blade 5",
    "PowerSubsystem": {
        "@odata.id": "/redfish/v1/Chassis/Blade5/PowerSubsystem"
    },
    "SerialNumber": "FCH25337EJ9",
    "Status": {
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/Blade5/Thermal"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade5/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/Blade5/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508",
            "PartNumber": "68-6847-03  ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FOX2521P34M",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade5/PowerSubsystem

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade5/Thermal

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade6

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/Blade6",
    "@odata.type": "#Chassis.v1_9_1.Chassis",
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade6/Actions/Chassis.Reset"
        }
    },
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/Blade6/Assembly"
    },
    "ChassisType": "Blade",
    "Id": "Blade6",
    "Location": {
        "PartLocation": {
            "LocationOrdinalValue": 6,
            "LocationType": "Slot"
        }
    },
    "Name": "Server Blade 6",
    "PowerSubsystem": {
        "@odata.id": "/redfish/v1/Chassis/Blade6/PowerSubsystem"
    },
    "Status": {
        "State": "Absent"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/Blade6/Thermal"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade6/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/Blade6/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508",
            "PartNumber": "68-6847-03  ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FOX2521P34M",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade6/PowerSubsystem

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade6/Thermal

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade7

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/Blade7",
    "@odata.type": "#Chassis.v1_9_1.Chassis",
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade7/Actions/Chassis.Reset"
        }
    },
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/Blade7/Assembly"
    },
    "ChassisType": "Blade",
    "Id": "Blade7",
    "Location": {
        "PartLocation": {
            "LocationOrdinalValue": 7,
            "LocationType": "Slot"
        }
    },
    "ManagedBy": [
        "/redfish/v1/Managers/CIMC7"
    ],
    "ManagedBy@odata.count": 1,
    "ManagersInChassis": [
        "/redfish/v1/Managers/CIMC7"
    ],
    "ManagersInChassis@odata.count": 1,
    "Manufacturer": "Cisco Systems Inc",
    "Model": "UCSX-210C-M6",
    "Name": "Server Blade 7",
    "PowerSubsystem": {
        "@odata.id": "/redfish/v1/Chassis/Blade7/PowerSubsystem"
    },
    "SerialNumber": "FCH25337EHW",
    "Status": {
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/Blade7/Thermal"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade7/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/Blade7/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508",
            "PartNumber": "68-6847-03  ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FOX2521P34M",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade7/PowerSubsystem

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade7/Thermal

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade8

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/Blade8",
    "@odata.type": "#Chassis.v1_9_1.Chassis",
    "Actions": {
        "#Chassis.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff"
            ],
            "target": "/redfish/v1/Chassis/Blade8/Actions/Chassis.Reset"
        }
    },
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/Blade8/Assembly"
    },
    "ChassisType": "Blade",
    "Id": "Blade8",
    "Location": {
        "PartLocation": {
            "LocationOrdinalValue": 8,
            "LocationType": "Slot"
        }
    },
    "Name": "Server Blade 8",
    "PowerSubsystem": {
        "@odata.id": "/redfish/v1/Chassis/Blade8/PowerSubsystem"
    },
    "Status": {
        "State": "Absent"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/Blade8/Thermal"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade8/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/Blade8/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508",
            "PartNumber": "68-6847-03  ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FOX2521P34M",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/Blade8/PowerSubsystem

```null
```

## /api-explorer/resources/redfish/v1/Chassis/Blade8/Thermal

```null
```

## /api-explorer/resources/redfish/v1/Chassis/CMC

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/CMC",
    "@odata.type": "#Chassis.v1_9_1.Chassis",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/CMC/Assembly"
    },
    "ChassisType": "Module",
    "Id": "CMC",
    "Location": {
        "Contacts": null,
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
            "County": null,
            "Floor": null,
            "Name": null,
            "Room": null,
            "State": null,
            "Street": null,
            "ZipCode": null
        }
    },
    "Manufacturer": "Cisco Systems Inc",
    "Model": "UCSX-I-9108-25G",
    "Name": "I/O Module Chassis Management Controller",
    "PartNumber": "73-20533-02 ",
    "PowerSubsystem": {
        "@odata.id": "/redfish/v1/Chassis/CMC/PowerSubsystem"
    },
    "SerialNumber": "FCH253070PZ",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/CMC/Thermal"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/CMC/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/CMC/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-I-9108-25G",
            "PartNumber": "73-20533-02 ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FCH253070PZ",
            "Version": "V02"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/CMC/PowerSubsystem

```null
```

## /api-explorer/resources/redfish/v1/Chassis/CMC/Thermal

```{
    "@odata.context": "/redfish/v1/$metadata#Thermal.Thermal",
    "@odata.id": "/redfish/v1/Chassis/CMC/Thermal",
    "@odata.type": "#Thermal.v1_5_2.Thermal",
    "Description": "Represents the properties for Temperature",
    "Fans": [
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Fans/1",
            "HotPluggable": false,
            "MemberId": "1",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 1 Fan 1",
            "Reading": 14403,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Fans/2",
            "HotPluggable": false,
            "MemberId": "2",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 1 Fan 2",
            "Reading": 12766,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Fans/3",
            "HotPluggable": false,
            "MemberId": "3",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 2 Fan 1",
            "Reading": 14456,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Fans/4",
            "HotPluggable": false,
            "MemberId": "4",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 2 Fan 2",
            "Reading": 12443,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Fans/5",
            "HotPluggable": false,
            "MemberId": "5",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 3 Fan 1",
            "Reading": 14043,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/CMC/Thermal#/Fans/6",
            "HotPluggable": false,
            "MemberId": "6",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 3 Fan 2",
            "Reading": 12522,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ],
    "Fans@odata.count": 6,
    "Id": "Thermal",
    "Name": "Thermal"
}
```

## /api-explorer/resources/redfish/v1/Chassis/FEM1

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/FEM1",
    "@odata.type": "#Chassis.v1_9_1.Chassis",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/FEM1/Assembly"
    },
    "ChassisType": "Module",
    "Id": "FEM1",
    "Location": {
        "PartLocation": {
            "LocationOrdinalValue": 1,
            "LocationType": "Slot"
        }
    },
    "Manufacturer": "Cisco Systems Inc",
    "Model": "UCSX-9508-RBLK",
    "Name": "Fabric Extender Module 1",
    "PartNumber": "73-19787-04 ",
    "PowerSubsystem": {
        "@odata.id": "/redfish/v1/Chassis/FEM1/PowerSubsystem"
    },
    "SerialNumber": "FCH2517712D",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/FEM1/Thermal"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/FEM1/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/FEM1/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/FEM1/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508-RBLK",
            "PartNumber": "73-19787-04 ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FCH2517712D",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/FEM1/PowerSubsystem

```null
```

## /api-explorer/resources/redfish/v1/Chassis/FEM1/Thermal

```{
    "@odata.context": "/redfish/v1/$metadata#Thermal.Thermal",
    "@odata.id": "/redfish/v1/Chassis/FEM1/Thermal",
    "@odata.type": "#Thermal.v1_5_2.Thermal",
    "Description": "Represents the properties for Temperature",
    "Fans": [
        {
            "@odata.id": "/redfish/v1/Chassis/FEM1/Thermal#/Fans/1",
            "HotPluggable": false,
            "MemberId": "1",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 1 Fan 1",
            "Reading": 14350,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FEM1/Thermal#/Fans/2",
            "HotPluggable": false,
            "MemberId": "2",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 1 Fan 2",
            "Reading": 12725,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FEM1/Thermal#/Fans/3",
            "HotPluggable": false,
            "MemberId": "3",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 2 Fan 1",
            "Reading": 14403,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FEM1/Thermal#/Fans/4",
            "HotPluggable": false,
            "MemberId": "4",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 2 Fan 2",
            "Reading": 12725,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FEM1/Thermal#/Fans/5",
            "HotPluggable": false,
            "MemberId": "5",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 3 Fan 1",
            "Reading": 14246,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FEM1/Thermal#/Fans/6",
            "HotPluggable": false,
            "MemberId": "6",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 3 Fan 2",
            "Reading": 12522,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ],
    "Fans@odata.count": 6,
    "Id": "Thermal",
    "Name": "Thermal"
}
```

## /api-explorer/resources/redfish/v1/Chassis/FEM2

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/FEM2",
    "@odata.type": "#Chassis.v1_9_1.Chassis",
    "Assembly": {
        "@odata.id": "/redfish/v1/Chassis/FEM2/Assembly"
    },
    "ChassisType": "Module",
    "Id": "FEM2",
    "Location": {
        "PartLocation": {
            "LocationOrdinalValue": 2,
            "LocationType": "Slot"
        }
    },
    "Manufacturer": "Cisco Systems Inc",
    "Model": "UCSX-9508-RBLK",
    "Name": "Fabric Extender Module 2",
    "PartNumber": "73-19787-04 ",
    "PowerSubsystem": {
        "@odata.id": "/redfish/v1/Chassis/FEM2/PowerSubsystem"
    },
    "SerialNumber": "FCH25177132",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/FEM2/Thermal"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/FEM2/Assembly

```{
    "@odata.context": "/redfish/v1/$metadata#Assembly.Assembly",
    "@odata.id": "/redfish/v1/Chassis/FEM2/Assembly",
    "@odata.type": "#Assembly.v1_2_1.Assembly",
    "Assemblies": [
        {
            "@odata.id": "/redfish/v1/Chassis/FEM2/Assembly#/Assemblies/0",
            "MemberId": "0",
            "Model": "UCSX-9508-RBLK",
            "PartNumber": "73-19787-04 ",
            "Producer": "Cisco Systems Inc",
            "SerialNumber": "FCH25177132",
            "Version": "V01"
        }
    ],
    "Description": "Assembly",
    "Id": "Assembly",
    "Name": "Assembly"
}
```

## /api-explorer/resources/redfish/v1/Chassis/FEM2/PowerSubsystem

```null
```

## /api-explorer/resources/redfish/v1/Chassis/FEM2/Thermal

```{
    "@odata.context": "/redfish/v1/$metadata#Thermal.Thermal",
    "@odata.id": "/redfish/v1/Chassis/FEM2/Thermal",
    "@odata.type": "#Thermal.v1_5_2.Thermal",
    "Description": "Represents the properties for Temperature",
    "Fans": [
        {
            "@odata.id": "/redfish/v1/Chassis/FEM2/Thermal#/Fans/1",
            "HotPluggable": false,
            "MemberId": "1",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 1 Fan 1",
            "Reading": 14403,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FEM2/Thermal#/Fans/2",
            "HotPluggable": false,
            "MemberId": "2",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 1 Fan 2",
            "Reading": 12684,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FEM2/Thermal#/Fans/3",
            "HotPluggable": false,
            "MemberId": "3",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 2 Fan 1",
            "Reading": 14350,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FEM2/Thermal#/Fans/4",
            "HotPluggable": false,
            "MemberId": "4",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 2 Fan 2",
            "Reading": 12725,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FEM2/Thermal#/Fans/5",
            "HotPluggable": false,
            "MemberId": "5",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 3 Fan 1",
            "Reading": 14195,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/FEM2/Thermal#/Fans/6",
            "HotPluggable": false,
            "MemberId": "6",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 3 Fan 2",
            "Reading": 12562,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ],
    "Fans@odata.count": 6,
    "Id": "Thermal",
    "Name": "Thermal"
}
```

## /api-explorer/resources/redfish/v1/Chassis/PeerCMC

```{
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/PeerCMC",
    "@odata.type": "#Chassis.v1_9_1.Chassis",
    "ChassisType": "Module",
    "Id": "PeerCMC",
    "Location": {
        "PartLocation": {
            "LocationOrdinalValue": 2,
            "LocationType": "Slot"
        }
    },
    "Name": "I/O Module Chassis Management Controller",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/PeerCMC/Thermal"
    }
}
```

## /api-explorer/resources/redfish/v1/Chassis/PeerCMC/Thermal

```{
    "@odata.context": "/redfish/v1/$metadata#Thermal.Thermal",
    "@odata.id": "/redfish/v1/Chassis/PeerCMC/Thermal",
    "@odata.type": "#Thermal.v1_5_2.Thermal",
    "Description": "Represents the properties for Temperature",
    "Fans": [
        {
            "@odata.id": "/redfish/v1/Chassis/PeerCMC/Thermal#/Fans/1",
            "HotPluggable": false,
            "MemberId": "1",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 1 Fan 1",
            "Reading": 14456,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/PeerCMC/Thermal#/Fans/2",
            "HotPluggable": false,
            "MemberId": "2",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 1 Fan 2",
            "Reading": 12684,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/PeerCMC/Thermal#/Fans/3",
            "HotPluggable": false,
            "MemberId": "3",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 2 Fan 1",
            "Reading": 14350,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/PeerCMC/Thermal#/Fans/4",
            "HotPluggable": false,
            "MemberId": "4",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 2 Fan 2",
            "Reading": 12603,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/PeerCMC/Thermal#/Fans/5",
            "HotPluggable": false,
            "MemberId": "5",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 3 Fan 1",
            "Reading": 14195,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        },
        {
            "@odata.id": "/redfish/v1/Chassis/PeerCMC/Thermal#/Fans/6",
            "HotPluggable": false,
            "MemberId": "6",
            "Model": "UCSX-RSFAN",
            "Name": "Fan Module 3 Fan 2",
            "Reading": 12562,
            "ReadingUnits": "RPM",
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ],
    "Fans@odata.count": 6,
    "Id": "Thermal",
    "Name": "Thermal"
}
```

