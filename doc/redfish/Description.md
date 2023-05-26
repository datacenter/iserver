# Get resource description

Each Redfish resource is defined with the set of mandatory properties that can be easily selected using --description flag.

Use --deep option to get description recursively starting with the root uri defined with --uri parameter.

## Get resource description

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --description

/redfish/v1/Systems/WZP23400AK4
-------------------------------
{
    "Id": "WZP23400AK4",
    "Name": "UCS C240 M5SN",
    "Description": "Represents general resources for the overall system"
}
```

## Get resources description recursively

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri EventService
    --description
    --deep

/redfish/v1/EventService
------------------------
{
    "@odata.id": "/redfish/v1/EventService",
    "@odata.type": "#EventService.v1_5_0.EventService",
    "@odata.context": "/redfish/v1/$metadata#EventService.EventService",
    "Id": "EventService",
    "Name": "Event Service",
    "Description": "Event Service represents the properties for the service"
}

/redfish/v1/EventService/Subscriptions
--------------------------------------
{
    "@odata.id": "/redfish/v1/EventService/Subscriptions",
    "@odata.type": "#EventDestinationCollection.EventDestinationCollection",
    "@odata.context": "/redfish/v1/$metadata#EventDestinationCollection.EventDestinationCollection",
    "Name": "Event Subscriptions Collection",
    "Description": "List of Event subscriptions"
}

/redfish/v1/EventService/Subscriptions/SNMP_1
---------------------------------------------
{
    "@odata.id": "/redfish/v1/EventService/Subscriptions/SNMP_1",
    "@odata.type": "#EventDestination.v1_7_0.EventDestination",
    "@odata.context": "/redfish/v1/$metadata#EventDestination.EventDestination",
    "Id": "SNMP_1",
    "Name": "EventSubscription SNMP_1",
    "Description": "Event Subscription Details"
}
```
