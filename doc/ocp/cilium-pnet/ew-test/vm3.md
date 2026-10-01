# Private Network - east-west connectivity test

[[Back]](./README.md) [[Next]](./vm4.md) [[Prev]](./p2.md)

![Overview](../../images/pnet/ew.png)

## vm3 - primary privnet:blue

Kubevirt VM primary connection to private network `X` with ipv4 address `Y` requires annotation and `bridge` mode

```yaml
spec:
  template:
    metadata:
      annotations:
        privnet.isovalent.com/network-attachment: '{"network": "X", "ipv4": "Y"}'
    spec:
      domain:
        devices:
          interfaces:
          - bridge: {}
            name: default
      networks:
      - name: default
        pod: {}
```

```shell
iserver create k8s vm --namespace b --name vm3 --template cirros --network pnet,blue,10.10.10.3
```

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  labels:
    app: vm3
  name: vm3
  namespace: b
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: vm3
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
        privnet.isovalent.com/network-attachment: '{"network": "blue", "ipv4": "10.10.10.3"}'
      labels:
        kubevirt.io/domain: vm3
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
          rng: {}
        resources:
          requests:
            memory: 1Gi
      evictionStrategy: LiveMigrate
      hostname: vm3
      networks:
      - name: default
        pod: {}
      volumes:
      - dataVolume:
          name: vm3
        name: rootdisk
```

## IP Stack

Notes:
- `eth0` with default route and /32 privnet address as per annotation
- vm3 can reach other endpoints over privnet blue in L3-way i.e., no L2 reachability

```
$ ip a
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc pfifo_fast qlen 1000
    link/ether de:fa:ad:37:56:1d brd ff:ff:ff:ff:ff:ff
    inet 10.10.10.3/32 brd 10.255.255.255 scope global eth0
```

```
$ ip r
default via 169.254.0.1 dev eth0 
169.254.0.1 dev eth0
```

```
$ ping 10.10.10.1 -c 1
PING 10.10.10.1 (10.10.10.1): 56 data bytes
64 bytes from 10.10.10.1: seq=0 ttl=63 time=0.197 ms

$ ping 10.10.10.2 -c 1
PING 10.10.10.2 (10.10.10.2): 56 data bytes
64 bytes from 10.10.10.2: seq=0 ttl=63 time=0.233 ms
```

```
$ arp -n
? (169.254.0.1) at 62:06:4a:b0:2b:68 [ether]  on eth0
```

## eBPF Map (delta)

Kubevirt VM with single privnet interface to private network triggers one endpoint and one map entry in eBPF maps

```
Cilium Agent Database
---------------------
- network  : 2
- subnet   : 3
- route    : 5
- inb      : 0
- endpoint : 3 (+1)
- map      : 5 (+1)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+-----------------+----------+-----------+-------------------------+------------+-------------------+--------------+-------+----------+
| ID | Private Network | Subnet   | Namespace | Name                    | IP         | MAC               | POD IP       | Node  | External |
+----+-----------------+----------+-----------+-------------------------+------------+-------------------+--------------+-------+----------+
| 3  | blue            | subnet-0 | b         | virt-launcher-vm3-h24s6 | 10.10.10.3 | de:fa:ad:37:56:1d | 10.128.2.129 | bm1-1 | False    | 
+----+-----------------+----------+-----------+-------------------------+------------+-------------------+--------------+-------+----------+

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-mapentries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
| ID | Type | Network      | Subnet           | CIDR          | MAC               | NH           | IfIndex | VNI | L2 Announce | Status | Gneigh |
+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
| 3  | E    | blue [15476] | subnet-0 [7581]  | 10.10.10.3/32 | de:fa:ad:37:56:1d | 10.128.2.129 | 0       | --- | False       | Done   | Done   | 
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
- endpoint : 3
- map      : 5


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

