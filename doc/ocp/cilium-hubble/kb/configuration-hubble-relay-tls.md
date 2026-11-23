## Hubble Relay with TLS

[[Back]](../README.md)

When Hubble Relay is deployed, Hubble listens on a TCP port on the host network. This allows Hubble Relay to communicate with all Hubble instances in the cluster. Connections between Hubble instances and Hubble Relay are secured using mutual TLS (mTLS) by default.

TLS certificates can be generated automatically incl. certificate rotation. As Hubble server and Hubble Relay support TLS certificates hot reloading, including CA certificates, this does not disrupt any existing connection. New connections are automatically established using the new certificates without having to restart Hubble server or Hubble Relay.

While there are several methods for automatic TLS certificate generation and rotation, this document relies on [certificate manager](../../cert-manager/README.md) that issues certificate locally in-cluster based on user-provided certificate authority (CA). Note that cert-manager can integrate with external certificate managers services.

## Cilium configuration

hubble:tls:auto:certManagerIssuerRef:name refers to ClusterIssuer object created in previous step

```yaml
spec:
  hubble:
    enabled: true
    relay:
      enabled: true
    tls:
      auto:
        certManagerIssuerRef:
          group: cert-manager.io
          kind: ClusterIssuer
          name: cilium-root-ca
        certValidityDuration: 1
        enabled: true
        method: certmanager
      enabled: true
```

## Cert manager 

Step 1: Install

