# HTPasswd Identity Provider - CRD Example

[[Back]](./README.md)

Goal
- create `new-one' htpasswd identity provider
- add 'aaa' user with 'bbb' password
- grant admin role to 'aaa'

## Secret

```
apiVersion: v1
data:
  htpasswd: YmJiOiQyeSQwNSR4bzc5ampwMlRPTmRTOHI2c2NFVkwub0xCTXZ3TnFvTmtYLm5CenA4VnFEN2xmbm1BVlFFcQphYWE6JDJ5JDEyJHVRYVZFOEFBYWJDZGRCNXZ2OXI3ZC5HZ2xaTWVKYmFtT1pRTFBSbThCWUs0MmtBaXlMeHZX
kind: Secret
metadata:
  name: new-one
  namespace: openshift-config
type: Opaque
```

## OAuth

```
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - htpasswd:
      fileData:
        name: new-one
    mappingMethod: claim
    name: new-one
    type: HTPasswd
```

## ClusterRoleBinding

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
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
  description: User:aaa
  kind: User
  name: aaa
```

[[Back]](./README.md)