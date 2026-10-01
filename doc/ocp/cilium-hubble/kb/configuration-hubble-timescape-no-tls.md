## Integrated Hubble Timescape without TLS

[[Back]](../README.md)

## Cilium configuration

```yaml
spec:
  enterprise:
    featureGate:
      approved:
      - HubbleTimescape
  hubble:
    enabled: true
    timescape:
      enabled: true
    tls:
      enabled: false
```

## Cilium agent

```
time=2026-06-29T20:19:15.086382046Z level=info msg="  --diagnostics-export-file='/var/run/cilium/hubble/status.log'"
time=2026-06-29T20:19:15.08679593Z level=info msg="  --enable-hubble='true'"
time=2026-06-29T20:19:15.086800544Z level=info msg="  --enable-hubble-open-metrics='false'"
time=2026-06-29T20:19:15.087485438Z level=info msg="  --feature-gates-approved='CNIChainingMode,ClusterMeshKVStoreMesh,BFD,BGPControlPlane,BGPRouteImport,CNIChainingMode,ClusterMesh,EVPN,EnterpriseBGPControlPlane,MultiNetwork,VTEPIntegration,PrivateNetworks,HubbleTimescape'"
time=2026-06-29T20:19:15.087581133Z level=info msg="  --hubble-connectionlog-export-enabled='false'"
time=2026-06-29T20:19:15.087586163Z level=info msg="  --hubble-connectionlog-export-file-compress='false'"
time=2026-06-29T20:19:15.087591398Z level=info msg="  --hubble-connectionlog-export-file-max-backups='5'"
time=2026-06-29T20:19:15.087596879Z level=info msg="  --hubble-connectionlog-export-file-max-size-mb='10'"
time=2026-06-29T20:19:15.087602644Z level=info msg="  --hubble-connectionlog-export-file-path='/var/run/cilium/hubble/connectionlog.log'"
time=2026-06-29T20:19:15.087608299Z level=info msg="  --hubble-connectionlog-export-interval='10s'"
time=2026-06-29T20:19:15.087613017Z level=info msg="  --hubble-disable-tls='true'"
time=2026-06-29T20:19:15.087617686Z level=info msg="  --hubble-drop-events='false'"
time=2026-06-29T20:19:15.087623489Z level=info msg="  --hubble-drop-events-extended='false'"
time=2026-06-29T20:19:15.087628476Z level=info msg="  --hubble-drop-events-interval='2m0s'"
time=2026-06-29T20:19:15.087633497Z level=info msg="  --hubble-drop-events-rate-limit='1'"
time=2026-06-29T20:19:15.087644185Z level=info msg="  --hubble-drop-events-reasons='auth_required,policy_denied'"
time=2026-06-29T20:19:15.087651702Z level=info msg="  --hubble-dynamic-metrics-config-path=''"
time=2026-06-29T20:19:15.087657443Z level=info msg="  --hubble-event-buffer-capacity='4095'"
time=2026-06-29T20:19:15.087662628Z level=info msg="  --hubble-event-queue-size='0'"
time=2026-06-29T20:19:15.087676342Z level=info msg="  --hubble-export-aggregation=''"
time=2026-06-29T20:19:15.087682453Z level=info msg="  --hubble-export-aggregation-ignore-source-port='true'"
time=2026-06-29T20:19:15.087688376Z level=info msg="  --hubble-export-aggregation-interval='0s'"
time=2026-06-29T20:19:15.087693227Z level=info msg="  --hubble-export-aggregation-renew-ttl='true'"
time=2026-06-29T20:19:15.087703686Z level=info msg="  --hubble-export-aggregation-state-filter='new,error,closed'"
time=2026-06-29T20:19:15.087709557Z level=info msg="  --hubble-export-aggregation-ttl='30s'"
time=2026-06-29T20:19:15.087715892Z level=info msg="  --hubble-export-allowlist=''"
time=2026-06-29T20:19:15.087722114Z level=info msg="  --hubble-export-denylist=''"
time=2026-06-29T20:19:15.087736232Z level=info msg="  --hubble-export-fieldaggregate=''"
time=2026-06-29T20:19:15.087750009Z level=info msg="  --hubble-export-fieldmask=''"
time=2026-06-29T20:19:15.087755677Z level=info msg="  --hubble-export-file-compress='false'"
time=2026-06-29T20:19:15.087760769Z level=info msg="  --hubble-export-file-max-backups='5'"
time=2026-06-29T20:19:15.08776612Z level=info msg="  --hubble-export-file-max-size-mb='10'"
time=2026-06-29T20:19:15.087772842Z level=info msg="  --hubble-export-file-path=''"
time=2026-06-29T20:19:15.087777861Z level=info msg="  --hubble-export-file-rotation-interval='0s'"
time=2026-06-29T20:19:15.087782896Z level=info msg="  --hubble-export-format-version='v1'"
time=2026-06-29T20:19:15.087789308Z level=info msg="  --hubble-export-node-name=''"
time=2026-06-29T20:19:15.087794224Z level=info msg="  --hubble-export-rate-limit='-1'"
time=2026-06-29T20:19:15.087799091Z level=info msg="  --hubble-export-timescape-aggregation='connection'"
time=2026-06-29T20:19:15.087804414Z level=info msg="  --hubble-export-timescape-aggregation-ignore-source-port='true'"
time=2026-06-29T20:19:15.087809287Z level=info msg="  --hubble-export-timescape-aggregation-renew-ttl='false'"
time=2026-06-29T20:19:15.087814728Z level=info msg="  --hubble-export-timescape-aggregation-state-filter='new,error'"
time=2026-06-29T20:19:15.087820437Z level=info msg="  --hubble-export-timescape-aggregation-ttl='30s'"
time=2026-06-29T20:19:15.087826717Z level=info msg="  --hubble-export-timescape-allowlist=''"
time=2026-06-29T20:19:15.087832989Z level=info msg="  --hubble-export-timescape-denylist=''"
time=2026-06-29T20:19:15.08783798Z level=info msg="  --hubble-export-timescape-enabled='true'"
time=2026-06-29T20:19:15.087852485Z level=info msg="  --hubble-export-timescape-fieldmask=''"
time=2026-06-29T20:19:15.08785871Z level=info msg="  --hubble-export-timescape-max-buffer-size='4096'"
time=2026-06-29T20:19:15.087865716Z level=info msg="  --hubble-export-timescape-node-name=''"
time=2026-06-29T20:19:15.087870716Z level=info msg="  --hubble-export-timescape-report-dropped-flows-interval='1m0s'"
time=2026-06-29T20:19:15.087875788Z level=info msg="  --hubble-export-timescape-target='hubble-timescape.cilium.svc.cluster.local:4261'"
time=2026-06-29T20:19:15.087890084Z level=info msg="  --hubble-export-timescape-tls-ca-files=''"
time=2026-06-29T20:19:15.087897781Z level=info msg="  --hubble-export-timescape-tls-cert-file=''"
time=2026-06-29T20:19:15.087902831Z level=info msg="  --hubble-export-timescape-tls-enabled='false'"
time=2026-06-29T20:19:15.087909029Z level=info msg="  --hubble-export-timescape-tls-key-file=''"
time=2026-06-29T20:19:15.087913983Z level=info msg="  --hubble-export-timescape-use-cilium-service-resolver='true'"
time=2026-06-29T20:19:15.08792042Z level=info msg="  --hubble-flowlogs-config-path=''"
time=2026-06-29T20:19:15.087940188Z level=info msg="  --hubble-listen-address=':4244'"
time=2026-06-29T20:19:15.087946185Z level=info msg="  --hubble-lost-event-send-interval='1s'"
time=2026-06-29T20:19:15.087952297Z level=info msg="  --hubble-metrics=''"
time=2026-06-29T20:19:15.087958352Z level=info msg="  --hubble-metrics-server=''"
time=2026-06-29T20:19:15.087963205Z level=info msg="  --hubble-metrics-server-enable-tls='false'"
time=2026-06-29T20:19:15.087969889Z level=info msg="  --hubble-metrics-server-tls-cert-file=''"
time=2026-06-29T20:19:15.087984158Z level=info msg="  --hubble-metrics-server-tls-client-ca-files=''"
time=2026-06-29T20:19:15.087991165Z level=info msg="  --hubble-metrics-server-tls-key-file=''"
time=2026-06-29T20:19:15.088003837Z level=info msg="  --hubble-monitor-events=''"
time=2026-06-29T20:19:15.088009643Z level=info msg="  --hubble-network-policy-correlation-enabled='true'"
time=2026-06-29T20:19:15.088014583Z level=info msg="  --hubble-prefer-ipv6='false'"
time=2026-06-29T20:19:15.08801927Z level=info msg="  --hubble-redact-enabled='false'"
time=2026-06-29T20:19:15.088034019Z level=info msg="  --hubble-redact-http-headers-allow=''"
time=2026-06-29T20:19:15.088048258Z level=info msg="  --hubble-redact-http-headers-deny=''"
time=2026-06-29T20:19:15.088054089Z level=info msg="  --hubble-redact-http-urlquery='false'"
time=2026-06-29T20:19:15.088058989Z level=info msg="  --hubble-redact-http-userinfo='true'"
time=2026-06-29T20:19:15.088063982Z level=info msg="  --hubble-redact-kafka-apikey='false'"
time=2026-06-29T20:19:15.08806881Z level=info msg="  --hubble-skip-unknown-cgroup-ids='true'"
time=2026-06-29T20:19:15.088073733Z level=info msg="  --hubble-socket-path='/var/run/cilium/hubble.sock'"
time=2026-06-29T20:19:15.088080034Z level=info msg="  --hubble-tls-cert-file=''"
time=2026-06-29T20:19:15.088093027Z level=info msg="  --hubble-tls-client-ca-files=''"
time=2026-06-29T20:19:15.08809962Z level=info msg="  --hubble-tls-key-file=''"
time=2026-06-29T20:19:15.451653375Z level=info msg="Certloader TLS watcher disabled" module=enterprise-agent.agent.controlplane.hubble config=certloader-server-tls
time=2026-06-29T20:19:15.451812638Z level=info msg="Hubble ConnectionLog exporter disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-connectionlog subsys=hubble-connectionlog
time=2026-06-29T20:19:15.451997644Z level=info msg="The Hubble static exporter is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-exporters
time=2026-06-29T20:19:15.452016626Z level=info msg="The Hubble dynamic exporter is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-exporters
time=2026-06-29T20:19:15.452270261Z level=info msg="Certloader TLS watcher disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter config=certloader-client-tls
time=2026-06-29T20:19:15.452521037Z level=info msg="The Hubble EE static exporter is disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter
time=2026-06-29T20:19:15.452546152Z level=info msg="The Hubble EE dynamic exporter is disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter
time=2026-06-29T20:19:15.452691819Z level=info msg="The Hubble packet drop events emitter is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-dropeventemitter
time=2026-06-29T20:19:15.453177002Z level=info msg="Certloader TLS watcher disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-metrics config=certloader-server-tls
time=2026-06-29T20:19:15.453403037Z level=info msg="Building the Hubble timescape exporter" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter config="{Enabled:true Target:hubble-timescape.cilium.svc.cluster.local:4261 Allowlist: Denylist: Fieldmask:[] NodeName: Aggregations:[connection] AggregationIgnoreSourcePort:true AggregationRenewTTL:false AggregationStateChangeFilter:[new error] AggregationTTL:30s MaxBufferSize:4096 ReportDroppedFlowsInterval:1m0s UseCiliumServiceResolver:true TLSEnabled:false TLSCertFile: TLSKeyFile: TLSCAFiles:[]}"
time=2026-06-29T20:19:15.453467324Z level=info msg="The Hubble metrics server is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-metrics
time=2026-06-29T20:19:16.410087844Z level=info msg="start streaming flow logs" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter subsys=hubble-timescape-exporter target=hubble-timescape.cilium.svc.cluster.local:4261
time=2026-06-29T20:19:16.411047985Z level=info msg="Configuring Hubble server" module=enterprise-agent.agent.controlplane.hubble maxFlows=4095 eventQueueSize=16384
time=2026-06-29T20:19:16.412026753Z level=info msg="Starting local Hubble server" module=enterprise-agent.agent.controlplane.hubble address=unix:///var/run/cilium/hubble.sock
time=2026-06-29T20:19:16.412048194Z level=warn msg="Hubble server will be exposing its API insecurely on this address" module=enterprise-agent.agent.controlplane.hubble address=unix:///var/run/cilium/hubble.sock
time=2026-06-29T20:19:16.41214332Z level=info msg="Starting Hubble server" module=enterprise-agent.agent.controlplane.hubble address=:4244 tls=false
time=2026-06-29T20:19:16.530670209Z level=info msg="New endpoint" ipv4=10.128.5.186 identity=25064 datapathPolicyRevision=0 k8sPodName=cilium/hubble-cli-7b54bf5dcc-hzf8t containerID=04010ec133 endpointID=2606 containerInterface=eth0 desiredPolicyRevision=0 ciliumEndpointName=cilium/hubble-cli-7b54bf5dcc-hzf8t ipv6="" subsys=endpoint
time=2026-06-29T20:19:23.361292592Z level=info msg="Reloaded endpoint BPF program" ipv4=10.128.5.186 identity=25064 datapathPolicyRevision=0 k8sPodName=cilium/hubble-cli-7b54bf5dcc-hzf8t containerID=04010ec133 endpointID=2606 containerInterface=eth0 desiredPolicyRevision=2 ciliumEndpointName=cilium/hubble-cli-7b54bf5dcc-hzf8t ipv6="" subsys=endpoint
time=2026-06-29T20:19:23.361749475Z level=info msg="Restored endpoint" ipv4=10.128.5.186 identity=25064 datapathPolicyRevision=2 k8sPodName=cilium/hubble-cli-7b54bf5dcc-hzf8t containerID=04010ec133 endpointID=2606 containerInterface=eth0 desiredPolicyRevision=2 ciliumEndpointName=cilium/hubble-cli-7b54bf5dcc-hzf8t ipv6="" subsys=endpoint ipAddrs="[ipv4 10.128.5.186 ipv6 ]"
```

