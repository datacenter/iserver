# VAST CSI - Operator

[[Back]](../README.md) [[iserver-way]](../create_operator.md) [[Next]](./driver.md)

The VAST Operator provides CSI driver for the VAST Data storage system configuration via custom resources
- [VastCSIDriver](./driver.md)
- [VastCluster](./cluster.md)
- [VastStorage](./storage.md)

## Namespace

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: vast-csi
~~~

## Operator Group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: vast-operator-group
  namespace: vast-csi
spec:
  targetNamespaces:
  - vast-csi
  upgradeStrategy: Default
~~~

## Subscription

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: vast-csi-operator
  namespace: vast-csi
spec:
  channel: stable
  installPlanApproval: Automatic
  name: vast-csi-operator
  source: certified-operators
  sourceNamespace: openshift-marketplace
~~~

## Expected outcome

![OperatorCreate](../../images/vast/operator_create.png)

```
$ oc get all -n vast-csi
NAME                                                       READY   STATUS    RESTARTS   AGE
pod/vast-csi-operator-controller-manager-8db976d65-4tslj   2/2     Running   0          20s

NAME                                                           TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/vast-csi-operator-controller-manager-metrics-service   ClusterIP   172.30.29.16   <none>        8443/TCP   21s

NAME                                                   READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/vast-csi-operator-controller-manager   1/1     1            1           20s

NAME                                                             DESIRED   CURRENT   READY   AGE
replicaset.apps/vast-csi-operator-controller-manager-8db976d65   1         1         1       20s
```

[[Back]](../README.md) [[iserver-way]](../create_operator.md) [[Next]](./driver.md)