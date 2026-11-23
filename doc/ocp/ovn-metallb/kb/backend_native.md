# MetalLB - Instance bgpBackend native

[[Back]](./instance.md) [[undefined]](./backend_undefined.md) [[native]](./backend_native.md) [[frr]](./backend_frr.md) [[frr-k8s]](./backend_frr_k8s.md)

> [!NOTE]
> OCP4.21.4 with OVNKubernetes CNI

```
apiVersion: metallb.io/v1beta1
kind: MetalLB
metadata:
  name: metallb
  namespace: metallb-system
spec:
  bgpBackend: native
```

Observations
- [ovn-bgp](../../ovn-bgp/README.md) **not enabled**
- metallb speaker pods **without** frr
- effectively disables bgp features with metallb - l2 mode

[[Back]](./instance.md) [[undefined]](./backend_undefined.md) [[native]](./backend_native.md) [[frr]](./backend_frr.md) [[frr-k8s]](./backend_frr_k8s.md)