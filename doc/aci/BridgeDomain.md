# Bridge Domain (BD)

## Command options

Filter options:
  - [name](./BridgeDomainFilterName.md)
  - [tenant](./BridgeDomainFilterTenant.md)
  - [vrf](./BridgeDomainFilterVrf.md)
  - [epg](./BridgeDomainFilterEpg.md)
  - [subnet](./BridgeDomainFilterSubnet.md)
  - [IP address](./BridgeDomainFilterIp.md)
  - [l3out](./BridgeDomainFilterL3Out.md)

View options:
  - [state](./BridgeDomainViewState.md)
  - [l2](./BridgeDomainViewL2.md)
  - [l3](./BridgeDomainViewL3.md)
  - [mcast](./BridgeDomainViewMcast.md)
  - [vrf](./BridgeDomainViewVrf.md)
  - [node](./BridgeDomainViewNode.md)
  - [intf](./BridgeDomainViewIntf.md)
  - [fault](./BridgeDomainViewFault.md)
  - [hfault](./BridgeDomainViewHistoryFault.md)
  - [event](./BridgeDomainViewEvent.md)
  - [audit](./BridgeDomainViewAudit.md)
  - [diag](./BridgeDomainViewDiag.md)
  - [all](./BridgeDomainViewAll.md)
  - [verbose](./BridgeDomainViewVerbose.md)

Output options:
  - [default](./BridgeDomainAllDefault.md)
  - [json](./BridgeDomainJson.md)

Command options

```
# iserver get aci bd --help

Usage: iserver.py get aci bd [OPTIONS]

  Get aci bridge domain

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by bridge domain name
  --tenant TEXT                   Filter by tenant name
  --vrf TEXT                      Filter by vrf name
  --epg TEXT                      Filter by epg name
  --address TEXT                  Filter by subnet with IP
  --subnet TEXT                   Filter by subnet within subnet
  --l3out TEXT                    Filter by l3out name
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|l2|l3|mcast|vrf|node|intf|fault|hfaul
                                  t|event|audit|diag|all|verbose]  [default:
                                  state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 80 ms and logs saved in /tmp/iserver\f856f3fa1730
```

[[Back]](./README.md)