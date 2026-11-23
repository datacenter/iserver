# Private Network - east-west connectivity test

[[Back]](./README.md) [[Next]](./commands.md) [[Prev]](./p5.md)

![Overview](../../images/pnet/ew.png)

## vm6 - primary privnet:red subnet-0, secondary privnet:red subnet-1

Combination of
- primary connection to privnet as in [vm3](./vm3.md)
- secondary connection to privnet as in [vm4](./vm4.md)

```shell
iserver create k8s vm --namespace d --name vm6 --template cirros \
    --network pnet,red,20.20.20.6 \
    --network pnet,red,20.20.21.6
```

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  labels:
    app: vm6
  name: vm6
  namespace: d
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: vm6
      namespace: d
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
        privnet.isovalent.com/network-attachment: '{"network": "red", "ipv4": "20.20.20.6"}'
        privnet.isovalent.com/secondary-network-attachments: '[{"network": "red",
          "ipv4": "20.20.21.6"}]'
      labels:
        kubevirt.io/domain: vm6
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
          - bridge: {}
            name: default
          - bridge: {}
            name: eth1
          rng: {}
        resources:
          requests:
            memory: 1Gi
      evictionStrategy: LiveMigrate
      hostname: vm6
      networks:
      - name: default
        pod: {}
      - multus:
          networkName: d/red-subnet-1
        name: eth1
      volumes:
      - dataVolume:
          name: vm6
        name: rootdisk
```

## IP Stack

>[!CAUTION]
>Multus interfaces are **not** automatically configured with ip settings. The changes can be done via CLI or wrapped into cloud-init / network-data startup files.

```
$ ip a
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc pfifo_fast qlen 1000
    link/ether 02:3a:45:71:dd:f9 brd ff:ff:ff:ff:ff:ff
    inet 20.20.20.6/32 brd 20.255.255.255 scope global eth0
3: eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop qlen 1000
    link/ether fe:92:d8:74:ee:5b brd ff:ff:ff:ff:ff:ff
```

### Add privne:red subnet-1

```
sudo ip addr add 20.20.21.6/32 dev eth1
sudo ifconfig eth1 up
sudo ip route add 20.20.21.0/24 via 169.254.0.2 dev eth1 onlink
```

### Test connectivity

```
$ ip a
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc pfifo_fast qlen 1000
    link/ether 02:3a:45:71:dd:f9 brd ff:ff:ff:ff:ff:ff
    inet 20.20.20.6/32 brd 20.255.255.255 scope global eth0
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast qlen 1000
    link/ether fe:92:d8:74:ee:5b brd ff:ff:ff:ff:ff:ff
    inet 20.20.21.6/32 scope global eth1
```

```
$ ip r
default via 169.254.0.1 dev eth0 
20.20.21.0/24 via 169.254.0.2 dev eth1 onlink 
169.254.0.1 dev eth0 
```

```
$ ping 20.20.20.5 -c 1
PING 20.20.20.5 (20.20.20.5): 56 data bytes
64 bytes from 20.20.20.5: seq=0 ttl=63 time=0.315 ms

