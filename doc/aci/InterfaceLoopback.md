# Node Interface - Loopback

## Command options

Filter options:
  - [Interface ID](./InterfaceLoopbackFilterId.md)
  - [IP](./InterfaceLoopbackFilterIp.md)
  - [Subnet](./InterfaceLoopbackFilterSubnet.md)

View options:
  - [state](./InterfaceLoopbackViewState.md)
  - [fault](./InterfaceLoopbackViewFault.md)
  - [hfault](./InterfaceLoopbackViewFaultHistory.md)
  - [event](./InterfaceLoopbackViewEvent.md)
  - [audit](./InterfaceLoopbackViewAudit.md)
  - [diag](./InterfaceLoopbackViewDiag.md)
  - [all](./InterfaceLoopbackViewAll.md)


Output options:
  - [default](./InterfaceLoopbackOutputDefault.md)
  - [json](./InterfaceLoopbackOutputJson.md)

Command options

```
# iserver get aci intf lb --help

Usage: iserver.py get aci intf lb [OPTIONS]

  Get aci node loobpack interface

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
  --address TEXT                  Filter by IP
  --subnet TEXT                   Filter by subnet
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

Info: finished in 65 ms and logs saved in /tmp/iserver\39f36d3a95aa
```

[[Back]](./README.md)