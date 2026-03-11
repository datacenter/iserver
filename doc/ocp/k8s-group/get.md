# Group - Get

## Workflow

- get all `Group` and `User` objects
- add tick if group user found

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
# iserver get k8s group --cluster bm1
Cluster: bm1 (type: ocp)

+----+------------------+-----------------------------------+------------------------------------------------+
| ID | Group            | User                              | LDAP Sync                                      |
+----+------------------+-----------------------------------+------------------------------------------------+
| 1  | ADMINS-XYZ       | user1@domain.com                  | ldapserver.domain.com                          |
|    |                  |                                   | CN=ADMINS-XYZ,OU=Groups,DC=domain,DC=com       |
|    |                  |                                   | 2026-03-05T16:04:55Z                           |
+----+------------------+-----------------------------------+------------------------------------------------+
| 2  | ADMINS-OPENSHIFT | [*] user2@domain.com              | ldapserver.domain.com                          |
|    |                  | user3@domain.com                  | CN=ADMINS-OPENSHIFT,OU=Groups,DC=domain,DC=com |
|    |                  |                                   | 2026-03-05T16:04:57Z                           |
+----+------------------+-----------------------------------+------------------------------------------------+
```

[[Back]](./README.md)