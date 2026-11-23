# UDN w/L2 Topology - Step 2: POD

[[Back]](./overview.md) [[Prev](./udn.md)] [[Next]](./vm.md)

## Connection to POD CIDR

- POD **always** connects to Kubernetes POD CIDR
- the default route configuration depends on connection to UDN

## Connection to primary UDN w/l2 topology

- POD **may** connect to udn as primary interface
- [namespace](../namespace.md) must be labeled as primary enabled
- [udn](./udn.md) must be configured with role:Primary
- no definition required on the Pod CRD level

## Connection to secondary UDN w/l2 topology

- POD **may** connect to udn and that can be localnet
- no namespace label required
- [udn](./udn.md) must be configured with role:Secondary
- pod select nad created by udn

```
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: sl2
```

## CIDR example

```
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: sl2
  name: p1-1
  namespace: island-p
spec:
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot
    securityContext:
      capabilities:
        add:
        - IPC_LOCK
        - SYS_RESOURCE
        - NET_RAW
      runAsUser: 0
  nodeName: bm1-1
```

## POD state example

```
# iserver get k8s pod --namespace island-y2 -v net

+----+----------+---------+----------+----------------+-----+-------------------+--------------+
| ID | Pod      | HostNet | Intf     | Network        | Def | MAC               | IP           |
+----+----------+---------+----------+----------------+-----+-------------------+--------------+
| 1  | island-p | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:80:01:4a | 10.128.1.74  |
|    | p1-1     |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:04 | 66.66.0.4    |
|    |          |         | net1     | island-p/sl2   | X   | 0a:58:42:42:01:03 | 66.66.1.3    |
+----+----------+---------+----------+----------------+-----+-------------------+--------------+
```

## IP Stack

```
$ oc exec -it -n island-p p1-1 -- ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
2: eth0@if19774: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:0a:80:01:4a brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.128.1.74/23 brd 10.128.1.255 scope global eth0
3: ovn-udn1@if19775: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:00:04 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.0.4/24 brd 66.66.0.255 scope global ovn-udn1
4: net1@if19776: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:01:03 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.1.3/24 brd 66.66.1.255 scope global net1
```

```
$ oc exec -it -n island-p p1-1 -- ip r
default via 66.66.0.1 dev ovn-udn1 
10.128.0.0/23 dev eth0 proto kernel scope link src 10.128.1.74
10.128.0.0/14 via 10.128.0.1 dev eth0
66.66.0.0/24 dev ovn-udn1 proto kernel scope link src 66.66.0.4
66.66.1.0/24 dev net1 proto kernel scope link src 66.66.1.3
100.64.0.0/16 via 10.128.0.1 dev eth0
100.65.0.0/16 via 66.66.0.1 dev ovn-udn1
172.30.0.0/16 via 66.66.0.1 dev ovn-udn1
```

## Annotation

```
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "ovn-kubernetes",
          "interface": "eth0",
          "ips": [
              "10.128.1.74"
          ],
          "mac": "0a:58:0a:80:01:4a",
          "dns": {}
      },{
          "name": "ovn-kubernetes",
          "interface": "ovn-udn1",
          "ips": [
              "66.66.0.4"
          ],
          "mac": "0a:58:42:42:00:04",
          "default": true,
          "dns": {}
      },{
          "name": "island-p/sl2",
          "interface": "net1",
          "ips": [
              "66.66.1.3"
          ],
          "mac": "0a:58:42:42:01:03",
          "dns": {}
      }]
    k8s.v1.cni.cncf.io/networks: sl2
```

[[Back]](./overview.md) [[Prev](./udn.md)] [[Next]](./vm.md)