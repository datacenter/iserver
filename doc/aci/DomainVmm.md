# VMM Domain

## Overview

- [APIC UI and CLI](./DomainVmmApicUi.md)

## Command options

Filter options:
  - [domain](./DomainVmmFilterName.md)
  - [aaep](./DomainVmmFilterAaep.md)
  - [pool](./DomainVmmFilterPool.md)
  - [vlan](./DomainVmmFilterVlan.md)

View options:
  - [state](./DomainVmmViewState.md)
  - [prop](./DomainVmmViewProp.md)
  - [vc](./DomainVmmViewVc.md)
  - [epg](./DomainVmmViewEpg.md)
  - [node](./DomainVmmViewNode.md)
  - [intf](./DomainVmmViewIntf.md)
  - [vlan](./DomainVmmViewVlan.md)
  - [reln](./DomainVmmViewReln.md)
  - [fault](./DomainVmmViewFault.md)
  - [hfault](./DomainVmmViewFaultHistory.md)
  - [event](./DomainVmmViewEvent.md)
  - [audit](./DomainVmmViewAudit.md)
  - [diag](./DomainVmmViewDiag.md)
  - [all](./DomainVmmViewAll.md)

Output options:
  - [default](./DomainVmmOutputDefault.md)
  - [json](./DomainVmmOutputJson.md)

```
# iserver get aci domain vmm --help

Usage: iserver.py get aci domain vmm [OPTIONS]

  Get aci domain vmm

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
  -v, --view TEXT                 [state|prop|vc|epg|node|intf|vlan|reln|fault
                                  |hfault|event|audit|diag|all]  [default:
                                  state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 87 ms and logs saved in /tmp/iserver\7093692e9d7d
```

[[Back]](./README.md)