## Config map

```
$ oc get configmaps -n cilium cilium-config -o yaml | grep -i hubble
  diagnostics-export-file: /var/run/cilium/hubble/status.log
  enable-hubble: "true"
  feature-gates-approved: CNIChainingMode,ClusterMeshKVStoreMesh,BFD,BGPControlPlane,BGPRouteImport,CNIChainingMode,ClusterMesh,EVPN,EnterpriseBGPControlPlane,MultiNetwork,VTEPIntegration,PrivateNetworks,HubbleTimescape
  hubble-connectionlog-export-enabled: "false"
  hubble-disable-tls: "true"
  hubble-export-timescape-aggregation: connection
  hubble-export-timescape-aggregation-renew-ttl: "false"
  hubble-export-timescape-aggregation-state-filter: new error
  hubble-export-timescape-enabled: "true"
  hubble-export-timescape-target: hubble-timescape.cilium.svc.cluster.local:4261
  hubble-export-timescape-use-cilium-service-resolver: "true"
  hubble-listen-address: :4244
  hubble-network-policy-correlation-enabled: "true"
  hubble-socket-path: /var/run/cilium/hubble.sock
```

## Hubble Timescape

```
$ oc get pod -n cilium
NAME                    READY   STATUS    RESTARTS       AGE
hubble-timescape-0      2/2     Running   0              24h
```

