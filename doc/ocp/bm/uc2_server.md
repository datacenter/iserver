# OpenShift Cluster with Cilium CNI

## Server checks

Before installation starts, workflow checks the server based on information provided in [cluster](./uc2_cluster.md) input file
- redfish access
- server hardware details
- virtual media control
- boot order control
- power control

These redfish operations are later executed during workflow.

Example output

```
Redfish endpoint: 10.5.5.1
- ChassisType: Rack
- Model: UCS C220 M5SX
- SerialNumber: Serial123
- PowerState: On
- Detected chassis type: Rack
Virtual Media [0]
- Name: Virtual CD
- Inserted: False
- MediaTypes: ['CD', 'DVD']
- ConnectedVia: NotConnected
- State: Disabled
- Health: OK
Virtual media test
- filename to be uploaded to web server: image-id.iso
Creating file in local web server: image-id.iso
- url: http://10.8.8.8/repo/image-id.iso
- virtual media inserted
- virtual media mapped
- virtual media ejected
Deleting file in local web server: image-id.iso
- web server file deleted
Boot settings
- boot source override enabled: Once
- boot source override target: Hdd
- target values: ['None', 'Pxe', 'Floppy', 'Cd', 'Hdd', 'BiosSetup', 'Diags']
- enabled values: ['Once', 'Continuous', 'Disabled']
- Cd, Hdd and None found in target values
- Once and Disabled found in enabled values
- Boot from Cd override enabled successfully
- Boot override disabled successfully
System power actions
- ComputerSystem.Reset action found
- Allowed values: ['On', 'ForceOff', 'GracefulShutdown', 'GracefulRestart', 'ForceRestart', 'Nmi', 'PowerCycle']
- Compute reset actions check successful
```

[Back](./uc2.md)