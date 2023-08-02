# Application Profile (AP)

## Overview

- [APIC UI and CLI](./ApplicationProfileApicUi.md)

## Command options

Filter options:
  - [name](./ApplicationProfileFilterName.md)
  - [tenant](./ApplicationProfileFilterTenant.md)
  - [epg](./ApplicationProfileFilterEpg.md)

View options:
  - [state](./ApplicationProfileViewState.md)
  - [node](./ApplicationProfileViewNode.md)
  - [intf](./ApplicationProfileViewIntf.md)
  - [fault](./ApplicationProfileViewFault.md)
  - [hfault](./ApplicationProfileViewHistoryFault.md)
  - [event](./ApplicationProfileViewEvent.md)
  - [audit](./ApplicationProfileViewAudit.md)
  - [diag](./ApplicationProfileViewDiag.md)
  - [all](./ApplicationProfileViewAll.md)

Output options:
  - [default](./ApplicationProfileOutputAll.md)
  - [json](./ApplicationProfileOutputJson.md)

Command options

```
# iserver get aci ap --help

Usage: iserver.py get aci ap [OPTIONS]

  Get aci application profile

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by application profile name
  --tenant TEXT                   Filter by tenant name
  --epg TEXT                      Filter by epg name
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|node|intf|fault|hfault|event|audit|di
                                  ag|all]  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 49 ms and logs saved in /tmp/iserver\cd20f696459d
```

[[Back]](./README.md)