# OpenShift nodes ssh access - Get keys

## Workflow

- identify machine config objects that define SSH keys; typically it will be 99-master-ssh and 99-worker-ssh
- download the content of machine config object into YAML file
- show public keys

## Requirements

None

## Configurable options

```
# iserver set ocp nfd --mode operator
  --cluster TEXT              Cluster name
```

## Example

```
# iserver get ocp ssh --cluster bm1 

OpenShift Workflow - Get SSH public keys
========================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


+--------------------------------+-------------+-------------------------+----------------------+
| Id                             | Type        | Key                     | Node                 |
+--------------------------------+-------------+-------------------------+----------------------+
| user1@host1                    | ssh-ed25519 | AAAAC3NzaC...UDXorVCR71 | ['master', 'worker'] |
+--------------------------------+-------------+-------------------------+----------------------+
| user2@host2                    | ssh-ed25519 | AAAAC3NzaC...xtIULcEKAJ | ['master', 'worker'] |
+--------------------------------+-------------+-------------------------+----------------------+
```

[[Back]](./README.md)