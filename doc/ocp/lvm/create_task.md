# LVM Storage - Create via Task

## Default generated LVMCluster CRD

```json
[
    {
        "lvm": {
            "operator": {
                "channel": "abc"
            },
            "cluster": {
            }
        }
    }
]
```

## Device-based generated LVMCluster CRD

```json
[
    {
        "lvm": {
            "operator": {
                "channel": "abc"
            },
            "cluster": {
                "device": [
                  "sda",
                  "sdb"
                ]
            }
        }
    }
]
```

## Custom LVMCluster CRD


```json
[
    {
        "lvm": {
            "operator": {
                "channel": "abc"
            },
            "cluster": {
                "filename": "xyz"
            }
        }
    }
]
```

Notes:
- [operator](./create_operator.md) and [cluster](./create_cluster.md) trigger workflow execution with optional input parameters
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies
- cluster.filename is optional must contain LVMCluster CRD in YAML format
  - the path defined in cluster.filename can be relative and then expected to be in the same directory as task.json file
  - the path defined in cluster.filename can be absolute

[[Back]](./README.md)