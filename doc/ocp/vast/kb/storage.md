# VAST CSI - VastStorage

[[Back]](../README.md) [[iserver-way]](../create_storage.md) [[Next]](./operator.md)

`VastStorage` defines VAST storage options to be used when provisioning volumes on the VAST cluster. This resource generates a storage class (and optionally a snapshot class) that you can use in your PVCs.

Generated storage class can be set to default with `"setDefaultStorageClass": true` property.

> [!NOTE]
> VastCluster **must** be in the same namespace as operator

## Example

```
apiVersion: storage.vastdata.com/v1
kind: VastStorage
metadata:
  name: vast-nfs
  namespace: vast-csi
spec:
  allowVolumeExpansion: true
  createSnapshotClass: true
  deletionViewPolicy: nfs-policy
  driverType: nfs
  provisioner: nfs
  secretName: my-vast
  secretNamespace: vast-csi
  storagePath: /my-nfs-path
  viewPolicy: nfs-policy
  vipPool: pool-01
  setDefaultStorageClass: true
```

[[Back]](../README.md) [[iserver-way]](../create_storage.md) [[Next]](./operator.md)