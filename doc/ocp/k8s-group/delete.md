# Group - Delete

## LDAP group prunning

Kubernetes groups synced from LDAP can be removed using 

```
# iserver delete k8s group --cluster bm1 --ldap
```

Similar task can run with 'oc adm prune groups' as long as the same sync configuration is used as explained [here](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/authentication_and_authorization/ldap-syncing#ldap-syncing-pruning_ldap-syncing-groups)

```
# oc adm prune groups --sync-config=/path/to/ldap-sync-config.yaml --confirm
```

## Configurable options

```
# iserver delete k8s group
  --cluster TEXT    Cluster Name
  --name TEXT       Select by group name
  --ldap-host TEXT  Synced from ldap host
  --ldap            Synced from ldap
  --no-confirm      No confirmation mode
```

## Example

```
# iserver delete k8s group --cluster bm1 --ldap --no-confirm

OpenShift Workflow - OAuth - Delete Group
=========================================

OpenShift Cluster: bm1

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

Delete Group
------------
- name: ADMINS-XYZ
- deleted
- wait for no Group ADMINS-XYZ [timeout:60s]

Delete Group
------------
- name: ADMINS-OPENSHIFT
- deleted
- wait for no Group ADMINS-OPENSHIFT [timeout:60s]

Completed tasks
- Selected groups deleted
```

[[Back]](./README.md)