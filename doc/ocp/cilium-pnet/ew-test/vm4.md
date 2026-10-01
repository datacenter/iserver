# Private Network - east-west connectivity test

[[Back]](./README.md) [[Next]](./p5.md) [[Prev]](./vm3.md)

![Overview](../../images/pnet/ew.png)

## vm4 - primary pod, 1st secondary privnet:blue, 2nd secondary privnet:red

Kubevirt VM secondary connection to private network `X` with ipv4 address `Y` belonging to subnet `Z` requires annotation and `bridge` mode. `N/X-Z` selects the NetworkAttachmentDefinition auto-created for privnet `X`. Repeat the same logic for multiple secondary interfaces

```yaml
spec:
  template:
    metadata:
      annotations:
        privnet.isovalent.com/secondary-network-attachments: '[{"network": "X", "ipv4": "Y"}]'
    spec:
      domain:
        devices:
          interfaces:
          - bridge: {}
            name: eth1
      networks:
      - multus:
          networkName: N/X-Z
        name: eth1
```

```shell
iserver create k8s vm --namespace b --name vm4 --template cirros \
    --network pod \
    --network pnet,blue,10.10.10.4 \
    --network pnet,red,20.20.21.4
```

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  labels:
    app: vm4
  name: vm4
  namespace: b
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: vm4
      namespace: b
    spec:
      pvc:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 500Mi
        volumeMode: Filesystem
      source:
        registry:
          url: docker://quay.io/kubevirt/cirros-container-disk-demo
  runStrategy: Always
  template:
    metadata:
      annotations:
        privnet.isovalent.com/secondary-network-attachments: '[{"network": "blue",
          "ipv4": "10.10.10.4"}, {"network": "red", "ipv4": "20.20.21.4"}]'
      labels:
        kubevirt.io/domain: vm4
    spec:
      domain:
        cpu:
          cores: 1
          sockets: 1
          threads: 1
        devices:
          disks:
          - disk:
              bus: virtio
            name: rootdisk
          interfaces:
          - masquerade: {}
            name: default
          - bridge: {}
            name: eth1
          - bridge: {}
            name: eth2
          rng: {}
        resources:
          requests:
            memory: 1Gi
      evictionStrategy: LiveMigrate
      hostname: vm4
      networks:
      - name: default
        pod: {}
      - multus:
          networkName: b/blue-subnet-0
        name: eth1
      - multus:
          networkName: b/red-subnet-1
        name: eth2
      volumes:
      - dataVolume:
          name: vm4
        name: rootdisk
```

## IP Stack

>[!CAUTION]
>Multus interfaces are **not** automatically configured with ip settings. The changes can be done via CLI or wrapped into cloud-init / network-data startup files.

```
$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast qlen 1000
    link/ether 52:f0:72:87:e2:1f brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.2/24 brd 10.0.2.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::50f0:72ff:fe87:e21f/64 scope link 
       valid_lft forever preferred_lft forever
3: eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop qlen 1000
    link/ether ce:68:ae:48:23:52 brd ff:ff:ff:ff:ff:ff
4: eth2: <BROADCAST,MULTICAST> mtu 1500 qdisc noop qlen 1000
    link/ether f6:ba:77:ee:88:a4 brd ff:ff:ff:ff:ff:ff
```

### Add privnet:blue

```
sudo ip addr add 10.10.10.4/32 dev eth1
sudo ifconfig eth1 up
sudo ip route add 10.10.10.0/24 via 169.254.0.2 dev eth1 onlink
```

### Add privnet:red

```
sudo ip addr add 20.20.21.4/32 dev eth2
sudo ifconfig eth2 up
sudo ip route add 20.20.20.0/24 via 169.254.0.3 dev eth2 onlink
sudo ip route add 20.20.21.0/24 via 169.254.0.3 dev eth2 onlink
```

### Test connectivity

```
$ ip a
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast qlen 1000
    link/ether 52:f0:72:87:e2:1f brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.2/24 brd 10.0.2.255 scope global eth0
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast qlen 1000
    link/ether ce:68:ae:48:23:52 brd ff:ff:ff:ff:ff:ff
    inet 10.10.10.4/32 scope global eth1
