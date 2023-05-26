# Find resource property by key

iserver supports searching getting selected properties by using --property parameter. Check [here](./Property.md) for more details.

In case you know the property name but you are not sure the resource URI. Or maybe you are not even sure the exact property name, then --key parameter with --deep option might be very useful.

iserver supports multiple --key parameters with logical OR operation.

Supported key parameter value:
- eq(value) will match case-insensitive properties with name value
- EQ(value) will match case-sensitive properties with name value
- in(value) will match case-insensitive properties that contain value
- IN(value) will match case-sensitive properties that contain value
- value is the same as eq(value)

Add --deep for recursive search starting with --uri.

## eq()

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_key.eq_ci:iserver.output.default
```

## EQ()

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_key.eq_cs:iserver.output.default
```

## in()

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_key.in_ci:iserver.output.default
```

## IN()

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_key.in_cs:iserver.output.default
```

## Recursive search

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_key.deep:iserver.output.default
```