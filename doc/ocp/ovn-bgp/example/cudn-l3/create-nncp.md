# OVNKubernetes BGP - Cluster User Defined Network (L3)

[[Back]](./README.md) [[Task]](./create-nncp-task.md)

## Networking setup

Requirements
- dedicated physical interfaces (ens11f0, ens11f1) to leaf switches
- active/backup bond
- no vlan encapsulation
- route to leaf loopback interface via bond

## CRD

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: my-policy-c02b5dc7343e
spec:
  desiredState:
    interfaces:
    - ipv4:
        enabled: false
      name: ens11f0
      state: up
      type: ethernet
    - ipv4:
        enabled: false
      name: ens11f1
      state: up
      type: ethernet
```

> [!NOTE]
> Similar NodeNetworkConfigurationPolicy for bm1-2 and bm1-3 nodes

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: my-policy-a90afe482072
spec:
  desiredState:
    interfaces:
    - ipv4:
        address:
        - ip: 66.66.66.10
          prefix-length: 24
        dhcp: false
        enabled: true
      link-aggregation:
        mode: active-backup
        port:
        - ens11f0
        - ens11f1
      name: bond666
      state: up
      type: bond
  nodeSelector:
    kubernetes.io/hostname: bm1-1
```

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: my-policy-a2698d7bb743
spec:
  desiredState:
    routes:
      config:
      - destination: 6.6.6.6/32
        next-hop-address: 66.66.66.66
        next-hop-interface: bond666
      - destination: 6.6.6.7/32
        next-hop-address: 66.66.66.66
        next-hop-interface: bond666
```

[[Back]](./README.md) [[Task]](./create-nncp-task.md)