# HTPasswd Identity Provider - Grant admin role to existing user

[[Back]](./set.md) [[Prev]](./add_new_user.md) [[Next]](./update_user.md)

## Workflow

- check if user is defined
- add user subject to `ClusterRoleBinding` object with `cluster-admin` name

## Before

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
| 2  | cluster | new-one      | new-one      | True      | aaa              |
|    |         |              |              |           | bbb              |
|    |         |              |              |           | ccc              |
|    |         |              |              |           | ddd              |
+----+---------+--------------+--------------+-----------+------------------+
```

## Action

```
# iserver set ocp htpasswd --cluster bm1 --provider new-one --admin ccc

OpenShift Workflow - Add HTPasswd Identity Provider
===================================================

OpenShift Cluster: bm1

htpasswd identity provider [new-one]
- found
- patch mode
- secret openshift-config/new-one
- check admin ccc

Add user subject to cluster role binding
----------------------------------------
- cluster role binding: cluster-admin
- user: ccc

Replace ClusterRoleBinding
--------------------------
- name: cluster-admin

~~~
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: 'true'
  labels:
    kubernetes.io/bootstrapping: rbac-defaults
  name: cluster-admin
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- apiGroup: rbac.authorization.k8s.io
  description: Group:system:masters
  kind: Group
  name: system:masters
- apiGroup: rbac.authorization.k8s.io
  description: User:akaliwod
  kind: User
  name: akaliwod
- apiGroup: rbac.authorization.k8s.io
  description: User:xxx
  kind: User
  name: xxx
- apiGroup: rbac.authorization.k8s.io
  description: User:yyy
  kind: User
  name: yyy
- apiGroup: rbac.authorization.k8s.io
  kind: User
  name: ccc

~~~
ClusterRoleBinding [cluster-admin] replaced

Completed tasks
- HTPasswd Identity Provider configured
```

## After

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
| 2  | cluster | new-one      | new-one      | True      | aaa              |
|    |         |              |              |           | bbb              |
|    |         |              |              |           | ccc (admin)      |
|    |         |              |              |           | ddd              |
+----+---------+--------------+--------------+-----------+------------------+
```

[[Back]](./set.md) [[Prev]](./add_new_user.md) [[Next]](./update_user.md)