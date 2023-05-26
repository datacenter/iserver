# Redfish Resources

Vendor | Model
--- | ---
Cisco | UCSX-210C-M6

## Root Resource

```
# iserver get redfish endpoint
    --cache ucsc-ucsx-210c-m6-fch25337ehm-5.0.1f-on
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Server
    --inventory-id FI4-1-1

/api-explorer/resources/redfish/v1/
-----------------------------------
{
    "@odata.context": "/redfish/v1/$metadata#ServiceRoot.ServiceRoot",
    "@odata.id": "/redfish/v1/",
    "@odata.type": "#ServiceRoot.v1_9_0.ServiceRoot",
    "AccountService": {
        "@odata.id": "/redfish/v1/AccountService"
    },
    "CertificateService": {
        "@odata.id": "/redfish/v1/CertificateService"
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
    "RedfishVersion": "1.9.0",
    "Registries": {
        "@odata.id": "/redfish/v1/Registries"
    },
    "SessionService": {
        "@odata.id": "/redfish/v1/SessionService"
    },
    "Systems": {
        "@odata.id": "/redfish/v1/Systems"
    },
    "Tasks": {
        "@odata.id": "/redfish/v1/TaskService"
    },
    "UUID": "F4E8E18C-6C28-4C75-8814-BFBE341D0620",
    "UpdateService": {
        "@odata.id": "/redfish/v1/UpdateService"
    }
}
```

## Children

- [/api-explorer/resources/redfish/v1/AccountService](./UriAccountService.md)
- [/api-explorer/resources/redfish/v1/CertificateService](./UriCertificateService.md)
- [/api-explorer/resources/redfish/v1/Chassis](./UriChassis.md)
- [/api-explorer/resources/redfish/v1/EventService](./UriEventService.md)
- [/api-explorer/resources/redfish/v1/JsonSchemas](./UriJsonSchemas.md)
- [/api-explorer/resources/redfish/v1/Managers](./UriManagers.md)
- [/api-explorer/resources/redfish/v1/Registries](./UriRegistries.md)
- [/api-explorer/resources/redfish/v1/SessionService](./UriSessionService.md)
- [/api-explorer/resources/redfish/v1/Systems](./UriSystems.md)
- [/api-explorer/resources/redfish/v1/TaskService](./UriTaskService.md)
- [/api-explorer/resources/redfish/v1/UpdateService](./UriUpdateService.md)
