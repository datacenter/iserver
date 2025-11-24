# Data Science (AI) Operator - Create Cluster

## Workflow

- create data science cluster either based on default configuration or user provided definition
- default configuration patched with all-managed components
- wait for data science cluster resources ready

## Requirements

- Data science operator [created](./create_operator.md)
- Serverless operator [created](../serverless/create_operator.md)
- Service Mesh operator [created](../serverless/create_operator.md)

## Expected Outcome

### Data Science Cluster ready

![DSC](../images/ai/cluster_create.png)

### Dashboard reachable

![Dashboard](../images/ai/dashboard.png)

## Configurable options

```
# iserver set ocp ai --mode cluster
  --cluster TEXT                 Cluster Name
  --filename TEXT                DataScienceCluster CRD
  --no-confirm                   Confirmation mode
```

## Example

```
# iserver set ocp ai --cluster bm1 --mode cluster      

OpenShift Workflow - Data Science (AI) - Create Data Science Cluster
====================================================================

OpenShift Cluster: bm1

Create Data Science Cluster Instance
------------------------------------
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
Continue [Y/N]? y

DataScienceCluster instance created

Wait for data science cluster crd [timeout:60]...
Wait for data science cluster ready...
Waiting for: Code Flare, Dashboard, Data Science Pipeline, Feast Operator, Kserver, Kqueue, Llama Stack Operator, Model Mesh Serving, Model Registry, Ray, Training Operator, TrustyAI, Workbench
Waiting for: Dashboard, Data Science Pipeline, Feast Operator, Kserver, Kqueue, Llama Stack Operator, Model Mesh Serving, Model Registry, Ray, Training Operator, TrustyAI, Workbench
Waiting for: Dashboard, Data Science Pipeline, Feast Operator, Kserver, Kqueue, Model Mesh Serving, Model Registry, Ray, Training Operator, TrustyAI, Workbench
Waiting for: Dashboard, Data Science Pipeline, Feast Operator, Kserver, Kqueue, Model Mesh Serving, Ray, Training Operator, TrustyAI, Workbench
Waiting for: Dashboard, Kserver, Kqueue, Model Mesh Serving, Ray, Training Operator, Workbench
Waiting for: Dashboard, Kserver, Model Mesh Serving, Ray, Training Operator, Workbench
Waiting for: Dashboard, Kserver, Model Mesh Serving, Ray, Training Operator
Waiting for: Kserver
Waiting for: 
Waiting for ready state...
Wait for data science cluster resources...

Completed tasks
- Data Science Cluster created
```

[[Back]](./README.md)