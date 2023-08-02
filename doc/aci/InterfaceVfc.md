# Node Interface - VFC

## Command options

Note: Feature *should* work. No environment available to test it.

Filter options:
  - Interface ID
  - Admin State
  - Oper State

  View options:
  - [state](./InterfaceVfcViewState.md)
  - [fault](./InterfaceVfcViewFault.md)
  - [hfault](./InterfaceVfcViewFaultHistory.md)
  - [event](./InterfaceVfcViewEvent.md)
  - [audit](./InterfaceVfcViewAudit.md)
  - [diag](./InterfaceVfcViewDiag.md)
  - [all](./InterfaceVfcViewAll.md)

Output options:
  - [default](./InterfaceVfcOutputDefault.md)
  - [json](./InterfaceVfcOutputJson.md)

Command options

```
# iserver get aci intf vfc --help

Usage: iserver.py get aci intf vfc [OPTIONS]

  Get aci node vfc interface

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

Info: finished in 85 ms and logs saved in /tmp/iserver\677d7898177e
```

[[Back]](./README.md)