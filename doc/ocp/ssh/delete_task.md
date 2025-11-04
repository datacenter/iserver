# OpenShift nodes ssh access - Delete via Task

## Input

```
[
    {
        "ssh": {
            "filename": [
              "key1.pub",
              "/tmp/key2.pub",
              "/tmp/mypubkeys
            ]
        }
    }
]
```

Notes:
- ssh keys to be added are defined with ssh.filename
- filename can be file or directory
- all files in the directory must be valid ssh public keys
- file or directory path must be absolute or relative to the location of task file

## Requirements

- all keys cannot be deleted

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


OpenShift Workflow - Delete SSH public key
==========================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Completed tasks
- SSH keys deleted
```

[[Back]](./README.md)