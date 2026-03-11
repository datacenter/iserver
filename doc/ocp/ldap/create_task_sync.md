# LDAP Identity Provider - Group Sync - Create via Task

[[Back]](./README.md) [[Prev]](./create_task.md) [[Next]](./delete.md)

## Input

```
[
    {
        "identity": {
            "type": "ldap",
            "mode": "sync",
            "method": "api",
            "provider": "ldap",
            "group": "ou=Groups,ou=se,dc=se,dc=domain,dc=com",
            "user": "ou=se,dc=se,dc=domain,dc=com",
            "whitelist": [
                "NORTH",
                "SOUTH"
            ],
            "groupUIDAttribute": "dn",
            "groupNameAttributes": "cn",
            "groupMembershipAttributes": "member",
            "userUIDAttribute": "dn",
            "userNameAttributes": "userPrincipalName",
            "job": "ldap-sync",
            "schedule": "*/30"
        }
    }
] 
```

## Requirements

None

## Expected outcome

```
# iserver get ocp ldap --cluster bm1

OpenShift Workflow - LDAP Identity Provider - Get
=================================================

OpenShift Cluster: bm1

+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+
| ID | OAuth   | Provider | LDAP                                                                               | Attribute                            | Usage    |
+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+
| 1  | cluster | ldap     | ldap://ldap-server.domain.com/ou=users,ou=se,dc=se,dc=domain,dc=com?sAMAccountName | id: sAMAccountName                   | User:  0 | 
|    |         |          | bindDN: CN=bm1,OU=Users,OU=se,DC=se,DC=domain,DC=com                               | name: cn                             | Group: 2 | 
|    |         |          | secret: ldap [exists:True]                                                         | email: mail                          |          | 
|    |         |          | mapping: claim                                                                     | preferredUsername: userPrincipalName |          |
+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+
```

```
# oc get cronjobs.batch -n ldap-sync
NAME                SCHEDULE       TIMEZONE   SUSPEND   ACTIVE   LAST SCHEDULE   AGE
ldap-group-syncer   */30 * * * *   <none>     False     0        <none>          44s
```

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json 
Cluster: bm1 (type: ocp)

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - LDAP Group - Sync Add
==========================================

OpenShift Cluster: bm1

+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+
| ID | OAuth   | Provider | LDAP                                                                               | Attribute                            | Usage    |
+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+
| 1  | cluster | ldap     | ldap://ldap-server.domain.com/ou=users,ou=se,dc=se,dc=domain,dc=com?sAMAccountName | id: sAMAccountName                   | User:  0 | 
|    |         |          | bindDN: CN=bm1,OU=Users,OU=se,DC=se,DC=domain,DC=com                               | name: cn                             | Group: 0 | 
|    |         |          | secret: ldap [exists:True]                                                         | email: mail                          |          | 
|    |         |          | mapping: claim                                                                     | preferredUsername: userPrincipalName |          |
+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+
~~~
apiVersion: v1
bindDN: CN=bm1,OU=Users,OU=se,DC=se,DC=domain,DC=com
bindPassword: secret
insecure: true
kind: LDAPSyncConfig
rfc2307:
  groupMembershipAttributes:
  - member
  groupNameAttributes:
  - cn
  groupUIDAttribute: dn
  groupsQuery:
    baseDN: ou=Groups,ou=se,dc=se,dc=domain,dc=com
    derefAliases: never
    filter: (objectClass=group)
    pageSize: 0
    scope: sub
  tolerateMemberNotFoundErrors: false
  tolerateMemberOutOfScopeErrors: false
  userNameAttributes:
  - userPrincipalName
  userUIDAttribute: dn
  usersQuery:
    baseDN: ou=se,dc=se,dc=domain,dc=com
    derefAliases: never
    pageSize: 0
    scope: sub
url: ldap://ldap-server.domain.com

~~~
LDAPSyncConfig uploaded: /tmp/16285eeb-8659-4d50-b3fc-2387bb3f96fe

Whitelist

~~~
CN=NORTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com
CN=SOUTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com
~~~
whitelist uploaded: /tmp/dc995591-4657-40cc-976e-5855bea51949
Run: oc adm groups sync --sync-config=/tmp/16285eeb-8659-4d50-b3fc-2387bb3f96fe --whitelist=/tmp/dc995591-4657-40cc-976e-5855bea51949
~~~
apiVersion: v1
items:
- apiVersion: user.openshift.io/v1
  kind: Group
  metadata:
    annotations:
      openshift.io/ldap.sync-time: "2026-03-10T21:25:58Z"
      openshift.io/ldap.uid: CN=NORTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com
      openshift.io/ldap.url: ldap-server.domain.com:389
    labels:
      openshift.io/ldap.host: ldap-server.domain.com
    name: NORTH
  users:
  - n1@domain.com
  - n2@domain.com
  - n3@domain.com
- apiVersion: user.openshift.io/v1
  kind: Group
  metadata:
    annotations:
      openshift.io/ldap.sync-time: "2026-03-10T21:25:58Z"
      openshift.io/ldap.uid: CN=SOUTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com
      openshift.io/ldap.url: ldap-server.domain.com:389
    labels:
      openshift.io/ldap.host: ldap-server.domain.com
    name: SOUTH
  users:
  - s1@domain.com
  - s2@domain.com
  - s3@domain.com
kind: List
metadata: {}

~~~
Run: oc adm groups sync --sync-config=/tmp/16285eeb-8659-4d50-b3fc-2387bb3f96fe --whitelist=/tmp/dc995591-4657-40cc-976e-5855bea51949 --confirm

