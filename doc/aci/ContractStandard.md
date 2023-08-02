# Standard Contract

## Command options

Filter options:
  - [name](./ContractStandardFilterName.md)
  - [tenant](./ContractStandardFilterTenant.md)

View options:
  - [state](./ContractStandardViewState.md)
  - [usage](./ContractStandardViewUsage.md)
  - [fault](./ContractStandardViewFault.md)
  - [hfault](./ContractStandardViewFaultHistory.md)
  - [event](./ContractStandardViewEvent.md)
  - [audit](./ContractStandardViewAudit.md)
  - [diag](./ContractStandardViewDiag.md)
  - [all](./ContractStandardViewAll.md)

Output options:
  - [default](./ContractStandardOutputDefault.md)
  - [json](./ContractStandardOutputJson.md)

Command options

```
# iserver get aci contract standard --help

Usage: iserver.py get aci contract standard [OPTIONS]

  Get aci contract

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by name
  --tenant TEXT                   Filter by tenant
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|usage|fault|hfault|event|audit|diag|a
                                  ll]  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 64 ms and logs saved in /tmp/iserver\f3727823f530
```

[[Back]](./README.md)