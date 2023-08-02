# Application Endpoint Group (EPG)

## Command options

Filter options:
  - [name](./ApplicationEpgFilterName.md)
  - [tenant](./ApplicationEpgFilterTenant.md)
  - [application profile](./ApplicationEpgFilterProfile.md)
  - [pcTag](./ApplicationEpgFilterPcTag.md)
  - [bridge domain](./ApplicationEpgFilterBridgeDomain.md)
  - [subnet](./ApplicationEpgFilterSubnet.md)
  - [IP address](./ApplicationEpgFilterIp.md)
  - [contract](./ApplicationEpgFilterContract.md)
  - [deployed node](./ApplicationEpgFilterNode.md)
  - [domain](./ApplicationEpgFilterDomain.md)
  - [leaf policy group](./ApplicationEpgFilterPg.md)

View options:
  - [state](./ApplicationEpgViewState.md)
  - [properties](./ApplicationEpgViewProperties.md)
  - [bd](./ApplicationEpgViewBridgeDomain.md)
  - [contract](./ApplicationEpgViewContract.md)
  - [node](./ApplicationEpgViewNode.md)
  - [stport](./ApplicationEpgViewPort.md)
  - [domain](./ApplicationEpgViewDomain.md)
  - [member](./ApplicationEpgViewMember.md)
  - [fault](./ApplicationEpgViewFault.md)
  - [hfault](./ApplicationEpgViewHistoryFault.md)
  - [event](./ApplicationEpgViewEvent.md)
  - [audit](./ApplicationEpgViewAudit.md)
  - [diag](./ApplicationEpgViewDiag.md)
  - [all](./ApplicationEpgViewAll.md)
  - [verbose](./ApplicationEpgViewVerbose.md)

Output options:
  - [default](./ApplicationEpgOutputDefault.md)
  - [json](./ApplicationEpgOutputJson.md)

Command options

```
# iserver get aci epg --help

Usage: iserver.py get aci epg [OPTIONS]

  Get aci epg

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --tenant TEXT                   Filter by tenant name
  --ap TEXT                       Filter by application profile name
  --name TEXT                     Filter by epg name
  --pctag TEXT                    Filter by pcTag
  --bd TEXT                       Filter by bridge domain name
  --subnet TEXT                   Filter by IP subnet
  --address TEXT                  Filter by IP address
  --contract TEXT                 Filter by contract name
  --node TEXT                     Filter by deployed node name
  --domain TEXT                   Filter by domain name
  --member [any|dyn|st]           [default: any]
  --pg TEXT                       Filter by policy group name
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|prop|bd|contract|ep|node|stport|domai
                                  n|member|fault|hfault|event|audit|diag|all|v
                                  erbose]  [default: state]
  --pivot                         Pivot view
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 65 ms and logs saved in /tmp/iserver\999de8dc0bd8
```

[[Back]](./README.md)