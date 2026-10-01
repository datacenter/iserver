# OpenShift Virtualization with GPU PCI Passthrough

The goal is to enabled GPU device with direct hardware access to any Virtual Machine (OCP Virtualization) that requests it.

## Requirements

- [GPU operator](../gpu/README.md) not installed
- [Container Virtualization Operator](../cnv/README.md) installed and configured
- [IOMMU enabled](./iommu.md)
- [Virtual Function I/O GPU driver](./vfio-pci.md)

## Expose GPU PCI host device

GPU device can be exposed to Virtual Machine only if specifically allowed in HyperConverged custom resource
- keep PCI device vendor and device id for GPU (as discovered using lspci)
- arbitrary resource name can be defined
- resource name will be listed in node description (capacity)
- resource name value will be later used in virtual machine definition in host device specification

```
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec:
  permittedHostDevices:
    pciHostDevices:
    - pciDeviceSelector: "10de:25b6"
      resourceName: "nvidia/my-gpu"
```

Make sure that systemHealthStatus is "healthy" after the change and resource name is listed on the node with GPU device

```
$ oc describe node bm5
Name:               bm5
Roles:              control-plane,master,worker
Capacity:
  nvidia/my-gpu:                  4
Allocatable:
  nvidia/my-gpu:                  4
```

[[Back]](./README.md)