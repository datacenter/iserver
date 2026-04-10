# MetalLB - Wipe all crds

[[Back]](./README.md)

Notes:
- runs [peer](./delete_peer.md), [cpmmunity](./delete_community.md), [bfd](./delete_bfd.md), [advertisement](./delete_adv.md), [pool](./delete_pool.md) with `__all__` input value

## Example

```
# iserver delete metallb --cluster bm1 --mode wipe

OpenShift Workflow - MetalLB Operator - Delete bgp peer
=======================================================

OpenShift Cluster: bm1
Operator metallb-operator found

+----+----------------+------------------------------------+
| ID | BGP Peer       | Spec                               |
+----+----------------+------------------------------------+
| 1  | metallb-system | {                                  | 
|    | leaf1          |   "disableMP": false,              | 
|    |                |   "dualStackAddressFamily": false, | 
|    |                |   "ebgpMultiHop": true,            | 
|    |                |   "myASN": 64667,                  | 
|    |                |   "peerASN": 64600,                | 
|    |                |   "peerAddress": "6.6.6.6",        | 
|    |                |   "peerPort": 179                  | 
|    |                | }                                  | 
+----+----------------+------------------------------------+

Delete BGPPeer
--------------
- namespace: metallb-system
- name: leaf1
- deleted
- wait for no BGPPeer metallb-system/leaf1 [timeout:60s]

+----+----------+------+
| ID | BGP Peer | Spec |
+----+----------+------+
+----+----------+------+

Completed tasks
- MetalLB bgp peer deleted

OpenShift Workflow - MetalLB Operator - Delete community
========================================================

OpenShift Cluster: bm1
Operator metallb-operator found

+----+----------------+-------------------------------+
| ID | Community      | Spec                          |
+----+----------------+-------------------------------+
| 1  | metallb-system | {                             | 
|    | community1     |   "communities": [            | 
|    |                |     {                         | 
|    |                |       "name": "NO_ADVERTISE", | 
|    |                |       "value": "65535:65282"  | 
|    |                |     }                         | 
|    |                |   ]                           | 
|    |                | }                             | 
+----+----------------+-------------------------------+

Delete Community
----------------
- namespace: metallb-system
- name: community1
- deleted
- wait for no Community metallb-system/community1 [timeout:60s]

+----+-----------+------+
| ID | Community | Spec |
+----+-----------+------+
+----+-----------+------+

Completed tasks
- MetalLB community deleted

OpenShift Workflow - MetalLB Operator - Delete bgp advertisement
================================================================

OpenShift Cluster: bm1
Operator metallb-operator found

+----+-------------------+-------------------------------+
| ID | BGP Advertisement | Spec                          |
+----+-------------------+-------------------------------+
| 1  | metallb-system    | {                             | 
|    | adv1              |   "aggregationLength": 32,    | 
|    |                   |   "aggregationLengthV6": 128, | 
|    |                   |   "communities": [            | 
|    |                   |     "666:66"                  | 
|    |                   |   ]                           | 
|    |                   | }                             | 
+----+-------------------+-------------------------------+

Delete BGPAdvertisement
-----------------------
- namespace: metallb-system
- name: adv1
- deleted
- wait for no BGPAdvertisement metallb-system/adv1 [timeout:60s]

+----+-------------------+------+
| ID | BGP Advertisement | Spec |
+----+-------------------+------+
+----+-------------------+------+

Completed tasks
- MetalLB bgp advertisement deleted

OpenShift Workflow - MetalLB Operator - Delete bfd profile
==========================================================

OpenShift Cluster: bm1
Operator metallb-operator found

+----+----------+------+
| ID | BGP Peer | Spec |
+----+----------+------+
+----+----------+------+
No bfd profile found

OpenShift Workflow - MetalLB Operator - Delete ip address pool
==============================================================

OpenShift Cluster: bm1
Operator metallb-operator found

+----+-------------------+-------------------+-------------------------+
| ID | IP Address Pool   | Address           | Status                  |
+----+-------------------+-------------------+-------------------------+
| 1  | metallb-system    | 1.1.1.1-1.1.1.1   | {                       | 
|    | pool-9aed05f01a79 | 2.2.2.0/24        |   "assignedIPv4": 1,    | 
|    |                   | 3.3.3.13-3.3.3.23 |   "assignedIPv6": 0,    | 
|    |                   |                   |   "availableIPv4": 267, | 
|    |                   |                   |   "availableIPv6": 0    | 
|    |                   |                   | }                       | 
+----+-------------------+-------------------+-------------------------+

Delete IPAddressPool
--------------------
- namespace: metallb-system
- name: pool-9aed05f01a79
- deleted
- wait for no IPAddressPool metallb-system/pool-9aed05f01a79 [timeout:60s]

+----+-----------------+---------+--------+
| ID | IP Address Pool | Address | Status |
+----+-----------------+---------+--------+
+----+-----------------+---------+--------+

Completed tasks
- MetalLB ip address pool deleted
```

[[Back]](./README.md)