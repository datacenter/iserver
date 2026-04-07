# OVNKubernetes BGP - Unconfigure via Task

## Input

```
[
    {
        "ovn-bgp": {
            "feature": {},
            "ra": {}
        }
    }
]
```

Notes:
- `feature` triggers [frr-k8s workflow execution](./feature_disable.md)
- `ra` triggers [route advertisement workflow execution](./ra_disable.md)

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

## Example

- [feature](./task_feature_disable.md)
- [ra](./task_ra_disable.md)

[[Back]](./README.md)