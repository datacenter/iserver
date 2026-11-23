# Ethernet driver

As example Ubuntu 22.04 in vCenter with **vmxnet3** driver

```
$ ip a
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:50:56:b2:b1:42 brd ff:ff:ff:ff:ff:ff
    altname enp2s1
    inet 10.10.10.205/28 brd 10.10.10.207 scope global ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feb2:b142/64 scope link
       valid_lft forever preferred_lft forever

$ sudo ethtool -i ens33
driver: vmxnet3
version: 1.6.0.0-k-NAPI
firmware-version:
expansion-rom-version:
bus-info: 0000:02:01.0
supports-statistics: yes
supports-test: no
supports-eeprom-access: no
supports-register-dump: yes
supports-priv-flags: no

$ sudo lsmod | grep virtio_net
$
```

After migration to OpenShift the driver changes to **virtio_net** 

Note: the change of interface name is related to [static IP](./static-ip.md) feature being disabled at this migration

```
$ ip a
2: enp1s0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 00:50:56:b2:b1:42 brd ff:ff:ff:ff:ff:ff

$ sudo ethtool -i enp1s0
driver: virtio_net
version: 1.0.0
firmware-version:
expansion-rom-version:
bus-info: 0000:01:00.0
supports-statistics: yes
supports-test: no
supports-eeprom-access: no
supports-register-dump: no
supports-priv-flags: no

$ sudo lsmod | grep vmxnet
$ 
```

As per [documentation](https://docs.redhat.com/en/documentation/migration_toolkit_for_virtualization/2.9/html/installing_and_using_the_migration_toolkit_for_virtualization/architecture_mtv#main-functions-virt-v2v-mtv_mtv) the driver modification is done by [v2v](./v2v.md). Let's trace it.

### Source

checking vmware instance and virtio driver is already installed

```
$ ls /lib/modules/5.15.0-164-generic/kernel/drivers/net/virtio_net.ko
/lib/modules/5.15.0-164-generic/kernel/drivers/net/virtio_net.ko
```

It is not loaded though

```
$ sudo lsmod | grep virtio_net
$
```

### virt-v2v documentation

Checking [virt-v2v documentation](https://libguestfs.org/virt-v2v.1.html)

```
Older versions of virt-v2v could install these drivers for certain Linux guests. 

This version of virt-v2v does not attempt to install new Linux kernels or drivers, 
but will warn you if they are not installed already.
```

However it says nothing about configuration or loading the kernel modules, just about installation.

### initramfs modules

At source (empty)

```
$ cat /etc/initramfs-tools/modules
# ... comments ...
```

After migration

```
$ cat /etc/initramfs-tools/modules
# ... comments ...
# The following modules were added by virt-v2v
virtio_blk
virtio_scsi
virtio_net
bochs
```

### Conversion pod

```
Building command: virt-v2v [
    -v 
    -x 
    -o kubevirt 
    -os /var/tmp/v2v 
    -i libvirt 
    -ic vpx://username@vc.domain.com/my-dc-name/host/my-cluster-name/my-host-name?no_verify=1 
    -ip /etc/secret/secretKey 
    --hostname usmall 
    --root first 
    -it vddk 
    -io vddk-libdir=/opt/vmware-vix-disklib-distrib 
    -io vddk-thumbprint=AA:BB:CC
    -- usmall
]
info: virt-v2v: virt-v2v 2.8.1rhel=10,release=13.el10_1 (x86_64)
```

later 

```
libguestfs: trace: v2v: aug_set "/files/etc/initramfs-tools/modules/#comment[last()+1]" "The following modules were added by virt-v2v"
guestfsd: <= aug_set (0x14) request length 148 bytes
guestfsd: => aug_set (0x14) took 0.00 secs
libguestfs: trace: v2v: aug_set = 0
libguestfs: trace: v2v: aug_clear "/files/etc/initramfs-tools/modules/virtio_blk"
guestfsd: <= aug_clear (0xef) request length 92 bytes
guestfsd: => aug_clear (0xef) took 0.00 secs
libguestfs: trace: v2v: aug_clear = 0
libguestfs: trace: v2v: aug_clear "/files/etc/initramfs-tools/modules/virtio_scsi"
guestfsd: <= aug_clear (0xef) request length 92 bytes
guestfsd: => aug_clear (0xef) took 0.00 secs
libguestfs: trace: v2v: aug_clear "/files/etc/initramfs-tools/modules/virtio_net"
guestfsd: <= aug_clear (0xef) request length 92 bytes
guestfsd: => aug_clear (0xef) took 0.00 secs
libguestfs: trace: v2v: aug_clear = 0
libguestfs: trace: v2v: aug_clear "/files/etc/initramfs-tools/modules/bochs"
guestfsd: <= aug_clear (0xef) request length 84 bytes
guestfsd: => aug_clear (0xef) took 0.00 secs
libguestfs: trace: v2v: aug_clear = 0
libguestfs: trace: v2v: aug_save
guestfsd: <= aug_save (0x19) request length 40 bytes
...
libguestfs: trace: v2v: aug_save = 0
libguestfs: trace: v2v: command "/usr/sbin/update-initramfs -v -c -k 5.15.0-164-generic"
```

[guestfish](https://libguestfs.org/guestfish.1.html) which is the tool for examining and modifying virtual machine filesystem is used to modify initramfs modules file... however... if aug_clear method removes the file content and this is how this method is documented, then no clue how modules are added to this file. Eventually for sure the lines are added.

[[Back]](./README.md)