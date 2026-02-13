# Cilium Operator - Get operator leader logs

## Workflow

- get pods in `cilium` namespace
- select pods with label app.kubernetes.io/name = cilium-operator
- select pod with leader role based on cilium-operator-resource-lock lease
- get the logs of operator leader

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
# iserver get ocp cilium operator --cluster bm1 -v logs

OpenShift Workflow - Cilium - Get operator
==========================================

OpenShift Cluster: bm1

Cilium Operator Leader [cilium/cilium-operator-5dcc9dbf6f-7pnmc]
----------------------------------------------------------------
~~~
time=2026-02-04T17:58:19.277663683Z level=info msg="  --agent-not-ready-taint-key='node.cilium.io/agent-not-ready'" subsys=cilium-operator-generic
time=2026-02-04T17:58:19.277718508Z level=info msg="  --auto-create-cilium-pod-ip-pools=''" subsys=cilium-operator-generic
time=2026-02-04T17:58:19.277724637Z level=info msg="  --auto-create-default-pod-network='true'" subsys=cilium-operator-generic
...

```

[[Back]](./README.md)