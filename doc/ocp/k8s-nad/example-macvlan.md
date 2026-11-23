# Network Attachment Definition - MacVLAN - Functional Test

[[Back]](./README.md) [[Prev]](./crd-schema-macvlan.md) [[Next]](./overview-macvlan.md)

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

Note: mac address of vlan-subinterface will be different inside the POD

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
      "type": "macvlan",
      "master": "eno5.666",
      "mode": "bridge",
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
      "type": "macvlan",
      "master": "eno5.666",
      "mode": "bridge",
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
  nodeName: bm3-1
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
  nodeName: bm3-2
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
2: net1@if306: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 5e:6d:89:7b:95:e0 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.10.10.1/24 brd 10.10.10.255 scope global net1
       valid_lft forever preferred_lft forever
    inet6 fe80::5c6d:89ff:fe7b:95e0/64 scope link
       valid_lft forever preferred_lft forever
307: eth0@if308: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 4a:b6:5d:f5:78:d8 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.128.3.90/32 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::48b6:5dff:fef5:78d8/64 scope link
       valid_lft forever preferred_lft forever
```

```
$ oc exec pod1 -- arp -n
? (10.10.10.2) at ca:14:1d:60:c7:b7 [ether]  on net1
```

```
$ oc exec pod1 -- ping 10.10.10.2 -c 3
PING 10.10.10.2 (10.10.10.2) 56(84) bytes of data.
64 bytes from 10.10.10.2: icmp_seq=1 ttl=64 time=0.095 ms
64 bytes from 10.10.10.2: icmp_seq=2 ttl=64 time=0.081 ms
64 bytes from 10.10.10.2: icmp_seq=3 ttl=64 time=0.091 ms

--- 10.10.10.2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2060ms
rtt min/avg/max/mdev = 0.081/0.089/0.095/0.005 ms
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
*  666     5e6d.897b.95e0   dynamic  NA         F      F    Eth1/15
*  666     ca14.1d60.c7b7   dynamic  NA         F      F    Eth1/16
```

[[Back]](./README.md) [[Prev]](./crd-schema-macvlan.md) [[Next]](./overview-macvlan.md)