# L3 Domain

## Overview

- [APIC UI and CLI](./DomainL3ApicUi.md)

## Command options

Filter options:
  - [domain](./DomainL3FilterName.md)
  - [aaep](./DomainL3FilterAaep.md)
  - [pool](./DomainL3FilterPool.md)
  - [vlan](./DomainL3FilterVlan.md)

View options:
  - [state](./DomainL3ViewState.md)
  - [node](./DomainL3ViewNode.md)
  - [intf](./DomainL3ViewIntf.md)
  - [vlan](./DomainL3ViewVlan.md)
  - [reln](./DomainL3ViewReln.md)
  - [fault](./DomainL3ViewFault.md)
  - [hfault](./DomainL3ViewFaultHistory.md)
  - [event](./DomainL3ViewEvent.md)
  - [audit](./DomainL3ViewAudit.md)
  - [diag](./DomainL3ViewDiag.md)
  - [all](./DomainL3ViewAll.md)

Output options:
  - [default](./DomainL3OutputDefault.md)
  - [json](./DomainL3OutputJson.md)

```
# iserver get aci domain l3 --help

Usage: iserver.py get aci domain l3 [OPTIONS]

  Get aci domain l3

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by domain name
  --aaep TEXT                     Filter by aaep name
  --pool TEXT                     Filter by vlan pool name
  --vlan INTEGER                  Filter by vlan id
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|node|intf|vlan|reln|fault|hfault|even
                                  t|audit|diag|all]  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 106 ms and logs saved in /tmp/iserver\d1a5a36a2191
```

[[Back]](./README.md)