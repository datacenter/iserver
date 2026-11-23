# Private Network - east-west connectivity test

[[Back]](./README.md) [[Next]](./p1.md) [[Prev]](./blue.md)

![Overview](../../images/pnet/ew.png)

## Private Network "red"

```shell
iserver set ocp cilium pnet --mode network --network red --cidr4 20.20.20.0/24 --cidr4 20.20.21.0/24 --nad b --nad c --nad d
```

```yaml
apiVersion: isovalent.com/v1alpha1
kind: ClusterwidePrivateNetwork
metadata:
  name: red
spec:
  networkAttachmentDefinitions:
    namespaceSelector:
      matchExpressions:
      - key: kubernetes.io/metadata.name
        operator: In
        values:
        - b
        - c
        - d
  subnets:
  - cidrv4: 20.20.20.0/24
    name: subnet-0
  - cidrv4: 20.20.21.0/24
    name: subnet-1
```

Notes:
- [ClusterwidePrivateNetwork](../kb/crd.md) defines private network that can be used as primary or secondary attachment for PODs and KubeVirt VMs
- in case of secondary interface attachment (Multus), **networkAttachmentDefinitions** must be added selecting the namespace for which NetworkAttachmentDefinition will be created

## Network Attachment Definition

NADs auto-created for selected namespace, network and subnet names combinations.

```
+----+-------------------------------+------------+-------------------------------------------------+------+
| ID | Network Attachment Definition | Type       | Config                                          | Age  |
+----+-------------------------------+------------+-------------------------------------------------+------+
| 1  | b                             | cilium-cni | {                                               | 2h0m | 
|    | red-subnet-0                  |            |   "cniVersion": "0.3.1",                        |      | 
|    |                               |            |   "type": "cilium-cni",                         |      | 
|    |                               |            |   "enable-debug": false,                        |      | 
|    |                               |            |   "log-format": "text-ts",                      |      | 
|    |                               |            |   "log-file": "/var/run/cilium/cilium-cni.log", |      | 
|    |                               |            |   "private-networks": {                         |      | 
|    |                               |            |     "network": "red",                           |      | 
|    |                               |            |     "subnet": "subnet-0"                        |      | 
|    |                               |            |   }                                             |      | 
|    |                               |            | }                                               |      | 
+----+-------------------------------+------------+-------------------------------------------------+------+
| 2  | b                             | cilium-cni | {                                               | 2h0m | 
|    | red-subnet-1                  |            |   "cniVersion": "0.3.1",                        |      | 
|    |                               |            |   "type": "cilium-cni",                         |      | 
|    |                               |            |   "enable-debug": false,                        |      | 
|    |                               |            |   "log-format": "text-ts",                      |      | 
|    |                               |            |   "log-file": "/var/run/cilium/cilium-cni.log", |      | 
|    |                               |            |   "private-networks": {                         |      | 
|    |                               |            |     "network": "red",                           |      | 
|    |                               |            |     "subnet": "subnet-1"                        |      | 
|    |                               |            |   }                                             |      | 
|    |                               |            | }                                               |      | 
+----+-------------------------------+------------+-------------------------------------------------+------+
| 3  | c                             | cilium-cni | {                                               | 2h0m | 
|    | red-subnet-0                  |            |   "cniVersion": "0.3.1",                        |      | 
|    |                               |            |   "type": "cilium-cni",                         |      | 
|    |                               |            |   "enable-debug": false,                        |      | 
|    |                               |            |   "log-format": "text-ts",                      |      | 
|    |                               |            |   "log-file": "/var/run/cilium/cilium-cni.log", |      | 
|    |                               |            |   "private-networks": {                         |      | 
|    |                               |            |     "network": "red",                           |      | 
|    |                               |            |     "subnet": "subnet-0"                        |      | 
|    |                               |            |   }                                             |      | 
|    |                               |            | }                                               |      | 
+----+-------------------------------+------------+-------------------------------------------------+------+
| 4  | c                             | cilium-cni | {                                               | 2h0m | 
|    | red-subnet-1                  |            |   "cniVersion": "0.3.1",                        |      | 
|    |                               |            |   "type": "cilium-cni",                         |      | 
|    |                               |            |   "enable-debug": false,                        |      | 
|    |                               |            |   "log-format": "text-ts",                      |      | 
|    |                               |            |   "log-file": "/var/run/cilium/cilium-cni.log", |      | 
|    |                               |            |   "private-networks": {                         |      | 
|    |                               |            |     "network": "red",                           |      | 
|    |                               |            |     "subnet": "subnet-1"                        |      | 
|    |                               |            |   }                                             |      | 
|    |                               |            | }                                               |      | 
+----+-------------------------------+------------+-------------------------------------------------+------+
| 5  | d                             | cilium-cni | {                                               | 2h0m | 
|    | red-subnet-0                  |            |   "cniVersion": "0.3.1",                        |      | 
|    |                               |            |   "type": "cilium-cni",                         |      | 
|    |                               |            |   "enable-debug": false,                        |      | 
|    |                               |            |   "log-format": "text-ts",                      |      | 
|    |                               |            |   "log-file": "/var/run/cilium/cilium-cni.log", |      | 
|    |                               |            |   "private-networks": {                         |      | 
|    |                               |            |     "network": "red",                           |      | 
|    |                               |            |     "subnet": "subnet-0"                        |      | 
|    |                               |            |   }                                             |      | 
|    |                               |            | }                                               |      | 
+----+-------------------------------+------------+-------------------------------------------------+------+
| 6  | d                             | cilium-cni | {                                               | 2h0m | 
|    | red-subnet-1                  |            |   "cniVersion": "0.3.1",                        |      | 
|    |                               |            |   "type": "cilium-cni",                         |      | 
|    |                               |            |   "enable-debug": false,                        |      | 
|    |                               |            |   "log-format": "text-ts",                      |      | 
|    |                               |            |   "log-file": "/var/run/cilium/cilium-cni.log", |      | 
|    |                               |            |   "private-networks": {                         |      | 
|    |                               |            |     "network": "red",                           |      | 
|    |                               |            |     "subnet": "subnet-1"                        |      | 
|    |                               |            |   }                                             |      | 
|    |                               |            | }                                               |      | 
+----+-------------------------------+------------+-------------------------------------------------+------+
```

