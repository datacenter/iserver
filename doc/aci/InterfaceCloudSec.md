# Node Interface - CloudSec

## Command options

Note: Feature *should* work. No environment available to test it.

Filter options:
  - Interface ID
  - Admin State
  - Oper State

View options:
  - [state](./InterfaceCloudSecViewState.md)
  - [fault](./InterfaceCloudSecViewFault.md)
  - [hfault](./InterfaceCloudSecViewFaultHistory.md)
  - [event](./InterfaceCloudSecViewEvent.md)
  - [audit](./InterfaceCloudSecViewAudit.md)
  - [diag](./InterfaceCloudSecViewDiag.md)
  - [all](./InterfaceCloudSecViewAll.md)

Output options:
  - [default](./InterfaceCloudSecOutputDefault.md)
  - [json](./InterfaceCloudSecOutputJson.md)

Command options

```
# iserver get aci intf cloudsec --help

Usage: iserver.py get aci intf cloudsec [OPTIONS]

  Get aci node cloudsec interface

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

Info: finished in 57 ms and logs saved in /tmp/iserver\e425062a3b56
```

[[Back]](./README.md)