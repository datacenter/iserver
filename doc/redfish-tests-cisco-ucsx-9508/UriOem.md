# Resource: /api-explorer/resources/redfish/v1/Oem

Vendor | Model
--- | ---
Cisco | UCSX-9508

## /api-explorer/resources/redfish/v1/Oem

```{
    "@odata.context": "/redfish/v1/$metadata#OemRoot.OemRoot",
    "@odata.id": "/redfish/v1/Oem",
    "@odata.type": "#OemRoot.v1_0_0.OemRoot",
    "CiscoEventSubscriptionList": {
        "@odata.id": "/redfish/v1/Oem/CiscoEventSubscriptionList"
    },
    "CiscoOpaque": {
        "@odata.id": "/redfish/v1/Oem/CiscoOpaque"
    },
    "Description": "Oem Root URI.",
    "Id": "OemRoot",
    "Name": "Credfish OEM Root Service"
}
```

## /api-explorer/resources/redfish/v1/Oem/CiscoEventSubscriptionList

```{
    "@odata.context": "/redfish/v1/$metadata#CiscoEventSubscriptionList.CiscoEventSubscriptionList",
    "@odata.id": "/redfish/v1/Oem/CiscoEventSubscriptionList",
    "@odata.type": "#CiscoEventSubscriptionList.v1_2_0.CiscoEventSubscriptionList",
    "DefaultTopic": "AD.streamingevent.dejavu",
    "Enabled": true,
    "EventSubscriptions": [
        {
            "ApplyToSubordinateResources": false,
            "ODataId": "/redfish/v1/Chassis/Blade1",
            "Topic": "AD.streamingevent.gobi"
        },
        {
            "ApplyToSubordinateResources": false,
            "ODataId": "/redfish/v1/Chassis/Blade2",
            "Topic": "AD.streamingevent.gobi"
        },
        {
            "ApplyToSubordinateResources": false,
            "ODataId": "/redfish/v1/Chassis/Blade3",
            "Topic": "AD.streamingevent.gobi"
        },
        {
            "ApplyToSubordinateResources": false,
            "ODataId": "/redfish/v1/Chassis/Blade4",
            "Topic": "AD.streamingevent.gobi"
        },
        {
            "ApplyToSubordinateResources": false,
            "ODataId": "/redfish/v1/Chassis/Blade5",
            "Topic": "AD.streamingevent.gobi"
        },
        {
            "ApplyToSubordinateResources": false,
            "ODataId": "/redfish/v1/Chassis/Blade6",
            "Topic": "AD.streamingevent.gobi"
        },
        {
            "ApplyToSubordinateResources": false,
            "ODataId": "/redfish/v1/Chassis/Blade7",
            "Topic": "AD.streamingevent.gobi"
        },
        {
            "ApplyToSubordinateResources": false,
            "ODataId": "/redfish/v1/Chassis/Blade8",
            "Topic": "AD.streamingevent.gobi"
        },
        {
            "ODataType": "#Chassis.v1_9_1.Chassis",
            "Topic": "AD.streamingevent.dejavu"
        },
        {
            "ODataType": "#Power.v1_5_3.Power",
            "Topic": "AD.streamingevent.dejavu"
        },
        {
            "ODataType": "#Thermal.v1_5_2.Thermal",
            "Topic": "AD.streamingevent.dejavu"
        },
        {
            "ODataType": "#Manager.v1_5_0.Manager",
            "Topic": "AD.streamingevent.dejavu"
        },
        {
            "ODataType": "#Assembly.v1_2_1.Assembly",
            "Topic": "AD.streamingevent.dejavu"
        },
        {
            "ODataType": "#SoftwareInventory.v1_2_2.SoftwareInventory",
            "Topic": "AD.streamingevent.dejavu"
        },
        {
            "ODataType": "#VLanNetworkInterfaceCollection.VLanNetworkInterfaceCollection ",
            "Topic": "AD.streamingevent.dejavu"
        }
    ],
    "EventSubscriptionsCount": 15,
    "Id": "CiscoEventSubscriptionList.v1_2_0",
    "Name": "Cisco Event Subscription List",
    "Version": 2
}
```

## /api-explorer/resources/redfish/v1/Oem/CiscoOpaque

```{
    "@odata.context": "/redfish/v1/$metadata#CiscoOpaque.CiscoOpaque",
    "@odata.id": "/redfish/v1/Oem/CiscoOpaque",
    "@odata.type": "#CiscoOpaque.v1_0_0.CiscoOpaque",
    "Id": "CiscoOpaque",
    "Name": "CiscoOpaque",
    "OpaqueItems": [
        {
            "Capabilities": [
                "WriteOnly",
                "FIOnly"
            ],
            "Hash": "7cd8ab8e4e1f7637a89f7a5aaffc72",
            "OpaqueID": "CiscoOpaque.0",
            "URL": "/cisco/blob/SldpShadowPasswordAuth"
        }
    ],
    "OpaqueItemsCount": 1
}
```

