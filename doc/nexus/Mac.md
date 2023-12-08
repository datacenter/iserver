# MAC Table

## Command options

Filter options:
  - [mac](./MacFilterMac.md)
  - [vlan](./MacFilterVlan.md)

Output options:
  - [default](./MacOutputDefault.md)
  - [json](./MacOutputJson.md)

## Command syntax

```
# iserver get nx mac --help

Usage: iserver.py get nx mac [OPTIONS]

  Get mac address table mac

Options:
  --device TEXT                Device name
  --ip TEXT                    Device IP
  --username TEXT              Device Username
  --password TEXT              Device Password
  --mac TEXT                   Filter by mac address
  --vlan TEXT                  Filter by vlan
  -v, --view TEXT              [state]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 103 ms and logs saved in /tmp/iserver\bb3d08de0543
```

[[Back]](./README.md)