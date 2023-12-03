# Intersight Server

## Filter by cpu

Use --cpu option to select servers based on CPU cores count. Supported values by example:
- "--cpu 28" will select servers with 28 CPU cores
- "--cpu gt28" will select servers with >28 CPU cores
- "--cpu ge28" will select servers with >=28 CPU cores
- "--cpu le28" will select servers with <=28 CPU cores
- "--cpu lt28" will select servers with <28 CPU cores
- "--cpu ne28" will select servers with !=28 CPU cores

Equal

```
DOC_TEMPLATE:get_server_filter.cpu_equal:iserver.output.default
```

Lower or Equal

```
DOC_TEMPLATE:get_server_filter.cpu_le:iserver.output.default
```

Greater or Equal

```
DOC_TEMPLATE:get_server_filter.cpu_ge:iserver.output.default
```

Developer output

```
DOC_TEMPLATE:get_server_filter.cpu_equal:devel.debug
```

[[Back]](./ServerInventory.md)