# HTPasswd Identity Provider - Get

## Workflow

- check api access to openshift cluster
- select OAuth CRD with identityProviders of HTPasswd type
- check Secret CRD with user credentials
- check ClusterRoleBinding CRD for admin role association

## Requirements

None

## Configurable options

```
# iserver get ocp htpasswd
  --cluster TEXT  Cluster Name
```

## Example

```
# iserver get ocp htpasswd --cluster bm1

OpenShift Workflow - Get HTPasswd Identity Provider
===================================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


+---------+----------+--------+-----------+--------------+
| OAuth   | Provider | Secret | Is Secret | User         |
+---------+----------+--------+-----------+--------------+
| cluster | custom   | custom | True      | kali (admin) |
+---------+----------+--------+-----------+--------------+
```

[[Back]](./README.md)