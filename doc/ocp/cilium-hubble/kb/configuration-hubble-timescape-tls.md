## Integrated Hubble Timescape with TLS

[[Back]](../README.md)

## Cilium configuration

```yaml
spec:
  hubble:
    enabled: true
    timescape:
      enabled: true
    tls:
      auto:
        certManagerIssuerRef:
          group: cert-manager.io
          kind: ClusterIssuer
          name: root-ca
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
  name: root-ca
spec:
  ca:
    secretName: root-ca
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

Once timescape starts, you expect to see the following cert-manager state

```
# iserver get ocp cert-manager -v res

OpenShift Workflow - Certificate Manager - Get Information
==========================================================

OpenShift Cluster: bm1


Certificate Manager Resources
-----------------------------
- cluster issuer      : 1
- issuer              : 0
- certificate request : 3
- certificate         : 3


+----+----------------+-----------+----------------------------------------------------+-------+
| ID | Cluster Issuer | Secret    | Certificate                                        | Ready |
+----+----------------+-----------+----------------------------------------------------+-------+
| 1  | root-ca        | ✓ root-ca | "version": "v3",                                   | ✓     | 
|    |                |           | "serial": 111,                                     |       | 
|    |                |           | "issuer": "CN=cilium-ca-root",                     |       | 
|    |                |           | "subject": "CN=cilium-ca-root",                    |       | 
|    |                |           | "sign_algo": "sha256WithRSAEncryption",            |       | 
|    |                |           | "hash_algo": "sha256",                             |       | 
|    |                |           | "valid_from": "2025-04-29T12:57:23.000000",        |       | 
|    |                |           | "valid_to": "2027-02-05T04:57:23.000000"           |       | 
+----+----------------+-----------+----------------------------------------------------+-------+

+----+---------------------------------+----------+-------+------------------------+-------------------------------------------------+
| ID | Certificate Request             | Approved | Ready | Issuer                 | Requester                                       |
+----+---------------------------------+----------+-------+------------------------+-------------------------------------------------+
| 1  | cilium                          | ✓        | ✓     | kind: ClusterIssuer    | system:serviceaccount:cert-manager:cert-manager | 
|    | hubble-server-certs-1           |          |       | name: root-ca          |                                                 | 
|    |                                 |          |       | group: cert-manager.io |                                                 | 
+----+---------------------------------+----------+-------+------------------------+-------------------------------------------------+
| 2  | cilium                          | ✓        | ✓     | kind: ClusterIssuer    | system:serviceaccount:cert-manager:cert-manager | 
|    | hubble-timescape-client-certs-1 |          |       | name: root-ca          |                                                 | 
|    |                                 |          |       | group: cert-manager.io |                                                 | 
+----+---------------------------------+----------+-------+------------------------+-------------------------------------------------+
| 3  | cilium                          | ✓        | ✓     | kind: ClusterIssuer    | system:serviceaccount:cert-manager:cert-manager | 
|    | hubble-timescape-server-certs-1 |          |       | name: root-ca          |                                                 | 
|    |                                 |          |       | group: cert-manager.io |                                                 | 
+----+---------------------------------+----------+-------+------------------------+-------------------------------------------------+

