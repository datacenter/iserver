# Certificate Manager - Enable feature

[[Back]](./README.md)

## Workflow

- check cert manager repo and helm chart
- add repo if required
- install helm if required
- check cert manager crds

## Requirements

- Cluster with [helm cli enabled](../cli/helm.md)
- [bashrc settings](../cli/configure_bashrc.md) may need to be configured with http proxy settings

## Expected outcome

Certificate manager CRDs available
- Issuer
- Certificate

## Configurable options

```
# iserver set ocp cert-manager --mode feature
  --cluster TEXT  Cluster Name
```

## Example

```
# iserver set ocp ocp cert-manager --cluster bm1 --mode feature

OpenShift Workflow - Certificate Manager - Install
==================================================

OpenShift Cluster: bm1
Add repo jetstack https://charts.jetstack.io
~~~
"jetstack" has been added to your repositories

~~~
Helm repo added
Install jetstack/cert-manager
~~~
NAME: cert-manager
LAST DEPLOYED: Tue May 26 19:48:02 2026
NAMESPACE: cert-manager
STATUS: deployed
REVISION: 1
DESCRIPTION: Install complete
TEST SUITE: None
NOTES:
cert-manager v1.20.2 has been deployed successfully!

In order to begin issuing certificates, you will need to set up a ClusterIssuer
or Issuer resource (for example, by creating a 'letsencrypt-staging' issuer).

More information on the different types of issuers and how to configure them
can be found in our documentation:

https://cert-manager.io/docs/configuration/

For information on how to configure cert-manager to automatically provision
Certificates for Ingress resources, take a look at the `ingress-shim`
documentation:

https://cert-manager.io/docs/usage/ingress/

For information on how to configure cert-manager to automatically provision
Certificates for Gateway API resources, take a look at the `gateway resource`
documentation:

https://cert-manager.io/docs/usage/gateway/

~~~
Helm installed

+----+--------------+--------------+----------+-----------------------------------------+----------+----------------------+-------------+
| ID | Namespace    | Name         | Revision | Updated                                 | Status   | Chart                | App Version |
+----+--------------+--------------+----------+-----------------------------------------+----------+----------------------+-------------+
| 1  | cert-manager | cert-manager | 1        | 2026-05-26 19:48:02.878893726 +0000 UTC | deployed | cert-manager-v1.20.2 | v1.20.2     | 
+----+--------------+--------------+----------+-----------------------------------------+----------+----------------------+-------------+


Certificate Manager Resources
-----------------------------
- issuer      : 0
- certificate : 0


Completed tasks
- certificate manager installed

+----+---------+--------------+----------------+---------+---------+--------------+
| ID | Target  | Scope        | Workflow       | Changes | Success | Duration [s] |
+----+---------+--------------+----------------+---------+---------+--------------+
| 1  | ocp:bm1 | cert-manager | create feature | 0       | ✓       | 89           | 
+----+---------+--------------+----------------+---------+---------+--------------+
```

[[Back]](./README.md)