# Cilium Isovalent Network Bridge - Disable feature

## Workflow

- check cilium cni operator state
- check current cilium configuration 
- select cluster mesh connection with inb selected by name (--mesh-name) or detected based on ssh and k8s connectors created by [enable](./enable.md) workflow
- delete inb k8s connector
- delete inb linux connector
- delete cluster mesh

Note: state of inb is not changed i.e., workflow is changing the ocp end of the cluster mesh as well as local iserver configurations

## Requirements

- Private network [enabled](../cilium-pnet/enable.md)
- Cluster mesh [enabled](../cilium-mesh/enable.md)

## Expected outcome

- openshift cluster mesh unconfigured
- Isovalent network bridge k8s and linux connectors deleted

## Configurable options

```
# iserver delete ocp cilium inb --mode feature
  --cluster TEXT       Cluster Name
  --mesh-name TEXT     Cluster mesh name
  --no-confirm         Confirmation mode
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
# iserver delete ocp cilium inb \
    --cluster bm1 \
    --mode feature \
    --mesh-name inb1 \
    --no-confirm


OpenShift Workflow - Cilium - Unconfigure Isovalent Network Bridge
==================================================================

OpenShift Cluster: bm1
Cilium CNI
Cluster mesh enabled
Private network enabled

inb: inb1
---------
Linux connector deleted: bm1-inb1
Kubernetes connector deleted: bm1-inb1

OpenShift Workflow - Cilium - Delete Cluster from Mesh
======================================================


OpenShift Cluster: bm1
Cilium CNI

Cluster mesh enabled

Cluster to be deleted

~~~
ips:
- 10.10.20.20
name: inb1
port: 32380

~~~

Cilium config update
--------------------
CiliumConfig CRD patched
Take a nap to detect automatic deployment restart...
Automatic pods rollout detected

Wait for Cilium resources
-------------------------
- pod: cilium-envoy-bwzml
- pod: cilium-envoy-gm8k5
- pod: cilium-envoy-v9jgx
- pod: cilium-gkjx6
- pod: cilium-operator-b5446b59f-sc2b8
- pod: cilium-operator-b5446b59f-vvrsn
- pod: cilium-qg27m
- pod: cilium-zzgj8
- pod: clife-controller-manager-6c79869f6c-gcj6l
- pod: clustermesh-apiserver-5fbcd5b558-gws27
- pod: hubble-timescape-0
- deployment: cilium-operator
- deployment: clife-controller-manager
- deployment: clustermesh-apiserver

Completed tasks
- Cluster mesh deleted

Completed tasks
- Cluster mesh deleted
- Isovalent network bridge k8s and linux connectors deleted
```
[[Back]](./README.md)