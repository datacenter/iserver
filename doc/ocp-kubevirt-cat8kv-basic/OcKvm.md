# OpenShift Virtualization - Cat8000v Test Results

## KVM Domain

```
# ssh core@10.58.24.218 sudo cat /var/lib/kubelet/pods/d83061b6-51e2-42a2-bf9c-468e273ea5fc/volumes/kubernetes.io~empty-dir/private/libvirt/qemu/default_cat8kv-01.xml
<!--
WARNING: THIS IS AN AUTO-GENERATED FILE. CHANGES TO IT ARE LIKELY TO BE
OVERWRITTEN AND LOST. Changes to this xml configuration should be made using:
  virsh edit default_cat8kv-01
or other application using the libvirt API.
-->

<domain type='kvm'>
  <name>default_cat8kv-01</name>
  <uuid>30592aed-01ef-5ef9-8a5a-512013936f65</uuid>
  <metadata>
    <kubevirt xmlns="http://kubevirt.io">
      <uid>60533689-c1b1-4b76-bbea-b42ec2a73ca6</uid>
      <graceperiod>
        <deletionGracePeriodSeconds>30</deletionGracePeriodSeconds>
      </graceperiod>
    </kubevirt>
  </metadata>
  <memory unit='KiB'>4194304</memory>
  <currentMemory unit='KiB'>4194304</currentMemory>
  <vcpu placement='static'>1</vcpu>
  <iothreads>1</iothreads>
  <sysinfo type='smbios'>
    <system>
      <entry name='manufacturer'>Red Hat</entry>
      <entry name='product'>Container-native virtualization</entry>
      <entry name='version'>4.11.3</entry>
      <entry name='uuid'>30592aed-01ef-5ef9-8a5a-512013936f65</entry>
      <entry name='sku'>4.11.3</entry>
      <entry name='family'>Red Hat</entry>
    </system>
  </sysinfo>
  <os>
    <type arch='x86_64' machine='pc-q35-rhel8.6.0'>hvm</type>
    <boot dev='hd'/>
    <smbios mode='sysinfo'/>
  </os>
  <features>
    <acpi/>
  </features>
  <cpu mode='host-model' check='partial'>
    <topology sockets='1' dies='1' cores='1' threads='1'/>
  </cpu>
  <clock offset='utc'/>
  <on_poweroff>destroy</on_poweroff>
  <on_reboot>restart</on_reboot>
  <on_crash>destroy</on_crash>
  <devices>
    <emulator>/usr/libexec/qemu-kvm</emulator>
    <disk type='block' device='disk' model='virtio-non-transitional'>
      <driver name='qemu' type='raw' cache='none' error_policy='stop' io='native' discard='unmap'/>
      <source dev='/dev/rootdisk'/>
      <target dev='vda' bus='virtio'/>
      <alias name='ua-rootdisk'/>
      <address type='pci' domain='0x0000' bus='0x04' slot='0x00' function='0x0'/>
    </disk>
    <disk type='block' device='cdrom'>
      <driver name='qemu' type='raw' cache='none' error_policy='stop' io='native' discard='unmap'/>
      <source dev='/dev/cdromdisk'/>
      <target dev='sda' bus='sata'/>
      <readonly/>
      <alias name='ua-cdromdisk'/>
      <address type='drive' controller='0' bus='0' target='0' unit='0'/>
    </disk>
    <controller type='usb' index='0' model='none'/>
    <controller type='scsi' index='0' model='virtio-non-transitional'>
      <address type='pci' domain='0x0000' bus='0x02' slot='0x00' function='0x0'/>
    </controller>
    <controller type='virtio-serial' index='0' model='virtio-non-transitional'>
      <address type='pci' domain='0x0000' bus='0x03' slot='0x00' function='0x0'/>
    </controller>
    <controller type='sata' index='0'>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x1f' function='0x2'/>
    </controller>
    <controller type='pci' index='0' model='pcie-root'/>
    <controller type='pci' index='1' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='1' port='0x10'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0' multifunction='on'/>
    </controller>
    <controller type='pci' index='2' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='2' port='0x11'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x1'/>
    </controller>
    <controller type='pci' index='3' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='3' port='0x12'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x2'/>
    </controller>
    <controller type='pci' index='4' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='4' port='0x13'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x3'/>
    </controller>
    <controller type='pci' index='5' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='5' port='0x14'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x4'/>
    </controller>
    <controller type='pci' index='6' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='6' port='0x15'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x5'/>
    </controller>
    <controller type='pci' index='7' model='pcie-root-port'>
      <model name='pcie-root-port'/>
      <target chassis='7' port='0x16'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x6'/>
    </controller>
    <interface type='ethernet'>
      <mac address='02:6c:cf:00:00:6a'/>
      <target dev='tap0' managed='no'/>
      <model type='virtio-non-transitional'/>
      <mtu size='1450'/>
      <alias name='ua-default'/>
      <rom enabled='no'/>
      <address type='pci' domain='0x0000' bus='0x01' slot='0x00' function='0x0'/>
    </interface>
    <serial type='unix'>
      <source mode='bind' path='/var/run/kubevirt-private/60533689-c1b1-4b76-bbea-b42ec2a73ca6/virt-serial0'/>
      <target type='isa-serial' port='0'>
        <model name='isa-serial'/>
      </target>
    </serial>
    <console type='unix'>
      <source mode='bind' path='/var/run/kubevirt-private/60533689-c1b1-4b76-bbea-b42ec2a73ca6/virt-serial0'/>
      <target type='serial' port='0'/>
    </console>
    <channel type='unix'>
      <target type='virtio' name='org.qemu.guest_agent.0'/>
      <address type='virtio-serial' controller='0' bus='0' port='1'/>
    </channel>
    <input type='mouse' bus='ps2'/>
    <input type='keyboard' bus='ps2'/>
    <graphics type='vnc' socket='/var/run/kubevirt-private/60533689-c1b1-4b76-bbea-b42ec2a73ca6/virt-vnc'>
      <listen type='socket' socket='/var/run/kubevirt-private/60533689-c1b1-4b76-bbea-b42ec2a73ca6/virt-vnc'/>
    </graphics>
    <audio id='1' type='none'/>
    <video>
      <model type='vga' vram='16384' heads='1' primary='yes'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x0'/>
    </video>
    <memballoon model='virtio-non-transitional'>
      <stats period='10'/>
      <address type='pci' domain='0x0000' bus='0x05' slot='0x00' function='0x0'/>
    </memballoon>
    <rng model='virtio-non-transitional'>
      <backend model='random'>/dev/urandom</backend>
      <address type='pci' domain='0x0000' bus='0x06' slot='0x00' function='0x0'/>
    </rng>
  </devices>
</domain>
```
