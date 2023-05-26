# Discovering Redfish resource references

Redfish resource identified with URI may contain references to other resources using @odata.id property e.g.,

```
"@odata.id": "/redfish/v1/Chassis/1/PCIeDevices",
"@odata.type": "#PCIeDeviceCollection.PCIeDeviceCollection",
"@odata.context": "/redfish/v1/$metadata#PCIeDeviceCollection.PCIeDeviceCollection",
"Description": "Collection of PCIeDevice resource instances for this system",
"Name": "PCIeDevice Collection",
"Members": [
    {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MRAID"
    },
    {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/MLOM"
    },
    {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/3"
    },
    {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/6"
    },
    {
        "@odata.id": "/redfish/v1/Chassis/1/PCIeDevices/L"
    }
],
"Members@odata.count": 5
```

iserver supports discovering the references in Redfish resource using --children option. iserver will get Redfish resouce identified with URI, analyze the JSON structure searching for @odata.id.

References can be discovered recursively when --deep option is defined. Check [here](./ChildrenDeep.md) for more details.

## Top level references

If --path is not specified, top level references are shown.

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_children.top:iserver.output.default
```

## Selected resource references

If URI is defined, referces are shown for the selected resource.

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_children.system:iserver.output.default
```
