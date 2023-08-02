# Bridge Domain

## State view

Get all bridge domains from selected APIC. Default output shows properties of bridge domains as well as related objects.
- bridge domain name and tenant
- subnets with usage based on endpoints
- endpoint groups (EPG) associated with bridge domain
- Resolved VRF (tenant/name)
- associated L3 Outs (tenant/name)

```
DOC_TEMPLATE:get_aci_bd.all_default:iserver.output.default
```

Developer

```
DOC_TEMPLATE:get_aci_bd.all_default:devel.debug
```

[[Back]](./BridgeDomain.md)