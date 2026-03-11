# HTPasswd Identity Provider - Add new user

[[Back]](./set.md) [[Prev]](./add_new_provider.md) [[Next]](./add_admin.md)

## Workflow

- Extract the htpasswd file content from secret associated with identity provider
- Add-or-replace user password with new value
- Encode the htpasswd file
- Update the secret

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
+----+---------+--------------+--------------+-----------+------------------+
```

## Action

```
# iserver set ocp htpasswd --cluster bm1 --provider new-one --user ccc:aaa --user ddd:aaa


OpenShift Workflow - Add HTPasswd Identity Provider
===================================================

OpenShift Cluster: bm1

htpasswd identity provider [new-one]
- found
- patch mode
- secret openshift-config/new-one
- check user ccc
- check user ddd

Generated htpasswd
~~~
bbb:...
aaa:...
ccc:...
ddd:...
~~~

Patch Secret
------------
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
Secret [openshift-config/new-one] patched

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
|    |         |              |              |           | ccc              |
|    |         |              |              |           | ddd              |
+----+---------+--------------+--------------+-----------+------------------+
```

[[Back]](./set.md) [[Prev]](./add_new_provider.md) [[Next]](./add_admin.md)