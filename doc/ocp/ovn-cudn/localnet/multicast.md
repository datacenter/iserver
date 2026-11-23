# CUDN w/Localnet Topology - Multicast w/OSPF

[[Back]](./overview.md)

## Setup

- two namespaces: island-y1 and island-y2
- namespaces multicast enabled
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
router ospf 666
!
interface GigabitEthernet2
 ip address dhcp
 ip ospf 666 area 0
 negotiation auto
```

### c8kv2

- namespace: island-y2
- node: bm1-2
- dhcp on secondary interface

```
router ospf 666
!
interface GigabitEthernet2
 ip address dhcp
 ip ospf 666 area 0
 negotiation auto
```

## OSPF

```
c8kv1#show ip ospf nei

Neighbor ID     Pri   State           Dead Time   Address         Interface
66.66.1.15        1   FULL/DR         00:00:37    66.66.1.15      GigabitEthernet2
```

## On-the-wire

> [!NOTE]
> Dedicated ovs configured with single physical interface upstream

```
02:65:2b:c5:ba:29 > 01:00:5e:00:00:05, 
      ethertype IPv4 (0x0800), length 114: 
      66.66.1.15 > 224.0.0.5: 
      OSPFv2, Hello, length 80
```

[[Back]](./overview.md)