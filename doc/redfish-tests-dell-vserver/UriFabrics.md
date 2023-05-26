# Resource: /redfish/v1/Fabrics

Vendor | Model
--- | ---
Dell | vServer

## /redfish/v1/Fabrics

```{
    "@odata.context": "/redfish/v1/$metadata#FabricCollection.FabricCollection",
    "@odata.id": "/redfish/v1/Fabrics",
    "@odata.type": "#FabricCollection.FabricCollection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Fabrics/PCIe"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Fabric Collection"
}
```

## /redfish/v1/Fabrics/PCIe

```{
    "@odata.context": "/redfish/v1/$metadata#Fabric.Fabric",
    "@odata.id": "/redfish/v1/Fabrics/PCIe",
    "@odata.type": "#Fabric.v1_1_1.Fabric",
    "Description": "PCIe Fabric",
    "FabricType": "PCIe",
    "Id": "PCIe",
    "Links": {},
    "Name": "PCIe Fabric",
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "Switches": {
        "@odata.id": "/redfish/v1/Fabrics/PCIe/Switches"
    }
}
```

## /redfish/v1/Fabrics/PCIe/Switches

```{
    "@odata.context": "/redfish/v1/$metadata#SwitchCollection.SwitchCollection",
    "@odata.id": "/redfish/v1/Fabrics/PCIe/Switches",
    "@odata.type": "#SwitchCollection.SwitchCollection",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Switch Collection"
}
```

