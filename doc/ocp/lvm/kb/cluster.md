# LVM Storage - Cluster

[[Back]](../README.md) [[operator]](./operator.md) [[iserver-way]](../create_cluster.md)


## Runtime Dynamic

```yaml
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: lvmcluster
  namespace: openshift-storage
spec:
  storage:
    deviceClasses:
    - default: false
      fstype: xfs
      name: vg1
      thinPoolConfig:
        chunkSizeCalculationPolicy: Static
        metadataSizeCalculationPolicy: Host
        name: thin-pool-1
        overprovisionRatio: 10
        sizePercent: 90
```

[[Back]](../README.md) [[operator]](./operator.md) [[iserver-way]](../create_cluster.md)