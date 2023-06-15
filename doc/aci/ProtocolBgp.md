# Node Protocol

## BGP

Node selection options:
  - Instance (VRF)
    - [single node](./ProtocolBgpNode.md)
    - [selected nodes](./ProtocolBgpNodes.md)
    - [all nodes](./ProtocolBgpNodesAll.md)
  - Neighbors
    - [node](./ProtocolBgpNeighborNode.md)
    - [nodes](./ProtocolBgpNeighborNodes.md)
    - [all nodes](./ProtocolBgpNeighbors.md)

Filter options:
  - Instance
    - [vrf](./ProtocolBgpInstanceVrf.md)
  - Neighbors
    - [vrf](./ProtocolBgpNeighborVrf.md)
    - [asn](./ProtocolBgpNeighborAsn.md)
    - [router id](./ProtocolBgpNeighborRouterId.md)
    - [neighbor address](./ProtocolBgpNeighborIp.md)
    - [ibgp|ebgp](./ProtocolBgpNeighborType.md)
    - [source interface](./ProtocolBgpNeighborInterface.md)
    - [state](./ProtocolBgpNeighborState.md)

View options:
  - [default](./ProtocolBgpNeighborSummary.md)
  - [transport](./ProtocolBgpNeighborTransport.md)
  - [connection](./ProtocolBgpNeighborConnection.md)
  - [af](./ProtocolBgpNeighborAf.md)
  - [bgp routes](./ProtocolBgpRoute.md)
  - [verbose](./ProtocolBgpNeighborVerbose.md)

Output options:
  - [default](./ProtocolBgpNeighborSummary.md)
  - [json](./ProtocolBgpJson.md)

Command options

```
# iserver get aci proto bgp --help

Usage: iserver.py get aci proto bgp [OPTIONS]

  Get aci node protocol bgp

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
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
  -v, --view [default|node|vrf|trans|conn|af|verbose|route]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 69 ms and logs saved in /tmp/iserver\1ba946f39b32
```

[[Back]](./Protocol.md)