+----+----------+---------------+-----------------------------------------------------------------------+
| ID | Group    | User          | LDAP Sync                                                             |
+----+----------+---------------+-----------------------------------------------------------------------+
| 1  | NORTH    | n1@domain.com | ldap-server.domain.com                                                | 
|    |          | n2@domain.com | CN=NORTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com                       | 
|    |          | n3@domain.com | 2026-03-10T21:25:59Z                                                  | 
+----+----------+---------------+-----------------------------------------------------------------------+
| 2  | SOUTH    | s1@domain.com | ldap-server.domain.com                                                | 
|    |          | s2@domain.com | CN=SOUTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com                       | 
|    |          | s3@domain.com | 2026-03-10T21:25:59Z                                                  | 
+----+----------+---------------+-----------------------------------------------------------------------+

Create Namespace
----------------
- name: ldap-sync

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: ldap-sync

~~~

Namespace created

Wait for namespace [timeout:60]...

Create ServiceAccount
---------------------
- namespace: ldap-sync
- name: ldap-group-syncer

~~~
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ldap-group-syncer
  namespace: ldap-sync

~~~
ServiceAccount [ldap-sync/ldap-group-syncer] created
- wait for ServiceAccount ldap-sync/ldap-group-syncer [timeout:60s]

Create ClusterRole
------------------
- name: ldap-group-syncer

~~~
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: ldap-group-syncer
rules:
- apiGroups:
  - ''
  - user.openshift.io
  resources:
  - groups
  verbs:
  - get
  - list
  - create
  - update

~~~
ClusterRole [ldap-group-syncer] created
- wait for ClusterRole ldap-group-syncer [timeout:60s]

Create ClusterRoleBinding
-------------------------
- name: ldap-group-syncer

~~~
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: ldap-group-syncer
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: ldap-group-syncer
subjects:
- kind: ServiceAccount
  name: ldap-group-syncer
  namespace: ldap-sync

~~~
ClusterRoleBinding [ldap-group-syncer] created
- wait for ClusterRoleBinding ldap-group-syncer [timeout:60s]

Create ConfigMap
----------------
- namespace: ldap-sync
- name: ldap-group-syncer

~~~
apiVersion: v1
data:
  sync.yaml: |-
    apiVersion: v1
    bindDN: CN=bm1,OU=Users,OU=se,DC=se,DC=domain,DC=com
    bindPassword: secret
    insecure: true
    kind: LDAPSyncConfig
    rfc2307:
      groupMembershipAttributes:
      - member
      groupNameAttributes:
      - cn
      groupUIDAttribute: dn
      groupsQuery:
        baseDN: ou=Groups,ou=se,dc=se,dc=domain,dc=com
        derefAliases: never
        filter: (objectClass=group)
        pageSize: 0
        scope: sub
      tolerateMemberNotFoundErrors: false
      tolerateMemberOutOfScopeErrors: false
      userNameAttributes:
      - userPrincipalName
      userUIDAttribute: dn
      usersQuery:
        baseDN: ou=se,dc=se,dc=domain,dc=com
        derefAliases: never
        pageSize: 0
        scope: sub
    url: ldap://ldap-server.domain.com
kind: ConfigMap
metadata:
  name: ldap-group-syncer
  namespace: ldap-sync

~~~
ConfigMap [ldap-sync/ldap-group-syncer] created
- wait for ConfigMap ldap-sync/ldap-group-syncer [timeout:60s]

Whitelist

~~~
CN=NORTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com
CN=SOUTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com
~~~

Create ConfigMap
----------------
- namespace: ldap-sync
- name: ldap-whitelist-group-syncer

~~~
apiVersion: v1
data:
  whitelist.txt: |-
    CN=NORTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com
    CN=SOUTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com
kind: ConfigMap
metadata:
  name: ldap-whitelist-group-syncer
  namespace: ldap-sync

~~~
ConfigMap [ldap-sync/ldap-whitelist-group-syncer] created
- wait for ConfigMap ldap-sync/ldap-whitelist-group-syncer [timeout:60s]

Create CronJob
--------------
- namespace: ldap-sync
- name: ldap-group-syncer

~~~
apiVersion: batch/v1
kind: CronJob
metadata:
  name: ldap-group-syncer
  namespace: ldap-sync
spec:
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      backoffLimit: 0
      template:
        spec:
          activeDeadlineSeconds: 500
          containers:
          - command:
            - /bin/bash
            - -c
            - oc adm groups sync --sync-config=/etc/config/sync.yaml --whitelist=/etc/whitelist/whitelist.txt
              --confirm
            image: registry.redhat.io/openshift4/ose-cli:latest
            name: ldap-group-syncer
            volumeMounts:
            - mountPath: /etc/config
              name: ldap-sync-volume
            - mountPath: /etc/whitelist
              name: ldap-sync-whitelist
          dnsPolicy: ClusterFirst
          restartPolicy: Never
          serviceAccountName: ldap-group-syncer
          terminationGracePeriodSeconds: 30
          volumes:
          - configMap:
              name: ldap-group-syncer
            name: ldap-sync-volume
          - configMap:
              name: ldap-whitelist-group-syncer
            name: ldap-sync-whitelist
      ttlSecondsAfterFinished: 1800
  schedule: '*/30 * * * *'

~~~
CronJob [ldap-sync/ldap-group-syncer] created
- wait for CronJob ldap-sync/ldap-group-syncer [timeout:60s]

Completed tasks
- LDAP groups configured
```

[[Back]](./README.md) [[Prev]](./create_task.md) [[Next]](./delete.md)