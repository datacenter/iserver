# Intra-udn traffic - implicit permit

[[Back]](../README.md)

![Overview](../../images/ovn-udn/intra_udn.png)

## IP stack

> [!NOTE]
> Service cidr 172.30.0.0/16 via ovn-udn1 i.e. primary udn attached interface

```
$ oc exec -it -n island-a p1-1 -- ip r
default via 66.66.0.1 dev ovn-udn1 
10.128.0.0/23 dev eth0 proto kernel scope link src 10.128.0.126
10.128.0.0/14 via 10.128.0.1 dev eth0
66.66.0.0/24 dev ovn-udn1 proto kernel scope link src 66.66.0.4
100.64.0.0/16 via 10.128.0.1 dev eth0
100.65.0.0/16 via 66.66.0.1 dev ovn-udn1
172.30.0.0/16 via 66.66.0.1 dev ovn-udn1
```

## curl tcp syn on-the-wire

```
10.10.10.210.45688 > 10.10.10.212.6081: 
    Geneve, Flags [C], vni 0xff0014, proto TEB (0x6558), options [8 bytes]: 
    0a:58:42:42:00:01 > 0a:58:42:42:00:2b, 
    ethertype IPv4 (0x0800), length 74: 
    66.66.0.4.51376 > 66.66.0.43.8080: 
    Flags [S], seq 565885329, win 65280, options [mss 1360,sackOK,TS val 2707956054 ecr 0,nop,wscale 7], length 0
```

[[Back]](../README.md)