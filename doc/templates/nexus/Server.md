# Cross Domain

## Server

This feature combines Intersight and NX-OS API. Select the server via CIMC IP (--address) and define the nexus device search domain.
- server's interfaces are discovered via Intersight API
- nexus device lldp, lacp and mac address table are collected

Server's connectivity to nexus devices is shown.

```
DOC_TEMPLATE:get_nx_server.default:iserver.output.default
```

[[Back]](./README.md)