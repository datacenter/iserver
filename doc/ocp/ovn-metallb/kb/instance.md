# MetalLB - Instance

[[Back]](../README.md) [[iserver-way]](../create_instance.md)

When you add a `MetalLB` custom resource to the cluster, the MetalLB [Operator](./operator.md) deploys MetalLB on the cluster. 

> [!NOTE]
> a single instance of the `MetalLB` custom resource supported

Refer to [documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/networking_operators/metallb-operator#nw-metallb-operator-deployment-specifications-for-metallb_metallb-operator-install) for possible control on how the MetalLB controller and speaker pods deploy and run in OpenShift Container Platform.

## Example

```
apiVersion: metallb.io/v1beta1
kind: MetalLB
metadata:
  name: metallb
  namespace: metallb-system
spec:
  bgpBackend: frr
```

## bgpBackend summary

> [!CAUTION]
> `frr-k8s` bgpBackend seems to be completely broken in OCP4.21.4

bgpBackend | metallb l3 | ovn-bgp integration | frr 
--- | --- | --- | ---
undefined | :white_check_mark: | :white_check_mark: | `openshift-frr-k8s` namespace
frr | :white_check_mark: | :x: | `metallb-system` speaker
native | :x: | :x: | can be deployed using [ovn-bgp](../../ovn-bgp/README.md)

[undefined](./backend_undefined.md)
- [ovn-bgp](../../ovn-bgp/README.md) automatically enabled i.e., `openshift-frr-k8s` created, `frr-k8s` enabled, frr deployed
  - if ovn-bgp is pre-enabled, then things are still working fine
- metallb speaker pods **without** frr
- [BGPPeer](./bgp_peer.md) generates per-host `FRRConfiguration` objects
- standalone `FRRConfiguration` objects supported and configure frr instance
- proper metallb + ovn-bgp integrated mode

[native](./backend_native.md)
- [ovn-bgp](../../ovn-bgp/README.md) **not enabled**
- metallb speaker pods **without** frr
- effectively disables bgp features with metallb - l2 mode

[frr](./backend_frr.md)
- [ovn-bgp](../../ovn-bgp/README.md) **not enabled automatically**
- metallb speaker pods **with** frr
- [BGPPeer](./bgp_peer.md) configures generates per-host `FRRConfiguration` objects
- standalone `FRRConfiguration` objects effectively **unsupported** since do not change speaker's frr instance configuration
- not the right mode if you want ovn-bgp

[frr-k8s](./backend_frr_k8s.md)
- [ovn-bgp](../../ovn-bgp/README.md) **not enabled automatically**
- metallb speaker pods **without** frr
- frr deployed in dedicated pods but keep on **crashing** or **pending** depending on ovn-bgp

[[Back]](../README.md) [[iserver-way]](../create_instance.md)