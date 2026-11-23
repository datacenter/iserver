# LDAP Identity Provider - Group Sync - Delete via Task

[[Back]](./README.md) [[Prev]](./delete_task.md) [[Next]](./get.md)

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


OpenShift Workflow - LDAP Group - Sync Prune
============================================

OpenShift Cluster: bm1

Delete CronJob
--------------
- namespace: ldap-sync
- name: ldap-group-syncer
- deleted
- wait for no CronJob ldap-sync/ldap-group-syncer [timeout:60s]

Delete Config Map
-----------------
- namespace: ldap-sync
- name: ldap-group-syncer
- wait for no config map

Delete Config Map
-----------------
- namespace: ldap-sync
- name: ldap-whitelist-group-syncer
- wait for no config map

Delete Config Map
-----------------
- namespace: ldap-sync
- name: ldap-blacklist-group-syncer
- already deleted

Delete Cluster Role Binding
---------------------------
- name: ldap-group-syncer
- wait for no cluster role binding

Delete Cluster Role
-------------------
- name: ldap-group-syncer
- wait for no cluster role

Delete ServiceAccount
---------------------
- namespace: ldap-sync
- name: ldap-group-syncer
- deleted
- wait for no ServiceAccount ldap-sync/ldap-group-syncer [timeout:60s]

Delete Namespace
----------------
- name: ldap-sync

Namespace [ldap-sync] resources
- no pods
- no deployments
- no daemon sets
- no replica sets
- no services
- no pvcs
- wait for no namespace

+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+
| ID | OAuth   | Provider | LDAP                                                                               | Attribute                            | Usage    |
+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+
| 1  | cluster | ldap     | ldap://ldap-server.domain.com/ou=users,ou=se,dc=se,dc=domain,dc=com?sAMAccountName | id: sAMAccountName                   | User:  0 | 
|    |         |          | bindDN: CN=bm1,OU=Users,OU=se,DC=se,DC=domain,DC=com                               | name: cn                             | Group: 2 | 
|    |         |          | secret: ldap [exists:True]                                                         | email: mail                          |          | 
|    |         |          | mapping: claim                                                                     | preferredUsername: userPrincipalName |          |
+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+

+----+----------+---------------+-----------------------------------------------------------------------+
| ID | Group    | User          | LDAP Sync                                                             |
+----+----------+---------------+-----------------------------------------------------------------------+
| 1  | NORTH    | n1@domain.com | ldap-server.domain.com                                                | 
|    |          | n2@domain.com | CN=NORTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com                       | 
|    |          | n3@domain.com | 2026-03-11T07:38:05Z                                                  | 
+----+----------+---------------+-----------------------------------------------------------------------+
| 2  | SOUTH    | s1@domain.com | ldap-server.domain.com                                                | 
|    |          | s2@domain.com | CN=SOUTH,OU=Groups,OU=se,DC=se,DC=domain,DC=com                       | 
|    |          | s3@domain.com | 2026-03-11T07:38:05Z                                                  | 
+----+----------+---------------+-----------------------------------------------------------------------+

Delete Group
------------
- name: NORTH
- deleted
- wait for no Group NORTH [timeout:60s]

Delete Group
------------
- name: SOUTH
- deleted
- wait for no Group SOUTH [timeout:60s]

Completed tasks
- LDAP groups deleted
```

[[Back]](./README.md) [[Prev]](./delete_task.md) [[Next]](./get.md)