# Redfish Resources

Vendor | Model
--- | ---
Dell | vServer

## Root Resource

```
# iserver get redfish endpoint
    --cache dell-poweredge-r650-ygfcbtjso8womr-5.10.00.00-on
    --type dell
    --ip 10.58.24.210
    --port 49153
    --username administrator
    --password ******

/redfish/v1/
------------
{
    "@odata.context": "/redfish/v1/$metadata#ServiceRoot.ServiceRoot",
    "@odata.id": "/redfish/v1",
    "@odata.type": "#ServiceRoot.v1_8_0.ServiceRoot",
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
    "JobService": {
        "@odata.id": "/redfish/v1/JobService"
    },
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
    "Name": "Root Service",
    "Oem": {
        "Dell": {
            "@odata.context": "/redfish/v1/$metadata#DellServiceRoot.DellServiceRoot",
            "@odata.type": "#DellServiceRoot.v1_0_0.DellServiceRoot",
            "IsBranded": 0,
            "ManagerMACAddress": "b0:7b:25:d1:5a:5a",
            "ServiceTag": "U8OIL5X"
        }
    },
    "Product": "Integrated Dell Remote Access Controller",
    "ProtocolFeaturesSupported": {
        "DeepOperations": {
            "DeepPATCH": false,
            "DeepPOST": false
        },
        "ExcerptQuery": false,
        "ExpandQuery": {
            "ExpandAll": true,
            "Levels": true,
            "Links": true,
            "MaxLevels": 1,
            "NoLinks": true
        },
        "FilterQuery": true,
        "OnlyMemberQuery": true,
        "SelectQuery": true
    },
    "RedfishVersion": "1.11.0",
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
    "TelemetryService": {
        "@odata.id": "/redfish/v1/TelemetryService"
    },
    "UpdateService": {
        "@odata.id": "/redfish/v1/UpdateService"
    },
    "Vendor": "Dell"
}
```

## Children

- [/redfish/v1/AccountService](./UriAccountService.md)
- [/redfish/v1/CertificateService](./UriCertificateService.md)
- [/redfish/v1/Chassis](./UriChassis.md)
- [/redfish/v1/EventService](./UriEventService.md)
- [/redfish/v1/Fabrics](./UriFabrics.md)
- [/redfish/v1/JobService](./UriJobService.md)
- [/redfish/v1/JsonSchemas](./UriJsonSchemas.md)
- [/redfish/v1/Managers](./UriManagers.md)
- [/redfish/v1/Registries](./UriRegistries.md)
- [/redfish/v1/SessionService](./UriSessionService.md)
- [/redfish/v1/Systems](./UriSystems.md)
- [/redfish/v1/TaskService](./UriTaskService.md)
- [/redfish/v1/TelemetryService](./UriTelemetryService.md)
- [/redfish/v1/UpdateService](./UriUpdateService.md)
