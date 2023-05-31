# VMM Domain

Get default properties of [all](./DomainVmmAll.md) Vmm Domains in selected APIC.

Filter options:
  - [name](./DomainVmmName.md)

View options:
  - [default](./DomainVmmAll.md)
  - [prop](./DomainVmmOutputProp.md)
  - [vc](./DomainVmmOutputVc.md)

Output options:
  - [default](./DomainVmmAll.md)
  - [json](./DomainVmmOutputJson.md)

Command options

```
# iserver get aci domain vmm --help

Usage: iserver.py get aci domain vmm [OPTIONS]

  Get aci domain vmm

Options:
  --apic TEXT                   APIC name
  --ip TEXT                     APIC IP
  --username TEXT               APIC Username
  --password TEXT               APIC Password
  --name TEXT                   Filter by domain name
  -v, --view [default|prop|vc]
  -o, --output [default|json]   [default: default]
  --devel                       Developer output
  --help                        Show this message and exit.

Info: finished in 26 ms and logs saved in /tmp/iserver\bcdba560f817
```

[[Back]](./README.md)