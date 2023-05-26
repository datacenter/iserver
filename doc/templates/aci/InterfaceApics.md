# Node Interface

## Multi-APIC node selection

Usage:
- define apic name as 'any' or 'all'
- define apic name in 'dom:<domain>' format where domain value is defined in [controller](./Controller.md) entries

Note:
- node name value defaults to 'any' unless defined by the user

Example:

```
DOC_TEMPLATE:get_aci_intf_mgmt.state_dom:iserver.output.default
```

[[Back]](./Interface.md)