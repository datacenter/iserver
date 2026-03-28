# UDN w/L2 Topology - Multicast w/OSPF

[[Back]](./overview.md)

## Setup

- namespaces: island-p
- single udn primary network w/l2 topology
- single udn secondary network w/l2 topology
- 2x c8kv vms to both udns, no connection to pod cidr, deployed on different nodes
- refer to [task](./task.md) for details

### c8kv1 

```
interface GigabitEthernet1
 ip address dhcp
 ip ospf 666 area 0
 negotiation auto
!
interface GigabitEthernet2
 ip address dhcp
 ip ospf 999 area 0
 negotiation auto
!
router ospf 666
!
router ospf 999
!
```

```
c8kv1#show interface
GigabitEthernet1 is up, line protocol is up 
  Hardware is vNIC, address is 0a58.4242.0010 (bia 0a58.4242.0010)
  Internet address is 66.66.0.16/24
GigabitEthernet2 is up, line protocol is up
  Hardware is vNIC, address is 0265.2bc5.ba2e (bia 0265.2bc5.ba2e)
  Internet address is 66.66.1.9/24
```

```
c8kv1#show ip route  
S*    0.0.0.0/0 [254/0] via 66.66.0.1
      66.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
C        66.66.0.0/24 is directly connected, GigabitEthernet1
L        66.66.0.16/32 is directly connected, GigabitEthernet1
C        66.66.1.0/24 is directly connected, GigabitEthernet2
L        66.66.1.9/32 is directly connected, GigabitEthernet2
      169.254.0.0/32 is subnetted, 1 subnets
S        169.254.1.1 [254/0] via 66.66.0.1, GigabitEthernet1
```

```
c8kv1#show arp       
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  66.66.0.1              99   0a58.4242.0001  ARPA   GigabitEthernet1
Internet  66.66.0.16              -   0a58.4242.0010  ARPA   GigabitEthernet1
Internet  66.66.0.26              2   0a58.4242.001a  ARPA   GigabitEthernet1
Internet  66.66.1.9               -   0265.2bc5.ba2e  ARPA   GigabitEthernet2
Internet  66.66.1.12              2   0265.2bc5.ba2f  ARPA   GigabitEthernet2
```

```
c8kv1#show ip ospf nei

Neighbor ID     Pri   State           Dead Time   Address         Interface
66.66.0.26        1   FULL/DR         00:00:38    66.66.1.12      GigabitEthernet2
66.66.1.12        1   FULL/DR         00:00:31    66.66.0.26      GigabitEthernet1
```

## On-the-wire

```
10.10.10.210.32623 > 10.10.10.211.6081: 
  Geneve, Flags [C], vni 0xff0061, proto TEB (0x6558), options [8 bytes]: 
  02:65:2b:c5:ba:2e > 01:00:5e:00:00:05, 
  ethertype IPv4 (0x0800), length 114: 
  66.66.1.9 > 224.0.0.5: 
  OSPFv2, Hello, length 80

10.10.10.211.18204 > 10.10.10.210.6081: 
  Geneve, Flags [C], vni 0xff0061, proto TEB (0x6558), options [8 bytes]: 
  02:65:2b:c5:ba:2f > 01:00:5e:00:00:05, 
  ethertype IPv4 (0x0800), length 114: 
  66.66.1.12 > 224.0.0.5: 
  OSPFv2, Hello, length 80
```

[[Back]](./overview.md)