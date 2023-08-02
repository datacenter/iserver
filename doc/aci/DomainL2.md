# L2 Domain

## Overview

- [APIC UI and CLI](./DomainL2ApicUi.md)

## Command options

Filter options:
  - [domain](./DomainL2FilterName.md)
  - [aaep](./DomainL2FilterAaep.md)
  - [pool](./DomainL2FilterPool.md)
  - [vlan](./DomainL2FilterVlan.md)

View options:
  - [state](./DomainL2ViewState.md)
  - [node](./DomainL2ViewNode.md)
  - [intf](./DomainL2ViewIntf.md)
  - [vlan](./DomainL2ViewVlan.md)
  - [reln](./DomainL2ViewReln.md)
  - [fault](./DomainL2ViewFault.md)
  - [hfault](./DomainL2ViewFaultHistory.md)
  - [event](./DomainL2ViewEvent.md)
  - [audit](./DomainL2ViewAudit.md)
  - [diag](./DomainL2ViewDiag.md)
  - [all](./DomainL2ViewAll.md)

Output options:
  - [default](./DomainL2OutputDefault.md)
  - [json](./DomainL2OutputJson.md)

```
# iserver get aci domain l2 --help

Usage: iserver.py get aci domain l2 [OPTIONS]

  Get aci domain l2

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

Info: finished in 59 ms and logs saved in /tmp/iserver\bac506ce723e
```

[[Back]](./README.md)