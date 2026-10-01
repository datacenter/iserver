## Hubble minimum configuration

[[Back]](../README.md)

- smallest possible configuration with hubble enabled
- hubble server started on every cluster node and running inside Cilium agent
- hubble server listening on :4244 with tls enabled by default
- connection to hubble server abstracted with hubble-peer service 443/TCP
- functional wise not much can be done i.e. hubble cli or ui not working

## Cilium configuration

```yaml
spec:
  hubble:
    enabled: true
```

## Cilium agent

```
time=2026-06-23T09:39:30.436589613Z level=info msg="  --diagnostics-export-file='/var/run/cilium/hubble/status.log'"
time=2026-06-23T09:39:30.436928931Z level=info msg="  --enable-hubble='true'"
time=2026-06-23T09:39:30.436932802Z level=info msg="  --enable-hubble-open-metrics='false'"
time=2026-06-23T09:39:30.437533758Z level=info msg="  --hubble-connectionlog-export-enabled='false'"
time=2026-06-23T09:39:30.437537825Z level=info msg="  --hubble-connectionlog-export-file-compress='false'"
time=2026-06-23T09:39:30.437542112Z level=info msg="  --hubble-connectionlog-export-file-max-backups='5'"
time=2026-06-23T09:39:30.437546231Z level=info msg="  --hubble-connectionlog-export-file-max-size-mb='10'"
time=2026-06-23T09:39:30.437550632Z level=info msg="  --hubble-connectionlog-export-file-path='/var/run/cilium/hubble/connectionlog.log'"
time=2026-06-23T09:39:30.437554884Z level=info msg="  --hubble-connectionlog-export-interval='10s'"
time=2026-06-23T09:39:30.437558563Z level=info msg="  --hubble-disable-tls='false'"
time=2026-06-23T09:39:30.437562429Z level=info msg="  --hubble-drop-events='false'"
time=2026-06-23T09:39:30.437566234Z level=info msg="  --hubble-drop-events-extended='false'"
time=2026-06-23T09:39:30.437570177Z level=info msg="  --hubble-drop-events-interval='2m0s'"
time=2026-06-23T09:39:30.437574118Z level=info msg="  --hubble-drop-events-rate-limit='1'"
time=2026-06-23T09:39:30.437584355Z level=info msg="  --hubble-drop-events-reasons='auth_required,policy_denied'"
time=2026-06-23T09:39:30.437590417Z level=info msg="  --hubble-dynamic-metrics-config-path=''"
time=2026-06-23T09:39:30.437595344Z level=info msg="  --hubble-event-buffer-capacity='4095'"
time=2026-06-23T09:39:30.437599312Z level=info msg="  --hubble-event-queue-size='0'"
time=2026-06-23T09:39:30.437620693Z level=info msg="  --hubble-export-aggregation=''"
time=2026-06-23T09:39:30.437625607Z level=info msg="  --hubble-export-aggregation-ignore-source-port='true'"
time=2026-06-23T09:39:30.437629963Z level=info msg="  --hubble-export-aggregation-interval='0s'"
time=2026-06-23T09:39:30.437633683Z level=info msg="  --hubble-export-aggregation-renew-ttl='true'"
time=2026-06-23T09:39:30.437642963Z level=info msg="  --hubble-export-aggregation-state-filter='new,error,closed'"
time=2026-06-23T09:39:30.437647617Z level=info msg="  --hubble-export-aggregation-ttl='30s'"
time=2026-06-23T09:39:30.437652476Z level=info msg="  --hubble-export-allowlist=''"
time=2026-06-23T09:39:30.437657229Z level=info msg="  --hubble-export-denylist=''"
time=2026-06-23T09:39:30.437669053Z level=info msg="  --hubble-export-fieldaggregate=''"
time=2026-06-23T09:39:30.43768229Z level=info msg="  --hubble-export-fieldmask=''"
time=2026-06-23T09:39:30.437686896Z level=info msg="  --hubble-export-file-compress='false'"
time=2026-06-23T09:39:30.437691175Z level=info msg="  --hubble-export-file-max-backups='5'"
time=2026-06-23T09:39:30.437695373Z level=info msg="  --hubble-export-file-max-size-mb='10'"
time=2026-06-23T09:39:30.437700642Z level=info msg="  --hubble-export-file-path=''"
time=2026-06-23T09:39:30.437704479Z level=info msg="  --hubble-export-file-rotation-interval='0s'"
time=2026-06-23T09:39:30.437708562Z level=info msg="  --hubble-export-format-version='v1'"
time=2026-06-23T09:39:30.437713508Z level=info msg="  --hubble-export-node-name=''"
time=2026-06-23T09:39:30.437717462Z level=info msg="  --hubble-export-rate-limit='-1'"
time=2026-06-23T09:39:30.437728983Z level=info msg="  --hubble-export-timescape-aggregation=''"
time=2026-06-23T09:39:30.437733802Z level=info msg="  --hubble-export-timescape-aggregation-ignore-source-port='true'"
time=2026-06-23T09:39:30.437737979Z level=info msg="  --hubble-export-timescape-aggregation-renew-ttl='true'"
time=2026-06-23T09:39:30.437747149Z level=info msg="  --hubble-export-timescape-aggregation-state-filter='new,error,closed'"
time=2026-06-23T09:39:30.437751871Z level=info msg="  --hubble-export-timescape-aggregation-ttl='30s'"
time=2026-06-23T09:39:30.437756886Z level=info msg="  --hubble-export-timescape-allowlist=''"
time=2026-06-23T09:39:30.437762792Z level=info msg="  --hubble-export-timescape-denylist=''"
time=2026-06-23T09:39:30.437766612Z level=info msg="  --hubble-export-timescape-enabled='false'"
time=2026-06-23T09:39:30.437778879Z level=info msg="  --hubble-export-timescape-fieldmask=''"
time=2026-06-23T09:39:30.437783605Z level=info msg="  --hubble-export-timescape-max-buffer-size='4096'"
time=2026-06-23T09:39:30.437789002Z level=info msg="  --hubble-export-timescape-node-name=''"
time=2026-06-23T09:39:30.437793221Z level=info msg="  --hubble-export-timescape-report-dropped-flows-interval='1m0s'"
time=2026-06-23T09:39:30.437797934Z level=info msg="  --hubble-export-timescape-target='hubble-timescape-export.hubble-timescape.svc.cluster.local:4261'"
time=2026-06-23T09:39:30.437809833Z level=info msg="  --hubble-export-timescape-tls-ca-files=''"
time=2026-06-23T09:39:30.437815712Z level=info msg="  --hubble-export-timescape-tls-cert-file=''"
time=2026-06-23T09:39:30.437819752Z level=info msg="  --hubble-export-timescape-tls-enabled='false'"
time=2026-06-23T09:39:30.437824901Z level=info msg="  --hubble-export-timescape-tls-key-file=''"
time=2026-06-23T09:39:30.437828894Z level=info msg="  --hubble-export-timescape-use-cilium-service-resolver='true'"
time=2026-06-23T09:39:30.437834201Z level=info msg="  --hubble-flowlogs-config-path=''"
time=2026-06-23T09:39:30.437838006Z level=info msg="  --hubble-listen-address=':4244'"
time=2026-06-23T09:39:30.437841848Z level=info msg="  --hubble-lost-event-send-interval='1s'"
time=2026-06-23T09:39:30.437847705Z level=info msg="  --hubble-metrics=''"
time=2026-06-23T09:39:30.437852633Z level=info msg="  --hubble-metrics-server=''"
time=2026-06-23T09:39:30.437856635Z level=info msg="  --hubble-metrics-server-enable-tls='false'"
time=2026-06-23T09:39:30.437862179Z level=info msg="  --hubble-metrics-server-tls-cert-file=''"
time=2026-06-23T09:39:30.437875068Z level=info msg="  --hubble-metrics-server-tls-client-ca-files=''"
time=2026-06-23T09:39:30.437881228Z level=info msg="  --hubble-metrics-server-tls-key-file=''"
time=2026-06-23T09:39:30.437892785Z level=info msg="  --hubble-monitor-events=''"
time=2026-06-23T09:39:30.437897366Z level=info msg="  --hubble-network-policy-correlation-enabled='true'"
time=2026-06-23T09:39:30.437902111Z level=info msg="  --hubble-prefer-ipv6='false'"
time=2026-06-23T09:39:30.437905927Z level=info msg="  --hubble-redact-enabled='false'"
time=2026-06-23T09:39:30.437918776Z level=info msg="  --hubble-redact-http-headers-allow=''"
time=2026-06-23T09:39:30.437930633Z level=info msg="  --hubble-redact-http-headers-deny=''"
time=2026-06-23T09:39:30.437935009Z level=info msg="  --hubble-redact-http-urlquery='false'"
time=2026-06-23T09:39:30.43793877Z level=info msg="  --hubble-redact-http-userinfo='true'"
time=2026-06-23T09:39:30.437942735Z level=info msg="  --hubble-redact-kafka-apikey='false'"
time=2026-06-23T09:39:30.437946778Z level=info msg="  --hubble-skip-unknown-cgroup-ids='true'"
time=2026-06-23T09:39:30.437950914Z level=info msg="  --hubble-socket-path='/var/run/cilium/hubble.sock'"
time=2026-06-23T09:39:30.437954794Z level=info msg="  --hubble-tls-cert-file='/var/lib/cilium/tls/hubble/server.crt'"
time=2026-06-23T09:39:30.437959051Z level=info msg="  --hubble-tls-client-ca-files='/var/lib/cilium/tls/hubble/client-ca.crt'"
time=2026-06-23T09:39:30.43796318Z level=info msg="  --hubble-tls-key-file='/var/lib/cilium/tls/hubble/server.key'"
time=2026-06-23T09:39:30.694596442Z level=info msg="Hubble ConnectionLog exporter disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-connectionlog subsys=hubble-connectionlog
time=2026-06-23T09:39:30.694754941Z level=info msg="The Hubble static exporter is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-exporters
time=2026-06-23T09:39:30.694769429Z level=info msg="The Hubble dynamic exporter is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-exporters
time=2026-06-23T09:39:30.694966578Z level=info msg="Certloader TLS watcher disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter config=certloader-client-tls
time=2026-06-23T09:39:30.694986007Z level=info msg="The Hubble timescape exporter is disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter
time=2026-06-23T09:39:30.695174409Z level=info msg="The Hubble EE static exporter is disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter
time=2026-06-23T09:39:30.695194284Z level=info msg="The Hubble EE dynamic exporter is disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter
time=2026-06-23T09:39:30.69531144Z level=info msg="The Hubble packet drop events emitter is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-dropeventemitter
time=2026-06-23T09:39:30.695702726Z level=info msg="Certloader TLS watcher disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-metrics config=certloader-server-tls
time=2026-06-23T09:39:30.695889149Z level=info msg="The Hubble metrics server is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-metrics
time=2026-06-23T09:39:31.438888964Z level=info msg="Configuring Hubble server" module=enterprise-agent.agent.controlplane.hubble maxFlows=4095 eventQueueSize=16384
time=2026-06-23T09:39:31.43969476Z level=info msg="Starting local Hubble server" module=enterprise-agent.agent.controlplane.hubble address=unix:///var/run/cilium/hubble.sock
time=2026-06-23T09:39:31.440147852Z level=info msg="Starting Hubble server" module=enterprise-agent.agent.controlplane.hubble address=:4244 tls=true
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

## Service

```
$ oc get service -n cilium
NAME              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
hubble-peer       ClusterIP   172.30.77.238    <none>        443/TCP    245d
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

```
$ oc get ep -n cilium
NAME              ENDPOINTS                                            AGE
hubble-peer       10.10.10.65:4244,10.10.10.66:4244,10.10.10.67:4244   45m
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
Cluster Pods:          166/166 managed by Cilium
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