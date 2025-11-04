# NVIDIA GPU Operator - Create All

## Workflow

Workflows deployed in sequence
- [create operator](./create_operator.md)
- [create policy](./create_policy.md)
- [create dashboard](./create_dashboard.md)

## Requirements

None

## Configurable options

```
# iserver set ocp gpu --mode all
  --cluster TEXT                  Cluster Name
  --channel TEXT                  Operator channel  [default: __default__]
  --filename TEXT                 NVIDIA Cluster Policy (optional with filename)
  --no-confirm                    Confirmation mode
```

[[Back]](./README.md)