# Node Feature Discovery Operator - Create via Task

[[Back]](./README.md) [[Next]](./delete_operator.md) [[Prev]](./create_instance.md)

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
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm
```

Notes:
- [operator](./create_operator.md) and [instance](./create_instance.md) triggers workflow execution with input parameters

[[Back]](./README.md) [[Next]](./delete_operator.md) [[Prev]](./create_instance.md)