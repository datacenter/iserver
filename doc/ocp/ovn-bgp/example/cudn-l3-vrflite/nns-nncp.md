# OVNKubernetes BGP - Cluster User Defined Network (L3) w/VRF-Lite

[[Back]](./README.md) [[CUDN]](./nns-cudn.md)

## Networking setup

Requirements
- dedicated physical interfaces (ens11f0, ens11f1) to leaf switches
- active/backup bond
- two vrfs (blue and red)
- vlan encapsulation per vrf
- route to leaf loopback interface via bond vlan per vrf

Note: IP stack state created by [nncp](./create-nncp.md)

## IP Stack

### VRF

```
$ ip vrf show
Name              Table
-----------------------
blue               667
red                668
```

### blue

```
$ ip r show vrf blue
67.67.0.6 via 67.67.67.67 dev bond666.667 proto static 
67.67.0.7 via 67.67.67.67 dev bond666.667 proto static
67.67.67.0/24 dev bond666.667 proto kernel scope link src 67.67.67.10 metric 401
```

```
$ ip a l vrf blue
20083: bond666.667@bond666: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master blue state UP group default qlen 1000
    link/ether aa:aa:aa:aa:aa:aa brd ff:ff:ff:ff:ff:ff
    inet 67.67.67.10/24 brd 67.67.67.255 scope global noprefixroute bond666.667
       valid_lft forever preferred_lft forever
```

### red

```
$ ip r show vrf red
68.68.0.6 via 68.68.68.68 dev bond666.668 proto static 
68.68.0.7 via 68.68.68.68 dev bond666.668 proto static
68.68.68.0/24 dev bond666.668 proto kernel scope link src 68.68.68.10 metric 402
```

```
$ ip a l vrf red
20085: bond666.668@bond666: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master red state UP group default qlen 1000
    link/ether aa:aa:aa:aa:aa:aa brd ff:ff:ff:ff:ff:ff
    inet 68.68.68.10/24 brd 68.68.68.255 scope global noprefixroute bond666.668
       valid_lft forever preferred_lft forever
```

[[Back]](./README.md) [[CUDN]](./nns-cudn.md)