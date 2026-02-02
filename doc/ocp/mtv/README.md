# Migration Toolkit for Virtualization

Migration Toolkit for Virtualization (MTV) migrates virtual machines at scale to Red Hat OpenShift Virtualization from:
- VMware
- Open Virtual Appliance
- OpenStack
- Red Hat Virtualization (RHEV)
- OpenShift Virtualization

Official documentation [link](https://developers.redhat.com/products/mtv)

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp mtv | check the mtv operator state and configuration | [Link](./get.md)
iserver set ocp mtv --mode operator | install mtv operator | [Link](./create_operator.md)
iserver set ocp mtv --mode instance | create forklift controller instance | [Link](./create_instance.md)
iserver set ocp mtv --mode provider | create provider | [Link](./create_provider.md)
iserver set ocp mtv --mode nmap | create network map | [Link](./create_network_map.md)
iserver set ocp mtv --mode smap | create storage map | [Link](./create_storage_map.md)
iserver set ocp mtv --mode plan | create migration plan | [Link](./create_plan.md)
iserver set ocp mtv --mode run | run migration plan | [Link](./run_run.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp mtv --mode plan | delete migration plan | [Link](./delete_plan.md)
iserver delete ocp mtv --mode nmap | delete network map | [Link](./delete_network_map.md)
iserver delete ocp mtv --mode smap | delete storage map | [Link](./delete_storage_map.md)
iserver delete ocp mtv --mode provider | delete provider | [Link](./delete_provider.md)
iserver delete ocp mtv --mode instance | delete mtv forklift controller instance | [Link](./delete_instance.md)
iserver delete ocp mtv --mode operator | delete mtv operator | [Link](./delete_operator.md)
iserver delete ocp mtv --mode wipe | delete migration plan, network maps, storage maps and providers | [Link](./delete_wipe.md)
iserver delete ocp mtv --mode all | delete mtv operator and associated resources | [Link](./delete_all.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

## Extras

- [VDDK image preparation](./vddk.md)
- [Conversion POD - where migration happens](./conversion-pod.md)
- [Ethernet vNIC driver change](./driver.md)
- [IP preservation options](./static-ip.md)
- [VMware Changed Block Tracking (CBT) setting](./cbt.md)
- [Virtual machine first boot system preparation](./first-boot.md)
- QEMU Guest Agent
    - [automatic installation](./qga-autoinstall.md)
    - [manual installation](./qga-manual.md)
- [VMware tools automatic uninstallation](./vmware-tools-removal.md)

Libguestfs
- [v2v](./v2v.md)
- [nbdkit](./nbdkit.md)
- [supermin](./supermin.md)

Support
- [Libguestfs v2v supported hypervisors](https://libguestfs.org/virt-v2v-support.1.html)
- [RedHat KB](https://access.redhat.com/articles/1351473)

[[Back]](../Operations.md)