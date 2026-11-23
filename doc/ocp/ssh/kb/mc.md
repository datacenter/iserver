# SSH Access Management via Machine Config

[[Back]](../README.md)

RedHat CoreOS contains a single user **core** with ssh key defined during [installation](../../bm/input_data_ssh_pub.md). This configuration is propagated to two MachineConfig objects `99-master-ssh` and `99-worker-ssh`. Note: showing one for brevity

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 99-master-ssh
spec:
  baseOSExtensionsContainerImage: ""
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
  kernelType: ""
  osImageURL: "" 
```

Changes to `sshAuthorizedKeys` property of MachineConfig specification trigger MachineConfigPool update triggered by Machine Config Operator. Once the mcp changes are applied, ssh authorized_keys file on desired hosts is following the MachineConfig specification.

## Note on authorized_keys file location

File: /etc/ssh/sshd_config.d/40-ssh-key-dir.conf

```
# sshd_config drop-in for /etc/ssh/sshd_config.d

# Use ssh-key-dir to read all SSH keys from ~/.ssh/authorized_keys.d
AuthorizedKeysCommand /usr/libexec/ssh-key-dir %u

# ssh-key-dir needs to be able to seteuid to the target user
AuthorizedKeysCommandUser root
```

As such ssh keys are in authorized_keys.d directory

```
$ find .ssh/
.ssh/
.ssh/authorized_keys.d
.ssh/authorized_keys.d/ignition
```

```
$ cat .ssh/authorized_keys.d/ignition 
ssh-ed25519 AAAA... user1@host
```

[[Back]](../README.md)