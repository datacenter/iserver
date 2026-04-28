# Node Feature Discovery Operator - Delete via Task

[[Back]](./README.md) [[Next]](./get.md) [[Prev]](./delete_instance.md)

## HowTo

```
[
  {
    "nfd": {
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

[[Back]](./README.md) [[Next]](./get.md) [[Prev]](./delete_instance.md)