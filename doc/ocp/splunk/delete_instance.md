# Splunk Operator - Delete Standalone Instance

## Workflow

- delete standalone splunk instance selected by name
- wait for instance resources gone
- delete instance route

## Requirements

None

## Configurable options

- Option --instance can be defined mulitple times
- Option --instance value '__all__' selects all instances

```
# iserver delete ocp splunk --mode instance
  --cluster TEXT                  Cluster Name
  --instance TEXT                 Standalone instance name
```

## Non-configurable defaults

```
{
    "namespace": "splunk-operator"
}
```

## Example

```
# iserver delete ocp splunk --mode instance --instance s1

OpenShift Workflow - Splunk Operator - Delete Instance
======================================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok


Delete splunk instance route
----------------------------
- instance namespace: splunk-operator
- instance name: s1
- route namespace: splunk-operator
- route name: splunk-s1-standalone-service
- route already deleted

Delete Splunk Standalone Cluster
--------------------------------
- namespace: splunk-operator
- name: s1

Standalone cluster deleted

Wait for no pod splunk-operator/splunk-s1-standalone-0...
Wait for no standalone splunk-operator/s1...

+----+------------+-------+-----+-----+---------+-------+-----+
| ID | Standalone | Ready | Pod | PVC | Service | Route | URL |
+----+------------+-------+-----+-----+---------+-------+-----+
+----+------------+-------+-----+-----+---------+-------+-----+

Completed tasks
- Standalone instance deleted
```

[[Back]](./README.md)