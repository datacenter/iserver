# redfish.json

Redfish credentials defined in redfish.json are used for redfish authentication for every server defined in [server.json](./input_data_server.md).

```
{
    "username": "user",
    "password": "pass"
}
```

In case of Fabric Interconnect connected servers, the credentials are for FI. So as the endpoint_ip in server.json. inventory_id attribute selects the server.

[Back](../BareMetalCluster.md)
