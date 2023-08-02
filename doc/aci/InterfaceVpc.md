# Node Interface - Virtual Port Channel (VPC)

## Command options

Filter options:
  - [Domain ID](./InterfaceVpcFilterId.md)
  - [Peer state](./InterfaceVpcFilterState.md)
  - [Members state](./InterfaceVpcFilterMember.md)

View options:
  - [state](./InterfaceVpcViewState.md)
  - [addr](./InterfaceVpcViewAddr.md)
  - [member](./InterfaceVpcViewMember.md)
  - [vlan](./InterfaceVpcViewVlan.md)
  - [fault](./InterfaceVpcViewFault.md)
  - [hfault](./InterfaceVpcViewFaultHistory.md)
  - [event](./InterfaceVpcViewEvent.md)
  - [audit](./InterfaceVpcViewAudit.md)
  - [diag](./InterfaceVpcViewDiag.md)
  - [all](./InterfaceVpcViewAll.md)

Output options:
  - [default](./InterfaceVpcOutputDefault.md)
  - [json](./InterfaceVpcOutputJson.md)

Command options

```
# iserver get aci intf vpc --help

Usage: iserver.py get aci intf vpc [OPTIONS]

  Get aci node virtual port channel interface

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --id TEXT                       Filter by vpc domain id
  --state [any|up|down]           [default: any]
  --member [any|up|down]          [default: any]
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|addr|member|vlan|fault|hfault|event|a
                                  udit|diag|all]  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 42 ms and logs saved in /tmp/iserver\9e700b0c7565
```

[[Back]](./README.md)