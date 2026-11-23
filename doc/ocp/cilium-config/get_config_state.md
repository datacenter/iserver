# Cilium Configuration - Get configuration state

## Workflow

- get `ciliumconfig` custom resource object
- show parse state

## Requirements

None

## Configurable options

```
# iserver get ocp cilium config
  --cluster TEXT   Cluster Name
  -v, --view TEXT  [config|map|state|all]  [default: config]
```

## Example (all good)

```
# iserver get ocp cilium config --cluster bm1 -v state 

OpenShift Workflow - Cilium - Get config
========================================

OpenShift Cluster: bm1

Cilium config state
- processing error: False
- values error: False
```

## Example (error)

```
# iserver get ocp cilium config --cluster bm1 -v state 

OpenShift Workflow - Cilium - Get config
========================================

OpenShift Cluster: bm1

Cilium config state
- processing error: True [reason:HelmError]
~~~
helm cannot generate manifests: error processing charts: values don't meet the specifications of the schema(s) in the following chart(s):
cilium:
- at '/hubble/enabled': got string, want boolean

~~~
- values error: False
```

[[Back]](./README.md)