# Private Network - Disable webhook

[[Back]](./README.md)

Private network webhook is required for [VM migration](../vm-migration-inb/) use case where migrated virtual machine from e.g., VMWare cluster will be connected to private network instead of default network. 

If webhook is disabled, migrated virtual machine connects to default network, even if private network exists.

## Workflow

- check cilium cni operator state
- check current cilium configuration
- check private network feature [enabled](./enable.md)
- disable private network webhook if not already disbled
- check if mutating webhook is gone automatically
- delete the mututating webhook otherwise

## Requirements

None

## Expected outcome

- Mutating webhook deleted

## Configurable options

```
# iserver delete ocp cilium pnet --mode webhook
  --cluster TEXT     Cluster Name
  --no-confirm       Confirmation mode
```

## Example

```
# iserver delete ocp cilium pnet --cluster bm1 --mode webhook

OpenShift Workflow - Cilium - Disable Private Network Webhook
=============================================================

OpenShift Cluster: bm1
Cilium cni found
Private network enabled

Cilium config update
--------------------
CiliumConfig CRD patched
Wait for mutating webhook being deleted...
[ERROR] timed out

Delete Mutating Webhook
-----------------------
- name: kubevirt-privnet-integration-webhook

Mutating webhook deleted

Wait for no mutating webhook...

Completed tasks
- Private Network webhook disabled
```

[[Back]](./README.md)