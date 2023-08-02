# Node Interface - Encapsulated Routed

## Command options

Filter options:
  - [Interface ID](./InterfaceL3eFilterId.md)
  - [Oper State](./InterfaceL3eFilterState.md)

View options:
  - [state](./InterfaceL3eViewState.md)
  - [fault](./InterfaceL3eViewFault.md)
  - [hfault](./InterfaceL3eViewFaultHistory.md)
  - [event](./InterfaceL3eViewEvent.md)
  - [audit](./InterfaceL3eViewAudit.md)
  - [diag](./InterfaceL3eViewDiag.md)
  - [all](./InterfaceL3eViewAll.md)

Output options:
  - [default](./InterfaceL3eOutputDefault.md)
  - [json](./InterfaceL3eOutputJson.md)

Command options

```
# iserver get aci intf l3e --help

Usage: iserver.py get aci intf l3e [OPTIONS]

  Get aci node encapsulated routed interface

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

Info: finished in 65 ms and logs saved in /tmp/iserver\3382ebc12879
```

[[Back]](./README.md)