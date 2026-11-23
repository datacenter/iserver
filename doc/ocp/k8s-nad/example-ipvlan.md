# Network Attachment Definition - IPVLAN - POD Functional Test

[[Back]](./README.md) [[Prev]](./crd-schema-ipvlan.md) [[Next]](./overview-ipvlan.md)

## NNCP

Create vlan-subinterface on every cluster node

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: policy
spec:
  desiredState:
    interfaces:
    - name: eno5.666
      state: up
      type: vlan
      vlan:
        base-iface: eno5
        id: 666
```

Note: mac address of vlan-subinterface will be the same inside the POD and seen by upstream switches

```
[core@bm1-1 ~]$ ifconfig eno5.666
eno5.666: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        ether 3c:57:31:cc:0d:b6  txqueuelen 1000  (Ethernet)
```

```
[core@bm1-2 ~]$ ifconfig eno5.666
eno5.666: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        ether 3c:57:31:cc:1f:26  txqueuelen 1000  (Ethernet)
```

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
      "cniVersion": "0.3.1",
      "type": "ipvlan",
      "master": "eno5.666",
      "mode": "l2",
      "ipam": {
        "type": "static",
        "addresses": [
          {
            "address": "10.10.10.1/24",
            "gateway": "10.10.10.254"
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
      "cniVersion": "0.3.1",
      "type": "ipvlan",
      "master": "eno5.666",
      "mode": "l2",
      "ipam": {
        "type": "static",
        "addresses": [
          {
            "address": "10.10.10.2/24",
            "gateway": "10.10.10.254"
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
$ oc exec pod1 -- ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: net1@if306: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN group default
    link/ether 3c:57:31:cc:0d:b6 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.10.10.1/24 brd 10.10.10.255 scope global net1
       valid_lft forever preferred_lft forever
    inet6 fe80::3c57:3100:1cc:db6/64 scope link
       valid_lft forever preferred_lft forever
309: eth0@if310: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether e2:2d:bc:d7:4f:17 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.128.3.129/32 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::e02d:bcff:fed7:4f17/64 scope link
       valid_lft forever preferred_lft forever
```

```
$ oc exec pod1 -- arp -n
? (10.10.10.2) at 3c:57:31:cc:1f:26 [ether]  on net1
```

```
$ oc exec pod1 -- ping 10.10.10.2 -c 3
PING 10.10.10.2 (10.10.10.2) 56(84) bytes of data.
64 bytes from 10.10.10.2: icmp_seq=1 ttl=64 time=0.114 ms
64 bytes from 10.10.10.2: icmp_seq=2 ttl=64 time=0.073 ms
64 bytes from 10.10.10.2: icmp_seq=3 ttl=64 time=0.099 ms

--- 10.10.10.2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2084ms
rtt min/avg/max/mdev = 0.073/0.095/0.114/0.016 ms
```

## Upstream Switch

```
leaf# show mac address-table vlan 666
Legend:
        * - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC
        age - seconds since last seen,+ - primary entry using vPC Peer-Link,
        (T) - True, (F) - False, C - ControlPlane MAC, ~ - vsan,
        (NA)- Not Applicable A - ESI Active Path, S - ESI Standby Path
        TL - True Learned, PS - Peer Sync, RO - Re-originate
   VLAN     MAC Address      Type      age     Secure NTFY Ports
---------+-----------------+--------+---------+------+----+------------------
*  666     3c57.31cc.0db6   dynamic  NA         F      F    Eth1/15
*  666     3c57.31cc.1f26   dynamic  NA         F      F    Eth1/16
```

[[Back]](./README.md) [[Prev]](./crd-schema-ipvlan.md) [[Next]](./overview-ipvlan.md)