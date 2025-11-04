# Splunk Operator - Get Information

## Workflow

- check operator subscription 
- check standalone instances

## Requirements

None

## Configurable options

```
# iserver get ocp splunk 
  --cluster TEXT                Cluster Name
```

## Non-configurable defaults

```
{
    "namespace": "splunk-operator",
    "name": "splunk-operator"
}
```

## Example

```
# iserver get ocp splunk --cluster bm1

OpenShift Workflow - Splunk Operator - Get Information
======================================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok



Operator
--------
- subscription          : splunk-operator/splunk-operator
- package               : openshift-marketplace/certified-operators/splunk-operator
- channel               : stable
- install plan          : splunk-operator/install-xd8w9
- install plan approved : ✓
- installed csv         : splunk-operator.v3.0.0
- latest_csv            : ✓


+----+-----------------+-------+-----+-----+---------+-------+--------------------------------------------------------------------------+
| ID | Standalone      | Ready | Pod | PVC | Service | Route | URL                                                                      |
+----+-----------------+-------+-----+-----+---------+-------+--------------------------------------------------------------------------+
| 1  | splunk-operator | ✓     | ✓   | 2/2 | ✓       | 1/1   | http://splunk-s1-standalone-service-splunk-operator.apps.bm1.domain.com |
|    | s1              |       |     |     |         |       | (admin, password)                                                        |
+----+-----------------+-------+-----+-----+---------+-------+--------------------------------------------------------------------------+
```

[[Back]](./README.md)