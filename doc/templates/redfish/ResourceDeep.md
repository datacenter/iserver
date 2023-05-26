# Get resource recursively

Resource properties can be fetched recursively when --deep option is defined. The uri value is starting or root uri from where references are discovered.

iserver shows all resources referenced with @odata.id recursively as long as the URI of the resource is part of the root uri.

Note: if --uri is not defined, the default '/' value is applied and all Redfish resources are displayed.

## Example

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_resource.event_service:iserver.output.default
```
