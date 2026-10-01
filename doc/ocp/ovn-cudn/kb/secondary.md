# CUDN - Secondary

[[Back]](../README.md)

Usage
- extra interface connection of Pod or Virtual Machine
- pod must be [configured](./localnet/pod.md) to connect to secondary cudn
- virtual machine must be [configured](./l2/vm.md) to connect to secondary cudn

Provisioning
- [cudn namespace selection](./namespace.md)
- multiple secondary cudn per selected namespace
- subnet mandatory for L3 tppology with max one v4 and one v6 cidr defined
- topology
  - [L2](../l2/overview.md)
  - [L3](../l3/overview.md)
  - [localnet](../localnet/overview.md)

## L2 with ipam enabled

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

Unlike [primary cudn](./primary.md), vrf is **not created** for secondary network.

`NetworkAttachmentDefinition` object for every selected namespace with cudn name and `spec.config` reflecting cudn definition

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  annotations:
    k8s.ovn.org/network-id: "17"
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
      "name":"cluster_udn_a1",
      "netAttachDefName":"a1p/a1",
      "role":"secondary",
      "subnets":"66.66.66.0/24",
      "topology":"layer2",
      "type":"ovn-k8s-cni-overlay"
    }
  '
```

## L2 with ipam disabled

When ipam is disabled the subnet is not defined, users must configure static IP addresses for the pods. As a consequence, port security only prevents MAC spoofing. 

```yaml
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: b1 
spec:
  namespaceSelector:
    matchLabels:
      "tenant": "b"
  network:
    topology: Layer2
    layer2:
      role: Secondary
      ipam:
        mode: Disabled
```

Unlike [primary cudn](./primary.md), vrf is **not created** for secondary network.

`NetworkAttachmentDefinition` object for every selected namespace with cudn name and `spec.config` reflecting cudn definition

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  annotations:
    k8s.ovn.org/network-id: "18"
    k8s.ovn.org/network-name: cluster_udn_b1
    k8s.ovn.org/tunnel-keys: '[]'
  labels:
    k8s.ovn.org/user-defined-network: ""
  name: b1
  namespace: b1p
  ownerReferences:
  - apiVersion: k8s.ovn.org/v1
    blockOwnerDeletion: true
    controller: true
    kind: ClusterUserDefinedNetwork
    name: b1
spec:
  config: '
    {
      "cniVersion":"1.1.0",
      "name":"cluster_udn_b1",
      "netAttachDefName":"b1p/b1",
      "role":"secondary",
      "topology":"layer2",
      "type":"ovn-k8s-cni-overlay"
    }
  '
```

## L3

>[!NOTE]
>L3 topology requires subnet configured and ipam enabled

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
      role: Secondary
      subnets:
      - cidr: 66.66.66.0/24
        hostSubnet: 26
```

Unlike [primary cudn](./primary.md), vrf is **not created** for secondary network.

`NetworkAttachmentDefinition` object for every selected namespace with cudn name and `spec.config` reflecting cudn definition

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  annotations:
    k8s.ovn.org/network-id: "20"
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
      "name":"cluster_udn_a1",
      "netAttachDefName":"a1p/a1",
      "role":"secondary",
      "subnets":"66.66.66.0/24/26",
      "topology":"layer3",
      "type":"ovn-k8s-cni-overlay"
    }
  '
```

## Localnet

Prepare localnet first

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: ovs-localnet-y
spec:
  desiredState:
    interfaces:
    - name: ovs-localnet-y
      type: ovs-bridge
      state: up
      bridge:
        allow-extra-patch-ports: true
        options:
          stp: false
          mcast-snooping-enable: true
        port:
        - name: ens11f0
    ovn:
      bridge-mappings:
      - localnet: localnet-y
        bridge: ovs-localnet-y
        state: present
```

wait until nncp completes

```yaml
status:
  conditions:
  - lastHeartbeatTime: "2026-07-06T09:20:42Z"
    lastTransitionTime: "2026-07-06T09:20:42Z"
    message: 3/3 nodes successfully configured
    reason: SuccessfullyConfigured
    status: "True"
    type: Available
```

### ipam enabled

Prepare cudn with localnet topology where `physicalNetworkName` property refers to localnet bridge mappings defined above

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
    topology: Localnet
    localnet:
      physicalNetworkName: localnet-y
      role: Secondary
      subnets:
      - 66.66.66.0/24
```

vrf is **not created** for secondary network.

`NetworkAttachmentDefinition` object for every selected namespace with cudn name and `spec.config` reflecting cudn definition

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  annotations:
    k8s.ovn.org/network-id: "22"
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
      "mtu":1500,
      "name":"cluster_udn_a1",
      "netAttachDefName":"a1p/a1",
      "physicalNetworkName":"localnet-y",
      "role":"secondary",
      "subnets":"66.66.66.0/24",
      "topology":"localnet",
      "type":"ovn-k8s-cni-overlay"
    }
  '
```

### ipam disabled

Prepare cudn with localnet topology where `physicalNetworkName` property refers to localnet bridge mappings defined above

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
    topology: Localnet
    localnet:
      physicalNetworkName: localnet-y
      role: Secondary
      ipam:
        mode: Disabled
```

vrf is **not created** for secondary network.

`NetworkAttachmentDefinition` object for every selected namespace with cudn name and `spec.config` reflecting cudn definition

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  annotations:
    k8s.ovn.org/network-id: "23"
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
      "mtu":1500,
      "name":"cluster_udn_a1",
      "netAttachDefName":"a1p/a1",
      "physicalNetworkName":"localnet-y",
      "role":"secondary",
      "topology":"localnet",
      "type":"ovn-k8s-cni-overlay"
    }
  '
```

[[Back]](../README.md)