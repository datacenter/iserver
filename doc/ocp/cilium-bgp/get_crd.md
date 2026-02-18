# Cilium BGP Control Plane - Get CRDs

## Workflow

- get bgp control plane configuration yaml

## Requirements

None

## Configurable options

```
# iserver get ocp cilium bgp -v crd
  --cluster TEXT     Cluster Name
```

## Example

```
# iserver get ocp cilium bgp --cluster bm1 -v crd

OpenShift Workflow - Cilium BGP Control Plane - Get
===================================================

OpenShift Cluster: bm1

~~~
apiVersion: isovalent.com/v1
kind: IsovalentBGPClusterConfig
metadata:
  name: cluster
spec:
  bgpInstances:
  - localASN: 64661
    name: bgp
    peers:
    - name: tor1
      peerASN: 64001
      peerAddress: 10.10.10.20
      peerConfigRef:
        name: peer
    - name: tor2
      peerASN: 64001
      peerAddress: 10.10.10.21
      peerConfigRef:
        name: peer
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPPeerConfig
metadata:
  name: peer
spec:
  ebgpMultihop: 5
  families:
  - advertisements:
      matchLabels:
        advertise: bgp
    afi: ipv4
    safi: unicast
  gracefulRestart:
    enabled: true
    restartTimeSeconds: 120
  timers:
    connectRetryTimeSeconds: 5
    holdTimeSeconds: 9
    keepAliveTimeSeconds: 3
  transport:
    peerPort: 179
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPAdvertisement
metadata:
  labels:
    advertise: bgp
  name: advertise-cluster
spec:
  advertisements:
  - advertisementType: Service
    selector:
      matchExpressions:
      - key: bgp
        operator: In
        values:
        - aaa
        - bbb
    service:
      addresses:
      - ClusterIP
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPAdvertisement
metadata:
  labels:
    advertise: bgp
  name: advertise-ext
spec:
  advertisements:
  - advertisementType: Service
    selector:
      matchExpressions:
      - key: dummy
        operator: NotIn
        values:
        - dummy
    service:
      addresses:
      - ExternalIP
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPAdvertisement
metadata:
  labels:
    advertise: bgp
  name: advertise-lb
spec:
  advertisements:
  - advertisementType: Service
    selector:
      matchExpressions:
      - key: dummy
        operator: NotIn
        values:
        - dummy
    service:
      addresses:
      - LoadBalancerIP
      aggregationLengthIPv4: 24
      aggregationLengthIPv6: 100
---
apiVersion: isovalent.com/v1
kind: IsovalentBGPAdvertisement
metadata:
  labels:
    advertise: bgp
  name: advertise-pod
spec:
  advertisements:
  - advertisementType: PodCIDR
    attributes:
      communities:
        standard:
        - 64661:100
        wellKnown:
        - blackhole
~~~
```

[[Back]](./README.md)