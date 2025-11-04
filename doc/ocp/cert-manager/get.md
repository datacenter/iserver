# Certificate Manager - Get

## Workflow

- check cert manager repo and helm chart
- check cert manager crds

## Requirements

Cluster with [helm cli enabled](../cli/helm.md)

## Configurable options

```
# iserver get ocp cert-manager 
  --cluster TEXT  Cluster Name
```

## Non-configurable defaults

```
{
    "namespace": "cert-manager",
    "helm": "cert-manager",
    "repo_name": "jetstack",
    "repo_url": "https://charts.jetstack.io"
}
```

## Example

```
# iserver get ocp ocp cert-manager --cluster bm1 


OpenShift Workflow - Certificate Manager - Get
==============================================

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
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- management node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- cli helm: ok

Check repo jetstack https://charts.jetstack.io
Found
Check helm chart cert-manager
Found
Issuer CRD [#0]
Certificate CRD [#0]
```

[[Back]](./README.md)