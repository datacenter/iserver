# Pool - VLAN

## Command options

Filter options:
  - [name](./PoolVlanFilterName.md)
  - [vlan](./PoolVlanFilterVlan.md)
  - [domain](./PoolVlanFilterDomain.md)

View options:
  - [state](./PoolVlanViewState.md)
  - [epg](./PoolVlanViewEpg.md)
  - [fault](./PoolVlanViewFault.md)
  - [hfault](./PoolVlanViewFaultHistory.md)
  - [event](./PoolVlanViewEvent.md)
  - [audit](./PoolVlanViewAudit.md)
  - [diag](./PoolVlanViewDiag.md)
  - [all](./PoolVlanViewAll.md)
  - [verbose](./PoolVlanViewVerbose.md)

Output options:
  - [default](./PoolVlanOutputDefault.md)
  - [json](./PoolVlanOutputJson.md)

Command options

```
# iserver get aci pool vlan --help

Usage: iserver.py get aci pool vlan [OPTIONS]

  Get aci pool vlan

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by pool name
  --vlan TEXT                     Filter by vlan
  --domain TEXT                   Filter by domain name
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|epg|fault|hfault|event|audit|diag|all
                                  ]  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 52 ms and logs saved in /tmp/iserver\2cac01125ccb
```

[[Back]](./README.md)