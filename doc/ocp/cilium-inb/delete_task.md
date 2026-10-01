# Cilium Isovalent Network Bridge - Delete via Task

## Input

```
[
  {
    "cilium-inb": {
      "feature": {
        "mesh-name": "inb1"
      }
    }
  }    
]
```

Notes:
- [disable feature](./disable.md) workflow execution with input parameters
- you can reuse the same task definition as in [enable feature task](./create_task.md); all parameters except for mesh-name are ignored

## Requirements

As per [disable feature](./disable.md) documentation

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Expected outcome

- openshift cluster mesh unconfigured
- Isovalent network bridge k8s and linux connectors deleted

## Example

```
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json

Cluster: bm1 (type: ocp)

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


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
- pod: cilium-g76gc
- pod: cilium-jxw8b
- pod: cilium-operator-b5446b59f-sc2b8
- pod: cilium-operator-b5446b59f-vvrsn
- pod: cilium-qz87s
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