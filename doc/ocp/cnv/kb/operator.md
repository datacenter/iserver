# Container Virtualization Operator - Install operator

[[Back]](../README.md) [[Next]](./instance.md) [[iserver-way]](../create_operator.md)

Container Virtualization functionalities are implemented via an operator that can be installed using OpenShift Console UI or sequence of objects created via command line (see below)
- Namespace e.g. openshift-cnv
- OperatorGroup in the created namespace
- Subscription in the created namespace

Once operator is installed, [instance](./instance.md) must be created.

## Namespace

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-cnv
~~~

## Operator Group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: cnv-operator-group
  namespace: openshift-cnv
spec:
  targetNamespaces:
  - openshift-cnv
  upgradeStrategy: Default
~~~

## Subscription

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec:
  channel: stable
  installPlanApproval: Automatic
  name: kubevirt-hyperconverged
  source: redhat-operators
  sourceNamespace: openshift-marketplace
~~~

## Expected outcome

![OperatorCreate](../../images/cnv/operator_create.png)

```
$ oc get all -n openshift-cnv
NAME                                                      READY   STATUS    RESTARTS   AGE
pod/aaq-operator-5f8fcf4c95-6rp5z                         1/1     Running   0          2m
pod/cdi-operator-779d4d6b99-6ztdf                         1/1     Running   0          2m1s
pod/cluster-network-addons-operator-7c86f7b694-zkhwf      2/2     Running   0          2m1s
pod/hco-operator-85c475c948-hzskl                         1/1     Running   0          2m2s
pod/hco-webhook-5f5989c8b5-r7b9w                          1/1     Running   0          2m1s
pod/hostpath-provisioner-operator-6dff86844f-4rtxr        1/1     Running   0          2m
pod/hyperconverged-cluster-cli-download-d6854d5b6-5wtgr   1/1     Running   0          2m1s
pod/kubevirt-migration-operator-5b8d596699-kk2jj          1/1     Running   0          2m
pod/ssp-operator-548b9677b7-j48hh                         1/1     Running   0          2m1s
pod/virt-operator-b5cb558d-ctrkb                          1/1     Running   0          2m1s
pod/virt-operator-b5cb558d-rq9pr                          1/1     Running   0          2m1s

NAME                                                      TYPE        CLUSTER-IP        EXTERNAL-IP   PORT(S)    AGE
service/hco-webhook-service                               ClusterIP   172.244.252.69    <none>        4343/TCP   2m2s
service/hostpath-provisioner-operator-service             ClusterIP   172.244.169.153   <none>        9443/TCP   2m2s
service/hyperconverged-cluster-webhook-operator-metrics   ClusterIP   172.244.124.179   <none>        8443/TCP   119s
service/kubevirt-hyperconverged-operator-metrics          ClusterIP   172.244.152.249   <none>        8443/TCP   2m
service/ssp-operator-metrics                              ClusterIP   172.244.164.252   <none>        443/TCP    2m
service/ssp-operator-service                              ClusterIP   172.244.71.128    <none>        9443/TCP   2m2s

NAME                                                  READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/aaq-operator                          1/1     1            1           2m
deployment.apps/cdi-operator                          1/1     1            1           2m1s
deployment.apps/cluster-network-addons-operator       1/1     1            1           2m1s
deployment.apps/hco-operator                          1/1     1            1           2m2s
deployment.apps/hco-webhook                           1/1     1            1           2m1s
deployment.apps/hostpath-provisioner-operator         1/1     1            1           2m
deployment.apps/hyperconverged-cluster-cli-download   1/1     1            1           2m1s
deployment.apps/kubevirt-migration-operator           1/1     1            1           2m
deployment.apps/ssp-operator                          1/1     1            1           2m1s
deployment.apps/virt-operator                         2/2     2            2           2m1s

NAME                                                            DESIRED   CURRENT   READY   AGE
replicaset.apps/aaq-operator-5f8fcf4c95                         1         1         1       2m
replicaset.apps/cdi-operator-779d4d6b99                         1         1         1       2m1s
replicaset.apps/cluster-network-addons-operator-7c86f7b694      1         1         1       2m1s
replicaset.apps/hco-operator-85c475c948                         1         1         1       2m2s
replicaset.apps/hco-webhook-5f5989c8b5                          1         1         1       2m1s
replicaset.apps/hostpath-provisioner-operator-6dff86844f        1         1         1       2m
replicaset.apps/hyperconverged-cluster-cli-download-d6854d5b6   1         1         1       2m1s
replicaset.apps/kubevirt-migration-operator-5b8d596699          1         1         1       2m
replicaset.apps/ssp-operator-548b9677b7                         1         1         1       2m1s
replicaset.apps/virt-operator-b5cb558d                          2         2         2       2m1s
```

[[Back]](../README.md) [[Next]](./instance.md) [[iserver-way]](../create_operator.md)