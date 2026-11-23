# OpenShift with Cilium CNI - Automated Fixups

[Back](../BareMetalCluster.md)

OpenShift cluster installation with Cilium CNI requires Cilium EE manifests to be part of the installation directory intent. One of the manifest file is CiliumConfig CRD that may need to be modified for two reasons
- ipam section defines cluster pool cidr and mask and that must be aligned with the same settings defined on OpenShift level
- operator replicas is by default two and if you are installing single node openshift, it should be changed to one

CiliumConfig CRD example showing the automatically added settings only

```yaml
kind: CiliumConfig
metadata:
  name: ciliumconfig
spec:
  ipam:
    operator:
      clusterPoolIPv4MaskSize: 23
      clusterPoolIPv4PodCIDRList:
      - "10.128.0.0/14"
  operator:
    replicas: 1
```

The way to disable automated fixups in cluster.json file:

```json
{
    "cilium": {
        "managed": false
    }
}
```

[Back](../BareMetalCluster.md)