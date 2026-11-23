# UDN w/L2 Topology - Unicast

[[Back]](./overview.md)

## Setup

- namespaces: island-p
- single udn primary network w/l2 topology
- single udn secondary network w/l2 topology
- 2x netshoot pods connecting to both udn, deployed on different nodes
- refer to [task](./task.md) for details

## p1-1

```
$ oc exec -it -n island-p p1-1 -- ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
2: eth0@if19774: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:0a:80:01:4a brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.128.1.74/23 brd 10.128.1.255 scope global eth0
3: ovn-udn1@if19775: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:00:04 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.0.4/24 brd 66.66.0.255 scope global ovn-udn1
4: net1@if19776: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:01:03 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.1.3/24 brd 66.66.1.255 scope global net1
```

```
$ oc exec -it -n island-p p1-1 -- ip r
default via 66.66.0.1 dev ovn-udn1 
10.128.0.0/23 dev eth0 proto kernel scope link src 10.128.1.74
10.128.0.0/14 via 10.128.0.1 dev eth0
66.66.0.0/24 dev ovn-udn1 proto kernel scope link src 66.66.0.4 
66.66.1.0/24 dev net1 proto kernel scope link src 66.66.1.3
100.64.0.0/16 via 10.128.0.1 dev eth0
100.65.0.0/16 via 66.66.0.1 dev ovn-udn1
172.30.0.0/16 via 66.66.0.1 dev ovn-udn1
```

## p1-2

```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
2: eth0@if458: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:0a:81:00:e8 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.129.0.232/23 brd 10.129.1.255 scope global eth0
3: ovn-udn1@if459: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:00:08 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.0.8/24 brd 66.66.0.255 scope global ovn-udn1
4: net1@if460: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:01:06 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.1.6/24 brd 66.66.1.255 scope global net1
```

```
$ oc exec -it -n island-p p1-2 -- ip r
default via 66.66.0.1 dev ovn-udn1 
10.128.0.0/14 via 10.129.0.1 dev eth0
10.129.0.0/23 dev eth0 proto kernel scope link src 10.129.0.232
66.66.0.0/24 dev ovn-udn1 proto kernel scope link src 66.66.0.8
66.66.1.0/24 dev net1 proto kernel scope link src 66.66.1.6
100.64.0.0/16 via 10.129.0.1 dev eth0
100.65.0.0/16 via 66.66.0.1 dev ovn-udn1
172.30.0.0/16 via 66.66.0.1 dev ovn-udn1
```

## Connectivity

```
$ oc exec -it -n island-p p1-1 -- ping 66.66.0.8 -c 1
PING 66.66.0.8 (66.66.0.8) 56(84) bytes of data.
64 bytes from 66.66.0.8: icmp_seq=1 ttl=64 time=7.38 ms

$ oc exec -it -n island-p p1-1 -- ping 66.66.1.6 -c 1
PING 66.66.1.6 (66.66.1.6) 56(84) bytes of data.
64 bytes from 66.66.1.6: icmp_seq=1 ttl=64 time=3.91 ms
```

```
$ oc exec -it -n island-p p1-1 -- arp -n
? (66.66.0.8) at 0a:58:42:42:00:08 [ether]  on ovn-udn1
? (66.66.1.6) at 0a:58:42:42:01:06 [ether]  on net1
```

## On-the-wire

```
10.10.10.210.39952 > 10.10.10.211.6081: 
    Geneve, Flags [C], vni 0xff0060, proto TEB (0x6558), options [8 bytes]: 
    0a:58:42:42:00:04 > 0a:58:42:42:00:08, 
    ethertype IPv4 (0x0800), length 98: 
    66.66.0.4 > 66.66.0.8: 
    ICMP echo request, id 38, seq 1, length 64
```

```
10.10.10.210.62352 > 10.10.10.211.6081: 
    Geneve, Flags [C], vni 0xff0061, proto TEB (0x6558), options [8 bytes]: 
    0a:58:42:42:01:03 > 0a:58:42:42:01:06, 
    ethertype IPv4 (0x0800), length 98: 
    66.66.1.3 > 66.66.1.6: 
    ICMP echo request, id 39, seq 1, length 64
```

[[Back]](./overview.md)