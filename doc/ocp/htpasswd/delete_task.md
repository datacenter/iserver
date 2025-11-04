# HTPasswd Identity Provider - Delete via Task

## Input

```
[
    {
        "identity": {
            "type": "htpasswd",
            "provider": "custom",
            "filename": [
                "htpasswd.txt"
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
# iserver delete ocp task --filename C:\tmp\task.json --cluster bm1


OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Delete HTPasswd Identity Provider
======================================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\auser1wod\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

Deleting user [user1] and identity [custom:user1]
User already deleted, checking for identity leftover
Deleting user [user1] from cluster-admin group
Deleting user [user2] and identity [custom:user2]
User already deleted, checking for identity leftover
Deleting user [user2] from cluster-admin group
Deleting user [user3] and identity [custom:user3]
User already deleted, checking for identity leftover
Deleting user [user3] from cluster-admin group
Deleting user [user4] and identity [custom:user4]
User already deleted, checking for identity leftover
Deleting user [user4] from cluster-admin group
Deleting secret [openshift-config/custom]
Deleting htpasswd identity provider [custom]
Removing user [user1] from cluster-admin group
Removing user [user2] from cluster-admin group
Removing user [user3] from cluster-admin group
Removing user [user4] from cluster-admin group
```

[[Back]](../Operations.md)