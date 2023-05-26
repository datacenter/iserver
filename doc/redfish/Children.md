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
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --children

Redfish resource references: /redfish/v1/
-----------------------------------------
/redfish/v1/AccountService
/redfish/v1/CertificateService
/redfish/v1/Chassis
/redfish/v1/EventService
/redfish/v1/Fabrics
/redfish/v1/JsonSchemas
/redfish/v1/Managers
/redfish/v1/Registries
/redfish/v1/SessionService
/redfish/v1/SessionService/Sessions
/redfish/v1/Systems
/redfish/v1/TaskService
/redfish/v1/UpdateService
```

## Selected resource references

If URI is defined, referces are shown for the selected resource.

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --children

Redfish resource references: /redfish/v1/Systems/WZP23400AK4
------------------------------------------------------------
/redfish/v1/Chassis/1
/redfish/v1/Chassis/1/Power
/redfish/v1/Chassis/1/Thermal
/redfish/v1/Managers/CIMC
/redfish/v1/Systems/WZP23400AK4/Bios
/redfish/v1/Systems/WZP23400AK4/EthernetInterfaces
/redfish/v1/Systems/WZP23400AK4/LogServices
/redfish/v1/Systems/WZP23400AK4/Memory
/redfish/v1/Systems/WZP23400AK4/MemoryDomains
/redfish/v1/Systems/WZP23400AK4/NetworkInterfaces
/redfish/v1/Systems/WZP23400AK4/PCIeDevices/3
/redfish/v1/Systems/WZP23400AK4/PCIeDevices/3/PCIeFunctions/3
/redfish/v1/Systems/WZP23400AK4/PCIeDevices/6
/redfish/v1/Systems/WZP23400AK4/PCIeDevices/6/PCIeFunctions/6
/redfish/v1/Systems/WZP23400AK4/PCIeDevices/L
/redfish/v1/Systems/WZP23400AK4/PCIeDevices/L/PCIeFunctions/L
/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MLOM
/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MLOM/PCIeFunctions/MLOM
/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MRAID
/redfish/v1/Systems/WZP23400AK4/PCIeDevices/MRAID/PCIeFunctions/MRAID
/redfish/v1/Systems/WZP23400AK4/Processors
/redfish/v1/Systems/WZP23400AK4/SecureBoot
/redfish/v1/Systems/WZP23400AK4/SimpleStorage
/redfish/v1/Systems/WZP23400AK4/Storage
```
