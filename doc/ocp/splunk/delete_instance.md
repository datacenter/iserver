# Splunk - Delete Standalone Instance

[[Back]](./README.md)

## Workflow

- delete standalone splunk instance selected by name
- wait for instance resources gone
- delete instance route

## Requirements

None

## Configurable options

```
# iserver delete ocp splunk --mode instance
  --cluster TEXT              Cluster name
  --name TEXT                 Standalone instance name
  --no-confirm                Confirmation mode
```

## Example

```
# iserver delete ocp splunk --cluster bm1 --mode instance --name inst1


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

Delete Standalone
-----------------
- namespace: splunk-operator
- name: inst1
- deleted
Wait for no Pod splunk-operator/splunk-inst1-standalone-0 [timeout:300s]
Wait for no Standalone splunk-operator/inst1 [timeout:60s]

Completed tasks
- Standalone instance deleted

+----+---------+--------+-----------------+---------+---------+--------------+
| ID | Target  | Scope  | Workflow        | Changes | Success | Duration [s] |
+----+---------+--------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | splunk | delete instance | 2       | ✓       | 38           | 
+----+---------+--------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)