[iserver-way](../../cert-manager/enable.md) or follow [official documentation](https://cert-manager.io/docs/installation/)

Step 2: Define ClusterIssuer

`ClusterIssuer` is cluster-wide custom resource with certificate authority (CA) that generate signed certificates. It refers to `Secret` object by name that must exist in `cert-manager` namespace and contain  ca certificate file (tls.crt) and ca private key (tls.key)

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: cilium-root-ca
spec:
  ca:
    secretName: cilium-root-ca
```

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: cilium-root-ca
  namespace: cert-manager
type: kubernetes.io/tls
data:
  tls.crt: ...
  tls.key: ...
```

## Config map

```
$ oc get configmaps -n cilium cilium-config -o yaml | grep -i hubble
  diagnostics-export-file: /var/run/cilium/hubble/status.log
  enable-hubble: "true"
  hubble-connectionlog-export-enabled: "false"
  hubble-disable-tls: "false"
  hubble-listen-address: :4244
  hubble-network-policy-correlation-enabled: "true"
  hubble-socket-path: /var/run/cilium/hubble.sock
  hubble-tls-cert-file: /var/lib/cilium/tls/hubble/server.crt
  hubble-tls-client-ca-files: /var/lib/cilium/tls/hubble/client-ca.crt
  hubble-tls-key-file: /var/lib/cilium/tls/hubble/server.key
```

## Hubble Relay

```
$ oc get deployment -n cilium
NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
hubble-relay               1/1     1            1           5d23h

$ oc get pod -n cilium
NAME                                        READY   STATUS    RESTARTS      AGE
hubble-cli-7b54bf5dcc-hzf8t                 1/1     Running   0             4d1h
```

Pod definition has extra volumes as compared with [no tls mode](./configuration-hubble-relay-no-tls.md)

```yaml
  - name: tls
    projected:
      defaultMode: 256
      sources:
      - secret:
          items:
          - key: tls.crt
            path: client.crt
          - key: tls.key
            path: client.key
          - key: ca.crt
            path: hubble-server-ca.crt
          name: hubble-relay-client-certs
```

Full definition

```yaml
$ oc get pod -n cilium hubble-relay-fb86549f4-sx8rq -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "portmap",
          "interface": "eth0",
          "ips": [
              "10.128.5.238"
          ],
          "mac": "72:97:14:51:bd:a2",
          "default": true,
          "dns": {},
          "gateway": [
              "10.128.5.173"
          ]
      }]
  creationTimestamp: "2026-06-26T12:53:22Z"
  generateName: hubble-relay-fb86549f4-
  labels:
    app.kubernetes.io/name: hubble-relay
    app.kubernetes.io/part-of: cilium
    k8s-app: hubble-relay
    pod-template-hash: fb86549f4
  name: hubble-relay-fb86549f4-sx8rq
  namespace: cilium
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: ReplicaSet
    name: hubble-relay-fb86549f4
    uid: 9cd660ef-7bc3-423c-a90d-62f1693717f5
  resourceVersion: "136145943"
  uid: 5ea1fb8b-85a9-463c-9e55-6e09694cad96
spec:
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchLabels:
            k8s-app: cilium
        topologyKey: kubernetes.io/hostname
  automountServiceAccountToken: false
  containers:
  - args:
    - serve
    command:
    - hubble-relay
    image: quay.io/isovalent-dev/...
    imagePullPolicy: IfNotPresent
    livenessProbe:
      failureThreshold: 12
      grpc:
        port: 4222
        service: ""
      initialDelaySeconds: 10
      periodSeconds: 10
      successThreshold: 1
      timeoutSeconds: 10
    name: hubble-relay
    ports:
    - containerPort: 4245
      name: grpc
      protocol: TCP
    readinessProbe:
      failureThreshold: 3
      grpc:
        port: 4222
        service: ""
      periodSeconds: 10
      successThreshold: 1
      timeoutSeconds: 3
    resources: {}
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
        - ALL
      runAsGroup: 65532
      runAsNonRoot: true
      runAsUser: 65532
      seccompProfile:
        type: RuntimeDefault
    startupProbe:
      failureThreshold: 20
      grpc:
        port: 4222
        service: ""
      initialDelaySeconds: 10
      periodSeconds: 3
      successThreshold: 1
      timeoutSeconds: 1
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: FallbackToLogsOnError
    volumeMounts:
    - mountPath: /etc/hubble-relay
      name: config
      readOnly: true
    - mountPath: /var/lib/hubble-relay/tls
      name: tls
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  nodeName: bm1-2
  nodeSelector:
    kubernetes.io/os: linux
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  restartPolicy: Always
  schedulerName: default-scheduler
  securityContext:
    fsGroup: 65532
    seccompProfile:
      type: RuntimeDefault
  serviceAccount: hubble-relay
  serviceAccountName: hubble-relay
  terminationGracePeriodSeconds: 1
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  volumes:
  - configMap:
      defaultMode: 420
      items:
      - key: config.yaml
        path: config.yaml
      name: hubble-relay-config
    name: config
  - name: tls
    projected:
      defaultMode: 256
      sources:
      - secret:
          items:
          - key: tls.crt
            path: client.crt
          - key: tls.key
            path: client.key
          - key: ca.crt
            path: hubble-server-ca.crt
          name: hubble-relay-client-certs
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2026-06-26T12:53:23Z"
    status: "True"
    type: PodReadyToStartContainers
  - lastProbeTime: null
    lastTransitionTime: "2026-06-26T12:53:22Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2026-06-26T12:53:58Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2026-06-26T12:53:58Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2026-06-26T12:53:22Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: cri-o://8ae0f6c8fd4f2d55105fcc171e23b53173428ecf5230fb1eb993f097e2f0af4f
    image: quay.io/isovalent-dev/hubble-relay-ubi-ci...
    imageID: quay.io/isovalent-dev/hubble-relay-ubi-ci...
    lastState: {}
    name: hubble-relay
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2026-06-26T12:53:23Z"
    volumeMounts:
    - mountPath: /etc/hubble-relay
      name: config
      readOnly: true
      recursiveReadOnly: Disabled
    - mountPath: /var/lib/hubble-relay/tls
      name: tls
      readOnly: true
      recursiveReadOnly: Disabled
  hostIP: 10.10.10.66
  hostIPs:
  - ip: 10.10.10.66
  phase: Running
  podIP: 10.128.5.238
  podIPs:
  - ip: 10.128.5.238
  qosClass: BestEffort
  startTime: "2026-06-26T12:53:22Z"
```

Hubble servers added successfully as peers, where 10.10.10.x is node ip

```
$ oc logs -n cilium hubble-relay-fb86549f4-pbrml
time=2026-06-25T09:09:44.196659401Z level=info msg="Starting gRPC health server..." subsys=hubble-relay address=:4222
time=2026-06-25T09:09:44.19670881Z level=info msg="Starting gRPC server..." subsys=hubble-relay options="{peerTarget:hubble-peer.cilium.svc.cluster.local.:443 retryTimeout:30000000000 listenAddress::4245 healthListenAddress::4222 metricsListenAddress: log:0xc00048d920 serverTLSConfig:<nil> insecureServer:true clientTLSConfig:0xc00048dc60 clusterName:default insecureClient:false observerOptions:[0x22d8840 0x22d8920] grpcMetrics:<nil> grpcUnaryInterceptors:[0x2390280] grpcStreamInterceptors:[0x2390340]}"
time=2026-06-25T09:09:44.21006888Z level=info msg="Received peer change notification" subsys=hubble-relay changeNotification="name:\"bm1-2\"  address:\"10.10.10.66:4244\"  type:PEER_ADDED  tls:{server_name:\"bm1-2.default.hubble-grpc.cilium.io\"}"
time=2026-06-25T09:09:44.210195873Z level=info msg="Received peer change notification" subsys=hubble-relay changeNotification="name:\"bm1-3\"  address:\"10.10.10.67:4244\"  type:PEER_ADDED  tls:{server_name:\"bm1-3.default.hubble-grpc.cilium.io\"}"
time=2026-06-25T09:09:44.210211367Z level=info msg="Received peer change notification" subsys=hubble-relay changeNotification="name:\"bm1-1\"  address:\"10.10.10.65:4244\"  type:PEER_ADDED  tls:{server_name:\"bm1-1.default.hubble-grpc.cilium.io\"}"
time=2026-06-25T09:09:44.210274447Z level=info msg=Connecting subsys=hubble-relay address=10.10.10.65:4244 tls=true peer=bm1-1
time=2026-06-25T09:09:44.21032387Z level=info msg=Connected subsys=hubble-relay address=10.10.10.65:4244 tls=true peer=bm1-1
time=2026-06-25T09:09:44.210395482Z level=info msg=Connecting subsys=hubble-relay address=10.10.10.66:4244 tls=true peer=bm1-2
time=2026-06-25T09:09:44.210420674Z level=info msg=Connecting subsys=hubble-relay address=10.10.10.67:4244 tls=true peer=bm1-3
time=2026-06-25T09:09:44.210590289Z level=info msg=Connected subsys=hubble-relay address=10.10.10.66:4244 tls=true peer=bm1-2
time=2026-06-25T09:09:44.210619457Z level=info msg=Connected subsys=hubble-relay address=10.10.10.67:4244 tls=true peer=bm1-3
```

## Service

```
$ oc get service -n cilium
NAME              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
hubble-peer       ClusterIP   172.30.77.238    <none>        443/TCP    251d
hubble-relay      ClusterIP   172.30.139.127   <none>        80/TCP     5d23h
```

```yaml
apiVersion: v1
kind: Service
metadata:
  annotations:
    meta.helm.sh/release-name: cilium-release
    meta.helm.sh/release-namespace: cilium
  creationTimestamp: "2026-06-23T10:30:19Z"
  labels:
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: hubble-relay
    app.kubernetes.io/part-of: cilium
    app.kubernetes.io/version: 1.19.0
    isovalent.io/managed-by: clife
    k8s-app: hubble-relay
  name: hubble-relay
  namespace: cilium
  ownerReferences:
  - apiVersion: cilium.io/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: CiliumConfig
    name: ciliumconfig
    uid: 23c5b57e-6fa3-429c-a86f-3e212122b307
  resourceVersion: "133707505"
  uid: 072c8d00-de5b-4da9-a865-5639769fea88
spec:
  clusterIP: 172.30.139.127
  clusterIPs:
  - 172.30.139.127
  internalTrafficPolicy: Cluster
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - port: 80
    protocol: TCP
    targetPort: grpc
  selector:
    k8s-app: hubble-relay
  sessionAffinity: None
  type: ClusterIP
status:
  loadBalancer: {}
```

```yaml
apiVersion: v1
kind: Service
metadata:
  annotations:
    meta.helm.sh/release-name: cilium-release
    meta.helm.sh/release-namespace: cilium
  creationTimestamp: "2025-10-20T17:45:37Z"
  labels:
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: hubble-peer
    app.kubernetes.io/part-of: cilium
    app.kubernetes.io/version: 1.19.0
    isovalent.io/managed-by: clife
    k8s-app: cilium
  name: hubble-peer
  namespace: cilium
  ownerReferences:
  - apiVersion: cilium.io/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: CiliumConfig
    name: ciliumconfig
    uid: 23c5b57e-6fa3-429c-a86f-3e212122b307
  resourceVersion: "136145231"
  uid: 832ebb20-75e6-4c8e-9519-2e61b55fe9e7
spec:
  clusterIP: 172.30.77.238
  clusterIPs:
  - 172.30.77.238
  internalTrafficPolicy: Local
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - name: peer-service
    port: 443
    protocol: TCP
    targetPort: 4244
  selector:
    k8s-app: cilium
  sessionAffinity: None
  type: ClusterIP
status:
  loadBalancer: {}
```

```
$ oc get ep -n cilium
NAME              ENDPOINTS                                            AGE
hubble-peer       10.10.10.65:4244,10.10.10.66:4244,10.10.10.67:4244   83m
hubble-relay      10.128.5.238:4245                                    83m
```

## Cilium status

```
$ cilium status -n cilium
    /¯¯\
 /¯¯\__/¯¯\    Cilium:             OK
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Envoy DaemonSet:    OK
 \__/¯¯\__/    Hubble Relay:       OK
    \__/       ClusterMesh:        disabled

DaemonSet              cilium                   Desired: 3, Ready: 3/3, Available: 3/3
DaemonSet              cilium-envoy             Desired: 3, Ready: 3/3, Available: 3/3
Deployment             cilium-operator          Desired: 2, Ready: 2/2, Available: 2/2
Deployment             hubble-relay             Desired: 1, Ready: 1/1, Available: 1/1
Containers:            cilium                   Running: 3
                       cilium-envoy             Running: 3
                       cilium-operator          Running: 2
                       clustermesh-apiserver    
                       hubble-relay             Running: 1
Cluster Pods:          171/171 managed by Cilium
```

## Verification

Certificate requested automatically based on cilium configuration

```
$ oc get certificaterequests.cert-manager.io -A
NAMESPACE   NAME                          APPROVED   DENIED   READY   ISSUER           REQUESTER                                         AGE
cilium      hubble-relay-client-certs-1   True                True    cilium-root-ca   system:serviceaccount:cert-manager:cert-manager   4h37m
cilium      hubble-server-certs-1         True                True    cilium-root-ca   system:serviceaccount:cert-manager:cert-manager   4h37m
```

Certificate created as per request

```
$ oc get certificate -A
NAMESPACE   NAME                        READY   SECRET                      AGE
cilium      hubble-relay-client-certs   True    hubble-relay-client-certs   21h
cilium      hubble-server-certs         True    hubble-server-certs         21h
```

Hubble relay pod running and using these certificates

```
$ oc get pod -n cilium
NAME                                        READY   STATUS    RESTARTS     AGE
hubble-relay-fb86549f4-pbrml                1/1     Running   0            21h
```

Hubble servers added successfully as peers, where 10.10.10.x is node ip

```
$ oc logs -n cilium hubble-relay-fb86549f4-pbrml
time=2026-06-25T09:09:44.196659401Z level=info msg="Starting gRPC health server..." subsys=hubble-relay address=:4222
time=2026-06-25T09:09:44.19670881Z level=info msg="Starting gRPC server..." subsys=hubble-relay options="{peerTarget:hubble-peer.cilium.svc.cluster.local.:443 retryTimeout:30000000000 listenAddress::4245 healthListenAddress::4222 metricsListenAddress: log:0xc00048d920 serverTLSConfig:<nil> insecureServer:true clientTLSConfig:0xc00048dc60 clusterName:default insecureClient:false observerOptions:[0x22d8840 0x22d8920] grpcMetrics:<nil> grpcUnaryInterceptors:[0x2390280] grpcStreamInterceptors:[0x2390340]}"
time=2026-06-25T09:09:44.21006888Z level=info msg="Received peer change notification" subsys=hubble-relay changeNotification="name:\"bm1-2\"  address:\"10.10.10.66:4244\"  type:PEER_ADDED  tls:{server_name:\"bm1-2.default.hubble-grpc.cilium.io\"}"
time=2026-06-25T09:09:44.210195873Z level=info msg="Received peer change notification" subsys=hubble-relay changeNotification="name:\"bm1-3\"  address:\"10.10.10.67:4244\"  type:PEER_ADDED  tls:{server_name:\"bm1-3.default.hubble-grpc.cilium.io\"}"
time=2026-06-25T09:09:44.210211367Z level=info msg="Received peer change notification" subsys=hubble-relay changeNotification="name:\"bm1-1\"  address:\"10.10.10.65:4244\"  type:PEER_ADDED  tls:{server_name:\"bm1-1.default.hubble-grpc.cilium.io\"}"
time=2026-06-25T09:09:44.210274447Z level=info msg=Connecting subsys=hubble-relay address=10.10.10.65:4244 tls=true peer=bm1-1
time=2026-06-25T09:09:44.21032387Z level=info msg=Connected subsys=hubble-relay address=10.10.10.65:4244 tls=true peer=bm1-1
time=2026-06-25T09:09:44.210395482Z level=info msg=Connecting subsys=hubble-relay address=10.10.10.66:4244 tls=true peer=bm1-2
time=2026-06-25T09:09:44.210420674Z level=info msg=Connecting subsys=hubble-relay address=10.10.10.67:4244 tls=true peer=bm1-3
time=2026-06-25T09:09:44.210590289Z level=info msg=Connected subsys=hubble-relay address=10.10.10.66:4244 tls=true peer=bm1-2
time=2026-06-25T09:09:44.210619457Z level=info msg=Connected subsys=hubble-relay address=10.10.10.67:4244 tls=true peer=bm1-3
```

[[Back]](../README.md)