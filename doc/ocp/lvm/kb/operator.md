# LVM Storage - Operator

[[Back]](../README.md) [[cluster]](./cluster.md) [[iserver-way]](../create_operator.md)

## Namespace

```yaml
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: 'true'
    pod-security.kubernetes.io/audit: privileged
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/warn: privileged
  name: openshift-storage
```

## Operator Group

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: lvm-operator-group
  namespace: openshift-storage
spec:
  targetNamespaces:
  - openshift-storage
  upgradeStrategy: Default
```

## Subscription

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: lvms
  namespace: openshift-storage
spec:
  channel: stable-4.21
  installPlanApproval: Automatic
  name: lvms-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```

[[Back]](../README.md) [[cluster]](./cluster.md) [[iserver-way]](../create_operator.md)