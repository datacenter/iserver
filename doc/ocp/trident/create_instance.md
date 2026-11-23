# Trident - Create Instance

[[Back]](./README.md) [[Next]](./create_all.md) [[Prev]](./create_operator.md)

## HowTo

```
# iserver set ocp trident --cluster bm1 --mode instance --no-confirm

# iserver set ocp trident --mode instance
  --cluster TEXT     Cluster Name
  --filename TEXT    TridentOrchestrator CRD
  --no-confirm       Confirmation mode
```

## Workflow

- create TridentOrchestrator based on package default or user-provided file

## Requirements

Trident operator must be [created](./create_operator.md)

## Expected outcome

![InstanceCreate](../images/trident/instance_create.png)

## Example

```
# iserver set ocp trident --cluster bm1 --mode instance --no-confirm

OpenShift Workflow - Trident Operator - Create Instance
=======================================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-operators/trident-operator
- package               : openshift-marketplace/certified-operators/trident-operator
- channel               : stable
- install plan          : openshift-operators/install-hv429
- install plan approved : V
- installed csv         : trident-operator.v26.2.0
- latest_csv            : V


Create TridentOrchestrator
--------------------------
- name: trident

~~~
apiVersion: trident.netapp.io/v1
kind: TridentOrchestrator
metadata:
  name: trident
spec:
  IPv6: false
  debug: true
  imagePullSecrets: []
  imageRegistry: ''
  namespace: trident
  nodePrep: []
  silenceAutosupport: false
~~~
TridentOrchestrator [trident] created
- wait for TridentOrchestrator trident [timeout:60s]
Wait for deployment openshift-operators/trident-operator ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment trident/trident-controller ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for daemonset trident/trident-node-linux ready (optional: False, timeout: 600s)...
Subscription trident ready

Completed tasks
- Trident orchestrator instance created

+----+---------+---------+-----------------+---------+---------+--------------+
| ID | Target  | Scope   | Workflow        | Changes | Success | Duration [s] |
+----+---------+---------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | trident | create instance | 1       | V       | 359          | 
+----+---------+---------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[Next]](./create_all.md) [[Prev]](./create_operator.md)