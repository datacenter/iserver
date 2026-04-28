# RunIt - Wait for installation finished

[[Back]](../BareMetalCluster.md) [[Next]](./example_post.md) [[Prev]](./example_extra_configuration.md)

Workflow
- track installation progress via API
- boot order to `Hdd`
- eject virtual media

```
Wait for cluster ready to be installed...
Start installation request...
Wait for installation started [cluster-id]...
Status changed to preparing-for-installation
Status changed to installing
Cluster reached desired state: installing
Changing servers to boot from hdd with optional vmedia eject
- 10.20.20.10
	Skipping vmedia eject for full iso
	Server boot source override set to hdd successful
- 10.20.20.11
	Skipping vmedia eject for full iso
	Server boot source override set to hdd successful
- 10.20.20.12
	Skipping vmedia eject for full iso
	Server boot source override set to hdd successful

Host 10.20.20.10 status changed to installing

Host 10.20.20.11 status changed to installing

Host 10.20.20.12 status changed to installing

Host 10.20.20.10 status changed to installing-in-progress

Host 10.20.20.12 status changed to installing-in-progress

Host 10.20.20.11 status changed to installing-in-progress

Host 10.20.20.11 status changed to installed

Host 10.20.20.10 status changed to installed

Host 10.20.20.12 status changed to installed

Installation finished...
Redfish vmedia eject successful: 10.20.20.10
Redfish vmedia eject successful: 10.20.20.11
Redfish vmedia eject successful: 10.20.20.12
```

[[Back]](../BareMetalCluster.md) [[Next]](./example_post.md) [[Prev]](./example_extra_configuration.md)