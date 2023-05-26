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
  --apic TEXT                  APIC name
  --ip TEXT                    APIC IP
  --username TEXT              APIC Username
  --password TEXT              APIC Password
  --name TEXT                  Filter by pool name
  --vlan TEXT                  Filter by vlan
  --domain TEXT                Filter by domain name
  -o, --output [default|json]  [default: default]
  --verbose                    Verbose output
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 26 ms and logs saved in /tmp/iserver\8e33640cdca5
```

[[Back]](./README.md)