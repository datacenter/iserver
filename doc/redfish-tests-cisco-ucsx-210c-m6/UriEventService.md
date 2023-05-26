# Resource: /api-explorer/resources/redfish/v1/EventService

Vendor | Model
--- | ---
Cisco | UCSX-210C-M6

## /api-explorer/resources/redfish/v1/EventService

```{
    "@odata.context": "/redfish/v1/$metadata#EventService.EventService",
    "@odata.id": "/redfish/v1/EventService",
    "@odata.type": "#EventService.v1_7_0.EventService",
    "Description": "Event Service represents the properties for the service",
    "Id": "EventService",
    "Name": "Event Service",
    "SMTP": {
        "Authentication": "None",
        "ConnectionProtocol": "None",
        "FromAddress": "210C-FCH25337EHM@cisco.com",
        "Port": null,
        "ServerAddress": null,
        "ServiceEnabled": null
    },
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Subscriptions": {
        "@odata.id": "/redfish/v1/EventService/Subscriptions"
    }
}
```

## /api-explorer/resources/redfish/v1/EventService/Subscriptions

```{
    "@odata.context": "/redfish/v1/$metadata#EventDestinationCollection.EventDestinationCollection",
    "@odata.id": "/redfish/v1/EventService/Subscriptions",
    "@odata.type": "#EventDestinationCollection.EventDestinationCollection",
    "Description": "List of Event subscriptions",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Event Subscriptions Collection"
}
```

