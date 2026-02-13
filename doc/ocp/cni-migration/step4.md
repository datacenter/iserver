# Cilium EE migration workflow

[[Back]](./step3.md) [[Next]](./step5.md)

## Step 4: Deploy Cilium

- fixup CiliumConfig
    - clusterPoolIPv4PodCIDRList and clusterPoolIPv4MaskSize following user-input values
    - k8sServiceHost and k8sServicePort based on internal api endpoint
    - devices set to br-ex with upstream interface of ovs
    - tunnelPort set to 4789
    - operator.replicas set to 1 if SNO
- fixup Deployment of CLife controller manager
    - env section with kubernetes service host and port based on internal api endpoint
- apply manifests
- update multus
- wait for cilium resources

### Output

```
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
  devices: br-ex,ens192
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
Continue [Y/N]? y

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

- pod: cilium-envoy-jf7wg
- pod: cilium-operator-79f555d58f-wjrj6
- pod: cilium-tr6cr
- pod: clife-controller-manager-5c5ccd57bc-2p7ln
- deployment: cilium-operator
- deployment: clife-controller-manager

+--------------------------+-------+------------+-----------+-------+
| Deployment               | Ready | Up-To-Date | Available | Age   |
+--------------------------+-------+------------+-----------+-------+
| cilium                   | 1/1   | 1          | 1         | 2h25m | 
| cilium-operator          |       |            |           |       | 
+--------------------------+-------+------------+-----------+-------+
| cilium                   | 1/1   | 1          | 1         | 2h25m | 
| clife-controller-manager |       |            |           |       | 
+--------------------------+-------+------------+-----------+-------+

+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+----------+
| Pod                                       | Ready | Status  | Condition          | Age   | Node                        | IP             | Net | Svc | Restarts |
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h25m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 0        | 
| cilium-envoy-jf7wg                        |       |         | PodScheduled: ✓    |       |                             |                |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |          | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h25m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 0        | 
| cilium-operator-79f555d58f-wjrj6          |       |         | PodScheduled: ✓    |       |                             |                |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |          | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h25m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 0        | 
| cilium-tr6cr                              |       |         | PodScheduled: ✓    |       |                             |                |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |          | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+----------+
| cilium                                    | 1/1   | Running | Initialized: ✓     | 2h25m | openshift.public.domain.com | 166.11.170.180 | 0   | --  | 0        | 
| clife-controller-manager-5c5ccd57bc-2p7ln |       |         | PodScheduled: ✓    |       |                             |                |     |     |          | 
|                                           |       |         | ContainersReady: ✓ |       |                             |                |     |     |          | 
|                                           |       |         | Ready: ✓           |       |                             |                |     |     |          | 
+-------------------------------------------+-------+---------+--------------------+-------+-----------------------------+----------------+-----+-----+----------+
```

[[Back]](./step3.md) [[Next]](./step5.md)