# CUDN - Primary

[[Back]](../README.md)

Usage 
- for primary interface of [Pod](../l2/pod_primary.md) or Virtual Machine
- pod connects to primary cudn automatically without any extra configuration
- virtual machine must be [configured](./l2/vm.md) to connect to primary cudn

Provisioning
- [cudn selected namespace](./namespace.md) **must** be defined with `k8s.ovn.org/primary-user-defined-network` label
- **max one** primary cudn per selected namespace
- subnet **mandatory** with **max one** v4 and one v6 cidr defined
- subnet can overlap across cudn
- `ipam.mode` by default enabled and cannot be disabled
- topology: [L2](../l2/overview.md), [L3](../l3/overview.md)

Limitations
- [localnet](../localnet/overview.md) topology not supported

## L2

```yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: a1
spec:
  namespaceSelector:
    matchLabels:
      "tenant": "a"
  network:
    topology: Layer2
    layer2:
      role: Primary
      subnets:
      - 66.66.66.0/24
```

Primary CUDN with [L2 topology](../l2/overview.md) triggers vrf creation on every cluster node

```
$ ip vrf show
Name              Table
-----------------------
a1                1084
```

One logical switch shared by all nodes e.g., ovn-k8s-mp10

>[!NOTE]
>vrf table is the same on every cluster node

```
$ ip r show vrf a1
default via 10.10.10.254 dev br-ex mtu 1400 
unreachable default metric 4278198272 
66.66.66.0/24 dev ovn-k8s-mp10 proto kernel scope link src 66.66.66.2 
169.254.0.3 via 66.66.66.1 dev ovn-k8s-mp10 
169.254.0.30 dev ovn-k8s-mp10 mtu 1400 
172.30.0.0/16 via 169.254.0.4 dev br-ex mtu 1400
```

`NetworkAttachmentDefinition` object for every selected namespace with cudn name and `spec.config` reflecting cudn definition

>[!NOTE]
>`metadata.annotations.k8s.ovn.org/network-id` value defines ovn-k8s-mp{$INDEX}

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  annotations:
    k8s.ovn.org/network-id: "10"
    k8s.ovn.org/network-name: cluster_udn_a1
    k8s.ovn.org/tunnel-keys: '[16711697,16715785]'
  labels:
    k8s.ovn.org/user-defined-network: ""
  name: a1
  namespace: a1p
  ownerReferences:
  - apiVersion: k8s.ovn.org/v1
    blockOwnerDeletion: true
    controller: true
    kind: ClusterUserDefinedNetwork
    name: a1
spec:
  config: '
    {
      "cniVersion":"1.1.0",
      "joinSubnet":"100.65.0.0/16,fd99::/64",
      "name":"cluster_udn_a1",
      "netAttachDefName":"a1p/a1",
      "role":"primary",
      "subnets":"66.66.66.0/24",
      "topology":"layer2",
      "transitSubnet":"100.88.0.0/16",
      "type":"ovn-k8s-cni-overlay"
    }
  '
```

## L3

```yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: a1
spec:
  namespaceSelector:
    matchLabels:
      "tenant": "a"
  network:
    topology: Layer3
    layer3:
      role: Primary
      subnets:
      - cidr: 66.66.66.0/24
        hostSubnet: 26
```

Primary CUDN with [L3 topology](../l3/overview.md) triggers vrf creation on every cluster node

```
$ ip vrf show
Name              Table
-----------------------
a1                1084
```

Layer 2 segment per node implemented on ovn switch e.g., ovn-k8s-mp12; each with a different subnet. Layer 3 routing is used to interconnect node subnets

```
[node1]$ ip r show vrf a1
default via 10.10.10.254 dev br-ex mtu 1400 
unreachable default metric 4278198272 
66.66.66.0/26 dev ovn-k8s-mp12 proto kernel scope link src 66.66.66.2 
66.66.66.0/24 via 66.66.66.1 dev ovn-k8s-mp12 
169.254.0.3 via 66.66.66.1 dev ovn-k8s-mp12 
169.254.0.34 dev ovn-k8s-mp12 mtu 1400 
172.30.0.0/16 via 169.254.0.4 dev br-ex mtu 1400 
```

```
[node2]$ ip r show vrf a1
default via 10.10.10.254 dev br-ex mtu 1400 
unreachable default metric 4278198272 
66.66.66.0/24 via 66.66.66.65 dev ovn-k8s-mp12 
66.66.66.64/26 dev ovn-k8s-mp12 proto kernel scope link src 66.66.66.66 
169.254.0.3 via 66.66.66.65 dev ovn-k8s-mp12 
169.254.0.34 dev ovn-k8s-mp12 mtu 1400 
172.30.0.0/16 via 169.254.0.4 dev br-ex mtu 1400
```

`NetworkAttachmentDefinition` object for every selected namespace with cudn name and `spec.config` reflecting cudn definition

>[!NOTE]
>`metadata.annotations.k8s.ovn.org/network-id` value defines ovn-k8s-mp{$INDEX}

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  annotations:
    k8s.ovn.org/network-id: "12"
    k8s.ovn.org/network-name: cluster_udn_a1
    k8s.ovn.org/tunnel-keys: '[]'
  labels:
    k8s.ovn.org/user-defined-network: ""
  name: a1
  namespace: a1p
  ownerReferences:
  - apiVersion: k8s.ovn.org/v1
    blockOwnerDeletion: true
    controller: true
    kind: ClusterUserDefinedNetwork
    name: a1
spec:
  config: '
    {
      "cniVersion":"1.1.0",
      "joinSubnet":"100.65.0.0/16,fd99::/64",
      "name":"cluster_udn_a1",
      "netAttachDefName":"a1p/a1",
      "role":"primary",
      "subnets":"66.66.66.0/24/26",
      "topology":"layer3",
      "type":"ovn-k8s-cni-overlay"
    }
  '
```

[[Back]](../README.md)