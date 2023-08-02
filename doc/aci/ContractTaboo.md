# Taboo Contract

## Command options

Filter options:
  - [name](./ContractTabooFilterName.md)
  - [tenant](./ContractTabooFilterTenant.md)

View options:
  - [state](./ContractTabooViewState.md)
  - [usage](./ContractTabooViewUsage.md)
  - [fault](./ContractTabooViewFault.md)
  - [hfault](./ContractTabooViewFaultHistory.md)
  - [event](./ContractTabooViewEvent.md)
  - [audit](./ContractTabooViewAudit.md)
  - [diag](./ContractTabooViewDiag.md)
  - [all](./ContractTabooViewAll.md)

Output options:
  - [default](./ContractTabooOutputDefault.md)
  - [json](./ContractTabooOutputJson.md)

Command options

```
# iserver get aci contract taboo --help

Usage: iserver.py get aci contract taboo [OPTIONS]

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

Info: finished in 33 ms and logs saved in /tmp/iserver\645611a08f5a
```

[[Back]](./README.md)