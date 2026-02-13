# Helm

Check helm cli on the cluster [management node](../Access.md)

## Workflow

- check helm via ssh on the cluster management node

## Requirements

Cluster [connector](../Access.md) must be defined with management ip
Ssh access to management node must work

## Configurable options

```
# iserver get ocp cli-helm 
  --cluster TEXT  OCP cluster name
```

## Example

```
# iserver get ocp cli-helm --cluster bm1

OpenShift Workflow - Check helm cli
===================================

OpenShift Cluster: bm1
Helm found and ready
~~~
version.BuildInfo{Version:"v3.19.0", GitCommit:"3d8990f0836691f0229297773f3524598f46bda6", GitTreeState:"clean", GoVersion:"go1.24.7"}

~~~
```

[[Back]](./README.md)