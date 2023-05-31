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
DOC_TEMPLATE:get_aci_proto_bgp.help:output
```

[[Back]](./Protocol.md)