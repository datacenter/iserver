# Cilium Cluster Mesh - Delete via Task

## Input

```
[
  {
    "cilium-mesh": {
      "feature": {
        "mesh-id": 1,
        "mesh-name": "ocp",
        "mesh-port": 32379,
        "ca-crt": "filename-crt",
        "ca-key": "filename-key"
      },
      "cluster": [
        {
          "mesh-ip": "10.10.10.10,
          "mesh-port": 32380,
          "mesh-name": "inb"
        }
      ],
      "timescape": {}
    }
  }
]
```

Notes:
- [timescape](./disable_timescape.md), [cluster](./delete_cluster.md) and [feature](./disable.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters may be silently ignored
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

## Requirements

None

## Configurable options

```
# iserver delete ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Expected outcome

- timescape mesh disabled
- cluster mesh deleted
- associated certificate manager and secrets deleted

## Example

```
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json 
Cluster: bm1 (type: ocp)

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Cilium - Delete Cluster from Mesh
======================================================

Workflow Parameters
-------------------
{
    "mesh-ip": "10.58.28.208",
    "mesh-name": "inb",
    "cluster": "bm1",
    "confirmation": true,
    "check-verbose": true,
    "namespace": "cilium",
    "package": "clife",
    "secret": "cilium-ca-root",
    "certificate": "cilium-ocp",
    "certificate-admin": "clustermesh-apiserver-admin-cert",
    "certificate-remote": "clustermesh-apiserver-remote-cert",
    "certificate-server": "clustermesh-apiserver-server-cert"
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
- 10.58.28.208
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
- pod: cilium-5v6t8
- pod: cilium-envoy-7c2z7
- pod: cilium-envoy-sm8bk
- pod: cilium-envoy-th29g
- pod: cilium-n7784
- pod: cilium-operator-6dd645ff7c-7wbjv
- pod: cilium-operator-6dd645ff7c-qsx4t
- pod: cilium-zdd6b
- pod: clife-controller-manager-7b4dd4bb46-nslcj
- pod: clustermesh-apiserver-869796877-rhprx
- deployment: cilium-operator
- deployment: clife-controller-manager
- deployment: clustermesh-apiserver

Completed tasks
- Cluster mesh deleted


OpenShift Workflow - Cilium - Disable Cluster Mesh
==================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "cilium",
    "package": "clife",
    "secret": "cilium-ca-root",
    "certificate": "cilium-ocp",
    "certificate-admin": "clustermesh-apiserver-admin-cert",
    "certificate-remote": "clustermesh-apiserver-remote-cert",
    "certificate-server": "clustermesh-apiserver-server-cert"
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


Cluster mesh will be disabled
- spec.cluster.id deleted
- spec.cluster.name deleted
- spec.cluster
- spec.clustermesh deleted

Cilium config update
--------------------
CiliumConfig CRD patched
Take a nap to detect automatic deployment restart...
Automatic pods rollout detected

Wait for Cilium resources
-------------------------
- pod: cilium-5v6t8
- pod: cilium-envoy-7c2z7
- pod: cilium-envoy-sm8bk
- pod: cilium-envoy-th29g
- pod: cilium-n7784
- pod: cilium-operator-6dd645ff7c-7wbjv
- pod: cilium-operator-6dd645ff7c-qsx4t
- pod: cilium-zdd6b
- pod: clife-controller-manager-7b4dd4bb46-nslcj
- deployment: cilium-operator
- deployment: clife-controller-manager

Delete Certificate
------------------
- namespace: cilium
- name: cilium-ocp
- wait for no certificate

Delete Issuer
-------------
- namespace: cilium
- name: cilium
- wait for no issuer

Delete Issuer
-------------
- namespace: cilium
- name: cilium-ca-root
- wait for no issuer

Delete Certificate
------------------
- namespace: cilium
- name: clustermesh-apiserver-admin-cert
- wait for no certificate

Delete Certificate
------------------
- namespace: cilium
- name: clustermesh-apiserver-remote-cert
- wait for no certificate

Delete Certificate
------------------
- namespace: cilium
- name: clustermesh-apiserver-server-cert
- wait for no certificate

Delete Secret
-------------
- namespace: cilium
- name: cilium-ca-root
- wait for no secret

Delete Secret
-------------
- namespace: cilium
- name: cilium-ocp
- wait for no secret

Delete Secret
-------------
- namespace: cilium
- name: clustermesh-apiserver-admin-cert
- wait for no secret

Delete Secret
-------------
- namespace: cilium
- name: clustermesh-apiserver-remote-cert
- wait for no secret

Delete Secret
-------------
- namespace: cilium
- name: clustermesh-apiserver-server-cert
- wait for no secret

Completed tasks
- Cluster mesh disabled
- Certificate manager resources deleted
- Root CA and certificate manager secrets deleted
```

[[Back]](./README.md)