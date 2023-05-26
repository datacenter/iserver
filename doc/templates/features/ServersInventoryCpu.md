# Filter by CPU cores

Use --cpu option to select servers based on CPU cores count. Supported values by example:
- "--cpu 28" will select servers with 28 CPU cores
- "--cpu gt28" will select servers with >28 CPU cores
- "--cpu ge28" will select servers with >=28 CPU cores
- "--cpu le28" will select servers with <=28 CPU cores
- "--cpu lt28" will select servers with <28 CPU cores
- "--cpu ne28" will select servers with !=28 CPU cores

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

## Equal

```
DOC_TEMPLATE:get_servers_cpu.equal:iserver.output.default
```

## Lower or Equal

```
DOC_TEMPLATE:get_servers_cpu.le:iserver.output.default
```

## Greater or Equal

```
DOC_TEMPLATE:get_servers_cpu.ge:iserver.output.default
```