```
$ oc get service -n cilium hubble-timescape
NAME               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                                               AGE
hubble-timescape   ClusterIP   172.30.199.148   <none>        4260/TCP,4261/TCP,80/TCP,8080/TCP,9090/TCP,8001/TCP   24h
```

Containers
- clickhouse: built-in database that keeps the last few hours of historical flow information
- timescape: main application with built-in ui

Container | Name | Port | Service | Description
--- | --- | --- | --- | ---
clickhouse | ch-port | tcp/8081 | --- | ---
clickhouse | ch-metrics | tcp/8001 | hubble-timescape tcp/8001 | In this setup metrics are disabled so probably not used
timescape | health-grpc | tcp/8083 | --- | ---
timescape | server-grpc | tcp/4244 | hubble-timescape tcp/80 | [Hubble CLI](./hubble-cli.md)
timescape | push | tcp/4260 | hubble-timescape tcp/4260 | [Push API](./timescape-push-api.md)
timescape | stream | tcp/4261 | hubble-timescape tcp/4261 | [Stream API](./timescape-stream-api.md)
timescape | ui | tcp/8000 | hubble-timescape tcp/8080 | [Web interface](./timescape-ui.md)
timescape | metrics | tcp/9090 | hubble-timescape tcp/9090 | In this setup metrics are disabled so probably not used
timescape | pprof | tcp/6060 | --- | ---

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
              "10.128.1.137"
          ],
          "mac": "8a:32:df:51:5f:31",
          "default": true,
          "dns": {},
          "gateway": [
              "10.128.1.92"
          ]
      }]
  creationTimestamp: "2026-06-29T12:19:02Z"
  generateName: hubble-timescape-
  labels:
    app.kubernetes.io/name: hubble-timescape
    app.kubernetes.io/part-of: cilium
    apps.kubernetes.io/pod-index: "0"
    controller-revision-hash: hubble-timescape-66c9bd6ffb
    k8s-app: hubble-timescape
    statefulset.kubernetes.io/pod-name: hubble-timescape-0
  name: hubble-timescape-0
  namespace: cilium
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: StatefulSet
    name: hubble-timescape
    uid: c7687927-5e61-48d4-bbc1-8f4f410899f7
  resourceVersion: "138481882"
  uid: ac7bad0a-c441-4ea0-9045-f41716ea0ebc
