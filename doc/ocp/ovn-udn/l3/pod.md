# UDN w/L3 Topology - Step 2: POD

[[Back]](./overview.md) [[Prev](./udn.md)] [[Next]](./vm.md)

## Connection to POD CIDR

- POD **always** connects to Kubernetes POD CIDR
- the default route configuration depends on connection to UDN

## Connection to primary UDN w/l3 topology

- POD **may** connect to udn as primary interface
- [namespace](../namespace.md) must be labeled as primary enabled
- [udn](./udn.md) must be configured with role:Primary
- no definition required on the Pod CRD level

## Connection to secondary UDN w/l3 topology

- POD **may** connect to udn and that can be localnet
- no namespace label required
- [udn](./udn.md) must be configured with role:Secondary
- pod select nad created by udn

```
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: sl3
```

## CIDR example

```
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: sl3
  name: p1-1
  namespace: island-q
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
# iserver get k8s pod --namespace island-q -v net

+----+----------+---------+----------+----------------+-----+-------------------+--------------+
| ID | Pod      | HostNet | Intf     | Network        | Def | MAC               | IP           |
+----+----------+---------+----------+----------------+-----+-------------------+--------------+
| 1  | island-q | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:80:01:50 | 10.128.1.80  |
|    | p1-1     |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:15 | 66.66.0.21   | 
|    |          |         | net1     | island-q/sl3   | X   | 0a:58:42:42:01:04 | 66.66.1.4    |
+----+----------+---------+----------+----------------+-----+-------------------+--------------+
```

## IP Stack

```
$ oc exec -it -n island-q p1-1 -- ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
2: eth0@if19788: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:0a:80:01:50 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.128.1.80/23 brd 10.128.1.255 scope global eth0
3: ovn-udn1@if19789: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:00:15 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.0.21/28 brd 66.66.0.31 scope global ovn-udn1
4: net1@if19790: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:01:04 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.1.4/28 brd 66.66.1.15 scope global net1
```

```
$ oc exec -it -n island-q p1-1 -- ip r
default via 66.66.0.17 dev ovn-udn1 
10.128.0.0/23 dev eth0 proto kernel scope link src 10.128.1.80
10.128.0.0/14 via 10.128.0.1 dev eth0
66.66.0.0/24 via 66.66.0.17 dev ovn-udn1
66.66.0.16/28 dev ovn-udn1 proto kernel scope link src 66.66.0.21
66.66.1.0/28 dev net1 proto kernel scope link src 66.66.1.4
66.66.1.0/24 via 66.66.1.1 dev net1
100.64.0.0/16 via 10.128.0.1 dev eth0
100.65.0.0/16 via 66.66.0.17 dev ovn-udn1
172.30.0.0/16 via 66.66.0.17 dev ovn-udn1
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
              "10.128.1.80"
          ],
          "mac": "0a:58:0a:80:01:50",
          "dns": {}
      },{
          "name": "ovn-kubernetes",
          "interface": "ovn-udn1",
          "ips": [
              "66.66.0.21"
          ],
          "mac": "0a:58:42:42:00:15",
          "default": true,
          "dns": {}
      },{
          "name": "island-q/sl3",
          "interface": "net1",
          "ips": [
              "66.66.1.4"
          ],
          "mac": "0a:58:42:42:01:04",
          "dns": {}
      }]
    k8s.v1.cni.cncf.io/networks: sl3
```

[[Back]](./overview.md) [[Prev](./udn.md)] [[Next]](./vm.md)