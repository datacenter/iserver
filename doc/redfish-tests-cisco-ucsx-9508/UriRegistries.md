# Resource: /api-explorer/resources/redfish/v1/Registries

Vendor | Model
--- | ---
Cisco | UCSX-9508

## /api-explorer/resources/redfish/v1/Registries

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFileCollection.MessageRegistryFileCollection",
    "@odata.id": "/redfish/v1/Registries",
    "@odata.type": "#MessageRegistryFileCollection.MessageRegistryFileCollection",
    "Description": "Registry Repository",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Registries/CiscoUcsOverallHealthStatus"
        },
        {
            "@odata.id": "/redfish/v1/Registries/CiscoUcsChassisFaults"
        },
        {
            "@odata.id": "/redfish/v1/Registries/CiscoUCS"
        },
        {
            "@odata.id": "/redfish/v1/Registries/Base"
        }
    ],
    "Members@odata.count": 4,
    "Name": "Registry File Collection"
}
```

## /api-explorer/resources/redfish/v1/Registries/Base

```{
    "@odata.context": "/redfish/v1/$metadata#Role.Role",
    "@odata.id": "/redfish/v1/Registries/Base",
    "@odata.type": "#MessageRegistryFile.v1_1_2.MessageRegistryFile",
    "Description": "Base Message Registry File locations",
    "Id": "Base",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/Oem/Cisco/Base.1.4.0.json"
        }
    ],
    "Name": "Base Message Registry file",
    "Registry": "Base.1.4"
}
```

## /api-explorer/resources/redfish/v1/Registries/CiscoUCS

```{
    "@odata.context": "/redfish/v1/$metadata#Role.Role",
    "@odata.id": "/redfish/v1/Registries/CiscoUCS",
    "@odata.type": "#MessageRegistryFile.v1_1_2.MessageRegistryFile",
    "Description": "Cisco UCS Message Registry File locations",
    "Id": "CiscoUCS",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/Oem/Cisco/CiscoUCS.v1_0_0.json"
        }
    ],
    "Name": "Cisco UCS Registry",
    "Registry": "CiscoUCS.1.0"
}
```

## /api-explorer/resources/redfish/v1/Registries/CiscoUcsChassisFaults

```{
    "@odata.context": "/redfish/v1/$metadata#Role.Role",
    "@odata.id": "/redfish/v1/Registries/CiscoUcsChassisFaults",
    "@odata.type": "#MessageRegistryFile.v1_1_2.MessageRegistryFile",
    "Description": "Faults Registry File for this system",
    "Id": "CiscoUcsChassisFaults",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/Oem/Cisco/CiscoChassisFaultCodes.v1_1_0.json"
        }
    ],
    "Name": "Faults Registry",
    "Registry": "CiscoChassisFaultCodes.1.1"
}
```

## /api-explorer/resources/redfish/v1/Registries/CiscoUcsOverallHealthStatus

```{
    "@odata.context": "/redfish/v1/$metadata#Role.Role",
    "@odata.id": "/redfish/v1/Registries/CiscoUcsOverallHealthStatus",
    "@odata.type": "#MessageRegistryFile.v1_1_2.MessageRegistryFile",
    "Description": "Overall Health Registry File for this system",
    "Id": "CiscoUcsOverallHealthStatus",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/Oem/Cisco/CiscoUcsOverallHealthStatus.v1_0_0.json"
        }
    ],
    "Name": "Overall Health Registry",
    "Registry": "CiscoUcsOverallHealthStatus.1.0"
}
```

