# RunIt - Redfish Check

[[Back]](../BareMetalCluster.md) [[Next]](./example_fqdn_check.md) [[Prev]](./example_openshift_api_check.md)

Workflow
- runs for every server defined in [server.json](./input_data_server.md)
- collect server base properties e.g. model, serial
- check virtual media
    - identify virtual media id for cimc mounted iso
    - eject media
    - prepare basic (but proper) iso on the [web server](./input_data_web.md)
    - map virtual media
    - eject virtual media
    - delete temporary iso file
- check available boot settings incl. `Cd`, `Hdd` and `None`
- check reset actions incl. `PowerCycle`

```
Check server redfish [bm1-1]
----------------------------
Redfish endpoint: 10.20.20.20
- @odata.id: /redfish/v1/Chassis/1
- ChassisType: Rack
- Model: UCS C240 M6SN
- SerialNumber: AAAA
- PowerState: On
- Detected chassis type: Rack
Virtual Media [0]
- @odata.id: /redfish/v1/Managers/CIMC/VirtualMedia/0
- Name: Virtual CD
- Inserted: True
- MediaTypes: ['CD', 'DVD']
- ConnectedVia: URI
- State: Enabled
- Health: OK
Virtual media ejected via redfish
Virtual media test
- filename to be uploaded to web server: image-a4d5bb22-cf5d-49a0-894f-e240bcf7efc6.iso
Creating file in local web server: image-a4d5bb22-cf5d-49a0-894f-e240bcf7efc6.iso
- url: http://10.10.10.10:8080/image-a4d5bb22-cf5d-49a0-894f-e240bcf7efc6.iso
- virtual media inserted [id:0]
- virtual media mapped
- virtual media ejected
Deleting file in local web server: image-a4d5bb22-cf5d-49a0-894f-e240bcf7efc6.iso
- web server file deleted
Boot settings
- boot source override enabled: Once
- boot source override target: Cd
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

[[Back]](../BareMetalCluster.md) [[Next]](./example_fqdn_check.md) [[Prev]](./example_openshift_api_check.md)