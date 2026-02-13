# Cilium Configuration - Get configuration

## Workflow

- get `ciliumconfig` custom resource object
- show configuration spec and parsed status

## Requirements

None

## Configurable options

```
# iserver get ocp cilium config
  --cluster TEXT   Cluster Name
  -v, --view TEXT  [config|map|state|all]  [default: config]
```

## Example

```
# iserver get ocp cilium config --cluster bm1

OpenShift Workflow - Cilium - Get config
========================================

OpenShift Cluster: bm1

~~~
cluster:
  id: 1
  name: ocp
clusterHealthPort: 9940
...
~~~

Cilium config state
- processing error: False
- values error: False
```

[[Back]](./README.md)