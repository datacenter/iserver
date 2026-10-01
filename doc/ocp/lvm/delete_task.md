# LVM Storage - Delete via Task

## Input

```json
[
    {
        "lvm": {
            "operator": {},
            "cluster": {}
        }
    }
]
```

Notes:
- [operator](./delete_operator.md) and [cluster](./delete_cluster.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters may be silently ignored
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

[[Back]](./README.md)