## eBPF Map (delta)

[ClusterwidePrivateNetwork](../kb/crd.md) triggers network, subnet, route and map entries in [eBPF Map](../kb/map.md)

```
Cilium Agent Database
---------------------
- network  : 2 (+1)
- subnet   : 3 (+2)
- route    : 5 (+4)
- inb      : 0
- endpoint : 0
- map      : 2 (+2)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: private-networks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+-----------------+-------+-----+--------------------------------+
| ID | Private Network | ID    | VNI | Subnet                         |
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
| 2  | red [15477]     | subnet-0 [58678] | none | 20.20.20.0/24 |        | --- | []    | 
| 3  | red [15477]     | subnet-1 [58679] | none | 20.20.21.0/24 |        | --- | []    | 
+----+-----------------+------------------+------+---------------+--------+-----+-------+

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-routes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+-----------------+----------+---------------+---------+-------+-------------------------+
| ID | Private Network | Subnet   | Destination   | Gateway | EVPN  | Peer                    |
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

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-mapentries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+------+-------------+------------------+---------------+-----+---------+---------+-----+-------------+--------+--------+
| ID | Type | Network     | Subnet           | CIDR          | MAC | NH      | IfIndex | VNI | L2 Announce | Status | Gneigh |
+----+------+-------------+------------------+---------------+-----+---------+---------+-----+-------------+--------+--------+
| 1  | P    | red [15477] | subnet-0 [58678] | 20.20.21.0/24 |     | 0.0.0.0 | 0       | 0   | False       | Done   | Done   | 
| 2  | P    | red [15477] | subnet-1 [58679] | 20.20.20.0/24 |     | 0.0.0.0 | 0       | 0   | False       | Done   | Done   | 
+----+------+-------------+------------------+---------------+-----+---------+---------+-----+-------------+--------+--------+
```

## eBPF Map (full)

