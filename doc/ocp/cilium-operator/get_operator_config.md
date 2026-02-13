# Cilium Operator - Get operator configuration

## Workflow

- get `ciliumconfig` custom resource object
- show `spec:operator` section

## Requirements

None

## Configurable options

```
# iserver get ocp cilium operator
  --cluster TEXT   Cluster Name
  -v, --view TEXT  [pod|config|logs]  [default: pod]
```

## Example

```
# iserver get ocp cilium operator --cluster bm1 -v config

OpenShift Workflow - Cilium - Get operator
==========================================

OpenShift Cluster: bm1

Operator Configuration
----------------------
~~~
operator:
  prometheus:
    enabled: true
    serviceMonitor:
      enabled: true

~~~
```

[[Back]](./README.md)