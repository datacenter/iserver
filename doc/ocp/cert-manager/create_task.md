# Certificate Manager - Create via Task

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
- you can reuse exactly the same input file that is used for [delete task](./delete_task.md)

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

## Expected outcome

- certificate manager installed
- crds available
  - Issuer
  - Certificate

## Example

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Certificate Manager - Install
==================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
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

Check repo jetstack https://charts.jetstack.io
Not found
Add repo jetstack https://charts.jetstack.io
~~~
"jetstack" has been added to your repositories


~~~
Helm repo added
Check helm chart cert-manager
Not found
Install jetstack/cert-manager
~~~
NAME: cert-manager
LAST DEPLOYED: Thu Nov  6 16:02:26 2025
NAMESPACE: cert-manager
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
⚠️  WARNING: New default private key rotation policy for Certificate resources.
The default private key rotation policy for Certificate resources was
changed to `Always` in cert-manager >= v1.18.0.
Learn more in the [1.18 release notes](https://cert-manager.io/docs/releases/release-notes/release-notes-1.18).

cert-manager v1.19.1 has been deployed successfully!

In order to begin issuing certificates, you will need to set up a ClusterIssuer
or Issuer resource (for example, by creating a 'letsencrypt-staging' issuer).

More information on the different types of issuers and how to configure them
can be found in our documentation:

https://cert-manager.io/docs/configuration/

For information on how to configure cert-manager to automatically provision
Certificates for Ingress resources, take a look at the `ingress-shim`
documentation:

https://cert-manager.io/docs/usage/ingress/


~~~
Helm installed
CRDs found

Completed tasks
- certificate manager installed
```

[[Back]](./README.md)