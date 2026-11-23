# Serverless - Install operator

[[Back]](../README.md) [[iserver-way]](../create_operator.md)

## Namespace

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-serverless
~~~

## Operator Group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: serverless-operator-group
  namespace: openshift-serverless
spec:
  upgradeStrategy: Default
~~~

## Subscription

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: serverless-operator
  namespace: openshift-serverless
spec:
  channel: stable
  installPlanApproval: Automatic
  name: serverless-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
~~~

## Expected outcome

![OperatorCreate](../../images/serverless/operator_create.png)

```
$ oc get all -n openshift-serverless

```

[[Back]](../README.md) [[iserver-way]](../create_operator.md)