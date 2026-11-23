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
- cluster node [166.11.170.180] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok


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
Upstream interface of OVS switch: eno5

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

+----------------------------+-------+------------+-----------+-----+
| Deployment                 | Ready | Up-To-Date | Available | Age |
+----------------------------+-------+------------+-----------+-----+
| openshift-network-operator | 1/1   | 1          | 1         | 10d | 
| network-operator           |       |            |           |     | 
+----------------------------+-------+------------+-----------+-----+

+--------------------------------------------------------+---------+---------+-------+-----+
| Replica Set                                            | Desired | Current | Ready | Age |
+--------------------------------------------------------+---------+---------+-------+-----+
| openshift-network-operator/network-operator-798d48796b | 1       | 1       | 1     | 10d | 
+--------------------------------------------------------+---------+---------+-------+-----+

+-----------------------------------+-------+---------+--------------------+-----+-----------------------------+----------------+-----+-----+---------------+
| Pod                               | Ready | Status  | Condition          | Age | Node                        | IP             | Net | Svc | Restarts      |
+-----------------------------------+-------+---------+--------------------+-----+-----------------------------+----------------+-----+-----+---------------+
| openshift-network-operator        | 1/1   | Running | Initialized: ✓     | 10d | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 8 (2h23m ago) | 
| network-operator-798d48796b-sfkf4 |       |         | PodScheduled: ✓    |     |                             |                |     |     |               | 
|                                   |       |         | ContainersReady: ✓ |     |                             |                |     |     |               | 
|                                   |       |         | Ready: ✓           |     |                             |                |     |     |               | 
+-----------------------------------+-------+---------+--------------------+-----+-----------------------------+----------------+-----+-----+---------------+

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
  devices: br-ex,eno5
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
  k8sServiceHost: "api-int.openshift.public.domain.com"
  k8sServicePort: 6443
  kubeProxyReplacement: "true"
  operator:
    prometheus:
      enabled: true
      serviceMonitor:
        enabled: true
    replicas: 1
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
          value: "api-int.openshift.public.domain.com"
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
    "socketDir": "/host/run/multus/socket",
    "auxiliaryCNIChainName": "vendor-cni-chain"
}
~~~
Config map udpated

Wait for Cilium resources
-------------------------

Take a nap...

- pod: clife-controller-manager-5c5ccd57bc-kknzt
- deployment: clife-controller-manager

+--------------------------+-------+------------+-----------+------+
| Deployment               | Ready | Up-To-Date | Available | Age  |
+--------------------------+-------+------------+-----------+------+
| cilium                   | 1/1   | 1          | 1         | 2h0m | 
| cilium-operator          |       |            |           |      | 
+--------------------------+-------+------------+-----------+------+
| cilium                   | 1/1   | 1          | 1         | 2h0m | 
| clife-controller-manager |       |            |           |      | 
+--------------------------+-------+------------+-----------+------+

+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+----------+
| Pod                                       | Ready | Status  | Condition          | Age  | Node                        | IP             | Net | Svc | Restarts |
+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+----------+
| cilium                                    | 0/1   | Pending | Initialized: ✓     | 2h0m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 0        | 
| cilium-envoy-7v7j9                        |       |         | PodScheduled: ✓    |      |                             |                |     |     |          | 
|                                           |       |         | ContainersReady: ✗ |      |                             |                |     |     |          | 
|                                           |       |         | Ready: ✗           |      |                             |                |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+----------+
| cilium                                    | 0/1   | Pending | Initialized: ✗     | 2h0m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 0        | 
| cilium-gfbjr                              |       |         | PodScheduled: ✓    |      |                             |                |     |     |          | 
|                                           |       |         | ContainersReady: ✗ |      |                             |                |     |     |          | 
|                                           |       |         | Ready: ✗           |      |                             |                |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h0m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 0        | 
| cilium-operator-79f555d58f-kssq5          |       |         | PodScheduled: ✓    |      |                             |                |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |      |                             |                |     |     |          | 
|                                           |       |         | Ready: ✓           |      |                             |                |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h0m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 0        | 
| clife-controller-manager-5c5ccd57bc-kknzt |       |         | PodScheduled: ✓    |      |                             |                |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |      |                             |                |     |     |          | 
|                                           |       |         | Ready: ✓           |      |                             |                |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+----------+

