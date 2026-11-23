# Input-Output Memory Management Unit (IOMMU)

The goal is to enable IOMMU on the kernel level.

## Requirements

- machine config pool must be in stable state

## Step: Check IOMMU state

```
$ dmesg | grep -i iommu
$
```

```
$ grep iommu /proc/cmdline
$ 
```

## Step: Machine Config 

Prepare MachineConfig to enable IOMMU on the kernel level following the [kernel parameters documentation](https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html).

Make sure to adjust labels to select the nodes where change should be applied. In case of SNO, role should be master e.g.
```
$ oc get mcp
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-3d96b9ce26325f6aeab5dd29aa2ef978   True      False      False      1              1                   1                     0                      107d
worker   rendered-worker-2a3e110916737305354e21a23b873f90   True      False      False      0              0                   0                     0                      107d
```

### Intel CPU

```
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 100-worker-iommu
spec:
  config:
    ignition:
      version: 3.2.0
  kernelArguments:
  - intel_iommu=on
```

### AMD CPU

```
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 100-worker-iommu
spec:
  config:
    ignition:
      version: 3.2.0
  kernelArguments:
  - amd_iommu=on
```

Notes: 
- [kernel parameters](https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html) do not define 'on' value 
- on value is defined in [OCP documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/virtualization/managing-vms)
- as per kernel documentation, AMD should have iommu enabled by default however it is not in dmesg output until machine config has been applied

### Apply

```
$ oc create -f iommu.yaml
```

```
$ oc get mcp
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-3d96b9ce26325f6aeab5dd29aa2ef978   False     True       False      1              0                   0                     0                      107d
worker   rendered-worker-37cf71a9cfa7a0e5f5fdf4681e434753   True      False      False      0              0                   0                     0                      107d
```

Automatic node reboot expected

```
Broadcast message from root@bm5 (Tue 2025-12-23 11:24:23 UTC):

The system will reboot now!
```

## Step: Check IOMMU state

Once the node is back online

```
$ grep iommu /proc/cmdline 
BOOT_IMAGE=... amd_iommu=on ...
```

```
$ dmesg | grep -i iommu
[    1.766664] iommu: Default domain type: Translated
[    1.766664] iommu: DMA domain TLB invalidation policy: lazy mode
[    1.802346] pci 0000:60:00.2: AMD-Vi: IOMMU performance counters supported
[    1.810629] pci 0000:60:01.0: Adding to iommu group 0
...
```

## Revert the change

Going back to default state with IOMMU disabled can be done by MachineConfig delete that was passing kernel parameter

```
$ oc delete -f iommu.yaml
```

```
$ oc get mcp
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-3d96b9ce26325f6aeab5dd29aa2ef978   False     True       False      1              0                   0                     0                      107d
worker   rendered-worker-37cf71a9cfa7a0e5f5fdf4681e434753   True      False      False      0              0                   0                     0                      107d
```

Automatic node reboot expected

```
Broadcast message from root@bm5 (Tue 2025-12-23 12:17:53 UTC):

The system will reboot now!
```

However in case of AMD (not sure about Intel), even if kernel parameter is not there, iommu is still enabled. 

```
$ grep iommu /proc/cmdline
$ 
```

```
$ dmesg | grep -i iommu
[    1.744188] iommu: Default domain type: Translated
[    1.744188] iommu: DMA domain TLB invalidation policy: lazy mode
[    1.779417] pci 0000:60:00.2: AMD-Vi: IOMMU performance counters supported
[    1.787302] pci 0000:60:01.0: Adding to iommu group 0
...
```

When amd_iommu=off parameter is defined in MachineConfig then after automatic reload, iommu is not initialized.

Such behavior confirms in-a-way the fact that has been mentioned when googling that in case of AMD CPU, IOMMU is enabled by default and it can be disabled with 'off' value when needed.

[[Back]](./README.md)