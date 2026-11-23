# OVNKubernetes BGP - Get BGP sessions

[[Back]](./README.md)

```
# iserver get ocp ovn-bgp --cluster bm1 -v session

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

+----+-------+---------------+---------+-------------+-----+
| ID | Node  | Pod           | Peer    | Status      | BFD |
+----+-------+---------------+---------+-------------+-----+
| 1  | bm1-1 | frr-k8s-c4jk4 | 6.6.6.6 | Established | N/A |
| 2  | bm1-1 | frr-k8s-c4jk4 | 6.6.6.7 | Established | N/A |
| 3  | bm1-2 | frr-k8s-9ckzb | 6.6.6.7 | Established | N/A |
| 4  | bm1-2 | frr-k8s-9ckzb | 6.6.6.6 | Established | N/A |
| 5  | bm1-3 | frr-k8s-zpxj6 | 6.6.6.7 | Established | N/A | 
| 6  | bm1-3 | frr-k8s-zpxj6 | 6.6.6.6 | Established | N/A |
+----+-------+---------------+---------+-------------+-----+
```

```
# iserver get ocp ovn-bgp cluster bm1 --peer 6.6.6.6 -v session

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

+----+-------+---------------+---------+-------------+-----+
| ID | Node  | Pod           | Peer    | Status      | BFD |
+----+-------+---------------+---------+-------------+-----+
| 1  | bm1-1 | frr-k8s-c4jk4 | 6.6.6.6 | Established | N/A |
| 2  | bm1-2 | frr-k8s-9ckzb | 6.6.6.6 | Established | N/A |
| 3  | bm1-3 | frr-k8s-zpxj6 | 6.6.6.6 | Established | N/A |
+----+-------+---------------+---------+-------------+-----+
```

```
# iserver get ocp ovn-bgp --cluster bm1  --peer 6.6.6.6 --node bm1-1 -v session

OpenShift Workflow - OVNKubernetes - Get frr-k8s information
============================================================

OpenShift Cluster: bm1

+----+-------+---------------+---------+-------------+-----+
| ID | Node  | Pod           | Peer    | Status      | BFD |
+----+-------+---------------+---------+-------------+-----+
| 1  | bm1-1 | frr-k8s-c4jk4 | 6.6.6.6 | Established | N/A | 
+----+-------+---------------+---------+-------------+-----+
```

[[Back]](./README.md)