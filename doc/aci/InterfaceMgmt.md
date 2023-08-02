# Node Interface - Management

## Command options

View options:
  - [state](./InterfaceMgmtViewState.md)
  - [addr](./InterfaceMgmtViewAddr.md)
  - [nei](./InterfaceMgmtViewNei.md)
  - [fault](./InterfaceMgmtViewFault.md)
  - [hfault](./InterfaceMgmtViewFaultHistory.md)
  - [event](./InterfaceMgmtViewEvent.md)
  - [audit](./InterfaceMgmtViewAudit.md)
  - [diag](./InterfaceMgmtViewDiag.md)
  - [all](./InterfaceMgmtViewAll.md)

Output options:
  - [default](./InterfaceMgmtOutputDefault.md)
  - [json](./InterfaceMgmtOutputJson.md)

Command options

```
# iserver get aci intf mgmt --help

Usage: iserver.py get aci intf mgmt [OPTIONS]

  Get aci node management interface

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|addr|nei|fault|hfault|event|audit|dia
                                  g|all]  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 29 ms and logs saved in /tmp/iserver\a2741115215f
```

[[Back]](./README.md)