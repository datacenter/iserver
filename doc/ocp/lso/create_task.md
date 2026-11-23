# Local Storage - Create via Task

[[Back]](./README.md)

## Input

```
[
    {
        "lso": {
            "operator": {},
            "volume": {
                "sc": "local-sc",
                "device": ["bm1-1:wwn-0x500a075118ef25c1", "bm1-2:wwn-0x500a075118ef266c"],
                "volume": "block",
                "max": 2,
                "limit": ["type:disk"]
            }
        }
    }
]
```

Notes:
- [operator](./create_operator.md) and [volume](./create_volume.md) trigger workflow execution with optional input parameters
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

[Back](./README.md)