4: eth2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast qlen 1000
    link/ether f6:ba:77:ee:88:a4 brd ff:ff:ff:ff:ff:ff
    inet 20.20.21.4/32 scope global eth2
```

```
$ ip r
default via 10.0.2.1 dev eth0 
10.0.2.0/24 dev eth0  src 10.0.2.2 
10.10.10.0/24 via 169.254.0.2 dev eth1 onlink 
20.20.20.0/24 via 169.254.0.3 dev eth2 onlink 
20.20.21.0/24 via 169.254.0.3 dev eth2 onlink
```

```
$ ping 10.10.10.1 -c 1
PING 10.10.10.1 (10.10.10.1): 56 data bytes
64 bytes from 10.10.10.1: seq=0 ttl=63 time=0.397 ms

$ ping 10.10.10.2 -c 1
PING 10.10.10.2 (10.10.10.2): 56 data bytes
64 bytes from 10.10.10.2: seq=0 ttl=63 time=0.156 ms

$ ping 10.10.10.3 -c 1
PING 10.10.10.3 (10.10.10.3): 56 data bytes
64 bytes from 10.10.10.3: seq=0 ttl=63 time=0.529 ms
```

```
$ arp -n
? (10.0.2.1) at 02:00:00:00:00:00 [ether]  on eth0
? (169.254.0.2) at c2:5a:1a:a4:b0:1c [ether]  on eth1
```

## eBPF Map (delta)

Every privnet connection triggers single endpoint and map entry

```
Cilium Agent Database
-------------------
- network  : 2
- subnet   : 3
- route    : 5
- inb      : 0
- endpoint : 5 (+2)
- map      : 7 (+2)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+-----------------+----------+-----------+----------------------------------------+------------+-------------------+--------------+-------+----------+
| ID | Private Network | Subnet   | Namespace | Name                                   | IP         | MAC               | POD IP       | Node  | External |
+----+-----------------+----------+-----------+----------------------------------------+------------+-------------------+--------------+-------+----------+
| 4  | red             | subnet-1 | b         | virt-launcher-vm4-n7pz7-pod151b6d47576 | 20.20.21.4 | f6:ba:77:ee:88:a4 | 10.128.0.248 | bm1-2 | False    | 
| 5  | blue            | subnet-0 | b         | virt-launcher-vm4-n7pz7-pod980816f36b7 | 10.10.10.4 | ce:68:ae:48:23:52 | 10.128.0.135 | bm1-2 | False    | 
+----+-----------------+----------+-----------+----------------------------------------+------------+-------------------+--------------+-------+----------+

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-mapentries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
| ID | Type | Network      | Subnet           | CIDR          | MAC               | NH           | IfIndex | VNI | L2 Announce | Status | Gneigh |
+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
| 4  | E    | blue [15476] | subnet-0 [7581]  | 10.10.10.4/32 | ce:68:ae:48:23:52 | 10.128.0.135 | 0       | --- | False       | Done   | Done   | 
| 6  | E    | red [15477]  | subnet-1 [58679] | 20.20.21.4/32 | f6:ba:77:ee:88:a4 | 10.128.0.248 | 0       | --- | False       | Done   | Done   | 
+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
```

## eBPF Map (full)

```
Cilium Agent Database
---------------------
- network  : 2
- subnet   : 3
- route    : 5
- inb      : 0
- endpoint : 5
- map      : 7


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: private-networks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+-----------------+-------+-----+--------------------------------+
| ID | Private Network | ID    | VNI | Subnet                         |
+----+-----------------+-------+-----+--------------------------------+
| 1  | blue            | 15476 | --- | [                              | 
|    |                 |       |     |   {                            | 
|    |                 |       |     |     "Name": "subnet-0",        | 
|    |                 |       |     |     "CIDRv4": "10.10.10.0/24", | 
|    |                 |       |     |     "CIDRv6": "",              | 
|    |                 |       |     |     "Routes": [],              | 
|    |                 |       |     |     "DHCP": {                  | 
|    |                 |       |     |       "mode": "none"           | 
|    |                 |       |     |     }                          | 
|    |                 |       |     |   }                            | 
|    |                 |       |     | ]                              | 
+----+-----------------+-------+-----+--------------------------------+
| 2  | red             | 15477 | --- | [                              | 
|    |                 |       |     |   {                            | 
|    |                 |       |     |     "Name": "subnet-0",        | 
|    |                 |       |     |     "CIDRv4": "20.20.20.0/24", | 
|    |                 |       |     |     "CIDRv6": "",              | 
|    |                 |       |     |     "Routes": [],              | 
|    |                 |       |     |     "DHCP": {                  | 
|    |                 |       |     |       "mode": "none"           | 
|    |                 |       |     |     }                          | 
|    |                 |       |     |   },                           | 
|    |                 |       |     |   {                            | 
|    |                 |       |     |     "Name": "subnet-1",        | 
|    |                 |       |     |     "CIDRv4": "20.20.21.0/24", | 
|    |                 |       |     |     "CIDRv6": "",              | 
|    |                 |       |     |     "Routes": [],              | 
|    |                 |       |     |     "DHCP": {                  | 
|    |                 |       |     |       "mode": "none"           | 
|    |                 |       |     |     }                          | 
|    |                 |       |     |   }                            | 
|    |                 |       |     | ]                              | 
+----+-----------------+-------+-----+--------------------------------+

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-subnets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+-----------------+------------------+------+---------------+--------+-----+-------+
| ID | Private Network | Subnet           | DHCP | CIDRv4        | CIDRv6 | VNI | Route |
+----+-----------------+------------------+------+---------------+--------+-----+-------+
| 1  | blue [15476]    | subnet-0 [7581]  | none | 10.10.10.0/24 |        | --- | []    | 
| 2  | red [15477]     | subnet-0 [58678] | none | 20.20.20.0/24 |        | --- | []    | 
| 3  | red [15477]     | subnet-1 [58679] | none | 20.20.21.0/24 |        | --- | []    | 
+----+-----------------+------------------+------+---------------+--------+-----+-------+

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-routes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+-----------------+----------+---------------+---------+-------+-------------------------+
| ID | Private Network | Subnet   | Destination   | Gateway | EVPN  | Peer                    |
+----+-----------------+----------+---------------+---------+-------+-------------------------+
| 1  | blue            | subnet-0 | 10.10.10.0/24 |         | False | {                       | 
|    |                 |          |               |         |       |   "Network": "",        | 
|    |                 |          |               |         |       |   "Subnet": "",         | 
|    |                 |          |               |         |       |   "ID": {               | 
|    |                 |          |               |         |       |     "Network": 0,       | 
|    |                 |          |               |         |       |     "Subnet": 0         | 
|    |                 |          |               |         |       |   }                     | 
|    |                 |          |               |         |       | }                       | 
+----+-----------------+----------+---------------+---------+-------+-------------------------+
| 2  | red             | subnet-0 | 20.20.20.0/24 |         | False | {                       | 
|    |                 |          |               |         |       |   "Network": "",        | 
|    |                 |          |               |         |       |   "Subnet": "",         | 
|    |                 |          |               |         |       |   "ID": {               | 
|    |                 |          |               |         |       |     "Network": 0,       | 
|    |                 |          |               |         |       |     "Subnet": 0         | 
|    |                 |          |               |         |       |   }                     | 
|    |                 |          |               |         |       | }                       | 
+----+-----------------+----------+---------------+---------+-------+-------------------------+
| 3  | red             | subnet-0 | 20.20.21.0/24 |         | False | {                       | 
|    |                 |          |               |         |       |   "Network": "red",     | 
|    |                 |          |               |         |       |   "Subnet": "subnet-1", | 
|    |                 |          |               |         |       |   "ID": {               | 
|    |                 |          |               |         |       |     "Network": 15477,   | 
|    |                 |          |               |         |       |     "Subnet": 58679     | 
|    |                 |          |               |         |       |   }                     | 
|    |                 |          |               |         |       | }                       | 
+----+-----------------+----------+---------------+---------+-------+-------------------------+
| 4  | red             | subnet-1 | 20.20.20.0/24 |         | False | {                       | 
|    |                 |          |               |         |       |   "Network": "red",     | 
|    |                 |          |               |         |       |   "Subnet": "subnet-0", | 
|    |                 |          |               |         |       |   "ID": {               | 
|    |                 |          |               |         |       |     "Network": 15477,   | 
|    |                 |          |               |         |       |     "Subnet": 58678     | 
|    |                 |          |               |         |       |   }                     | 
|    |                 |          |               |         |       | }                       | 
+----+-----------------+----------+---------------+---------+-------+-------------------------+
| 5  | red             | subnet-1 | 20.20.21.0/24 |         | False | {                       | 
|    |                 |          |               |         |       |   "Network": "",        | 
|    |                 |          |               |         |       |   "Subnet": "",         | 
|    |                 |          |               |         |       |   "ID": {               | 
|    |                 |          |               |         |       |     "Network": 0,       | 
|    |                 |          |               |         |       |     "Subnet": 0         | 
|    |                 |          |               |         |       |   }                     | 
|    |                 |          |               |         |       | }                       | 
+----+-----------------+----------+---------------+---------+-------+-------------------------+

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+-----------------+----------+-----------+----------------------------------------+------------+-------------------+--------------+-------+----------+
| ID | Private Network | Subnet   | Namespace | Name                                   | IP         | MAC               | POD IP       | Node  | External |
+----+-----------------+----------+-----------+----------------------------------------+------------+-------------------+--------------+-------+----------+
| 1  | blue            | subnet-0 | a         | p1                                     | 10.10.10.1 | 72:54:31:fa:5a:72 | 10.128.2.68  | bm1-1 | False    | 
| 2  | blue            | subnet-0 | a         | p2-eth1                                | 10.10.10.2 | 0e:a6:dd:6d:7d:b6 | 10.128.1.68  | bm1-2 | False    | 
| 3  | blue            | subnet-0 | b         | virt-launcher-vm3-h24s6                | 10.10.10.3 | de:fa:ad:37:56:1d | 10.128.2.129 | bm1-1 | False    | 
| 4  | red             | subnet-1 | b         | virt-launcher-vm4-n7pz7-pod151b6d47576 | 20.20.21.4 | f6:ba:77:ee:88:a4 | 10.128.0.248 | bm1-2 | False    | 
| 5  | blue            | subnet-0 | b         | virt-launcher-vm4-n7pz7-pod980816f36b7 | 10.10.10.4 | ce:68:ae:48:23:52 | 10.128.0.135 | bm1-2 | False    | 
+----+-----------------+----------+-----------+----------------------------------------+------------+-------------------+--------------+-------+----------+

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-mapentries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
| ID | Type | Network      | Subnet           | CIDR          | MAC               | NH           | IfIndex | VNI | L2 Announce | Status | Gneigh |
+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
| 1  | E    | blue [15476] | subnet-0 [7581]  | 10.10.10.1/32 | 72:54:31:fa:5a:72 | 10.128.2.68  | 0       | --- | False       | Done   | Done   | 
| 2  | E    | blue [15476] | subnet-0 [7581]  | 10.10.10.2/32 | 0e:a6:dd:6d:7d:b6 | 10.128.1.68  | 0       | --- | False       | Done   | Done   | 
| 3  | E    | blue [15476] | subnet-0 [7581]  | 10.10.10.3/32 | de:fa:ad:37:56:1d | 10.128.2.129 | 0       | --- | False       | Done   | Done   | 
| 4  | E    | blue [15476] | subnet-0 [7581]  | 10.10.10.4/32 | ce:68:ae:48:23:52 | 10.128.0.135 | 0       | --- | False       | Done   | Done   | 
| 5  | P    | red [15477]  | subnet-0 [58678] | 20.20.21.0/24 |                   | 0.0.0.0      | 0       | 0   | False       | Done   | Done   | 
| 6  | E    | red [15477]  | subnet-1 [58679] | 20.20.21.4/32 | f6:ba:77:ee:88:a4 | 10.128.0.248 | 0       | --- | False       | Done   | Done   | 
| 7  | P    | red [15477]  | subnet-1 [58679] | 20.20.20.0/24 |                   | 0.0.0.0      | 0       | 0   | False       | Done   | Done   | 
+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
```

## Example

```
# iserver create k8s vm --namespace b --name vm4 --template cirros --network pod --network pnet,blue,10.10.10.4 --network pnet,red,20.20.21.4

