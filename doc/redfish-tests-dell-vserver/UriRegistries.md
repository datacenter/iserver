# Resource: /redfish/v1/Registries

Vendor | Model
--- | ---
Dell | vServer

## /redfish/v1/Registries

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFileCollection.MessageRegistryFileCollection",
    "@odata.id": "/redfish/v1/Registries",
    "@odata.type": "#MessageRegistryFileCollection.MessageRegistryFileCollection",
    "Description": "Registry Repository",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Registries/Messages"
        },
        {
            "@odata.id": "/redfish/v1/Registries/BaseMessages"
        },
        {
            "@odata.id": "/redfish/v1/Registries/ManagerAttributeRegistry"
        },
        {
            "@odata.id": "/redfish/v1/Registries/BiosAttributeRegistry.v1_0_0"
        },
        {
            "@odata.id": "/redfish/v1/Registries/BootSourcesRegistry.v1_0_0"
        },
        {
            "@odata.id": "/redfish/v1/Registries/NetworkAttributesRegistry"
        },
        {
            "@odata.id": "/redfish/v1/Registries/ResourceEventMessageRegistry"
        }
    ],
    "Members@odata.count": 6,
    "Name": "Registry File Collection"
}
```

## /redfish/v1/Registries/BaseMessages

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/BaseMessages",
    "@odata.type": "#MessageRegistryFile.v1_1_3.MessageRegistryFile",
    "Description": "Base Message Registry File locations",
    "Id": "BaseMessages",
    "Languages": [
        "En"
    ],
    "Languages@odata.count": 1,
    "Location": [
        {
            "Language": "En",
            "PublicationUri": "https://redfish.dmtf.org/registries/v1/Base.1.8.1.json",
            "Uri": "/redfish/v1/Registries/BaseMessages/BaseRegistry.json"
        }
    ],
    "Location@odata.count": 1,
    "Name": "Base Message Registry File",
    "Registry": "Base.1.8.1"
}
```

## /redfish/v1/Registries/BiosAttributeRegistry.v1_0_0

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/BiosAttributeRegistry.v1_0_0",
    "@odata.type": "#MessageRegistryFile.v1_1_3.MessageRegistryFile",
    "Description": "BIOS Attribute Registry File locations",
    "Id": "BiosAttributeRegistry.v1_0_0",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Systems/System.Embedded.1/Bios/BiosRegistry"
        }
    ],
    "Name": "BIOS Attribute Registry File",
    "Oem": {},
    "Registry": "BiosAttributeRegistry1.0"
}
```

## /redfish/v1/Registries/BootSourcesRegistry.v1_0_0

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/BootSourcesRegistry.v1_0_0",
    "@odata.type": "#MessageRegistryFile.v1_1_3.MessageRegistryFile",
    "Description": "BootSources Attribute Registry File locations",
    "Id": "BootSourcesRegistry.v1_0_0",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Systems/System.Embedded.1/BootSources/BootSourcesRegistry"
        }
    ],
    "Name": "BootSources Attribute Registry File",
    "Oem": {},
    "Registry": "BootSourcesRegistry1.0"
}
```

## /redfish/v1/Registries/ManagerAttributeRegistry

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/ManagerAttributeRegistry",
    "@odata.type": "#MessageRegistryFile.v1_1_3.MessageRegistryFile",
    "Description": "Manager Attribute Registry File Locations",
    "Id": "ManagerAttributeRegistry",
    "Languages": [
        "En"
    ],
    "Languages@odata.count": 1,
    "Location": [
        {
            "Language": "En",
            "Uri": "/redfish/v1/Registries/ManagerAttributeRegistry/ManagerAttributeRegistry.v1_0_0.json"
        }
    ],
    "Location@odata.count": 1,
    "Name": "Manager Attribute Registry File",
    "Registry": "ManagerAttributeRegistry.1.0"
}
```

## /redfish/v1/Registries/Messages

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/Messages",
    "@odata.type": "#MessageRegistryFile.v1_1_3.MessageRegistryFile",
    "Description": "iDRAC Message Registry File locations",
    "Id": "Messages",
    "Languages": [
        "En"
    ],
    "Languages@odata.count": 1,
    "Location": [
        {
            "Language": "En",
            "Uri": "/redfish/v1/Registries/Messages/EEMIRegistry"
        }
    ],
    "Location@odata.count": 1,
    "Name": "iDRAC Message Registry File",
    "Registry": "iDRAC.1.6.1"
}
```

## /redfish/v1/Registries/NetworkAttributesRegistry

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/NetworkAttributesRegistry",
    "@odata.type": "#MessageRegistryFile.v1_1_3.MessageRegistryFile",
    "Description": "Network Attributes Registry File Locations",
    "Id": "NetworkAttributesRegistry",
    "Languages": [
        "En"
    ],
    "Languages@odata.count": 1,
    "Location": [
        {
            "Language": "En",
            "Uri": "/redfish/v1/Registries/NetworkAttributesRegistry/NetworkAttributesRegistry.json"
        }
    ],
    "Location@odata.count": 1,
    "Name": "Network Attributes Registry File",
    "Registry": "NetworkAttributeRegistry"
}
```

## /redfish/v1/Registries/ResourceEventMessageRegistry

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.id": "/redfish/v1/Registries/ResourceEventMessageRegistry",
    "@odata.type": "#MessageRegistryFile.v1_1_3.MessageRegistryFile",
    "Description": "Resource Event Registry File Locations",
    "Id": "ResourceEventMessageRegistry",
    "Languages": [
        "En"
    ],
    "Languages@odata.count": 1,
    "Location": [
        {
            "Language": "En",
            "PublicationUri": "https://redfish.dmtf.org/registries/ResourceEvent.1.0.3.json",
            "Uri": "/redfish/v1/Registries/ResourceEventMessageRegistry/ResourceEventMessageRegistry.json"
        }
    ],
    "Location@odata.count": 1,
    "Name": "Resource Event Message Registry File",
    "Registry": "ResourceEvent.1.0.3"
}
```

