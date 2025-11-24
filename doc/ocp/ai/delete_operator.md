# Data Science (AI) Operator - Delete Operator

## Workflow

- delete data science initializations
- delete auths
- delete image streams
- delete operator subscription
- delete operator group
- check for no resources
- delete namespaces
  - redhat-ods-operator
  - redhat-ods-applications
  - redhat-ods-monitoring
  - rhods-notebooks
  - rhoai-model-registries

## Requirements

No data science cluster [created](./create_cluster.md)

## Configurable options

```
# iserver delete ocp ai --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp ai --cluster bm1 -- mode operator

OpenShift Workflow - Data Science (AI) - Delete Operator
========================================================

OpenShift Cluster: bm1

Delete Image Streams
--------------------
- no image stream found

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
- no build config found

Delete services
---------------
- no service found

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
- already deleted

Delete Namespace
----------------
- name: rhoai-model-registries
- already deleted

Completed tasks
- Data science cluster initializations deleted
- Data auths deleted
- Data image streams deleted
- Subscription and csv deleted
- Operator Group deleted
- Namespaces deleted
```

[[Back]](./README.md)