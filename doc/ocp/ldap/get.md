# LDAP Identity Provider - Get

[[Back]](./README.md) [[Prev]](./delete_task_sync.md) [[Next]](./set.md)

## Workflow

- get `OAuth` crd with identityProviders of LDAP type
- get `Secret` crd with ldap password

## Requirements

None

## Configurable options

```
# iserver get ocp ldap
  --cluster TEXT  Cluster Name
```

## Example (view:state)

```
# iserver get ocp ldap --cluster bm1

OpenShift Workflow - Get LDAP Identity Provider
===============================================

OpenShift Cluster: bm1

+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+
| ID | OAuth   | Provider | LDAP                                                                               | Attribute                            | Usage    |
+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+
| 1  | cluster | ldap     | ldap://ldap-server.domain.com/ou=users,ou=se,dc=se,dc=domain,dc=com?sAMAccountName | id: sAMAccountName                   | User:  0 | 
|    |         |          | bindDN: CN=bm1,OU=Users,OU=se,DC=se,DC=domain,DC=com                               | name: cn                             | Group: 0 | 
|    |         |          | secret: ldap [exists:True]                                                         | email: mail                          |          | 
|    |         |          | mapping: claim                                                                     | preferredUsername: userPrincipalName |          |
+----+---------+----------+------------------------------------------------------------------------------------+--------------------------------------+----------+
```

[[Back]](./README.md) [[Prev]](./delete_task_sync.md) [[Next]](./set.md)