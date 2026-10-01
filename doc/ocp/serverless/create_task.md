# Serverless - Create via Task

## HowTo

```
[
  {
    "serverless": {
      "operator": {
        "channel": "xyz"
      }
    }
  }
]
```

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm
```

Notes:
- [operator](./create_operator.md) triggers workflow execution with input parameters

[[Back]](./README.md)