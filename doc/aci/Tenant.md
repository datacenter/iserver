# Tenant

## Command options

Filter options:
  - [name](./TenantFilterName.md)

View options:
  - [state](./TenantViewState.md)
  - [count](./TenantViewCount.md)
  - [fault](./TenantViewFault.md)
  - [hfault](./TenantViewFaultHistory.md)
  - [event](./TenantViewEvent.md)
  - [audit](./TenantViewAudit.md)
  - [diag](./TenantViewDiag.md)
  - [all](./TenantViewAll.md)

Output options:
  - [default](./TenantOutputDefault.md)
  - [json](./TenantOutputJson.md)

Command options

```
# iserver get aci tenant --help

Usage: iserver.py get aci tenant [OPTIONS]

  Get aci tenant

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by tenant name
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|count|fault|hfault|event|audit|diag|a
                                  ll]  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 125 ms and logs saved in /tmp/iserver\67635a81a41f
```

[[Back]](./README.md)