# VLAN Domain

Get default properties of [all](./PoolVlanAll.md) VLAN Pools in selected APIC.

Filter options:
  - [name](./PoolVlanName.md)
  - [vlan](./PoolVlanVlan.md)
  - [domain](./PoolVlanDomain.md)

Output options:
  - [default](./PoolVlanAll.md)
  - [json](./PoolVlanOutputJson.md)

Command options

```
# iserver get aci pool vlan --help

Usage: iserver.py get aci pool vlan [OPTIONS]

  Get aci pool vlan

Options:
  --apic TEXT                   APIC name
  --ip TEXT                     APIC IP
  --username TEXT               APIC Username
  --password TEXT               APIC Password
  --name TEXT                   Filter by pool name
  --vlan TEXT                   Filter by vlan
  --domain TEXT                 Filter by domain name
  -v, --view [default|verbose]
  -o, --output [default|json]   [default: default]
  --no-cache                    Disable cache
  --devel                       Developer output
  --help                        Show this message and exit.

Info: finished in 35 ms and logs saved in /tmp/iserver\7f6f08a4ee9c
```

[[Back]](./README.md)