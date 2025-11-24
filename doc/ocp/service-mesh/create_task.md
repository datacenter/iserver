# Service Mesh Operator - Create via Task

## Input

```
[
    {
        "service-mesh": {
            "operator": {
                "channel": "__default__"
            }
        }
    }
]
```

Notes:
- [operator](./create_operator.md) trigger workflow execution with optional input parameters

## Requirements

None

## Expected outcome

![OperatorCreate](../images/service-mesh/operator_create.png)

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
Cluster: bm3 (type: ocp)

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Service Mesh Operator - Create Operator
============================================================

OpenShift Cluster: bm3

Create Namespace
----------------
- name: openshift-operators
- already defined

Create Subscription
-------------------
Subscription: openshift-operators/servicemeshoperator3
Source: openshift-marketplace/redhat-operators/servicemeshoperator3
Install plan approval: Automatic
Getting subscription and packege manifest information...
Channel: stable
- CSV [servicemeshoperator3.v3.2.0]
- CSV Display name [Red Hat OpenShift Service Mesh 3]
- CVS Version [3.2.0]
- CSV Provider [{'name': 'Red Hat, Inc.'}]
- CSV Maturity [alpha]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: servicemeshoperator3
  namespace: openshift-operators
spec:
  channel: stable
  installPlanApproval: Automatic
  name: servicemeshoperator3
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  startingCSV: servicemeshoperator3.v3.2.0

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-bjjft
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-operators/servicemesh-operator3

Completed tasks
- Namespace created
- Operator Group created
- Service mesh operator installed
```

[[Back]](./README.md)