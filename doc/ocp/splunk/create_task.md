# Splunk - Create via Task

[[Back]](./README.md)

## Input

```json
[
    {
        "splunk": {
            "operator": {
                "version": "3.1.0"
            },
            "instance": {
                "instance": [
                    {
                        "name": "inst1",
                        "etc-size": "10Gi",
                        "etc-sc": "lvms-vg1",
                        "var-size": "100Gi",
                        "var-sc": "lvms-vg1",
                        "sa": "default"
                    }
                ]
            }
        }
    }
]
```

Notes:
- [operator](./create_operator.md), and [instance](./create_instance.md) trigger workflow execution with optional input parameters
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

[[Back]](./README.md)