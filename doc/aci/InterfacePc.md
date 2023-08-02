# Node Interface - Port Channel (PC)

## Command options

Filter options:
  - [Port Channel ID](./InterfacePcFilterId.md)
  - [Port Channel Name](./InterfacePcFilterName.md)
  - [VPC Domain](./InterfacePcFilterDomain.md)
  - [Speed](./InterfacePcFilterSpeed.md)
  - [State](./InterfacePcFilterState.md)

View options:
  - [state](./InterfacePcViewState.md)
  - [port](./InterfacePcViewPort.md)
  - [fault](./InterfacePcViewFault.md)
  - [hfault](./InterfacePcViewFaultHistory.md)
  - [event](./InterfacePcViewEvent.md)
  - [audit](./InterfacePcViewAudit.md)
  - [diag](./InterfacePcViewDiag.md)
  - [all](./InterfacePcViewAll.md)

Output options:
  - [default](./InterfacePcOutputDefault.md)
  - [json](./InterfacePcOutputJson.md)

Command options

```
# iserver get aci intf pc --help

Usage: iserver.py get aci intf pc [OPTIONS]

  Get aci node port channel interface

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --id TEXT                       Filter by port channel id
  --name TEXT                     Filter by name
  --speed TEXT                    Filter by speed
  --domain TEXT                   Filter by domain id
  --state [any|up|down]           Filter by state  [default: any]
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|phy|lacp|vlan|stats|fault|hfault|even
                                  t|audit|diag|all]  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 71 ms and logs saved in /tmp/iserver\4b89e88f7373
```

[[Back]](./README.md)