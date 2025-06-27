# SSH Public Key

OpenShift cluster nodes support ssh with public key after installation using username 'core'. The SSH public key is sent to OpenShift Console via API upon cluster initialization. Single SSH public key can be defined during installation. For extra ssh keys use ssh task.

SSH public key can be defined in cluster.ssh_public_key property or ssh.pub

## cluster.json

```
{
    "name": "bm1",
    "openshift_version": "4.17.2",
    "cpu_architecture": "x86_64",
    "ssh_public_key": "ssh-ed25519 AAAA...",
    ...
}
```

## ssh.pub

```
ssh-ed25519 AAAAC...
```

Note: this is the content of ssh public key file

[Back](../BareMetalCluster.md)
