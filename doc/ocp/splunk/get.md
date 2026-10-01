# Splunk - Get Information

[[Back]](./README.md)

## Workflow

- check operator subscription 
- check standalone instances

## Configurable options

```
# iserver get ocp splunk 
  --cluster TEXT   Cluster name
  -v, --view TEXT  [state|res|all]  [default: state]
```

## Example (view:state)

```
# iserver get ocp splunk --cluster bm1

OpenShift Workflow - Splunk Operator - Get Information
======================================================

OpenShift Cluster: bm1

Collecting state...


State
-----
- package   : openshift-marketplace/certified-operators/splunk-operator
- csv       : splunk-operator.v3.1.0
- resources : V



Splunk Custom Resources
-----------------------
- standalone          : 1
- cluster master      : 0
- cluster manager     : 0
- indexer cluster     : 0
- license manager     : 0
- license master      : 0
- monitoring console  : 0
- search head cluster : 0


View: state (def), res, all
```

## Example (view:res)

```
# iserver get ocp splunk --cluster bm1 -v res

OpenShift Workflow - Splunk Operator - Get Information
======================================================

OpenShift Cluster: bm1

Collecting state...


Splunk Custom Resources
-----------------------
- standalone          : 1
- cluster master      : 0
- cluster manager     : 0
- indexer cluster     : 0
- license manager     : 0
- license master      : 0
- monitoring console  : 0
- search head cluster : 0


+----+-----------------+-------+-----+-----+---------+-------+----------------------------------------------------------------------------+
| ID | Standalone      | Ready | Pod | PVC | Service | Route | URL                                                                        |
+----+-----------------+-------+-----+-----+---------+-------+----------------------------------------------------------------------------+
| 1  | splunk-operator | V     | V   | 2/2 | V       | 1/1   | http://splunk-inst1-standalone-service-splunk-operator.apps.bm1.domain.com | 
|    | inst1           |       |     |     |         |       |                                                                            | 
+----+-----------------+-------+-----+-----+---------+-------+----------------------------------------------------------------------------+

View: state (def), res, all
```

[[Back]](./README.md)