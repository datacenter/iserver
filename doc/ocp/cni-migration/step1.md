# Cilium EE migration workflow

[[Back]](./README.md) [[Next]](./step2.md)

## Step 1: Check cluster state and input parameters

- cluster must run OVNKubernetes CNI
- target cluster network does not overlap with current cluster network
- get upstream interface of br-ex ovs switch on any of the cluster nodes
- all cluster operators must be available

### Output

```
Step 1: Check cluster state and input parameters
================================================


OpenShift Network
-----------------
- Name            : cluster
- Network Type    : OVNKubernetes
- Cluster Network : 10.128.0.0/14
- Host Prefix     : 23
- Service Network : 172.30.0.0/16

Target cluster network does not overlap with ovn cluster network
Upstream interface of OVS switch: ens192

Collect Cluster Operators
-------------------------
- authentication [True]
- baremetal [True]
- cloud-controller-manager [True]
- cloud-credential [True]
- cluster-autoscaler [True]
- config-operator [True]
- console [True]
- control-plane-machine-set [True]
- csi-snapshot-controller [True]
- dns [True]
- etcd [True]
- image-registry [True]
- ingress [True]
- insights [True]
- kube-apiserver [True]
- kube-controller-manager [True]
- kube-scheduler [True]
- kube-storage-version-migrator [True]
- machine-api [True]
- machine-approver [True]
- machine-config [True]
- marketplace [True]
- monitoring [True]
- network [True]
- node-tuning [True]
- olm [True]
- openshift-apiserver [True]
- openshift-controller-manager [True]
- openshift-samples [True]
- operator-lifecycle-manager [True]
- operator-lifecycle-manager-catalog [True]
- operator-lifecycle-manager-packageserver [True]
- service-ca [True]
- storage [True]
```

[[Back]](./README.md) [[Next]](./step2.md)