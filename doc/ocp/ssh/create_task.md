# SSH Access - Create via Task

[[Back]](./README.md) [[cli-way]](./create_key.md) [[Delete]](./delete_task.md)

## HowTo

```json
[
  {
    "ssh": {
      "key": {
        "filename": [
          "key1.pub",
          "/tmp/key2.pub",
          "/tmp/mypubkeys"
        ]
      }
    }
  }
]
```

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm
```

Notes:
- filename item can be file or directory
- all files in the directory must be valid ssh public keys
- file or directory path must be absolute or relative to the location of task file

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
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

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
| 1  | ocp:bm1 | ssh   | create key | 2       | V       | 75           | 
+----+---------+-------+------------+---------+---------+--------------+
```

[[Back]](./README.md) [[cli-way]](./create_key.md) [[Delete]](./delete_task.md)