# UDN and Multicast

[[Back]](../README.md)

## Namespace

> [!NOTE]
> Multicast must be enabled in namespace with `k8s.ovn.org/multicast-enabled: "true"` annotation

```
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    k8s.ovn.org/multicast-enabled: "true"
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
  name: island
```

## User defined network with L2 topology

```
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: p1-l2
  namespace: island-a
spec:
  layer2:
    role: Primary
    subnets:
    - 66.66.1.0/24
  topology: Layer2
```

## OSPF use case

> [!NOTE]
> Cat8000v virtual machines connected to primary udn only

![OSPF](../../images/ovn-udn/l2_ospf.png)

```
c8kv2#show int gigabitEthernet 1
GigabitEthernet1 is up, line protocol is up 
  Hardware is vNIC, address is 0a58.4242.0017 (bia 0a58.4242.0017)
  Internet address is 66.66.0.23/24
```

```
c8kv2#show ip ospf interface gigabitEthernet 1
GigabitEthernet1 is up, line protocol is up 
  Internet Address 66.66.0.23/24, Interface ID 5, Area 0
  Attached via Interface Enable
  Process ID 666, Router ID 66.66.0.23, Network Type BROADCAST, Cost: 1
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           1         no          no            Base
  Enabled by interface config, including secondary ip addresses
  Transmit Delay is 1 sec, State BDR, Priority 1
  Designated Router (ID) 66.66.1.9, Interface address 66.66.0.30
  Backup Designated router (ID) 66.66.0.23, Interface address 66.66.0.23
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:04
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Index 1/1/1, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 1, maximum is 1
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 1, Adjacent neighbor count is 1
    Adjacent with neighbor 66.66.1.9  (Designated Router)
  Suppress hello for 0 neighbor(s)
```

## Overlay

```
10.10.10.211.31469 > 10.10.10.212.6081: 
    Geneve, Flags [C], vni 0xff0014, proto TEB (0x6558), options [8 bytes]: 
    0a:58:42:42:00:17 > 01:00:5e:00:00:05, 
    ethertype IPv4 (0x0800), length 114: 
    66.66.0.23 > 224.0.0.5: 
    OSPFv2, Hello, length 80
```

[[Back]](../README.md)