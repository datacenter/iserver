# UDN w/L3 Topology - Unicast

[[Back]](./overview.md)

## Setup

- namespaces: island-q
- single udn primary network w/l3 topology
- single udn secondary network w/l3 topology
- 2x netshoot pods connecting to both udn, deployed on different nodes
- refer to [task](./task.md) for details

## p1-1

```
$ oc exec -it -n island-q p1-1 -- ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
2: eth0@if19788: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:0a:80:01:50 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.128.1.80/23 brd 10.128.1.255 scope global eth0
3: ovn-udn1@if19789: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:00:15 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.0.21/28 brd 66.66.0.31 scope global ovn-udn1
4: net1@if19790: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:01:04 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.1.4/28 brd 66.66.1.15 scope global net1
```

```
$ oc exec -it -n island-q p1-1 -- ip r
default via 66.66.0.17 dev ovn-udn1 
10.128.0.0/23 dev eth0 proto kernel scope link src 10.128.1.80
10.128.0.0/14 via 10.128.0.1 dev eth0
66.66.0.0/24 via 66.66.0.17 dev ovn-udn1
66.66.0.16/28 dev ovn-udn1 proto kernel scope link src 66.66.0.21
66.66.1.0/28 dev net1 proto kernel scope link src 66.66.1.4
66.66.1.0/24 via 66.66.1.1 dev net1
100.64.0.0/16 via 10.128.0.1 dev eth0
100.65.0.0/16 via 66.66.0.17 dev ovn-udn1
172.30.0.0/16 via 66.66.0.17 dev ovn-udn1
```

## p1-2

```
$ oc exec -it -n island-q p1-2 -- ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
2: eth0@if470: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:0a:81:00:ec brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.129.0.236/23 brd 10.129.1.255 scope global eth0
3: ovn-udn1@if471: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:00:24 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.0.36/28 brd 66.66.0.47 scope global ovn-udn1
4: net1@if472: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:01:15 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.1.21/28 brd 66.66.1.31 scope global net1
```

```
$ oc exec -it -n island-q p1-2 -- ip r
default via 66.66.0.33 dev ovn-udn1 
10.128.0.0/14 via 10.129.0.1 dev eth0
10.129.0.0/23 dev eth0 proto kernel scope link src 10.129.0.236
66.66.0.0/24 via 66.66.0.33 dev ovn-udn1
66.66.0.32/28 dev ovn-udn1 proto kernel scope link src 66.66.0.36
66.66.1.0/24 via 66.66.1.17 dev net1
66.66.1.16/28 dev net1 proto kernel scope link src 66.66.1.21
100.64.0.0/16 via 10.129.0.1 dev eth0
100.65.0.0/16 via 66.66.0.33 dev ovn-udn1
172.30.0.0/16 via 66.66.0.33 dev ovn-udn1
```

## Connectivity

```
$ oc exec -it -n island-q p1-1 -- ping -c 1 66.66.0.36
PING 66.66.0.36 (66.66.0.36) 56(84) bytes of data.
64 bytes from 66.66.0.36: icmp_seq=1 ttl=62 time=5.38 ms

$ oc exec -it -n island-q p1-1 -- ping -c 1 66.66.1.21
PING 66.66.1.21 (66.66.1.21) 56(84) bytes of data.
64 bytes from 66.66.1.21: icmp_seq=1 ttl=62 time=7.42 ms
```

```
$ oc exec -it -n island-q p1-1 -- arp -n
? (66.66.1.1) at 0a:58:42:42:01:01 [ether]  on net1
? (66.66.0.17) at 0a:58:42:42:00:11 [ether]  on ovn-udn1
```

## On-the-wire

```
10.10.10.210.59173 > 10.10.10.211.6081: 
    Geneve, Flags [C], vni 0xff0062, proto TEB (0x6558), options [8 bytes]: 
    0a:58:64:58:00:02 > 0a:58:64:58:00:03, 
    ethertype IPv4 (0x0800), length 98: 
    66.66.0.21 > 66.66.0.36: 
    ICMP echo request, id 42, seq 1, length 64

10.10.10.210.21855 > 10.10.10.211.6081: 
    Geneve, Flags [C], vni 0xff0063, proto TEB (0x6558), options [8 bytes]: 
    0a:58:64:58:00:02 > 0a:58:64:58:00:03, 
    ethertype IPv4 (0x0800), length 98: 
    66.66.1.4 > 66.66.1.21: 
    ICMP echo request, id 43, seq 1, length 64
```

[[Back]](./overview.md)