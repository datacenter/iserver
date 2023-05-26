# Resource: /redfish/v1/EventService

Vendor | Model
--- | ---
Cisco | UCSC-C220-M5SX

## /redfish/v1/EventService

```{
    "@odata.context": "/redfish/v1/$metadata#EventService.EventService",
    "@odata.id": "/redfish/v1/EventService",
    "@odata.type": "#EventService.v1_5_0.EventService",
    "Actions": {
        "#EventService.SubmitTestEvent": {
            "target": "/redfish/v1/EventService/Actions/EventService.SubmitTestEvent"
        }
    },
    "DeliveryRetryAttempts": 3,
    "DeliveryRetryIntervalSeconds": 30,
    "Description": "Event Service represents the properties for the service",
    "EventTypesForSubscription": [
        "Alert"
    ],
    "Id": "EventService",
    "Name": "Event Service",
    "SMTP": {
        "FromAddress": "",
        "Port": 25,
        "ServerAddress": "",
        "ServiceEnabled": false
    },
    "ServiceEnabled": false,
    "Status": {
        "Health": "OK",
        "State": "Disabled"
    },
    "Subscriptions": {
        "@odata.id": "/redfish/v1/EventService/Subscriptions"
    }
}
```

## /redfish/v1/EventService/Subscriptions

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

