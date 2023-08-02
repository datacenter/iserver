# Node Protocol - BGP

## Command options

Filter options:
  - [asn](./ProtocolBgpFilterAsn.md)
  - [vrf](./ProtocolBgpFilterVrf.md)
  - [router id](./ProtocolBgpFilterRouterId.md)
  - [neighbor address](./ProtocolBgpFilterIp.md)
  - [ibgp|ebgp](./ProtocolBgpFilterType.md)
  - [source interface](./ProtocolBgpFilterInterface.md)
  - [state](./ProtocolBgpFilterState.md)

View options:
  - [inst](./ProtocolBgpViewInstance.md)
  - [dom](./ProtocolBgpViewDomain.md)
  - [nei](./ProtocolBgpViewNeighbor.md)
  - [route](./ProtocolBgpViewRoute.md)
  - [fault](./ProtocolBgpViewFault.md)
  - [hfault](./ProtocolBgpViewFaultHistory.md)
  - [event](./ProtocolBgpViewEvent.md)
  - [diag](./ProtocolBgpViewDiag.md)
  - [all](./ProtocolBgpViewAll.md)

Output options:
  - [default](./ProtocolBgpOutputDefault.md)
  - [json](./ProtocolBgpOutputJson.md)

Command options

```
# iserver get aci proto bgp --help

Usage: iserver.py get aci proto bgp [OPTIONS]

  Get aci node protocol bgp

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --asn TEXT                      Filter by BGP ASN
  --vrf TEXT                      Filter by VRF name
  --rtr-ip TEXT                   Filter by BGP Router IP address
  --rtr-subnet TEXT               Filter by BGP Router IP subnet
  --type [any|ibgp|ebgp]          Filter by BGP neighbor type  [default: any]
  --nbr-ip TEXT                   Filter by BPG Neighbor IP address
  --nbr-subnet TEXT               Filter by BPG Neighbor IP subnet
  --state [any|up|down]           Filter by BGP neighbor state  [default: any]
  --intf TEXT                     Filter by BGP Neighbor source interface
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [inst|dom|nei|route|fault|hfault|event|diag|
                                  all]  [default: nei]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 33 ms and logs saved in /tmp/iserver\659835208b3a
```

[[Back]](./README.md)