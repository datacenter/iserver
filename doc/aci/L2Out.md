# L2 Out

Get default properties of [all](./L2OutAll.md) L2Outs in selected APIC.

Filter options:
  - [name](./L2OutName.md)
  - [tenant](./L2OutTenant.md)

Output options:
  - [default](./L2OutAll.md)
  - [json](./L2OutJson.md)

Command options

```
# iserver get aci l2out --help

Usage: iserver.py get aci l2out [OPTIONS]

  Get aci l2out

Options:
  --apic TEXT                  APIC name
  --ip TEXT                    APIC IP
  --username TEXT              APIC Username
  --password TEXT              APIC Password
  --name TEXT                  Filter by application profile name
  --tenant TEXT                Filter by tenant name
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 34 ms and logs saved in /tmp/iserver\9d62c0ca2d37
```

[[Back]](./README.md)