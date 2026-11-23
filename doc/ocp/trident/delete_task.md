# Trident - Delete via Task

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
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json
```

Notes:
- [operator](./delete_operator.md) and [instance](./delete_instance.md) parameters are ignored for delete workflow

[[Back]](./README.md)