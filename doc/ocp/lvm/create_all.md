# LVM Storage Operator - Create All

## Workflow

Workflows deployed in sequence
- [create operator](./create_operator.md)
- [create cluster](./create_cluster.md)

## Requirements

None

## Configurable options

```
# iserver set ocp lvm --mode all
  --cluster TEXT                  Cluster Name
  --channel TEXT                  Operator channel  [default: __default__]
  --filename TEXT                 LVM Cluster
  --device TEXT                   Device names for lvm storage  
  --no-confirm                    Confirmation mode
```

[[Back]](./README.md)