# Certificate Manager - Create via Task

[[Back]](./README.md)

## Input

```
[
  {
    "cert-manager": {
      "feature": {},
      "issuer": [
        {
          "namespace": "default",
          "name": "default-root-ca",
          "crt": "root-ca.crt",
          "key": "root-ca.key"
        },
        {
          "name": "root-ca",
          "crt": "root-ca.crt",
          "key": "root-ca.key"
        }
      ],
      "crt": [
        {
          "namespace": "default",
          "name": "test1",
          "cn": "my-default",
          "issuer": "default-root-ca"
        },
        {
          "namespace": "default",
          "name": "test2",
          "cn": "abc",
          "issuer": "root-ca"
        }
      ],
      "wipe": {}
    }
  }
]
```

Notes:
- [feature](./enable.md), [issuer](./create_issuer.md), [crt](./create_crt.md) trigger workflow execution with optional input parameters
- [wipe](./wipe.md) workflow is ignored in create task
- you can reuse exactly the same input file that is used for [delete task](./delete_task.md)

## Requirements

None

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

[[Back]](./README.md)