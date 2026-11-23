# Local Storage - Delete via Task

## Input

```
[
    {
        "lso": {
            "operator": {},
            "volume": {}
        }
    }
]
```

Notes:
- [volume](./delete_volume.md) and [operator](./delete_operator.md) trigger workflow execution
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters may be silently ignored
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

[[Back]](./README.md)