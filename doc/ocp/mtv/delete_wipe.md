# Migration Toolkit for Virtualization - Delete Migration Resources (Wipe)

## Workflow

Run workflows:
- [delete plans](./delete_plan.md)
- [delete network maps](./delete_network_map.md)
- [delete storage maps](./delete_storage_map.md)
- [delete provider](./delete_providers.md)

Note: failing workflow stops execution

## Requirements

mtv operator [installed](./create_operator.md)

## Configurable options

```
# iserver delete ocp mtv --mode wipe
  --cluster TEXT                  Cluster Name
  --no-confirm                    Confirmation mode
```

[[Back]](./README.md)