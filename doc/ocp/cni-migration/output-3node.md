# Cilium EE migration example

## Command

```
iserver set ocp cni --mode cilium \
    --cluster bm1  \
    --cidr 10.253.0.0/16 \
    --host-prefix 24 \
    --manifest local-directory-with-cilium-ee-manifests \
    --no-confirm
```

## Output

```
OpenShift Workflow - Cilium CNI - Migration
===========================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "cidr": "10.253.0.0/16",
    "host_prefix": 24,
    "manifest": "local-directory-with-cilium-ee-manifests",
    "start": 1,
    "stop": 10,
    "confirmation": false,
    "check-verbose": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok


Step 1: Check cluster state and input parameters
================================================


OpenShift Network
-----------------
- Name            : cluster
- Network Type    : OVNKubernetes
- Cluster Network : 10.128.0.0/14
- Host Prefix     : 23
- Service Network : 172.30.0.0/16

Target cluster network does not overlap with ovn cluster network
Upstream interface of OVS switch: bond0.666

Collect Cluster Operators
-------------------------
- authentication [True]
- baremetal [True]
- cloud-controller-manager [True]
- cloud-credential [True]
- cluster-autoscaler [True]
- config-operator [True]
- console [True]
- control-plane-machine-set [True]
- csi-snapshot-controller [True]
- dns [True]
- etcd [True]
- image-registry [True]
- ingress [True]
- insights [True]
- kube-apiserver [True]
- kube-controller-manager [True]
- kube-scheduler [True]
- kube-storage-version-migrator [True]
- machine-api [True]
- machine-approver [True]
- machine-config [True]
- marketplace [True]
- monitoring [True]
- network [True]
- node-tuning [True]
- olm [True]
- openshift-apiserver [True]
- openshift-controller-manager [True]
- openshift-samples [True]
- operator-lifecycle-manager [True]
- operator-lifecycle-manager-catalog [True]
- operator-lifecycle-manager-packageserver [True]
- service-ca [True]
- storage [True]

Step 2: Disable cluster network operator
========================================


Disable network operator management
-----------------------------------

~~~
api: config.openshift.io/v1
kind: ClusterVersion
metadata:
  name: version
spec:
  overrides:
  - group: apps
    kind: Deployment
    name: network-operator
    namespace: openshift-network-operator
    unmanaged: true

~~~
Patch successful

Network Operator
----------------

+----------------------------+-------+------------+-----------+--------+
| Deployment                 | Ready | Up-To-Date | Available | Age    |
+----------------------------+-------+------------+-----------+--------+
| openshift-network-operator | 1/1   | 1          | 1         | 16h18m | 
| network-operator           |       |            |           |        | 
+----------------------------+-------+------------+-----------+--------+

+--------------------------------------------------------+---------+---------+-------+--------+
| Replica Set                                            | Desired | Current | Ready | Age    |
+--------------------------------------------------------+---------+---------+-------+--------+
| openshift-network-operator/network-operator-69cffcb848 | 1       | 1       | 1     | 16h18m | 
+--------------------------------------------------------+---------+---------+-------+--------+

+-----------------------------------+-------+---------+--------------------+--------+-------+-------------+-----+-----+----------------+
| Pod                               | Ready | Status  | Condition          | Age    | Node  | IP          | Net | Svc | Restarts       |
+-----------------------------------+-------+---------+--------------------+--------+-------+-------------+-----+-----+----------------+
| openshift-network-operator        | 1/1   | Running | Initialized: ✓     | 15h39m | bm1-1 | 10.10.10.10 | 0   | --  | 2 (15h13m ago) | 
| network-operator-69cffcb848-mnckf |       |         | PodScheduled: ✓    |        |       |             |     |     |                | 
|                                   |       |         | ContainersReady: ✓ |        |       |             |     |     |                | 
|                                   |       |         | Ready: ✓           |        |       |             |     |     |                | 
+-----------------------------------+-------+---------+--------------------+--------+-------+-------------+-----+-----+----------------+

Configure deployment replicas
-----------------------------
- namespace: openshift-network-operator
- name: network-operator
- replicas: 0

~~~
apiVersion: apps/v1
kind: Deployment
metadata:
  name: network-operator
  namespace: openshift-network-operator
spec:
  replicas: 0

~~~
Patch successful

Wait for desired replica pods...

Delete Config Map
-----------------
- namespace: openshift-network-operator
- name: applied-cluster
- wait for no config map

Set Machine Config Pool Pause
-----------------------------
- name: master
- pause: True

~~~
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: master
spec:
  paused: true

~~~
Patch successful

Set Machine Config Pool Pause
-----------------------------
- name: worker
- pause: True

~~~
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: worker
spec:
  paused: true

~~~
Patch successful

Step 3: Change default CNI
==========================


Set Cluster Network Type
------------------------
- type: Cilium
- cidr: 10.253.0.0/16
- host prefix: 24

~~~
apiVersion: config.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  clusterNetwork:
  - cidr: 10.253.0.0/16
    hostPrefix: 24
  networkType: Cilium
status: null

~~~
Patch successful

Set Cluster Network Operator Type
---------------------------------
- type: Cilium
- cidr: 10.253.0.0/16
- host prefix: 24
- kube proxy replaceement: False

~~~
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  clusterNetwork:
  - cidr: 10.253.0.0/16
    hostPrefix: 24
  defaultNetowkr:
    type: Cilium
  deployKubeProxy: false
status: null

~~~
Patch successful

Step 4: Deploy Cilium
=====================


Cilium Manifests Fixup
----------------------

~~~
apiVersion: cilium.io/v1alpha1
kind: CiliumConfig
metadata:
  labels:
    app.kubernetes.io/name: clife
  name: ciliumconfig
spec:
  cluster:
    name: default
  clusterHealthPort: 9940
  cni:
    binPath: /var/lib/cni/bin
    chainingMode: portmap
    confPath: /var/run/multus/cni/net.d
    exclusive: false
  devices: br-ex,bond0.666
  enterprise:
    featureGate:
      approved:
      - CNIChainingMode
  hubble:
    enabled: true
  ipam:
    mode: cluster-pool
    operator:
      clusterPoolIPv4MaskSize: 24
      clusterPoolIPv4PodCIDRList:
      - 10.253.0.0/16
  k8sServiceHost: "api-int.bm1.domain.com"
  k8sServicePort: 6443
  kubeProxyReplacement: "true"
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

~~~
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app.kubernetes.io/managed-by: kustomize
    app.kubernetes.io/name: clife
    control-plane: controller-manager
  name: clife-controller-manager
  namespace: cilium
spec:
  replicas: 1
  selector:
    matchLabels:
      control-plane: controller-manager
  strategy:
    type: Recreate
  template:
    metadata:
      annotations:
        kubectl.kubernetes.io/default-container: manager
      labels:
        control-plane: controller-manager
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: kubernetes.io/arch
                operator: In
                values:
                - amd64
                - arm64
              - key: kubernetes.io/os
                operator: In
                values:
                - linux
      containers:
      - args:
        - --health-probe-bind-address=:49081
        - --metrics-bind-address=:18443
        - --leader-elect
        command:
        - /clife-manager
        env:
        - name: NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
        - name: KUBERNETES_SERVICE_HOST
          value: "api-int.bm1.domain.com"
        - name: KUBERNETES_SERVICE_PORT
          value: "6443"
        image: image-version@sha256:...
        livenessProbe:
          httpGet:
            path: /healthz
            port: 49081
          initialDelaySeconds: 15
          periodSeconds: 20
        name: manager
        ports:
        - containerPort: 49081
          name: probe
          protocol: TCP
        - containerPort: 18443
          name: metrics
          protocol: TCP
        readinessProbe:
          httpGet:
            path: /readyz
            port: 49081
          initialDelaySeconds: 5
          periodSeconds: 10
        resources:
          limits:
            cpu: 1000m
            memory: 768Mi
          requests:
            cpu: 100m
            memory: 768Mi
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
      hostNetwork: true
      securityContext:
        runAsNonRoot: true
        seccompProfile:
          type: RuntimeDefault
      serviceAccountName: clife-controller-manager
      terminationGracePeriodSeconds: 10
      tolerations:
      - operator: Exists

~~~

Apply manifests
---------------
- CustomResourceDefinition:ciliumconfigs.cilium.io
- Namespace:cilium
- ServiceAccount:clife-controller-manager
- OperatorGroup:clife
- Role:clife-leader-election-role
- RoleBinding:clife-leader-election-rolebinding
- ClusterRole:clife-ciliumconfig-admin-role
- ClusterRole:clife-ciliumconfig-editor-role
- ClusterRole:clife-ciliumconfig-viewer-role
- ClusterRole:clife-manager-role
- ClusterRole:clife-metrics-auth-role
- ClusterRole:clife-metrics-reader
- ClusterRoleBinding:clife-manager-rolebinding
- ClusterRoleBinding:clife-metrics-auth-rolebinding
- Service:clife-metrics
- Subscription:clife
- CiliumConfig:ciliumconfig
- Deployment:clife-controller-manager

Multus Update
-------------

~~~
{
    "cniVersion": "0.3.1",
    "chrootDir": "/hostroot",
    "logToStderr": true,
    "logLevel": "verbose",
    "binDir": "/var/lib/cni/bin",
    "perNodeCertificate": {
        "enabled": true,
        "bootstrapKubeconfig": "/var/lib/kubelet/kubeconfig",
        "certDir": "/etc/cni/multus/certs",
        "certDuration": "24h"
    },
    "cniConfigDir": "/host/etc/cni/net.d",
    "multusConfigFile": "auto",
    "multusAutoconfigDir": "/host/run/multus/cni/net.d",
    "namespaceIsolation": true,
    "globalNamespaces": "default,openshift-multus,openshift-sriov-network-operator,openshift-cnv",
    "readinessindicatorfile": "/host/run/multus/cni/net.d/05-cilium.conflist",
    "daemonSocketDir": "/run/multus/socket",
    "socketDir": "/host/run/multus/socket"
}
~~~
Config map udpated

Wait for Cilium resources
-------------------------

Take a nap...

- pod: cilium-envoy-cc6m7
- pod: cilium-envoy-f46p9
- pod: cilium-envoy-hxknk
- pod: cilium-l9l76
- pod: cilium-nmgrv
- pod: cilium-operator-57564d47cb-bfrq8
- pod: cilium-operator-57564d47cb-nzncl
- pod: cilium-pbvpf
- pod: clife-controller-manager-7b9f4c698d-n2mwl
- deployment: cilium-operator
- deployment: clife-controller-manager

+--------------------------+-------+------------+-----------+------+
| Deployment               | Ready | Up-To-Date | Available | Age  |
+--------------------------+-------+------------+-----------+------+
| cilium                   | 2/2   | 2          | 2         | 4h5m | 
| cilium-operator          |       |            |           |      | 
+--------------------------+-------+------------+-----------+------+
| cilium                   | 1/1   | 1          | 1         | 5h4m | 
| clife-controller-manager |       |            |           |      | 
+--------------------------+-------+------------+-----------+------+

+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| Pod                                       | Ready | Status  | Condition          | Age  | Node  | IP          | Net | Svc | Restarts |
+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 4h5m | bm1-3 | 10.10.10.12 | 0   | --  | 0        | 
| cilium-envoy-cc6m7                        |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 4h5m | bm1-2 | 10.10.10.11 | 0   | --  | 0        | 
| cilium-envoy-f46p9                        |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 4h5m | bm1-1 | 10.10.10.10 | 0   | --  | 0        | 
| cilium-envoy-hxknk                        |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 4h5m | bm1-1 | 10.10.10.10 | 0   | --  | 0        | 
| cilium-l9l76                              |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 4h5m | bm1-3 | 10.10.10.12 | 0   | --  | 0        | 
| cilium-nmgrv                              |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 4h5m | bm1-1 | 10.10.10.10 | 0   | --  | 0        | 
| cilium-operator-57564d47cb-bfrq8          |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 4h5m | bm1-3 | 10.10.10.12 | 0   | --  | 0        | 
| cilium-operator-57564d47cb-nzncl          |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 4h5m | bm1-2 | 10.10.10.11 | 0   | --  | 0        | 
| cilium-pbvpf                              |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 5h4m | bm1-3 | 10.10.10.12 | 0   | --  | 0        | 
| clife-controller-manager-7b9f4c698d-n2mwl |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|                                           |       |         | Ready: ✓           |      |       |             |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+

Step 5: Re-enable OpenShift operator management
===============================================


Delete kube API server pods
---------------------------

+--------------------------+-------+---------+--------------------+--------+-------+-------------+-----+-----+----------+
| Pod                      | Ready | Status  | Condition          | Age    | Node  | IP          | Net | Svc | Restarts |
+--------------------------+-------+---------+--------------------+--------+-------+-------------+-----+-----+----------+
| openshift-kube-apiserver | 5/5   | Running | Initialized: ✓     | 18h1m  | bm1-1 | 10.10.10.10 | 0   | --  | 0        | 
| kube-apiserver-bm1-1     |       |         | PodScheduled: ✓    |        |       |             |     |     |          | 
|                          |       |         | ContainersReady: ✓ |        |       |             |     |     |          | 
|                          |       |         | Ready: ✓           |        |       |             |     |     |          | 
+--------------------------+-------+---------+--------------------+--------+-------+-------------+-----+-----+----------+
| openshift-kube-apiserver | 5/5   | Running | Initialized: ✓     | 17h58m | bm1-2 | 10.10.10.11 | 0   | --  | 0        | 
| kube-apiserver-bm1-2     |       |         | PodScheduled: ✓    |        |       |             |     |     |          | 
|                          |       |         | ContainersReady: ✓ |        |       |             |     |     |          | 
|                          |       |         | Ready: ✓           |        |       |             |     |     |          | 
+--------------------------+-------+---------+--------------------+--------+-------+-------------+-----+-----+----------+
| openshift-kube-apiserver | 5/5   | Running | Initialized: ✓     | 17h55m | bm1-3 | 10.10.10.12 | 0   | --  | 0        | 
| kube-apiserver-bm1-3     |       |         | PodScheduled: ✓    |        |       |             |     |     |          | 
|                          |       |         | ContainersReady: ✓ |        |       |             |     |     |          | 
|                          |       |         | Ready: ✓           |        |       |             |     |     |          | 
+--------------------------+-------+---------+--------------------+--------+-------+-------------+-----+-----+----------+

Delete
- kube-apiserver-bm1-1
- kube-apiserver-bm1-2
- kube-apiserver-bm1-3

Delete machine config deployments
---------------------------------

+-----------------------------------+-------+------------+-----------+--------+
| Deployment                        | Ready | Up-To-Date | Available | Age    |
+-----------------------------------+-------+------------+-----------+--------+
| openshift-machine-config-operator | 1/1   | 1          | 1         | 18h30m | 
| machine-config-controller         |       |            |           |        | 
+-----------------------------------+-------+------------+-----------+--------+
| openshift-machine-config-operator | 1/1   | 1          | 1         | 19h23m | 
| machine-config-operator           |       |            |           |        | 
+-----------------------------------+-------+------------+-----------+--------+

+--------------------------------------------+-------+---------+--------------------+--------+-------+-------------+-----+-----+----------------+
| Pod                                        | Ready | Status  | Condition          | Age    | Node  | IP          | Net | Svc | Restarts       |
+--------------------------------------------+-------+---------+--------------------+--------+-------+-------------+-----+-----+----------------+
| openshift-machine-config-operator          | 2/2   | Running | Initialized: ✓     | 18h30m | bm1-2 | 10.128.0.19 | 0   | --  | 1 (18h18m ago) | 
| machine-config-controller-58f77b6849-mdfvx |       |         | PodScheduled: ✓    |        |       |             |     |     |                | 
|                                            |       |         | ContainersReady: ✓ |        |       |             |     |     |                | 
|                                            |       |         | Ready: ✓           |        |       |             |     |     |                | 
+--------------------------------------------+-------+---------+--------------------+--------+-------+-------------+-----+-----+----------------+
| openshift-machine-config-operator          | 2/2   | Running | Initialized: ✓     | 18h44m | bm1-1 | 10.129.0.29 | 0   | --  | 1 (18h18m ago) | 
| machine-config-operator-85bb75494f-chk22   |       |         | PodScheduled: ✓    |        |       |             |     |     |                | 
|                                            |       |         | ContainersReady: ✓ |        |       |             |     |     |                | 
|                                            |       |         | Ready: ✓           |        |       |             |     |     |                | 
+--------------------------------------------+-------+---------+--------------------+--------+-------+-------------+-----+-----+----------------+

Rollout restart

Take a nap...


Wait for deployment ready

+-----------------------------------+-------+------------+-----------+--------+
| Deployment                        | Ready | Up-To-Date | Available | Age    |
+-----------------------------------+-------+------------+-----------+--------+
| openshift-machine-config-operator | 1/1   | 1          | 1         | 18h30m | 
| machine-config-controller         |       |            |           |        | 
+-----------------------------------+-------+------------+-----------+--------+
| openshift-machine-config-operator | 1/1   | 1          | 1         | 19h23m | 
| machine-config-operator           |       |            |           |        | 
+-----------------------------------+-------+------------+-----------+--------+

+--------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| Pod                                        | Ready | Status  | Condition          | Age  | Node  | IP          | Net | Svc | Restarts |
+--------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| openshift-machine-config-operator          | 2/2   | Running | Initialized: ✓     | 2h0m | bm1-3 | 10.130.0.29 | 0   | --  | 0        | 
| machine-config-controller-6878c88497-qlr89 |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|                                            |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|                                            |       |         | Ready: ✓           |      |       |             |     |     |          | 
+--------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| openshift-machine-config-operator          | 2/2   | Running | Initialized: ✓     | 2h0m | bm1-3 | 10.130.0.30 | 0   | --  | 0        | 
| machine-config-operator-5cd86b8699-l7wsq   |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|                                            |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|                                            |       |         | Ready: ✓           |      |       |             |     |     |          | 
+--------------------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+

Network Operator
----------------

+----------------------------+-------+------------+-----------+--------+
| Deployment                 | Ready | Up-To-Date | Available | Age    |
+----------------------------+-------+------------+-----------+--------+
| openshift-network-operator | 0/0   | None       | None      | 19h24m | 
| network-operator           |       |            |           |        | 
+----------------------------+-------+------------+-----------+--------+

Configure deployment replicas
-----------------------------
- namespace: openshift-network-operator
- name: network-operator
- replicas: 1

~~~
apiVersion: apps/v1
kind: Deployment
metadata:
  name: network-operator
  namespace: openshift-network-operator
spec:
  replicas: 1

~~~
Patch successful

Wait for desired replica pods...

+--------------------------------------------------------+---------+---------+-------+--------+
| Replica Set                                            | Desired | Current | Ready | Age    |
+--------------------------------------------------------+---------+---------+-------+--------+
| openshift-network-operator/network-operator-69cffcb848 | 1       | 1       | 1     | 19h24m | 
+--------------------------------------------------------+---------+---------+-------+--------+

+-----------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| Pod                               | Ready | Status  | Condition          | Age  | Node  | IP          | Net | Svc | Restarts |
+-----------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+
| openshift-network-operator        | 1/1   | Running | Initialized: ✓     | 2h0m | bm1-3 | 10.10.10.12 | 0   | --  | 0        | 
| network-operator-69cffcb848-jp292 |       |         | PodScheduled: ✓    |      |       |             |     |     |          | 
|                                   |       |         | ContainersReady: ✓ |      |       |             |     |     |          | 
|                                   |       |         | Ready: ✓           |      |       |             |     |     |          | 
+-----------------------------------+-------+---------+--------------------+------+-------+-------------+-----+-----+----------+

Enable network operator management
----------------------------------

~~~
api: config.openshift.io/v1
kind: ClusterVersion
metadata:
  name: version
spec:
  overrides: null

~~~
Patch successful

Step 6: Restart cluster
=======================


+----+-------+-------+-------+--------+------+-----+-----+-----+--------+-------------------+--------+
| ID | Node  | Ready | Taint | Memory | Disk | PID | CNV | MCP | Role   | IP                | Age    |
+----+-------+-------+-------+--------+------+-----+-----+-----+--------+-------------------+--------+
| 1  | bm1-1 | ✓     | ---   | ✓      | ✓    | ✓   | ✗   | ✓   | Master | 10.10.10.10 (int) | 18h50m | 
|    |       |       |       |        |      |     |     |     | Worker |                   |        | 
+----+-------+-------+-------+--------+------+-----+-----+-----+--------+-------------------+--------+
| 2  | bm1-2 | ✓     | ---   | ✓      | ✓    | ✓   | ✗   | ✓   | Master | 10.10.10.11 (int) | 18h50m | 
|    |       |       |       |        |      |     |     |     | Worker |                   |        | 
+----+-------+-------+-------+--------+------+-----+-----+-----+--------+-------------------+--------+
| 3  | bm1-3 | ✓     | ---   | ✓      | ✓    | ✓   | ✗   | ✓   | Master | 10.10.10.12 (int) | 18h10m | 
|    |       |       |       |        |      |     |     |     | Worker |                   |        | 
+----+-------+-------+-------+--------+------+-----+-----+-----+--------+-------------------+--------+

Set Machine Config Pool Pause
-----------------------------
- name: worker
- pause: False

~~~
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: worker
spec:
  paused: false

~~~
Patch successful

Set Machine Config Pool Pause
-----------------------------
- name: master
- pause: False

~~~
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: master
spec:
  paused: false

~~~
Patch successful

Wait for mcp-initiated cluster nodes restart
--------------------------------------------
Max time: 3600 seconds
Node [bm1-1] Status ['Ready', 'PreferNoSchedule', 'UpdateInProgress']
Node [bm1-2] Status ['Ready', 'PreferNoSchedule', 'UpdateInProgress']
Node [bm1-3] Status ['Ready', 'PreferNoSchedule', 'UpdateInProgress']
Node [bm1-1] Status ['Ready']
Node [bm1-1] Status ['Ready', 'NoSchedule', 'unschedulable']
Node [bm1-1] Status ['Not Ready', 'NoSchedule', 'unschedulable', 'unreachable']
Node [bm1-1] down on restart
Node [bm1-1] Status ['Not Ready', 'NoSchedule', 'unschedulable', 'unreachable', 'agent-not-ready']
Node [bm1-1] Status ['Not Ready', 'NoSchedule', 'NoExecute', 'unschedulable', 'unreachable', 'agent-not-ready']
Node [bm1-1] Status ['Not Ready', 'NoSchedule', 'NoExecute', 'unschedulable', 'agent-not-ready', 'not-ready']
Node [bm1-1] Status ['Ready']
Node [bm1-1] back operational
Node [bm1-2] Status ['Ready']
Node [bm1-2] Status ['Ready', 'NoSchedule', 'unschedulable']
Node [bm1-2] Status ['Not Ready', 'NoSchedule', 'unschedulable', 'unreachable']
Node [bm1-2] down on restart
Node [bm1-2] Status ['Not Ready', 'NoSchedule', 'unschedulable', 'unreachable', 'agent-not-ready']
Node [bm1-2] Status ['Not Ready', 'NoSchedule', 'NoExecute', 'unschedulable', 'unreachable', 'agent-not-ready']
Node [bm1-2] Status ['Not Ready', 'NoSchedule', 'NoExecute', 'unschedulable', 'agent-not-ready', 'not-ready']
Node [bm1-2] Status ['Not Ready', 'NoSchedule', 'NoExecute', 'agent-not-ready', 'not-ready']
Node [bm1-2] Status ['Ready', 'NoExecute', 'not-ready']
Node [bm1-2] Status ['Ready']
Node [bm1-2] back operational
Node [bm1-3] Status ['Ready']
Node [bm1-3] Status ['Ready', 'NoSchedule', 'unschedulable']
Node [bm1-3] Status ['Not Ready', 'NoSchedule', 'unschedulable', 'unreachable', 'agent-not-ready']
Node [bm1-3] down on restart
Node [bm1-3] Status ['Not Ready', 'NoSchedule', 'NoExecute', 'unschedulable', 'unreachable', 'agent-not-ready']
Node [bm1-3] Status ['Not Ready', 'NoSchedule', 'NoExecute', 'unschedulable', 'agent-not-ready', 'not-ready']
Node [bm1-1] Status ['Ready', 'PreferNoSchedule', 'UpdateInProgress']
Node [bm1-2] Status ['Ready', 'PreferNoSchedule', 'UpdateInProgress']
Node [bm1-3] Status ['Not Ready', 'NoSchedule', 'NoExecute', 'PreferNoSchedule', 'unschedulable', 'agent-not-ready', 'not-ready', 'UpdateInProgress']
Node [bm1-3] Status ['Not Ready', 'NoSchedule', 'NoExecute', 'PreferNoSchedule', 'agent-not-ready', 'not-ready', 'UpdateInProgress']
Node [bm1-3] Status ['Ready', 'PreferNoSchedule', 'UpdateInProgress']
Node [bm1-1] Status ['Ready']
Node [bm1-1] Status ['Ready', 'NoSchedule', 'unschedulable']
Node [bm1-1] Status ['Not Ready', 'NoSchedule', 'unschedulable', 'unreachable', 'agent-not-ready']
Node [bm1-1] Status ['Not Ready', 'NoSchedule', 'NoExecute', 'unschedulable', 'unreachable', 'agent-not-ready']
Node [bm1-1] Status ['Not Ready', 'NoSchedule', 'NoExecute', 'unschedulable', 'agent-not-ready', 'unreachable', 'not-ready']
Node [bm1-1] Status ['Not Ready', 'NoSchedule', 'NoExecute', 'unschedulable', 'agent-not-ready', 'not-ready']
Node [bm1-1] Status ['Not Ready', 'NoSchedule', 'NoExecute', 'agent-not-ready', 'not-ready']
Node [bm1-1] Status ['Ready']
Node [bm1-3] Status ['Ready']
Node [bm1-3] back operational
All nodes restarted
Wait for kubernetes api [30min]...

Step 7: Wait cluster ready
==========================

Wait nodes ready [30min]...

+----+-------+-------+------------------+--------+------+-----+-----+-----+--------+-------------------+--------+
| ID | Node  | Ready | Taint            | Memory | Disk | PID | CNV | MCP | Role   | IP                | Age    |
+----+-------+-------+------------------+--------+------+-----+-----+-----+--------+-------------------+--------+
| 1  | bm1-1 | ✓     | ---              | ✓      | ✓    | ✓   | ✗   | ✓   | Master | 10.10.10.10 (int) | 19h35m | 
|    |       |       |                  |        |      |     |     |     | Worker |                   |        | 
+----+-------+-------+------------------+--------+------+-----+-----+-----+--------+-------------------+--------+
| 2  | bm1-2 | ✓     | PreferNoSchedule | ✓      | ✓    | ✓   | ✗   | ✓   | Master | 10.10.10.11 (int) | 19h35m | 
|    |       |       |                  |        |      |     |     |     | Worker |                   |        | 
+----+-------+-------+------------------+--------+------+-----+-----+-----+--------+-------------------+--------+
| 3  | bm1-3 | ✓     | NoSchedule       | ✓      | ✓    | ✓   | ✗   | ✗   | Master | 10.10.10.12 (int) | 18h55m | 
|    |       |       |                  |        |      |     |     |     | Worker |                   |        | 
+----+-------+-------+------------------+--------+------+-----+-----+-----+--------+-------------------+--------+

Wait machine config pool ready [1hr]...

+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+----------------------------------+--------+
| Machine Config Pool | Config                                           | Updated | Updating | Degraded | Machines | Ready | Updated | Degraded | Unavail | Machine Config                   | Age    |
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+----------------------------------+--------+
| master              | rendered-master-58862610b23ab6a9ea0f6d0c817e9282 | ✓       | ✗        | ✗        | 3        | 3     | 3       | 0        | 0       | 00-master                        | 19h37m | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-master-container-runtime      |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-master-kubelet                |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 50-masters-chrony-configuration  |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 97-master-generated-kubelet      |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 98-master-generated-kubelet      |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-assisted-installer-master-ssh |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-master-generated-registries   |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-master-ssh                    |        | 
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+----------------------------------+--------+
| worker              | rendered-worker-72045aa2570c7c2465f60d21dc326504 | ✓       | ✗        | ✗        | 0        | 0     | 0       | 0        | 0       | 00-worker                        | 19h37m | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-worker-container-runtime      |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-worker-kubelet                |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 50-workers-chrony-configuration  |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 97-worker-generated-kubelet      |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 98-worker-generated-kubelet      |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-worker-generated-registries   |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-worker-ssh                    |        | 
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+----------------------------------+--------+

Wait Cluster Operators
- wait for authentication available
- wait for baremetal available
- wait for cloud-controller-manager available
- wait for cloud-credential available
- wait for cluster-autoscaler available
- wait for config-operator available
- wait for console available
- wait for control-plane-machine-set available
- wait for csi-snapshot-controller available
- wait for dns available
- wait for etcd available
- wait for image-registry available
- wait for ingress available
- wait for insights available
- wait for kube-apiserver available
- wait for kube-controller-manager available
- wait for kube-scheduler available
- wait for kube-storage-version-migrator available
- wait for machine-api available
- wait for machine-approver available
- wait for machine-config available
- wait for marketplace available
- wait for monitoring available
- wait for network available
- wait for node-tuning available
- wait for olm available
- wait for openshift-apiserver available
- wait for openshift-controller-manager available
- wait for openshift-samples available
- wait for operator-lifecycle-manager available
- wait for operator-lifecycle-manager-catalog available
- wait for operator-lifecycle-manager-packageserver available
- wait for service-ca available
- wait for storage available

Check Cluster Operators
-----------------------

+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| Cluster Operator                         | Version | Owner          | Available | Progressing | Degraded | Upgradeable | Since  | Age    |
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| authentication                           | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h28m  | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| baremetal                                | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h37m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| cloud-controller-manager                 | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h49m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| cloud-credential                         | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 20h29m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| cluster-autoscaler                       | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h34m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| config-operator                          | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h38m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| console                                  | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h20m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| control-plane-machine-set                | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h35m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| csi-snapshot-controller                  | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h39m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| dns                                      | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h36m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| etcd                                     | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h33m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| image-registry                           | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h21m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| ingress                                  | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 3h5m   | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| insights                                 | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h38m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| kube-apiserver                           | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h32m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| kube-controller-manager                  | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h32m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| kube-scheduler                           | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h32m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| kube-storage-version-migrator            | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h20m  | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| machine-api                              | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h30m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| machine-approver                         | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h35m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| machine-config                           | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h37m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| marketplace                              | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h37m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| monitoring                               | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h38m  | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| network                                  | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h39m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| node-tuning                              | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h16m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| olm                                      | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h10m  | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| openshift-apiserver                      | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h29m  | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| openshift-controller-manager             | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h25m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| openshift-samples                        | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h25m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| operator-lifecycle-manager               | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h35m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| operator-lifecycle-manager-catalog       | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h36m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| operator-lifecycle-manager-packageserver | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h38m  | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| service-ca                               | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h38m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| storage                                  | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 19h38m | 20h31m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+

Wait for Cilium resources
-------------------------

Take a nap...

- pod: cilium-envoy-cc6m7
- pod: cilium-envoy-f46p9
- pod: cilium-envoy-hxknk
- pod: cilium-l9l76
- pod: cilium-nmgrv
- pod: cilium-operator-57564d47cb-k9jkg
- pod: cilium-operator-57564d47cb-n2k9j
- pod: cilium-pbvpf
- pod: clife-controller-manager-7b9f4c698d-j829x
- deployment: cilium-operator
- deployment: clife-controller-manager

+--------------------------+-------+------------+-----------+-------+
| Deployment               | Ready | Up-To-Date | Available | Age   |
+--------------------------+-------+------------+-----------+-------+
| cilium                   | 2/2   | 2          | 2         | 5h13m | 
| cilium-operator          |       |            |           |       | 
+--------------------------+-------+------------+-----------+-------+
| cilium                   | 1/1   | 1          | 1         | 6h12m | 
| clife-controller-manager |       |            |           |       | 
+--------------------------+-------+------------+-----------+-------+

+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| Pod                                       | Ready | Status  | Condition          | Age   | Node  | IP          | Net | Svc | Restarts      |
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 5h13m | bm1-3 | 10.10.10.12 | 0   | --  | 2 (2h12m ago) | 
| cilium-envoy-cc6m7                        |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 5h13m | bm1-2 | 10.10.10.11 | 0   | --  | 2 (2h2m ago)  | 
| cilium-envoy-f46p9                        |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 5h13m | bm1-1 | 10.10.10.10 | 0   | --  | 2 (2h22m ago) | 
| cilium-envoy-hxknk                        |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 5h13m | bm1-1 | 10.10.10.10 | 0   | --  | 2 (2h22m ago) | 
| cilium-l9l76                              |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 5h13m | bm1-3 | 10.10.10.12 | 0   | --  | 2 (2h12m ago) | 
| cilium-nmgrv                              |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h22m | bm1-1 | 10.10.10.10 | 0   | --  | 0             | 
| cilium-operator-57564d47cb-k9jkg          |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h12m | bm1-3 | 10.10.10.12 | 0   | --  | 0             | 
| cilium-operator-57564d47cb-n2k9j          |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 5h13m | bm1-2 | 10.10.10.11 | 0   | --  | 2 (2h1m ago)  | 
| cilium-pbvpf                              |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h12m | bm1-3 | 10.10.10.12 | 0   | --  | 0             | 
| clife-controller-manager-7b9f4c698d-j829x |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+

Step 8: Post migration
======================

Remove device from cilium config
- patched
Deployment [cilium/cilium-operator] patch successful
Daemon set [cilium/cilium] patch successful

Wait for Cilium resources
-------------------------

Take a nap...

- pod: cilium-2fsbl
- pod: cilium-envoy-cc6m7
- pod: cilium-envoy-f46p9
- pod: cilium-envoy-hxknk
- pod: cilium-hsn6l
- pod: cilium-lc7zj
- pod: cilium-operator-86687c864-9nxm9
- pod: cilium-operator-86687c864-t2287
- pod: clife-controller-manager-7b9f4c698d-j829x
- deployment: cilium-operator
- deployment: clife-controller-manager

+--------------------------+-------+------------+-----------+-------+
| Deployment               | Ready | Up-To-Date | Available | Age   |
+--------------------------+-------+------------+-----------+-------+
| cilium                   | 2/2   | 2          | 2         | 6h50m | 
| cilium-operator          |       |            |           |       | 
+--------------------------+-------+------------+-----------+-------+
| cilium                   | 1/1   | 1          | 1         | 7h49m | 
| clife-controller-manager |       |            |           |       | 
+--------------------------+-------+------------+-----------+-------+

+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| Pod                                       | Ready | Status  | Condition          | Age   | Node  | IP          | Net | Svc | Restarts      |
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 3h36m | bm1-3 | 10.10.10.12 | 0   | --  | 0             | 
| cilium-2fsbl                              |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 6h50m | bm1-3 | 10.10.10.12 | 0   | --  | 2 (3h49m ago) | 
| cilium-envoy-cc6m7                        |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 6h50m | bm1-2 | 10.10.10.11 | 0   | --  | 2 (3h38m ago) | 
| cilium-envoy-f46p9                        |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 6h50m | bm1-1 | 10.10.10.10 | 0   | --  | 2 (3h59m ago) | 
| cilium-envoy-hxknk                        |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 3h36m | bm1-1 | 10.10.10.10 | 0   | --  | 0             | 
| cilium-hsn6l                              |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 3h36m | bm1-2 | 10.10.10.11 | 0   | --  | 0             | 
| cilium-lc7zj                              |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 3h36m | bm1-3 | 10.10.10.12 | 0   | --  | 0             | 
| cilium-operator-86687c864-9nxm9           |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 3h36m | bm1-2 | 10.10.10.11 | 0   | --  | 0             | 
| cilium-operator-86687c864-t2287           |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 3h48m | bm1-3 | 10.10.10.12 | 0   | --  | 0             | 
| clife-controller-manager-7b9f4c698d-j829x |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+

Approve cilium install plan
- installplan cilium/install-kcvcm will be approved
- patched (approved)

Remove ovn-kubernetes namespace

Namespace [openshift-ovn-kubernetes] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
Namespace deleted

Prepare kubeconfig
.kube directory already exists
kubeconfig uploaded

OpenShift Workflow - Install cilium cli
=======================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": true,
    "check_verbose": false,
    "url": "https://github.com/cilium/cilium-cli/releases/download/v0.18.6/cilium-linux-amd64.tar.gz",
    "check-verbose": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- management node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- cli cilium: not found

Downloading cilium binary from https://github.com/cilium/cilium-cli/releases/download/v0.18.6/cilium-linux-amd64.tar.gz
Uploading cilium binary to cluster management node
Unpack
Change file flags
Cilium binary ready to be used
cilium-cli: v0.18.6 compiled with go1.24.5 on linux/amd64
cilium image (default): v1.18.0
cilium image (stable): unknown
cilium image (running): unknown. Unable to obtain cilium version. Reason: release: not found


~~~
    /¯¯\
 /¯¯\__/¯¯\    Cilium:             OK
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Envoy DaemonSet:    OK
 \__/¯¯\__/    Hubble Relay:       disabled
    \__/       ClusterMesh:        disabled

DaemonSet              cilium                   Desired: 3, Ready: 3/3, Available: 3/3
DaemonSet              cilium-envoy             Desired: 3, Ready: 3/3, Available: 3/3
Deployment             cilium-operator          Desired: 2, Ready: 2/2, Available: 2/2
Containers:            cilium                   Running: 3
                       cilium-envoy             Running: 3
                       cilium-operator          Running: 2
                       clustermesh-apiserver    
                       hubble-relay             
Cluster Pods:          111/111 managed by Cilium
~~~

Step 9: Cluster Restart
=======================

Reload nodes
- bm1-1
- bm1-2
- bm1-3

Wait for no kubernetes api [10min]...

Wait for kubernetes api [30min]...

Wait nodes ready [30min]...

+----+-------+-------+-------+--------+------+-----+-----+-----+--------+-------------------+--------+
| ID | Node  | Ready | Taint | Memory | Disk | PID | CNV | MCP | Role   | IP                | Age    |
+----+-------+-------+-------+--------+------+-----+-----+-----+--------+-------------------+--------+
| 1  | bm1-1 | ✓     | ---   | ✓      | ✓    | ✓   | ✗   | ✓   | Master | 10.10.10.10 (int) | 22h0m  | 
|    |       |       |       |        |      |     |     |     | Worker |                   |        | 
+----+-------+-------+-------+--------+------+-----+-----+-----+--------+-------------------+--------+
| 2  | bm1-2 | ✓     | ---   | ✓      | ✓    | ✓   | ✗   | ✓   | Master | 10.10.10.11 (int) | 22h0m  | 
|    |       |       |       |        |      |     |     |     | Worker |                   |        | 
+----+-------+-------+-------+--------+------+-----+-----+-----+--------+-------------------+--------+
| 3  | bm1-3 | ✓     | ---   | ✓      | ✓    | ✓   | ✗   | ✓   | Master | 10.10.10.12 (int) | 21h19m | 
|    |       |       |       |        |      |     |     |     | Worker |                   |        | 
+----+-------+-------+-------+--------+------+-----+-----+-----+--------+-------------------+--------+

Wait machine config pool ready [1hr]...

+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+----------------------------------+--------+
| Machine Config Pool | Config                                           | Updated | Updating | Degraded | Machines | Ready | Updated | Degraded | Unavail | Machine Config                   | Age    |
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+----------------------------------+--------+
| master              | rendered-master-58862610b23ab6a9ea0f6d0c817e9282 | ✓       | ✗        | ✗        | 3        | 3     | 3       | 0        | 0       | 00-master                        | 21h40m | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-master-container-runtime      |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-master-kubelet                |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 50-masters-chrony-configuration  |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 97-master-generated-kubelet      |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 98-master-generated-kubelet      |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-assisted-installer-master-ssh |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-master-generated-registries   |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-master-ssh                    |        | 
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+----------------------------------+--------+
| worker              | rendered-worker-72045aa2570c7c2465f60d21dc326504 | ✓       | ✗        | ✗        | 0        | 0     | 0       | 0        | 0       | 00-worker                        | 21h40m | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-worker-container-runtime      |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-worker-kubelet                |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 50-workers-chrony-configuration  |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 97-worker-generated-kubelet      |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 98-worker-generated-kubelet      |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-worker-generated-registries   |        | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-worker-ssh                    |        | 
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+----------------------------------+--------+

Wait Cluster Operators
- wait for authentication available
- wait for baremetal available
- wait for cloud-controller-manager available
- wait for cloud-credential available
- wait for cluster-autoscaler available
- wait for config-operator available
- wait for console available
- wait for control-plane-machine-set available
- wait for csi-snapshot-controller available
- wait for dns available
- wait for etcd available
- wait for image-registry available
- wait for ingress available
- wait for insights available
- wait for kube-apiserver available
- wait for kube-controller-manager available
- wait for kube-scheduler available
- wait for kube-storage-version-migrator available
- wait for machine-api available
- wait for machine-approver available
- wait for machine-config available
- wait for marketplace available
- wait for monitoring available
- wait for network available
- wait for node-tuning available
- wait for olm available
- wait for openshift-apiserver available
- wait for openshift-controller-manager available
- wait for openshift-samples available
- wait for operator-lifecycle-manager available
- wait for operator-lifecycle-manager-catalog available
- wait for operator-lifecycle-manager-packageserver available
- wait for service-ca available
- wait for storage available

Check Cluster Operators
-----------------------

+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| Cluster Operator                         | Version | Owner          | Available | Progressing | Degraded | Upgradeable | Since  | Age    |
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| authentication                           | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h13m  | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| baremetal                                | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h40m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| cloud-controller-manager                 | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h53m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| cloud-credential                         | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 22h33m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| cluster-autoscaler                       | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h37m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| config-operator                          | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h42m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| console                                  | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h23m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| control-plane-machine-set                | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h38m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| csi-snapshot-controller                  | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h42m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| dns                                      | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h39m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| etcd                                     | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h37m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| image-registry                           | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h24m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| ingress                                  | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h12m  | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| insights                                 | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h41m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| kube-apiserver                           | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h36m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| kube-controller-manager                  | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h36m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| kube-scheduler                           | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h35m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| kube-storage-version-migrator            | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h13m  | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| machine-api                              | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h33m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| machine-approver                         | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h38m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| machine-config                           | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h40m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| marketplace                              | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h40m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| monitoring                               | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 4h41m  | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| network                                  | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h42m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| node-tuning                              | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h20m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| olm                                      | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h13m  | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| openshift-apiserver                      | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h12m  | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| openshift-controller-manager             | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h29m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| openshift-samples                        | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h28m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| operator-lifecycle-manager               | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h38m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| operator-lifecycle-manager-catalog       | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h39m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| operator-lifecycle-manager-packageserver | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 4h42m  | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| service-ca                               | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h42m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+
| storage                                  | 4.18.9  | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 21h42m | 22h34m | 
|                                          |         | version        |           |             |          |             |        |        | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+--------+--------+

Wait for Cilium resources
-------------------------

Take a nap...

- pod: cilium-2fsbl
- pod: cilium-envoy-cc6m7
- pod: cilium-envoy-f46p9
- pod: cilium-envoy-hxknk
- pod: cilium-hsn6l
- pod: cilium-lc7zj
- pod: cilium-operator-86687c864-9nxm9
- pod: cilium-operator-86687c864-t2287
- pod: clife-controller-manager-6c68c776fc-vvnsj
- deployment: cilium-operator
- deployment: clife-controller-manager

+--------------------------+-------+------------+-----------+-------+
| Deployment               | Ready | Up-To-Date | Available | Age   |
+--------------------------+-------+------------+-----------+-------+
| cilium                   | 2/2   | 2          | 2         | 7h17m | 
| cilium-operator          |       |            |           |       | 
+--------------------------+-------+------------+-----------+-------+
| cilium                   | 1/1   | 1          | 1         | 8h16m | 
| clife-controller-manager |       |            |           |       | 
+--------------------------+-------+------------+-----------+-------+

+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| Pod                                       | Ready | Status  | Condition          | Age   | Node  | IP          | Net | Svc | Restarts      |
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 4h3m  | bm1-3 | 10.10.10.12 | 0   | --  | 1 (2h16m ago) | 
| cilium-2fsbl                              |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 7h17m | bm1-3 | 10.10.10.12 | 0   | --  | 3 (2h17m ago) | 
| cilium-envoy-cc6m7                        |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 7h17m | bm1-2 | 10.10.10.11 | 0   | --  | 3 (2h15m ago) | 
| cilium-envoy-f46p9                        |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 7h17m | bm1-1 | 10.10.10.10 | 0   | --  | 3 (2h16m ago) | 
| cilium-envoy-hxknk                        |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 4h3m  | bm1-1 | 10.10.10.10 | 0   | --  | 1 (2h16m ago) | 
| cilium-hsn6l                              |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 4h3m  | bm1-2 | 10.10.10.11 | 0   | --  | 1 (2h15m ago) | 
| cilium-lc7zj                              |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 4h3m  | bm1-3 | 10.10.10.12 | 0   | --  | 1 (2h17m ago) | 
| cilium-operator-86687c864-9nxm9           |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 4h3m  | bm1-2 | 10.10.10.11 | 0   | --  | 1 (2h15m ago) | 
| cilium-operator-86687c864-t2287           |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h27m | bm1-2 | 10.10.10.11 | 0   | --  | 3 (2h14m ago) | 
| clife-controller-manager-6c68c776fc-vvnsj |       |         | PodScheduled: ✓    |       |       |             |     |     |               | 
|                                           |       |         | ContainersReady: ✓ |       |       |             |     |     |               | 
|                                           |       |         | Ready: ✓           |       |       |             |     |     |               | 
+-------------------------------------------+-------+---------+--------------------+-------+-------+-------------+-----+-----+---------------+

~~~
    /¯¯\
 /¯¯\__/¯¯\    Cilium:             OK
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Envoy DaemonSet:    OK
 \__/¯¯\__/    Hubble Relay:       disabled
    \__/       ClusterMesh:        disabled

DaemonSet              cilium                   Desired: 3, Ready: 3/3, Available: 3/3
DaemonSet              cilium-envoy             Desired: 3, Ready: 3/3, Available: 3/3
Deployment             cilium-operator          Desired: 2, Ready: 2/2, Available: 2/2
Containers:            cilium                   Running: 3
                       cilium-envoy             Running: 3
                       cilium-operator          Running: 2
                       clustermesh-apiserver    
                       hubble-relay             
Cluster Pods:          111/111 managed by Cilium
~~~
```

[[Back]](./README.md)