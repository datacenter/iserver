# Cilium Cluster Mesh - Delete cluster

## Workflow

- check cilium cni operator state
- check current cilium configuration if cilium mesh is enabled
- check if selected cluster is configured 
- delete if needed
- restart cilium operators and agents
- wait for cilium resources to be back up

## Requirements

None

## Configurable options

```
# iserver delete ocp cilium mesh --mode cluster
  --cluster TEXT            Cluster Name
  --mesh-name TEXT          Cluster mesh name
  --mesh-ip TEXT            Cluster mesh ip
  --no-confirm              Confirmation mode
```

## Non-configurable defaults

```
{
    "namespace": "cilium",
    "package": "clife"
}
```

## Example

```
# iserver delete ocp cilium mesh --cluster bm1 --mode cluster --mesh-name inb

OpenShift Workflow - Cilium - Delete Cluster from Mesh
======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "mesh-name": "inb",
    "mesh-ip": null,
    "confirmation": true,
    "check-verbose": true,
    "namespace": "cilium",
    "package": "clife"
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok



Operator
--------
- subscription          : cilium/clife
- package               : openshift-marketplace/certified-operators/clife
- channel               : 1.17
- install plan          : cilium/install-v6tpt
- install plan approved : ✓
- installed csv         : clife.v1.17.9-cee.1
- latest_csv            : ✓


Cluster mesh enabled

Cluster to be deleted

~~~
ips:
- 10.10.10.20
name: inb
port: 32380

~~~

Cilium config update
--------------------
CiliumConfig CRD patched
Take a nap to detect automatic deployment restart...
Fallback to forced reload
Deployment [cilium/cilium-operator] patch successful
Daemon set [cilium/cilium] patch successful

Wait for Cilium resources
-------------------------
- pod: cilium-568s4
- pod: cilium-envoy-7c2z7
- pod: cilium-envoy-sm8bk
- pod: cilium-envoy-th29g
- pod: cilium-gvn85
- pod: cilium-knlvn
- pod: cilium-operator-96b744f4b-dd7ws
- pod: cilium-operator-96b744f4b-vt6cc
- pod: clife-controller-manager-7b4dd4bb46-nslcj
- pod: clustermesh-apiserver-869796877-k6h7h
- deployment: cilium-operator
- deployment: clife-controller-manager
- deployment: clustermesh-apiserver

Completed tasks
- Cluster mesh deleted
```

[[Back]](./README.md)