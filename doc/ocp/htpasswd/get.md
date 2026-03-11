# HTPasswd Identity Provider - Get

[[Back]](./README.md) [[Prev]](./delete_task.md) [[Next]](./set.md)

## Workflow

- get `OAuth` crd with identityProviders of HTPasswd type
- get `Secret` crd with user credentials
- get `ClusterRoleBinding` crd for admin role association

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

OpenShift Cluster: bm1

+----+---------+--------------+--------------+-----------+------------------+
| ID | OAuth   | Provider     | Secret       | Is Secret | User             |
+----+---------+--------------+--------------+-----------+------------------+
| 1  | cluster | local-admins | local-admins | True      | akaliwod (admin) |
|    |         |              |              |           | xxx (admin)      |
|    |         |              |              |           | yyy (admin)      |
+----+---------+--------------+--------------+-----------+------------------+
```

[[Back]](./README.md) [[Prev]](./delete_task.md) [[Next]](./set.md)