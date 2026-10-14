# NMState Operator - Delete Instance

[[Back]](./README.md)

## Workflow

- delete NodeNetworkConfigurationPolicy objects
- delete nmstate instance
- wait for instance resources to be deleted
## Requirements

None

## Configurable options

```
# iserver delete ocp nmstate --mode instance
  --cluster TEXT         Cluster Name
```

## Example

```
# iserver delete ocp nmstate --cluster bm1 --mode instance

OpenShift Workflow - NMState Operator - Delete Instance
=======================================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-nmstate/kubernetes-nmstate-operator
- package               : openshift-marketplace/redhat-operators/kubernetes-nmstate-operator
- channel               : stable
- install plan          : openshift-nmstate/install-5cl5n
- install plan approved : ✓
- installed csv         : kubernetes-nmstate-operator.4.21.0-202609301335
- latest_csv            : ✓


Delete Node Network Configuration Policies
------------------------------------------
- no nncp found

Delete NMState Instance
-----------------------
- name: nmstate
- wait for no nmstate instance
Wait for no Deployment openshift-nmstate/nmstate-console-plugin [timeout:180s]
Wait for no Deployment openshift-nmstate/nmstate-metrics [timeout:180s]
Wait for no Deployment openshift-nmstate/nmstate-webhook [timeout:180s]
Wait for no DaemonSet openshift-nmstate/nmstate-handler [timeout:180s]
Subscription nmstate resources gone

Completed tasks
- nncp crds deleted
- nmstate instance deleted

+----+---------+---------+-----------------+---------+---------+--------------+
| ID | Target  | Scope   | Workflow        | Changes | Success | Duration [s] |
+----+---------+---------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | nmstate | delete instance | 1       | ✓       | 3            | 
+----+---------+---------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)