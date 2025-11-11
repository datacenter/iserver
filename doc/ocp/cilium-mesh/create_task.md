# Cilium Cluster Mesh - Create via Task

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
          "mesh-ip": "10.10.10.100,
          "mesh-port": 32380,
          "mesh-name": "inb",
          "wait": false
        }
      ],
      "timescape": {}
    }
  }
]
```

Notes:
- [feature](./enable.md), [cluster](./create_cluster.md) and [timescape](./enable_timescape.md) trigger workflow execution with optional input parameters
- feature.ca-crt and feature.ca-key filenames
  - can be relative and then expected to be in the same directory as task.json file
  - can be absolute
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

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

## Expected outcome

- cilium mesh enabled
- cluster mesh defined

## Example

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm


OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Cilium - Enable Cluster Mesh
=================================================

Workflow Parameters
-------------------
{
    "mesh-id": 1,
    "mesh-name": "ocp",
    "mesh-port": 32379,
    "cluster": "bm1",
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
~~~
apiVersion: cilium.io/v1alpha1
kind: CiliumConfig
metadata:
  labels:
    app.kubernetes.io/name: clife
  name: ciliumconfig
  resourceVersion: '2344018'
spec:
  cluster:
    id: 1
    name: ocp
  clusterHealthPort: 9940
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
  cni:
    binPath: /var/lib/cni/bin
    chainingMode: portmap
    confPath: /var/run/multus/cni/net.d
    exclusive: false
  enterprise:
    featureGate:
      approved:
      - CNIChainingMode
      strict: false
    privateNetworks:
      enabled: true
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
- pod: clustermesh-apiserver-869796877-hwfjt
- deployment: cilium-operator
- deployment: clife-controller-manager
- deployment: clustermesh-apiserver

Completed tasks
- Root CA secret created
- Certificate manager resources created
- Cluster mesh enabled

OpenShift Workflow - Cilium - Add Cluster to Mesh
=================================================

Workflow Parameters
-------------------
{
    "mesh-ip": "10.10.10.100",
    "mesh-port": 32380,
    "mesh-name": "inb",
    "cluster": "bm1",
    "confirmation": false,
    "wait": true,
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


Cilium config update
--------------------
CiliumConfig CRD patched
Take a nap to detect automatic deployment restart...
Fallback to forced reload
Deployment [cilium/cilium-operator] patch successful
Daemon set [cilium/cilium] patch successful

Wait for Cilium resources
-------------------------
- pod: cilium-envoy-7c2z7
- pod: cilium-envoy-sm8bk
- pod: cilium-envoy-th29g
- pod: cilium-operator-6cdf5b7d-hbqkd
- pod: cilium-operator-6cdf5b7d-khftp
- pod: cilium-whlpv
- pod: cilium-wpf4p
- pod: cilium-zfhnn
- pod: clife-controller-manager-7b4dd4bb46-nslcj
- pod: clustermesh-apiserver-869796877-hwfjt
- deployment: cilium-operator
- deployment: clife-controller-manager
- deployment: clustermesh-apiserver

Wait for cluster [inb] connected...

+----+--------------+------------+--------------+--------------+---------+--------------+-------+-------------+-------+
| ID | Cluster Name | Cluster ID | Cluster IP   | Cluster Port | Summary | Cilium Agent | Node  | Node IP     | Ready |
+----+--------------+------------+--------------+--------------+---------+--------------+-------+-------------+-------+
| 1  | inb          | 2          | 10.10.10.100 | 32380        | 3/3     | cilium-zfhnn | bm1-1 | 10.20.20.17 | ✓     | 
|    |              |            |              |              |         | cilium-whlpv | bm1-2 | 10.20.20.18 | ✓     | 
|    |              |            |              |              |         | cilium-wpf4p | bm1-3 | 10.20.20.19 | ✓     | 
+----+--------------+------------+--------------+--------------+---------+--------------+-------+-------------+-------+

Completed tasks
- Cluster mesh added
```

[[Back]](./README.md)