Step 5: Re-enable OpenShift operator management
===============================================


Delete kube API server pods
---------------------------

+--------------------------------------------+-------+---------+--------------------+-----+-----------------------------+----------------+-----+-----+----------------+
| Pod                                        | Ready | Status  | Condition          | Age | Node                        | IP             | Net | Svc | Restarts       |
+--------------------------------------------+-------+---------+--------------------+-----+-----------------------------+----------------+-----+-----+----------------+
| openshift-kube-apiserver                   | 5/5   | Running | Initialized: ✓     | 9d  | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 26 (2h25m ago) | 
| kube-apiserver-openshift.public.domain.com |       |         | PodScheduled: ✓    |     |                             |                |     |     |                | 
|                                            |       |         | ContainersReady: ✓ |     |                             |                |     |     |                | 
|                                            |       |         | Ready: ✓           |     |                             |                |     |     |                | 
+--------------------------------------------+-------+---------+--------------------+-----+-----------------------------+----------------+-----+-----+----------------+

Delete
- kube-apiserver-openshift.public.domain.com

Delete machine config deployments
---------------------------------

+-----------------------------------+-------+------------+-----------+-----+
| Deployment                        | Ready | Up-To-Date | Available | Age |
+-----------------------------------+-------+------------+-----------+-----+
| openshift-machine-config-operator | 1/1   | 1          | 1         | 10d | 
| machine-config-controller         |       |            |           |     | 
+-----------------------------------+-------+------------+-----------+-----+
| openshift-machine-config-operator | 1/1   | 1          | 1         | 10d | 
| machine-config-operator           |       |            |           |     | 
+-----------------------------------+-------+------------+-----------+-----+

+--------------------------------------------+-------+---------+--------------------+-----+-----------------------------+-------------+-----+-----+----------------+
| Pod                                        | Ready | Status  | Condition          | Age | Node                        | IP          | Net | Svc | Restarts       |
+--------------------------------------------+-------+---------+--------------------+-----+-----------------------------+-------------+-----+-----+----------------+
| openshift-machine-config-operator          | 2/2   | Running | Initialized: ✓     | 10d | openshift.public.domain.com | 10.128.0.34 | 0   | --  | 15 (2h21m ago) | 
| machine-config-controller-594f4479f5-54zn5 |       |         | PodScheduled: ✓    |     |                             |             |     |     |                | 
|                                            |       |         | ContainersReady: ✓ |     |                             |             |     |     |                | 
|                                            |       |         | Ready: ✓           |     |                             |             |     |     |                | 
+--------------------------------------------+-------+---------+--------------------+-----+-----------------------------+-------------+-----+-----+----------------+
| openshift-machine-config-operator          | 2/2   | Running | Initialized: ✓     | 10d | openshift.public.domain.com | 10.128.0.10 | 0   | --  | 15 (2h23m ago) | 
| machine-config-operator-847bd8d8b8-4d2pb   |       |         | PodScheduled: ✓    |     |                             |             |     |     |                | 
|                                            |       |         | ContainersReady: ✓ |     |                             |             |     |     |                | 
|                                            |       |         | Ready: ✓           |     |                             |             |     |     |                | 
+--------------------------------------------+-------+---------+--------------------+-----+-----------------------------+-------------+-----+-----+----------------+

Rollout restart

Take a nap...


Wait for deployment ready

+-----------------------------------+-------+------------+-----------+-----+
| Deployment                        | Ready | Up-To-Date | Available | Age |
+-----------------------------------+-------+------------+-----------+-----+
| openshift-machine-config-operator | 1/1   | 1          | 1         | 10d | 
| machine-config-controller         |       |            |           |     | 
+-----------------------------------+-------+------------+-----------+-----+
| openshift-machine-config-operator | 1/1   | 1          | 1         | 10d | 
| machine-config-operator           |       |            |           |     | 
+-----------------------------------+-------+------------+-----------+-----+

