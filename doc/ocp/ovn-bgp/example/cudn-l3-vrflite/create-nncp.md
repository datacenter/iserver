# OVNKubernetes BGP - Cluster User Defined Network (L3) w/VRF-Lite

[[Back]](./README.md) [[Task]](./create-nncp-task.md)

## Networking setup

Requirements
- dedicated physical interfaces (ens11f0, ens11f1) to leaf switches
- active/backup bond
- two [vrfs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.14/html/networking/kubernetes-nmstate#virt-example-host-vrf_k8s-nmstate-updating-node-network-config) (blue and red)
- vlan encapsulation per vrf
- route to leaf loopback interface via bonded vlan per vrf

## CRD

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: interface-bonding
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
    - link-aggregation:
        mode: active-backup
        port:
        - ens11f0
        - ens11f1
      name: bond666
      state: up
      type: bond
```

> [!NOTE]
> Similar NodeNetworkConfigurationPolicy for bm1-2 and bm1-3 nodes

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: vrf-blue-policy
spec:
  desiredState:
    interfaces:
    - name: bond666.667
      state: up
      type: vlan
      ipv4:
        address:
        - ip: 67.67.67.10
          prefix-length: 24
        dhcp: false
        enabled: true
      vlan:
        base-iface: bond666
        id: 667
    - name: blue
      type: vrf
      state: up
      vrf:
        port:
        - bond666.667
        route-table-id: 667
    routes:
      config:
      - destination: 67.67.0.6/32
        next-hop-address: 67.67.67.67
        next-hop-interface: bond666.667
        table-id: 667
      - destination: 67.67.0.7/32
        next-hop-address: 67.67.67.67
        next-hop-interface: bond666.667
        table-id: 667
  nodeSelector:
    kubernetes.io/hostname: bm1-1
```

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: vrf-red-policy
spec:
  desiredState:
    interfaces:
    - name: bond666.668
      state: up
      type: vlan
      ipv4:
        address:
        - ip: 68.68.68.10
          prefix-length: 24
        dhcp: false
        enabled: true
      vlan:
        base-iface: bond666
        id: 668
    - name: blue
      type: vrf
      state: up
      vrf:
        port:
        - bond666.668
        route-table-id: 668
    routes:
      config:
      - destination: 68.68.0.6/32
        next-hop-address: 68.68.68.68
        next-hop-interface: bond666.668
        table-id: 668
      - destination: 68.68.0.7/32
        next-hop-address: 68.68.68.68
        next-hop-interface: bond666.668
        table-id: 668
  nodeSelector:
    kubernetes.io/hostname: bm1-1
```

[[Back]](./README.md) [[Task]](./create-nncp-task.md)