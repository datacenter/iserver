# Container Virtualization Operator - Delete Operator

## Workflow

- delete operator subscription
- delete operator group
- delete namespace

## Requirements

Hyperconverged instance cannot exists

## Configurable options

```
# iserver delete ocp cnv --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp cnv --cluster bm1 --mode operator

OpenShift Workflow - Container Virtualization Operator - Delete Operator
========================================================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-cnv/kubevirt-hyperconverged
- package               : openshift-marketplace/redhat-operators/kubevirt-hyperconverged
- channel               : stable
- install plan          : openshift-cnv/install-lnx26
- install plan approved : V
- installed csv         : kubevirt-hyperconverged-operator.v4.21.3
- latest_csv            : V


Delete Subscription
-------------------
- subscription: openshift-cnv/kubevirt-hyperconverged
- checking cluster service version...
- csv found and will be deleted: openshift-cnv/kubevirt-hyperconverged-operator.v4.21.3
- wait for no subscription
- check cluster service version: openshift-cnv/kubevirt-hyperconverged-operator.v4.21.3
- wait for no csv
- wait for no Deployment openshift-cnv/aaq-operator [timeout:180s]
- wait for no ReplicaSet openshift-cnv/aaq-operator-5f8fcf4c95 [timeout:180s]
- wait for no Pod openshift-cnv/aaq-operator-5f8fcf4c95-6rp5z [timeout:180s]
- wait for no Deployment openshift-cnv/cdi-operator [timeout:180s]
- wait for no ReplicaSet openshift-cnv/cdi-operator-779d4d6b99 [timeout:180s]
- wait for no Pod openshift-cnv/cdi-operator-779d4d6b99-6ztdf [timeout:180s]
- wait for no Deployment openshift-cnv/cluster-network-addons-operator [timeout:180s]
- wait for no ReplicaSet openshift-cnv/cluster-network-addons-operator-7c86f7b694 [timeout:180s]
- wait for no Pod openshift-cnv/cluster-network-addons-operator-7c86f7b694-zkhwf [timeout:180s]
- wait for no Deployment openshift-cnv/hco-operator [timeout:180s]
- wait for no ReplicaSet openshift-cnv/hco-operator-85c475c948 [timeout:180s]
- wait for no Pod openshift-cnv/hco-operator-85c475c948-hzskl [timeout:180s]
- wait for no Deployment openshift-cnv/hco-webhook [timeout:180s]
- wait for no ReplicaSet openshift-cnv/hco-webhook-5f5989c8b5 [timeout:180s]
- wait for no Pod openshift-cnv/hco-webhook-5f5989c8b5-r7b9w [timeout:180s]
- wait for no Deployment openshift-cnv/hostpath-provisioner-operator [timeout:180s]
- wait for no ReplicaSet openshift-cnv/hostpath-provisioner-operator-6dff86844f [timeout:180s]
- wait for no Pod openshift-cnv/hostpath-provisioner-operator-6dff86844f-4rtxr [timeout:180s]
- wait for no Deployment openshift-cnv/hyperconverged-cluster-cli-download [timeout:180s]
- wait for no ReplicaSet openshift-cnv/hyperconverged-cluster-cli-download-d6854d5b6 [timeout:180s]
- wait for no Pod openshift-cnv/hyperconverged-cluster-cli-download-d6854d5b6-5wtgr [timeout:180s]
- wait for no Deployment openshift-cnv/ssp-operator [timeout:180s]
- wait for no ReplicaSet openshift-cnv/ssp-operator-548b9677b7 [timeout:180s]
- wait for no Pod openshift-cnv/ssp-operator-548b9677b7-j48hh [timeout:180s]
- wait for no Deployment openshift-cnv/virt-operator [timeout:180s]
- wait for no ReplicaSet openshift-cnv/virt-operator-b5cb558d [timeout:180s]
- wait for no Pod openshift-cnv/virt-operator-b5cb558d-ctrkb [timeout:180s]
- wait for no Pod openshift-cnv/virt-operator-b5cb558d-rq9pr [timeout:180s]
- wait for no Deployment openshift-cnv/cdi-apiserver [timeout:180s]
- wait for no Deployment openshift-cnv/cdi-deployment [timeout:180s]
- wait for no Deployment openshift-cnv/cdi-uploadproxy [timeout:180s]
- wait for no Deployment openshift-cnv/kubemacpool-cert-manager [timeout:180s]
- wait for no Deployment openshift-cnv/kubemacpool-mac-controller-manager [timeout:180s]
- wait for no Deployment openshift-cnv/kubevirt-apiserver-proxy [timeout:180s]
- wait for no Deployment openshift-cnv/kubevirt-console-plugin [timeout:180s]
- wait for no Deployment openshift-cnv/kubevirt-ipam-controller-manager [timeout:180s]
- wait for no Deployment openshift-cnv/virt-api [timeout:180s]
- wait for no Deployment openshift-cnv/virt-controller [timeout:180s]
- wait for no Deployment openshift-cnv/virt-exportproxy [timeout:180s]
- wait for no Deployment openshift-cnv/virt-template-validator [timeout:180s]
- wait for no DaemonSet openshift-cnv/bridge-marker [timeout:180s]
- wait for no DaemonSet openshift-cnv/kube-cni-linux-bridge-plugin [timeout:180s]
- wait for no DaemonSet openshift-cnv/passt-binding-cni [timeout:180s]
- wait for no DaemonSet openshift-cnv/virt-handler [timeout:180s]
Subscription cnv resources gone

Delete services
---------------
- no service found

Delete PODs
-----------

Object filter
- namespace:openshift-cnv

Delete

Delete OperatorGroup
--------------------
- namespace: openshift-cnv
- name: cnv-operator-group
- deleted
- wait for no OperatorGroup openshift-cnv/cnv-operator-group [timeout:60s]

Namespace [openshift-cnv] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- no user defined networks
- no cluster user defined networks

Delete Namespace
----------------
- name: openshift-cnv
- wait for no namespace

Completed tasks
- Subscription deleted
- Operator Group deleted
- Namespace deleted

+----+---------+-------+-----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow        | Changes | Success | Duration [s] |
+----+---------+-------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | cnv   | delete operator | 4       | V       | 63           | 
+----+---------+-------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)