OpenShift Workflow - Virtual Machine - Create
=============================================

OpenShift Cluster: bm1

Create VirtualMachine
---------------------
- namespace: b
- name: vm4

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  labels:
    app: vm4
  name: vm4
  namespace: b
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: vm4
      namespace: b
    spec:
      pvc:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 500Mi
        volumeMode: Filesystem
      source:
        registry:
          url: docker://quay.io/kubevirt/cirros-container-disk-demo
  runStrategy: Always
  template:
    metadata:
      annotations:
        privnet.isovalent.com/secondary-network-attachments: '[{"network": "blue",
          "ipv4": "10.10.10.4"}, {"network": "red", "ipv4": "20.20.21.4"}]'
      labels:
        kubevirt.io/domain: vm4
    spec:
      domain:
        cpu:
          cores: 1
          sockets: 1
          threads: 1
        devices:
          disks:
          - disk:
              bus: virtio
            name: rootdisk
          interfaces:
          - masquerade: {}
            name: default
          - bridge: {}
            name: eth1
          - bridge: {}
            name: eth2
          rng: {}
        resources:
          requests:
            memory: 1Gi
      evictionStrategy: LiveMigrate
      hostname: vm4
      networks:
      - name: default
        pod: {}
      - multus:
          networkName: b/blue-subnet-0
        name: eth1
      - multus:
          networkName: b/red-subnet-1
        name: eth2
      volumes:
      - dataVolume:
          name: vm4
        name: rootdisk
