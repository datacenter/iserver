# MetalLB - Community

[[Back]](../README.md) [[iserver-way]](../create_community.md)

`Community` custom resource defines named aliases for community values that can be used in [BGPAdvertisement](./adv.md) `spec.communities`.

Refer to [documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html-single/ingress_and_load_balancing/index#metallb-configure-community-alias) for complete spec.

## CRD Example

```
apiVersion: metallb.io/v1beta1
kind: Community
metadata:
  name: community1
  namespace: metallb-system
spec:
  communities:
    - name: NO_ADVERTISE
      value: '65535:65282'
```

## How to use (BGPAdvertisement)

```
apiVersion: metallb.io/v1beta1
kind: BGPAdvertisement
metadata:
  name: bgp-community-sample
  namespace: metallb-system
spec:
  communities:
    - NO_ADVERTISE
```

[[Back]](../README.md) [[iserver-way]](../create_community.md)