## Hubble Relay without TLS

[[Back]](../README.md)

## Cilium configuration

```yaml
spec:
  hubble:
    enabled: true
    relay:
      enabled: true
    tls:
      enabled: false
```

## Cilium agent

```
time=2026-06-23T10:33:19.17128518Z level=info msg="  --diagnostics-export-file='/var/run/cilium/hubble/status.log'"
time=2026-06-23T10:33:19.171717937Z level=info msg="  --enable-hubble='true'"
time=2026-06-23T10:33:19.171722608Z level=info msg="  --enable-hubble-open-metrics='false'"
time=2026-06-23T10:33:19.172459878Z level=info msg="  --hubble-connectionlog-export-enabled='false'"
time=2026-06-23T10:33:19.172465442Z level=info msg="  --hubble-connectionlog-export-file-compress='false'"
time=2026-06-23T10:33:19.172470697Z level=info msg="  --hubble-connectionlog-export-file-max-backups='5'"
time=2026-06-23T10:33:19.172475886Z level=info msg="  --hubble-connectionlog-export-file-max-size-mb='10'"
time=2026-06-23T10:33:19.172481171Z level=info msg="  --hubble-connectionlog-export-file-path='/var/run/cilium/hubble/connectionlog.log'"
time=2026-06-23T10:33:19.172486919Z level=info msg="  --hubble-connectionlog-export-interval='10s'"
time=2026-06-23T10:33:19.172491802Z level=info msg="  --hubble-disable-tls='true'"
time=2026-06-23T10:33:19.172496503Z level=info msg="  --hubble-drop-events='false'"
time=2026-06-23T10:33:19.172501162Z level=info msg="  --hubble-drop-events-extended='false'"
time=2026-06-23T10:33:19.172506211Z level=info msg="  --hubble-drop-events-interval='2m0s'"
time=2026-06-23T10:33:19.172511091Z level=info msg="  --hubble-drop-events-rate-limit='1'"
time=2026-06-23T10:33:19.172528242Z level=info msg="  --hubble-drop-events-reasons='auth_required,policy_denied'"
time=2026-06-23T10:33:19.172539074Z level=info msg="  --hubble-dynamic-metrics-config-path=''"
time=2026-06-23T10:33:19.172544519Z level=info msg="  --hubble-event-buffer-capacity='4095'"
time=2026-06-23T10:33:19.172549329Z level=info msg="  --hubble-event-queue-size='0'"
time=2026-06-23T10:33:19.172561302Z level=info msg="  --hubble-export-aggregation=''"
time=2026-06-23T10:33:19.17256704Z level=info msg="  --hubble-export-aggregation-ignore-source-port='true'"
time=2026-06-23T10:33:19.172572397Z level=info msg="  --hubble-export-aggregation-interval='0s'"
time=2026-06-23T10:33:19.17257729Z level=info msg="  --hubble-export-aggregation-renew-ttl='true'"
time=2026-06-23T10:33:19.172587269Z level=info msg="  --hubble-export-aggregation-state-filter='new,error,closed'"
time=2026-06-23T10:33:19.172593404Z level=info msg="  --hubble-export-aggregation-ttl='30s'"
time=2026-06-23T10:33:19.172599521Z level=info msg="  --hubble-export-allowlist=''"
time=2026-06-23T10:33:19.172605384Z level=info msg="  --hubble-export-denylist=''"
time=2026-06-23T10:33:19.172616536Z level=info msg="  --hubble-export-fieldaggregate=''"
time=2026-06-23T10:33:19.17262862Z level=info msg="  --hubble-export-fieldmask=''"
time=2026-06-23T10:33:19.172633674Z level=info msg="  --hubble-export-file-compress='false'"
time=2026-06-23T10:33:19.172638662Z level=info msg="  --hubble-export-file-max-backups='5'"
time=2026-06-23T10:33:19.172643569Z level=info msg="  --hubble-export-file-max-size-mb='10'"
time=2026-06-23T10:33:19.172649887Z level=info msg="  --hubble-export-file-path=''"
time=2026-06-23T10:33:19.1726546Z level=info msg="  --hubble-export-file-rotation-interval='0s'"
time=2026-06-23T10:33:19.172659531Z level=info msg="  --hubble-export-format-version='v1'"
time=2026-06-23T10:33:19.172665132Z level=info msg="  --hubble-export-node-name=''"
time=2026-06-23T10:33:19.172670192Z level=info msg="  --hubble-export-rate-limit='-1'"
time=2026-06-23T10:33:19.172682298Z level=info msg="  --hubble-export-timescape-aggregation=''"
time=2026-06-23T10:33:19.17268821Z level=info msg="  --hubble-export-timescape-aggregation-ignore-source-port='true'"
time=2026-06-23T10:33:19.17269325Z level=info msg="  --hubble-export-timescape-aggregation-renew-ttl='true'"
time=2026-06-23T10:33:19.172702544Z level=info msg="  --hubble-export-timescape-aggregation-state-filter='new,error,closed'"
time=2026-06-23T10:33:19.172709884Z level=info msg="  --hubble-export-timescape-aggregation-ttl='30s'"
time=2026-06-23T10:33:19.172716107Z level=info msg="  --hubble-export-timescape-allowlist=''"
time=2026-06-23T10:33:19.172722187Z level=info msg="  --hubble-export-timescape-denylist=''"
time=2026-06-23T10:33:19.172727035Z level=info msg="  --hubble-export-timescape-enabled='false'"
time=2026-06-23T10:33:19.172738953Z level=info msg="  --hubble-export-timescape-fieldmask=''"
time=2026-06-23T10:33:19.172745182Z level=info msg="  --hubble-export-timescape-max-buffer-size='4096'"
time=2026-06-23T10:33:19.172751731Z level=info msg="  --hubble-export-timescape-node-name=''"
time=2026-06-23T10:33:19.172757237Z level=info msg="  --hubble-export-timescape-report-dropped-flows-interval='1m0s'"
time=2026-06-23T10:33:19.172762755Z level=info msg="  --hubble-export-timescape-target='hubble-timescape-export.hubble-timescape.svc.cluster.local:4261'"
time=2026-06-23T10:33:19.17277457Z level=info msg="  --hubble-export-timescape-tls-ca-files=''"
time=2026-06-23T10:33:19.172781475Z level=info msg="  --hubble-export-timescape-tls-cert-file=''"
time=2026-06-23T10:33:19.17278641Z level=info msg="  --hubble-export-timescape-tls-enabled='false'"
time=2026-06-23T10:33:19.172792818Z level=info msg="  --hubble-export-timescape-tls-key-file=''"
time=2026-06-23T10:33:19.172798002Z level=info msg="  --hubble-export-timescape-use-cilium-service-resolver='true'"
time=2026-06-23T10:33:19.172804671Z level=info msg="  --hubble-flowlogs-config-path=''"
time=2026-06-23T10:33:19.172809228Z level=info msg="  --hubble-listen-address=':4244'"
time=2026-06-23T10:33:19.172813987Z level=info msg="  --hubble-lost-event-send-interval='1s'"
time=2026-06-23T10:33:19.172819649Z level=info msg="  --hubble-metrics=''"
time=2026-06-23T10:33:19.172825534Z level=info msg="  --hubble-metrics-server=''"
time=2026-06-23T10:33:19.172830437Z level=info msg="  --hubble-metrics-server-enable-tls='false'"
time=2026-06-23T10:33:19.172836585Z level=info msg="  --hubble-metrics-server-tls-cert-file=''"
time=2026-06-23T10:33:19.172848618Z level=info msg="  --hubble-metrics-server-tls-client-ca-files=''"
time=2026-06-23T10:33:19.172856129Z level=info msg="  --hubble-metrics-server-tls-key-file=''"
time=2026-06-23T10:33:19.172866969Z level=info msg="  --hubble-monitor-events=''"
time=2026-06-23T10:33:19.172872644Z level=info msg="  --hubble-network-policy-correlation-enabled='true'"
time=2026-06-23T10:33:19.17287738Z level=info msg="  --hubble-prefer-ipv6='false'"
time=2026-06-23T10:33:19.17288196Z level=info msg="  --hubble-redact-enabled='false'"
time=2026-06-23T10:33:19.172893945Z level=info msg="  --hubble-redact-http-headers-allow=''"
time=2026-06-23T10:33:19.172905616Z level=info msg="  --hubble-redact-http-headers-deny=''"
time=2026-06-23T10:33:19.17291118Z level=info msg="  --hubble-redact-http-urlquery='false'"
time=2026-06-23T10:33:19.172916767Z level=info msg="  --hubble-redact-http-userinfo='true'"
time=2026-06-23T10:33:19.172921411Z level=info msg="  --hubble-redact-kafka-apikey='false'"
time=2026-06-23T10:33:19.172926254Z level=info msg="  --hubble-skip-unknown-cgroup-ids='true'"
time=2026-06-23T10:33:19.172930904Z level=info msg="  --hubble-socket-path='/var/run/cilium/hubble.sock'"
time=2026-06-23T10:33:19.172937437Z level=info msg="  --hubble-tls-cert-file=''"
time=2026-06-23T10:33:19.172953689Z level=info msg="  --hubble-tls-client-ca-files=''"
time=2026-06-23T10:33:19.172960552Z level=info msg="  --hubble-tls-key-file=''"
time=2026-06-23T10:33:19.496232372Z level=info msg="Certloader TLS watcher disabled" module=enterprise-agent.agent.controlplane.hubble config=certloader-server-tls
time=2026-06-23T10:33:19.496408023Z level=info msg="Hubble ConnectionLog exporter disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-connectionlog subsys=hubble-connectionlog
time=2026-06-23T10:33:19.496592041Z level=info msg="The Hubble static exporter is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-exporters
time=2026-06-23T10:33:19.496610135Z level=info msg="The Hubble dynamic exporter is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-exporters
time=2026-06-23T10:33:19.496854721Z level=info msg="Certloader TLS watcher disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter config=certloader-client-tls
time=2026-06-23T10:33:19.496891285Z level=info msg="The Hubble timescape exporter is disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter
time=2026-06-23T10:33:19.497121914Z level=info msg="The Hubble EE static exporter is disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter
time=2026-06-23T10:33:19.497147665Z level=info msg="The Hubble EE dynamic exporter is disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter
time=2026-06-23T10:33:19.497291362Z level=info msg="The Hubble packet drop events emitter is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-dropeventemitter
time=2026-06-23T10:33:19.49776047Z level=info msg="Certloader TLS watcher disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-metrics config=certloader-server-tls
time=2026-06-23T10:33:19.497989979Z level=info msg="The Hubble metrics server is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-metrics
time=2026-06-23T10:33:21.388502465Z level=info msg="Configuring Hubble server" module=enterprise-agent.agent.controlplane.hubble maxFlows=4095 eventQueueSize=16384
time=2026-06-23T10:33:21.389309822Z level=info msg="Starting local Hubble server" module=enterprise-agent.agent.controlplane.hubble address=unix:///var/run/cilium/hubble.sock
time=2026-06-23T10:33:21.389326963Z level=warn msg="Hubble server will be exposing its API insecurely on this address" module=enterprise-agent.agent.controlplane.hubble address=unix:///var/run/cilium/hubble.sock
time=2026-06-23T10:33:21.389401289Z level=info msg="Starting Hubble server" module=enterprise-agent.agent.controlplane.hubble address=:4244 tls=false
time=2026-06-23T10:33:21.570677615Z level=info msg="New endpoint" ipv4=10.128.0.176 ipv6="" k8sPodName=cilium/hubble-relay-fb86549f4-2tx2s endpointID=1693 ciliumEndpointName=cilium/hubble-relay-fb86549f4-2tx2s containerID=2a252684be datapathPolicyRevision=0 identity=11475 desiredPolicyRevision=0 containerInterface=eth0 subsys=endpoint
time=2026-06-23T10:33:21.571051232Z level=info msg="Create endpoint request" module=enterprise-agent.agent.controlplane.endpoint-api addressing="&{IPv4:10.128.0.253 IPv4ExpirationUUID:e91c8229-d78f-453f-bca2-e43905ce4dd2 IPv4PoolName:default IPv6: IPv6ExpirationUUID: IPv6PoolName:}" containerID=2e12a9b2a5468ef17b70d09a12f686777f5dc97ea367ff23a26d3913e9565de9 containerInterface=eth0 datapathConfiguration="&{DisableSipVerification:false ExternalIpam:false InstallEndpointRoute:false RequireArpPassthrough:false RequireEgressProg:false RequireRouting:<nil>}" interface=lxc35c7f6ebe6db k8sPodName=cilium/hubble-relay-648b467d76-87lp7 k8sUID=8686853f-d7d3-4856-b8f8-3cdc5ba039f2 labels=[] sync-build=true
time=2026-06-23T10:33:21.571490786Z level=info msg="New endpoint" containerID=2e12a9b2a5 desiredPolicyRevision=0 ipv4=10.128.0.253 k8sPodName=cilium/hubble-relay-648b467d76-87lp7 containerInterface="" ipv6="" ciliumEndpointName=cilium/hubble-relay-648b467d76-87lp7 endpointID=614 datapathPolicyRevision=0 subsys=endpoint
time=2026-06-23T10:33:21.57191465Z level=info msg="Resolving identity labels (blocking)" containerID=2e12a9b2a5 desiredPolicyRevision=0 ipv4=10.128.0.253 k8sPodName=cilium/hubble-relay-648b467d76-87lp7 containerInterface="" ipv6="" ciliumEndpointName=cilium/hubble-relay-648b467d76-87lp7 endpointID=614 datapathPolicyRevision=0 subsys=endpoint identityLabels="k8s:app.kubernetes.io/name=hubble-relay,k8s:app.kubernetes.io/part-of=cilium,k8s:io.cilium.k8s.namespace.labels.app.kubernetes.io/managed-by=kustomize,k8s:io.cilium.k8s.namespace.labels.app.kubernetes.io/name=clife,k8s:io.cilium.k8s.namespace.labels.control-plane=controller-manager,k8s:io.cilium.k8s.namespace.labels.kubernetes.io/metadata.name=cilium,k8s:io.cilium.k8s.namespace.labels.olm.operatorgroup.uid/84b4b2bd-0c3d-4a95-91f3-123d3b5b1407,k8s:io.cilium.k8s.namespace.labels.openshift.io/cluster-logging=true,k8s:io.cilium.k8s.namespace.labels.openshift.io/cluster-monitoring=true,k8s:io.cilium.k8s.namespace.labels.openshift.io/run-level=0,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/audit-version=latest,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/audit=privileged,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/warn-version=latest,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/warn=privileged,k8s:io.cilium.k8s.policy.cluster=default,k8s:io.cilium.k8s.policy.serviceaccount=hubble-relay,k8s:io.kubernetes.pod.namespace=cilium,k8s:k8s-app=hubble-relay"
time=2026-06-23T10:33:21.572128619Z level=info msg="Identity of endpoint changed" containerID=2e12a9b2a5 desiredPolicyRevision=0 ipv4=10.128.0.253 k8sPodName=cilium/hubble-relay-648b467d76-87lp7 containerInterface="" ipv6="" ciliumEndpointName=cilium/hubble-relay-648b467d76-87lp7 endpointID=614 datapathPolicyRevision=0 subsys=endpoint new-identity=11475 old-identity="no identity" identityLabels="k8s:app.kubernetes.io/name=hubble-relay,k8s:app.kubernetes.io/part-of=cilium,k8s:io.cilium.k8s.namespace.labels.app.kubernetes.io/managed-by=kustomize,k8s:io.cilium.k8s.namespace.labels.app.kubernetes.io/name=clife,k8s:io.cilium.k8s.namespace.labels.control-plane=controller-manager,k8s:io.cilium.k8s.namespace.labels.kubernetes.io/metadata.name=cilium,k8s:io.cilium.k8s.namespace.labels.olm.operatorgroup.uid/84b4b2bd-0c3d-4a95-91f3-123d3b5b1407,k8s:io.cilium.k8s.namespace.labels.openshift.io/cluster-logging=true,k8s:io.cilium.k8s.namespace.labels.openshift.io/cluster-monitoring=true,k8s:io.cilium.k8s.namespace.labels.openshift.io/run-level=0,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/audit-version=latest,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/audit=privileged,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/warn-version=latest,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/warn=privileged,k8s:io.cilium.k8s.policy.cluster=default,k8s:io.cilium.k8s.policy.serviceaccount=hubble-relay,k8s:io.kubernetes.pod.namespace=cilium,k8s:k8s-app=hubble-relay"
time=2026-06-23T10:33:21.572244Z level=info msg="Waiting for endpoint to be generated" containerID=2e12a9b2a5 desiredPolicyRevision=0 ipv4=10.128.0.253 k8sPodName=cilium/hubble-relay-648b467d76-87lp7 containerInterface="" ipv6="" ciliumEndpointName=cilium/hubble-relay-648b467d76-87lp7 endpointID=614 datapathPolicyRevision=0 identity=11475 subsys=endpoint
time=2026-06-23T10:33:21.847175474Z level=info msg="Delete endpoint by containerID request" module=enterprise-agent.agent.controlplane.endpoint-api containerID=2a252684befbe94c0f29127e4c5fa97e2d2b364f6e910659ffdf2ae2e02a92a7 endpointID=1693 k8sPodName=hubble-relay-fb86549f4-2tx2s k8sNamespace=cilium
time=2026-06-23T10:33:22.971108159Z level=info msg="Removed endpoint" ipv4=10.128.0.176 ipv6="" k8sPodName=cilium/hubble-relay-fb86549f4-2tx2s endpointID=1693 ciliumEndpointName=cilium/hubble-relay-fb86549f4-2tx2s containerID=2a252684be datapathPolicyRevision=0 identity=11475 desiredPolicyRevision=0 containerInterface=eth0 subsys=endpoint
time=2026-06-23T10:33:27.946972408Z level=info msg="Reloaded endpoint BPF program" containerID=2e12a9b2a5 desiredPolicyRevision=2 ipv4=10.128.0.253 k8sPodName=cilium/hubble-relay-648b467d76-87lp7 containerInterface="" ipv6="" ciliumEndpointName=cilium/hubble-relay-648b467d76-87lp7 endpointID=614 datapathPolicyRevision=0 identity=11475 subsys=endpoint
time=2026-06-23T10:33:27.947440177Z level=info msg="Successful endpoint creation" containerID=2e12a9b2a5 desiredPolicyRevision=2 ipv4=10.128.0.253 k8sPodName=cilium/hubble-relay-648b467d76-87lp7 containerInterface="" ipv6="" ciliumEndpointName=cilium/hubble-relay-648b467d76-87lp7 endpointID=614 datapathPolicyRevision=2 identity=11475 subsys=endpoint-api
time=2026-06-23T10:33:28.112490602Z level=info msg="Reloaded endpoint BPF program" containerID=2e12a9b2a5 desiredPolicyRevision=2 ipv4=10.128.0.253 k8sPodName=cilium/hubble-relay-648b467d76-87lp7 containerInterface="" ipv6="" ciliumEndpointName=cilium/hubble-relay-648b467d76-87lp7 endpointID=614 datapathPolicyRevision=2 identity=11475 subsys=endpoint
```

