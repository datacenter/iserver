# Private Network - Enable webhook

[[Back]](./README.md)

Private network webhook is required for [VM migration](../vm-migration-inb/) use case where migrated virtual machine from e.g., VMWare cluster will be connected to private network instead of default network. 

## Workflow

- check cilium cni operator state
- check current cilium configuration
- check private network feature [enabled](./enable.md)
- enable private network webhook if not already enabled
- check if mutating webhook exists

Cilium configuration patch

```
enterprise:
  privateNetworks:
    webhook:
      enabled: true
      tls:
        auto:
          enabled: true
          method: servingcert
```

## Requirements

- private network [enabled](./enable.md)

## Expected outcome

- Mutating webhook created
- Service created

## Configurable options

```
# iserver set ocp cilium pnet --mode webhook
  --cluster TEXT     Cluster Name
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp cilium pnet --cluster bm1 --mode webhook

OpenShift Workflow - Cilium - Enable Private Network Webhook
============================================================

OpenShift Cluster: bm1
Cilium cni found
Private network enabled
~~~
enterprise:
  privateNetworks:
    webhook:
      enabled: true
      tls:
        auto:
          enabled: true
          method: servingcert

~~~

Cilium config update
--------------------
CiliumConfig CRD patched
Wait for mutating webhook being created...

Completed tasks
- Private Network webhook enabled and ready
```

[[Back]](./README.md)