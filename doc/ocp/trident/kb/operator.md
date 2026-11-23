# Trident - Install operator

[[Back]](../README.md) [[Next]](./instance.md) [[iserver-way]](../create_operator.md)

## Namespace

> [!NOTE]
> Trident operator should be installed in `openshift-operators` namespace that should already exist

## Operator Group

> [!NOTE]
> Trident operator does not required dedicated operator group and uses `global-operators`.

## Subscription

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: trident-operator
  namespace: openshift-operators
spec:
  channel: stable
  installPlanApproval: Automatic
  name: trident-operator
  source: certified-operators
  sourceNamespace: openshift-marketplace
~~~

## Expected outcome

![OperatorCreate](../../images/trident/operator_create.png)

```
$ oc get all -n openshift-operators
NAME                                                   READY   STATUS    RESTARTS   AGE
pod/trident-operator-5f4b49d487-cppq8                  1/1     Running   0          8m42s

NAME                                              READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/trident-operator                  1/1     1            1           8m42s

NAME                                                         DESIRED   CURRENT   READY   AGE
replicaset.apps/trident-operator-5f4b49d487                  1         1         1       8m42s
```

[[Back]](../README.md) [[Next]](./instance.md) [[iserver-way]](../create_operator.md)