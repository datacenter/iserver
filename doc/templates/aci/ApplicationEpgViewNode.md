# Application Endpoint Group (EPG)

## Get EPGs' deployed nodes properties

Use '--view node' to get deployed node properties of selected epgs
- epg name, application profile and tenant
- node properties
    - name
    - ip address
    - admin state
    - fabric state
    - model
    - serial
    - version

```
DOC_TEMPLATE:get_aci_epg.view_node:iserver.output.default
```

Use '--pivot' option to get the node specific output

```
DOC_TEMPLATE:get_aci_epg.view_node_pivot:iserver.output.default
```

Developer

```
DOC_TEMPLATE:get_aci_epg.view_node:devel.debug
```

[[Back]](./ApplicationEpg.md)