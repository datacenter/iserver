# Helm

Check helm cli on the cluster [management node](../ManagementServer.md)

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

OpenShift Workflow - CLI - Get helm
===================================

OpenShift Cluster: bm1
~~~
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART                   APP VERSION
my-vast         vast-csi        1               2026-04-29 12:28:36.309264617 +0000 UTC deployed        vastcluster-v2.6.4                 
nfs             vast-csi        1               2026-04-29 12:28:23.631921721 +0000 UTC deployed        vastcsidriver-v2.6.4               
vast-nfs        vast-csi        1               2026-04-29 12:28:45.307760281 +0000 UTC deployed        vaststorage-v2.6.4                 
~~~

View: list (def), ver, all
```

[[Back]](./README.md)