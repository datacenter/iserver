# LDAP Identity Provider - Delete via Task

[[Back]](./README.md) [[Prev]](./delete.md) [[Next]](./delete_task_sync.md)

## Input

```
[
    {
        "identity": {
            "type": "ldap",
            "provider": "ldap",
            "url": "ldap://ldap-server.domain.com/ou=users,ou=se,dc=se,dc=domain,dc=com?sAMAccountName",
            "bind": "CN=bm1,OU=Users,OU=se,DC=se,DC=domain,DC=com",
            "secret": "secret",
            "id": [
              "sAMAccountName"
            ],
            "name": [
              "cn"
            ],
            "email": [
              "mail"
            ],
            "username": [
              "userPrincipalName"
            ],
            "insecure": true
        }
    }
]  
```

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


OpenShift Workflow - LDAP Identity Provider - Delete
====================================================

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
ldap:
  attributes:
    email:
    - mail
    id:
    - sAMAccountName
    name:
    - cn
    preferredUsername:
    - userPrincipalName
  bindDN: CN=bm1,OU=Users,OU=se,DC=se,DC=domain,DC=com
  bindPassword:
    name: ldap
  insecure: true
  url: ldap://ldap-server.domain.com/ou=users,ou=se,dc=se,dc=domain,dc=com?sAMAccountName
mappingMethod: claim
name: ldap
type: LDAP

~~~

No users from identity provider

No groups from identity provider

Delete identity provider from oauth
-----------------------------------
- oauth: cluster
- provider: ldap

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
  - htpasswd:
      fileData:
        name: local-admins
    mappingMethod: claim
    name: local-admins
    type: HTPasswd

~~~
OAuth [cluster] replaced

OAuth restart
- wait for no Pod openshift-authentication/oauth-openshift-7bc9ccdfb7-76gzd [timeout:180s]
- wait for no Pod openshift-authentication/oauth-openshift-7bc9ccdfb7-g2fn6 [timeout:180s]
- wait for no Pod openshift-authentication/oauth-openshift-7bc9ccdfb7-nrdtv [timeout:180s]
- wait for deployment openshift-authentication/oauth-openshift ready state [timeout:180s]

Delete Secret
-------------
- namespace: openshift-config
- name: ldap
- wait for no secret

Completed tasks
- LDAP Identity Provider deleted with dependencies
```

[[Back]](./README.md) [[Prev]](./delete.md) [[Next]](./delete_task_sync.md)