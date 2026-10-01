# SSH Access - Delete via Task

[[Back]](./README.md) [[cli-way]](./delete_key.md) [[Add]](./create_task.md)

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
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm
```

> [!CAUTION]
> All keys cannot be deleted

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
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

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
| 1  | ocp:bm1 | ssh   | delete key | 2       | V       | 77           | 
+----+---------+-------+------------+---------+---------+--------------+
```

[[Back]](./README.md) [[cli-way]](./delete_key.md) [[Add]](./create_task.md)