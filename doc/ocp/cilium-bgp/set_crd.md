# Cilium BGP Control Plane - Set CRDs

## Workflow

- check cilium cni
- check bgp control plane enabled
- get bgp control plane related crds from input file
- apply one-by-one

## Requirements

None

## Configurable options

```
# iserver set ocp cilium bgp --mode crd
  --cluster TEXT     Cluster Name
  --filename TEXT    CRD filename
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp cilium bgp --cluster bm1 --mode crd --filename C:\tmp\bgp-bm1.yaml

OpenShift Workflow - Cilium BGP Control Plane - Apply configuration
===================================================================

OpenShift Cluster: bm1

~~~
apiVersion: isovalent.com/v1
kind: IsovalentBGPClusterConfig
metadata:
  name: aci
spec:
  bgpInstances:
  - localASN: 64661
    name: aci
    peers:
    - name: leaf_a
      peerASN: 64001
      peerAddress: 10.10.10.20
      peerConfigRef:
        name: aci
    - name: leaf_b
      peerASN: 64001
      peerAddress: 10.10.10.21
      peerConfigRef:
        name: aci
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPPeerConfig
metadata:
  name: aci
spec:
  ebgpMultihop: 1
  families:
  - advertisements:
      matchLabels:
        advertise: aci
    afi: ipv4
    safi: unicast
  timers:
    connectRetryTimeSeconds: 5
    holdTimeSeconds: 9
    keepAliveTimeSeconds: 3
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPAdvertisement
metadata:
  labels:
    advertise: aci
  name: aci
spec:
  advertisements:
  - advertisementType: PodCIDR
  - advertisementType: Service
    selector:
      matchExpressions:
      - key: bgp
        operator: In
        values:
        - advertise
    service:
      addresses:
      - LoadBalancerIP

~~~
Continue [Y/N]? y
IsovalentBGPClusterConfig aci updated
IsovalentBGPPeerConfig aci updated
IsovalentBGPAdvertisement aci updated
```

[[Back]](./README.md)