# Resource: /api-explorer/resources/redfish/v1/Registries

Vendor | Model
--- | ---
Cisco | UCSX-210C-M6

## /api-explorer/resources/redfish/v1/Registries

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFileCollection.MessageRegistryFileCollection",
    "@odata.id": "/redfish/v1/Registries",
    "@odata.type": "#MessageRegistryFileCollection.MessageRegistryFileCollection",
    "Description": "Registry Repository",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Registries/Base"
        },
        {
            "@odata.id": "/redfish/v1/Registries/CiscoUCS"
        },
        {
            "@odata.id": "/redfish/v1/Registries/CiscoUcsSensorFaults"
        },
        {
            "@odata.id": "/redfish/v1/Registries/CiscoUcsHsu"
        },
        {
            "@odata.id": "/redfish/v1/Registries/CiscoUCSStorage"
        },
        {
            "@odata.id": "/redfish/v1/Registries/CiscoUcsOverallHealthStatus"
        }
    ],
    "Members@odata.count": 6,
    "Name": "Registry File Collection"
}
```

## /api-explorer/resources/redfish/v1/Registries/Base

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/Base",
    "@odata.type": "#MessageRegistryFile.v1_1_3.MessageRegistryFile",
    "Description": "Base Message Registry file locations",
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
    "Registry": "Base.1.4.0"
}
```

## /api-explorer/resources/redfish/v1/Registries/CiscoUCS

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/CiscoUCS",
    "@odata.type": "#MessageRegistryFile.v1_1_3.MessageRegistryFile",
    "Description": "Cisco UCS Message Registry File locations",
    "Id": "CiscoUCS",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/Oem/Cisco/CiscoUCS.1.0.0.json"
        }
    ],
    "Name": "Cisco UCS Registry",
    "Registry": "CiscoUCS.1.0.0"
}
```

## /api-explorer/resources/redfish/v1/Registries/CiscoUCSStorage

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/CiscoUCSStorage",
    "@odata.type": "#MessageRegistryFile.v1_1_3.MessageRegistryFile",
    "Description": "Storage Faults RegistryFile for this system",
    "Id": "CiscoUCSStorage",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/Oem/Cisco/CiscoUCSStorage.1.0.0.json"
        }
    ],
    "Name": "Storage Faults Registry",
    "Registry": "CiscoUCSStorage.1.0.0"
}
```

## /api-explorer/resources/redfish/v1/Registries/CiscoUcsHsu

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/CiscoUcsHsu",
    "@odata.type": "#MessageRegistryFile.v1_1_3.MessageRegistryFile",
    "Description": "Hsu Faults RegistryFile for this system",
    "Id": "CiscoUcsHsu",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/Oem/Cisco/CiscoUcsHsu.1.0.0.json"
        }
    ],
    "Name": "Hsu Faults Registry",
    "Registry": "CiscoUcsHsu.1.0.0"
}
```

## /api-explorer/resources/redfish/v1/Registries/CiscoUcsOverallHealthStatus

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/CiscoUcsOverallHealthStatus",
    "@odata.type": "#MessageRegistryFile.v1_1_3.MessageRegistryFile",
    "Description": "Overall Health RegistryFile for this system",
    "Id": "CiscoUcsOverallHealthStatus",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/Oem/Cisco/CiscoUcsOverallHealthStatus.1.0.0.json"
        }
    ],
    "Name": "Overall Health Registry",
    "Registry": "CiscoUcsOverallHealthStatus.1.0.0"
}
```

## /api-explorer/resources/redfish/v1/Registries/CiscoUcsSensorFaults

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/CiscoUcsSensorFaults",
    "@odata.type": "#MessageRegistryFile.v1_1_3.MessageRegistryFile",
    "Description": "Sensor Faults RegistryFile for this system",
    "Id": "CiscoUcsSensorFaults",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/Oem/Cisco/CiscoUcsSensorFaults.1.1.0.json"
        }
    ],
    "Name": "Sensor Faults Registry",
    "Registry": "CiscoUcsSensorFaults.1.1.0"
}
```

