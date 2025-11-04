# Container Virtualization Operator - Create via Task

## Input

```
[
    {
        "cnv": {
            "operator": {
                "channel": "xyz"
            },
            "instance": {
                "filename": "xyz"
            }
        }
    }
]
```

Notes:
- [operator](./create_operator.md) and [instance](./create_instance.md) trigger workflow execution with optional input parameters
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies
- instance.filename is optional must contain HyperConverged CRD in YAML format
  - the path defined in instance.filename can be relative and then expected to be in the same directory as task.json file
  - the path defined in instance.filename can be absolute
- operator.channel and instance.filename are optional

## Requirements

None

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example

```
# iserver set ocp task --filename C:\tmp\task.json --no-confirm --cluster bm1


OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Container Virtualization Operator - Create Operator
========================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "channel": "stable",
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


Create Namespace
----------------
- name: openshift-cnv

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-cnv

~~~

Namespace created

Wait for namespace [timeout:60]...

Create Operator Group
---------------------
Operator group: openshift-cnv/cnv-operator-group

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

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: openshift-cnv/kubevirt-hyperconverged
Source: openshift-marketplace/redhat-operators/kubevirt-hyperconverged
Install plan approval: Automatic
Getting subscription and packege manifest information...
Channel: stable
- CSV [kubevirt-hyperconverged-operator.v4.18.17]
- CSV Display name [OpenShift Virtualization]
- CVS Version [4.18.17]
- CSV Provider [{'name': 'Red Hat'}]
- CSV Maturity [alpha]

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

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-bmqck
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-cnv/aaq-operator
- openshift-cnv/cdi-operator
- openshift-cnv/cluster-network-addons-operator
- openshift-cnv/hco-operator
- openshift-cnv/hco-webhook
- openshift-cnv/hostpath-provisioner-operator
- openshift-cnv/hyperconverged-cluster-cli-download
- openshift-cnv/ssp-operator
- openshift-cnv/virt-operator

Completed tasks
- Namespace created
- Operator Group created
- Cnv Operator installed

OpenShift Workflow - Container Virtualization Operator - Create HyperConverged Instance
=======================================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "channel": "stable",
    "instance": null,
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

Operator
--------
- subscription: openshift-cnv/kubevirt-hyperconverged
- channel: stable
- csv: kubevirt-hyperconverged-operator.v4.18.17

Cnv operator ready

Create HyperConverged Instance
------------------------------

~~~
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  annotations:
    deployOVS: 'false'
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec: {}

~~~

HyperConverged instance created

Wait for hyperconverged instance and resources...
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-cnv/cdi-apiserver
- openshift-cnv/cdi-deployment
- openshift-cnv/cdi-uploadproxy
- openshift-cnv/kubemacpool-cert-manager
- openshift-cnv/kubemacpool-mac-controller-manager
- openshift-cnv/kubevirt-apiserver-proxy
- openshift-cnv/kubevirt-console-plugin
- openshift-cnv/kubevirt-ipam-controller-manager
- openshift-cnv/virt-api
- openshift-cnv/virt-controller
- openshift-cnv/virt-exportproxy
- openshift-cnv/virt-template-validator
Wait for deamon sets ready...
- openshift-cnv/bridge-marker
- openshift-cnv/kube-cni-linux-bridge-plugin
- openshift-cnv/passt-binding-cni
- openshift-cnv/virt-handler

Completed tasks
- HyperConverged instance created and ready
```

[[Back]](./README.md)