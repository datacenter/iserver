# Node Interface - MACsec

## Command options

Filter options:
  - [Interface ID](./InterfaceMacSecFilterId.md)

View options:
  - [state](./InterfaceMacSecViewState.md)
  - [fault](./InterfaceMacSecViewFault.md)
  - [hfault](./InterfaceMacSecViewFaultHistory.md)
  - [event](./InterfaceMacSecViewEvent.md)
  - [audit](./InterfaceMacSecViewAudit.md)
  - [diag](./InterfaceMacSecViewDiag.md)
  - [all](./InterfaceMacSecViewAll.md)
  - [verbose](./InterfaceMacSecViewVerbose.md)

Output options:
  - [default](./InterfaceMacSecOutputDefault.md)
  - [json](./InterfaceMacSecOutputJson.md)

Command options

```
# iserver get aci intf macsec --help

Usage: iserver.py get aci intf macsec [OPTIONS]

  Get aci node macsec interface

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
  --type [any|leaf|fabric]        [default: any]
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|fault|hfault|event|audit|diag|all|ver
                                  bose]  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 65 ms and logs saved in /tmp/iserver\498cf2964cb2
```

[[Back]](./README.md)