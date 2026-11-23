# Virtual Machine with GPU PCI Passthrough

The goal of this setup is to pass GPU device with direct hardware access to Virtual Machine and install nvidia driver.

Description
- A virtualization feature (using VFIO) that dedicates a physical GPU directly to a single Virtual Machine (VM)
- The hypervisor (like KVM) assigns the entire PCIe device to the guest VM, giving it direct hardware access
- Near bare-metal performance, excellent for gaming, high-end rendering, or AI training within a VM
- The GPU can't be easily shared with other VMs; setup is more complex as compared with [GPU operator](../gpu/README.md)
- Best for single VMs needing maximum GPU power, bypassing virtualization overhead

## Prerequisites

- [GPU operator](../gpu/README.md) *not* installed
- [Container Virtualization Operator](../cnv/README.md) installed and configured

## Cluster preparation

- [IOMMU enabled](./iommu.md)
- [Virtual Function I/O GPU driver](./vfio-pci.md)
- [GPU Passthrough devices enabled for virtualization](./hyperconverged.md)

## Virtual Machine

Distribution | Create Virtual Machine | Enable NVIDIA Driver | Functional Test
--- | --- | --- | ---
RHEL8 | [Link](./virtual-machine-rhel8.md) | [Link](./driver-rhel8.md) | ---
RHEL9 | [Link](./virtual-machine-rhel9.md) | [Link](./driver-rhel9.md) | [Link](./test-rhel9.md)

## Expected final outcome

GPU device with NVIDIA driver at VM level

```
$ lspci -nn -k -d ::0302
09:00.0 3D controller [0302]: NVIDIA Corporation GA107GL [A2 / A16] [10de:25b6] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:14a9]
        Kernel driver in use: nvidia
        Kernel modules: nouveau, nvidia_drm, nvidia
```

## Cleanup

tbd

[[Back]](../Operations.md)