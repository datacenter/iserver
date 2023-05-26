# Node Protocol - BGP

## Filter BGP neighbors by session type (ebgp|ibgp)

Use --output parameter to select neighborship attributes template
- [summary](./ProtocolBgpNeighborSummary.md)
- [transport](./ProtocolBgpNeighborTransport.md)
- [connection](./ProtocolBgpNeighborConnection.md)
- [af](./ProtocolBgpNeighborAf.md)
- [verbose](./ProtocolBgpNeighborVerbose.md)

Example: iBGP

```
DOC_TEMPLATE:get_aci_proto_bgp.ibgp:iserver.output.default
```

Example: eBGP

```
DOC_TEMPLATE:get_aci_proto_bgp.ebgp:iserver.output.default
```

[[Back]](./ProtocolBgp.md)