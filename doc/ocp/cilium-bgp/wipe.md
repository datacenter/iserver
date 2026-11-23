# Cilium BGP Control Plane - Wipe all CRDs

## Workflow

- check cilium cni
- check bgp control plane enabled
- delete all bgp control plane related crds

## Requirements

None

## Configurable options

```
# iserver delete ocp cilium bgp --mode wipe
  --cluster TEXT     Cluster Name
```

## Example

```
# iserver set ocp cilium bgp --cluster bm1 --mode wipe

OpenShift Workflow - Cilium BGP Control Plane - Wipe
====================================================

OpenShift Cluster: bm1

IsovalentBGPAdvertisement advertise-cluster deleted
IsovalentBGPAdvertisement advertise-ext deleted
IsovalentBGPAdvertisement advertise-lb deleted
IsovalentBGPAdvertisement advertise-pod deleted
IsovalentBGPPeerConfig peer deleted
IsovalentBGPClusterConfig cluster deleted

Completed tasks
- All BGP control plane configuration crds deleted
```

[[Back]](./README.md)