+----+-------------------------------+-----------------------------+---------------------------------+-------------------------------------------------------------+-------+
| ID | Certificate                   | Issuer                      | Secret                          | Certificate                                                 | Ready |
+----+-------------------------------+-----------------------------+---------------------------------+-------------------------------------------------------------+-------+
| 1  | cilium                        | "group": "cert-manager.io", | ✓ hubble-server-certs           | "version": "v3",                                            | ✓     | 
|    | hubble-server-certs           | "kind": "ClusterIssuer",    |                                 | "serial": 222,                                              |       | 
|    |                               | "name": "root-ca"           |                                 | "issuer": "CN=cilium-ca-root",                              |       | 
|    |                               |                             |                                 | "subject": "CN=*.default.hubble-grpc.cilium.io",            |       | 
|    |                               |                             |                                 | "sign_algo": "sha256WithRSAEncryption",                     |       | 
|    |                               |                             |                                 | "hash_algo": "sha256",                                      |       | 
|    |                               |                             |                                 | "valid_from": "2026-07-01T07:31:24.000000",                 |       | 
|    |                               |                             |                                 | "valid_to": "2026-07-02T07:31:24.000000"                    |       | 
+----+-------------------------------+-----------------------------+---------------------------------+-------------------------------------------------------------+-------+
| 2  | cilium                        | "group": "cert-manager.io", | ✓ hubble-timescape-client-certs | "version": "v3",                                            | ✓     | 
|    | hubble-timescape-client-certs | "kind": "ClusterIssuer",    |                                 | "serial": 333,                                              |       | 
|    |                               | "name": "root-ca"           |                                 | "issuer": "CN=cilium-ca-root",                              |       | 
|    |                               |                             |                                 | "subject": "CN=hubble-timescape-client",                    |       | 
|    |                               |                             |                                 | "sign_algo": "sha256WithRSAEncryption",                     |       | 
|    |                               |                             |                                 | "hash_algo": "sha256",                                      |       | 
|    |                               |                             |                                 | "valid_from": "2026-07-01T07:31:23.000000",                 |       | 
|    |                               |                             |                                 | "valid_to": "2026-07-02T07:31:23.000000"                    |       | 
+----+-------------------------------+-----------------------------+---------------------------------+-------------------------------------------------------------+-------+
| 3  | cilium                        | "group": "cert-manager.io", | ✓ hubble-timescape-server-certs | "version": "v3",                                            | ✓     | 
|    | hubble-timescape-server-certs | "kind": "ClusterIssuer",    |                                 | "serial": 444,                                              |       | 
|    |                               | "name": "root-ca"           |                                 | "issuer": "CN=cilium-ca-root",                              |       | 
|    |                               |                             |                                 | "subject": "CN=hubble-timescape",                           |       | 
|    |                               |                             |                                 | "sign_algo": "sha256WithRSAEncryption",                     |       | 
|    |                               |                             |                                 | "hash_algo": "sha256",                                      |       | 
|    |                               |                             |                                 | "valid_from": "2026-07-01T07:31:24.000000",                 |       | 
|    |                               |                             |                                 | "valid_to": "2026-07-02T07:31:24.000000"                    |       | 
+----+-------------------------------+-----------------------------+---------------------------------+-------------------------------------------------------------+-------+
```

## Cilium agent

```
time=2026-07-01T07:31:43.086412868Z level=info msg="  --diagnostics-export-file='/var/run/cilium/hubble/status.log'"
time=2026-07-01T07:31:43.086830225Z level=info msg="  --enable-hubble='true'"
time=2026-07-01T07:31:43.086835277Z level=info msg="  --enable-hubble-open-metrics='false'"
time=2026-07-01T07:31:43.087483465Z level=info msg="  --feature-gates-approved='CNIChainingMode,ClusterMeshKVStoreMesh,BFD,BGPControlPlane,BGPRouteImport,CNIChainingMode,ClusterMesh,EVPN,EnterpriseBGPControlPlane,MultiNetwork,VTEPIntegration,PrivateNetworks,HubbleTimescape'"
time=2026-07-01T07:31:43.087588966Z level=info msg="  --hubble-connectionlog-export-enabled='false'"
time=2026-07-01T07:31:43.087596565Z level=info msg="  --hubble-connectionlog-export-file-compress='false'"
time=2026-07-01T07:31:43.087602095Z level=info msg="  --hubble-connectionlog-export-file-max-backups='5'"
time=2026-07-01T07:31:43.087607599Z level=info msg="  --hubble-connectionlog-export-file-max-size-mb='10'"
time=2026-07-01T07:31:43.087613111Z level=info msg="  --hubble-connectionlog-export-file-path='/var/run/cilium/hubble/connectionlog.log'"
time=2026-07-01T07:31:43.087618588Z level=info msg="  --hubble-connectionlog-export-interval='10s'"
time=2026-07-01T07:31:43.087623548Z level=info msg="  --hubble-disable-tls='false'"
time=2026-07-01T07:31:43.087628368Z level=info msg="  --hubble-drop-events='false'"
time=2026-07-01T07:31:43.087633148Z level=info msg="  --hubble-drop-events-extended='false'"
time=2026-07-01T07:31:43.087638182Z level=info msg="  --hubble-drop-events-interval='2m0s'"
time=2026-07-01T07:31:43.087643317Z level=info msg="  --hubble-drop-events-rate-limit='1'"
time=2026-07-01T07:31:43.087653014Z level=info msg="  --hubble-drop-events-reasons='auth_required,policy_denied'"
time=2026-07-01T07:31:43.087662026Z level=info msg="  --hubble-dynamic-metrics-config-path=''"
time=2026-07-01T07:31:43.08766758Z level=info msg="  --hubble-event-buffer-capacity='4095'"
time=2026-07-01T07:31:43.087672733Z level=info msg="  --hubble-event-queue-size='0'"
time=2026-07-01T07:31:43.087684479Z level=info msg="  --hubble-export-aggregation=''"
time=2026-07-01T07:31:43.087690282Z level=info msg="  --hubble-export-aggregation-ignore-source-port='true'"
time=2026-07-01T07:31:43.087695478Z level=info msg="  --hubble-export-aggregation-interval='0s'"
time=2026-07-01T07:31:43.087700416Z level=info msg="  --hubble-export-aggregation-renew-ttl='true'"
time=2026-07-01T07:31:43.087710103Z level=info msg="  --hubble-export-aggregation-state-filter='new,error,closed'"
time=2026-07-01T07:31:43.087717385Z level=info msg="  --hubble-export-aggregation-ttl='30s'"
time=2026-07-01T07:31:43.087723511Z level=info msg="  --hubble-export-allowlist=''"
time=2026-07-01T07:31:43.087729458Z level=info msg="  --hubble-export-denylist=''"
time=2026-07-01T07:31:43.087743856Z level=info msg="  --hubble-export-fieldaggregate=''"
time=2026-07-01T07:31:43.087764803Z level=info msg="  --hubble-export-fieldmask=''"
time=2026-07-01T07:31:43.087770456Z level=info msg="  --hubble-export-file-compress='false'"
time=2026-07-01T07:31:43.087775577Z level=info msg="  --hubble-export-file-max-backups='5'"
time=2026-07-01T07:31:43.087780598Z level=info msg="  --hubble-export-file-max-size-mb='10'"
time=2026-07-01T07:31:43.087786723Z level=info msg="  --hubble-export-file-path=''"
time=2026-07-01T07:31:43.087791698Z level=info msg="  --hubble-export-file-rotation-interval='0s'"
time=2026-07-01T07:31:43.087797129Z level=info msg="  --hubble-export-format-version='v1'"
time=2026-07-01T07:31:43.087803053Z level=info msg="  --hubble-export-node-name=''"
time=2026-07-01T07:31:43.08780822Z level=info msg="  --hubble-export-rate-limit='-1'"
time=2026-07-01T07:31:43.087813251Z level=info msg="  --hubble-export-timescape-aggregation='connection'"
time=2026-07-01T07:31:43.087818903Z level=info msg="  --hubble-export-timescape-aggregation-ignore-source-port='true'"
time=2026-07-01T07:31:43.087823864Z level=info msg="  --hubble-export-timescape-aggregation-renew-ttl='false'"
time=2026-07-01T07:31:43.087829168Z level=info msg="  --hubble-export-timescape-aggregation-state-filter='new,error'"
time=2026-07-01T07:31:43.087834165Z level=info msg="  --hubble-export-timescape-aggregation-ttl='30s'"
time=2026-07-01T07:31:43.087840896Z level=info msg="  --hubble-export-timescape-allowlist=''"
time=2026-07-01T07:31:43.087847042Z level=info msg="  --hubble-export-timescape-denylist=''"
time=2026-07-01T07:31:43.087851798Z level=info msg="  --hubble-export-timescape-enabled='true'"
time=2026-07-01T07:31:43.087866328Z level=info msg="  --hubble-export-timescape-fieldmask=''"
time=2026-07-01T07:31:43.087872623Z level=info msg="  --hubble-export-timescape-max-buffer-size='4096'"
time=2026-07-01T07:31:43.087879408Z level=info msg="  --hubble-export-timescape-node-name=''"
time=2026-07-01T07:31:43.087884628Z level=info msg="  --hubble-export-timescape-report-dropped-flows-interval='1m0s'"
time=2026-07-01T07:31:43.087889916Z level=info msg="  --hubble-export-timescape-target='hubble-timescape.cilium.svc.cluster.local:4261'"
time=2026-07-01T07:31:43.087895673Z level=info msg="  --hubble-export-timescape-tls-ca-files='/var/lib/cilium/tls/hubble-export-timescape/client-ca.crt'"
time=2026-07-01T07:31:43.087901613Z level=info msg="  --hubble-export-timescape-tls-cert-file='/var/lib/cilium/tls/hubble-export-timescape/client.crt'"
time=2026-07-01T07:31:43.087906994Z level=info msg="  --hubble-export-timescape-tls-enabled='true'"
time=2026-07-01T07:31:43.087911935Z level=info msg="  --hubble-export-timescape-tls-key-file='/var/lib/cilium/tls/hubble-export-timescape/client.key'"
time=2026-07-01T07:31:43.087917334Z level=info msg="  --hubble-export-timescape-use-cilium-service-resolver='true'"
time=2026-07-01T07:31:43.087923567Z level=info msg="  --hubble-flowlogs-config-path=''"
time=2026-07-01T07:31:43.087928228Z level=info msg="  --hubble-listen-address=':4244'"
time=2026-07-01T07:31:43.087932895Z level=info msg="  --hubble-lost-event-send-interval='1s'"
time=2026-07-01T07:31:43.087939208Z level=info msg="  --hubble-metrics=''"
time=2026-07-01T07:31:43.087946144Z level=info msg="  --hubble-metrics-server=''"
time=2026-07-01T07:31:43.087951216Z level=info msg="  --hubble-metrics-server-enable-tls='false'"
time=2026-07-01T07:31:43.087957805Z level=info msg="  --hubble-metrics-server-tls-cert-file=''"
time=2026-07-01T07:31:43.08797223Z level=info msg="  --hubble-metrics-server-tls-client-ca-files=''"
time=2026-07-01T07:31:43.08797924Z level=info msg="  --hubble-metrics-server-tls-key-file=''"
time=2026-07-01T07:31:43.08799325Z level=info msg="  --hubble-monitor-events=''"
time=2026-07-01T07:31:43.087999028Z level=info msg="  --hubble-network-policy-correlation-enabled='true'"
time=2026-07-01T07:31:43.088004068Z level=info msg="  --hubble-prefer-ipv6='false'"
time=2026-07-01T07:31:43.088008931Z level=info msg="  --hubble-redact-enabled='false'"
time=2026-07-01T07:31:43.088022502Z level=info msg="  --hubble-redact-http-headers-allow=''"
time=2026-07-01T07:31:43.088038341Z level=info msg="  --hubble-redact-http-headers-deny=''"
time=2026-07-01T07:31:43.088043887Z level=info msg="  --hubble-redact-http-urlquery='false'"
time=2026-07-01T07:31:43.088048863Z level=info msg="  --hubble-redact-http-userinfo='true'"
time=2026-07-01T07:31:43.088053634Z level=info msg="  --hubble-redact-kafka-apikey='false'"
time=2026-07-01T07:31:43.088058569Z level=info msg="  --hubble-skip-unknown-cgroup-ids='true'"
time=2026-07-01T07:31:43.088063967Z level=info msg="  --hubble-socket-path='/var/run/cilium/hubble.sock'"
time=2026-07-01T07:31:43.088069793Z level=info msg="  --hubble-tls-cert-file='/var/lib/cilium/tls/hubble/server.crt'"
time=2026-07-01T07:31:43.088075263Z level=info msg="  --hubble-tls-client-ca-files='/var/lib/cilium/tls/hubble/client-ca.crt'"
time=2026-07-01T07:31:43.088080494Z level=info msg="  --hubble-tls-key-file='/var/lib/cilium/tls/hubble/server.key'"
time=2026-07-01T07:31:43.420238102Z level=info msg="Hubble ConnectionLog exporter disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-connectionlog subsys=hubble-connectionlog
time=2026-07-01T07:31:43.420438216Z level=info msg="The Hubble static exporter is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-exporters
time=2026-07-01T07:31:43.420458138Z level=info msg="The Hubble dynamic exporter is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-exporters
time=2026-07-01T07:31:43.420992586Z level=info msg="The Hubble EE static exporter is disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter
time=2026-07-01T07:31:43.421021028Z level=info msg="The Hubble EE dynamic exporter is disabled" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter
time=2026-07-01T07:31:43.42118921Z level=info msg="The Hubble packet drop events emitter is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-dropeventemitter
time=2026-07-01T07:31:43.421724806Z level=info msg="Certloader TLS watcher disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-metrics config=certloader-server-tls
time=2026-07-01T07:31:43.42196777Z level=info msg="Building the Hubble timescape exporter" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter config="{Enabled:true Target:hubble-timescape.cilium.svc.cluster.local:4261 Allowlist: Denylist: Fieldmask:[] NodeName: Aggregations:[connection] AggregationIgnoreSourcePort:true AggregationRenewTTL:false AggregationStateChangeFilter:[new error] AggregationTTL:30s MaxBufferSize:4096 ReportDroppedFlowsInterval:1m0s UseCiliumServiceResolver:true TLSEnabled:true TLSCertFile:/var/lib/cilium/tls/hubble-export-timescape/client.crt TLSKeyFile:/var/lib/cilium/tls/hubble-export-timescape/client.key TLSCAFiles:[/var/lib/cilium/tls/hubble-export-timescape/client-ca.crt]}"
time=2026-07-01T07:31:43.422045781Z level=info msg="The Hubble metrics server is disabled" module=enterprise-agent.agent.controlplane.hubble.hubble-metrics
time=2026-07-01T07:31:45.818102911Z level=info msg="start streaming flow logs" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter subsys=hubble-timescape-exporter target=hubble-timescape.cilium.svc.cluster.local:4261
time=2026-07-01T07:31:45.818442028Z level=info msg="Configuring Hubble server" module=enterprise-agent.agent.controlplane.hubble maxFlows=4095 eventQueueSize=16384
time=2026-07-01T07:31:45.819003104Z level=error msg="failed to stream flow logs" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter subsys=hubble-timescape-exporter target=hubble-timescape.cilium.svc.cluster.local:4261 error="failed to create stream: rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp 172.30.199.148:4261: connect: connection refused\""
time=2026-07-01T07:31:45.819036663Z level=info msg="retrying export after backoff" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter subsys=hubble-timescape-exporter target=hubble-timescape.cilium.svc.cluster.local:4261 duration=2s retries=1
time=2026-07-01T07:31:45.819336262Z level=info msg="Starting local Hubble server" module=enterprise-agent.agent.controlplane.hubble address=unix:///var/run/cilium/hubble.sock
time=2026-07-01T07:31:45.819432461Z level=info msg="Starting Hubble server" module=enterprise-agent.agent.controlplane.hubble address=:4244 tls=true
time=2026-07-01T07:31:45.995939019Z level=info msg="New endpoint" ipv6="" desiredPolicyRevision=0 ciliumEndpointName=cilium/hubble-timescape-0 containerID=dbe474a123 identity=773 containerInterface=eth0 datapathPolicyRevision=0 ipv4=10.128.1.137 endpointID=502 k8sPodName=cilium/hubble-timescape-0 subsys=endpoint
time=2026-07-01T07:31:47.81914685Z level=info msg="start streaming flow logs" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter subsys=hubble-timescape-exporter target=hubble-timescape.cilium.svc.cluster.local:4261
time=2026-07-01T07:31:47.819962852Z level=error msg="failed to stream flow logs" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter subsys=hubble-timescape-exporter target=hubble-timescape.cilium.svc.cluster.local:4261 error="failed to create stream: rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp 172.30.199.148:4261: connect: connection refused\""
time=2026-07-01T07:31:47.819995231Z level=info msg="retrying export after backoff" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter subsys=hubble-timescape-exporter target=hubble-timescape.cilium.svc.cluster.local:4261 duration=4s retries=2
time=2026-07-01T07:31:49.685987114Z level=info msg="Delete endpoint by containerID request" module=enterprise-agent.agent.controlplane.endpoint-api containerID=dbe474a123af155521b02ab22b4dbadf1171297051fdf44663c9b9bbbbe575d3 endpointID=502 k8sPodName=hubble-timescape-0 k8sNamespace=cilium
time=2026-07-01T07:31:51.578719786Z level=info msg="Removed endpoint" ipv6="" desiredPolicyRevision=0 ciliumEndpointName=cilium/hubble-timescape-0 containerID=dbe474a123 identity=773 containerInterface=eth0 datapathPolicyRevision=0 ipv4=10.128.1.137 endpointID=502 k8sPodName=cilium/hubble-timescape-0 subsys=endpoint
time=2026-07-01T07:31:51.820312683Z level=info msg="start streaming flow logs" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter subsys=hubble-timescape-exporter target=hubble-timescape.cilium.svc.cluster.local:4261
time=2026-07-01T07:31:51.821056525Z level=error msg="failed to stream flow logs" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter subsys=hubble-timescape-exporter target=hubble-timescape.cilium.svc.cluster.local:4261 error="failed to create stream: rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp 172.30.199.148:4261: connect: connection refused\""
time=2026-07-01T07:31:51.821095479Z level=info msg="retrying export after backoff" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter subsys=hubble-timescape-exporter target=hubble-timescape.cilium.svc.cluster.local:4261 duration=8s retries=3
time=2026-07-01T07:31:54.746351645Z level=info msg="Create endpoint request" module=enterprise-agent.agent.controlplane.endpoint-api addressing="&{IPv4:10.128.1.52 IPv4ExpirationUUID:70f4ea62-29e3-4fa3-88fd-df4012773875 IPv4PoolName:default IPv6: IPv6ExpirationUUID: IPv6PoolName:}" containerID=0ecfc3bf4e4f32aa5ba668798e3656bb367ede14d28806169061fcdabdad977e containerInterface=eth0 datapathConfiguration="&{DisableSipVerification:false ExternalIpam:false InstallEndpointRoute:false RequireArpPassthrough:false RequireEgressProg:false RequireRouting:<nil>}" interface=lxc9168182ee10c k8sPodName=cilium/hubble-timescape-0 k8sUID=ce7e609c-b30a-4e76-af75-ee0fef8c74eb labels=[] sync-build=true
time=2026-07-01T07:31:54.746802401Z level=info msg="New endpoint" datapathPolicyRevision=0 ciliumEndpointName=cilium/hubble-timescape-0 containerInterface="" ipv4=10.128.1.52 endpointID=3672 ipv6="" desiredPolicyRevision=0 k8sPodName=cilium/hubble-timescape-0 containerID=0ecfc3bf4e subsys=endpoint
time=2026-07-01T07:31:54.747096358Z level=info msg="Resolving identity labels (blocking)" datapathPolicyRevision=0 ciliumEndpointName=cilium/hubble-timescape-0 containerInterface="" ipv4=10.128.1.52 endpointID=3672 ipv6="" desiredPolicyRevision=0 k8sPodName=cilium/hubble-timescape-0 containerID=0ecfc3bf4e subsys=endpoint identityLabels="k8s:app.kubernetes.io/name=hubble-timescape,k8s:app.kubernetes.io/part-of=cilium,k8s:io.cilium.k8s.namespace.labels.app.kubernetes.io/managed-by=kustomize,k8s:io.cilium.k8s.namespace.labels.app.kubernetes.io/name=clife,k8s:io.cilium.k8s.namespace.labels.control-plane=controller-manager,k8s:io.cilium.k8s.namespace.labels.kubernetes.io/metadata.name=cilium,k8s:io.cilium.k8s.namespace.labels.olm.operatorgroup.uid/84b4b2bd-0c3d-4a95-91f3-123d3b5b1407,k8s:io.cilium.k8s.namespace.labels.openshift.io/cluster-logging=true,k8s:io.cilium.k8s.namespace.labels.openshift.io/cluster-monitoring=true,k8s:io.cilium.k8s.namespace.labels.openshift.io/run-level=0,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/audit-version=latest,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/audit=privileged,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/warn-version=latest,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/warn=privileged,k8s:io.cilium.k8s.policy.cluster=default,k8s:io.cilium.k8s.policy.serviceaccount=hubble-timescape,k8s:io.kubernetes.pod.namespace=cilium,k8s:k8s-app=hubble-timescape"
time=2026-07-01T07:31:54.747260482Z level=info msg="Identity of endpoint changed" datapathPolicyRevision=0 ciliumEndpointName=cilium/hubble-timescape-0 containerInterface="" ipv4=10.128.1.52 endpointID=3672 ipv6="" desiredPolicyRevision=0 k8sPodName=cilium/hubble-timescape-0 containerID=0ecfc3bf4e subsys=endpoint new-identity=773 old-identity="no identity" identityLabels="k8s:app.kubernetes.io/name=hubble-timescape,k8s:app.kubernetes.io/part-of=cilium,k8s:io.cilium.k8s.namespace.labels.app.kubernetes.io/managed-by=kustomize,k8s:io.cilium.k8s.namespace.labels.app.kubernetes.io/name=clife,k8s:io.cilium.k8s.namespace.labels.control-plane=controller-manager,k8s:io.cilium.k8s.namespace.labels.kubernetes.io/metadata.name=cilium,k8s:io.cilium.k8s.namespace.labels.olm.operatorgroup.uid/84b4b2bd-0c3d-4a95-91f3-123d3b5b1407,k8s:io.cilium.k8s.namespace.labels.openshift.io/cluster-logging=true,k8s:io.cilium.k8s.namespace.labels.openshift.io/cluster-monitoring=true,k8s:io.cilium.k8s.namespace.labels.openshift.io/run-level=0,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/audit-version=latest,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/audit=privileged,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/warn-version=latest,k8s:io.cilium.k8s.namespace.labels.pod-security.kubernetes.io/warn=privileged,k8s:io.cilium.k8s.policy.cluster=default,k8s:io.cilium.k8s.policy.serviceaccount=hubble-timescape,k8s:io.kubernetes.pod.namespace=cilium,k8s:k8s-app=hubble-timescape"
time=2026-07-01T07:31:54.747335636Z level=info msg="Waiting for endpoint to be generated" datapathPolicyRevision=0 identity=773 ciliumEndpointName=cilium/hubble-timescape-0 containerInterface="" ipv4=10.128.1.52 endpointID=3672 ipv6="" desiredPolicyRevision=0 k8sPodName=cilium/hubble-timescape-0 containerID=0ecfc3bf4e subsys=endpoint
time=2026-07-01T07:31:55.33000611Z level=info msg="Reloaded endpoint BPF program" datapathPolicyRevision=0 identity=773 ciliumEndpointName=cilium/hubble-timescape-0 containerInterface="" ipv4=10.128.1.52 endpointID=3672 ipv6="" desiredPolicyRevision=2 k8sPodName=cilium/hubble-timescape-0 containerID=0ecfc3bf4e subsys=endpoint
time=2026-07-01T07:31:55.3304533Z level=info msg="Successful endpoint creation" datapathPolicyRevision=2 identity=773 ciliumEndpointName=cilium/hubble-timescape-0 containerInterface="" ipv4=10.128.1.52 endpointID=3672 ipv6="" desiredPolicyRevision=2 k8sPodName=cilium/hubble-timescape-0 containerID=0ecfc3bf4e subsys=endpoint-api
time=2026-07-01T07:31:59.821835516Z level=info msg="start streaming flow logs" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter subsys=hubble-timescape-exporter target=hubble-timescape.cilium.svc.cluster.local:4261
time=2026-07-01T07:31:59.822659905Z level=error msg="failed to stream flow logs" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter subsys=hubble-timescape-exporter target=hubble-timescape.cilium.svc.cluster.local:4261 error="failed to create stream: rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp 172.30.199.148:4261: connect: connection refused\""
time=2026-07-01T07:31:59.822693135Z level=info msg="retrying export after backoff" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter subsys=hubble-timescape-exporter target=hubble-timescape.cilium.svc.cluster.local:4261 duration=16s retries=4
time=2026-07-01T07:32:15.822789086Z level=info msg="start streaming flow logs" module=enterprise-agent.enterprise-controlplane.enterprise-hubble.enterprise-hubble-exporter.hubble-timescape-exporter subsys=hubble-timescape-exporter target=hubble-timescape.cilium.svc.cluster.local:4261
```

## Config map

```
$ oc get configmaps -n cilium cilium-config -o yaml | grep -i hubble
  diagnostics-export-file: /var/run/cilium/hubble/status.log
  enable-hubble: "true"
  feature-gates-approved: CNIChainingMode,ClusterMeshKVStoreMesh,BFD,BGPControlPlane,BGPRouteImport,CNIChainingMode,ClusterMesh,EVPN,EnterpriseBGPControlPlane,MultiNetwork,VTEPIntegration,PrivateNetworks,HubbleTimescape
  hubble-connectionlog-export-enabled: "false"
  hubble-disable-tls: "false"
  hubble-export-timescape-aggregation: connection
  hubble-export-timescape-aggregation-renew-ttl: "false"
  hubble-export-timescape-aggregation-state-filter: new error
  hubble-export-timescape-enabled: "true"
  hubble-export-timescape-target: hubble-timescape.cilium.svc.cluster.local:4261
  hubble-export-timescape-tls-ca-files: /var/lib/cilium/tls/hubble-export-timescape/client-ca.crt
  hubble-export-timescape-tls-cert-file: /var/lib/cilium/tls/hubble-export-timescape/client.crt
  hubble-export-timescape-tls-enabled: "true"
  hubble-export-timescape-tls-key-file: /var/lib/cilium/tls/hubble-export-timescape/client.key
  hubble-export-timescape-use-cilium-service-resolver: "true"
  hubble-listen-address: :4244
  hubble-network-policy-correlation-enabled: "true"
  hubble-socket-path: /var/run/cilium/hubble.sock
  hubble-tls-cert-file: /var/lib/cilium/tls/hubble/server.crt
  hubble-tls-client-ca-files: /var/lib/cilium/tls/hubble/client-ca.crt
  hubble-tls-key-file: /var/lib/cilium/tls/hubble/server.key
