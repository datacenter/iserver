# MetalLB - Create bgp peer

[[Back]](./README.md) [[Delete]](./delete_peer.md)

Notes:
- `iserver set ocp metallb --mode peer` command with user-inputs supports selected parameters only
- use `iserver set ocp file` for full flexibility of yaml definition

## Example with user inputs

```
# iserver set ocp metallb --cluster bm1 --mode peer

OpenShift Workflow - MetalLB Operator - Create bgp peer
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
|    |                |   "peerAddress": "6.6.6.7",        |
|    |                |   "peerPort": 179                  |
|    |                | }                                  |
+----+----------------+------------------------------------+

BGP peer crd name: leaf1
BGP peer name already defined and will be updated
My ASN [64667]:
Peer ASN [64600]: 
Peer address [6.6.6.7]: 6.6.6.6
Multihop [T]:
- T
- F
Value:

Replace BGPPeer
---------------
- namespace: metallb-system
- name: leaf1

~~~
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  name: leaf1
  namespace: metallb-system
  resourceVersion: '18025158'
spec:
  ebgpMultiHop: true
  myASN: 64667
  peerASN: 64600
  peerAddress: 6.6.6.6

~~~
Continue [Y/N]? y
BGPPeer [metallb-system/leaf1] replaced

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

Completed tasks
- MetalLB bgp peer defined
```

[[Back]](./README.md) [[Delete]](./delete_peer.md)