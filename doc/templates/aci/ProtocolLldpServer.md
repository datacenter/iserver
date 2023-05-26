# Node Protocol - LLDP

## Filter by server's ip address

- Server must be found by IP address in intersight account
- MAC address of every network adapter is added to endpoint search criteria

```
DOC_TEMPLATE:get_aci_proto_lldp.server:iserver.output.default
```

- Use context to get interface details

```
DOC_TEMPLATE:get_aci_proto_lldp.context:iserver.output.default
```

[[Back Protocol]](./ProtocolLldp.md) [[Back Cross Domain]](./XdServer.md)