## Config map

```
$ oc get configmaps -n cilium cilium-config -o yaml | grep -i hubble
  diagnostics-export-file: /var/run/cilium/hubble/status.log
  enable-hubble: "true"
  hubble-connectionlog-export-enabled: "false"
  hubble-disable-tls: "true"
  hubble-listen-address: :4244
  hubble-network-policy-correlation-enabled: "true"
  hubble-socket-path: /var/run/cilium/hubble.sock
```

## Hubble Relay

```
$ oc get deployment -n cilium
NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
hubble-relay               1/1     1            1           85m

$ oc get pod -n cilium
NAME                                        READY   STATUS    RESTARTS        AGE
hubble-relay-648b467d76-87lp7               1/1     Running   0               82m
```

```yaml
$ oc get pod -n cilium hubble-relay-648b467d76-87lp7 -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "portmap",
          "interface": "eth0",
          "ips": [
              "10.128.0.253"
          ],
          "mac": "32:40:55:7f:ed:96",
          "default": true,
          "dns": {},
          "gateway": [
              "10.128.1.92"
          ]
      }]
  creationTimestamp: "2026-06-23T10:33:12Z"
  generateName: hubble-relay-648b467d76-
  labels:
    app.kubernetes.io/name: hubble-relay
    app.kubernetes.io/part-of: cilium
    k8s-app: hubble-relay
    pod-template-hash: 648b467d76
  name: hubble-relay-648b467d76-87lp7
  namespace: cilium
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: ReplicaSet
    name: hubble-relay-648b467d76
    uid: 0dcf8438-f3c6-49a1-ae02-6aa0ae13be66
  resourceVersion: "133709764"
  uid: 8686853f-d7d3-4856-b8f8-3cdc5ba039f2
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
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  nodeName: bm1-3
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
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2026-06-23T10:33:28Z"
    status: "True"
    type: PodReadyToStartContainers
  - lastProbeTime: null
    lastTransitionTime: "2026-06-23T10:33:12Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2026-06-23T10:33:39Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2026-06-23T10:33:39Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2026-06-23T10:33:12Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: cri-o://ca7ca8f83dd8c52665505c55b67983a7d735660be7206c26b8d9ab48cc25c5bc
    image: quay.io/isovalent-dev/hubble-relay-ubi-ci...
    imageID: quay.io/isovalent-dev/hubble-relay-ubi-ci...
    lastState: {}
    name: hubble-relay
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2026-06-23T10:33:28Z"
    volumeMounts:
    - mountPath: /etc/hubble-relay
      name: config
      readOnly: true
      recursiveReadOnly: Disabled
  hostIP: 10.10.10.67
  hostIPs:
  - ip: 10.10.10.67
  phase: Running
  podIP: 10.128.0.253
  podIPs:
  - ip: 10.128.0.253
  qosClass: BestEffort
  startTime: "2026-06-23T10:33:12Z"
```

