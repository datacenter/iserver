# Grafana Operator - Delete via Task

## Input

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

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm
```

Notes:
- [crd](./delete_crd.md), [wipe](./delete_wipe.md) and [operator](./delete_operator.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some tasks or task parameters may be silently ignored
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies
- if you want to clean up setup, use "wipe" option in case some crds are not deleted in task way
- "wipe" option in [create task](./create_task.md) is ignored

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