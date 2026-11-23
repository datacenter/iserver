# NMState Operator - Delete via Task

[[Back]](./README.md)

## Input

```
[
    {
        "nmstate": {
            "operator": {},
            "instace": {}
        }
    }
]
```

Notes:
- [operator](./delete_operator.md), [instace](./delete_instance.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters are silently ignored

## Requirements

None

## Configurable options

```
# iserver delete ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

[[Back]](./README.md)