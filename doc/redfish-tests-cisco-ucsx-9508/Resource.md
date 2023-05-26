# Redfish Resources

Vendor | Model
--- | ---
Cisco | UCSX-9508

## Root Resource

```
# iserver get redfish endpoint
    --cache chassis-UCSX-9508-fox2521p34m
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Chassis
    --inventory-id IoCard-1-1

/api-explorer/resources/redfish/v1/
-----------------------------------
{
    "@odata.context": "/redfish/v1/$metadata#ServiceRoot.ServiceRoot",
    "@odata.id": "/redfish/v1",
    "@odata.type": "#ServiceRoot.v1_5_1.ServiceRoot",
    "AccountService": {
        "@odata.id": "/redfish/v1/AccountService"
    },
    "Chassis": {
        "@odata.id": "/redfish/v1/Chassis"
    },
    "Description": "Root Service",
    "EventService": {
        "@odata.id": "/redfish/v1/EventService"
    },
    "Id": "RootService",
    "JsonSchemas": {
        "@odata.id": "/redfish/v1/JsonSchemas"
    },
    "Links": {
        "Sessions": {
            "@odata.id": "/redfish/v1/SessionService/Sessions"
        }
    },
    "Managers": {
        "@odata.id": "/redfish/v1/Managers"
    },
    "Name": "Cisco RESTful Root Service",
    "Oem": {
        "@odata.id": "/redfish/v1/Oem"
    },
    "RedfishVersion": "1.5.1",
    "Registries": {
        "@odata.id": "/redfish/v1/Registries"
    },
    "SessionService": {
        "@odata.id": "/redfish/v1/SessionService"
    },
    "Tasks": {
        "@odata.id": "/redfish/v1/TaskService"
    },
    "UpdateService": {
        "@odata.id": "/redfish/v1/UpdateService"
    }
}
```

## Children

- [/api-explorer/resources/redfish/v1/AccountService](./UriAccountService.md)
- [/api-explorer/resources/redfish/v1/Chassis](./UriChassis.md)
- [/api-explorer/resources/redfish/v1/EventService](./UriEventService.md)
- [/api-explorer/resources/redfish/v1/JsonSchemas](./UriJsonSchemas.md)
- [/api-explorer/resources/redfish/v1/Managers](./UriManagers.md)
- [/api-explorer/resources/redfish/v1/Oem](./UriOem.md)
- [/api-explorer/resources/redfish/v1/Registries](./UriRegistries.md)
- [/api-explorer/resources/redfish/v1/SessionService](./UriSessionService.md)
- [/api-explorer/resources/redfish/v1/TaskService](./UriTaskService.md)
- [/api-explorer/resources/redfish/v1/UpdateService](./UriUpdateService.md)
