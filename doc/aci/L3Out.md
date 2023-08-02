# L3 Out

## Command options

Filter options:
  - [name](./L3OutFilterName.md)
  - [tenant](./L3OutFilterTenant.md)
  - [vrf](./L3OutFilterVrf.md)
  - [domain](./L3OutFilterDomain.md)
  - [node](./L3OutFilterNode.md)
  - [bgp](./L3OutFilterBgp.md)
  - [eigrp](./L3OutFilterEigrp.md)
  - [ospf](./L3OutFilterOspf.md)
  - [pim](./L3OutFilterPim.md)
  - [mpls](./L3OutFilterMpls.md)

View options:
  - [state](./L3OutViewState.md)
  - [epg](./L3OutViewEpg.md)
  - [node](./L3OutViewNode.md])
  - [fault](./L3OutViewFault.md)
  - [hfault](./L3OutViewFaultHistory.md)
  - [event](./L3OutViewEvent.md)
  - [audit](./L3OutViewAudit.md)
  - [diag](./L3OutViewDiag.md)
  - [all](./L3OutViewAll.md)

Output options:
  - [default](./L3OutOutputDefault.md)
  - [json](./L3OutOutputJson.md)

Command options

```
# iserver get aci l3out --help

Usage: iserver.py get aci l3out [OPTIONS]

  Get aci l3out

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by l3out name
  --tenant TEXT                   Filter by tenant name
  --vrf TEXT                      Filter by vrf name
  --domain TEXT                   Filter by domain name
  --node TEXT                     Filter by node id
  --bgp                           Filter bgp protocol
  --eigrp                         Filter eigrp protocol
  --ospf                          Filter osfp protocol
  --pim                           Filter pim enabled
  --mpls                          Filter mpls enabled
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|epg|node|fault|hfault|event|audit|dia
                                  g|all]  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 45 ms and logs saved in /tmp/iserver\6060d8d1e074
```

[[Back]](./README.md)