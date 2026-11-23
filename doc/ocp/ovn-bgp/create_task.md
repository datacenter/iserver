# OVNKubernetes BGP - Configure via Task

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
- `feature` triggers [frr-k8s workflow execution](./feature_enable.md)
- `ra` triggers [route advertisement workflow execution](./ra_enable.md)

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

## Example

- [feature](./task_feature_enable.md)
- [ra](./task_ra_enable.md)

[[Back]](./README.md)