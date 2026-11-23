# MetalLB - Delete bgp peer

[[Back]](./README.md) [[Create]](./create_peer.md)

Notes:
- `peer` value `__all__` selects all peers
- if `peer` parameter is not specified, the peer must be selected from the list using index

## Example with selection

```
# iserver delete ocp metallb --cluster bm1 --mode peer

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
```

[[Back]](./README.md) [[Create]](./create_peer.md)