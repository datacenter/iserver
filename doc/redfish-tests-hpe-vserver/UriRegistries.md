# Resource: /redfish/v1/Registries

Vendor | Model
--- | ---
HPE | vServer

## /redfish/v1/Registries

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFileCollection.MessageRegistryFileCollection",
    "@odata.etag": "W/\"21C260DB\"",
    "@odata.id": "/redfish/v1/Registries",
    "@odata.type": "#MessageRegistryFileCollection.MessageRegistryFileCollection",
    "Description": "Registry Repository",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Registries/Base"
        },
        {
            "@odata.id": "/redfish/v1/Registries/HpeCommon"
        },
        {
            "@odata.id": "/redfish/v1/Registries/HpeDcpmmDiags"
        },
        {
            "@odata.id": "/redfish/v1/Registries/iLO"
        },
        {
            "@odata.id": "/redfish/v1/Registries/iLOeRS"
        },
        {
            "@odata.id": "/redfish/v1/Registries/iLOEvents"
        },
        {
            "@odata.id": "/redfish/v1/Registries/TaskEvent"
        },
        {
            "@odata.id": "/redfish/v1/Registries/%23SUTReg.v2_5_6.SUTReg"
        },
        {
            "@odata.id": "/redfish/v1/Registries/BiosAttributeRegistryU46.v1_1_56"
        },
        {
            "@odata.id": "/redfish/v1/Registries/HpeBiosMessageRegistry.v1_0_0"
        }
    ],
    "Members@odata.count": 10,
    "Name": "Registry File Repository"
}
```

## /redfish/v1/Registries/%23SUTReg.v2_5_6.SUTReg

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.etag": "W/\"AF7524D0\"",
    "@odata.id": "/redfish/v1/Registries/%23SUTReg.v2_5_6.SUTReg",
    "@odata.type": "#MessageRegistryFile.v1_0_4.MessageRegistryFile",
    "Description": "Registry Definition File for #SUTReg.v2_5_6.SUTReg",
    "Id": "%23SUTReg.v2_5_6.SUTReg",
    "Languages": [
        "en",
        "jp"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/registrystore/registries/en/sutreg.v2_5_6.sutreg"
        },
        {
            "Language": "jp",
            "Uri": "/redfish/v1/registrystore/registries/jp/sutreg.v2_5_6.sutreg"
        }
    ],
    "Name": "#SUTReg.v2_5_6.SUTReg Message Registry File",
    "Registry": "#SUTReg.v2_5_6.SUTReg"
}
```

## /redfish/v1/Registries/Base

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.etag": "W/\"0DCA67A0\"",
    "@odata.id": "/redfish/v1/Registries/Base",
    "@odata.type": "#MessageRegistryFile.v1_0_4.MessageRegistryFile",
    "Description": "Registry Definition File for Base",
    "Id": "Base",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/RegistryStore/registries/en/Base.json"
        }
    ],
    "Name": "Base Message Registry File",
    "Registry": "Base.1.4.0"
}
```

## /redfish/v1/Registries/BiosAttributeRegistryU46.v1_1_56

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.etag": "W/\"E9317232\"",
    "@odata.id": "/redfish/v1/Registries/BiosAttributeRegistryU46.v1_1_56",
    "@odata.type": "#MessageRegistryFile.v1_0_4.MessageRegistryFile",
    "Description": "Registry Definition File for BiosAttributeRegistryU46.v1_1_56",
    "Id": "BiosAttributeRegistryU46.v1_1_56",
    "Languages": [
        "en",
        "ja",
        "zh"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/registrystore/registries/en/biosattributeregistryu46.v1_1_56"
        },
        {
            "Language": "ja",
            "Uri": "/redfish/v1/registrystore/registries/ja/biosattributeregistryu46.v1_1_56"
        },
        {
            "Language": "zh",
            "Uri": "/redfish/v1/registrystore/registries/zh/biosattributeregistryu46.v1_1_56"
        }
    ],
    "Name": "BiosAttributeRegistryU46.v1_1_56 Message Registry File",
    "Registry": "BiosAttributeRegistryU46.v1_1_56"
}
```

