# Find resource property by value

iserver supports searching for properties by value defined in multiple --value parameters with logical OR operation.

Supported value parameters (string):
- eq(value) will match case-insensitive value
- EQ(value) will match case-sensitive value
- in(sub-value) will match case-insensitive values that contain sub-value
- IN(sub-value) will match case-sensitive values that contain sub-value
- value is the same as eq(value)

Supported value parameters (numeric):
- eq(value) is == check
- gt(value) is > check
- ge(value) is >= check
- lt(value) is < check
- le(value) is <= check

Add --deep for recursive search starting with --uri.

## eq(value) or value

String

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_value.eq_ci:iserver.output.default
```

Integer

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_value.eq:iserver.output.default
```

## EQ(value)

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_value.eq_cs:iserver.output.default
```

## in()

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_value.in_ci:iserver.output.default
```

## IN()

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_value.in_cs:iserver.output.default
```

## gt()

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_value.gt:iserver.output.default
```

## ge()

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_value.ge:iserver.output.default
```

## lt()

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_value.lt:iserver.output.default
```

## le()

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_value.le:iserver.output.default
```

## Multiple values

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_value.multiple:iserver.output.default
```

## Reference

All outputs above are in the context of the System resource outputs

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_value.reference:iserver.output.default
```

## Recursive search

```
DOC_TEMPLATE:get_redfish_endpoint_ucsc_value.deep:iserver.output.default
```