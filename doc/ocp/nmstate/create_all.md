# MMState Operator - Create All

[[Back]](./README.md)

## Workflow

Workflows deployed in sequence
- [create operator](./create_operator.md)
- [enable lldp](./enable_lldp.md)

## Requirements

None

## Configurable options

```
# iserver set ocp nmstate --mode all
  --cluster TEXT              Cluster Name
  --channel TEXT              Operator channel  [default: __default__]
  --filename TEXT             NMState CRD
  --fw                        Disable LLDP on NIC fw level
  --keep-nncp                 Keep NNCP
  --skip-down                 Skip interfaces down
  --no-confirm                Confirmation mode
```

[[Back]](./README.md)