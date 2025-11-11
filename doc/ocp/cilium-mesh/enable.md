# Cilium Cluster Mesh - Enable feature

## Workflow

- check cilium cni operator state
- check current cilium configuration
- prepare root ca secret
- prepare certificate manager issuer and certificate resources
- enable cilium mesh with user provided cluster mesh id, name and node port
- restart cilium operators and agents
- wait for cilium resources to be back up

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
    \__/       ClusterMesh:        OK
```

## Configurable options

```
# iserver set ocp cilium mesh --mode feature
  --cluster TEXT            Cluster Name
  --mesh-id INTEGER         Cluster mesh id
  --mesh-name TEXT          Cluster mesh name
  --mesh-port INTEGER       Cluster mesh port
  --ca-crt TEXT             Root ca crt
  --ca-key TEXT             Root ca key
  --no-confirm              Confirmation mode
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
# iserver set ocp cilium mesh \
    --cluster bm1 \
    --mode feature \
    --mesh-id 1 \
    --mesh-name ocp \
    --mesh-port 32379 \
    --ca-crt C:\tmp\root-ca.crt \
    --ca-key C:\tmp\root-ca.key \
    --no-confirm

OpenShift Workflow - Cilium - Enable Cluster Mesh
=================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "mesh-id": 1,
    "mesh-name": "ocp",
    "mesh-port": 32379,
    "confirmation": false,
    "root-ca-crt": "user-provided",
    "root-ca-key": "user-provided",
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


Root CA Cert
------------
Cilium root ca secret
- namespace: cilium
- name: cilium-ca-root
- secret will be created based on user provided root ca crt and key

Create Secret
-------------
- namespace: cilium
- name: cilium-ca-root

Secret created

Wait for secret [timeout:60]...

Create Issuer
-------------
- namespace: cilium
- name: cilium-ca-root

~~~
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: cilium-ca-root
  namespace: cilium
spec:
  ca:
    secretName: cilium-ca-root

~~~
- issuer created
- wait until issuer found...

Create Certificate
------------------
- namespace: cilium
- name: cilium-ocp

~~~
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: cilium-ocp
  namespace: cilium
spec:
  commonName: cilium-ocp
  isCA: true
  issuerRef:
    group: cert-manager.io
    kind: Issuer
    name: cilium-ca-root
  secretName: cilium-ocp

~~~
- certificate created
- wait until certificate found...

Create Issuer
-------------
- namespace: cilium
- name: cilium

~~~
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: cilium
  namespace: cilium
spec:
  ca:
    secretName: cilium-ocp

~~~
- issuer created
- wait until issuer found...

Cluster mesh configuration
--------------------------
~~~
cluster:
  id: 1
  name: ocp
clustermesh:
  apiserver:
    kvstoremesh:
      enabled: false
    nodePort: 32379
    replicas: 1
    service: {}
    tls:
      authMode: cluster
      auto:
        certManagerIssuerRef:
          group: cert-manager.io
          kind: Issuer
          name: cilium
        certValidityDuration: 1
        enabled: true
        method: certmanager
    type: NodePort
  useAPIServer: true

~~~

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
- pod: clustermesh-apiserver-869796877-wpt4h
- deployment: cilium-operator
- deployment: clife-controller-manager
- deployment: clustermesh-apiserver

Completed tasks
- Root CA secret created
- Certificate manager resources created
- Cluster mesh enabled
```

```
# iserver get ocp cilium mesh --cluster bm1


OpenShift Workflow - Cilium - Get Mesh
======================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok


Cluster mesh configuration

~~~
apiserver:
  kvstoremesh:
    enabled: false
  nodePort: 32379
  replicas: 1
  service: {}
  tls:
    authMode: cluster
    auto:
      certManagerIssuerRef:
        group: cert-manager.io
        kind: Issuer
        name: cilium
      certValidityDuration: 1
      enabled: true
      method: certmanager
  type: NodePort
useAPIServer: true

~~~

+----+--------------+------------+------------+--------------+---------+--------------+------+---------+-------+
| ID | Cluster Name | Cluster ID | Cluster IP | Cluster Port | Summary | Cilium Agent | Node | Node IP | Ready |
+----+--------------+------------+------------+--------------+---------+--------------+------+---------+-------+
+----+--------------+------------+------------+--------------+---------+--------------+------+---------+-------+
```
[[Back]](./README.md)