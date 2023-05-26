# Resource: /redfish/v1/Fabrics

Vendor | Model
--- | ---
Cisco | UCSC-C240-M5SN

## /redfish/v1/Fabrics

```{
    "@odata.context": "/redfish/v1/$metadata#FabricCollection.FabricCollection",
    "@odata.id": "/redfish/v1/Fabrics",
    "@odata.type": "#FabricCollection.FabricCollection",
    "Description": "Collection of Fabrics",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Fabrics/PCIeFabric"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Fabric Collection"
}
```

## /redfish/v1/Fabrics/PCIeFabric

```{
    "@odata.context": "/redfish/v1/$metadata#Fabric.Fabric",
    "@odata.id": "/redfish/v1/Fabrics/PCIeFabric",
    "@odata.type": "#Fabric.v1_1_0.Fabric",
    "Description": "SAS Fabric Description",
    "FabricType": "PCIe",
    "Id": "PCIeFabric",
    "MaxZones": 1,
    "Name": "PCIeFabric",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Switches": {
        "@odata.id": "/redfish/v1/Fabrics/PCIeFabric/Switches"
    }
}
```

## /redfish/v1/Fabrics/PCIeFabric/Switches

```{
    "@odata.context": "/redfish/v1/$metadata#SwitchCollection.SwitchCollection",
    "@odata.id": "/redfish/v1/Fabrics/PCIeFabric/Switches",
    "@odata.type": "#SwitchCollection.SwitchCollection",
    "Description": "Collection of Switches",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Fabrics/PCIeFabric/Switches/PCIe-Switch"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Switch Collection"
}
```

## /redfish/v1/Fabrics/PCIeFabric/Switches/PCIe-Switch

```{
    "@odata.context": "/redfish/v1/$metadata#Switch.Switch",
    "@odata.id": "/redfish/v1/Fabrics/PCIeFabric/Switches/PCIe-Switch",
    "@odata.type": "#Switch.v1_3_0.Switch",
    "Description": "Switch Information",
    "Id": "PCIe-Switch",
    "Manufacturer": "MICROSEM",
    "Model": "PFX 48XG3",
    "Name": "PCIe-Switch",
    "Oem": {
        "Cisco": {
            "ActiveFirmwareRevision": "1.8.0.58-24b3",
            "ComponentId": "8533",
            "LinkStatus": "Optimal",
            "P2PDeviceId": "efbe",
            "P2PVendorId": "f811",
            "ProductId": "PFX 48XG3",
            "ProductRevision": "RevB",
            "ShutdownTemperatureInCel": "105 degrees C",
            "SwitchTemperatureInCel": "46 degrees C"
        }
    },
    "PowerState": "On",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "SwitchType": "PCIe"
}
```

