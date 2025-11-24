# Data Science (AI) Operator - Delete via Task

## Input

```
[
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

Notes:
- [cluster](./delete_cluster.md) and [operator](./delete_operator.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters may be silently ignored

## Requirements

None

## Configurable options

```
# iserver delete ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example

```
# iserver delete ocp task --file C:\tmp\task.json --cluster bm1             

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Data Science (AI) - Delete Data Science Cluster
====================================================================

OpenShift Cluster: bm1

Completed tasks
- Selected data science cluster deleted

OpenShift Workflow - Data Science (AI) - Delete Operator
========================================================

OpenShift Cluster: bm1

Delete Image Streams
--------------------
- redhat-ods-applications/code-server-notebook
- wait for no image stream
- redhat-ods-applications/codeserver-datascience-cpu-py312-ubi9
- wait for no image stream
- redhat-ods-applications/cuda-rstudio-rhel9
- wait for no image stream
- redhat-ods-applications/jupyter-datascience-cpu-py312-ubi9
- wait for no image stream
- redhat-ods-applications/jupyter-minimal-cpu-py312-ubi9
- wait for no image stream
- redhat-ods-applications/jupyter-minimal-cuda-py312-ubi9
- wait for no image stream
- redhat-ods-applications/jupyter-minimal-rocm-py312-ubi9
- wait for no image stream
- redhat-ods-applications/jupyter-pytorch-cuda-py312-ubi9
- wait for no image stream
- redhat-ods-applications/jupyter-pytorch-llmcompressor
- wait for no image stream
- redhat-ods-applications/jupyter-pytorch-rocm-py312-ubi9
- wait for no image stream
- redhat-ods-applications/jupyter-rocm-minimal
- wait for no image stream
- redhat-ods-applications/jupyter-rocm-pytorch
- wait for no image stream
- redhat-ods-applications/jupyter-rocm-tensorflow
- wait for no image stream
- redhat-ods-applications/jupyter-tensorflow-cuda-py312-ubi9
- wait for no image stream
- redhat-ods-applications/jupyter-trustyai-cpu-py312-ubi9
- wait for no image stream
- redhat-ods-applications/minimal-gpu
- wait for no image stream
- redhat-ods-applications/odh-trustyai-notebook
- wait for no image stream
- redhat-ods-applications/pytorch
- wait for no image stream
- redhat-ods-applications/rstudio-rhel9
- wait for no image stream
- redhat-ods-applications/runtime-datascience
- wait for no image stream
- redhat-ods-applications/runtime-datascience-cpu-py312-ubi9
- wait for no image stream
- redhat-ods-applications/runtime-minimal
- wait for no image stream
- redhat-ods-applications/runtime-minimal-cpu-py312-ubi9
- wait for no image stream
- redhat-ods-applications/runtime-pytorch
- wait for no image stream
- redhat-ods-applications/runtime-pytorch-cuda-py312-ubi9
- wait for no image stream
- redhat-ods-applications/runtime-pytorch-llmcompressor
- wait for no image stream
- redhat-ods-applications/runtime-pytorch-rocm-py312-ubi9
- wait for no image stream
- redhat-ods-applications/runtime-rocm-pytorch
- wait for no image stream
- redhat-ods-applications/runtime-rocm-tensorflow
- wait for no image stream
- redhat-ods-applications/runtime-tensorflow
- wait for no image stream
- redhat-ods-applications/runtime-tensorflow-cuda-py312-ubi9
- wait for no image stream
- redhat-ods-applications/s2i-generic-data-science-notebook
- wait for no image stream
- redhat-ods-applications/s2i-minimal-notebook
- wait for no image stream
- redhat-ods-applications/tensorflow
- wait for no image stream

Delete Subscription
-------------------
- subscription: redhat-ods-operator/rhods-operator
- checking cluster service version...
- csv found and will be deleted: redhat-ods-operator/rhods-operator.2.25.0
- wait for no subscription
- check cluster service version: redhat-ods-operator/rhods-operator.2.25.0
- wait for no csv
Wait for deployments deleted (optional: False)...
- redhat-ods-operator/rhods-operator

Delete Build Configs
--------------------
- redhat-ods-applications/cuda-rstudio-server-rhel9
- wait for no build config
- redhat-ods-applications/rstudio-server-rhel9
- wait for no build config

Delete services
---------------
- redhat-ods-applications/modelmesh-serving

Delete Operator Group
---------------------
- namespace: redhat-ods-operator
- name: ods-operator-group
- wait for no operator group

Delete Namespace
----------------
- name: redhat-ods-operator

Namespace [redhat-ods-operator] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Delete Namespace
----------------
- name: redhat-ods-applications

Namespace [redhat-ods-applications] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Delete Namespace
----------------
- name: redhat-ods-monitoring

Namespace [redhat-ods-monitoring] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Delete Namespace
----------------
- name: rhods-notebooks

Namespace [rhods-notebooks] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Delete Namespace
----------------
- name: rhoai-model-registries

Namespace [rhoai-model-registries] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- Data science cluster initializations deleted
- Data auths deleted
- Data image streams deleted
- Subscription and csv deleted
- Operator Group deleted
- Namespaces deleted
```

[[Back]](./README.md)