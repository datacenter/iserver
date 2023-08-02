# Virtual Routing and Forwarding (VRF)

## Command options

Filter options:
  - [name](./VrfFilterName.md)
  - [tenant](./VrfFilterTenant.md)
  - [pcTag](./VrfFilterPcTag.md)
  - [vnid](./VrfFilterVnid.md)
  - [bridge domain](./VrfFilterBridgeDomain.md)
  - [epg](./VrfFilterEpg.md)
  - [subnet](./VrfFilterSubnet.md)
  - [IP address](./VrfFilterIp.md)
  - [l3out](./VrfFilterL3Out.md)

View options:
  - [state](./VrfViewState.md)
  - [properties](./VrfViewProps.md)
  - [route](./VrfViewRoute.md)
  - [node](./VrfViewNode.md)
  - [intf](./VrfViewIntf.md)
  - [fault](./VrfViewFault.md)
  - [hfault](./VrfViewFaultHistory.md)
  - [event](./VrfViewEvent.md)
  - [audit](./VrfViewAudit.md)
  - [diag](./VrfViewDiag.md)
  - [all](./VrfViewAll.md)
  - [verbose](./VrfViewVerbose.md)

Output options:
  - [default](./VrfOutputDefault.md)
  - [json](./VrfOutputJson.md)

Command options

```
# iserver get aci vrf --help

Usage: iserver.py get aci vrf [OPTIONS]

  Get aci vrfs

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     VRF name
  --tenant TEXT                   Tenant name
  --pctag TEXT                    Filter by pcTag
  --vnid TEXT                     Filter by vnid
  --bd TEXT                       Filter by bridge domain name
  --epg TEXT                      Filter by epg name
  --address TEXT                  Filter by subnet with IP
  --subnet TEXT                   Filter by subnet within subnet
  --l3out TEXT                    Filter by l3out name
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|route|prop|node|intf|fault|hfault|eve
                                  nt|audit|diag|all|verbose]  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 30 ms and logs saved in /tmp/iserver\4b5654a395a5
```

[[Back]](./README.md)