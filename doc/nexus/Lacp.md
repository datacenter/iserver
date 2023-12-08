# Link Aggregation Control Protocol (LACP)

## Command options

Filter options:
  - [id](./LldpFilterId.md)
  - [mac](./LldpFilterMac.md)

Output options:
  - [default](./LldpOutputDefault.md)
  - [json](./LldpOutputJson.md)

## Command syntax

```
# iserver get nx lacp --help

Usage: iserver.py get nx lacp [OPTIONS]

  Get lacp neighbor

Options:
  --device TEXT                Device name
  --ip TEXT                    Device IP
  --username TEXT              Device Username
  --password TEXT              Device Password
  --mac TEXT                   Filter by mac address
  -v, --view TEXT              [state]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 72 ms and logs saved in /tmp/iserver\ec477d8ea54f
```

[[Back]](./README.md)