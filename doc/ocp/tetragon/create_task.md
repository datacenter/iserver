# Tetragon Operator - Create via Task

## HowTo

```json
[
    {
        "tetragon": {
            "operator": {
                "version": "1.19.4"
            },
            "crd": {
                "filename": [
                    "policy/policy.yaml"
                ]
            },
            "wipe": {}
        }
    }
]
```

Notes:
- [operator](./create_operator.md), [crd](./create_crd.md) trigger workflow execution with optional input parameters
- [wipe](./delete_wipe.md) is ignored in create task

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

[[Back]](./README.md)