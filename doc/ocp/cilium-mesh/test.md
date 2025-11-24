# Cilium Private Network - Functional test

## Workflow

- create two private networks
- deploy two pods on each network in dedicated test namespace
- verify ip and mac address assignment
- verify that pods can ping if on the same network
- verify that pods cannot ping if on the different network
- cleanup test setup
- in case workflow breaks i.e. unexpected state, it exits leaving the resources as-is for further analysis
- if --no-confirm is used, every configuration step must be acknowledged

## Requirements

Private network [enabled](./enable.md)

## Configurable options

```
# iserver set ocp cilium pnet --mode test
  --cluster TEXT     Cluster Name
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp cilium pnet --mode test --cluster bm1 --no-confirm

OpenShift Workflow - Cilium - Private Network Functional Test
=============================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "test-namespace": "test-pnet",
    "test-network-a": {
        "name": "test-network-a",
        "cidr4": "192.168.250.0/24",
        "cidr6": "fd10:0:250::0/64",
        "pod1": "pod-a1",
        "pod1v4": "192.168.250.33",
        "pod1v6": "fd10:0:250::33",
        "pod1mac": "d6:3a:9e:72:bf:21",
        "pod2": "pod-a2",
        "pod2v4": "192.168.250.34",
        "pod2v6": "fd10:0:250::34",
        "pod2mac": "d6:3a:9e:72:bf:22"
    },
    "test-network-b": {
        "name": "test-network-b",
        "cidr4": "192.168.250.0/24",
        "cidr6": "fd10:0:250::0/64",
        "pod1": "pod-b1",
        "pod1v4": "192.168.250.33",
        "pod1v6": "fd10:0:250::33",
        "pod1mac": "d6:3a:9e:72:bf:23",
        "pod2": "pod-b2",
        "pod2v4": "192.168.250.35",
        "pod2v6": "fd10:0:250::35",
        "pod2mac": "d6:3a:9e:72:bf:24"
    },
    "cleanup": true,
    "cleanup-on-error": false,
    "check-verbose": true,
    "namespace": "cilium",
    "package": "clife",
    "operator-name": "cilium-operator",
    "agent-name": "cilium"
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok



Operator
--------
- subscription          : cilium/clife
- package               : openshift-marketplace/certified-operators/clife
- channel               : 1.17
- install plan          : cilium/install-8rhpx
- install plan approved : ✓
- installed csv         : clife.v1.17.9-cee.1
- latest_csv            : ✓


Check private network crd
-------------------------
- ClusterwidePrivateNetwork
- PrivateNetworkEndpointSlice
- PrivateNetworkExternalEndpoint

Create namespace
----------------
- namespace: test-pnet
- namespace does not exist
- namespace created

Create Clusterwide Private Network
----------------------------------
- name: test-network-a
- cidrv4: 192.168.250.0/24
- cidrv6: fd10:0:250::0/64

~~~
apiVersion: isovalent.com/v1alpha1
kind: ClusterwidePrivateNetwork
metadata:
  name: test-network-a
spec:
  subnets:
  - cidr: 192.168.250.0/24
  - cidr: fd10:0:250::0/64

~~~

Network created

Wait for network...

Create Clusterwide Private Network
----------------------------------
- name: test-network-b
- cidrv4: 192.168.250.0/24
- cidrv6: fd10:0:250::0/64

~~~
apiVersion: isovalent.com/v1alpha1
kind: ClusterwidePrivateNetwork
metadata:
  name: test-network-b
spec:
  subnets:
  - cidr: 192.168.250.0/24
  - cidr: fd10:0:250::0/64

~~~

Network created

Wait for network...
Create pods
apiVersion: v1
kind: Pod
metadata:
  annotations:
    network.v1alpha1.isovalent.com/network-attachment: '{"network": "test-network-a",
      "ipv4": "192.168.250.33", "ipv6": "fd10:0:250::33", "mac": "d6:3a:9e:72:bf:21"}'
  name: pod-a1
  namespace: test-pnet
spec:
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot

apiVersion: v1
kind: Pod
metadata:
  annotations:
    network.v1alpha1.isovalent.com/network-attachment: '{"network": "test-network-a",
      "ipv4": "192.168.250.34", "ipv6": "fd10:0:250::34", "mac": "d6:3a:9e:72:bf:22"}'
  name: pod-a2
  namespace: test-pnet
spec:
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot

apiVersion: v1
kind: Pod
metadata:
  annotations:
    network.v1alpha1.isovalent.com/network-attachment: '{"network": "test-network-b",
      "ipv4": "192.168.250.33", "ipv6": "fd10:0:250::33", "mac": "d6:3a:9e:72:bf:23"}'
  name: pod-b1
  namespace: test-pnet
spec:
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot

apiVersion: v1
kind: Pod
metadata:
  annotations:
    network.v1alpha1.isovalent.com/network-attachment: '{"network": "test-network-b",
      "ipv4": "192.168.250.35", "ipv6": "fd10:0:250::35", "mac": "d6:3a:9e:72:bf:24"}'
  name: pod-b2
  namespace: test-pnet
spec:
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot

Wait for pods
- test-pnet/pod-a1
- test-pnet/pod-a2
- test-pnet/pod-b1
- test-pnet/pod-b2

Validate IP address assingment
------------------------------
Pod test-pnet/pod-a1
~~~
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
229: eth0@if230: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UP group default
    link/ether d6:3a:9e:72:bf:21 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.168.250.33/32 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::78d2:bcff:fe5b:d554/64 scope link
       valid_lft forever preferred_lft forever

~~~
IP address match
MAC address match

Pod test-pnet/pod-a2
~~~
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
231: eth0@if232: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UP group default
    link/ether d6:3a:9e:72:bf:22 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.168.250.34/32 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::e887:16ff:fe63:e185/64 scope link
       valid_lft forever preferred_lft forever

~~~
IP address match
MAC address match

Pod test-pnet/pod-b1
~~~
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
233: eth0@if234: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UP group default
    link/ether d6:3a:9e:72:bf:23 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.168.250.33/32 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::ec8b:dfff:fe16:3d1a/64 scope link
       valid_lft forever preferred_lft forever

~~~
IP address match
MAC address match

Pod test-pnet/pod-b2
~~~
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
235: eth0@if236: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UP group default
    link/ether d6:3a:9e:72:bf:24 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.168.250.35/32 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::7c5d:47ff:fef0:7e81/64 scope link
       valid_lft forever preferred_lft forever

~~~
IP address match
MAC address match

Validate connectivity within the network
----------------------------------------
Network: test-network-a
~~~
PING 192.168.250.34 (192.168.250.34) 56(84) bytes of data.
64 bytes from 192.168.250.34: icmp_seq=1 ttl=63 time=0.087 ms
64 bytes from 192.168.250.34: icmp_seq=2 ttl=63 time=0.082 ms
64 bytes from 192.168.250.34: icmp_seq=3 ttl=63 time=0.083 ms

--- 192.168.250.34 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2038ms
rtt min/avg/max/mdev = 0.082/0.084/0.087/0.002 ms

~~~
Ping successful

Network: test-network-b
~~~
PING 192.168.250.35 (192.168.250.35) 56(84) bytes of data.
64 bytes from 192.168.250.35: icmp_seq=1 ttl=63 time=0.089 ms
64 bytes from 192.168.250.35: icmp_seq=2 ttl=63 time=0.095 ms
64 bytes from 192.168.250.35: icmp_seq=3 ttl=63 time=0.087 ms

--- 192.168.250.35 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2045ms
rtt min/avg/max/mdev = 0.087/0.090/0.095/0.003 ms

~~~
Ping successful

Validate connectivity across the network
----------------------------------------
Network: test-network-a
~~~
PING 192.168.250.35 (192.168.250.35) 56(84) bytes of data.

--- 192.168.250.35 ping statistics ---
3 packets transmitted, 0 received, 100% packet loss, time 2051ms


~~~
Ping unsuccessful
Delete pods
- test-pnet/pod-a1
- test-pnet/pod-a2
- test-pnet/pod-b1
- test-pnet/pod-b2

Delete Clusterwide Private Network
----------------------------------
- name: test-network-a

Network deleted

Wait for not network...

Delete Clusterwide Private Network
----------------------------------
- name: test-network-b

Network deleted

Wait for not network...

Delete namespace
----------------
- namespace deleted: test-pnet
```

[[Back]](./README.md)