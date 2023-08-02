# Virtual Routing and Forwarding (VRF)

## State view

Get all vrfs from selected APIC. Default output shows main properties of vrfs as well as associated objects.
- vrf name and tenant
- policy control enforcement preference and direction
- associated EPGs
- associated bridge domains and IP subnets
- associated L3 Outs

```
DOC_TEMPLATE:get_aci_vrf.all_default:iserver.output.default
```

Developer

```
DOC_TEMPLATE:get_aci_vrf.all_default:devel.debug
```

[[Back]](./Vrf.md)