# CNI

## OVNKubernetes (default)

Configuration

```
    "network_type": "OVNKubernetes"
```

## Cilium

Configuration:
```
    "network_type": "Cilium"
```

Requirements:
- Cilium requires manifests subdirectory that have to be created manually based on the Cilium manifests package for OpenShift

Settings:
- Cilium configuration settings can be in dedicated cilium.json file or in cilium json structure within cluster.json file.
- default settings

```
    "cilium": {
        "verify": true,
        "manage": true,
        "cidr": true
    }
```

- if cilium:verify is false, then no checks on manifests on top of the existence of files
- if cilium:verify is true, then manifests files are read and one file with CiliumConfig CR must be found with CIDR settings aligned with cluster.json
- if cilium:manage is false, then no modifications are made to any of manifest files
- if cilium:manage is true, then flag-controller changes are made to manifest files
- if cilium:cidr is true, then CiliumConfig CR ipam section is (re)created based on cluster.json

Example generated CiliumConfig CR spec based on cilium:cidr

```
kind: CiliumConfig
spec:
  ipam:
    mode: cluster-pool
    operator:
      clusterPoolIPv4MaskSize: 23
      clusterPoolIPv4PodCIDRList: 10.128.0.0/14
```

[Back](../BareMetalCluster.md)
