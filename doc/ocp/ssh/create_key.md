# SSH Access - Add key

[[Back]](./README.md) [[task-way]](./create_task.md) [[Delete]](./delete_key.md)

## Workflow

- identify machine config objects that define SSH keys; typically it will be `99-master-ssh` and `99-worker-ssh`
- download the content of machine config object into YAML file
- edit the yaml file to add ssh keys
- apply machine config
- wait until machine config propagation across the cluster nodes is completed

## Configurable options

Filename
- can be defined multiple times
- can be directory
- all files in the directory must be valid ssh public keys

```
# iserver set ocp ssh 
  --cluster TEXT              Cluster name
  --role [any|master|worker]  [default: any]
  --filename TEXT             SSH public key to be added [multiple]
  --no-wait                   No-wait for mcp update
```

## Example

```
# iserver set ocp ssh --cluster bm1 --filename /tmp/ssh.pub --no-confirm

OpenShift Workflow - SSH Public Key - Add
=========================================

OpenShift Cluster: bm1

SSH public keys matching rules to be deleted
- ssh-ed25519 AAAA... user@host2
New master keys [1] will be added

Replace MachineConfig
---------------------
- name: 99-master-ssh

~~~
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  resourceVersion: '10570249'
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
        - ssh-ed25519 AAAA...
          user@host2
  fips: false
  kernelArguments: null
  kernelType: ''
  osImageURL: ''
~~~
MachineConfig [99-master-ssh] replaced
New worker keys [1] will be added

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
        - ssh-ed25519 AAAA...
          user@host2
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
- SSH keys added

+----+---------+-------+------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow   | Changes | Success | Duration [s] |
+----+---------+-------+------------+---------+---------+--------------+
| 1  | ocp:bm1 | ssh   | create key | 2       | V       | 65           | 
+----+---------+-------+------------+---------+---------+--------------+
```

[[Back]](./README.md) [[task-way]](./create_task.md) [[Delete]](./delete_key.md)