# Contract Filter

## Command options

Filter options:
  - [name](./ContractFilterFilterName.md)
  - [tenant](./ContractFilterFilterTenant.md)

View options:
  - [state](./ContractFilterViewState.md)
  - [usage](./ContractFilterViewUsage.md)
  - [fault](./ContractFilterViewFault.md)
  - [hfault](./ContractFilterViewFaultHistory.md)
  - [event](./ContractFilterViewEvent.md)
  - [audit](./ContractFilterViewAudit.md)
  - [diag](./ContractFilterViewDiag.md)
  - [all](./ContractFilterViewAll.md)

Output options:
  - [default](./ContractFilterOutputDefault.md)
  - [json](./ContractFilterOutputJson.md)

Command options

```
# iserver get aci contract filter --help

Usage: iserver.py get aci contract filter [OPTIONS]

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

Info: finished in 35 ms and logs saved in /tmp/iserver\d0849c225686
```

[[Back]](./README.md)