```
Cilium Agent Database
---------------------
- network  : 2
- subnet   : 3
- route    : 5
- inb      : 0
- endpoint : 0
- map      : 2


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

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-mapentries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+------+-------------+------------------+---------------+-----+---------+---------+-----+-------------+--------+--------+
| ID | Type | Network     | Subnet           | CIDR          | MAC | NH      | IfIndex | VNI | L2 Announce | Status | Gneigh |
+----+------+-------------+------------------+---------------+-----+---------+---------+-----+-------------+--------+--------+
| 1  | P    | red [15477] | subnet-0 [58678] | 20.20.21.0/24 |     | 0.0.0.0 | 0       | 0   | False       | Done   | Done   | 
| 2  | P    | red [15477] | subnet-1 [58679] | 20.20.20.0/24 |     | 0.0.0.0 | 0       | 0   | False       | Done   | Done   | 
+----+------+-------------+------------------+---------------+-----+---------+---------+-----+-------------+--------+--------+
```

## Example

```
# iserver set ocp cilium pnet --mode network --network red --cidr4 20.20.20.0/24 --cidr4 20.20.21.0/24 --nad b --nad c --nad d

OpenShift Workflow - Isovalent Private Network - Create
=======================================================

OpenShift Cluster: bm1
Cilium cni found


Isovalent Private Network State
-------------------------------
- enabled : ✓
- multus  : ✓
- webhook : ✗
- crds    : ✓
- ready   : ✓


Create Clusterwide Private Network
----------------------------------
- name: red

~~~
apiVersion: isovalent.com/v1alpha1
kind: ClusterwidePrivateNetwork
metadata:
  name: red
spec:
  networkAttachmentDefinitions:
    namespaceSelector:
      matchExpressions:
      - key: kubernetes.io/metadata.name
        operator: In
        values:
        - b
        - c
        - d
  subnets:
  - cidrv4: 20.20.20.0/24
    name: subnet-0
  - cidrv4: 20.20.21.0/24
    name: subnet-1
~~~

Network created

Wait for network...

+----+-----------------------------+----------+------+---------------+--------+-----+------------------+----------------+
| ID | Clusterwide Private Network | Subnet   | DHCP | CIDRv4        | CIDRv6 | POD | Multus Namespace | NAD            |
+----+-----------------------------+----------+------+---------------+--------+-----+------------------+----------------+
| 1  | red                         | subnet-0 | none | 20.20.20.0/24 | --     | --- | b                | b/red-subnet-0 | 
|    |                             | subnet-1 | none | 20.20.21.0/24 | --     |     | c                | b/red-subnet-1 | 
|    |                             |          |      |               |        |     | d                | c/red-subnet-0 | 
|    |                             |          |      |               |        |     |                  | c/red-subnet-1 | 
|    |                             |          |      |               |        |     |                  | d/red-subnet-0 | 
|    |                             |          |      |               |        |     |                  | d/red-subnet-1 | 
+----+-----------------------------+----------+------+---------------+--------+-----+------------------+----------------+

+----+-------------------------------+------------+-------------------------------------------------+------+
| ID | Network Attachment Definition | Type       | Config                                          | Age  |
+----+-------------------------------+------------+-------------------------------------------------+------+
| 1  | b                             | cilium-cni | {                                               | 2h0m | 
|    | red-subnet-0                  |            |   "cniVersion": "0.3.1",                        |      | 
|    |                               |            |   "type": "cilium-cni",                         |      | 
|    |                               |            |   "enable-debug": false,                        |      | 
|    |                               |            |   "log-format": "text-ts",                      |      | 
|    |                               |            |   "log-file": "/var/run/cilium/cilium-cni.log", |      | 
|    |                               |            |   "private-networks": {                         |      | 
|    |                               |            |     "network": "red",                           |      | 
|    |                               |            |     "subnet": "subnet-0"                        |      | 
|    |                               |            |   }                                             |      | 
|    |                               |            | }                                               |      | 
+----+-------------------------------+------------+-------------------------------------------------+------+
| 2  | b                             | cilium-cni | {                                               | 2h0m | 
|    | red-subnet-1                  |            |   "cniVersion": "0.3.1",                        |      | 
|    |                               |            |   "type": "cilium-cni",                         |      | 
|    |                               |            |   "enable-debug": false,                        |      | 
|    |                               |            |   "log-format": "text-ts",                      |      | 
|    |                               |            |   "log-file": "/var/run/cilium/cilium-cni.log", |      | 
|    |                               |            |   "private-networks": {                         |      | 
|    |                               |            |     "network": "red",                           |      | 
|    |                               |            |     "subnet": "subnet-1"                        |      | 
|    |                               |            |   }                                             |      | 
|    |                               |            | }                                               |      | 
+----+-------------------------------+------------+-------------------------------------------------+------+
| 3  | c                             | cilium-cni | {                                               | 2h0m | 
|    | red-subnet-0                  |            |   "cniVersion": "0.3.1",                        |      | 
|    |                               |            |   "type": "cilium-cni",                         |      | 
|    |                               |            |   "enable-debug": false,                        |      | 
|    |                               |            |   "log-format": "text-ts",                      |      | 
|    |                               |            |   "log-file": "/var/run/cilium/cilium-cni.log", |      | 
|    |                               |            |   "private-networks": {                         |      | 
|    |                               |            |     "network": "red",                           |      | 
|    |                               |            |     "subnet": "subnet-0"                        |      | 
|    |                               |            |   }                                             |      | 
|    |                               |            | }                                               |      | 
+----+-------------------------------+------------+-------------------------------------------------+------+
| 4  | c                             | cilium-cni | {                                               | 2h0m | 
|    | red-subnet-1                  |            |   "cniVersion": "0.3.1",                        |      | 
|    |                               |            |   "type": "cilium-cni",                         |      | 
|    |                               |            |   "enable-debug": false,                        |      | 
|    |                               |            |   "log-format": "text-ts",                      |      | 
|    |                               |            |   "log-file": "/var/run/cilium/cilium-cni.log", |      | 
|    |                               |            |   "private-networks": {                         |      | 
|    |                               |            |     "network": "red",                           |      | 
|    |                               |            |     "subnet": "subnet-1"                        |      | 
|    |                               |            |   }                                             |      | 
|    |                               |            | }                                               |      | 
+----+-------------------------------+------------+-------------------------------------------------+------+
| 5  | d                             | cilium-cni | {                                               | 2h0m | 
|    | red-subnet-0                  |            |   "cniVersion": "0.3.1",                        |      | 
|    |                               |            |   "type": "cilium-cni",                         |      | 
|    |                               |            |   "enable-debug": false,                        |      | 
|    |                               |            |   "log-format": "text-ts",                      |      | 
|    |                               |            |   "log-file": "/var/run/cilium/cilium-cni.log", |      | 
|    |                               |            |   "private-networks": {                         |      | 
|    |                               |            |     "network": "red",                           |      | 
|    |                               |            |     "subnet": "subnet-0"                        |      | 
|    |                               |            |   }                                             |      | 
|    |                               |            | }                                               |      | 
+----+-------------------------------+------------+-------------------------------------------------+------+
| 6  | d                             | cilium-cni | {                                               | 2h0m | 
|    | red-subnet-1                  |            |   "cniVersion": "0.3.1",                        |      | 
|    |                               |            |   "type": "cilium-cni",                         |      | 
|    |                               |            |   "enable-debug": false,                        |      | 
|    |                               |            |   "log-format": "text-ts",                      |      | 
|    |                               |            |   "log-file": "/var/run/cilium/cilium-cni.log", |      | 
|    |                               |            |   "private-networks": {                         |      | 
|    |                               |            |     "network": "red",                           |      | 
|    |                               |            |     "subnet": "subnet-1"                        |      | 
|    |                               |            |   }                                             |      | 
|    |                               |            | }                                               |      | 
+----+-------------------------------+------------+-------------------------------------------------+------+

Completed tasks
- Private Network created

+----+---------+-------------+----------------+---------+---------+--------------+
| ID | Target  | Scope       | Workflow       | Changes | Success | Duration [s] |
+----+---------+-------------+----------------+---------+---------+--------------+
| 1  | ocp:bm1 | cilium-pnet | create network | 1       | ✓       | 16           | 
+----+---------+-------------+----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[Next]](./p1.md) [[Prev]](./blue.md)