```

## Hubble Timescape

```
$ oc get pod -n cilium
NAME                    READY   STATUS    RESTARTS       AGE
hubble-timescape-0      2/2     Running   0             25m
```

```
$ oc get service -n cilium hubble-timescape
NAME               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                                                AGE
hubble-timescape   ClusterIP   172.30.199.148   <none>        4260/TCP,4261/TCP,443/TCP,8080/TCP,9090/TCP,8001/TCP   43h
```

Containers
- clickhouse: built-in database that keeps the last few hours of historical flow information
- timescape: main application with built-in ui

Container | Name | Port | Service | Description
--- | --- | --- | --- | ---
clickhouse | ch-port | tcp/8081 | --- | ---
clickhouse | ch-metrics | tcp/8001 | hubble-timescape tcp/8001 | In this setup metrics are disabled so probably not used
timescape | health-grpc | tcp/8083 | --- | ---
timescape | server-grpc | tcp/4244 | hubble-timescape tcp/443 | [Hubble CLI](./hubble-cli.md)
timescape | push | tcp/4260 | hubble-timescape tcp/4260 | [Push API](./timescape-push-api.md)
timescape | stream | tcp/4261 | hubble-timescape tcp/4261 | [Stream API](./timescape-stream-api.md)
timescape | ui | tcp/8000 | hubble-timescape tcp/8080 | [Web interface](./timescape-ui.md)
timescape | metrics | tcp/9090 | hubble-timescape tcp/9090 | In this setup metrics are disabled so probably not used
timescape | pprof | tcp/6060 | --- | ---

Pod definition has extra volumes as compared with [no tls mode](./configuration-hubble-timescape-no-tls.md)

```yaml
  - name: tls
    projected:
      defaultMode: 256
      sources:
      - secret:
          items:
          - key: tls.crt
            path: server.crt
          - key: tls.key
            path: server.key
          - key: ca.crt
            path: ca.crt
          name: hubble-timescape-server-certs
