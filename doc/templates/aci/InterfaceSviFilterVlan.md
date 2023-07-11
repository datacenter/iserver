# Node Interface - SVI

## Filter by vlan

Supported values
- integer-based: gt, ge, lt, le, start-end
- string-based: strich match or any substring

Example: range of values

```
DOC_TEMPLATE:get_aci_intf_svi.vlan_range:iserver.output.default
```

Example: string match

```
DOC_TEMPLATE:get_aci_intf_svi.vlan_match:iserver.output.default
```

Developer

```
DOC_TEMPLATE:get_aci_intf_svi.vlan_range:devel.debug
```

[[Back]](./InterfaceSvi.md)