# Cilium EE migration workflow

[[Back]](./step2.md) [[Next]](./step4.md)

## Step 3: Change default CNI

- set network.config cluster to Cilium
- set network.operator cluster to Cilium

### Output

```
Step 3: Change default CNI
==========================


Set Cluster Network Type
------------------------
- type: Cilium
- cidr: 10.253.0.0/16
- host prefix: 24

~~~
apiVersion: config.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  clusterNetwork:
  - cidr: 10.253.0.0/16
    hostPrefix: 24
  networkType: Cilium
status: null

~~~
Continue [Y/N]? y
Patch successful

Set Cluster Network Operator Type
---------------------------------
- type: Cilium
- cidr: 10.253.0.0/16
- host prefix: 24
- kube proxy replaceement: False

~~~
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  clusterNetwork:
  - cidr: 10.253.0.0/16
    hostPrefix: 24
  defaultNetowkr:
    type: Cilium
  deployKubeProxy: false
status: null

~~~
Continue [Y/N]? y
Patch successful
```

[[Back]](./step2.md) [[Next]](./step4.md)