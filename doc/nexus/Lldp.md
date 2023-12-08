# Link Layer Discovery Protocol (LLDP)

## Command options

Filter options:
  - [id](./LldpFilterId.md)
  - [mac](./LldpFilterMac.md)

Output options:
  - [default](./LldpOutputDefault.md)
  - [json](./LldpOutputJson.md)

## Command syntax

```
# iserver get nx lldp --help

Usage: iserver.py get nx lldp [OPTIONS]

  Get lldp neighbor

Options:
  --device TEXT                Device name
  --ip TEXT                    Device IP
  --username TEXT              Device Username
  --password TEXT              Device Password
  --id TEXT                    Filter neighbor by device id
  --mac TEXT                   Filter neighbor by mac address
  -v, --view TEXT              [state]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 36 ms and logs saved in /tmp/iserver\cb29976a113d
```

[[Back]](./README.md)