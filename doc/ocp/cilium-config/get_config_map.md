# Cilium Configuration - Get configuration configmap

## Workflow

- get `cilium-config` configmap in `cilium` namespace

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
# iserver get ocp cilium config --cluster bm1 -v map

OpenShift Workflow - Cilium - Get config
========================================

OpenShift Cluster: bm1

Cilium Config Map
-----------------
agent-not-ready-taint-key: node.cilium.io/agent-not-ready
auto-direct-node-routes: false
...
```

[[Back]](./README.md)