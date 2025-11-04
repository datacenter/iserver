# Certificate Manager - Disable feature

## Workflow

- check cert manager crds
- if any issuer or certificate exists and --wipe is not used, then break
- clean up otherwise
- uninstall helm chart
- remove repository
- delete namespace

## Requirements

Cluster with [helm cli enabled](../cli/helm.md)

## Configurable options

```
# iserver delete ocp cert-manager
  --cluster TEXT  Cluster Name
  --wipe          Wipe crds
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
# iserver delete ocp cert-manager --cluster bm1 --wipe

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
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- management node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- cli helm: ok

Check cluster manager crds...
- Issuer CRD [#2]
- Certificate CRD [#4]
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