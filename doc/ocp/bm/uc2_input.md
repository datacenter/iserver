# OpenShift Cluster with Cilium CNI

## Input Files

The cluster deployed and configured based on the following files
- [cluster.json](./uc2_cluster.md) definining cluster and tasks intent
- [bonding.yaml](./uc2_bonding.md) for interface pair with vlan connection to data center fabric
- manifests directory created with Cilium OSS or Cilium EE manifests
- no modification to Cilium manifests files required

iserver by default searches for manifest file with CiliumConfig CR and updates its content with CIDR specification matching OpenShift cluster CIDR [settings](./uc2_cluster.md)

```
kind: CiliumConfig
spec:
  ipam:
    mode: cluster-pool
    operator:
      clusterPoolIPv4MaskSize: 23
      clusterPoolIPv4PodCIDRList: 10.128.0.0/14
```

[Back](./uc2.md)