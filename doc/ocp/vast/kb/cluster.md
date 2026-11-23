# VAST CSI - VastCluster

[[Back]](../README.md) [[iserver-way]](../create_cluster.md) [[Next]](./storage.md)

`VastCluster` specifies the VAST endpoint and credentials to connect to the VAST cluster where volumes will be provisioned. These settings are stored in a VAST CSI Driver's Kubernetes secret.

> [!NOTE]
> VastCluster **must** be in the same namespace as operator

## Example

```
apiVersion: storage.vastdata.com/v1
kind: VastCluster
metadata:
  name: my-vast
  namespace: vast-csi
spec:
  endpoint: my-vast.domain.com
  password: password
  username: admin
```

[[Back]](../README.md) [[iserver-way]](../create_cluster.md) [[Next]](./storage.md)