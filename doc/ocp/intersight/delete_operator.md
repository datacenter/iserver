# Cisco Intersight Plugin - Delete operator

[[Back]](./README.md) [[Next]](./delete_instance.md) [[kb]](./kb/operator.md)

## Workflow

Checks
- operator should be [installed](./create_operator.md)
- [ui plugin](./kb/ui_plugin.md) should be [disabled](./disable_plugin.md)
- intersight instance should be [deleted](./delete_instance.md)

Action
- delete subscription
- wait for resources gone
- delete operator group
- delete namespace

## Example

```
iserver delete ocp intersight --cluster bm1 --mode operator

OpenShift Workflow - Cisco Intersight Operator - Delete Operator
================================================================

OpenShift Cluster: bm1

Operator
- subscription          : cisco-intersight/cisco-intersight
- package               : openshift-marketplace/certified-operators/cisco-intersight
- channel               : stable
- install plan          : cisco-intersight/install-h9zzj
- install plan approved : ✓
- installed csv         : cisco-intersight.v1.0.0
- latest_csv            : ✓


Delete Subscription
-------------------
- subscription: cisco-intersight/cisco-intersight
- checking cluster service version...
- csv found and will be deleted: cisco-intersight/cisco-intersight.v1.0.0
- wait for no subscription
- check cluster service version: cisco-intersight/cisco-intersight.v1.0.0
- wait for no csv
- wait for Deployment cisco-intersight/cisco-intersight-operator [timeout:180s]
- wait for Deployment cisco-intersight/cisco-intersight-api [timeout:180s]
- wait for Deployment cisco-intersight/intersight-plugin-console-plugin [timeout:180s]
- wait for DaemonSet cisco-intersight/ucs-serial-discover [timeout:180s]
- wait for DaemonSet cisco-intersight/ucs-tool [timeout:180s]
Subscription intersight resources gone

Delete OperatorGroup
--------------------
- namespace: cisco-intersight
- name: cisco-intersight
- deleted
- wait for no OperatorGroup cisco-intersight/cisco-intersight [timeout:60s]

Namespace [cisco-intersight] resources
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
- name: cisco-intersight
- wait for no namespace

Completed tasks
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md) [[Next]](./delete_instance.md) [[kb]](./kb/operator.md)