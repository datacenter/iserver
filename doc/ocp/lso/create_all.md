# Local Storage Operator - Create operator and volumes

## Workflow

Workflows deployed in sequence
- [create operator](./create_operator.md)
- [create volume](./create_volume.md)

## Requirements

None

## Configurable options

```
# iserver set ocp lso --mode all
  --cluster TEXT                Cluster Name
  --nso                         Enable node selector override namespace annotation [default: false]
  --channel TEXT                Operator channel  [default: __default__]
  --device TEXT                 Device for local volumes
  --sc TEXT                     Storage class name  [default: local-sc]
  --limit TEXT                  Device discovery limitations
  --volume [block|fs]           Volume mode  [default: block]
  --fs TEXT                     Filesystem type if filesystem volume [default: ext4]
  --max INTEGER                 Max discovered devices per node (default unlimited)  [default: -1]
  --no-confirm                  Confirmation mode  
```

[[Back]](./README.md)