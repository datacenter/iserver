# UDN and POD - State

[[Back]](../README.md) [[Prev]](../create/pod_task.md) [[Next]](../overview/pod.md)

```
$ oc exec -n island p1-3 -- ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
2: eth0@if211: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:0a:82:00:7f brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.130.0.127/23 brd 10.130.1.255 scope global eth0
3: ovn-udn1@if212: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:00:06 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.0.6/24 brd 66.66.0.255 scope global ovn-udn1
4: net1@if213: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:01:03 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.1.3/24 brd 66.66.1.255 scope global net1
5: net2@if214: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc noqueue state UP group default
    link/ether 0a:58:42:42:02:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 66.66.2.2/24 brd 66.66.2.255 scope global net2
```

```
$ oc exec -n island p1-3 -- ip r
default via 66.66.0.1 dev ovn-udn1 
66.66.1.0/24 dev net1 proto kernel scope link src 66.66.1.3
66.66.2.0/24 dev net2 proto kernel scope link src 66.66.2.2
```

```
# iserver get k8s pod --namespace island -v net
Cluster: bm1 (type: ocp)

+----+--------+---------+----------+----------------+-----+-------------------+--------------+
| ID | Pod    | HostNet | Intf     | Network        | Def | MAC               | IP           |
+----+--------+---------+----------+----------------+-----+-------------------+--------------+
| 1  | island | X       | eth0     | ovn-kubernetes | X   | 0a:58:0a:82:00:7f | 10.130.0.127 |
|    | p1-3   |         | ovn-udn1 | ovn-kubernetes | V   | 0a:58:42:42:00:06 | 66.66.0.6    |
|    |        |         | net1     | island/s1-l2   | X   | 0a:58:42:42:01:03 | 66.66.1.3    |
|    |        |         | net2     | island/s2-l2   | X   | 0a:58:42:42:02:02 | 66.66.2.2    |
+----+--------+---------+----------+----------------+-----+-------------------+--------------+
```

```
# oc get pod -n island p1-3 -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "ovn-kubernetes",
          "interface": "eth0",
          "ips": [
              "10.130.0.127"
          ],
          "mac": "0a:58:0a:82:00:7f",
          "dns": {}
      },{
          "name": "ovn-kubernetes",
          "interface": "ovn-udn1",
          "ips": [
              "66.66.0.6"
          ],
          "mac": "0a:58:42:42:00:06",
          "default": true,
          "dns": {}
      },{
          "name": "island/s1-l2",
          "interface": "net1",
          "ips": [
              "66.66.1.3"
          ],
          "mac": "0a:58:42:42:01:03",
          "dns": {}
      },{
          "name": "island/s2-l2",
          "interface": "net2",
          "ips": [
              "66.66.2.2"
          ],
          "mac": "0a:58:42:42:02:02",
          "dns": {}
      }]
    k8s.v1.cni.cncf.io/networks: s1-l2,s2-l2
```

[[Back]](../README.md) [[Prev]](../create/pod_task.md) [[Next]](../overview/pod.md)