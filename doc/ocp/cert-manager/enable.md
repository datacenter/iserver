# Certificate Manager - Enable feature

## Workflow

- check cert manager repo and helm chart
- add repo if required
- install helm if required
- check cert manager crds

## Requirements

Cluster with [helm cli enabled](../cli/helm.md)

## Expected Outcome

Certificate manager CRDs available
- Issuer
- Certificate

## Configurable options

```
# iserver set ocp cert-manager 
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
# iserver set ocp ocp cert-manager --cluster bm1 


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
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- management node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
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
LAST DEPLOYED: Thu Oct 30 16:40:09 2025
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