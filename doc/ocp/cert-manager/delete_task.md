# Certificate Manager - Delete via Task

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
- [feature](./disable.md), [issuer](./delete_issuer.md), [crt](./delete_crt.md), [wipe](./wipe.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [create task](./create_task.md)

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