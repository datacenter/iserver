# OpenShift Cluster with Cilium CNI

## Multi-node cluster

The reference [cluster input data](./uc2_cluster.md) defines single server

```
{
    "server": [
        {
            "hostname": "sno",
            "kube": true,
            ...
        }
    ]
}
```

If you want multi-node cluster
- add as many servers as needed into server list, following the same input format
- make sure only one server has kube:true, this is cluster management node where CLI tools are installed (if defined)
- in case of more that 3 servers are defined, assigne master or worker role using 'role' server attribute
- define ingress and api ip addresses e.g.

```
{
    "api": "10.6.6.10",
    "ingress": "10.6.6.11",
    "server": [
        {
            "hostname": "sno",
            "kube": true,
            ...
        }
    ]
}
```

[Back](./uc2.md)