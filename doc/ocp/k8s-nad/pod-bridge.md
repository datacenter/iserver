# Network Attachment Definition - Bridge - Functional Test

## Pods w/nad

```
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: pod1
  namespace: default
spec:
  config: |-
    {
      "name": "br1",
      "cniVersion": "0.3.1",
      "type": "bridge",
      "bridge": "mybr1",
      "isDefaultGateway": true,
      "ipMasq": false,
      "ipam": {
        "type": "host-local",
        "subnet": "10.1.1.0/28",
        "rangeStart": "10.1.1.2",
        "rangeEnd": "10.1.1.8",
        "gateway": "10.1.1.1",
        "routes": [
          { 
            "dst": "10.1.2.0/28",
            "gw": "10.1.1.1"
          }
        ]
      }
    }
---
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: pod2
  namespace: default
spec:
  config: |-
    {
      "name": "br2",
      "cniVersion": "0.3.1",
      "type": "bridge",
      "bridge": "mybr2",
      "isDefaultGateway": true,
      "ipMasq": false,
      "ipam": {
        "type": "host-local",
        "subnet": "10.1.2.0/28",
        "rangeStart": "10.1.2.2",
        "rangeEnd": "10.1.2.8",
        "gateway": "10.1.2.1",
        "routes": [
          {
            "dst": "10.1.1.0/28",
            "gw": "10.1.2.1"
          }
        ]
      }
    }
---
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: pod1
  name: pod1
spec:
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    securityContext:
      runAsUser: 0
      capabilities:
        add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW"]
    name: netshoot
  nodeName: bm1-1
---
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: pod2
  name: pod2
spec:
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    securityContext:
      runAsUser: 0
      capabilities:
        add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW"]
    name: netshoot
  nodeName: bm1-2
```

## pod1

```
$ oc exec -it pod1 -- ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: net1@if334: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 52:36:67:a7:58:de brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.1.1.2/28 brd 10.1.1.15 scope global net1
       valid_lft forever preferred_lft forever
    inet6 fe80::5036:67ff:fea7:58de/64 scope link 
       valid_lft forever preferred_lft forever
331: eth0@if332: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 9a:b1:2c:71:db:54 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.128.2.172/32 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::98b1:2cff:fe71:db54/64 scope link
       valid_lft forever preferred_lft forever
```

```
$ oc exec -it pod1 -- ip r
default via 10.1.1.1 dev net1 
default via 10.128.3.215 dev eth0 mtu 1450
10.1.1.0/28 dev net1 proto kernel scope link src 10.1.1.2
10.1.2.0/28 via 10.1.1.1 dev net1
10.128.3.215 dev eth0 scope link
```

Default gateway

```
$ oc exec -it pod1 -- ping 10.1.1.1 -c 3
PING 10.1.1.1 (10.1.1.1) 56(84) bytes of data.
64 bytes from 10.1.1.1: icmp_seq=1 ttl=64 time=0.051 ms
64 bytes from 10.1.1.1: icmp_seq=2 ttl=64 time=0.043 ms
64 bytes from 10.1.1.1: icmp_seq=3 ttl=64 time=0.037 ms

--- 10.1.1.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2046ms
rtt min/avg/max/mdev = 0.037/0.043/0.051/0.005 ms
```

```
$ oc exec -it pod1 -- arp -n
? (10.1.1.1) at e2:a2:d1:fe:9d:fc [ether]  on net1
```

## host w/pod1

Virtual Ethernet (veth) between root network namespace and pod1 network namespace.

```
$ ip a
333: mybr1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether e2:a2:d1:fe:9d:fc brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.1/28 brd 10.1.1.15 scope global mybr1
       valid_lft forever preferred_lft forever
    inet6 fe80::e0a2:d1ff:fefe:9dfc/64 scope link
       valid_lft forever preferred_lft forever
334: veth0b0b9c2c@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master mybr1 state UP group default   
    link/ether d2:5c:e8:19:de:82 brd ff:ff:ff:ff:ff:ff link-netns a2a49b02-b1ac-46d9-9cce-3dcd550ef847
    inet6 fe80::d05c:e8ff:fe19:de82/64 scope link
       valid_lft forever preferred_lft forever
```

ifIndex (334) also seen inside the pod as net1@if334

```
$ bridge link
334: veth0b0b9c2c@eno5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 master mybr1 state forwarding priority 32 cost 2
```

```
$ bridge fdb
33:33:00:00:00:01 dev mybr1 self permanent
01:00:5e:00:00:6a dev mybr1 self permanent
33:33:00:00:00:6a dev mybr1 self permanent
01:00:5e:00:00:01 dev mybr1 self permanent
33:33:ff:fe:9d:fc dev mybr1 self permanent
e2:a2:d1:fe:9d:fc dev mybr1 vlan 1 master mybr1 permanent
e2:a2:d1:fe:9d:fc dev mybr1 master mybr1 permanent
52:36:67:a7:58:de dev veth0b0b9c2c master mybr1
d2:5c:e8:19:de:82 dev veth0b0b9c2c vlan 1 master mybr1 permanent
d2:5c:e8:19:de:82 dev veth0b0b9c2c master mybr1 permanent
```

