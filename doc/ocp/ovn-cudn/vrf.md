# Cluster User Defined Network (CUDN) - VRF

[[Back]](./README.md)

![Overview](../images/ovn-bgp/cudn_only.png)

> [!NOTE]
> The outputs from one of the cluster nodes

```
$ ip vrf show
Name              Table
-----------------------
tenant-blue      20833
tenant-red       20835
```

## tenant-blue

```
$ ip r show vrf tenant-blue
default via 10.10.10.222 dev br-ex mtu 1400 
unreachable default metric 4278198272
69.69.100.0/24 via 69.69.100.17 dev ovn-k8s-mp3 
69.69.100.16/28 dev ovn-k8s-mp3 proto kernel scope link src 69.69.100.18
169.254.0.3 via 69.69.100.17 dev ovn-k8s-mp3
169.254.0.16 dev ovn-k8s-mp3 mtu 1400
172.30.0.0/16 via 169.254.0.4 dev br-ex mtu 1400
```

## tenant-red

```
$ ip r show vrf tenant-red
default via 10.10.10.222 dev br-ex mtu 1400 
unreachable default metric 4278198272
69.69.200.0/28 dev ovn-k8s-mp4 proto kernel scope link src 69.69.200.2
69.69.200.0/24 via 69.69.200.1 dev ovn-k8s-mp4
169.254.0.3 via 69.69.200.1 dev ovn-k8s-mp4 
169.254.0.18 dev ovn-k8s-mp4 mtu 1400
172.30.0.0/16 via 169.254.0.4 dev br-ex mtu 1400
```

[[Back]](./README.md)