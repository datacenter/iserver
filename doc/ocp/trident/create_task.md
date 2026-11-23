# Trident - Create via Task

[[Back]](./README.md)

## HowTo

```
[
  {
    "trident": {
      "operator": {
        "channel": "xyz"
      },
      "instance": {
        "filename": "xyz"
      }
    }
  }
]
```

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm
```

Notes:
- [operator](./create_operator.md) and [instance](./create_instance.md) triggers workflow execution with input parameters

[[Back]](./README.md)