+----+-----------------+----------+-----------+-------------------------+------------+-------------------+--------------+-------+----------+
| ID | Private Network | Subnet   | Namespace | Name                    | IP         | MAC               | POD IP       | Node  | External |
+----+-----------------+----------+-----------+-------------------------+------------+-------------------+--------------+-------+----------+
| 1  | blue            | subnet-0 | a         | p1                      | 10.10.10.1 | 72:54:31:fa:5a:72 | 10.128.2.68  | bm1-1 | False    | 
| 2  | blue            | subnet-0 | a         | p2-eth1                 | 10.10.10.2 | 0e:a6:dd:6d:7d:b6 | 10.128.1.68  | bm1-2 | False    | 
| 3  | blue            | subnet-0 | b         | virt-launcher-vm3-h24s6 | 10.10.10.3 | de:fa:ad:37:56:1d | 10.128.2.129 | bm1-1 | False    | 
+----+-----------------+----------+-----------+-------------------------+------------+-------------------+--------------+-------+----------+

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-mapentries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
| ID | Type | Network      | Subnet           | CIDR          | MAC               | NH           | IfIndex | VNI | L2 Announce | Status | Gneigh |
+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
| 1  | E    | blue [15476] | subnet-0 [7581]  | 10.10.10.1/32 | 72:54:31:fa:5a:72 | 10.128.2.68  | 0       | --- | False       | Done   | Done   | 
| 2  | E    | blue [15476] | subnet-0 [7581]  | 10.10.10.2/32 | 0e:a6:dd:6d:7d:b6 | 10.128.1.68  | 0       | --- | False       | Done   | Done   | 
| 3  | E    | blue [15476] | subnet-0 [7581]  | 10.10.10.3/32 | de:fa:ad:37:56:1d | 10.128.2.129 | 0       | --- | False       | Done   | Done   | 
| 4  | P    | red [15477]  | subnet-0 [58678] | 20.20.21.0/24 |                   | 0.0.0.0      | 0       | 0   | False       | Done   | Done   | 
| 5  | P    | red [15477]  | subnet-1 [58679] | 20.20.20.0/24 |                   | 0.0.0.0      | 0       | 0   | False       | Done   | Done   | 
+----+------+--------------+------------------+---------------+-------------------+--------------+---------+-----+-------------+--------+--------+
```

## Example

```
# iserver create k8s vm --namespace b --name vm3 --template cirros --network pnet,blue,10.10.10.3

OpenShift Workflow - Virtual Machine - Create
=============================================

OpenShift Cluster: bm1

Create VirtualMachine
---------------------
- namespace: b
- name: vm3

~~~
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  labels:
    app: vm3
  name: vm3
  namespace: b
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: vm3
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
        privnet.isovalent.com/network-attachment: '{"network": "blue", "ipv4": "10.10.10.3"}'
      labels:
        kubevirt.io/domain: vm3
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
          rng: {}
        resources:
          requests:
            memory: 1Gi
      evictionStrategy: LiveMigrate
      hostname: vm3
      networks:
      - name: default
        pod: {}
      volumes:
      - dataVolume:
          name: vm3
        name: rootdisk
~~~
VirtualMachine [b/vm3] created
Wait for data volume b/vm3 uploaded...
Wait for VirtualMachine b/vm3 [timeout:60s]
Wait for VirtualMachine b/vm3 [timeout:360s] with {"status": "Running"}

+----+-----------------+-----+--------+----------+-----------+---------+--------------+------+
| ID | Virtual Machine | CPU | Memory | Disk     | Interface | Status  | Restart Reqd | Age  |
+----+-----------------+-----+--------+----------+-----------+---------+--------------+------+
| 1  | b               | 1   | 1Gi    | rootdisk | default   | Running | ✗            | 2h1m | 
|    | vm3             |     |        |          |           |         |              |      | 
+----+-----------------+-----+--------+----------+-----------+---------+--------------+------+

+----+-------------+-------+-----+-----+----------------------+-----+----------------------------+---------+------+
| ID | VM Instance | Node  | CPU | Mem | Disk                 | PVC | Interface                  | State   | Age  |
+----+-------------+-------+-----+-----+----------------------+-----+----------------------------+---------+------+
| 1  | b           | bm1-1 | 1   | 1Gi | rootdisk/vda - 500Mi | vm3 | [default] 10.10.10.3 (pod) | Running | 2h1m | 
|    | vm3         |       |     |     |                      |     |                            |         |      | 
+----+-------------+-------+-----+-----+----------------------+-----+----------------------------+---------+------+

Completed tasks
- Virtual machine created

+----+---------+--------+-----------+---------+---------+--------------+
| ID | Target  | Scope  | Workflow  | Changes | Success | Duration [s] |
+----+---------+--------+-----------+---------+---------+--------------+
| 1  | ocp:bm1 | ocp-vm | create vm | 1       | ✓       | 119          | 
+----+---------+--------+-----------+---------+---------+--------------+
```

[[Back]](./README.md) [[Next]](./vm4.md) [[Prev]](./p2.md)