# Application Endpoint Group (EPG)

## Get EPGs' contract properties

Use '--view contract' to get contract properties of selected epgs
- epg name, application profile and tenant
- contracts consumed, provided and taboo

```
DOC_TEMPLATE:get_aci_epg.view_contract:iserver.output.default
```

Use '--pivot' flag to get contract specific output

```
DOC_TEMPLATE:get_aci_epg.view_contract_pivot:iserver.output.default
```

Developer

```
DOC_TEMPLATE:get_aci_epg.view_contract:devel.debug
```

[[Back]](./ApplicationEpg.md)