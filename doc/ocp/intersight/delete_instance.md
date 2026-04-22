# Cisco Intersight Plugin - Delete instance

[[Back]](./README.md) [[Next]](./disable_plugin.md) [[kb]](./kb/instance.md)

## Workflow

Checks
- operator should be [installed](./create_operator.md)

Action
- delete CiscoIntersight resource if found
- wait for resources gone

## Configurable options

```
# iserver delete ocp intersight --mode instance
  --cluster TEXT     Cluster Name
```

## Example

```
iserver delete ocp intersight --cluster bm1 --mode instance

OpenShift Workflow - Cisco Intersight Operator - Delete Instance
================================================================

OpenShift Cluster: bm1
Subscription cisco-intersight found

Delete CiscoIntersight
----------------------
- namespace: cisco-intersight
- name: intersight-resource
- deleted
- wait for no CiscoIntersight cisco-intersight/intersight-resource [timeout:60s]
- wait for Deployment cisco-intersight/cisco-intersight-api [timeout:180s]
- wait for Deployment cisco-intersight/intersight-plugin-console-plugin [timeout:180s]
- wait for DaemonSet cisco-intersight/ucs-serial-discover [timeout:180s]
- wait for DaemonSet cisco-intersight/ucs-tool [timeout:180s]
Subscription intersight resources gone

Completed tasks
- Cisco intersight instance deleted
```

[[Back]](./README.md) [[Next]](./disable_plugin.md) [[kb]](./kb/instance.md)