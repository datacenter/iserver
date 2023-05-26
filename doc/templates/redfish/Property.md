# Get resource properties

Redfish resource properties can be (long) list of JSON properties. If you want limited output with only few properties then you can add multiple --property parameters.

Note: iserver returns properties in JSON format so you can pipe the outcome of iserver command with iq or any other JSON parser tool to select the required properties if that's what you prefer.

## Get selected key system

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_property.system:iserver.output.default
```

## Get JSON subfields

If selected property is not top level one, use dot notation.

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_property.processor:iserver.output.default
```

If property key name contains the dot itself then follow the example for the correct command execution syntax

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_property.dotted:iserver.output.default
```
