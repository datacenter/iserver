# Cilium Agent - Get logs

## Workflow

- get pods in `cilium` namespace
- select pods with label app.kubernetes.io/name = cilium-agent
- optionally select agent pod by `--name`
- get the logs of cilium agent pods

## Requirements

None

## Configurable options

```
# iserver get ocp cilium agent
  --cluster TEXT   Cluster Name
  --name TEXT      Agent name
  -v, --view TEXT  [pod|logs]  [default: pod]
```

## Example

```
# iserver get ocp cilium agent --cluster bm1 --name cilium-4ccpl -v logs

OpenShift Workflow - Cilium - Get agent
=======================================

OpenShift Cluster: bm3

Cilium Agent [cilium/cilium-4ccpl]
----------------------------------
~~~
time=2026-02-12T08:11:09.154502071Z level=info msg="Memory available for map entries (0.250% of 404311371776B): 1010778429B"
time=2026-02-12T08:11:09.154551707Z level=info msg="option bpf-ct-global-tcp-max set by dynamic sizing to 3546590"
time=2026-02-12T08:11:09.154558934Z level=info msg="option bpf-ct-global-any-max set by dynamic sizing to 1773295"
...
```

[[Back]](./README.md)