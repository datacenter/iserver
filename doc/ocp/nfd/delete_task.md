# Node Feature Discovery Operator - Delete via Task

## Input

```
[
    {
        "nfd": {
            "operator": {
                "filename": "xyz"
            }
        }
    }
]
```

Notes:
- [operator](./delete_operator.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters e.g. filename may be silently ignored

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
# iserver delete ocp task --file C:\tmp\task.json --cluster bm1             
OpenShift Cluster: bm1

OpenShift Workflow - Node Feature Discover Operator - Delete Operator
=====================================================================

OpenShift Cluster: bm1


Operator
--------
- subscription          : openshift-nfd/nfd
- package               : openshift-marketplace/redhat-operators/nfd
- channel               : stable
- install plan          : openshift-nfd/install-gt7fs
- install plan approved : ✓
- installed csv         : nfd.4.21.0-202603230446
- latest_csv            : ✓


Delete NodeFeatureDiscovery
---------------------------
- namespace: openshift-nfd
- name: nfd-instance
- deleted
- wait for no NodeFeatureDiscovery openshift-nfd/nfd-instance [timeout:60s]

Delete Subscription
-------------------
- subscription: openshift-nfd/nfd
- checking cluster service version...
- csv found and will be deleted: openshift-nfd/nfd.4.21.0-202603230446
- wait for no subscription
- check cluster service version: openshift-nfd/nfd.4.21.0-202603230446
- wait for no csv
Wait for no deployment openshift-nfd/nfd-master (optional: False, timout: 180s)...
Wait for no deployment openshift-nfd/nfd-controller-manager (optional: False, timout: 180s)...
Wait for no daemonset (optional: False, timout: 180s)...
Subscription nfd resources gone

Delete Operator Group
---------------------
- namespace: openshift-nfd
- name: nfd-operator-group
- wait for no operator group

Namespace [openshift-nfd] resources
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
- name: openshift-nfd
- wait for no namespace

Completed tasks
- NFD instances deleted
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md)