MAC addresses
- veth root network namespace d2:5c:e8:19:de:82
- veth pod1 network namespace 52:36:67:a7:58:de
- default gateway (bridge) e2:a2:d1:fe:9d:fc

## pod2

```
$ oc exec -it pod2 -- ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: net1@if3508: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 2a:8f:a8:1e:42:11 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.1.2.2/28 brd 10.1.2.15 scope global net1
       valid_lft forever preferred_lft forever
    inet6 fe80::288f:a8ff:fe1e:4211/64 scope link
       valid_lft forever preferred_lft forever
3505: eth0@if3506: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 8e:b8:5f:57:ff:30 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.128.1.199/32 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::8cb8:5fff:fe57:ff30/64 scope link
       valid_lft forever preferred_lft forever
```

```
$ oc exec -it pod2 -- ip r
default via 10.1.2.1 dev net1 
default via 10.128.1.155 dev eth0 mtu 1450
10.1.1.0/28 via 10.1.2.1 dev net1
10.1.2.0/28 dev net1 proto kernel scope link src 10.1.2.2
10.128.1.155 dev eth0 scope link
```

Default gateway

```
$ oc exec -it pod2 -- ping 10.1.2.1 -c 3
PING 10.1.2.1 (10.1.2.1) 56(84) bytes of data.
64 bytes from 10.1.2.1: icmp_seq=1 ttl=64 time=0.071 ms
64 bytes from 10.1.2.1: icmp_seq=2 ttl=64 time=0.036 ms
64 bytes from 10.1.2.1: icmp_seq=3 ttl=64 time=0.070 ms

--- 10.1.2.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2043ms
rtt min/avg/max/mdev = 0.036/0.059/0.071/0.016 ms
```

```
$ oc exec -it pod2 -- arp -n
? (10.1.2.1) at 3a:f4:d2:ff:95:6d [ether]  on net1
```

## host w/pod2

Virtual Ethernet (veth) between root network namespace and pod2 network namespace.

```
$ ip a
3507: mybr2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 3a:f4:d2:ff:95:6d brd ff:ff:ff:ff:ff:ff
    inet 10.1.2.1/28 brd 10.1.2.15 scope global mybr2
       valid_lft forever preferred_lft forever
    inet6 fe80::38f4:d2ff:feff:956d/64 scope link
       valid_lft forever preferred_lft forever
3508: veth5a6117d3@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master mybr2 state UP group default
    link/ether 9a:4e:46:90:4f:58 brd ff:ff:ff:ff:ff:ff link-netns 4e8f2de0-6e8b-421e-8fdf-35f08216f83d
    inet6 fe80::984e:46ff:fe90:4f58/64 scope link
       valid_lft forever preferred_lft forever
```

ifIndex (3508) also seen inside the pod as net1@if3508

```
$ bridge link
3508: veth5a6117d3@eno5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 master mybr2 state forwarding priority 32 cost 2
```

```
$ bridge fdb
33:33:00:00:00:01 dev mybr2 self permanent
01:00:5e:00:00:6a dev mybr2 self permanent
33:33:00:00:00:6a dev mybr2 self permanent
01:00:5e:00:00:01 dev mybr2 self permanent
33:33:ff:ff:95:6d dev mybr2 self permanent
3a:f4:d2:ff:95:6d dev mybr2 vlan 1 master mybr2 permanent
3a:f4:d2:ff:95:6d dev mybr2 master mybr2 permanent
2a:8f:a8:1e:42:11 dev veth5a6117d3 master mybr2
9a:4e:46:90:4f:58 dev veth5a6117d3 vlan 1 master mybr2 permanent
9a:4e:46:90:4f:58 dev veth5a6117d3 master mybr2 permanent
```

MAC addresses
- veth root network namespace 9a:4e:46:90:4f:58
- veth pod1 network namespace 2a:8f:a8:1e:42:11
- default gateway (bridge) 3a:f4:d2:ff:95:6d

## Connectivity between the pods

Requires IP route entries on both hosts

host w/pod1

```
$ sudo ip route add 10.1.2.0/28 via 10.58.24.98
```

host w/pod2

```
$ sudo ip route add 10.1.1.0/28 via 10.58.24.97
```

```
$ oc exec -it pod1 -- ping 10.1.2.1 -c 3
PING 10.1.2.1 (10.1.2.1) 56(84) bytes of data.
64 bytes from 10.1.2.1: icmp_seq=1 ttl=63 time=0.133 ms
64 bytes from 10.1.2.1: icmp_seq=2 ttl=63 time=0.116 ms
64 bytes from 10.1.2.1: icmp_seq=3 ttl=63 time=0.096 ms

--- 10.1.2.1 ping statistics ---
```

[[Back]](./README.md)