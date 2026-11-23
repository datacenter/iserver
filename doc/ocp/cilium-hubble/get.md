# Cilium Timescape - Get

## Workflow

- check timescape feature

## Requirements

None

## Configurable options

```
# iserver get ocp cilium timescape 
  --cluster TEXT     Cluster Name
```

## Example

```
# iserver get ocp cilium timescape --cluster bm1

OpenShift Workflow - Cilium - Get Timescape
===========================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "cilium",
    "package": "clife",
    "operator-name": "cilium-operator",
    "agent-name": "cilium"
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


Cilium configuration
--------------------

~~~
enterprise:
  featureGate:
    approved:
    - CNIChainingMode
    - HubbleTimescape
    strict: false
hubble:
  enabled: true
  export:
    timescape:
      tls:
        mtls:
          enabled: true
  relay:
    enabled: false
  timescape:
    enabled: true
    ingester:
      k8sImporter:
        enabled: true
    static:
      exporter:
        enabled: true
    useStreamAPI: true
  tls:
    enabled: true

~~~

+----+--------------------+-------+---------+--------------------+--------+-------+--------------+-----+-----+----------+
| ID | Pod                | Ready | Status  | Condition          | Age    | Node  | IP           | Net | Svc | Restarts |
+----+--------------------+-------+---------+--------------------+--------+-------+--------------+-----+-----+----------+
| 1  | cilium             | 2/2   | Running | Initialized: ✓     | 17h11m | bm1-2 | 10.128.0.247 | 1   | 2   | 0        | 
|    | hubble-timescape-0 |       |         | PodScheduled: ✓    |        |       |              |     |     |          | 
|    |                    |       |         | ContainersReady: ✓ |        |       |              |     |     |          | 
|    |                    |       |         | Ready: ✓           |        |       |              |     |     |          | 
+----+--------------------+-------+---------+--------------------+--------+-------+--------------+-----+-----+----------+

+----+---------------------------+-----------+------------+-------------+----------+--------+
| ID | Service                   | Type      | Cluster IP | External IP | Port     | Age    |
+----+---------------------------+-----------+------------+-------------+----------+--------+
| 1  | cilium                    | ClusterIP | 172.30.6.5 | ---         | 4260/TCP | 17h11m | 
|    | hubble-timescape          |           |            |             | 4261/TCP |        | 
|    |                           |           |            |             | 443/TCP  |        | 
|    |                           |           |            |             | 8080/TCP |        | 
|    |                           |           |            |             | 9090/TCP |        | 
|    |                           |           |            |             | 8001/TCP |        | 
+----+---------------------------+-----------+------------+-------------+----------+--------+
| 2  | cilium                    | ClusterIP | ---        | ---         |          | 17h11m | 
|    | hubble-timescape-headless |           |            |             |          |        | 
+----+---------------------------+-----------+------------+-------------+----------+--------+

+----+---------------------------+----------+----------------------+-----------------------+
| ID | Endpoint                  | Headless | Address              | Port                  |
+----+---------------------------+----------+----------------------+-----------------------+
| 1  | cilium                    | ✗        | 10.128.0.247 [bm1-2] | TCP/4261 [stream]     | 
|    | hubble-timescape          |          | 10.128.0.247 [bm1-2] | TCP/8001 [ch-metrics] | 
|    |                           |          | 10.128.0.247 [bm1-2] | TCP/4244 [grpc]       | 
|    |                           |          | 10.128.0.247 [bm1-2] | TCP/9090 [metrics]    | 
|    |                           |          | 10.128.0.247 [bm1-2] | TCP/8080 [ui]         | 
|    |                           |          | 10.128.0.247 [bm1-2] | TCP/4260 [push]       | 
+----+---------------------------+----------+----------------------+-----------------------+
| 2  | cilium                    | ✓        | ---                  | ---                   | 
|    | hubble-timescape-headless |          |                      |                       | 
+----+---------------------------+----------+----------------------+-----------------------+

Timescape summary
- enabled
- resources ready
- ui route: http://hubble-timescape-cilium.apps.bm1.domain.com
```

[[Back]](./README.md)