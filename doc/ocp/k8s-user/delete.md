# User - Delete

## Workflow

- get all `User` and `Identity` objects
- delete selected users with associated identities

## Configurable options

```
# iserver get k8s group
  --cluster TEXT                  Cluster name
  --name TEXT                     Filter by name
  --ldap-host TEXT                Synced from ldap host
  --ldap                          Synced from ldap
```

## Example

```
# iserver delete k8s group --cluster bm1 --name akaliwod

OpenShift Workflow - OAuth - Delete User
========================================

OpenShift Cluster: bm1

+----+---------------------+--------------------+-------+-----------------------+---------------+---------------+
| ID | User                | Full Name          | Group | Identity              | Provider Name | Provider User |
+----+---------------------+--------------------+-------+-----------------------+---------------+---------------+
| 1  | akaliwod            | ---                | ---   | local-admins:akaliwod | local-admins  | akaliwod      | 
| 2  | akaliwod@domain.com | Arkadiusz Kaliwoda | ---   | ldap:YWthbGl3b2Q      | ldap          | YWthbGl3b2Q   | 
+----+---------------------+--------------------+-------+-----------------------+---------------+---------------+

Delete user
-----------
- user: akaliwod
- with identities

Delete User
-----------
- name: akaliwod
- deleted
- wait for no User akaliwod [timeout:60s]

Delete Identity
---------------
- name: local-admins:akaliwod

Delete Identity
---------------
- name: local-admins:akaliwod
- deleted
- wait for no Identity local-admins:akaliwod [timeout:60s]

Delete user
-----------
- user: akaliwod@domain.com
- with identities

Delete User
-----------
- name: akaliwod@domain.com
- deleted
- wait for no User akaliwod@domain.com [timeout:60s]

Delete Identity
---------------
- name: ldap:YWthbGl3b2Q

Delete Identity
---------------
- name: ldap:YWthbGl3b2Q
- deleted
- wait for no Identity ldap:YWthbGl3b2Q [timeout:60s]

Completed tasks
- Selected users deleted
```

[[Back]](./README.md)