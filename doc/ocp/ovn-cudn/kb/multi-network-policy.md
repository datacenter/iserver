# MultiNetworkPolicy

[[Back]](../README.md)

The multi-network policy API, which is provided by the `MultiNetworkPolicy` custom resource definition
(CRD) in the k8s.cni.cncf.io API group, is compatible with an OVN-Kubernetes secondary network.

It is disabled by default

```yaml
$ oc get network.operator cluster -o yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  ...
  useMultiNetworkPolicy: false
```

Enable procedure

```yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  useMultiNetworkPolicy: true
```

```
$ oc patch network.operator.openshift.io cluster --type=merge --patch-file=./enable-multi-network-policy.yaml 
network.operator.openshift.io/cluster patched
```

As the result

```
$ oc api-resources 
NAME                   SHORTNAMES     APIVERSION                   NAMESPACED   KIND
multi-networkpolicies  multi-policy   k8s.cni.cncf.io/v1beta1      true         MultiNetworkPolicy
```

[[Back]](../README.md)