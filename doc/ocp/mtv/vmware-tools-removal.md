# VMware tools automatic uninstallation

VMware tools are not needed once the virtual machine is migrated to OpenShift with KVM hypervisor. QEMU guest agent is required instead.

## Debian/Ubuntu

Pre-migration state

```
ubuntu@usmall:~$ sudo apt list open-vm-tools
Listing... Done
open-vm-tools/jammy-updates,jammy-security,now 2:12.3.5-3~ubuntu0.22.04.3 amd64 [installed]
```

There is no sign of any attemp to remove open-vm-tools in [conversion pod](./conversion-pod.md) logs. 

Post-migration state

```
ubuntu@usmall:~$ sudo apt list open-vm-tools
Listing... Done
open-vm-tools/jammy-updates,jammy-security,now 2:12.3.5-3~ubuntu0.22.04.3 amd64 [installed]
```

## RHEL/Fedora/CentOS

Pre-migration state

```
# yum list installed open-vm-tools
Installed Packages
open-vm-tools.x86_64                    11.2.0-2.el8
```

In [conversion pod](./conversion-pod.md) logs

```
libguestfs: trace: v2v: sh "dnf -y remove 'open-vm-tools'"
guestfsd: => aug_match (0x18) took 0.00 secs
guestfsd: <= sh (0x6f) request length 76 bytes
```

Post-migration state

```
# yum list installed open-vm-tools
Error: No matching Packages to list
```

[[Back]](./README.md)