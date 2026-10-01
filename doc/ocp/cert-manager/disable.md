# Certificate Manager - Disable feature

[[Back]](./README.md)

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

## Example

```
# iserver delete ocp cert-manager --cluster bm1 --wipe

OpenShift Workflow - Certificate Manager - Uninstall
====================================================

OpenShift Cluster: bm1


Certificate Manager Resources
-----------------------------
- issuer      : 0
- certificate : 0

Uninstall helm cert-manager
Helm installed
Remove helm repo jetstack
Helm repo removed

Delete Namespace
----------------
- name: cert-manager

Namespace [cert-manager] resources
- no deployments
- no daemon_sets
- no replica_sets
- no pods
- no services
- no pvcs
- no jobs
Wait for no Namespace cert-manager [timeout:60s]

Completed tasks
- resources wiped
- helm uninstalled
- helm repo removed
- namespace deleted

+----+---------+--------------+----------------+---------+---------+--------------+
| ID | Target  | Scope        | Workflow       | Changes | Success | Duration [s] |
+----+---------+--------------+----------------+---------+---------+--------------+
| 1  | ocp:bm1 | cert-manager | delete feature | 1       | ✓       | 19           | 
+----+---------+--------------+----------------+---------+---------+--------------+
```

[[Back]](./README.md)