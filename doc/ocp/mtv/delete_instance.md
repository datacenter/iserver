# Migration Toolkit for Virtualization - Delete Forklift Controller Instance

## Workflow

- delete forklift controller instance

## Requirements

- mtv operator [installed](./create_operator.md)
- [no plan](./delete_plan.md)
- [no storage map](./delete_storage_map.md)
- [no network map](./delete_network_map.md)
- [no provider](./delete_provider.md)

## Configurable options

```
# iserver delete ocp mtv --mode instance
  --cluster TEXT                  Cluster Name
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver delete ocp mtv --cluster bm1 --mode instance

OpenShift Workflow - Migration Toolkit for Virtualization Operator - Delete Forklift Controller Instance
========================================================================================================

OpenShift Cluster: bm1

Mtv Operator
- subscription: openshift-mtv/mtv-operator
- channel: release-v2.10
- csv: mtv-operator.v2.10.3
- ready

No providers found

No network maps found

No storage maps found

No migration plans

No migrations


Delete Forklift Controller
--------------------------
- namespace: openshift-mtv
- name: forklift-controller

Forklift controller instance deleted

Wait for no forklift controller instance...
Wait for no forklift controller instance resources...
Wait for deployments deleted (optional: False)...
- openshift-mtv/forklift-api
- openshift-mtv/forklift-cli-download
- openshift-mtv/forklift-controller
- openshift-mtv/forklift-ova-proxy
- openshift-mtv/forklift-ui-plugin
- openshift-mtv/forklift-validation
- openshift-mtv/forklift-volume-populator-controller

Completed tasks
- forklift controller instance deleted
```

[[Back]](./README.md)