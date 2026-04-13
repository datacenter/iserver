# OVNKubernetes BGP - Cluster User Defined Network (L3)

[[Back]](./README.md) [[CRD]](./cudn-crd.md) [[Task]](./cudn-crd-task.md)

![Overview](../../../images/ovn-bgp/cudn.png)

## CUDN

Requirements
- primary cudn
- L3 topology
- assigned with two namespaces each
- bgp:enabled labeled
- tenant-blue: 69.69.100.0/24 with hostSubnet:28
- tenant-red: 69.69.200.0/24 with hostSubnet:28

## IP Stack

> [!NOTE]
> The outputs from one of the cluster nodes

### VRF

```
$ ip vrf show
Name              Table
-----------------------
tenant-blue      21038
tenant-red       21040
```

### tenant-blue

```
$ ip r show vrf tenant-blue
default via 10.10.10.222 dev br-ex mtu 1400
unreachable default metric 4278198272
69.69.100.0/28 dev ovn-k8s-mp1 proto kernel scope link src 69.69.100.2
69.69.100.0/24 via 69.69.100.1 dev ovn-k8s-mp1
169.254.0.3 via 69.69.100.1 dev ovn-k8s-mp1
169.254.0.12 dev ovn-k8s-mp1 mtu 1400
172.30.0.0/16 via 169.254.0.4 dev br-ex mtu 1400
```

### tenant-red

```
$ ip r show vrf tenant-red
default via 10.10.10.222 dev br-ex mtu 1400 
unreachable default metric 4278198272
69.69.200.0/28 dev ovn-k8s-mp2 proto kernel scope link src 69.69.200.2
69.69.200.0/24 via 69.69.200.1 dev ovn-k8s-mp2
169.254.0.3 via 69.69.200.1 dev ovn-k8s-mp2
169.254.0.14 dev ovn-k8s-mp2 mtu 1400
172.30.0.0/16 via 169.254.0.4 dev br-ex mtu 1400
```

[[Back]](./README.md) [[CRD]](./cudn-crd.md) [[Task]](./cudn-crd-task.md)