spec:
  containers:
  - image: quay.io/isovalent/clickhouse-server:25.8.11.66-alpine...
    imagePullPolicy: Always
    livenessProbe:
      failureThreshold: 3
      httpGet:
        path: /ping
        port: ch-http
        scheme: HTTP
      initialDelaySeconds: 60
      periodSeconds: 3
      successThreshold: 1
      timeoutSeconds: 1
    name: clickhouse
    ports:
    - containerPort: 8123
      name: ch-http
      protocol: TCP
    - containerPort: 8001
      name: ch-metrics
      protocol: TCP
    readinessProbe:
      failureThreshold: 3
      httpGet:
        path: /ping
        port: ch-http
        scheme: HTTP
      periodSeconds: 10
      successThreshold: 1
      timeoutSeconds: 1
    resources: {}
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
        - ALL
      privileged: false
      runAsGroup: 101
      runAsNonRoot: true
      runAsUser: 101
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: FallbackToLogsOnError
    volumeMounts:
    - mountPath: /etc/clickhouse-server/config.d/
      name: clickhouse-config
      readOnly: true
    - mountPath: /etc/clickhouse-server/profiles.d/
      name: clickhouse-profile
      readOnly: true
    - mountPath: /etc/clickhouse-server/users.d/
      name: clickhouse-user
      readOnly: true
    - mountPath: /var/lib/clickhouse
      name: clickhouse-data
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-79rg9
      readOnly: true
  - args:
    - run
    command:
    - /usr/bin/hubble-timescape
    env:
    - name: HUBBLE_TIMESCAPE_DSN
      value: clickhouse://localhost:9000/hubble?dial_timeout=10s
    image: quay.io/isovalent/hubble-timescape-lite:v1.18.6...
    imagePullPolicy: Always
    livenessProbe:
      failureThreshold: 3
      grpc:
        port: 8083
        service: ""
      periodSeconds: 10
      successThreshold: 1
      timeoutSeconds: 1
    name: timescape
    ports:
    - containerPort: 8083
      name: health-grpc
      protocol: TCP
    - containerPort: 4244
      name: server-grpc
      protocol: TCP
    - containerPort: 4260
      name: push
      protocol: TCP
    - containerPort: 4261
      name: stream
      protocol: TCP
    - containerPort: 8000
      name: ui
      protocol: TCP
    - containerPort: 9090
      name: metrics
      protocol: TCP
    - containerPort: 6060
      name: pprof
      protocol: TCP
    readinessProbe:
      failureThreshold: 3
      grpc:
        port: 8083
        service: ""
      periodSeconds: 10
      successThreshold: 1
      timeoutSeconds: 1
    resources: {}
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
        - ALL
      privileged: false
      runAsGroup: 65532
      runAsNonRoot: true
      runAsUser: 65532
    startupProbe:
      failureThreshold: 32
      grpc:
        port: 8083
        service: ""
      periodSeconds: 10
      successThreshold: 1
      timeoutSeconds: 1
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: FallbackToLogsOnError
    volumeMounts:
    - mountPath: /etc/hubble-timescape
      name: config
      readOnly: true
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-79rg9
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  hostname: hubble-timescape-0
  nodeName: bm1-3
  nodeSelector:
    kubernetes.io/os: linux
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  restartPolicy: Always
  schedulerName: default-scheduler
  securityContext:
    fsGroup: 65532
  serviceAccount: hubble-timescape
  serviceAccountName: hubble-timescape
  subdomain: timescape
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
      items:
      - key: config.yaml
        path: config.yaml
      name: hubble-timescape-config
    name: config
  - configMap:
      defaultMode: 420
      items:
      - key: clickhouse-settings.xml
        path: clickhouse-settings.xml
      name: hubble-timescape-clickhouse-settings
    name: clickhouse-config
  - configMap:
      defaultMode: 420
      items:
      - key: clickhouse-profiles.xml
        path: clickhouse-profiles.xml
      name: hubble-timescape-clickhouse-settings
    name: clickhouse-profile
  - configMap:
      defaultMode: 420
      items:
      - key: clickhouse-users.xml
        path: clickhouse-user.xml
      name: hubble-timescape-clickhouse-settings
    name: clickhouse-user
  - emptyDir:
      sizeLimit: 5Gi
    name: clickhouse-data
  - name: kube-api-access-79rg9
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
    lastTransitionTime: "2026-06-29T12:19:08Z"
    status: "True"
    type: PodReadyToStartContainers
  - lastProbeTime: null
    lastTransitionTime: "2026-06-29T12:19:02Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2026-06-29T12:19:13Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2026-06-29T12:19:13Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2026-06-29T12:19:02Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: cri-o://22d5edcf38259d5c38a71606a5c97b806ba3c158d9f9a0a99342769d7f8bafdb
    image: quay.io/isovalent/clickhouse-server...
    imageID: quay.io/isovalent/clickhouse-server...
    lastState: {}
    name: clickhouse
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2026-06-29T12:19:05Z"
    volumeMounts:
    - mountPath: /etc/clickhouse-server/config.d/
      name: clickhouse-config
      readOnly: true
      recursiveReadOnly: Disabled
    - mountPath: /etc/clickhouse-server/profiles.d/
      name: clickhouse-profile
      readOnly: true
      recursiveReadOnly: Disabled
    - mountPath: /etc/clickhouse-server/users.d/
      name: clickhouse-user
      readOnly: true
      recursiveReadOnly: Disabled
    - mountPath: /var/lib/clickhouse
      name: clickhouse-data
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-79rg9
      readOnly: true
      recursiveReadOnly: Disabled
  - containerID: cri-o://6ab8759067d0bc82807f4616ea7f1573823d38f840caadfd65ed4781b87d3558
    image: quay.io/isovalent/hubble-timescape-lite...
    imageID: quay.io/isovalent/hubble-timescape-lite...
    lastState: {}
    name: timescape
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2026-06-29T12:19:08Z"
    volumeMounts:
    - mountPath: /etc/hubble-timescape
      name: config
      readOnly: true
      recursiveReadOnly: Disabled
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-79rg9
      readOnly: true
      recursiveReadOnly: Disabled
  hostIP: 10.10.10.67
  hostIPs:
  - ip: 10.10.10.67
  phase: Running
  podIP: 10.128.1.137
  podIPs:
  - ip: 10.128.1.137
  qosClass: BestEffort
  startTime: "2026-06-29T12:19:02Z"
