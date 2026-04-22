# Cisco Intersight Plugin - Delete via Task

[[Back]](./README.md) [[Next]](../kb/operator.md) [[Create Task]](./create_task.md)

## Input

```
[
    {
        "intersight": {
            "operator": {},
            "instance": {
                "ucs-tool": true
            },
            "ui": {},
            "register": {
                "client-id": "AAAA",
                "client-secret": "BBBB",
                "location": "us"
            }
        }
    }
]
```

Notes:
- [operator](./delete_operator.md), [instance](./delete_instance.md) and [ui](./delete_plugin.md) triggers workflow execution with input parameter
- register section is ignored in delete task
- the same task definition can be reused for [create](./create_task.md)

## Requirements

None

## Configurable options

```
# iserver delete ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example

```
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm


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

OpenShift Workflow - Cisco Intersight Operator - Delete Instance
================================================================

OpenShift Cluster: bm1
Subscription cisco-intersight found

OpenShift Workflow - Cisco Intersight Operator - Disable UI plugin
==================================================================

Subscription cisco-intersight found
Intersight ui plugin already disabled

Delete CiscoIntersight
----------------------
- namespace: cisco-intersight
- name: cisco-intersight
- deleted
- wait for no CiscoIntersight cisco-intersight/cisco-intersight [timeout:60s]
- wait for Deployment cisco-intersight/cisco-intersight-api [timeout:180s]
- wait for Deployment cisco-intersight/intersight-plugin-console-plugin [timeout:180s]
- wait for DaemonSet cisco-intersight/ucs-serial-discover [timeout:180s]
Subscription intersight resources gone

Completed tasks
- Cisco intersight instance deleted

OpenShift Workflow - Cisco Intersight Operator - Delete Operator
================================================================

OpenShift Cluster: bm1

Operator
- subscription          : cisco-intersight/cisco-intersight
- package               : openshift-marketplace/certified-operators/cisco-intersight
- channel               : stable
- install plan          : cisco-intersight/install-x6k55
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

[[Back]](./README.md) [[Next]](../kb/operator.md) [[Create Task]](./create_task.md)