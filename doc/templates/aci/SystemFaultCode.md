# System Fault

## Filter by fault code

Supported values
- integer-based: gt, ge, lt, le, start-end
- string-based: strich match or any substring

Example: range of values

```
DOC_TEMPLATE:get_aci_system_fault.code_range:iserver.output.default
```

Example: string match

```
DOC_TEMPLATE:get_aci_system_fault.code_match:iserver.output.default
```

Developer

```
DOC_TEMPLATE:get_aci_system_fault.code_range:devel.debug
```

[[Back]](./SystemFault.md)