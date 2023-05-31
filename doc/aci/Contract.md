# Contract

Get all properties of [all](./ContractAll.md) Contracts in selected APIC.

Filter options:
  - [type: standard](./ContractStandard.md)
  - [type: taboo](./ContractTaboo.md)
  - [type: contract filters](./ContractFilter.md)
  - [name](./ContractName.md)
  - [tenant](./ContractTenant.md)

View options:
  - [default](./ContractName.md)
  - [prop](./ContractOutputProp.md)
  - [usage](./ContractOutputUsage.md)

Output options:
  - [default](./ContractName.md)
  - [json](./ContractOutputJson.md)

Command options

```
# iserver get aci contract --help

Usage: iserver.py get aci contract [OPTIONS]

  Get aci contract

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by name
  --tenant TEXT                   Filter by tenant
  --type [all|standard|taboo|filter]
                                  [default: all]
  -v, --view [default|prop|usage]
  -o, --output [default|json]     [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 29 ms and logs saved in /tmp/iserver\9266472984a2
```

[[Back]](./README.md)