## /redfish/v1/Registries/HpeBiosMessageRegistry.v1_0_0

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.etag": "W/\"F9F90F59\"",
    "@odata.id": "/redfish/v1/Registries/HpeBiosMessageRegistry.v1_0_0",
    "@odata.type": "#MessageRegistryFile.v1_0_4.MessageRegistryFile",
    "Description": "Registry Definition File for HpeBiosMessageRegistry.v1_0_0",
    "Id": "HpeBiosMessageRegistry.v1_0_0",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/registrystore/registries/en/hpebiosmessageregistry.v1_0_0"
        }
    ],
    "Name": "HpeBiosMessageRegistry.v1_0_0 Message Registry File",
    "Registry": "HpeBiosMessageRegistry.v1_0_0"
}
```

## /redfish/v1/Registries/HpeCommon

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.etag": "W/\"51CD97AE\"",
    "@odata.id": "/redfish/v1/Registries/HpeCommon",
    "@odata.type": "#MessageRegistryFile.v1_0_4.MessageRegistryFile",
    "Description": "Registry Definition File for HpeCommon",
    "Id": "HpeCommon",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/RegistryStore/registries/en/HpeCommon.json"
        }
    ],
    "Name": "HpeCommon Message Registry File",
    "Registry": "HpeCommon.2.0.0"
}
```

## /redfish/v1/Registries/HpeDcpmmDiags

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.etag": "W/\"59C1F74B\"",
    "@odata.id": "/redfish/v1/Registries/HpeDcpmmDiags",
    "@odata.type": "#MessageRegistryFile.v1_0_4.MessageRegistryFile",
    "Description": "Registry Definition File for HpeDcpmmDiags",
    "Id": "HpeDcpmmDiags",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/RegistryStore/registries/en/HpeDcpmmDiags.json"
        }
    ],
    "Name": "HpeDcpmmDiags Message Registry File",
    "Registry": "HpeDcpmmDiags.1.0.0"
}
```

## /redfish/v1/Registries/TaskEvent

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.etag": "W/\"AAC2D8F6\"",
    "@odata.id": "/redfish/v1/Registries/TaskEvent",
    "@odata.type": "#MessageRegistryFile.v1_0_4.MessageRegistryFile",
    "Description": "Registry Definition File for TaskEvent",
    "Id": "TaskEvent",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/RegistryStore/registries/en/TaskEvent.json"
        }
    ],
    "Name": "TaskEvent Message Registry File",
    "Registry": "TaskEvent.1.0.0"
}
```

## /redfish/v1/Registries/iLO

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.etag": "W/\"4F6B5DE7\"",
    "@odata.id": "/redfish/v1/Registries/iLO",
    "@odata.type": "#MessageRegistryFile.v1_0_4.MessageRegistryFile",
    "Description": "Registry Definition File for iLO",
    "Id": "iLO",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/RegistryStore/registries/en/iLO.json"
        }
    ],
    "Name": "iLO Message Registry File",
    "Registry": "iLO.2.14.0"
}
```

## /redfish/v1/Registries/iLOEvents

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.etag": "W/\"D0E7E926\"",
    "@odata.id": "/redfish/v1/Registries/iLOEvents",
    "@odata.type": "#MessageRegistryFile.v1_0_4.MessageRegistryFile",
    "Description": "Registry Definition File for iLOEvents",
    "Id": "iLOEvents",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/RegistryStore/registries/en/iLOEvents.json"
        }
    ],
    "Name": "iLOEvents Message Registry File",
    "Registry": "iLOEvents.2.3.0"
}
```

## /redfish/v1/Registries/iLOeRS

```{
    "@odata.context": "/redfish/v1/$metadata#MessageRegistryFile.MessageRegistryFile",
    "@odata.etag": "W/\"2C6F4D05\"",
    "@odata.id": "/redfish/v1/Registries/iLOeRS",
    "@odata.type": "#MessageRegistryFile.v1_0_4.MessageRegistryFile",
    "Description": "Registry Definition File for iLOeRS",
    "Id": "iLOeRS",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/RegistryStore/registries/en/iLOeRS.json"
        }
    ],
    "Name": "iLOeRS Message Registry File",
    "Registry": "iLOeRS.1.0.0"
}
```

