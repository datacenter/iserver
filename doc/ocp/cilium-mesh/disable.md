# Cilium Cluster Mesh - Disable feature

## Workflow

- check cilium cni operator state
- check current cilium configuration if cilium mesh is configured
- delete spec.cluster.id, spec.cluster.name and spec.clustermesh
- restart cilium operators and agents
- wait for cilium resources to be back up
- delete certificate manager resources 
- delete certificate manager secret 
- deleted root CA secret 

## Requirements

None

## Expected outcome

```
$ cilium status -n cilium
    /¯¯\
 /¯¯\__/¯¯\    Cilium:             OK
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Envoy DaemonSet:    OK
 \__/¯¯\__/    Hubble Relay:       disabled
    \__/       ClusterMesh:        disabled
```

```
$ cilium clustermesh status -n cilium
⚠️  Cluster not configured for clustermesh, use '--set cluster.id' and '--set cluster.name' with 'cilium install'
```

## Configurable options

```
# iserver delete ocp cilium mesh --mode feature
  --cluster TEXT     Cluster Name
```

## Non-configurable defaults

```
{
    "namespace": "cilium",
    "package": "clife",
    "secret": "cilium-ca-root",
    "certificate": "cilium-ocp",
    "certificate-admin": "clustermesh-apiserver-admin-cert",
    "certificate-remote": "clustermesh-apiserver-remote-cert",
    "certificate-server": "clustermesh-apiserver-server-cert"
}
```

## Example

```
# iserver delete ocp cilium mesh --cluster bm1 --mode feature --no-confirm


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
- pod: cilium-4dghb
- pod: cilium-72gb8
- pod: cilium-envoy-7c2z7
- pod: cilium-envoy-sm8bk
- pod: cilium-envoy-th29g
- pod: cilium-operator-7fbd986d87-2chzc
- pod: cilium-operator-7fbd986d87-89htm
- pod: cilium-sz4qd
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