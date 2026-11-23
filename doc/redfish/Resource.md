# Get resource

[[Next]](./Oem.md) [[Back]](./README.md)

Get specific Redfish resource defined with --uri parameter
- full uri syntax e.g. --uri /redfish/v1/Chassis/1/NetworkAdapters 
- shortened uri syntax e.g. --uri Chassis/1/NetworkAdapters
- SYSTEM_ID value in uri is replaced with proper system-id value of the server
- all properties of the requested resource are shown in JSON format unless --property parameter is used

## Example: get network adapters resource

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Chassis/1/NetworkAdapters

/redfish/v1/Chassis/1/NetworkAdapters
-------------------------------------
{
    "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters",
    "@odata.type": "#NetworkAdapterCollection.NetworkAdapterCollection",
    "@odata.context": "/redfish/v1/$metadata#NetworkAdapterCollection.NetworkAdapterCollection",
    "Description": "Collection of NetworkAdapter resource instances for this system",
    "Name": "NetworkAdapter Collection",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/UCSC-MLOM-C25Q-04_FAA11122233"
        }
    ],
    "Members@odata.count": 1
}
```

## Example: get storage controller resource


Note: SYSTEM_ID value is replaced with proper system identifier 

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID/Storage/MRAID

/redfish/v1/Systems/FA11122233/Storage/MRAID
---------------------------------------------
{
    "@odata.id": "/redfish/v1/Systems/FA11122233/Storage/MRAID",
    "@odata.type": "#Storage.v1_8_0.Storage",
    "@odata.context": "/redfish/v1/$metadata#Storage.Storage",
    "Description": "Storage Controller",
    "Drives": [
        {
            "@odata.id": "/redfish/v1/Systems/FA11122233/Storage/MRAID/Drives/9"
        },
        {
            "@odata.id": "/redfish/v1/Systems/FA11122233/Storage/MRAID/Drives/10"
        }
    ],
    "Volumes": {
        "@odata.id": "/redfish/v1/Systems/FA11122233/Storage/MRAID/Volumes"
    },
    ...
}
```

## Example: get selected properties

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --property HostName \
    --property Model \
    --property Id

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "HostName": "My-server",
    "Model": "UCSC-C240-M5SN",
    "Id": "FA11122233"
}
```

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --property ProcessorSummary.Model \
    --property ProcessorSummary.Count

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "ProcessorSummary.Model": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
    "ProcessorSummary.Count": 2
}
```

```
# iserver get redfish uri
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems/SYSTEM_ID \
    --property "Actions.'#ComputerSystem.Reset'.'ResetType@Redfish.AllowableValues'"

/redfish/v1/Systems/FA11122233
-------------------------------
{
    "Actions.'#ComputerSystem.Reset'.'ResetType@Redfish.AllowableValues'": [
        "On",
        "ForceOff",
        "GracefulShutdown",
        "GracefulRestart",
        "ForceRestart",
        "Nmi",
        "PowerCycle"
    ]
}
```

[[Back]](./README.md)