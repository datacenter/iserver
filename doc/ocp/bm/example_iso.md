# RunIt - ISO

[[Back]](../BareMetalCluster.md) [[Next]](./example_boot.md) [[Prev]](./example_create_cluster.md)

Workflow
- download generated iso
- (optional) manipulate iso with user/password authentication instead of ssh pubkey only
- upload iso to web server

```
Download ISO
------------
- url: https://.../full.iso
- ssl verify: True
- timeout: 600
- target filename: /tmp/cluster-id.iso

Core user password override
---------------------------
- core password: mypass
- container: docker
- ip: localhost

ISO manipulation locally
------------------------
Iso filename: /tmp/aaa.iso
Run: sudo docker run -v /tmp:/data:Z --rm quay.io/coreos/coreos-installer:release iso ignition show /data/aaa.iso
Ignition output loaded
Run: openssl passwd -6 mypass
Core password updated in ignition
{
    "groups": [
        "sudo"
    ],
    "name": "core",
    "passwordHash": "...",
    "sshAuthorizedKeys": [
        "ssh-ed25519 ..."
    ]
}
Run: sudo docker run -v /tmp:/data:Z --rm quay.io/coreos/coreos-installer:release iso customize --output /data/new-aaa.iso --force /data/aaa.iso --live-ignition /data/ignition-aaa.iso
```

[[Back]](../BareMetalCluster.md) [[Next]](./example_boot.md) [[Prev]](./bm/example_create_cluster.md)