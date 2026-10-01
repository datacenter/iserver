# Splunk - Create via Task

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
- [operator](./create_operator.md), and [instance](./create_instance.md) trigger workflow execution with optional input parameters
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

[[Back]](./README.md)