# CNI

## Default CNI

```
    "network_type": "OVNKubernetes"
```

## Other CNI

```
    "network_type": "Cilium",
    "variables": {
        "CLUSTER_NETWORK_CIDR": "10.128.0.0/14",
        "CLUSTER_NETWORK_HOST_PREFIX": "23"
    },
```

Cilium requires manifests subdirectory. Manifest yaml files may have variables specially in cluster-network-07-cilium-ciliumconfig.yaml that has references to CIDRs defined at base level.

Note:
- even if cluster_network_cidr defines the Network CIDR, you have to define it manually as variable and make sure variable name matches ${VAR} in manifest

[Back](../BareMetalCluster.md)
