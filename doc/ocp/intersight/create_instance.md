# Cisco Intersight Plugin - Create instance

[[Back]](./README.md) [[Next]](./enable_plugin.md) [[kb]](./kb/instance.md)

## Workflow

Checks
- operator should be [installed](./create_operator.md)

Action
- create CiscoIntersight resource with user-defined OsDiscoveryToolInstall value (default: false)
- instance name defaults to 'cisco-intersight'
- if instance already exists, update `spec:OsDiscoveryToolInstall`
- wait for instance ready state
- wait for resources

> [!CAUTION]
> Max one CiscoIntersight object expected

## Expected outcome

![Instance](../images/intersight/instance_create.png)

## Configurable options

```
# iserver set ocp intersight --mode instance
  --cluster TEXT     Cluster Name
  --ucs-tool         Enable OsDiscoveryToolInstall
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp intersight --cluster bm1 --mode instance --ucs-tool

OpenShift Workflow - Cisco Intersight Operator - Define Instance
================================================================

OpenShift Cluster: bm1
Subscription cisco-intersight found

Create CiscoIntersight
----------------------
- namespace: cisco-intersight
- name: cisco-intersight

~~~
apiVersion: intersight.cisco.com/v1
kind: CiscoIntersight
metadata:
  name: cisco-intersight
  namespace: cisco-intersight
spec:
  OsDiscoveryToolInstall: true
~~~
CiscoIntersight [cisco-intersight/cisco-intersight] created
- wait for CiscoIntersight cisco-intersight/cisco-intersight [timeout:60s]
Wait for deployment cisco-intersight/cisco-intersight-operator ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment cisco-intersight/cisco-intersight-api ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment cisco-intersight/intersight-plugin-console-plugin ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for daemonset cisco-intersight/ucs-serial-discover ready (optional: False, timeout: 600s)...
Wait for daemonset cisco-intersight/ucs-tool ready (optional: True, timeout: 600s)...
Subscription intersight ready

Completed tasks
- Cisco intersight ready
```

[[Back]](./README.md) [[Next]](./enable_plugin.md) [[kb]](./kb/instance.md)