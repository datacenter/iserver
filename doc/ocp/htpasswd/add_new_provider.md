# HTPasswd Identity Provider - Add new provider

[[Back]](./set.md) [[Prev]](./update_user.md) [[Next]](./add_new_user.md)

## Workflow

- Create an htpasswd file to store the user and password information.
- Create a secret to represent the htpasswd file.
- Define an htpasswd identity provider resource that references the secret.
- Apply the resource to the default OAuth configuration to add the identity provider.

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
```

## Action

```
# cat /tmp/htpasswd.txt
bbb:...
```

```
# iserver set ocp htpasswd --cluster bm1 --provider new-one --user aaa:aaa --filename /tmp/htpasswd.txt 

OpenShift Workflow - Add HTPasswd Identity Provider
===================================================

OpenShift Cluster: bm1

htpasswd identity provider [new-one]
- not found
- post mode
- secret openshift-config/new-one
- check user bbb
- check user aaa

Add htpasswd identity provider to oauth
---------------------------------------
- oauth: cluster
- provider: new-one
- secret: new-one

Replace OAuth
-------------
- name: cluster

~~~
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - htpasswd:
      fileData:
        name: local-admins
    mappingMethod: claim
    name: local-admins
    type: HTPasswd
  - htpasswd:
      fileData:
        name: new-one
    mappingMethod: claim
    name: new-one
    type: HTPasswd

~~~
OAuth [cluster] replaced
OAuth updated with htpasswd [new-one]

Generated htpasswd
~~~
bbb:...
aaa:...
~~~

Create Secret
-------------
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
Secret [openshift-config/new-one] created
- wait for Secret openshift-config/new-one [timeout:60s]

Completed tasks
- HTPasswd Identity Provider configured
```

## After

![New](../images/htpasswd/new_provider.png)

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

[[Back]](./set.md) [[Prev]](./update_user.md) [[Next]](./add_new_user.md)