~~~
VirtualMachine [b/vm4] created
Wait for data volume b/vm4 uploaded...
Wait for VirtualMachine b/vm4 [timeout:60s]
Wait for VirtualMachine b/vm4 [timeout:360s] with {"status": "Running"}

+----+-----------------+-----+--------+----------+----------------+---------+--------------+------+
| ID | Virtual Machine | CPU | Memory | Disk     | Interface      | Status  | Restart Reqd | Age  |
+----+-----------------+-----+--------+----------+----------------+---------+--------------+------+
| 1  | b               | 1   | 1Gi    | rootdisk | default (masq) | Running | ✗            | 2h2m | 
|    | vm4             |     |        |          | eth1           |         |              |      | 
|    |                 |     |        |          | eth2           |         |              |      | 
+----+-----------------+-----+--------+----------+----------------+---------+--------------+------+

+----+-------------+-------+-----+-----+----------------------+-----+--------------------------------------------+---------+------+
| ID | VM Instance | Node  | CPU | Mem | Disk                 | PVC | Interface                                  | State   | Age  |
+----+-------------+-------+-----+-----+----------------------+-----+--------------------------------------------+---------+------+
| 1  | b           | bm1-2 | 1   | 1Gi | rootdisk/vda - 500Mi | vm4 | [default] 10.128.0.220 (pod:masq)          | Running | 2h2m | 
|    | vm4         |       |     |     |                      |     | [eth1] 10.10.10.4 (multus:b/blue-subnet-0) |         |      | 
|    |             |       |     |     |                      |     | [eth2] 20.20.21.4 (multus:b/red-subnet-1)  |         |      | 
+----+-------------+-------+-----+-----+----------------------+-----+--------------------------------------------+---------+------+

Completed tasks
- Virtual machine created

+----+---------+--------+-----------+---------+---------+--------------+
| ID | Target  | Scope  | Workflow  | Changes | Success | Duration [s] |
+----+---------+--------+-----------+---------+---------+--------------+
| 1  | ocp:bm1 | ocp-vm | create vm | 1       | ✓       | 146          | 
+----+---------+--------+-----------+---------+---------+--------------+
```

[[Back]](./README.md) [[Next]](./p5.md) [[Prev]](./vm3.md)