```
$ kubectl logs -n cilium hubble-relay-648b467d76-87lp7 
time=2026-06-23T10:33:28.311576815Z level=info msg="Starting gRPC health server..." subsys=hubble-relay address=:4222
time=2026-06-23T10:33:28.311629316Z level=info msg="Starting gRPC server..." subsys=hubble-relay options="{peerTarget:hubble-peer.cilium.svc.cluster.local.:80 retryTimeout:30000000000 listenAddress::4245 healthListenAddress::4222 metricsListenAddress: log:0xc0003cd370 serverTLSConfig:<nil> insecureServer:true clientTLSConfig:<nil> clusterName:default insecureClient:true observerOptions:[0x22d8840 0x22d8920] grpcMetrics:<nil> grpcUnaryInterceptors:[0x2390280] grpcStreamInterceptors:[0x2390340]}"
time=2026-06-23T10:33:28.314549843Z level=info msg="Received peer change notification" subsys=hubble-relay changeNotification="name:\"bm1-3\"  address:\"10.10.10.67:4244\"  type:PEER_ADDED"
time=2026-06-23T10:33:28.314621009Z level=info msg="Received peer change notification" subsys=hubble-relay changeNotification="name:\"bm1-1\"  address:\"10.10.10.65:4244\"  type:PEER_ADDED"
time=2026-06-23T10:33:28.314636772Z level=info msg="Received peer change notification" subsys=hubble-relay changeNotification="name:\"bm1-2\"  address:\"10.10.10.66:4244\"  type:PEER_ADDED"
time=2026-06-23T10:33:28.314706184Z level=info msg=Connecting subsys=hubble-relay address=10.10.10.66:4244 tls=false peer=bm1-2
time=2026-06-23T10:33:28.314718635Z level=info msg=Connecting subsys=hubble-relay address=10.10.10.67:4244 tls=false peer=bm1-3
time=2026-06-23T10:33:28.314724954Z level=info msg=Connecting subsys=hubble-relay address=10.10.10.65:4244 tls=false peer=bm1-1
time=2026-06-23T10:33:28.31476753Z level=info msg=Connected subsys=hubble-relay address=10.10.10.66:4244 tls=false peer=bm1-2
time=2026-06-23T10:33:28.314780948Z level=info msg=Connected subsys=hubble-relay address=10.10.10.67:4244 tls=false peer=bm1-3
time=2026-06-23T10:33:28.31478364Z level=info msg=Connected subsys=hubble-relay address=10.10.10.65:4244 tls=false peer=bm1-1
```

