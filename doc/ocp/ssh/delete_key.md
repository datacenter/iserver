# OpenShift nodes ssh access - Delete key

## Workflow

- identify machine config objects that define SSH keys; typically it will be 99-master-ssh and 99-worker-ssh
- download the content of machine config object into YAML file
- edit the yaml file to delete ssh keys
- apply machine config
- wait until machine config propagation across the cluster nodes is completed

## Requirements

- all keys cannot be deleted

## Configurable options

Filename
- can be defined multiple times
- can be directory
- all files in the directory must be valid ssh public keys

Key
- can be defined multiple times
- selects configured public key by any substring match

```
# iserver delete ocp ssh
  --cluster TEXT              Cluster name
  --role [any|master|worker]  [default: any]
  --filename TEXT             SSH public key to be deleted
  --key TEXT                  SSH public key search pattern to be removed
  --no-wait                   No-wait for mcp update
```

## Example

```
# iserver delete ocp ssh --cluster bm1 --filename /tmp/ssh.pub

OpenShift Workflow - Delete SSH public key
==========================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok

Wait for machine config pool update...
- master
- worker

Completed tasks
- SSH keys deleted
```

[[Back]](./README.md)