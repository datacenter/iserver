# Container Virtualization Operator - Delete Operator

## Workflow

- delete node feature discover instance
- delete operator subscription
- delete operator group
- delete namespace

## Requirements

None

## Configurable options

```
# iserver delete ocp cnv --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp cnv --cluster bm1       

OpenShift Workflow - Container Virtualization Operator - Delete Operator
========================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "check-verbose": true,
    "namespace": "openshift-cnv",
    "name": "kubevirt-hyperconverged",
    "operator-group-name": "cnv-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Delete Subscription
-------------------
- subscription: openshift-cnv/kubevirt-hyperconverged
- checking cluster service version...
- csv found and will be deleted: openshift-cnv/kubevirt-hyperconverged-operator.v4.18.17
- wait for no subscription
- check cluster service version: openshift-cnv/kubevirt-hyperconverged-operator.v4.18.17
- wait for no csv
Wait for deployments deleted (optional: False)...
- openshift-cnv/aaq-operator
- openshift-cnv/cdi-operator
- openshift-cnv/cluster-network-addons-operator
- openshift-cnv/hco-operator
- openshift-cnv/hco-webhook
- openshift-cnv/hostpath-provisioner-operator
- openshift-cnv/hyperconverged-cluster-cli-download
- openshift-cnv/ssp-operator
- openshift-cnv/virt-operator

Delete Operator Group
---------------------
- namespace: openshift-cnv
- name: cnv-operator-group
- wait for no operator group

Delete namespaced services
--------------------------
- namespace: openshift-cnv
- hyperconverged-cluster-cli-download
- kubevirt-apiserver-proxy-service
- kubevirt-console-plugin-service

Delete PODs
-----------

Object filter
- namespace:openshift-cnv

Delete
- hyperconverged-cluster-cli-download-54f4ddddb5-dzkf8
- wait for no pod...

Delete Namespace
----------------
- name: openshift-cnv

Namespace [openshift-cnv] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- Subscription and csv deleted
- Operator Group deleted
- Namespace deleted
```

[[Back]](./README.md)