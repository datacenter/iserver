# Cisco Intersight Plugin - Enable ui plugin

[[Back]](./README.md) [[Next]](./register.md) [[kb]](./kb/ui_plugin.md) [[disable]](./disable_plugin.md)

## Workflow

Checks
- operator should be [installed](./create_operator.md)
- instance should be [created](./create_instance.md)

Action
- patch `console.operator` object with `intersight-plugin` enabled

## Expected outcome

![Enable](../images/intersight/plugin_menu.png)

## Configurable options

```
# iserver set ocp intersight --mode ui
  --cluster TEXT     Cluster Name
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp intersight --cluster bm1 --mode ui

OpenShift Workflow - Cisco Intersight Operator - Enable UI plugin
=================================================================

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
  - intersight-plugin
~~~
Console [cluster] patched

Completed tasks
- Cisco intersight ui plugin enabled
```

[[Back]](./README.md) [[Next]](./register.md) [[kb]](./kb/ui_plugin.md) [[disable]](./disable_plugin.md)