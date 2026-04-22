# Cisco Intersight Plugin - Disable ui plugin

[[Back]](./README.md) [[Next]](./delete_all.md) [[kb]](./kb/ui_plugin.md) [[enable]](./enable_plugin.md)

## Workflow

Checks
- operator should be [installed](./create_operator.md)
- instance should be [created](./create_instance.md)

Action
- patch `console.operator` object without `intersight-plugin`

## Configurable options

```
# iserver delete ocp intersight --mode ui
  --cluster TEXT     Cluster Name
  --no-confirm       Confirmation mode
```

## Example

```
# iserver delete ocp intersight --cluster bm1 --mode ui


OpenShift Workflow - Cisco Intersight Operator - Disable UI plugin
==================================================================

OpenShift Cluster: bm1
Subscription cisco-intersight found

Patch Console
-------------
- name: cluster

~~~
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
spec:
  plugins:
  - networking-console-plugin
  - monitoring-plugin
~~~
Console [cluster] patched

Completed tasks
- Cisco intersight ui plugin disabled
```

[[Back]](./README.md) [[Next]](./delete_all.md) [[kb]](./kb/ui_plugin.md) [[enable]](./enable_plugin.md)