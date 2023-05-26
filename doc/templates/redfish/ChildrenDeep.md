# Discovering Redfish resources references recursively

References can be discovered recursively for all resources when --deep option is defined. In such case, iserver will analyze (children) resources referenced with @odata.id recursively as long as the URI of the resource is part of the root uri defined with --uri option.

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_children.chassis_deep:iserver.output.default
```

If URI is not defined, then the default URI is '/'. In such case all references are discovered except of hard-coded URIs excluded from search defined per endpoint type.

For example UCS-C:

```
    '/redfish/v1/JsonSchemas',
    '/redfish/v1/Chassis/1/LogServices',
    '/redfish/v1/SessionService',
    '/redfish/v1/Managers/CIMC/LogServices',
    '/redfish/v1/Systems/%s/LogServices' % (system_id)
```

Example output of full search for UCS-C:

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_children.full_deep:iserver.output.default
```