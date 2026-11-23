# OVNKubernetes BGP - Cluster User Defined Network (L3) w/VRF-Lite

[[Back]](./README.md) 

## OVN-K routing via host

BGP VRF-Lite setup [requires](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/advanced_networking/route-advertisements#advertising-pod-ips-from-a-user-defined-network-over-bgp-with-vpn_about-route-advertisements) `routingViaHost=true` in the `ovnKubernetesConfig.gatewayConfig` specification of the OVN-Kubernetes network plugin.

```
# oc patch networks.operator.openshift.io cluster --type=merge -p '{"spec":{"defaultNetwork":{"ovnKubernetesConfig":{"gatewayConfig":{"routingViaHost": true}}}}}'
```

```
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  defaultNetwork:
    gatewayConfig:
      routingViaHost: true
```

[[Back]](./README.md) 