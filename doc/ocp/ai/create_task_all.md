# Data Science (AI) Operator - Create via Task

![Dependencies](../images/ai/dependencies.png)

## Input

```
[
    {
        "serverless": {
            "operator": {
                "channel": "__default__"
            }
        }
    },
    {
        "service-mesh": {
            "operator": {
                "channel": "__default__"
            }
        }
    },
    {
        "ai": {
            "operator": {
              "channel": "__default__"  
            },
            "cluster": {
              "filename": "xyz"
            }
        }
    }
]
```

Refer to task documentation for details
- [serverless](../serverless/create_task.md)
- [service mesh](../service-mesh/create_task.md)
- [ai](../ai/create_task.md)

## Requirements

None

## Expected Outcome

### Serverless Operator installed

![Serverless](../images/serverless/operator_create.png)

### Service Mesh Operator installed

![ServiceMesh](../images/service-mesh/operator_create.png)

### AI Operator installed

![OperatorCreate](../images/ai/operator_create.png)

### Operator resources ready

![OperatorResources](../images/ai/operator_resources.png)

### Data Science Cluster ready

![DSC](../images/ai/cluster_create.png)

### Dashboard reachable

![Dashboard](../images/ai/dashboard.png)

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


OpenShift Workflow - Serverless Operator - Create Operator
==========================================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: openshift-serverless

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-serverless

~~~

Namespace created

Wait for namespace [timeout:60]...

Create Operator Group
---------------------
Operator group: openshift-serverless/serverless-operator-group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: serverless-operator-group
  namespace: openshift-serverless
spec:
  upgradeStrategy: Default

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: openshift-serverless/serverless-operator
Source: openshift-marketplace/redhat-operators/serverless-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Channel: stable
- CSV [serverless-operator.v1.37.0]
- CSV Display name [Red Hat OpenShift Serverless]
- CVS Version [1.37.0]
- CSV Provider [{'name': 'Red Hat'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: serverless-operator
  namespace: openshift-serverless
spec:
  channel: stable
  installPlanApproval: Automatic
  name: serverless-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-qd4sc
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-serverless/knative-openshift
- openshift-serverless/knative-openshift-ingress
- openshift-serverless/knative-operator-webhook

Completed tasks
- Namespace created
- Operator Group created
- Serverless operator installed

OpenShift Workflow - Service Mesh Operator - Create Operator
============================================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: openshift-operators
- already defined

Create Subscription
-------------------
Subscription: openshift-operators/servicemeshoperator
Source: openshift-marketplace/redhat-operators/servicemeshoperator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Channel: stable
- CSV [servicemeshoperator.v2.6.11]
- CSV Display name [Red Hat OpenShift Service Mesh 2]
- CVS Version [2.6.11-0]
- CSV Provider [{'name': 'Red Hat, Inc.'}]
- CSV Maturity [alpha]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: servicemeshoperator
  namespace: openshift-operators
spec:
  channel: stable
  installPlanApproval: Automatic
  name: servicemeshoperator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  startingCSV: servicemeshoperator.v2.6.11

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-6nchx
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-operators/istio-operator

Completed tasks
- Namespace created
- Operator Group created
- Service mesh operator installed

OpenShift Workflow - Data Science (AI) - Create Operator
========================================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: redhat-ods-operator

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: redhat-ods-operator

~~~

Namespace created

Wait for namespace [timeout:60]...

Create Operator Group
---------------------
Operator group: redhat-ods-operator/ods-operator-group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: ods-operator-group
  namespace: redhat-ods-operator
spec:
  upgradeStrategy: Default

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: redhat-ods-operator/rhods-operator
Source: openshift-marketplace/redhat-operators/rhods-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Channel: stable
- CSV [rhods-operator.2.25.0]
- CSV Display name [Red Hat OpenShift AI]
- CVS Version [2.25.0]
- CSV Provider [{'name': 'Red Hat, Inc.'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: rhods-operator
  namespace: redhat-ods-operator
spec:
  channel: stable
  installPlanApproval: Automatic
  name: rhods-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-szmnx
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- redhat-ods-operator/rhods-operator
Wait for data science cluster initialization...
default-dsci
Wait for data science cluster initialization [default-dsci] ready...
Wait for auth...
auth
Wait for auth [auth] ready...

Completed tasks
- Namespace created
- Operator Group created
- Data Science (AI) Operator installed
- Data Science Cluster Initialization ready
- Auth ready

OpenShift Workflow - Data Science (AI) - Create Data Science Cluster
====================================================================

OpenShift Cluster: bm1
AI Operator
-----------
- subscription: redhat-ods-operator/rhods-operator
- channel: stable
- csv: rhods-operator.2.25.0
Serverless Operator
-------------------
- subscription: openshift-serverless/serverless-operator
- channel: stable
- csv: serverless-operator.v1.37.0
Service Mesh Operator
---------------------
- subscription: openshift-operators/servicemeshoperator
- channel: stable
- csv: servicemeshoperator.v2.6.11

Create Data Science Cluster
---------------------------
- name: default-dsc

~~~
apiVersion: datasciencecluster.opendatahub.io/v1
kind: DataScienceCluster
metadata:
  labels:
    app.kubernetes.io/created-by: rhods-operator
    app.kubernetes.io/instance: default-dsc
    app.kubernetes.io/managed-by: kustomize
    app.kubernetes.io/name: datasciencecluster
    app.kubernetes.io/part-of: rhods-operator
  name: default-dsc
spec:
  components:
    codeflare:
      managementState: Managed
    dashboard:
      managementState: Managed
    datasciencepipelines:
      managementState: Managed
    feastoperator:
      managementState: Managed
    kserve:
      managementState: Managed
      nim:
        managementState: Managed
      serving:
        ingressGateway:
          certificate:
            type: OpenshiftDefaultIngress
        managementState: Managed
        name: knative-serving
    kueue:
      managementState: Managed
    llamastackoperator:
      managementState: Managed
    modelmeshserving:
      managementState: Managed
    modelregistry:
      managementState: Managed
      registriesNamespace: rhoai-model-registries
    ray:
      managementState: Managed
    trainingoperator:
      managementState: Managed
    trustyai:
      managementState: Managed
    workbenches:
      managementState: Managed

~~~

DataScienceCluster created

Wait for data science cluster crd [timeout:60]...
Wait for data science cluster ready...
Waiting for: Code Flare, Dashboard, Data Science Pipeline, Feast Operator, Kserver, Kqueue, Llama Stack Operator, Model Mesh Serving, Model Registry, Ray, Training Operator, TrustyAI, Workbench
Waiting for: Code Flare, Dashboard, Kserver, Kqueue, Model Mesh Serving, Ray, Training Operator
Waiting for: Code Flare, Dashboard, Kserver, Kqueue, Ray
Waiting for: Code Flare, Dashboard, Kserver
Waiting for: Code Flare, Dashboard
Waiting for: Code Flare
Waiting for: 
Waiting for ready state...
Wait for data science cluster resources...

Completed tasks
- Data Science Cluster created
```

[[Back]](./README.md)