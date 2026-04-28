# RunIt - Boot

[[Back]](../BareMetalCluster.md) [[Next]](./example_extra_configuration.md) [[Prev]](./example_iso.md)

Workflow
- virtual media mount
- power cycle servers via redfish
- wait for server to be discovered (call-back-home)

```
Redfish vmedia mapping created successfuly: 10.20.20.10
Redfish boot source set to cd successful: 10.20.20.10
Power cycle: 10.20.20.10
Server booted: 10.20.20.10
Redfish vmedia mapping created successfuly: 10.20.20.11
Redfish boot source set to cd successful: 10.20.20.11
Power cycle: 10.20.20.11
Server booted: 10.20.20.11
Redfish vmedia mapping created successfuly: 10.20.20.12
Redfish boot source set to cd successful: 10.20.20.12
Power cycle: 10.20.20.12
Server booted: 10.20.20.12
Wait for all the servers discovered...
```

[[Back]](../BareMetalCluster.md) [[Next]](./example_extra_configuration.md) [[Prev]](./example_iso.md)