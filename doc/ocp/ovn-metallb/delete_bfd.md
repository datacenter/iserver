# MetalLB - Delete bgp bfd

[[Back]](./README.md) [[Create]](./create_bfd.md)

Notes:
- `bfd` value `__all__` selects all bfds
- if `bfd` parameter is not specified, the bfd must be selected from the list using index

## Example with selection

```
# iserver delete ocp metallb --cluster bm1 --mode bfd

OpenShift Workflow - MetalLB Operator - Delete bfd profile
==========================================================

OpenShift Cluster: bm1
Operator metallb-operator found

+----+----------------+---------------------------+
| ID | BGP Peer       | Spec                      |
+----+----------------+---------------------------+
| 1  | metallb-system | {                         |
|    | profile1       |   "detectMultiplier": 3,  |
|    |                |   "echoInterval": 50,     |
|    |                |   "echoMode": false,      |
|    |                |   "minimumTtl": 254,      |
|    |                |   "passiveMode": false,   |
|    |                |   "receiveInterval": 300, |
|    |                |   "transmitInterval": 300 |
|    |                | }                         |
+----+----------------+---------------------------+
Select bfd by index (0=all): 1

Delete BFDProfile
-----------------
- namespace: metallb-system
- name: profile1
- deleted
- wait for no BFDProfile metallb-system/profile1 [timeout:60s]

+----+----------+------+
| ID | BGP Peer | Spec |
+----+----------+------+
+----+----------+------+

Completed tasks
- MetalLB bfd profile deleted
```

[[Back]](./README.md) [[Create]](./create_bfd.md)