```

```yaml
apiVersion: v1
kind: Service
metadata:
  annotations:
    meta.helm.sh/release-name: cilium-release
    meta.helm.sh/release-namespace: cilium
  creationTimestamp: "2026-06-29T12:19:02Z"
  labels:
    app.kubernetes.io/component: hubble-timescape
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: hubble-timescape
    app.kubernetes.io/part-of: cilium
    app.kubernetes.io/version: 1.19.0
    isovalent.io/managed-by: clife
    k8s-app: hubble-timescape
  name: hubble-timescape
  namespace: cilium
  ownerReferences:
  - apiVersion: cilium.io/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: CiliumConfig
    name: ciliumconfig
    uid: 23c5b57e-6fa3-429c-a86f-3e212122b307
  resourceVersion: "138481663"
  uid: 13df1035-1480-4eee-866c-525dda158082
spec:
  clusterIP: 172.30.199.148
  clusterIPs:
  - 172.30.199.148
  internalTrafficPolicy: Cluster
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - name: push
    port: 4260
    protocol: TCP
    targetPort: push
  - name: stream
    port: 4261
    protocol: TCP
    targetPort: stream
  - name: grpc
    port: 80
    protocol: TCP
    targetPort: server-grpc
  - name: ui
    port: 8080
    protocol: TCP
    targetPort: ui
  - name: metrics
    port: 9090
    protocol: TCP
    targetPort: metrics
  - name: ch-metrics
    port: 8001
    protocol: TCP
    targetPort: ch-metrics
  selector:
    app.kubernetes.io/name: hubble-timescape
    app.kubernetes.io/part-of: cilium
    k8s-app: hubble-timescape
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
Cluster Pods:          171/171 managed by Cilium
```

[[Back]](../README.md)