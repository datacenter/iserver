```shell
iserver set ocp cilium pnet --mode feature --pnet local-access
iserver set ocp cilium pnet --mode multus
```

fix: multus change should restart cilium
one-step (?)

```yaml
enterprise:
  privateNetworks:
    enabled: true
    mode: local-access
    networkAttachmentDefinitions:
      enabled: true
```