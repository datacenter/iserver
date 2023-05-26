# Resource: /redfish/v1/EventService

Vendor | Model
--- | ---
HPE | vServer

## /redfish/v1/EventService

```{
    "@odata.context": "/redfish/v1/$metadata#EventService.EventService",
    "@odata.etag": "W/\"C56F367A\"",
    "@odata.id": "/redfish/v1/EventService",
    "@odata.type": "#EventService.v1_0_8.EventService",
    "Actions": {
        "#EventService.SubmitTestEvent": {
            "EventType@Redfish.AllowableValues": [
                "StatusChange",
                "ResourceUpdated",
                "ResourceAdded",
                "ResourceRemoved",
                "Alert"
            ],
            "target": "/redfish/v1/EventService/Actions/EventService.SubmitTestEvent"
        }
    },
    "DeliveryRetryAttempts": 3,
    "DeliveryRetryIntervalSeconds": 30,
    "Description": "Event Subscription service",
    "EventTypesForSubscription": [
        "StatusChange",
        "ResourceUpdated",
        "ResourceAdded",
        "ResourceRemoved",
        "Alert"
    ],
    "Id": "EventService",
    "Name": "Event Service",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeEventService.HpeEventService",
            "@odata.id": "/redfish/v1/EventService",
            "@odata.type": "#HpeEventService.v2_1_0.HpeEventService",
            "Actions": {
                "#HpeEventService.ImportCACertificate": {
                    "target": "/redfish/v1/EventService/Actions/Oem/Hpe/HpeEventService.ImportCACertificate"
                }
            },
            "CACertificates": {
                "@odata.id": "/redfish/v1/EventService/CACertificates"
            },
            "Id": "EventService",
            "RequestedMaxEventsToQueueDefault": 3,
            "RetireOldEventInMinutesDefault": 10,
            "TTLCountDefault": 999999,
            "TTLUnitsDefault": "minutes"
        }
    },
    "ServiceEnabled": true,
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "Subscriptions": {
        "@odata.id": "/redfish/v1/EventService/Subscriptions"
    }
}
```

## /redfish/v1/EventService/CACertificates

```{
    "@odata.context": "/redfish/v1/$metadata#HpeCertificateCollection.HpeCertificateCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/EventService/CACertificates",
    "@odata.type": "#HpeCertificateCollection.HpeCertificateCollection",
    "Description": "Trusted CA Certificates for REST Event Mutual Authentication",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "REST CA Certificates"
}
```

## /redfish/v1/EventService/Subscriptions

```{
    "@odata.context": "/redfish/v1/$metadata#EventDestinationCollection.EventDestinationCollection",
    "@odata.etag": "W/\"AA6D42B0\"",
    "@odata.id": "/redfish/v1/EventService/Subscriptions",
    "@odata.type": "#EventDestinationCollection.EventDestinationCollection",
    "Description": "iLO User Event Subscriptions",
    "Members": [
        {
            "@odata.id": "/redfish/v1/EventService/Subscriptions/1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "EventSubscriptions"
}
```

## /redfish/v1/EventService/Subscriptions/1

```{
    "@odata.context": "/redfish/v1/$metadata#EventDestination.EventDestination",
    "@odata.etag": "W/\"07DC051F\"",
    "@odata.id": "/redfish/v1/EventService/Subscriptions/1",
    "@odata.type": "#EventDestination.v1_0_0.EventDestination",
    "Context": "",
    "Description": "iLO Event Subscription",
    "Destination": "https://10.29.152.124/rest/event-sink?resourceUri=/rest/server-hardware/39383250-3834-4D32-3231-33323034374B&resourceCategory=server-hardware",
    "EventTypes": [
        "ResourceAdded",
        "ResourceUpdated",
        "ResourceRemoved",
        "StatusChange",
        "Alert"
    ],
    "HttpHeaders": [],
    "Id": "1",
    "Name": "Event Subscription",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeEventDestination.HpeEventDestination",
            "@odata.type": "#HpeEventDestination.v2_1_0.HpeEventDestination",
            "DeliveryRetryAttempts": 1440,
            "DeliveryRetryIntervalInSeconds": 60,
            "MutualAuthenticationEnabled": false,
            "RequestedMaxEventsToQueue": 64,
            "RetireOldEventInMinutes": 10
        }
    },
    "Protocol": "Redfish"
}
```

