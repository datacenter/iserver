# Intersight Open Telemetry - Get instances resources

## Workflow

- check namespace
- get secret
- get configmaps
- get deployment
- get service
- get service monitor

## Requirements

None

## Configurable options

```
# iserver get ocp iotel 
  --cluster TEXT     Cluster Name
  --verbose          Verbose output
  --no-confirm       Confirmation mode
```

## Example

```
# iserver get ocp iotel --cluster bm1 


OpenShift Workflow - Intersight Open Telemetry (iotel) - Get instance resources
===============================================================================

OpenShift Cluster: bm1

+----+------------------+-------+
| ID | Secret           | Owner |
+----+------------------+-------+
| 1  | intersight-otel  | ---   | 
|    | intersight-iac   |       | 
+----+------------------+-------+

+------------------------------------------+------+------+
| Config Map                               | Data | Age  |
+------------------------------------------+------+------+
| intersight-otel/intersight-iac           | 1    | 1h5m | 
| intersight-otel/kube-root-ca.crt         | 1    | 1h5m | 
| intersight-otel/openshift-service-ca.crt | 1    | 1h5m | 
| intersight-otel/otel-iac                 | 1    | 1h5m | 
+------------------------------------------+------+------+

+----+-----------------+-------+------------+-----------+------+
| ID | Deployment      | Ready | Up-To-Date | Available | Age  |
+----+-----------------+-------+------------+-----------+------+
| 1  | intersight-otel | 1/1   | 1          | 1         | 1h5m | 
|    | instance-iac    |       |            |           |      | 
+----+-----------------+-------+------------+-----------+------+

+----+---------------------------------+-------+---------+--------------------+------+-------+--------------+-----+-----+--------------+
| ID | Pod                             | Ready | Status  | Condition          | Age  | Node  | IP           | Net | Svc | Restarts     |
+----+---------------------------------+-------+---------+--------------------+------+-------+--------------+-----+-----+--------------+
| 1  | intersight-otel                 | 2/2   | Running | Initialized: ✓     | 1h5m | bm1-3 | 10.128.4.246 | 1   | 1   | 1 (1h5m ago) | 
|    | instance-iac-7d7859b78f-crz8c   |       |         | PodScheduled: ✓    |      |       |              |     |     |              | 
|    |                                 |       |         | ContainersReady: ✓ |      |       |              |     |     |              | 
|    |                                 |       |         | Ready: ✓           |      |       |              |     |     |              | 
+----+---------------------------------+-------+---------+--------------------+------+-------+--------------+-----+-----+--------------+

+----+-----------------+-----------+----------------+--------------------------------+--------------------------+---------------------------------+------+
| ID | Service         | Type      | IP             | Port                           | Selector                 | POD                             | Age  |
+----+-----------------+-----------+----------------+--------------------------------+--------------------------+---------------------------------+------+
| 1  | intersight-otel | ClusterIP | 172.30.128.234 | TCP/2112 [prometheus-exporter] | app:instance-iac         | instance-iac-7d7859b78f-crz8c   | 1h5m | 
|    | otel-iac        |           |                |                                | component:otel-collector |                                 |      | 
+----+-----------------+-----------+----------------+--------------------------------+--------------------------+---------------------------------+------+

+----+-----------------+-------+-----------------+-------------------------------------------------+--------+
| ID | Service Monitor | Owner | Endpoint        | POD                                             | Target |
+----+-----------------+-------+-----------------+-------------------------------------------------+--------+
| 1  | intersight-otel | ---   | intersight-otel | intersight-otel/instance-iac-7d7859b78f-crz8c   | ✓      | 
|    | otel-iac        |       | otel-iac        |                                                 |        | 
+----+-----------------+-------+-----------------+-------------------------------------------------+--------+
```

[[Back]](./README.md)