# Node Feature Discovery Operator - Get

## Workflow

- get nfd operator state
- get node annotations with --verbose option

## Example

```
# iserver get ocp nfd --verbose

OpenShift Workflow - Node Feature Discover Operator - Get Information
=====================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "verbose": true,
    "check-verbose": true,
    "namespace": "openshift-nfd",
    "name": "nfd",
    "operator-group-name": "nfd-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

Operator
--------
- subscription: openshift-nfd/nfd
- channel: stable
- csv: nfd.4.18.0-202509240837
- instance: nfd-instance

Operator functional readiness
-----------------------------
ready

NFD node annotations
--------------------
- node [ocp-bm1]
        cpu-cpuid.ADX
        cpu-cpuid.AESNI
        cpu-cpuid.AMXFP8
        cpu-cpuid.AVX
        cpu-cpuid.AVX2
        cpu-cpuid.AVX512BW
        cpu-cpuid.AVX512CD
        cpu-cpuid.AVX512DQ
        cpu-cpuid.AVX512F
        cpu-cpuid.AVX512VL
        cpu-cpuid.AVX512VNNI
        cpu-cpuid.CMPXCHG8
        cpu-cpuid.FLUSH_L1D
        cpu-cpuid.FMA3
        cpu-cpuid.FXSR
        cpu-cpuid.FXSROPT
        cpu-cpuid.IA32_ARCH_CAP
        cpu-cpuid.IBPB
        cpu-cpuid.LAHF
        cpu-cpuid.MD_CLEAR
        cpu-cpuid.MOVBE
        cpu-cpuid.MPX
        cpu-cpuid.OSXSAVE
        cpu-cpuid.SPEC_CTRL_SSBD
        cpu-cpuid.STIBP
        cpu-cpuid.SYSCALL
        cpu-cpuid.SYSEE
        cpu-cpuid.VMX
        cpu-cpuid.X87
        cpu-cpuid.XGETBV1
        cpu-cpuid.XSAVE
        cpu-cpuid.XSAVEC
        cpu-cpuid.XSAVEOPT
        cpu-cpuid.XSAVES
        cpu-cstate.enabled
        cpu-hardware_multithreading
        cpu-model.family
        cpu-model.id
        cpu-model.vendor_id
        cpu-pstate.scaling_governor
        cpu-pstate.status
        cpu-pstate.turbo
        kernel-config.NO_HZ
        kernel-config.NO_HZ_FULL
        kernel-selinux.enabled
        kernel-version.full
        kernel-version.major
        kernel-version.minor
        kernel-version.revision
        memory-numa
        network-sriov.capable
        pci-102b.present
        pci-1137.present
        pci-8086.present
        pci-8086.sriov.capable
        storage-nonrotationaldisk
        system-os_release.ID
        system-os_release.OPENSHIFT_VERSION
        system-os_release.OSTREE_VERSION
        system-os_release.RHEL_VERSION
        system-os_release.VERSION_ID
        system-os_release.VERSION_ID.major
        system-os_release.VERSION_ID.minor
```

[[Back]](./README.md)