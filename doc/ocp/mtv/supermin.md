# supermin

[Supermin](https://libguestfs.org/supermin.1.html) appliance is mini virtual machine that contain the bare minimum components on top of the filesystem.

In the context of [v2v](./v2v.md), supermin provides an runtime environment used by libguestfs libraries to inspect and modify the disk image.

```
libguestfs: run supermin
libguestfs: command: run: /usr/bin/supermin
libguestfs: command: run: \ --build
libguestfs: command: run: \ --verbose
libguestfs: command: run: \ --if-newer
libguestfs: command: run: \ --lock /var/tmp/.guestfs-107/lock
libguestfs: command: run: \ --copy-kernel
libguestfs: command: run: \ -f ext2
libguestfs: command: run: \ --host-cpu x86_64
libguestfs: command: run: \ /usr/lib64/guestfs/supermin.d
libguestfs: command: run: \ -o /var/tmp/.guestfs-107/appliance.d
supermin: version: 5.3.5
```

This will create files called /var/tmp/.guestfs-107/appliance.d/kernel and /var/tmp/.guestfs-107/appliance.d/root etc, which is the full sized bootable appliance.

[[Back]](./README.md)