## Service

```
$ oc get service -n cilium
NAME              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
hubble-peer       ClusterIP   172.30.77.238    <none>        443/TCP    245d
hubble-relay      ClusterIP   172.30.139.127   <none>        80/TCP     86m
```

```yaml
$ oc get service -n cilium hubble-peer -o yaml
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
  resourceVersion: "133679729"
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

```
$ oc get ep -n cilium
NAME              ENDPOINTS                                            AGE
hubble-peer       10.10.10.65:4244,10.10.10.66:4244,10.10.10.67:4244   52s
hubble-relay      10.128.0.253:4245                                    52s
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
Cluster Pods:          167/167 managed by Cilium
```

## Listening ports

```
$ netstat -na | grep LISTEN
tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:9964            0.0.0.0:*               LISTEN     
tcp        0      0 10.10.10.65:45521       0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:36309         0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:34245           0.0.0.0:*               LISTEN     
tcp        0      0 10.10.10.65:10250       0.0.0.0:*               LISTEN     
tcp        0      0 10.10.10.65:9100        0.0.0.0:*               LISTEN     
tcp        0      0 10.10.10.65:9940        0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:9977          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:9891          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:9890          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:9879          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:9878          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:9743          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:9537          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:9234          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:9100          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:8798          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:8797          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:10248         0.0.0.0:*               LISTEN     
tcp6       0      0 :::2380                 :::*                    LISTEN     
tcp6       0      0 :::2379                 :::*                    LISTEN     
tcp6       0      0 :::111                  :::*                    LISTEN     
tcp6       0      0 :::22                   :::*                    LISTEN     
tcp6       0      0 :::53                   :::*                    LISTEN     
tcp6       0      0 :::8089                 :::*                    LISTEN     
tcp6       0      0 :::6385                 :::*                    LISTEN     
tcp6       0      0 :::6443                 :::*                    LISTEN     
tcp6       0      0 :::6080                 :::*                    LISTEN     
tcp6       0      0 :::4244                 :::*                    LISTEN     
tcp6       0      0 :::10357                :::*                    LISTEN     
tcp6       0      0 :::10255                :::*                    LISTEN     
tcp6       0      0 :::10259                :::*                    LISTEN     
tcp6       0      0 :::10257                :::*                    LISTEN     
tcp6       0      0 :::9445                 :::*                    LISTEN     
tcp6       0      0 :::9444                 :::*                    LISTEN     
tcp6       0      0 :::9637                 :::*                    LISTEN     
tcp6       0      0 :::9963                 :::*                    LISTEN     
tcp6       0      0 :::9962                 :::*                    LISTEN     
tcp6       0      0 :::9980                 :::*                    LISTEN     
tcp6       0      0 :::9979                 :::*                    LISTEN     
tcp6       0      0 :::9978                 :::*                    LISTEN     
tcp6       0      0 :::9102                 :::*                    LISTEN     
tcp6       0      0 :::9001                 :::*                    LISTEN     
tcp6       0      0 :::18443                :::*                    LISTEN     
tcp6       0      0 :::17697                :::*                    LISTEN     
tcp6       0      0 :::18080                :::*                    LISTEN     
tcp6       0      0 :::22623                :::*                    LISTEN     
tcp6       0      0 :::22624                :::*                    LISTEN     
tcp6       0      0 :::29102                :::*                    LISTEN     
tcp6       0      0 :::49081                :::*                    LISTEN     
tcp6       0      0 ::1:29445               :::*                    LISTEN     
tcp6       0      0 :::51971                :::*                    LISTEN 
```

[[Back]](../README.md)