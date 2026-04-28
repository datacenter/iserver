# ssh.pub

[[Back]](../BareMetalCluster.md) [[Next]](./input_data_web.md) [[Prev]](./input_data_nmstate.md)

OpenShift cluster nodes support ssh with public key after installation using username `core`. The SSH public key is sent to OpenShift Console via API upon cluster initialization. **Single SSH public key** can be defined during installation. For extra ssh keys use [ssh day2 feature](../ssh/README.md).

```
ssh-ed25519 AAAAC...
```

Note: put the content of ssh public key file as-is

[[Back]](../BareMetalCluster.md) [[Next]](./input_data_web.md) [[Prev]](./input_data_nmstate.md)