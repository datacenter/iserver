# Intersight Server

## Filter by psu

Supported filtering rules:
- state:on selects servers with at least one psu on
- state:off selects servers with at least one psu off
- serial:pattern selects servers with psu serial number matching pattern
- model:pattern selects servers with psu serial number matching model

Multiple psu filters follow AND logic.

Select psu off

```
DOC_TEMPLATE:get_server_filter.psu_off:iserver.output.default
```

Select psu serial

```
DOC_TEMPLATE:get_server_filter.psu_serial:iserver.output.default
```

Select psu model

```
DOC_TEMPLATE:get_server_filter.psu_model:iserver.output.default
```

Select psu model and serial

```
DOC_TEMPLATE:get_server_filter.psu_model_and_serial:iserver.output.default
```

Developer output

```
DOC_TEMPLATE:get_server_filter.psu_off:devel.debug
```

[[Back]](./ServerInventory.md)