# SSH Access - Delete key

[[Back]](./README.md) [[task-way]](./delete_task.md) [[Add]](./create_key.md)

## Workflow

- identify machine config objects that define SSH keys; typically it will be 99-master-ssh and 99-worker-ssh
- download the content of machine config object into YAML file
- edit the yaml file to delete ssh keys
- apply machine config
- wait until machine config propagation across the cluster nodes is completed

> [!CAUTION]
> All keys cannot be deleted

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
# iserver delete ocp ssh --cluster bm1 --filename /tmp/ssh.pub --no-confirm

OpenShift Workflow - SSH Public Key - Delete
============================================

OpenShift Cluster: bm1

SSH public keys matching rules to be deleted
- AAAA...

Replace MachineConfig
---------------------
- name: 99-master-ssh

~~~
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: 99-master-ssh
spec:
  baseOSExtensionsContainerImage: ''
  config:
    ignition:
      version: 3.2.0
    passwd:
      users:
      - name: core
        sshAuthorizedKeys:
        - ssh-ed25519 AAAA...
          user@host1
  fips: false
  kernelArguments: null
  kernelType: ''
  osImageURL: ''
~~~
MachineConfig [99-master-ssh] replaced

Replace MachineConfig
---------------------
- name: 99-worker-ssh

~~~
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 99-worker-ssh
spec:
  baseOSExtensionsContainerImage: ''
  config:
    ignition:
      version: 3.2.0
    passwd:
      users:
      - name: core
        sshAuthorizedKeys:
        - ssh-ed25519 AAAA...
          user@host1
  fips: false
  kernelArguments: null
  kernelType: ''
  osImageURL: ''
~~~
MachineConfig [99-worker-ssh] replaced
Wait for machine config pool update...
- master
- worker

Completed tasks
- SSH keys deleted

+----+---------+-------+------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow   | Changes | Success | Duration [s] |
+----+---------+-------+------------+---------+---------+--------------+
| 1  | ocp:bm1 | ssh   | delete key | 2       | V       | 65           | 
+----+---------+-------+------------+---------+---------+--------------+
```

[[Back]](./README.md) [[task-way]](./delete_task.md) [[Add]](./create_key.md)