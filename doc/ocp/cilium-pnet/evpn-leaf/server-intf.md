# Server interfaces

[[Back]](./README.md) [[Next]](./server-bgp.md)

## loopback

Every node configured with loopback ip, used as bgp router-id and vtep source

Node | Interface | IP address 
--- | --- | --- 
bm1-1 | lo | 100.64.10.1
bm1-2 | lo | 100.64.10.2
bm1-3 | lo | 100.64.10.3

>[!NOTE]
>Showing bm1-1 lo for brevity. Check [full configuration](./kube-baseline.md)

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: bm1-1-lo
spec:
  desiredState:
    interfaces:
    - ipv4:
        address:
        - ip: 100.64.10.1
          prefix-length: 32
        dhcp: false
        enabled: true
      name: lo
      state: up
      type: loopback
  nodeSelector:
    kubernetes.io/hostname: bm1-1
```

## p2p connection with leaf (RFC5549)

Node | Interface | IP address 
--- | --- | --- 
bm1-1 | eno5 | **unnumbered** 
bm1-1 | eno6 | **unnumbered** 
bm1-2 | eno5 | **unnumbered** 
bm1-2 | eno6 | **unnumbered** 
bm1-3 | eno5 | **unnumbered** 
bm1-3 | eno6 | **unnumbered** 

>[!NOTE]
>In case you want to make sure that there is no IPv4 address configured on physical interface
>The interfaces use IPv6 link-local addresses

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: eno5-unnumbered
spec:
  desiredState:
    interfaces:
    - ipv4:
        enabled: false
      name: eno5
      state: up
      type: ethernet
---
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: eno5-unnumbered
spec:
  desiredState:
    interfaces:
    - ipv4:
        enabled: false
      name: eno6
      state: up
      type: ethernet
```

Once `NodeNetworkConfigurationPolicy` is successfully applied

```
$ ip a show eno5
2: eno5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc mq state UP group default qlen 1000
    link/ether aa:aa:aa:aa:aa:aa brd ff:ff:ff:ff:ff:ff
    inet6 fe80::5ccd:e7f3:cbfa:cc50/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

```
ip a show eno6
3: eno6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc mq state UP group default qlen 1000
    link/ether bb:bb:bb:bb:bb:bb brd ff:ff:ff:ff:ff:ff
    inet6 fe80::200d:c753:4467:28a7/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

Corresponding configuration on leaf device

```
leaf-1# show run interface ethernet 1/11
interface Ethernet1/11
  description bm1-1 eno5
  ttag
  ttag-strip
  mtu 9216
  fec fc-fec
  medium p2p
  ip forward
  ipv6 address use-link-local-only
  ipv6 link-local use-bia
  no shutdown
```

[[Back]](./README.md) [[Next]](./server-bgp.md)