# MetalLB - Delete operator

[[Back]](./README.md) [[Create]](./create_operator.md)

## Workflow

- delete subscription 
- delete operator group
- delete namespace
- wait for resources gone

## Example

```
# iserver delete ocp metallb --cluster bm1 --mode operator

OpenShift Workflow - MetalLB Operator - Delete Operator
=======================================================

OpenShift Cluster: bm1


Operator
--------
- subscription          : metallb-system/metallb-operator
- package               : openshift-marketplace/redhat-operators/metallb-operator
- channel               : stable
- install plan          : metallb-system/install-hfq5s
- install plan approved : ✓
- installed csv         : metallb-operator.v4.21.0-202603300221
- latest_csv            : ✓


Delete Subscription
-------------------
- subscription: metallb-system/metallb-operator
- checking cluster service version...
- csv found and will be deleted: metallb-system/metallb-operator.v4.21.0-202603300221
- wait for no subscription
- check cluster service version: metallb-system/metallb-operator.v4.21.0-202603300221
- wait for no csv
- wait for Deployment metallb-system/metallb-operator-controller-manager [timeout:180s]
- wait for ReplicaSet metallb-system/metallb-operator-controller-manager-77c9cccf6 [timeout:180s]
- wait for Pod metallb-system/metallb-operator-controller-manager-77c9cccf6-fzqrq [timeout:180s]
- wait for Deployment metallb-system/metallb-operator-webhook-server [timeout:180s]
- wait for ReplicaSet metallb-system/metallb-operator-webhook-server-688bd755f5 [timeout:180s]
- wait for Pod metallb-system/metallb-operator-webhook-server-688bd755f5-kn8w9 [timeout:180s]
Subscription metallb resources gone

Delete OperatorGroup
--------------------
- namespace: metallb-system
- name: metallb-system
- deleted
- wait for no OperatorGroup metallb-system/metallb-system [timeout:60s]

Namespace [metallb-system] resources
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
- name: metallb-system
- wait for no namespace

Completed tasks
- MetalLB instances deleted
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md) [[Create]](./create_operator.md)