## Provisioning - user data

[[Back]](./provisioned.md)

User data describes the desired configuration of the instance in a format specific to the first-boot software:
- cloud-init supports two formats: cloud-config YAML and a shell script (distinguished by the header).
- Ignition uses its own format.
- Glean does not support user data at all.

Example for cloud-init yaml

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: test-userdata
  namespace: openshift-machine-api
type: Opaque
stringData:
  userData: |
    #cloud-config
    users:
      - name: root
        lock_passwd: false
        ssh_authorized_keys:
          - ssh-ed25519 AAAA... user@hostname
      - name: cloud-user
        lock_passwd: false
        ssh_authorized_keys:
          - ssh-ed25519 AAAA... user@hostname
    chpasswd:
      list: |
        cloud-user:test123
        root:test123
      expire: false
    ssh_pwauth: true
    disable_root: false
    runcmd:
      - systemctl enable --now sshd
```

[[Back]](./provisioned.md)