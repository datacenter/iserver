# NMState Operator - Create via Task

[[Back]](./README.md)

## Input

```
[
    {
        "nmstate": {
            "operator": {
              "channel": "abc"
            },
            "instace": {
              "filename": "xyz"
            },
            "lldp": {
              "fw": true|false(def),
              "include-down": true|false(def),
              "delete-nncp": true|false(def)
            }
        }
    }
]
```

Notes:
- [operator](./create_operator.md), [instance](./create_instance.md) and [lldp](./enable_lldp.md) trigger workflow execution with optional input parameters
- `operator.channel` optional with `stable` default
- `instance.filename` optional and must contain NMState CRD in YAML format
  - the path defined in operator.filename can be relative and then expected to be in the same directory as task.json file
  - the path defined in operator.filename can be absolute

## Requirements

None

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