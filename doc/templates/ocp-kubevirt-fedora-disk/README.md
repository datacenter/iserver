# OpenShift Virtualization

## Fedora Test Results - Extra Disks

Deployment files
- [virtual machine](../../tests/ocp/kubevirt/fedora/fedora06-vm.yaml)
- [service](../../tests/ocp/kubevirt/fedora/fedora06-svc.yaml)

Features
- 1 vCPU
- 1G RAM
- 1x 30G Disk
- Virtual Machine image based on existing pvc
- Extra Disks
- Cloud-init with ssh credentials
- Single interface (pod networking)

## Results

OpenShift Client (oc) outputs
- [Virtual Machine](./OcVm.md)
- [Virtual Machine Instance](./OcVmi.md)
- [Virtual Machine Launcher Pod](./OcPod.md)
- [Persistent Volume](./OcPv.md)
- [Persistent Volume Claim](./OcPvc.md)
- [Data Volume](./OcDv.md)

Other outputs
- [KVM Domain](./OcKvm.md)
