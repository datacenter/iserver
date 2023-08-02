# Node Interface - Fc

## Command options

Note: Feature *should* work. No environment available to test it.

Filter options:
  - Interface ID
  - Admin State
  - Oper State

View options:
  - [state](./InterfaceFcViewState.md)
  - [fault](./InterfaceFcViewFault.md)
  - [hfault](./InterfaceFcViewFaultHistory.md)
  - [event](./InterfaceFcViewEvent.md)
  - [audit](./InterfaceFcViewAudit.md)
  - [diag](./InterfaceFcViewDiag.md)
  - [all](./InterfaceFcViewAll.md)

Output options:
  - [default](./InterfaceFcOutputDefault.md)
  - [json](./InterfaceFcOutputJson.md)

Command options

```
# iserver get aci intf fc --help

Usage: iserver.py get aci intf fc [OPTIONS]

  Get aci node fc interface

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --id TEXT                       Port name
  --admin [any|up|down]           [default: any]
  --oper [any|up|down]            [default: any]
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|fault|hfault|event|audit|diag|all]
                                  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 58 ms and logs saved in /tmp/iserver\0bdee7bfb0b1
```

[[Back]](./README.md)