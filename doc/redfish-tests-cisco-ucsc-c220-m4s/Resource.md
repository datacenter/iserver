# Redfish Resources

Vendor | Model
--- | ---
Cisco | UCSC-C220-M4S

## Root Resource

```
# iserver get redfish endpoint
    --cache ucsc-ucs-c220-m4s-fch2017v24j-4.1.2g-off
    --type ucsc
    --ip 10.58.50.59
    --username admin
    --password ******

/redfish/v1/
------------
{
    "@odata.context": "/redfish/v1/$metadata#ServiceRoot",
    "@odata.id": "/redfish/v1/",
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
    "Product": "UCS C220 M4S",
    "RedfishVersion": "1.2.0",
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
- [/redfish/v1/JsonSchemas](./UriJsonSchemas.md)
- [/redfish/v1/Managers](./UriManagers.md)
- [/redfish/v1/Registries](./UriRegistries.md)
- [/redfish/v1/SessionService](./UriSessionService.md)
- [/redfish/v1/Systems](./UriSystems.md)
- [/redfish/v1/TaskService](./UriTaskService.md)
- [/redfish/v1/UpdateService](./UriUpdateService.md)
