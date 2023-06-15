# L2 Domain

Get default properties of [all](./DomainL2All.md) L2 Domains in selected APIC.

Filter options:
  - [name](./DomainL2Name.md)

Output options:
  - [default](./DomainL2All.md)
  - [json](./DomainL2OutputJson.md)

Command options

```
# iserver get aci domain l2 --help

Usage: iserver.py get aci domain l2 [OPTIONS]

  Get aci domain l2

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

Info: finished in 46 ms and logs saved in /tmp/iserver\3b83b8dcc971
```

[[Back]](./README.md)