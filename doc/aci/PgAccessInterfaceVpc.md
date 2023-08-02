# Policy Group - Access Interface - Leaf Access PC/VPC

## Command options

Filter options:
  - [name](./PgAccessInterfaceVpcFilterName.md)
  - [aaep](./PgAccessInterfaceVpcFilterAaep.md)

View options:
  - [state](./PgAccessInterfaceVpcViewState.md)
  - [aaep](./PgAccessInterfaceVpcViewAaep.md)
  - [node](./PgAccessInterfaceVpcViewNode.md)
  - [intf](./PgAccessInterfaceVpcViewIntf.md)
  - [fault](./PgAccessInterfaceVpcViewFault.md)
  - [hfault](./PgAccessInterfaceVpcViewFaultHistory.md)
  - [event](./PgAccessInterfaceVpcViewEvent.md)
  - [audit](./PgAccessInterfaceVpcViewAudit.md)
  - [diag](./PgAccessInterfaceVpcViewDiag.md)
  - [all](./PgAccessInterfaceVpcViewAll.md)

Output options:
  - [default](./PgAccessInterfaceVpcOutputDefault.md)
  - [json](./PgAccessInterfaceVpcOutputJson.md)

Command options

```
# iserver get aci pg access intf port --help

Usage: iserver.py get aci pg access intf port [OPTIONS]

  Get aci policy group interface port

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by name
  --aaep TEXT                     Filter by aaep
  --policy TEXT                   Filter by policy
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|aaep|node|intf|vlan|fault|hfault|even
                                  t|audit|diag|all]  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 109 ms and logs saved in /tmp/iserver\e70caee34095
```

[[Back]](./PgAccessInterface.md)