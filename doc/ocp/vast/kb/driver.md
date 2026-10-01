# VAST CSI - VastCSIDriver

[[Back]](../README.md) [[iserver-way]](../create_driver.md) [[Next]](./cluster.md)

`VastCSIDriver` is custom resource introduced by [operator](./operator.md) with common specification for the VAST CSI Controller and VAST CSI Node

> [!NOTE]
> VastCDIDriver **must** be in the same namespace as operator

## Example

```
apiVersion: storage.vastdata.com/v1
kind: VastCSIDriver
metadata:
  name: csi.vastdata.com
  namespace: vast-csi
spec:
  driverType: "nfs"
  image:
    csiVastPlugin:
      repository: docker.io/vastdataorg/csi:v2.6.4
```

[[Back]](../README.md) [[iserver-way]](../create_driver.md) [[Next]](./cluster.md)