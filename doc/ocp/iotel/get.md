# Intersight Open Telemetry - Get instance

## Workflow

- collect kubernetes resources in namespace intersight-otel: secret, config map, deployment, service, service monitor
- show instance summary
- use --poller option to get poller config map state
- use --verbose option to get kubernetes resources details

## Requirements

None

## Configurable options

```
# iserver get ocp iotel 
  --cluster TEXT     Cluster Name
  --suffix TEXT      Select suffix by name
  --poller           Show pollers
  --verbose          Verbose output
  --no-confirm       Confirmation mode
```

## Example

```
# iserver get ocp iotel --cluster bm1 

OpenShift Workflow - Intersight Open Telemetry (iotel) - Get instance
=====================================================================

OpenShift Cluster: bm3
Collect resources in namespace intersight-otel
- deployment
- pod
- secret
- config map
- service
- service monitor

+----+-----------------+-------+--------+----------------+--------+-------+---------------------------+--------------+-----------------+
| ID | Deployment      | Ready | Suffix | Intersight API | Poller | Query | Metric                    | OTEL Service | Service Monitor |
+----+-----------------+-------+--------+----------------+--------+-------+---------------------------+--------------+-----------------+
| 1  | intersight-otel | 1/1   | isctl  | ✓              | ✓      | 24    | intersight.advisory.count | ✓            | ✓               |
|    | instance-isctl  |       |        |                |        |       | intersight.alarm.count    |              |                 |
+----+-----------------+-------+--------+----------------+--------+-------+---------------------------+--------------+-----------------+

Output option: --poller, --verbose
```

[[Back]](./README.md)