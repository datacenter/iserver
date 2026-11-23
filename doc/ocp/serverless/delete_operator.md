# Serverless - Delete Operator

## Workflow

- delete operator subscription
- delete operator group
- delete namespace

## Requirements

None

## Configurable options

```
# iserver delete ocp serverless --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp serverless --cluster bm1

OpenShift Workflow - Serverless Operator - Delete Operator
==========================================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-serverless/serverless-operator
- package               : openshift-marketplace/redhat-operators/serverless-operator
- channel               : stable
- install plan          : openshift-serverless/install-jskgp
- install plan approved : V
- installed csv         : serverless-operator.v1.37.1
- latest_csv            : V


Delete Subscription
-------------------
- subscription: openshift-serverless/serverless-operator
- checking cluster service version...
- csv found and will be deleted: openshift-serverless/serverless-operator.v1.37.1
- wait for no subscription
- check cluster service version: openshift-serverless/serverless-operator.v1.37.1
- wait for no csv
- wait for no Deployment openshift-serverless/knative-openshift [timeout:180s]
- wait for no ReplicaSet openshift-serverless/knative-openshift-7fb87c6c7 [timeout:180s]
- wait for no Pod openshift-serverless/knative-openshift-7fb87c6c7-l8brg [timeout:180s]
- wait for no Deployment openshift-serverless/knative-openshift-ingress [timeout:180s]
- wait for no ReplicaSet openshift-serverless/knative-openshift-ingress-5db649758c [timeout:180s]
- wait for no Pod openshift-serverless/knative-openshift-ingress-5db649758c-4w76m [timeout:180s]
- wait for no Deployment openshift-serverless/knative-operator-webhook [timeout:180s]
- wait for no ReplicaSet openshift-serverless/knative-operator-webhook-7846c66f9d [timeout:180s]
- wait for no Pod openshift-serverless/knative-operator-webhook-7846c66f9d-9kv22 [timeout:180s]
Subscription serverless resources gone

Delete OperatorGroup
--------------------
- namespace: openshift-serverless
- name: serverless-operator-group
- deleted
- wait for no OperatorGroup openshift-serverless/serverless-operator-group [timeout:60s]

Namespace [openshift-serverless] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- no user defined networks
- no cluster user defined networks

Delete Namespace
----------------
- name: openshift-serverless
- wait for no namespace

Completed tasks
- Subscription deleted
- Operator Group deleted
- Namespace deleted

+----+---------+------------+-----------------+---------+---------+--------------+
| ID | Target  | Scope      | Workflow        | Changes | Success | Duration [s] |
+----+---------+------------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | serverless | delete operator | 4       | V       | 56           | 
+----+---------+------------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)