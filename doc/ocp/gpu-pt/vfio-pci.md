# GPU with vfio-pci driver

The goal is changing the kernel driver for GPU device to Virtual Function I/O vfio-pci which is better for GPU/PCI passthrough use case.

## Requirements

- [IOMMU enabled](./iommu.md).

## Step: Check GPU Device

```
$ lspci -nn -k -d ::0302
c5:00.0 3D controller [0302]: NVIDIA Corporation GA107GL [A2 / A16] [10de:25b6] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:14a9]
        Kernel driver in use: nvidia
        Kernel modules: nouveau
c6:00.0 3D controller [0302]: NVIDIA Corporation GA107GL [A2 / A16] [10de:25b6] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:14a9]
        Kernel driver in use: nvidia
        Kernel modules: nouveau
c7:00.0 3D controller [0302]: NVIDIA Corporation GA107GL [A2 / A16] [10de:25b6] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:14a9]
        Kernel driver in use: nvidia
        Kernel modules: nouveau
c8:00.0 3D controller [0302]: NVIDIA Corporation GA107GL [A2 / A16] [10de:25b6] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:14a9]
        Kernel driver in use: nvidia
        Kernel modules: nouveau
```

## Step: Bind GPU device with vfio-pci driver

```
$ cat vfio.bu 
variant: openshift
version: 4.18.0
metadata:
  name: 100-worker-vfiopci
  labels:
    machineconfiguration.openshift.io/role: master
storage:
  files:
  - path: /etc/modprobe.d/vfio.conf
    mode: 0644
    overwrite: true
    contents:
      inline: |
        options vfio-pci ids=10de:25b6
  - path: /etc/modules-load.d/vfio-pci.conf
    mode: 0644
    overwrite: true
    contents:
      inline: vfio-pci
```

```
$ butane vfio.bu -o vfio.yaml
```

```
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: 100-worker-vfiopci
spec:
  config:
    ignition:
      version: 3.4.0
    storage:
      files:
        - contents:
            compression: ""
            source: data:,options%20vfio-pci%20ids%3D10de%3A25b6%0A
          mode: 420
          overwrite: true
          path: /etc/modprobe.d/vfio.conf
        - contents:
            compression: ""
            source: data:,vfio-pci
          mode: 420
          overwrite: true
          path: /etc/modules-load.d/vfio-pci.conf
```

```
$ oc apply -f vfio.yaml
```

```
$ oc get mcp
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-dab2b3f86d7e530693fd51294d49273a   False     True       False      1              0                   0                     0                      108d
worker   rendered-worker-37cf71a9cfa7a0e5f5fdf4681e434753   True      False      False      0              0                   0                     0                      108d
```

Node reboot expected

```
Broadcast message from root@bm5 (Tue 2025-12-23 16:15:24 UTC):

The system will reboot now!
```

## Verify

```
$ lspci -nn -k -d ::0302
c5:00.0 3D controller [0302]: NVIDIA Corporation GA107GL [A2 / A16] [10de:25b6] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:14a9]
        Kernel driver in use: vfio-pci
        Kernel modules: nouveau
```

[[Back]](./README.md)