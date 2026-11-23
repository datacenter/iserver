# OpenShift Data Foundation (ODF) - Delete Cluster

## Workflow

- delete StorageCluster CRD 
- wait for cluster cleanup to complete
- delete rook filesystem from every cluster node

## Requirements

ODF cluster may not be used

## Configurable options

```
# iserver delete ocp odf --mode cluster
  --cluster TEXT                 Cluster Name
```

## Example

```
# iserver delete ocp odf --cluster bm1 --mode cluster

```

[[Back]](./README.md)