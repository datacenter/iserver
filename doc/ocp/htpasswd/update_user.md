# HTPasswd Identity Provider - Update user

[[Back]](./set.md) [[Prev]](./add_admin.md) [[Next]](./update_user.md)

## Workflow

- Extract the htpasswd file content from secret associated with identity provider
- Add-or-replace user password
- Encode the htpasswd file
- Update the `Secret`

## Action

```
# iserver set ocp htpasswd --cluster bm1 --provider new-one --user ddd:newsecret

OpenShift Workflow - Add HTPasswd Identity Provider
===================================================

OpenShift Cluster: bm1

htpasswd identity provider [new-one]
- found
- patch mode
- secret openshift-config/new-one
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

[[Back]](./set.md) [[Prev]](./add_admin.md) [[Next]](./update_user.md)