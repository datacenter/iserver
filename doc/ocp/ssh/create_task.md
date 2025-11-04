# OpenShift nodes ssh access - Create via Task

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

None

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


OpenShift Workflow - Add SSH public key
=======================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

Wait for machine config pool update...
- master
- worker

Completed tasks
- SSH keys added
```

[[Back]](./README.md)