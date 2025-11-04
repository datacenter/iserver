# NMState Operator - Create via Task

## Input

```
[
    {
        "nmstate": {
            "operator": {
              "filename": "xyz"
            },
            "lldp": {
              "fw": true|false,
              "keep-nncp": true|false,
              "skip-down": true|false
            }
        }
    }
]
```

Notes:
- [operator](./create_operator.md) and [lldp](./enable_lldp.md) trigger workflow execution with optional input parameters
- operator.filename is optional and must contain NMState CRD in YAML format
  - the path defined in operator.filename can be relative and then expected to be in the same directory as task.json file
  - the path defined in operator.filename can be absolute

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
[
    {
        "nmstate": {
            "operator": {},
            "lldp": {
              "fw": true,
              "keep-nncp": false,
              "skip-down": true
            }
        }
    }
]
```

```
# iserver set ocp task --filename C:\tmp\task.json --cluster bm1 --no-confirm
OpenShift Cluster: bm1

Cluster: bm1 (type: ocp)

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - NMState Operator - Create Operator
=======================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "channel": "stable",
    "instance": null,
    "check-verbose": true,
    "namespace": "openshift-nmstate",
    "name": "kubernetes-nmstate-operator",
    "operator-group-name": "nmstate-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Create Namespace
----------------
- name: openshift-nmstate

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-nmstate

~~~

Namespace created

Wait for namespace [timeout:60]...

Create Operator Group
---------------------
Operator group: openshift-nmstate/nmstate-operator-group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: nmstate-operator-group
  namespace: openshift-nmstate
spec:
  targetNamespaces:
  - openshift-nmstate
  upgradeStrategy: Default

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: openshift-nmstate/kubernetes-nmstate-operator
Source: openshift-marketplace/redhat-operators/kubernetes-nmstate-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Channel: stable
- CSV [kubernetes-nmstate-operator.4.18.0-202509241752]
- CSV Display name [Kubernetes NMState Operator]
- CVS Version [4.18.0-202509241752]
- CSV Provider [{'name': 'Red Hat, Inc.'}]
- CSV Maturity [GA]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: kubernetes-nmstate-operator
  namespace: openshift-nmstate
spec:
  channel: stable
  installPlanApproval: Automatic
  name: kubernetes-nmstate-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-drtf5
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-nmstate/nmstate-operator

Create NMState Instance
-----------------------

~~~
apiVersion: nmstate.io/v1
kind: NMState
metadata:
  name: nmstate
spec: {}

~~~

NMState instance created

Wait for nmstate instance [timeout:60]...
Wait for nmstate instance resources...
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-nmstate/nmstate-operator
- openshift-nmstate/nmstate-console-plugin
- openshift-nmstate/nmstate-webhook
Wait for nns ready on all cluster nodes
Node [ocp-bm1] nns collected

Completed tasks
- Namespace created
- Operator Group created
- NMState Operator installed and configured

OpenShift Workflow - NMState Operator - Enable LLDP
===================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "settings": {
        "enable": true,
        "nic-fw-disable": true,
        "delete-nncp": true,
        "include-down": false
    },
    "check-verbose": true,
    "namespace": "openshift-nmstate",
    "name": "kubernetes-nmstate-operator",
    "operator-group-name": "nmstate-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok


Get interface details
---------------------
- node [ocp-bm1]
        interface: bond1
        interface: bond1.702
        interface: cilium_vxlan
        interface: eno1
                ethtool
                lspci
                priv flags
                state
        interface: eno2
                ethtool
                lspci
                priv flags
                state
        interface: eno5
                ethtool
                lspci
                priv flags
                state
        interface: eno6
                ethtool
                lspci
                priv flags
                state
        interface: eno7
                ethtool
                lspci
                priv flags
                state
        interface: eno8
                ethtool
                lspci
                priv flags
                state
        interface: enp216s0f0
                ethtool
                lspci
                priv flags
                state
        interface: enp216s0f1
                ethtool
                lspci
                priv flags
                state
        interface: ens1f0
                ethtool
                lspci
                priv flags
                state
        interface: ens1f1
                ethtool
                lspci
                priv flags
                state
        interface: lo
Disable lldp on ethernet interface fw level [ocp-bm1]
Interface eno1 [0000:3b:00.0] - no change
Interface eno2 [0000:3b:00.1] - no change
Interface eno5 [0000:1d:00.0] - no change
Interface eno6 [0000:1d:00.1] - no change
Interface eno7 [0000:1d:00.2] - no change
Interface eno8 [0000:1d:00.3] - no change
Interface enp216s0f0 [0000:d8:00.0] - no change
Interface enp216s0f1 [0000:d8:00.1] - no change
Interface ens1f0 [0000:5e:00.0] - no change
Interface ens1f1 [0000:5e:00.1] - no change
Enable lldp on nmstate level [ocp-bm1]
Interface eno1 - skip on interface oper down
Interface eno2 - skip on interface oper down
Interface eno5 - already enabled
Interface eno6 - already enabled
Interface eno7 - already enabled
Interface eno8 - already enabled
Interface enp216s0f0 - already enabled
Interface enp216s0f1 - already enabled
Interface ens1f0 - already enabled
Interface ens1f1 - already enabled

Completed tasks
- LLDP disabled on fw nic level
- LLDP enabled on nmstate level
```

[[Back]](./README.md)