# HTPasswd Identity Provider - Delete user

[[Back]](./delete.md) [[Prev]](./delete_admin.md) [[Next]](./delete_provider.md)

## Workflow

- Extract the htpasswd file content from `Secret`
- Remove the line with user password
- Encode the htpasswd file
- Update the `Secret`
- Remove existing resources for each deleted user i.e. `User` and `Identity`
- remove user subject from `ClusterRoleBinding` object with `cluster-admin` name
- if no user left identity provider, trigger [provider delete](./delete_provider.md) workflow

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
# iserver delete ocp htpasswd --cluster bm1 --provider new-one --user ccc --user ddd

OpenShift Workflow - Delete HTPasswd Identity Provider
======================================================

OpenShift Cluster: bm1

htpasswd identity provider [new-one]
- found

Delete user
-----------
- user: ccc
- with identities
- incl identity: new-one:ccc
- already deleted

Delete Identity
---------------
- name: new-one:ccc
- already deleted

Remove user subject from cluster role binding
---------------------------------------------
- cluster role binding: cluster-admin
- user: ccc
- already deleted

Delete user
-----------
- user: ddd
- with identities
- incl identity: new-one:ddd
- already deleted

Delete Identity
---------------
- name: new-one:ddd
- already deleted

Remove user subject from cluster role binding
---------------------------------------------
- cluster role binding: cluster-admin
- user: ddd
- already deleted

Generated htpasswd
~~~
aaa:...
bbb:...
~~~

Replace Secret
--------------
- namespace: openshift-config
- name: new-one

~~~
apiVersion: v1
data:
  htpasswd: ...
kind: Secret
metadata:
  name: new-one
  namespace: openshift-config
type: Opaque

~~~
Secret [openshift-config/new-one] replaced

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
+----+---------+--------------+--------------+-----------+------------------+
```

[[Back]](./delete.md) [[Prev]](./delete_admin.md) [[Next]](./delete_provider.md)