# Intersight Server

## Filter by memory

Use --memory option to select servers based on total available memory. Supported values by example:
- "--memory 128" will select servers with 128 [GiB] of memory
- "--memory gt128" will select servers with >128 [GiB] of memory
- "--memory ge128" will select servers with >=128 [GiB] of memory
- "--memory le128" will select servers with <=128 [GiB] of memory
- "--memory lt128" will select servers with <128 [GiB] of memory
- "--memory ne128" will select servers with !=128 [GiB] of memory

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

Equal

```
DOC_TEMPLATE:get_server_filter.mem_equal:iserver.output.default
```

Lower or Equal

```
DOC_TEMPLATE:get_server_filter.mem_le:iserver.output.default
```

Greater or Equal

```
DOC_TEMPLATE:get_server_filter.mem_ge:iserver.output.default
```

Developer output

```
DOC_TEMPLATE:get_server_filter.mem_ge:devel.debug
```

[[Back]](./ServerInventory.md)