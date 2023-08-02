# Attachable Access Entity Profile (AAEP)

## Command options

Filter options:
  - [name](./AaepFilterName.md)

View options:
  - [state](./ProtocolAaepViewState.md)
  - [epg](./ProtocolAaepViewEpg.md)
  - [node](./ProtocolAaepViewNode.md)
  - [intf](./ProtocolAaepViewInterface.md)
  - [pol](./ProtocolAaepViewPolicy.md)
  - [fault](./ProtocolAaepViewFault.md)
  - [hfault](./ProtocolAaepViewFaultHistory.md)
  - [event](./ProtocolAaepViewEvent.md)
  - [audit](./ProtocolAaepViewAudit.md)
  - [diag](./ProtocolAaepViewDiag.md)
  - [all](./ProtocolAaepViewAll.md)

Output options:
  - [default](./AaepOutputDefault.md)
  - [json](./AaepOutputJson.md)

Command options

```
# iserver get aci aaep --help

Usage: iserver.py get aci aaep [OPTIONS]

  Get aci aaep

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by profile name
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|epg|node|intf|pol|fault|hfault|event|
                                  audit|diag|all]  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 34 ms and logs saved in /tmp/iserver\cebea96fcf0f
```

[[Back]](./README.md)