+------------------------------------------+-------+---------+--------------------+------+-----------------------------+--------------+-----+-----+----------+
| Pod                                      | Ready | Status  | Condition          | Age  | Node                        | IP           | Net | Svc | Restarts |
+------------------------------------------+-------+---------+--------------------+------+-----------------------------+--------------+-----+-----+----------+
| openshift-machine-config-operator        | 2/2   | Running | Initialized: ✓     | 2h0m | openshift.public.domain.com | 10.128.0.128 | 0   | --  | 0        | 
| machine-config-controller-69b67d5-d9zzf  |       |         | PodScheduled: ✓    |      |                             |              |     |     |          | 
|                                          |       |         | ContainersReady: ✓ |      |                             |              |     |     |          | 
|                                          |       |         | Ready: ✓           |      |                             |              |     |     |          | 
+------------------------------------------+-------+---------+--------------------+------+-----------------------------+--------------+-----+-----+----------+
| openshift-machine-config-operator        | 2/2   | Running | Initialized: ✓     | 2h0m | openshift.public.domain.com | 10.128.0.127 | 0   | --  | 0        | 
| machine-config-operator-758655df57-tprp8 |       |         | PodScheduled: ✓    |      |                             |              |     |     |          | 
|                                          |       |         | ContainersReady: ✓ |      |                             |              |     |     |          | 
|                                          |       |         | Ready: ✓           |      |                             |              |     |     |          | 
+------------------------------------------+-------+---------+--------------------+------+-----------------------------+--------------+-----+-----+----------+

Network Operator
----------------

+----------------------------+-------+------------+-----------+-----+
| Deployment                 | Ready | Up-To-Date | Available | Age |
+----------------------------+-------+------------+-----------+-----+
| openshift-network-operator | 0/0   | None       | None      | 10d | 
| network-operator           |       |            |           |     | 
+----------------------------+-------+------------+-----------+-----+

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

+--------------------------------------------------------+---------+---------+-------+-----+
| Replica Set                                            | Desired | Current | Ready | Age |
+--------------------------------------------------------+---------+---------+-------+-----+
| openshift-network-operator/network-operator-798d48796b | 1       | 1       | 1     | 10d | 
+--------------------------------------------------------+---------+---------+-------+-----+

+-----------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+----------+
| Pod                               | Ready | Status  | Condition          | Age  | Node                        | IP             | Net | Svc | Restarts |
+-----------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+----------+
| openshift-network-operator        | 1/1   | Running | Initialized: ✓     | 2h0m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 0        | 
| network-operator-798d48796b-tbdk2 |       |         | PodScheduled: ✓    |      |                             |                |     |     |          | 
|                                   |       |         | ContainersReady: ✓ |      |                             |                |     |     |          | 
|                                   |       |         | Ready: ✓           |      |                             |                |     |     |          | 
+-----------------------------------+-------+---------+--------------------+------+-----------------------------+----------------+-----+-----+----------+

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

Wait for no kubernetes api [1hr]...
Wait for kubernetes api [30min]...

Step 7: Wait cluster ready
==========================

Wait nodes ready [30min]...

+-----------------------------+-------+--------+------+-----+-----+-----+--------+----------------------+-----+
| Node                        | Ready | Memory | Disk | PID | CNV | MCP | Role   | IP                   | Age |
+-----------------------------+-------+--------+------+-----+-----+-----+--------+----------------------+-----+
| openshift.public.domain.com | ✓     | ✓      | ✓    | ✓   | ✓   | ✗   | Master | 166.11.170.180 (int) | 10d | 
|                             |       |        |      |     |     |     | Worker |                      |     | 
+-----------------------------+-------+--------+------+-----+-----+-----+--------+----------------------+-----+

Wait machine config pool ready [1hr]...

