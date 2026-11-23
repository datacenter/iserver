# MetalLB - Operator

[[Back]](../README.md) [[iserver-way]](../create_operator.md)

## Step 1: Namespace

```
apiVersion: metallb.io/v1beta1
kind: MetalLB
metadata:
  name: metallb
  namespace: metallb-system
spec:
  bgpBackend: frr
```

## Step 2: Operator Group

```
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: metallb-system
  namespace: metallb-system
spec:
  upgradeStrategy: Default
```

## Step 3: Subscription

```
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: metallb-operator
  namespace: metallb-system
spec:
  channel: stable
  installPlanApproval: Automatic
  name: metallb-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```

## Expected outcome

![OperatorCreate](../../images/metallb/operator_create.png)

[[Back]](../README.md) [[iserver-way]](../create_operator.md)