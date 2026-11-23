# RHEL9 Virtual Machine with GPU PCI Passthrough

The goal of this setup is to pass GPU device with direct hardware access to RHEL9 Virtual Machine.

## Expected Outcome

Host level

```
$ lspci -nn -k -d ::0302
c5:00.0 3D controller [0302]: NVIDIA Corporation GA107GL [A2 / A16] [10de:25b6] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:14a9]
        Kernel driver in use: vfio-pci
        Kernel modules: nouveau
c6:00.0 3D controller [0302]: NVIDIA Corporation GA107GL [A2 / A16] [10de:25b6] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:14a9]
        Kernel driver in use: vfio-pci
        Kernel modules: nouveau
c7:00.0 3D controller [0302]: NVIDIA Corporation GA107GL [A2 / A16] [10de:25b6] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:14a9]
        Kernel driver in use: vfio-pci
        Kernel modules: nouveau
c8:00.0 3D controller [0302]: NVIDIA Corporation GA107GL [A2 / A16] [10de:25b6] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:14a9]
        Kernel driver in use: vfio-pci
        Kernel modules: nouveau
```

VM level

```
$ lspci -nn -k -d ::0302
09:00.0 3D controller [0302]: NVIDIA Corporation GA107GL [A2 / A16] [10de:25b6] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:14a9]
        Kernel driver in use: nouveau
        Kernel modules: nouveau
```

## Virtual Machine Template (Console UI)

Create Virtual Machine from RHEL9 template, follow the defaults, wait until VM is up

```
$ lspci -nn -k -d ::0302
$
```

Since no changes have been made to VM specification yet, GPU device is not exposed inside the VM. 

Stop the virtual machine and edit its specification
- refer to resource name as deviceName, 
- 'name' value can be aritrary and is not referred anywhere else
- start virtual machine

```
$ oc edit virtualmachine -n openshift rhel9-black-halibut-74
spec:
  template:
    spec:
      devices:
        hostDevices:
        - deviceName: nvidia/my-gpu
          name: hostGpuDevice
```

Once virtual machine is up again

```
$ virtctl console -n openshift rhel9-black-halibut-74
Successfully connected to rhel9-black-halibut-74 console. The escape sequence is ^]

rhel9-black-halibut-74 login: cloud-user
Password:
Last login: Tue Dec 23 12:06:14 on tty1
[cloud-user@rhel9-black-halibut-74 ~]$ lspci -nn -k -d ::0302
09:00.0 3D controller [0302]: NVIDIA Corporation GA107GL [A2 / A16] [10de:25b6] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:14a9]
        Kernel driver in use: nouveau
        Kernel modules: nouveau
```

Check on node resources level that GPU has been allocated

```
$ oc describe node bm5
Name:               bm5
Roles:              control-plane,master,worker
Capacity:
  nvidia/my-gpu:                  4
Allocatable:
  nvidia/my-gpu:                  4
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource                       Requests      Limits
  --------                       --------      ------
  cpu                            12664m (4%)   23010m (9%)
  memory                         31101Mi (6%)  58218Mi (11%)
  ephemeral-storage              50M (0%)      0 (0%)
  hugepages-1Gi                  0 (0%)        0 (0%)
  hugepages-2Mi                  0 (0%)        0 (0%)
  devices.kubevirt.io/kvm        1             1
  devices.kubevirt.io/tun        1             1
  devices.kubevirt.io/vhost-net  1             1
  nvidia/my-gpu                  1             1
```

## Virtual Machine CR

```
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: my-vm-with-gpu
  namespace: default
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: my-vm-with-gpu
    spec:
      sourceRef:
        kind: DataSource
        name: rhel9
        namespace: openshift-virtualization-os-images
      storage:
        resources:
          requests:
            storage: 30Gi
  runStrategy: RerunOnFailure
  template:
    metadata:
      annotations:
        vm.kubevirt.io/flavor: small
        vm.kubevirt.io/os: rhel9
        vm.kubevirt.io/workload: server
      labels:
        kubevirt.io/domain: my-vm-with-gpu
        kubevirt.io/size: small
        network.kubevirt.io/headlessService: headless
    spec:
      architecture: amd64
      domain:
        cpu:
          cores: 1
          sockets: 1
          threads: 1
        devices:
          disks:
          - disk:
              bus: virtio
            name: rootdisk
          - disk:
              bus: virtio
            name: cloudinitdisk
          hostDevices:
          - deviceName: nvidia/my-gpu
            name: hostGpuDevice
          interfaces:
          - macAddress: 02:db:9f:00:00:00
            masquerade: {}
            model: virtio
            name: default
          rng: {}
        memory:
          guest: 2Gi
        resources: {}
      networks:
      - name: default
        pod: {}
      volumes:
      - dataVolume:
          name: my-vm-with-gpu
        name: rootdisk
      - cloudInitNoCloud:
          userData: |-
            #cloud-config
            user: cloud-user
            password: pass123
            chpasswd: { expire: False }
        name: cloudinitdisk
```

[[Back]](./README.md)