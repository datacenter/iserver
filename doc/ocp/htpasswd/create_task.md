# HTPasswd Identity Provider - Create via Task

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

## Expected outcome

![Htpasswd](../images/htpasswd.png)

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
# iserver set ocp task --filename C:\tmp\task.json --cluster bm1

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Add HTPasswd Identity Provider
===================================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

OAuth updated with htpasswd [custom]
Secret openshift-config/custom created
Add username user1 to cluster admins group
Add username user2 to cluster admins group
Add username user3 to cluster admins group
Add username user4 to cluster admins group
```

[[Back]](../Operations.md)