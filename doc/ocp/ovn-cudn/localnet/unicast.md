# CUDN w/Localnet Topology - Unicast 

[[Back]](./overview.md)

## Setup

- two namespaces: island-y1 and island-y2
- single cudn secondary network with localnet topology across two namespaces
- c8kv vm per namespace connected to cudn w/localnet topology
- c8kv vms on different nodes
- refer to [task](./task.md) for full details

## IP Stack

```
# iserver get k8s vmi --cluster bm1

+----+-------------+-------+-----+-----+---------------------+-------+--------------------------------------------+-----------------------+---------+
| ID | VM Instance | Node  | CPU | Mem | Disk                | PVC   | Interface                                  | Svc                   | State   |
+----+-------------+-------+-----+-----+---------------------+-------+--------------------------------------------+-----------------------+---------+
| 1  | island-y1   | bm1-1 | 1   | 4Gi | rootdisk/vda - 10Gi | c8kv1 | [default] 66.66.0.20 (pod:l2bridge)        | NodePort:TCP/22:30106 | Running |
|    | c8kv1       |       |     |     | day0                | ---   | [net1] 66.66.1.12 (multus:island-y1/ysphy) |                       |         |
+----+-------------+-------+-----+-----+---------------------+-------+--------------------------------------------+-----------------------+---------+
| 2  | island-y2   | bm1-2 | 1   | 4Gi | rootdisk/vda - 10Gi | c8kv2 | [default] 66.66.0.29 (pod:l2bridge)        | NodePort:TCP/22:31707 | Running |
|    | c8kv2       |       |     |     | day0                | ---   | [net1] 66.66.1.15 (multus:island-y2/ysphy) |                       |         |
+----+-------------+-------+-----+-----+---------------------+-------+--------------------------------------------+-----------------------+---------+
```

### c8kv1 

- namespace: island-y1
- node: bm1-1
- dhcp on secondary interface

```
interface GigabitEthernet2
 ip address dhcp
 negotiation auto
```

```
c8kv1#show int gi2
GigabitEthernet2 is up, line protocol is up 
  Hardware is vNIC, address is 0265.2bc5.ba28 (bia 0265.2bc5.ba28)
  Internet address is 66.66.1.12/24
```

```
c8kv1#show ip route
S*    0.0.0.0/0 [254/0] via 66.66.0.1
      66.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
C        66.66.0.0/24 is directly connected, GigabitEthernet1
L        66.66.0.20/32 is directly connected, GigabitEthernet1
C        66.66.1.0/24 is directly connected, GigabitEthernet2
L        66.66.1.12/32 is directly connected, GigabitEthernet2
      169.254.0.0/32 is subnetted, 1 subnets
S        169.254.1.1 [254/0] via 66.66.0.1, GigabitEthernet1
```

```
c8kv1#show arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  66.66.0.1             139   0a58.4242.0001  ARPA   GigabitEthernet1
Internet  66.66.0.20              -   0a58.4242.0014  ARPA   GigabitEthernet1
Internet  66.66.1.12              -   0265.2bc5.ba28  ARPA   GigabitEthernet2
Internet  66.66.1.15              0   0265.2bc5.ba29  ARPA   GigabitEthernet2
```

### c8kv2

- namespace: island-y2
- node: bm1-2
- dhcp on secondary interface

```
interface GigabitEthernet2
 ip address dhcp
 negotiation auto
```

```
c8kv1#show int gi2
GigabitEthernet2 is up, line protocol is up 
  Hardware is vNIC, address is 0265.2bc5.ba29 (bia 0265.2bc5.ba29)
  Internet address is 66.66.1.15/24
```

```
c8kv1#show ip route
S*    0.0.0.0/0 [254/0] via 66.66.0.1
      66.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
C        66.66.0.0/24 is directly connected, GigabitEthernet1
L        66.66.0.29/32 is directly connected, GigabitEthernet1
C        66.66.1.0/24 is directly connected, GigabitEthernet2
L        66.66.1.15/32 is directly connected, GigabitEthernet2
      169.254.0.0/32 is subnetted, 1 subnets
S        169.254.1.1 [254/0] via 66.66.0.1, GigabitEthernet1
```

```
c8kv2#show arp     
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  66.66.0.1             141   0a58.4242.0001  ARPA   GigabitEthernet1
Internet  66.66.0.29              -   0a58.4242.001d  ARPA   GigabitEthernet1
Internet  66.66.1.12              0   0265.2bc5.ba28  ARPA   GigabitEthernet2
Internet  66.66.1.15              -   0265.2bc5.ba29  ARPA   GigabitEthernet2
```

## Ping

```
c8kv1#ping 66.66.1.15
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 66.66.1.15, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/2/7 ms
```

## On-the-wire

> [!NOTE]
> Dedicated ovs configured with single physical interface upstream

```
02:65:2b:c5:ba:28 > 02:65:2b:c5:ba:29, 
    ethertype IPv4 (0x0800), length 114: 
    66.66.1.12 > 66.66.1.15: 
    ICMP echo request, id 1, seq 0, length 80
```

Upstream Nexus switch

```
nexus# show mac address-table 
*    1     0265.2bc5.ba28   dynamic  NA         F      F    Eth1/1
*    1     0265.2bc5.ba29   dynamic  NA         F      F    Eth1/2
```

[[Back]](./overview.md)