```

Full definition

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
              "10.128.1.52"
          ],
          "mac": "5a:00:94:ed:2b:38",
          "default": true,
          "dns": {},
          "gateway": [
              "10.128.1.92"
          ]
      }]
  creationTimestamp: "2026-07-01T07:31:53Z"
  generateName: hubble-timescape-
  labels:
    app.kubernetes.io/name: hubble-timescape
    app.kubernetes.io/part-of: cilium
    apps.kubernetes.io/pod-index: "0"
    controller-revision-hash: hubble-timescape-885ff59b7
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
  resourceVersion: "139890086"
  uid: ce7e609c-b30a-4e76-af75-ee0fef8c74eb
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
      name: kube-api-access-djjq2
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
    - mountPath: /var/lib/hubble-timescape/tls
      name: tls
      readOnly: true
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-djjq2
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
  - name: tls
    projected:
      defaultMode: 256
      sources:
      - secret:
          items:
          - key: tls.crt
            path: server.crt
          - key: tls.key
            path: server.key
          - key: ca.crt
            path: ca.crt
          name: hubble-timescape-server-certs
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
  - name: kube-api-access-djjq2
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
    lastTransitionTime: "2026-07-01T07:32:00Z"
    status: "True"
    type: PodReadyToStartContainers
  - lastProbeTime: null
    lastTransitionTime: "2026-07-01T07:31:53Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2026-07-01T07:32:04Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2026-07-01T07:32:04Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2026-07-01T07:31:53Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: cri-o://c969c32d134c1e4dd1995a8a294332eb404b1a5522e456b3ec29fce5a25bee6d
    image: quay.io/isovalent/clickhouse-server...
    imageID: quay.io/isovalent/clickhouse-server...
    lastState: {}
    name: clickhouse
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2026-07-01T07:31:57Z"
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
      name: kube-api-access-djjq2
      readOnly: true
      recursiveReadOnly: Disabled
  - containerID: cri-o://2035903a28143070996676a38a050b767b789902a00b34f05635bafb494f4148
    image: quay.io/isovalent/hubble-timescape-lite...
    imageID: quay.io/isovalent/hubble-timescape-lite...
    lastState: {}
    name: timescape
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2026-07-01T07:32:00Z"
    volumeMounts:
    - mountPath: /etc/hubble-timescape
      name: config
      readOnly: true
      recursiveReadOnly: Disabled
    - mountPath: /var/lib/hubble-timescape/tls
      name: tls
      readOnly: true
      recursiveReadOnly: Disabled
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-djjq2
      readOnly: true
      recursiveReadOnly: Disabled
  hostIP: 10.10.10.67
  hostIPs:
  - ip: 10.10.10.67
  phase: Running
  podIP: 10.128.1.52
  podIPs:
  - ip: 10.128.1.52
  qosClass: BestEffort
  startTime: "2026-07-01T07:31:53Z"
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
  resourceVersion: "139889232"
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
    port: 443
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