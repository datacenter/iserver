# Cilium BGP Control Plane - Delete via Task

## Input

```
[
  {
    "cilium-bgp": {
      "feature": {},
      "cluster": {},
      "wipe": {}
    }
  }
]
```

Note:
- all bgp control plane resources wiped if `wipe` or `feature` workflow defined
- cluster settings ignored

## Requirements

None

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example Output

```
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json 


OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


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

OpenShift Workflow - Cilium BGP Control Plane - Disable
=======================================================

OpenShift Cluster: bm1
Cilium cni found

Disable BGP Control Plane
-------------------------

Cilium config update
--------------------
~~~
apiVersion: cilium.io/v1alpha1
kind: CiliumConfig
metadata:
  labels:
    app.kubernetes.io/name: clife
  name: ciliumconfig
  resourceVersion: '46036818'
spec:
  cluster:
    name: default
  clusterHealthPort: 9940
  cni:
    binPath: /var/lib/cni/bin
    chainingMode: portmap
    confPath: /var/run/multus/cni/net.d
    exclusive: false
  enterprise:
    featureGate:
      approved:
      - CNIChainingMode
  hubble:
    enabled: true
  ipam:
    mode: cluster-pool
    operator:
      clusterPoolIPv4MaskSize: 23
      clusterPoolIPv4PodCIDRList:
      - 10.128.0.0/14
  kubeProxyReplacement: false
  operator:
    prometheus:
      enabled: true
      serviceMonitor:
        enabled: true
  prometheus:
    enabled: true
    serviceMonitor:
      enabled: true
  securityContext:
    privileged: true
  sessionAffinity: true
  tunnelPort: 4789

~~~
CiliumConfig CRD patched
Take a nap to check cilium config state and detect automatic deployment restart...
Cilium configuration valid
Forced agent reload
Forced operator reload
Deployment [cilium/cilium-operator] patch successful
Daemon set [cilium/cilium] patch successful

Wait for Cilium resources
-------------------------
- pod: cilium-2vm76
- pod: cilium-9w77z
- pod: cilium-envoy-bvb7h
- pod: cilium-envoy-nw4ds
- pod: cilium-envoy-vwmjc
- pod: cilium-mnlvr
- pod: cilium-operator-75c7d566dc-lz5xn
- pod: cilium-operator-75c7d566dc-rn2fb
- pod: clife-controller-manager-559df4fc56-2278s
- deployment: cilium-operator
- deployment: clife-controller-manager

Completed tasks
- BGP Control Plane feature disabled
```

[[Back]](./README.md)