+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+---------------------------------+-----+
| Machine Config Pool | Config                                           | Updated | Updating | Degraded | Machines | Ready | Updated | Degraded | Unavail | Machine Config                  | Age |
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+---------------------------------+-----+
| master              | rendered-master-4320b886e0195d20e70e326bb7d57416 | ✓       | ✗        | ✗        | 1        | 1     | 1       | 0        | 0       | 00-master                       | 10d | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-master-container-runtime     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-master-kubelet               |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 50-master-dnsmasq-configuration |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 50-masters-chrony-configuration |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 97-master-generated-kubelet     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 98-master-generated-kubelet     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-master-generated-registries  |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-master-ssh                   |     | 
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+---------------------------------+-----+
| worker              | rendered-worker-9073a9791cddaabe3fb9da5dea0df801 | ✓       | ✗        | ✗        | 0        | 0     | 0       | 0        | 0       | 00-worker                       | 10d | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-worker-container-runtime     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-worker-kubelet               |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 50-workers-chrony-configuration |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 97-worker-generated-kubelet     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 98-worker-generated-kubelet     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-worker-generated-registries  |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-worker-ssh                   |     | 
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+---------------------------------+-----+

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

+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| Cluster Operator                         | Version | Owner          | Available | Progressing | Degraded | Upgradeable | Since | Age |
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| authentication                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h10m | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| baremetal                                | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| cloud-controller-manager                 | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| cloud-credential                         | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| cluster-autoscaler                       | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| config-operator                          | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| console                                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| control-plane-machine-set                | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| csi-snapshot-controller                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| dns                                      | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h5m  | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| etcd                                     | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| image-registry                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 9d    | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| ingress                                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| insights                                 | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| kube-apiserver                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| kube-controller-manager                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| kube-scheduler                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| kube-storage-version-migrator            | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| machine-api                              | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| machine-approver                         | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| machine-config                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| marketplace                              | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| monitoring                               | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 9d    | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| network                                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| node-tuning                              | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| olm                                      | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| openshift-apiserver                      | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 9d    | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| openshift-controller-manager             | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 9d    | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| openshift-samples                        | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| operator-lifecycle-manager               | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| operator-lifecycle-manager-catalog       | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| operator-lifecycle-manager-packageserver | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h5m  | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| service-ca                               | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| storage                                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+

Wait for Cilium resources
-------------------------

Take a nap...

- pod: cilium-envoy-7v7j9
- pod: cilium-gfbjr
- pod: cilium-operator-79f555d58f-kssq5
- pod: clife-controller-manager-5c5ccd57bc-kknzt
- deployment: cilium-operator
- deployment: clife-controller-manager

+--------------------------+-------+------------+-----------+-------+
| Deployment               | Ready | Up-To-Date | Available | Age   |
+--------------------------+-------+------------+-----------+-------+
| cilium                   | 1/1   | 1          | 1         | 2h16m | 
| cilium-operator          |       |            |           |       | 
+--------------------------+-------+------------+-----------+-------+
| cilium                   | 1/1   | 1          | 1         | 2h16m | 
| clife-controller-manager |       |            |           |       | 
+--------------------------+-------+------------+-----------+-------+

+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| Pod                                       | Ready | Status  | Condition          | Age   | Node                        | IP             | Net | Svc | Restarts     |
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h16m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 1 (2h7m ago) | 
| cilium-envoy-7v7j9                        |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h16m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 1 (2h7m ago) | 
| cilium-gfbjr                              |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h16m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 2 (2h7m ago) | 
| cilium-operator-79f555d58f-kssq5          |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h16m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 3 (2h7m ago) | 
| clife-controller-manager-5c5ccd57bc-kknzt |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+

Step 8: Post migration
======================

Remove device from cilium config
- patched
Deployment [cilium/cilium-operator] patch successful
Daemon set [cilium/cilium] patch successful

Wait for Cilium resources
-------------------------

Take a nap...

- pod: cilium-envoy-7v7j9
- pod: cilium-operator-849cdbd5c-2snz4
- pod: cilium-vp29d
- pod: clife-controller-manager-5c5ccd57bc-kknzt
- deployment: cilium-operator
- deployment: clife-controller-manager

+--------------------------+-------+------------+-----------+-------+
| Deployment               | Ready | Up-To-Date | Available | Age   |
+--------------------------+-------+------------+-----------+-------+
| cilium                   | 1/1   | 1          | 1         | 2h16m | 
| cilium-operator          |       |            |           |       | 
+--------------------------+-------+------------+-----------+-------+
| cilium                   | 1/1   | 1          | 1         | 2h17m | 
| clife-controller-manager |       |            |           |       | 
+--------------------------+-------+------------+-----------+-------+

