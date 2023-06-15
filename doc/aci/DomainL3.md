# L3 Domain

Get default properties of [all](./DomainL3All.md) L3 Domains in selected APIC.

Filter options:
  - [name](./DomainL3Name.md)

Output options:
  - [default](./DomainL3All.md)
  - [json](./DomainL3OutputJson.md)

Command options

```
# iserver get aci domain l3 --help

Usage: iserver.py get aci domain l3 [OPTIONS]

  Get aci domain l3

Options:
  --apic TEXT                  APIC name
  --ip TEXT                    APIC IP
  --username TEXT              APIC Username
  --password TEXT              APIC Password
  --name TEXT                  Filter by domain name
  -o, --output [default|json]  [default: default]
  --no-cache                   Disable cache
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 48 ms and logs saved in /tmp/iserver\16d796219c39
```

[[Back]](./README.md)