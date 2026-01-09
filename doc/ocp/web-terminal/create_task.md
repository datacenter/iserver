# CLI Web Terminal - Create via Task

## Input

```
[
    {
        "cli": {
            "web": {
                "operator": {}
            }
        }
    }
]
```

Notes:
- [web](./set.md) trigger workflow execution with optional input parameters
- web.channel is optional

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
Cluster: bm1 (type: ocp)

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - CLI Tools Installation
===========================================

Workflow Parameters
-------------------
{
    "web": {
        "operator": {
            "cluster": "bm1",
            "confirmation": true,
            "channel": "__default__",
            "verbose": false,
            "check-verbose": false
        }
    },
    "cluster": "bm1",
    "exec": [],
    "check-verbose": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:milan]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


OpenShift Workflow - Web Terminal Operator - Create Operator
============================================================

OpenShift Cluster: bm1

Create Subscription
-------------------
Subscription: openshift-operators/web-terminal
Source: openshift-marketplace/redhat-operators/web-terminal
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: fast
- CSV [web-terminal.v1.13.0]
- CSV Display name [Web Terminal]
- CVS Version [1.13.0]
- CSV Provider [{'name': 'Red Hat'}]
- CSV Maturity [alpha]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: web-terminal
  namespace: openshift-operators
spec:
  channel: fast
  installPlanApproval: Automatic
  name: web-terminal
  source: redhat-operators
  sourceNamespace: openshift-marketplace

~~~
Continue [Y/N]? y

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-98cgh
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-operators/web-terminal-controller
- openshift-operators/devworkspace-controller-manager
- openshift-operators/devworkspace-webhook-server

Completed tasks
- Web terminal operator installed
```

[[Back]](./README.md)