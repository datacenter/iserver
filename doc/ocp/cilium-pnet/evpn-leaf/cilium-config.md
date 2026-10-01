# Cilium configuration

[[Back]](./README.md) [[Next]](./server-intf.md)

Required features
- bgp control plane with route import
- private network
- evpn
- vxlan tunnel port for east-west traffic changed from default 4789 e.g. 4790

```yaml
spec:
  enterprise:
    featureGate:
      approved:
      - CNIChainingMode
      - BGPControlPlane
      - BGPRouteImport
      - EVPN
      - EnterpriseBGPControlPlane
      - MultiNetwork
      - VTEPIntegration
      - PrivateNetworks
      strict: false
    bgpControlPlane:
      enabled: true
      routeImport:
        enabled: true
    evpn:
      enabled: true
    privateNetworks:
      enabled: true
  tunnelPort: 4790
```

[[Back]](./README.md) [[Next]](./server-intf.md)