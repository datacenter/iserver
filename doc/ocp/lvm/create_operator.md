# LVM Storage - Create operator

[[Back]](./README.md) [[kb]](./kb/operator.md) [[cluster]](./create_cluster.md)

## Workflow

- create openshift-storage namespace with extra labels
- create operator group
- create subscription with user controlled channel or defaultChannelName

```
    labels['openshift.io/cluster-monitoring'] = 'true'
    labels['pod-security.kubernetes.io/enforce'] = 'privileged'
    labels['pod-security.kubernetes.io/audit'] = 'privileged'
    labels['pod-security.kubernetes.io/warn'] = 'privileged'
```

## Requirements

None

## Configurable options

```
# iserver set ocp lvm --mode operator
  --cluster TEXT                  Cluster Name
  --channel TEXT                  Operator channel  [default: __default__]
  --no-confirm                    Confirmation mode
```

## Expected outcome

![OperatorCreate](../images/lvm/operator_create.png)

## Example

```
# iserver set ocp lvm --cluster bm1 --mode operator --no-confirm


OpenShift Workflow - LVM - Create Operator
==========================================

OpenShift Cluster: bm1
Subscription not found lvms-operator

Create Namespace
----------------
- name: openshift-storage

~~~
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: 'true'
    pod-security.kubernetes.io/audit: privileged
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/warn: privileged
  name: openshift-storage
~~~
Namespace [openshift-storage] created
Wait for namespace [timeout:60]...

Check labels
- openshift.io/cluster-monitoring:true found
- pod-security.kubernetes.io/enforce:privileged found
- pod-security.kubernetes.io/audit:privileged found
- pod-security.kubernetes.io/warn:privileged found

Create OperatorGroup
--------------------
- namespace: openshift-storage
- name: lvm-operator-group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: lvm-operator-group
  namespace: openshift-storage
spec:
  targetNamespaces:
  - openshift-storage
  upgradeStrategy: Default
~~~
OperatorGroup [openshift-storage/lvm-operator-group] created
- wait for OperatorGroup openshift-storage/lvm-operator-group [timeout:60s]

Create Subscription
-------------------
Subscription: openshift-storage/lvms
Source: openshift-marketplace/redhat-operators/lvms-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: stable-4.18
- CSV [lvms-operator.v4.18.4]
- CSV Display name [LVM Storage]
- CVS Version [4.18.4]
- CSV Provider [{'name': 'Red Hat'}]
- CSV Maturity [alpha]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: lvms
  namespace: openshift-storage
spec:
  channel: stable-4.18
  installPlanApproval: Automatic
  name: lvms-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-9t9vh
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployment openshift-storage/lvms-operator ready (optional: False, allow zero replicas: False, timeout: 600s)...
Subscription lvm ready

Operator
- subscription          : openshift-storage/lvms
- package               : openshift-marketplace/redhat-operators/lvms-operator
- channel               : stable-4.18
- install plan          : openshift-storage/install-9t9vh
- install plan approved : ✓
- installed csv         : lvms-operator.v4.18.4
- latest_csv            : ✓


Completed tasks
- Namespace created
- Operator Group created
- Subscription created

+----+---------+-------+-----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow        | Changes | Success | Duration [s] |
+----+---------+-------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | lvm   | create operator | 3       | ✓       | 23           | 
+----+---------+-------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[kb]](./kb/operator.md) [[cluster]](./create_cluster.md)