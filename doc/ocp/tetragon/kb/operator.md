# Tetragon - Operator

[[Back]](../README.md) [[iserver-way]](../create_operator.md)

Tetragon Enterprise in an OpenShift cluster is installed as operator with the Operator Lifecycle Manager (OLM) framework.

> [!NOTE]
> Tetragon can be installed independently of Cilium CNI

![Resources](../../images/tetragon/resources.png)

## Namespace

```yaml
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/user-monitoring: 'true'
  name: tetragon
```

## Catalog Source

> [!CAUTION]
> CatalogSource [required](https://docs.isovalent.com/iep/latest/tetragon/installation/openshift.html) to install Tetragon operator

## Operator Group

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: tetragon
  namespace: tetragon
spec:
  upgradeStrategy: Default
```

## Subscription

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  labels:
    operators.coreos.com/tetragon-operator.tetragon: ''
  name: tetragon-operator
  namespace: tetragon
spec:
  channel: v1.18
  installPlanApproval: Automatic
  name: tetragon-operator
  source: tetragon-catalog
  sourceNamespace: tetragon
```

## Expected outcome

![OperatorCreate](../../images/tetragon/operator_create.png)

```
$ oc get all -n tetragon
NAME                                                                  READY   STATUS      RESTARTS   AGE
pod/tetragon-9hwbf                                                    1/1     Running     0          73s
pod/tetragon-catalog-s8rjs                                            1/1     Running     0          5m36s
pod/tetragon-d2455                                                    1/1     Running     0          73s
pod/tetragon-gwnbs                                                    1/1     Running     0          73s
pod/tetragon-operator-646c4b6845-th7ld                                1/1     Running     0          74s

NAME                       TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)     AGE
service/tetragon-catalog   ClusterIP   172.244.28.46   <none>        50051/TCP   5m36s

NAME                      DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
daemonset.apps/tetragon   3         3         3       3            3           kubernetes.io/os=linux   73s

NAME                                READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/tetragon-operator   1/1     1            1           74s

NAME                                           DESIRED   CURRENT   READY   AGE
replicaset.apps/tetragon-operator-646c4b6845   1         1         1       74s
```

[[Back]](../README.md) [[iserver-way]](../create_operator.md)