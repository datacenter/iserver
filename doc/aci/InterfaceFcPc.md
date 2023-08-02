# Node Interface - FcPc

## Command options

Note: Feature *should* work. No environment available to test it.

Filter options:
  - Interface ID
  - Admin State
  - Oper State

View options:
  - [state](./InterfaceFcPcViewState.md)
  - [fault](./InterfaceFcPcViewFault.md)
  - [hfault](./InterfaceFcPcViewFaultHistory.md)
  - [event](./InterfaceFcPcViewEvent.md)
  - [audit](./InterfaceFcPcViewAudit.md)
  - [diag](./InterfaceFcPcViewDiag.md)
  - [all](./InterfaceFcPcViewAll.md)

Output options:
  - [default](./InterfaceFcPcOutputDefault.md)
  - [json](./InterfaceFcPcOutputJson.md)

Command options

```
# iserver get aci intf fcpc --help

Usage: iserver.py get aci intf fcpc [OPTIONS]

  Get aci node fcpc interface

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

Info: finished in 77 ms and logs saved in /tmp/iserver\1d9d05192b15
```

[[Back]](./README.md)