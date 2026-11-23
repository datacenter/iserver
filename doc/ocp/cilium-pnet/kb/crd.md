# Private Network - Custom Resources

[[Back]](../README.md) [[iserver-way]](../get_map.md) [[Next]](../ew-test/README.md)

## ClusterwidePrivateNetwork

`ClusterwidePrivateNetwork` custom resource defines private network 

```yaml
apiVersion: isovalent.com/v1alpha1
kind: ClusterwidePrivateNetwork
metadata:
  name: blue
spec:
  subnets:
  - name: subnet-0
    cidrv4: 10.10.10.0/24
```

Key fields:

| Field | Description |
|-------|-------------|
| `spec.subnets[].name` | Required. RFC 1123 label (1-63 chars, lowercase alphanumeric and dashes). |
| `spec.subnets[].cidrv4` | IPv4 CIDR. At least one of `cidrv4`/`cidrv6` is required. Immutable once set. |
| `spec.subnets[].cidrv6` | IPv6 CIDR. At least one of `cidrv4`/`cidrv6` is required. Immutable once set. |
| `spec.subnets[].routes` | Per-subnet routes (max 64). |
| `spec.subnets[].dhcp` | Per-subnet DHCP relay configuration. |
| `spec.vni` | Optional 24-bit VNI for EVPN/VXLAN (0-16777215). |
| `spec.networkBridges` | INB cluster references (bridge mode only). |

## PrivateNetworkEndpointSlice

`PrivateNetworkEndpointSlice` custom resource is used internally by private network feature for state propagation. It contains the list of workloads attached to a Private Network and hosted by a given node, and their network parameters.

```
$ oc get privatenetworkendpointslices.isovalent.com -A
NAMESPACE   NAME    AGE
a           bm3-1   21h
b           bm3-2   20h
c           bm3-1   20h
```

```yaml
apiVersion: isovalent.com/v1alpha1
kind: PrivateNetworkEndpointSlice
metadata:
  name: bm3-1
  namespace: a
  ownerReferences:
  - apiVersion: cilium.io/v2
    kind: CiliumNode
    name: bm3-1
nodeName: bm3-1
endpoints:
- activatedAt: "2026-05-15T18:35:21.870000Z"
  endpoint:
    addressing:
      ipv4: 10.128.2.134
    name: p2-eth1
  flags: {}
  interface:
    addressing:
      ipv4: 10.10.10.2
    mac: 76:10:19:cc:65:86
    network: blue
```

## PrivateNetworkExternalEndpoint

`PrivateNetworkExternalEndpoint` assigns a name and a set of labels to a workload running outside of Kubernetes and connected via the [Isovalent Network Bridge (INB)](../../cilium-inb/README.md), for network policy and observability purposes.

```yaml
apiVersion: isovalent.com/v1alpha1
kind: PrivateNetworkExternalEndpoint
metadata:
  name: example-workload
  namespace: example
spec:
  inactive: false
  interface:
    network: blue
    addressing:
      ipv4: "192.168.250.42"
      ipv6: "fc00:0:250::42"
    mac: "ff:22:f1:22:21:51"
```

Key fields:

| Field | Description |
|-------|-------------|
| `spec.inactive` | Marking a workload as inactive makes it unreachable from other Cilium-managed endpoints. Setting an external workload as inactive can be useful after having migrated that external workload over to a Cilium-managed Kubernetes cluster. Defaults to `false` if omitted. |
| `spec.interface` | Required. Describes the network interface of the external workload. |
| `spec.interface.network` | A reference to an existing ClusterwidePrivateNetwork resource by name. |
| `spec.interface.addressing` | IP addresses of external workload. |
| `spec.interface.mac` | MAC address of the external workload’s network interface. |

All properties immutable once set.

## PrivateNetworkNodeAttachment

`PrivateNetworkNodeAttachment` attaches a `ClusterwidePrivateNetwork` to one or more network interfaces on the Kubernetes nodes, to provide connectivity to external networks in **local access** mode

```yaml
apiVersion: isovalent.com/v1alpha1
kind: PrivateNetworkNodeAttachment
metadata:
  name: blue-attachment
spec:
  privateNetworkRef:
    name: blue
  nodeSelector:                  # Optional: target specific nodes
    matchLabels:
      zone: external
  attachments:
  - interface: eth1              # Physical interface on the node
    subnetRefs:
    - name: subnet-0
  - interface: eth2
    subnetRefs:
    - name: subnet-1
    vlanID: 100                  # Optional: creates a DOT1Q VLAN sub-interface (eth2.100)
```

Key fields:

| Field | Description |
|-------|-------------|
| `spec.privateNetworkRef.name` | Required. References a `ClusterwidePrivateNetwork`. |
| `spec.nodeSelector` | Optional. Label selector to apply only to matching nodes. If omitted, applies to all nodes. |
| `spec.attachments[].interface` | Required. Interface name on the node (max 15 chars). |
| `spec.attachments[].subnetRefs` | Optional. List of subnet names reachable via this interface. Empty means all subnets. |
| `spec.attachments[].vlanID` | Optional. VLAN ID (1-4094). When set, Cilium creates a DOT1Q sub-interface. |

[[Back]](../README.md) [[iserver-way]](../get_map.md) [[Next]](../ew-test/README.md)