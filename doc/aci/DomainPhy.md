# Physical Domain

## Overview

- [APIC UI and CLI](./DomainPhyApicUi.md)

## Command options

Filter options:
  - [domain](./DomainPhyFilterName.md)
  - [aaep](./DomainPhyFilterAaep.md)
  - [pool](./DomainPhyFilterPool.md)
  - [vlan](./DomainPhyFilterVlan.md)

View options:
  - [state](./DomainPhyViewState.md)
  - [node](./DomainPhyViewNode.md)
  - [intf](./DomainPhyViewIntf.md)
  - [vlan](./DomainPhyViewVlan.md)
  - [reln](./DomainPhyViewReln.md)
  - [fault](./DomainPhyViewFault.md)
  - [hfault](./DomainPhyViewFaultHistory.md)
  - [event](./DomainPhyViewEvent.md)
  - [audit](./DomainPhyViewAudit.md)
  - [diag](./DomainPhyViewDiag.md)
  - [all](./DomainPhyViewAll.md)

Output options:
  - [default](./DomainPhyOutputDefault.md)
  - [json](./DomainPhyOutputJson.md)

```
# iserver get aci domain phy --help

Usage: iserver.py get aci domain phy [OPTIONS]

  Get aci domain phy

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

Info: finished in 112 ms and logs saved in /tmp/iserver\f01d67a5edd0
```

[[Back]](./README.md)