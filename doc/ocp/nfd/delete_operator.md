# Node Feature Discover Operator - Delete Operator

## Workflow

- delete node feature discover instance
- delete operator subscription
- delete operator group
- delete namespace

## Requirements

None

## Configurable options

```
# iserver delete ocp nfd --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp nfd --cluster bm1

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