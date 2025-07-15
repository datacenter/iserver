# Verification

Steps:
- verify input data against [input data model](./input_data.md)
- OpenShift Console API access
- web server checks
- redfish server checks
- cluster fqdn resolution

## Redfish

Server checks
- Redfish access
- Main server properties
- Virtual media control
- Boot source override control
- System power actions

```
Redfish endpoint: <server-ip>
- ChassisType: Blade
- Model: UCSX-210C-M7
- SerialNumber: Serial123
- Detected chassis type: Blade
Virtual Media [3]
- Name: CIMC-Mapped vDVD
- Inserted: False
- MediaTypes: ['DVD']
- ConnectedVia: URI
- State: Disabled
- Health: OK
Virtual media test
- filename to be uploaded to web server: image-id.iso
- url: http://<web-server>/image-id.iso
- virtual media inserted
- virtual media mapped
- virtual media ejected
- web server file deleted
Boot settings
- boot source override enabled: Disabled
- boot source override target: None
- target values: ['None', 'Pxe', 'Floppy', 'Cd', 'Hdd', 'BiosSetup', 'Diags']
- enabled values: ['Once', 'Continuous', 'Disabled']
- Cd, Hdd and None found in target values
- Once and Disabled found in enabled values
- Boot from Cd override enabled successfully
- Boot override disabled successfully
System power actions
- ComputerSystem.Reset action found
- Allowed values: ['On', 'ForceOff', 'ForceRestart', 'GracefulShutdown', 'GracefulRestart', 'PowerCycle']
- Compute reset actions check successful
```

[Back](../BareMetalCluster.md)
