# Resource: /redfish/v1/Fabrics

Vendor | Model
--- | ---
Cisco | UCSC-C240-M5SX

## /redfish/v1/Fabrics

```{
    "@odata.context": "/redfish/v1/$metadata#FabricCollection.FabricCollection",
    "@odata.id": "/redfish/v1/Fabrics",
    "@odata.type": "#FabricCollection.FabricCollection",
    "Description": "Collection of Fabrics",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Fabric Collection"
}
```

## /redfish/v1/Fabrics/SASFabric

```{
    "@odata.context": "/redfish/v1/$metadata#Fabric.Fabric",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric",
    "@odata.type": "#Fabric.v1_1_0.Fabric",
    "Description": "SAS Fabric Description",
    "FabricType": "SAS",
    "Id": "SASFabric",
    "MaxZones": 1,
    "Name": "SASFabric",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Switches": {
        "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches"
    }
}
```

## /redfish/v1/Fabrics/SASFabric/Switches

```{
    "@odata.context": "/redfish/v1/$metadata#SwitchCollection.SwitchCollection",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches",
    "@odata.type": "#SwitchCollection.SwitchCollection",
    "Description": "Collection of Switches",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Switch Collection"
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1

```{
    "@odata.context": "/redfish/v1/$metadata#Switch.Switch",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1",
    "@odata.type": "#Switch.v1_3_0.Switch",
    "Description": "Switch Information",
    "Id": "SASEXP1",
    "Manufacturer": "LSI",
    "Model": "CubR SAS3 Expander",
    "Name": "SASEXP1",
    "Oem": {
        "Cisco": {
            "ActiveFirmwareRevision": "65.09.16.00",
            "BackupFirmwareRevision": "65.11.20.00",
            "BackupImageState": "valid",
            "BootFirmwareRevision": "65.02.13.00",
            "CiscoVersion": "                ",
            "ComponentId": "2.59",
            "ComponentRevision": "1",
            "CurrentEndDeviceFrameBuffering": "0",
            "DrivePresence": "E00003",
            "EnclosureLogicalId": "55C710DC69150ABF",
            "ExecutingFirmwarePartition": "2",
            "ExpanderOperationStatus": "Operable",
            "ManufacturingMajorRevision": "1",
            "ManufacturingMinorRevision": "1",
            "ManufacturingPlatformId": "0",
            "MaxDriveSlots": 26,
            "OperationStatusReason": "",
            "PersistedEndDeviceFrameBuffering": "E00003",
            "ProtocolVersion": "2",
            "SasAddress": "55C710DC691501BF",
            "StartSlotNumber": 1,
            "TemperatureInCelsius": 49
        }
    },
    "Ports": {
        "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports"
    },
    "PowerState": "On",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "SwitchType": "SAS"
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports

```{
    "@odata.context": "/redfish/v1/$metadata#PortCollection.PortCollection",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports",
    "@odata.type": "#PortCollection.PortCollection",
    "Description": "Collection of Ports",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/0"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/1"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/2"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/3"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/4"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/5"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/6"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/7"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/8"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/9"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/10"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/11"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/12"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/13"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/14"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/15"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/16"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/17"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/18"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/19"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/20"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/21"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/22"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/23"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/24"
        },
        {
            "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/25"
        }
    ],
    "Members@odata.count": 26,
    "Name": "Port Collection"
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/0

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/0",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "0",
    "MaxSpeedGbps": 12,
    "Name": "0",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/1

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/1",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "1",
    "MaxSpeedGbps": 12,
    "Name": "1",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/10

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/10",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "10",
    "MaxSpeedGbps": 12,
    "Name": "10",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/11

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/11",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "11",
    "MaxSpeedGbps": 12,
    "Name": "11",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/12

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/12",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "12",
    "MaxSpeedGbps": 12,
    "Name": "12",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/13

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/13",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "13",
    "MaxSpeedGbps": 12,
    "Name": "13",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/14

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/14",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "14",
    "MaxSpeedGbps": 12,
    "Name": "14",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/15

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/15",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "15",
    "MaxSpeedGbps": 12,
    "Name": "15",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/16

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/16",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "16",
    "MaxSpeedGbps": 12,
    "Name": "16",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/17

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/17",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "17",
    "MaxSpeedGbps": 12,
    "Name": "17",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/18

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/18",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "18",
    "MaxSpeedGbps": 12,
    "Name": "18",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/19

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/19",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "19",
    "MaxSpeedGbps": 12,
    "Name": "19",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/2

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/2",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "2",
    "MaxSpeedGbps": 12,
    "Name": "2",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/20

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/20",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "20",
    "MaxSpeedGbps": 12,
    "Name": "20",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/21

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/21",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "21",
    "MaxSpeedGbps": 12,
    "Name": "21",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/22

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/22",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "22",
    "MaxSpeedGbps": 12,
    "Name": "22",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/23

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/23",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "23",
    "MaxSpeedGbps": 12,
    "Name": "23",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/24

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/24",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "24",
    "MaxSpeedGbps": 12,
    "Name": "24",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/25

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/25",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "25",
    "MaxSpeedGbps": 12,
    "Name": "25",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/3

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/3",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "3",
    "MaxSpeedGbps": 12,
    "Name": "3",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/4

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/4",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "4",
    "MaxSpeedGbps": 12,
    "Name": "4",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/5

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/5",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "5",
    "MaxSpeedGbps": 12,
    "Name": "5",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/6

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/6",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "6",
    "MaxSpeedGbps": 12,
    "Name": "6",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/7

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/7",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "7",
    "MaxSpeedGbps": 12,
    "Name": "7",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/8

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/8",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "8",
    "MaxSpeedGbps": 12,
    "Name": "8",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

## /redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/9

```{
    "@odata.context": "/redfish/v1/$metadata#Port.Port",
    "@odata.id": "/redfish/v1/Fabrics/SASFabric/Switches/SASEXP1/Ports/9",
    "@odata.type": "#Port.v1_2_0.Port",
    "CurrentSpeedGbps": 12,
    "Description": "Port Information",
    "Id": "9",
    "MaxSpeedGbps": 12,
    "Name": "9",
    "PortProtocol": "SAS",
    "PortType": "BidirectionalPort",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Width": 4
}
```

