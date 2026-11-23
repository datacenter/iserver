# Virtual-to-Virtual (v2v) migration

[virt-v2v](https://manpages.ubuntu.com/manpages/noble/man1/virt-v2v.1.html) converts a single guest from a foreign hypervisor to run on KVM. 

It runs in [conversion pod](./conversion-pod.md) and this is the first thing conversion container does

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

Workflow steps
- get source libvirt xml details
- start [nbdkit](./nbdkit.md) that exports the vmware vmdk disk source over the network
- add nbd exposed remote disk via unix socket as drive to v2v
- run [supermin](./supermin.md) build appliance
- perform filesystem conversion and changes incl.
  - [first boot system preparation](./first-boot.md)

## Source libvirt xml exmample

```
<domain type='vmware' xmlns:vmware='http://libvirt.org/schemas/domain/vmware/1.0'>
  <name>usmall</name>
  <uuid>4232104e-0a6e-cc9e-b8cf-f0283fadeac2</uuid>
  <memory unit='KiB'>2097152</memory>
  <currentMemory unit='KiB'>2097152</currentMemory>
  <vcpu placement='static'>2</vcpu>
  <cputune>
    <shares>2000</shares>
  </cputune>
  <os firmware='efi'>
    <type arch='x86_64'>hvm</type>
  </os>
  <clock offset='utc'/>
  <on_poweroff>destroy</on_poweroff>
  <on_reboot>restart</on_reboot>
  <on_crash>destroy</on_crash>
  <devices>
    <disk type='file' device='disk'>
      <source file='MyNAS/usmall.vmdk'/>
      <target dev='sda' bus='scsi'/>
      <address type='drive' controller='0' bus='0' target='0' unit='0'/>
    </disk>
    <disk type='file' device='cdrom'>
      <source file='[MyNAS] ubuntu2204.iso'/>
      <target dev='sda' bus='sata'/>
      <readonly/>
      <address type='drive' controller='0' bus='0' target='0' unit='0'/>
    </disk>
    <controller type='scsi' index='0' model='vmpvscsi'/>
    <controller type='sata' index='0'/>
    <interface type='vds'>
      <mac address='00:50:56:b2:b1:42' type='generated'/>
      <source switchid='5032e4c6-b5bc-d1c5-63a8-7a02c0c94abd' portid='5357' portgroupid='dvportgroup-48937' connectionid='282981317'/>
      <model type='vmxnet3'/>
    </interface>
    <video>
      <model type='vmvga' vram='8192' primary='yes'/>
    </video>
  </devices>
  <vmware:datacenterpath>eu-spdc-dc</vmware:datacenterpath>
  <vmware:moref>vm-61951</vmware:moref>
</domain>
```

[[Back]](./README.md)