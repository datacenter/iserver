# Node - Reboot

## Workflow

- reboot the node using 'sudo reboot' via ssh
- wait for node ssh access
- wait for k8s api
- wait for node ready

## Requirements

[SSH access](../Access.md) to cluster nodes


## Configurable options

- use --node multiple times in case you want to gracefully reload multiple nodes one after another

```
# iserver set ocp node reboot
  --cluster TEXT  OCP cluster name
  --node TEXT     Node name
```

## Example

```

OpenShift Workflow - Node reboot
================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "node": [
        "bm1-3"
    ],
    "wait": true,
    "sequential": true,
    "max-time": 600,
    "check-verbose": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok
- cluster node [*****]: ok

Node [bm1-3] cli [sudo reboot]


Wait for node [bm1-3] up
- ssh
- k8s api
- node ready
```

[[Back]](./README.md)