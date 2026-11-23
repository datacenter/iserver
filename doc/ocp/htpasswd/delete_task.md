# HTPasswd Identity Provider - Delete via Task

[[Back]](./README.md) [[Prev]](./delete.md) [[Next]](./get.md)

## Input

```
[
    {
        "identity": {
            "type": "htpasswd",
            "provider": "new-one",
            "userpass": [
                "aaa:aaa"
            ],
            "filename": [
                "/tmp/htpasswd.txt"
            ],
            "admins": [
                "__ALL__"
            ]
        }
    }
] 
```

Notes:
- htpasswd users to be added are defined with identity.filename
- filename can be file or directory
- all files in the directory must be valid htpasswd files
- file or directory path must be absolute or relative to the location of task file

## Requirements

None

## Configurable options

```
# iserver delete ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example

```
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json

OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Delete HTPasswd Identity Provider
======================================================

OpenShift Cluster: bm1

htpasswd identity provider [new-one]
- found

Delete user
-----------
- user: bbb
- with identities
- incl identity: new-one:bbb
- already deleted

Delete Identity
---------------
- name: new-one:bbb
- already deleted

Remove user subject from cluster role binding
---------------------------------------------
- cluster role binding: cluster-admin
- user: bbb

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
  description: User:aaa
  kind: User
  name: aaa

~~~
ClusterRoleBinding [cluster-admin] replaced

Delete user
-----------
- user: aaa
- with identities
- incl identity: new-one:aaa
- already deleted

Delete Identity
---------------
- name: new-one:aaa
- already deleted

Remove user subject from cluster role binding
---------------------------------------------
- cluster role binding: cluster-admin
- user: aaa

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

~~~
ClusterRoleBinding [cluster-admin] replaced

Delete Secret
-------------
- namespace: openshift-config
- name: new-one
- wait for no secret

Delete identity provider from oauth
-----------------------------------
- oauth: cluster
- provider: new-one

Replace OAuth
-------------
- name: cluster

~~~
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  annotations:
    include.release.openshift.io/ibm-cloud-managed: 'true'
    include.release.openshift.io/self-managed-high-availability: 'true'
    release.openshift.io/create-only: 'true'
  name: cluster
spec:
  identityProviders:
  - ldap:
    mappingMethod: claim
    name: ldap
    type: LDAP
    ...
  - htpasswd:
      fileData:
        name: local-admins
    mappingMethod: claim
    name: local-admins
    type: HTPasswd

~~~
OAuth [cluster] replaced

Remove user subject from cluster role binding
---------------------------------------------
- cluster role binding: cluster-admin
- user: bbb
- already deleted

Remove user subject from cluster role binding
---------------------------------------------
- cluster role binding: cluster-admin
- user: aaa
- already deleted

Completed tasks
- HTPasswd Identity Provider configured
```

[[Back]](./README.md) [[Prev]](./delete.md) [[Next]](./get.md)