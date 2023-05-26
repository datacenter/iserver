# Redfish Resources

Vendor | Model
--- | ---
Cisco | UCSC-C240-M5SX

## Root Resource

```
# iserver get redfish endpoint
    --cache ucsc-c240-m5sx-wzp23450c8k-4.1.3d-on
    --type ucsc
    --ip 10.58.50.51
    --username admin
    --password ******

/redfish/v1/
------------
{
    "@odata.context": "/redfish/v1/$metadata#ServiceRoot.ServiceRoot",
    "@odata.id": "/redfish/v1",
    "@odata.type": "#ServiceRoot.v1_5_1.ServiceRoot",
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
    "Fabrics": {
        "@odata.id": "/redfish/v1/Fabrics"
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
    "Product": "UCSC-C240-M5SX",
    "RedfishVersion": "1.5.1",
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
    "UpdateService": {
        "@odata.id": "/redfish/v1/UpdateService"
    },
    "Vendor": "Cisco Systems Inc."
}
```

## Children

- [/redfish/v1/AccountService](./UriAccountService.md)
- [/redfish/v1/CertificateService](./UriCertificateService.md)
- [/redfish/v1/Chassis](./UriChassis.md)
- [/redfish/v1/EventService](./UriEventService.md)
- [/redfish/v1/Fabrics](./UriFabrics.md)
- [/redfish/v1/JsonSchemas](./UriJsonSchemas.md)
- [/redfish/v1/Managers](./UriManagers.md)
- [/redfish/v1/Registries](./UriRegistries.md)
- [/redfish/v1/SessionService](./UriSessionService.md)
- [/redfish/v1/Systems](./UriSystems.md)
- [/redfish/v1/TaskService](./UriTaskService.md)
- [/redfish/v1/UpdateService](./UriUpdateService.md)
