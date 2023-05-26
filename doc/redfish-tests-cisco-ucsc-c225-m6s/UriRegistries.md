# Resource: /redfish/v1/Registries

Vendor | Model
--- | ---
Cisco | UCSC-C225-M6S

## /redfish/v1/Registries

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFileCollection.MessageRegistryFileCollection",
    "@odata.id": "/redfish/v1/Registries",
    "@odata.type": "#MessageRegistryFileCollection.MessageRegistryFileCollection",
    "Description": "Registry Repository",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Registries/CiscoUcsMessageRegistry"
        },
        {
            "@odata.id": "/redfish/v1/Registries/Base"
        },
        {
            "@odata.id": "/redfish/v1/Registries/CiscoBiosAttributeRegistry.v1_0_0"
        }
    ],
    "Members@odata.count": 3,
    "Name": "Registry File Collection"
}
```

## /redfish/v1/Registries/Base

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/Base",
    "@odata.type": "#MessageRegistryFile.v1_1_1.MessageRegistryFile",
    "Description": "Base Message Registry File locations",
    "Id": "Base",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/Base/Base.1.4.0.json"
        }
    ],
    "Name": "Base Message Registry file",
    "Registry": "Base.1.4"
}
```

## /redfish/v1/Registries/CiscoBiosAttributeRegistry.v1_0_0

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/CiscoBiosAttributeRegistry.v1_0_0",
    "@odata.type": "#MessageRegistryFile.v1_1_1.MessageRegistryFile",
    "Description": "BIOS Attribute Registry File locations",
    "Id": "CiscoBiosAttributeRegistry.v1_0_0",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/CiscoBiosAttributeRegistry.v1_0_0/BiosAttributeRegistry.json"
        }
    ],
    "Name": "BIOS Attribute Registry",
    "Registry": "BiosAttributeRegistry.1.0"
}
```

## /redfish/v1/Registries/CiscoUcsMessageRegistry

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/CiscoUcsMessageRegistry",
    "@odata.type": "#MessageRegistryFile.v1_1_1.MessageRegistryFile",
    "Description": "Cisco UCS Message Registry File locations",
    "Id": "CiscoUcsMessageRegistry",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/CiscoUcsMessageRegistry/CiscoUCS.1.0.0.json"
        }
    ],
    "Name": "Cisco UCS Registry",
    "Registry": "CiscoUCS.1.0"
}
```