+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| Pod                                       | Ready | Status  | Condition          | Age   | Node                        | IP             | Net | Svc | Restarts     |
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h16m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 1 (2h7m ago) | 
| cilium-envoy-7v7j9                        |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h0m  | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 0            | 
| cilium-operator-849cdbd5c-2snz4           |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h0m  | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 0            | 
| cilium-vp29d                              |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h17m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 3 (2h7m ago) | 
| clife-controller-manager-5c5ccd57bc-kknzt |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+

Approve cilium install plan
- installplan cilium/install-f4pbv will be approved
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
.kube directory created
kubeconfig uploaded

OpenShift Workflow - Install cilium cli
=======================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "check_verbose": false,
    "url": "https://github.com/cilium/cilium-cli/releases/download/v0.18.6/cilium-linux-amd64.tar.gz",
    "check-verbose": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [166.11.170.180] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- management node [166.11.170.180] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- cli cilium: not found

Downloading cilium binary from https://github.com/cilium/cilium-cli/releases/download/v0.18.6/cilium-linux-amd64.tar.gz
Uploading cilium binary to cluster management node
Unpack
Change file flags
Cilium binary ready to be used
cilium-cli: v0.18.6 compiled with go1.24.5 on linux/amd64
cilium image (default): v1.18.0
cilium image (stable): v1.18.2
cilium image (running): unknown. Unable to obtain cilium version. Reason: Kubernetes cluster unreachable: Get "http://localhost:8080/version": dial tcp [::1]:8080: connect: connection refused

~~~
    /¯¯\
 /¯¯\__/¯¯\    Cilium:             OK
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Envoy DaemonSet:    OK
 \__/¯¯\__/    Hubble Relay:       disabled
    \__/       ClusterMesh:        disabled

DaemonSet              cilium                   Desired: 1, Ready: 1/1, Available: 1/1
DaemonSet              cilium-envoy             Desired: 1, Ready: 1/1, Available: 1/1
Deployment             cilium-operator          Desired: 1, Ready: 1/1, Available: 1/1
Containers:            cilium                   Running: 1
                       cilium-envoy             Running: 1
                       cilium-operator          Running: 1
                       clustermesh-apiserver
                       hubble-relay
Cluster Pods:          102/102 managed by Cilium
Helm chart version:
~~~

Step 9: Cluster Restart
=======================


Reload nodes
- openshift.public.domain.com

Wait for no kubernetes api [1hr]...
Wait for kubernetes api [30min]...
Wait nodes ready [30min]...

+-----------------------------+-------+--------+------+-----+-----+-----+--------+----------------------+-----+
| Node                        | Ready | Memory | Disk | PID | CNV | MCP | Role   | IP                   | Age |
+-----------------------------+-------+--------+------+-----+-----+-----+--------+----------------------+-----+
| openshift.public.domain.com | ✓     | ✓      | ✓    | ✓   | ✓   | ✓   | Master | 166.11.170.180 (int) | 10d | 
|                             |       |        |      |     |     |     | Worker |                      |     | 
+-----------------------------+-------+--------+------+-----+-----+-----+--------+----------------------+-----+

Wait machine config pool ready [1hr]...

+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+---------------------------------+-----+
| Machine Config Pool | Config                                           | Updated | Updating | Degraded | Machines | Ready | Updated | Degraded | Unavail | Machine Config                  | Age |
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+---------------------------------+-----+
| master              | rendered-master-4320b886e0195d20e70e326bb7d57416 | ✓       | ✗        | ✗        | 1        | 1     | 1       | 0        | 0       | 00-master                       | 10d | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-master-container-runtime     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-master-kubelet               |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 50-master-dnsmasq-configuration |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 50-masters-chrony-configuration |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 97-master-generated-kubelet     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 98-master-generated-kubelet     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-master-generated-registries  |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-master-ssh                   |     | 
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+---------------------------------+-----+
| worker              | rendered-worker-9073a9791cddaabe3fb9da5dea0df801 | ✓       | ✗        | ✗        | 0        | 0     | 0       | 0        | 0       | 00-worker                       | 10d | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-worker-container-runtime     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 01-worker-kubelet               |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 50-workers-chrony-configuration |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 97-worker-generated-kubelet     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 98-worker-generated-kubelet     |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-worker-generated-registries  |     | 
|                     |                                                  |         |          |          |          |       |         |          |         | 99-worker-ssh                   |     | 
+---------------------+--------------------------------------------------+---------+----------+----------+----------+-------+---------+----------+---------+---------------------------------+-----+

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

