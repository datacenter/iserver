# Endpoint

## Filter by server's ip address

- Server must be found by IP address in intersight account
- MAC address of every network adapter is added to endpoint search criteria

```
DOC_TEMPLATE:get_aci_endpoint.server:iserver.output.default
```

- Use -o fabric option to get interface related information for get_aci_endpoint.server

```
DOC_TEMPLATE:get_aci_endpoint.server_fabric:iserver.output.default
```

- Use context to get interface details

```
DOC_TEMPLATE:get_aci_endpoint.server_context:iserver.output.default
```

[[Back Endpoint]](./Endpoint.md) [[Back Cross Domain]](./XdServer.md)