# Network Attachment Definition - VLAN - Functional Test

## Phy interface

Note: there is no need for NNCP to create vlan-subinterface on the main interface

```
[core@bm1-1 ~]$ ifconfig eno5
eno5: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::3652:1d6e:97d4:e89  prefixlen 64  scopeid 0x20<link>
        ether 3c:57:31:cc:0d:b6  txqueuelen 1000  (Ethernet)
        RX packets 735301  bytes 43915790 (41.8 MiB)
        RX errors 0  dropped 139  overruns 0  frame 0
        TX packets 21715  bytes 3586412 (3.4 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

```
[core@bm1-2 ~]$ ifconfig eno5
eno5: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::aadf:9818:7fef:1531  prefixlen 64  scopeid 0x20<link>
        ether 3c:57:31:cc:1f:26  txqueuelen 1000  (Ethernet)
        RX packets 130  bytes 35327 (34.4 KiB)
        RX errors 0  dropped 94  overruns 0  frame 0
        TX packets 20158  bytes 3333027 (3.1 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
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
      "type": "vlan",
      "master": "eno5",
      "vlanId": 666,
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
      "type": "vlan",
      "master": "eno5",
      "vlanId": 666,
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
2: net1@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 3c:57:31:cc:0d:b6 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.10.10.1/24 brd 10.10.10.255 scope global net1
       valid_lft forever preferred_lft forever
    inet6 fe80::3e57:31ff:fecc:db6/64 scope link
       valid_lft forever preferred_lft forever
329: eth0@if330: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 36:57:5b:42:bb:63 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.128.3.61/32 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::3457:5bff:fe42:bb63/64 scope link
       valid_lft forever preferred_lft forever
```

```
$ oc exec pod1 -- arp -n
? (10.10.10.2) at 3c:57:31:cc:1f:26 [ether]  on net1
```

```
$ oc exec pod1 -- ping 10.10.10.2 -c 3
PING 10.10.10.2 (10.10.10.2) 56(84) bytes of data.
64 bytes from 10.10.10.2: icmp_seq=1 ttl=64 time=0.055 ms
64 bytes from 10.10.10.2: icmp_seq=2 ttl=64 time=0.052 ms
64 bytes from 10.10.10.2: icmp_seq=3 ttl=64 time=0.056 ms

--- 10.10.10.2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2074ms
rtt min/avg/max/mdev = 0.052/0.054/0.056/0.001 ms
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

[[Back]](./README.md)