# Cilium CNI - Get configuration

## Workflow

- get ciliumconfig object
- get cilium-config config map

## Requirements

None

## Configurable options

```
# iserver get ocp cilium config
  --cluster TEXT   Cluster Name
```

## Example

Note: actual cilium config and config map is not shown in the output

```
# iserver get ocp cilium state --cluster bm1 -v config


OpenShift Workflow - Get Cilium CNI
===================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- management node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok


Cilium Config
-------------
Processing error: False
Values error: False

cluster:
  name: default
...

Cilium Config Map
-----------------
...
```

[[Back]](./README.md)