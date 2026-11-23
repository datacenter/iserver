# Cilium BGP Control Plane - Enable feature

## Workflow

- check cilium cni operator state
- check current cilium configuration
- enable BGP control plane in cilium configuration
- wait for crd

## Requirements

None

## Configurable options

```
# iserver set ocp cilium bgp --mode feature
  --cluster TEXT   Cluster Name
  --no-confirm     Confirmation mode
```

## Example

```
# iserver set ocp cilium bgp --cluster bm1 --mode feature


OpenShift Workflow - Cilium BGP Control Plane - Enable
======================================================

OpenShift Cluster: bm1
Cilium cni found

Enable BGP Control Plane
------------------------
~~~
enterprise:
  bgpControlPlane:
    enabled: true

~~~

Cilium config update
--------------------
~~~
apiVersion: cilium.io/v1alpha1
kind: CiliumConfig
metadata:
  labels:
    app.kubernetes.io/name: clife
  name: ciliumconfig
  resourceVersion: '46035617'
spec:
  cluster:
    name: default
...
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
- pod: cilium-5b6w9
- pod: cilium-b4h6w
- pod: cilium-cgmtc
- pod: cilium-envoy-bvb7h
- pod: cilium-envoy-nw4ds
- pod: cilium-envoy-vwmjc
- pod: cilium-operator-6bc9648446-49qn6
- pod: cilium-operator-6bc9648446-v5lxn
- pod: clife-controller-manager-559df4fc56-2278s
- deployment: cilium-operator
- deployment: clife-controller-manager
Wait for IsovalentBGPClusterConfig CRD
BGP Control Plane CRDs found

Completed tasks
- BGP Control Plane feature enabled
- CRD ready
```

[[Back]](./README.md)