# Get resource recursively

Resource properties can be fetched recursively when --deep option is defined. The uri value is starting or root uri from where references are discovered.

iserver shows all resources referenced with @odata.id recursively as long as the URI of the resource is part of the root uri.

Note: if --uri is not defined, the default '/' value is applied and all Redfish resources are displayed.

## Example

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri EventService
    --deep

/redfish/v1/EventService
------------------------
{
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

/redfish/v1/EventService/Subscriptions
--------------------------------------
{
    "@odata.context": "/redfish/v1/$metadata#EventDestinationCollection.EventDestinationCollection",
    "@odata.id": "/redfish/v1/EventService/Subscriptions",
    "@odata.type": "#EventDestinationCollection.EventDestinationCollection",
    "Description": "List of Event subscriptions",
    "Members": [
        {
            "@odata.id": "/redfish/v1/EventService/Subscriptions/SNMP_1"
        }
    ],
    "Members@odata.count": 1,
    "Name": "Event Subscriptions Collection"
}

/redfish/v1/EventService/Subscriptions/SNMP_1
---------------------------------------------
{
    "@odata.context": "/redfish/v1/$metadata#EventDestination.EventDestination",
    "@odata.id": "/redfish/v1/EventService/Subscriptions/SNMP_1",
    "@odata.type": "#EventDestination.v1_7_0.EventDestination",
    "Context": null,
    "Description": "Event Subscription Details",
    "Destination": "snmp://10.58.50.203:7162",
    "Id": "SNMP_1",
    "MessageIds": [
        "F0381",
        "F0395",
        "F0176",
        "F0919",
        "F0385",
        "F0391",
        "F0393",
        "F0394",
        "F0187",
        "F0882",
        "F0434",
        "F1040",
        "F0397",
        "F0410",
        "F0460",
        "F0730",
        "F0185",
        "F0177",
        "F0425",
        "F0869",
        "F0186",
        "F0411",
        "F0920",
        "F0174",
        "F0389",
        "F0729",
        "F0868",
        "F0462",
        "F0383",
        "F0731",
        "F0461",
        "F0918",
        "F0921",
        "F0188",
        "F0409",
        "F0392",
        "F0179",
        "F0180",
        "F0396",
        "F0424"
    ],
    "Name": "EventSubscription SNMP_1",
    "Protocol": "SNMPv2c",
    "SubscriptionType": "SNMPTrap"
}
```
