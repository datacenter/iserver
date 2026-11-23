# OVNKubernetes BGP - Cluster User Defined Network (L3)

[[Back]](./README.md) [[CUDN]](./nns-cudn.md)

## Networking setup

Requirements
- dedicated physical interfaces (ens11f0, ens11f1) to leaf switches
- active/backup bond
- no vlan encapsulation
- route to leaf loopback interface via bond

## IP Stack

```
$ ip a 
6: ens11f0: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc mq master bond666 state UP group default qlen 1000
    link/ether aa:aa:aa:aa:aa:aa brd ff:ff:ff:ff:ff:ff
    altname enp75s0f0
8: ens11f1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc mq master bond666 state UP group default qlen 1000
    link/ether aa:aa:aa:aa:aa:aa brd ff:ff:ff:ff:ff:ff
    altname enp75s0f1
20020: bond666: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether aa:aa:aa:aa:aa:aa brd ff:ff:ff:ff:ff:ff
    inet 66.66.66.10/24 brd 66.66.66.255 scope global noprefixroute bond666
       valid_lft forever preferred_lft forever
```

```
$ ip r
6.6.6.6 via 66.66.66.66 dev bond666 proto static
6.6.6.7 via 66.66.66.66 dev bond666 proto static
```

```
$ ip vrf show
Name              Table
-----------------------
No VRF has been configured
```

[[Back]](./README.md) [[CUDN]](./nns-cudn.md)