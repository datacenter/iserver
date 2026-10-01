# Splunk - Delete via Task

[[Back]](./README.md)

## Input

```
[
    {
        "splunk": {
            "operator": {
                "channel": "channel-name"
            },
            "instance": [
                {
                    "instance": "instance-name"
                }
            ]
        }
    }
]
```

Notes:
- [instance](./delete_instance.md) and [operator](./delete_operator.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md), some parameters may be silently ignored
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

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