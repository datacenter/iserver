# MetalLB - Create bfd profile

[[Back]](./README.md) [[Delete]](./delete_bfd.md)

Notes:
- `iserver set ocp metallb --mode bfd` command with user-inputs supports selected parameters only
- use `iserver set ocp file` for full flexibility of yaml definition

## Example with user inputs

```
# iserver set ocp metallb --cluster bm1 --mode bfd


OpenShift Workflow - MetalLB Operator - Create bfd profile
==========================================================

OpenShift Cluster: bm1
Operator metallb-operator found

+----+----------+------+
| ID | BGP Peer | Spec |
+----+----------+------+
+----+----------+------+

BFD profile crd name: profile1
detectMultiplier [3]: 
echoMode [F]:
- T
- F
Value:
echoInterval [50]: 
minimumTtl [254]: 
passiveMode [F]:
- T
- F
Value:
receiveInterval [300]: 
transmitInterval [300]:

Create BFDProfile
-----------------
- namespace: metallb-system
- name: profile1

~~~
apiVersion: metallb.io/v1beta1
kind: BFDProfile
metadata:
  name: profile1
  namespace: metallb-system
spec:
  detectMultiplier: 3
  echoInterval: 50
  echoMode: false
  minimumTtl: 254
  passiveMode: false
  receiveInterval: 300
  transmitInterval: 300

~~~
BFDProfile [metallb-system/profile1] created
- wait for BFDProfile metallb-system/profile1 [timeout:60s]

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

Completed tasks
- MetalLB bfd profile defined
```

[[Back]](./README.md) [[Delete]](./delete_bfd.md)