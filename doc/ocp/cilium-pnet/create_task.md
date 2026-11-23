# Cilium Cluster Private Network - Create via Task

[[Back]](./README.md)

## Input

```
[
  {
    "cilium-pnet": {
      "feature": {},
      "webhook": {},
      "wipe": {},
      "test": {}
    }
  }
]
```

Notes:
- [feature](./enable.md), [webhook](./enable_webhook.md) [test](./test.md) trigger workflow execution with optional input parameters
- you can reuse exactly the same input file that was used for [delete task](./delete_task.md), some parameters may be silently ignored such as wipe
- not all workflows have to be defined however be aware of workflow execution requirements and dependencies

## Requirements

None

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Expected outcome

- cilium private network enabled
- private network test completed

## Example

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Cilium - Enable Private Network
====================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "fixup": false,
    "check-verbose": true,
    "namespace": "cilium",
    "package": "clife",
    "operator-name": "cilium-operator",
    "agent-name": "cilium"
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok



Operator
--------
- subscription          : cilium/clife
- package               : openshift-marketplace/certified-operators/clife
- channel               : 1.17
- install plan          : cilium/install-v6tpt
- install plan approved : ✓
- installed csv         : clife.v1.17.9-cee.1
- latest_csv            : ✓

~~~
cni:
  binPath: /var/lib/cni/bin
  chainingMode: portmap
  confPath: /var/run/multus/cni/net.d
  exclusive: false
enterprise:
  featureGate:
    strict: false
  privateNetworks:
    enabled: true

~~~

Cilium config update
--------------------
CiliumConfig CRD patched
Take a nap to detect automatic deployment restart...
Automatic pods rollout detected

Wait for Cilium resources
-------------------------
- pod: cilium-envoy-7c2z7
- pod: cilium-envoy-sm8bk
- pod: cilium-envoy-th29g
- pod: cilium-fdx2v
- pod: cilium-kdb8l
- pod: cilium-lxxp7
- pod: cilium-operator-6fcc595dd6-jsftn
- pod: cilium-operator-6fcc595dd6-tntn4
- pod: clife-controller-manager-7b4dd4bb46-nslcj
- deployment: cilium-operator
- deployment: clife-controller-manager

Check private network crd
-------------------------
- ClusterwidePrivateNetwork
- PrivateNetworkEndpointSlice
- PrivateNetworkExternalEndpoint

Completed tasks
- Private Network feature enabled
- CRD ready

OpenShift Workflow - Cilium - Private Network Functional Test
=============================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": false,
    "check-verbose": true,
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
    "namespace": "cilium",
    "package": "clife",
    "operator-name": "cilium-operator",
    "agent-name": "cilium"
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok



Operator
--------
- subscription          : cilium/clife
- package               : openshift-marketplace/certified-operators/clife
- channel               : 1.17
- install plan          : cilium/install-v6tpt
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
1031: eth0@if1032: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UP group default 
    link/ether d6:3a:9e:72:bf:21 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.168.250.33/32 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::3c62:6cff:fe10:8939/64 scope link 
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
1033: eth0@if1034: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UP group default 
    link/ether d6:3a:9e:72:bf:22 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.168.250.34/32 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::6c66:8dff:fe33:2f16/64 scope link 
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
1035: eth0@if1036: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UP group default 
    link/ether d6:3a:9e:72:bf:23 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.168.250.33/32 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::d8b7:e4ff:fec9:3704/64 scope link 
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
1037: eth0@if1038: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UP group default 
    link/ether d6:3a:9e:72:bf:24 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.168.250.35/32 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::b422:5eff:feab:f8a3/64 scope link 
       valid_lft forever preferred_lft forever

~~~
IP address match
MAC address match

Validate connectivity within the network
----------------------------------------
Network: test-network-a
~~~
PING 192.168.250.34 (192.168.250.34) 56(84) bytes of data.
64 bytes from 192.168.250.34: icmp_seq=1 ttl=63 time=0.093 ms
64 bytes from 192.168.250.34: icmp_seq=2 ttl=63 time=0.077 ms
64 bytes from 192.168.250.34: icmp_seq=3 ttl=63 time=0.077 ms

--- 192.168.250.34 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2057ms
rtt min/avg/max/mdev = 0.077/0.082/0.093/0.007 ms

~~~
Ping successful

Network: test-network-b
~~~
PING 192.168.250.35 (192.168.250.35) 56(84) bytes of data.
64 bytes from 192.168.250.35: icmp_seq=1 ttl=63 time=0.096 ms
64 bytes from 192.168.250.35: icmp_seq=2 ttl=63 time=0.075 ms
64 bytes from 192.168.250.35: icmp_seq=3 ttl=63 time=0.073 ms

--- 192.168.250.35 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2067ms
rtt min/avg/max/mdev = 0.073/0.081/0.096/0.010 ms

~~~
Ping successful

Validate connectivity across the network
----------------------------------------
Network: test-network-a
~~~
PING 192.168.250.35 (192.168.250.35) 56(84) bytes of data.

--- 192.168.250.35 ping statistics ---
3 packets transmitted, 0 received, 100% packet loss, time 2070ms


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

Test completed successfully
```

[[Back]](./README.md)