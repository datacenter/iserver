# Node Protocol - BGP

## Filter BGP neighbors by Router ID

Use --view parameter to select neighborship attributes template
- [default](./ProtocolBgpNeighborSummary.md)
- [transport](./ProtocolBgpNeighborTransport.md)
- [connection](./ProtocolBgpNeighborConnection.md)
- [af](./ProtocolBgpNeighborAf.md)
- [verbose](./ProtocolBgpNeighborVerbose.md)

Example: IP address

```
DOC_TEMPLATE:get_aci_proto_bgp.router_ip:iserver.output.default
```

Example: IP subnet

```
DOC_TEMPLATE:get_aci_proto_bgp.router_subnet:iserver.output.default
```

Developer

```
DOC_TEMPLATE:get_aci_proto_bgp.router_ip:devel.debug
```

[[Back]](./ProtocolBgp.md)