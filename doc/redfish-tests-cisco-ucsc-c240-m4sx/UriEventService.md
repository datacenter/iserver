# Resource: /redfish/v1/EventService

Vendor | Model
--- | ---
Cisco | UCSC-C240-M4SX

## /redfish/v1/EventService

```{
    "@odata.context": "/redfish/v1/$metadata#EventService",
    "@odata.id": "/redfish/v1/EventService",
    "@odata.type": "#EventService.v1_2_0.EventService",
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
    "@odata.context": "/redfish/v1/$metadata#EventService/Subscriptions",
    "@odata.id": "/redfish/v1/EventService/Subscriptions",
    "@odata.type": "#EventDestinationCollection.EventDestinationCollection",
    "Description": "List of Event subscriptions",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Event Subscriptions Collection"
}
```