+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| Cluster Operator                         | Version | Owner          | Available | Progressing | Degraded | Upgradeable | Since | Age |
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| authentication                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h55m | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| baremetal                                | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| cloud-controller-manager                 | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| cloud-credential                         | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| cluster-autoscaler                       | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| config-operator                          | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| console                                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| control-plane-machine-set                | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| csi-snapshot-controller                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| dns                                      | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h44m | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| etcd                                     | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| image-registry                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 9d    | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| ingress                                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| insights                                 | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| kube-apiserver                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| kube-controller-manager                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| kube-scheduler                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| kube-storage-version-migrator            | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| machine-api                              | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| machine-approver                         | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| machine-config                           | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| marketplace                              | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| monitoring                               | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 9d    | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| network                                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| node-tuning                              | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| olm                                      | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| openshift-apiserver                      | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 9d    | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| openshift-controller-manager             | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 9d    | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| openshift-samples                        | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| operator-lifecycle-manager               | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| operator-lifecycle-manager-catalog       | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| operator-lifecycle-manager-packageserver | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 2h50m | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| service-ca                               | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+
| storage                                  | 4.19.13 | ClusterVersion | ✓         | ✓           | ✓        | ✓           | 10d   | 10d | 
|                                          |         | version        |           |             |          |             |       |     | 
+------------------------------------------+---------+----------------+-----------+-------------+----------+-------------+-------+-----+

Wait for Cilium resources
-------------------------

Take a nap...

- pod: cilium-envoy-7v7j9
- pod: cilium-operator-849cdbd5c-2snz4
- pod: cilium-vp29d
- pod: clife-controller-manager-5755b9f7f5-s7gbc
- deployment: cilium-operator
- deployment: clife-controller-manager

+--------------------------+-------+------------+-----------+------+
| Deployment               | Ready | Up-To-Date | Available | Age  |
+--------------------------+-------+------------+-----------+------+
| cilium                   | 1/1   | 1          | 1         | 3h1m | 
| cilium-operator          |       |            |           |      | 
+--------------------------+-------+------------+-----------+------+
| cilium                   | 1/1   | 1          | 1         | 3h1m | 
| clife-controller-manager |       |            |           |      | 
+--------------------------+-------+------------+-----------+------+

+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| Pod                                       | Ready | Status  | Condition          | Age   | Node                        | IP             | Net | Svc | Restarts     |
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 3h1m  | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 2 (2h0m ago) | 
| cilium-envoy-7v7j9                        |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h44m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 1 (2h0m ago) | 
| cilium-operator-849cdbd5c-2snz4           |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h44m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 1 (2h0m ago) | 
| cilium-vp29d                              |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h44m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 2 (2h0m ago) | 
| clife-controller-manager-5755b9f7f5-s7gbc |       |         | PodScheduled: ✓    |       |                             |                |     |     |              | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |              | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |              | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+--------------+

~~~
    /¯¯\
 /¯¯\__/¯¯\    Cilium:             OK
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Envoy DaemonSet:    OK
 \__/¯¯\__/    Hubble Relay:       disabled
    \__/       ClusterMesh:        disabled

DaemonSet              cilium                   Desired: 1, Ready: 1/1, Available: 1/1
DaemonSet              cilium-envoy             Desired: 1, Ready: 1/1, Available: 1/1
Deployment             cilium-operator          Desired: 1, Ready: 1/1, Available: 1/1
Containers:            cilium                   Running: 1
                       cilium-envoy             Running: 1
                       cilium-operator          Running: 1
                       clustermesh-apiserver    
                       hubble-relay             
Cluster Pods:          102/104 managed by Cilium
Helm chart version:    
~~~
```

[[Back]](./README.md)