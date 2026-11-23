# Server p2p connection with leaf

[[Back]](./README.md) [[Next]](./server-bgp.md) [[addressing scheme]](./address.md)

Node | Interface | IP address 
--- | --- | --- 
bm1-1 | eno5 | 100.64.66.111/31 
bm1-2 | eno5 | 100.64.66.121/31
bm1-3 | eno5 | 100.64.66.131/31

>[!NOTE]
>Example below for single server in Kubernetes cluster

- server `bm1-1` with eno5 interface connected to upstream leaf device
- ipv4 address 100.64.66.111/31

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: bm1-1-eno5
spec:
  desiredState:
    interfaces:
    - ipv4:
        address:
        - ip: 100.64.66.111
          prefix-length: 31
        dhcp: false
        enabled: true
      name: eno5
      state: up
      type: ethernet
  nodeSelector:
    kubernetes.io/hostname: bm1-1
```

Once `NodeNetworkConfigurationPolicy` is successfully applied

```
$ ip a show eno5
2: eno5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc mq state UP group default qlen 1000
    link/ether aa:aa:aa:aa:aa:aa brd ff:ff:ff:ff:ff:ff
    inet 100.64.66.121/31 scope global noprefixroute eno5
       valid_lft forever preferred_lft forever
```

Corresponding configuration on leaf device

```
leaf-1# show run interface ethernet 1/12

interface Ethernet1/12
  description bm1-1
  ip address 100.64.66.110/31
  no shutdown
```

Test

```
$ ping 100.64.66.110 -c 1
PING 100.64.66.110 (100.64.66.110) 56(84) bytes of data.
64 bytes from 100.64.66.110: icmp_seq=1 ttl=255 time=0.796 ms
```

[[Back]](./README.md) [[Next]](./server-bgp.md) [[addressing scheme]](./address.md)