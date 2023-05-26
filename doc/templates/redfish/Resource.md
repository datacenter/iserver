# Get resource

Resources in Redfish are defined with URI (link) typically starting with /redfish/v1/.

iserver supports full uri syntax e.g. /redfish/v1/Chassis/1/NetworkAdapters as well as shortened syntax e.g. Chassis/1/NetworkAdapters.

All properties of the requested resource are shown in JSON format.

Note: Resource properties can be fetched recursively when --deep option is defined. Check [here](./ResourceDeep.md) for more details.

## Get network adapters resource

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_resource.network:iserver.output.default
```

## Get storage controller resource

Depending on endpoint type, URI may contain system identifier value that is device specific. iserver supports uri syntax with SYSTEM_ID value that will be automatically replaced with proper system identifier.

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_resource.storage:iserver.output.default
```