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

OpenShift Workflow - Container Virtualization Operator - Create Operator
========================================================================

OpenShift Cluster: bm1
Subscription not found kubevirt-hyperconverged

Create Namespace
----------------
- name: openshift-cnv

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-cnv
~~~
Namespace [openshift-cnv] created
Wait for namespace [timeout:60]...

Create OperatorGroup
--------------------
- namespace: openshift-cnv
- name: cnv-operator-group

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
OperatorGroup [openshift-cnv/cnv-operator-group] created
- wait for OperatorGroup openshift-cnv/cnv-operator-group [timeout:60s]

Create Subscription
-------------------
Subscription: openshift-cnv/kubevirt-hyperconverged
Source: openshift-marketplace/redhat-operators/kubevirt-hyperconverged
Install plan approval: Automatic
Getting subscription and packege manifest information...
Channel: stable
- CSV [kubevirt-hyperconverged-operator.v4.21.3]
- CSV Display name [OpenShift Virtualization]
- CVS Version [4.21.3]
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
Install plan: install-zbr78
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployment openshift-cnv/aaq-operator ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/cdi-operator ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/cluster-network-addons-operator ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/hco-operator ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/hco-webhook ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/hostpath-provisioner-operator ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/hyperconverged-cluster-cli-download ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/ssp-operator ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/virt-operator ready (optional: False, allow zero replicas: False, timeout: 600s)...
Subscription cnv ready

Operator
- subscription          : openshift-cnv/kubevirt-hyperconverged
- package               : openshift-marketplace/redhat-operators/kubevirt-hyperconverged
- channel               : stable
- install plan          : openshift-cnv/install-zbr78
- install plan approved : V
- installed csv         : kubevirt-hyperconverged-operator.v4.21.3
- latest_csv            : V


Completed tasks
- Namespace created
- Operator Group created
- Subscription created

OpenShift Workflow - Container Virtualization Operator - Create HyperConverged Instance
=======================================================================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-cnv/kubevirt-hyperconverged
- package               : openshift-marketplace/redhat-operators/kubevirt-hyperconverged
- channel               : stable
- install plan          : openshift-cnv/install-zbr78
- install plan approved : V
- installed csv         : kubevirt-hyperconverged-operator.v4.21.3
- latest_csv            : V


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
Wait for deployment openshift-cnv/cdi-apiserver ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/cdi-deployment ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/cdi-uploadproxy ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/kubemacpool-cert-manager ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/kubemacpool-mac-controller-manager ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/kubevirt-apiserver-proxy ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/kubevirt-console-plugin ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/kubevirt-ipam-controller-manager ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/virt-api ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/virt-controller ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/virt-exportproxy ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-cnv/virt-template-validator ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for daemonset openshift-cnv/bridge-marker ready (optional: False, timeout: 600s)...
Wait for daemonset openshift-cnv/kube-cni-linux-bridge-plugin ready (optional: False, timeout: 600s)...
Wait for daemonset openshift-cnv/passt-binding-cni ready (optional: True, timeout: 600s)...
Success with optional condition
Wait for daemonset openshift-cnv/virt-handler ready (optional: False, timeout: 600s)...
Subscription cnv ready

Completed tasks
- HyperConverged instance created and ready

+----+---------+-------+-----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow        | Changes | Success | Duration [s] |
+----+---------+-------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | cnv   | create operator | 3       | V       | 114          | 
| 2  | ocp:bm1 | cnv   | create instance | 1       | V       | 138          | 
+----+---------+-------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)