$ ping 20.20.21.4 -c 1
PING 20.20.21.4 (20.20.21.4): 56 data bytes
64 bytes from 20.20.21.4: seq=0 ttl=63 time=0.551 ms
```

## eBPF (delta)

Every privnet connection triggers single endpoint and map entry

```
Cilium Agent Database
---------------------
- network  : 2
- subnet   : 3
- route    : 5
- inb      : 0
- endpoint : 9 (+2)
- map      : 11 (+2)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+-----------------+----------+-----------+----------------------------------------+------------+-------------------+--------------+-------+----------+
| ID | Private Network | Subnet   | Namespace | Name                                   | IP         | MAC               | POD IP       | Node  | External |
+----+-----------------+----------+-----------+----------------------------------------+------------+-------------------+--------------+-------+----------+
| 8  | red             | subnet-1 | d         | virt-launcher-vm6-4q58t-pod980816f36b7 | 20.20.21.6 | fe:92:d8:74:ee:5b | 10.128.3.109 | bm1-1 | False    | 
| 9  | red             | subnet-0 | d         | virt-launcher-vm6-4q58t                | 20.20.20.6 | 02:3a:45:71:dd:f9 | 10.128.3.75  | bm1-1 | False    | 
+----+-----------------+----------+-----------+----------------------------------------+------------+-------------------+--------------+-------+----------+

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-mapentries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
| ID | Type | Network      | Subnet           | CIDR          | MAC               | NH           | IfIndex | VNI | L2 Announce | Status | Gneigh |
+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
| 7  | E    | red [15477]  | subnet-0 [58678] | 20.20.20.6/32 | 02:3a:45:71:dd:f9 | 10.128.3.75  | 0       | --- | False       | Done   | Done   | 
| 10 | E    | red [15477]  | subnet-1 [58679] | 20.20.21.6/32 | fe:92:d8:74:ee:5b | 10.128.3.109 | 0       | --- | False       | Done   | Done   | 
+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
```

## eBPF (full)

```
Cilium Agent Database
---------------------
- network  : 2
- subnet   : 3
- route    : 5
- inb      : 0
- endpoint : 9
- map      : 11


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
| 6  | red             | subnet-0 | c         | p5-eth1                                | 20.20.20.5 | 82:cd:c3:7c:48:cb | 10.128.1.56  | bm1-2 | False    | 
| 7  | blue            | subnet-0 | c         | p5                                     | 10.10.10.5 | ea:10:6e:b3:d1:87 | 10.128.1.211 | bm1-2 | False    | 
| 8  | red             | subnet-1 | d         | virt-launcher-vm6-4q58t-pod980816f36b7 | 20.20.21.6 | fe:92:d8:74:ee:5b | 10.128.3.109 | bm1-1 | False    | 
| 9  | red             | subnet-0 | d         | virt-launcher-vm6-4q58t                | 20.20.20.6 | 02:3a:45:71:dd:f9 | 10.128.3.75  | bm1-1 | False    | 
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
| 5  | E    | blue [15476] | subnet-0 [7581]  | 10.10.10.5/32 | ea:10:6e:b3:d1:87 | 10.128.1.211 | 0       | --- | False       | Done   | Done   | 
| 6  | E    | red [15477]  | subnet-0 [58678] | 20.20.20.5/32 | 82:cd:c3:7c:48:cb | 10.128.1.56  | 0       | --- | False       | Done   | Done   | 
| 7  | E    | red [15477]  | subnet-0 [58678] | 20.20.20.6/32 | 02:3a:45:71:dd:f9 | 10.128.3.75  | 0       | --- | False       | Done   | Done   | 
| 8  | P    | red [15477]  | subnet-0 [58678] | 20.20.21.0/24 |                   | 0.0.0.0      | 0       | 0   | False       | Done   | Done   | 
| 9  | E    | red [15477]  | subnet-1 [58679] | 20.20.21.4/32 | f6:ba:77:ee:88:a4 | 10.128.0.248 | 0       | --- | False       | Done   | Done   | 
| 10 | E    | red [15477]  | subnet-1 [58679] | 20.20.21.6/32 | fe:92:d8:74:ee:5b | 10.128.3.109 | 0       | --- | False       | Done   | Done   | 
| 11 | P    | red [15477]  | subnet-1 [58679] | 20.20.20.0/24 |                   | 0.0.0.0      | 0       | 0   | False       | Done   | Done   | 
+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
```

## Example

```
# iserver create k8s vm --namespace d --name vm6 --template cirros --network pnet,red,20.20.20.6 --network pnet,red,20.20.21.6

OpenShift Workflow - Virtual Machine - Create
=============================================

OpenShift Cluster: bm1

Create VirtualMachine
---------------------
- namespace: d
- name: vm6

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  labels:
    app: vm6
  name: vm6
  namespace: d
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: vm6
      namespace: d
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
        privnet.isovalent.com/network-attachment: '{"network": "red", "ipv4": "20.20.20.6"}'
        privnet.isovalent.com/secondary-network-attachments: '[{"network": "red",
          "ipv4": "20.20.21.6"}]'
      labels:
        kubevirt.io/domain: vm6
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
          - bridge: {}
            name: default
          - bridge: {}
            name: eth1
          rng: {}
        resources:
          requests:
            memory: 1Gi
      evictionStrategy: LiveMigrate
      hostname: vm6
      networks:
      - name: default
        pod: {}
      - multus:
          networkName: d/red-subnet-1
        name: eth1
      volumes:
      - dataVolume:
          name: vm6
        name: rootdisk
~~~
VirtualMachine [d/vm6] created
Wait for data volume d/vm6 uploaded...
Wait for VirtualMachine d/vm6 [timeout:60s]
Wait for VirtualMachine d/vm6 [timeout:360s] with {"status": "Running"}

+----+-----------------+-----+--------+----------+-----------+---------+--------------+------+
| ID | Virtual Machine | CPU | Memory | Disk     | Interface | Status  | Restart Reqd | Age  |
+----+-----------------+-----+--------+----------+-----------+---------+--------------+------+
| 1  | d               | 1   | 1Gi    | rootdisk | default   | Running | ✗            | 2h0m | 
|    | vm6             |     |        |          | eth1      |         |              |      | 
+----+-----------------+-----+--------+----------+-----------+---------+--------------+------+

+----+-------------+-------+-----+-----+----------------------+-----+-------------------------------------------+---------+------+
| ID | VM Instance | Node  | CPU | Mem | Disk                 | PVC | Interface                                 | State   | Age  |
+----+-------------+-------+-----+-----+----------------------+-----+-------------------------------------------+---------+------+
| 1  | d           | bm1-1 | 1   | 1Gi | rootdisk/vda - 500Mi | vm6 | [default] 20.20.20.6 (pod)                | Running | 2h0m | 
|    | vm6         |       |     |     |                      |     | [eth1] 20.20.21.6 (multus:d/red-subnet-1) |         |      | 
+----+-------------+-------+-----+-----+----------------------+-----+-------------------------------------------+---------+------+

Completed tasks
- Virtual machine created

+----+---------+--------+-----------+---------+---------+--------------+
| ID | Target  | Scope  | Workflow  | Changes | Success | Duration [s] |
+----+---------+--------+-----------+---------+---------+--------------+
| 1  | ocp:bm1 | ocp-vm | create vm | 1       | ✓       | 81           | 
+----+---------+--------+-----------+---------+---------+--------------+
```

[[Back]](./README.md) [[Next]](./commands.md) [[Prev]](./p5.md)