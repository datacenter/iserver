# Redfish Resources

Vendor | Model
--- | ---
HPE | vServer

## Root Resource

```
# iserver get redfish endpoint
    --cache hpe-proliant-dl360-gen10-plus-vyrbx9uj4s-2.55-on
    --type hpe
    --ip 10.58.24.211
    --port 49153
    --username administrator
    --password ******

/redfish/v1/
------------
{
    "@odata.context": "/redfish/v1/$metadata#ServiceRoot.ServiceRoot",
    "@odata.etag": "W/\"C5625CB5\"",
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
    "Name": "HPE RESTful Root Service",
    "Oem": {
        "Hpe": {
            "@odata.context": "/redfish/v1/$metadata#HpeiLOServiceExt.HpeiLOServiceExt",
            "@odata.type": "#HpeiLOServiceExt.v2_3_0.HpeiLOServiceExt",
            "Links": {
                "ResourceDirectory": {
                    "@odata.id": "/redfish/v1/ResourceDirectory"
                }
            },
            "Manager": [
                {
                    "DefaultLanguage": "en",
                    "FQDN": null,
                    "HostName": "ILOVYRBX9UJ4S",
                    "IPManager": {
                        "BiosManaged": false,
                        "FirmwareManaged": false,
                        "ManagerProductName": "HPE OneView",
                        "ManagerType": "OneView",
                        "ManagerUrl": {
                            "xref": "https://10.29.152.124"
                        },
                        "ManagerVersion": "6.60.00",
                        "Name": "Management Console Information",
                        "OvManagesiLOIP": false,
                        "SppVersion": null,
                        "StorageManaged": false,
                        "Type": "HPQ_iLOManagerDescriptor/1.1.0",
                        "iLOManaged": true,
                        "type": "IpManagerBlob"
                    },
                    "Languages": [
                        {
                            "Language": "en",
                            "TranslationName": "English",
                            "Version": "2.55"
                        }
                    ],
                    "ManagerFirmwareVersion": "2.55",
                    "ManagerType": "iLO 5",
                    "Status": {
                        "Health": "OK"
                    }
                }
            ],
            "Moniker": {
                "ADVLIC": "iLO Advanced",
                "BMC": "iLO",
                "BSYS": "BladeSystem",
                "CLASS": "Baseboard Management Controller",
                "FEDGRP": "DEFAULT",
                "IPROV": "Intelligent Provisioning",
                "PRODABR": "iLO",
                "PRODFAM": "Integrated Lights-Out",
                "PRODGEN": "iLO 5",
                "PRODNAM": "Integrated Lights-Out 5",
                "PRODTAG": "HPE iLO 5",
                "STDLIC": "iLO Standard",
                "SUMABR": "SUM",
                "SUMGR": "Smart Update Manager",
                "SYSFAM": "ProLiant",
                "SYSMGMT": "Enhanced",
                "VENDABR": "HPE",
                "VENDNAM": "Hewlett-Packard Enterprise",
                "VNIC": "Virtual NIC",
                "WWW": "www.hpe.com",
                "WWWAHSV": "www.hpe.com/servers/ahsv",
                "WWWBMC": "www.hpe.com/servers/ilo",
                "WWWDOC": "www.hpe.com/support/ilo-docs",
                "WWWERS": "www.hpe.com/services/getconnected",
                "WWWGLIS": "www.hpe.com/glis",
                "WWWINFOSIGHT": "infosight.hpe.com",
                "WWWIOL": "www.hpe.com/info/insightonline",
                "WWWLIC": "www.hpe.com/info/ilo",
                "WWWLML": "www.hpe.com/support",
                "WWWPASS": "www.hpe.com/support/hpesc",
                "WWWPRV": "www.hpe.com/info/privacy",
                "WWWQSPEC": "www.hpe.com/info/qs",
                "WWWRESTDOC": "www.hpe.com/us/en/servers/restful-api.html",
                "WWWSUP": "www.hpe.com/support/ilo5",
                "WWWSWLIC": "www.hpe.com/software/SWLicensing"
            },
            "Sessions": {
                "CertCommonName": "ILOVYRBX9UJ4S",
                "CertificateLoginEnabled": false,
                "KerberosEnabled": false,
                "LDAPAuthLicenced": true,
                "LDAPEnabled": false,
                "LocalLoginEnabled": true,
                "LoginFailureDelay": 0,
                "LoginHint": {
                    "Hint": "POST to /Sessions to login using the following JSON object:",
                    "HintPOSTData": {
                        "Password": "password",
                        "UserName": "username"
                    }
                },
                "SecurityOverride": false,
                "ServerName": "VYRBX9UJ4S.cisco.lab"
            },
            "System": [
                {
                    "Status": {
                        "Health": "OK"
                    }
                }
            ],
            "Time": "2022-08-03T17:11:28Z"
        }
    },
    "Product": "ProLiant DL360 Gen10 Plus",
    "ProtocolFeaturesSupported": {
        "ExpandQuery": {
            "ExpandAll": false,
            "Levels": true,
            "Links": false,
            "MaxLevels": 1,
            "NoLinks": true
        },
        "FilterQuery": true,
        "OnlyMemberQuery": true,
        "SelectQuery": true
    },
    "RedfishVersion": "1.6.0",
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
    "UUID": "ca8a15fe-d0cd-5c67-80a4-1db248fde958",
    "UpdateService": {
        "@odata.id": "/redfish/v1/UpdateService"
    },
    "Vendor": "HPE"
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
- [/redfish/v1/ResourceDirectory](./UriResourceDirectory.md)
- [/redfish/v1/SessionService](./UriSessionService.md)
- [/redfish/v1/Systems](./UriSystems.md)
- [/redfish/v1/TaskService](./UriTaskService.md)
- [/redfish/v1/TelemetryService](./UriTelemetryService.md)
- [/redfish/v1/UpdateService](./UriUpdateService.md)
