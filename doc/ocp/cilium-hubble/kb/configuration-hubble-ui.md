## Hubble UI

[[Back]](../README.md)

Hubble UI needs to be enabled in Cilium configuration, it expects Hubble Relay being enabled either with or without TLS

## Cilium configuration

>[!NOTE]
>Example below uses relay without tls

```yaml
spec:
  hubble:
    enabled: true
    relay:
      enabled: true
    tls:
      enabled: false
    ui:
      enabled: true
```

## UI

Once enabled, hubble ui runs in dedicated deployment

```
$ oc get deployment -n cilium
NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
hubble-ui                  1/1     1            1           81s
```

```
$ oc get pod -n cilium
NAME                                        READY   STATUS    RESTARTS      AGE
hubble-ui-7fc9dd9559-kdmp7                  2/2     Running   0             112s
```

It has two containers
- frontend based on nginx that listens on port 8081
- backend that listens for events from hubble relay on port 8090 (gRPC)

```yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "portmap",
          "interface": "eth0",
          "ips": [
              "10.128.4.140"
          ],
          "mac": "0e:23:1e:31:75:87",
          "default": true,
          "dns": {},
          "gateway": [
              "10.128.5.173"
          ]
      }]
  creationTimestamp: "2026-06-29T10:05:30Z"
  generateName: hubble-ui-7fc9dd9559-
  labels:
    app.kubernetes.io/name: hubble-ui
    app.kubernetes.io/part-of: cilium
    k8s-app: hubble-ui
    pod-template-hash: 7fc9dd9559
  name: hubble-ui-7fc9dd9559-kdmp7
  namespace: cilium
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: ReplicaSet
    name: hubble-ui-7fc9dd9559
    uid: 5f3a2105-a04f-4370-b27b-19fa4d47d2d9
  resourceVersion: "138409353"
  uid: c401383c-275e-4bcd-a11c-10eb2300880d
spec:
  automountServiceAccountToken: true
  containers:
  - image: quay.io/cilium/hubble-ui:v0.13.3...
    imagePullPolicy: IfNotPresent
    livenessProbe:
      failureThreshold: 3
      httpGet:
        path: /healthz
        port: http
        scheme: HTTP
      periodSeconds: 10
      successThreshold: 1
      timeoutSeconds: 1
    name: frontend
    ports:
    - containerPort: 8081
      name: http
      protocol: TCP
    readinessProbe:
      failureThreshold: 3
      httpGet:
        path: /
        port: http
        scheme: HTTP
      periodSeconds: 10
      successThreshold: 1
      timeoutSeconds: 1
    resources: {}
    securityContext:
      allowPrivilegeEscalation: false
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: FallbackToLogsOnError
    volumeMounts:
    - mountPath: /etc/nginx/conf.d/default.conf
      name: hubble-ui-nginx-conf
      subPath: nginx.conf
    - mountPath: /tmp
      name: tmp-dir
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-n4p5b
      readOnly: true
  - env:
    - name: EVENTS_SERVER_PORT
      value: "8090"
    - name: FLOWS_API_ADDR
      value: hubble-relay:80
    image: quay.io/cilium/hubble-ui-backend:v0.13.3...
    imagePullPolicy: IfNotPresent
    name: backend
    ports:
    - containerPort: 8090
      name: grpc
      protocol: TCP
    resources: {}
    securityContext:
      allowPrivilegeEscalation: false
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: FallbackToLogsOnError
    volumeMounts:
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-n4p5b
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
    fsGroup: 1001
    runAsGroup: 1001
    runAsUser: 1001
  serviceAccount: hubble-ui
  serviceAccountName: hubble-ui
  terminationGracePeriodSeconds: 30
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
      name: hubble-ui-nginx
    name: hubble-ui-nginx-conf
  - emptyDir: {}
    name: tmp-dir
  - name: kube-api-access-n4p5b
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace
      - configMap:
          items:
          - key: service-ca.crt
            path: service-ca.crt
          name: openshift-service-ca.crt
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2026-06-29T10:06:23Z"
    status: "True"
    type: PodReadyToStartContainers
  - lastProbeTime: null
    lastTransitionTime: "2026-06-29T10:05:30Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2026-06-29T10:06:23Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2026-06-29T10:06:23Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2026-06-29T10:05:30Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: cri-o://4a722a5996c898c3a849f35596200ac13ea9bbbf2cc98e4ce1124c47cc82f83e
    image: quay.io/cilium/hubble-ui-backend...
    imageID: quay.io/cilium/hubble-ui-backend...
    lastState: {}
    name: backend
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2026-06-29T10:06:22Z"
    volumeMounts:
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-n4p5b
      readOnly: true
      recursiveReadOnly: Disabled
  - containerID: cri-o://857e4cf62450c78a183d310faebe9f2d7ddf752e6a72ea3d1b8001b59f0117e3
    image: quay.io/cilium/hubble-ui...
    imageID: quay.io/cilium/hubble-ui...
    lastState: {}
    name: frontend
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2026-06-29T10:05:58Z"
    volumeMounts:
    - mountPath: /etc/nginx/conf.d/default.conf
      name: hubble-ui-nginx-conf
    - mountPath: /tmp
      name: tmp-dir
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-n4p5b
      readOnly: true
      recursiveReadOnly: Disabled
  hostIP: 10.10.10.66
  hostIPs:
  - ip: 10.10.10.66
  phase: Running
  podIP: 10.128.4.140
  podIPs:
  - ip: 10.128.4.140
  qosClass: BestEffort
  startTime: "2026-06-29T10:05:30Z"
```

## Service

```
$ oc get service -n cilium 
NAME              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
hubble-ui         ClusterIP   172.30.59.28     <none>        80/TCP     11m
```

Serice listening on TCP/80 and exposing hubble-ui container frontend TCP/8081

```yaml
apiVersion: v1
kind: Service
metadata:
  annotations:
    meta.helm.sh/release-name: cilium-release
    meta.helm.sh/release-namespace: cilium
  creationTimestamp: "2026-06-29T10:05:30Z"
  labels:
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: hubble-ui
    app.kubernetes.io/part-of: cilium
    app.kubernetes.io/version: 1.19.0
    isovalent.io/managed-by: clife
    k8s-app: hubble-ui
  name: hubble-ui
  namespace: cilium
  ownerReferences:
  - apiVersion: cilium.io/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: CiliumConfig
    name: ciliumconfig
    uid: 23c5b57e-6fa3-429c-a86f-3e212122b307
  resourceVersion: "138408445"
  uid: 55a0be79-4b79-4243-8689-d802ae2bfc1f
spec:
  clusterIP: 172.30.59.28
  clusterIPs:
  - 172.30.59.28
  internalTrafficPolicy: Cluster
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 8081
  selector:
    k8s-app: hubble-ui
  sessionAffinity: None
  type: ClusterIP
status:
  loadBalancer: {}
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
Deployment             hubble-ui                Desired: 1, Ready: 1/1, Available: 1/1
Containers:            cilium                   Running: 3
                       cilium-envoy             Running: 3
                       cilium-operator          Running: 2
                       clustermesh-apiserver    
                       hubble-relay             Running: 1
                       hubble-ui                Running: 1
Cluster Pods:          172/172 managed by Cilium
```

[[Back]](../README.md)