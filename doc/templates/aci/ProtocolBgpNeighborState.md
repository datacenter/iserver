# Node Protocol - BGP

## Filter BGP neighbors by state (established|idle)

Use --output parameter to select neighborship attributes template
- [summary](./ProtocolBgpNeighborSummary.md)
- [transport](./ProtocolBgpNeighborTransport.md)
- [connection](./ProtocolBgpNeighborConnection.md)
- [af](./ProtocolBgpNeighborAf.md)
- [verbose](./ProtocolBgpNeighborVerbose.md)

Example: established (up)

```
DOC_TEMPLATE:get_aci_proto_bgp.state_established:iserver.output.default
```

Example: idle (down)

```
DOC_TEMPLATE:get_aci_proto_bgp.state_idle:iserver.output.default
```

[[Back]](./ProtocolBgp.md)