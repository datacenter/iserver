# Splunk - Delete Standalone Instance

[[Back]](./README.md)

## Workflow

- delete standalone splunk instance selected by name
- wait for instance resources gone
- delete instance route

## Requirements

None

## Configurable options

- Option --instance can be defined mulitple times
- Option --instance value `__all__` selects all instances

```
# iserver delete ocp splunk --mode instance
  --cluster TEXT                  Cluster Name
  --instance TEXT                 Standalone instance name
```

## Example

```
# iserver delete ocp splunk --mode instance --instance __all__

OpenShift Workflow - Splunk Operator - Delete Instance
======================================================

OpenShift Cluster: bm1

Delete splunk instance route
----------------------------
- instance namespace: splunk-operator
- instance name: inst1
- route namespace: splunk-operator
- route name: splunk-inst1-standalone-service

Route deleted

Delete Splunk Standalone Cluster
--------------------------------
- namespace: splunk-operator
- name: inst1

Standalone cluster deleted

Wait for no pod splunk-operator/splunk-inst1-standalone-0...
Wait for no standalone splunk-operator/inst1...

+----+------------+-------+-----+-----+---------+-------+-----+
| ID | Standalone | Ready | Pod | PVC | Service | Route | URL |
+----+------------+-------+-----+-----+---------+-------+-----+
+----+------------+-------+-----+-----+---------+-------+-----+

Completed tasks
- Standalone instance deleted

+----+---------+--------+-----------------+---------+---------+--------------+
| ID | Target  | Scope  | Workflow        | Changes | Success | Duration [s] |
+----+---------+--------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | splunk | delete instance | 2       | ✓       | 38           | 
+----+---------+--------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)