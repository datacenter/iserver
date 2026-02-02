# Certificate Manager - Delete via Task

## Input

```
[
  {
    "cert-manager": {
      "feature": {}
    }
  }
]
```

Notes:
- [feature](./disable.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md)

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

## Expected outcome

- cert-manager uninstalled

## Example

```
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json 

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Certificate Manager - Uninstall
====================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "wipe": true,
    "check-verbose": true,
    "namespace": "cert-manager",
    "helm": "cert-manager",
    "repo_name": "jetstack",
    "repo_url": "https://charts.jetstack.io"
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok
- cluster node [*****]: ok
- management node [*****]: ok
- cli helm: ok

Check cluster manager crds...
- Issuer CRD [#0]
- Certificate CRD [#0]
Check helm chart cert-manager
Found
Uninstall helm cert-manager
Helm installed
Check repo jetstack https://charts.jetstack.io
Found
Remove helm repo jetstack
Helm repo removed

Delete Namespace
----------------
- name: cert-manager

Namespace [cert-manager] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

Completed tasks
- resources wiped
- helm uninstalled
- helm repo removed
- namespace deleted
```

[[Back]](./README.md)