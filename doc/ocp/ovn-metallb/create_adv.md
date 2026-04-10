# MetalLB - Create bgp advertisement

[[Back]](./README.md) [[Delete]](./delete_adv.md)

Notes:
- `iserver set ocp metallb --mode adv` command with user-inputs supports selected parameters only
- use `iserver set ocp file` for full flexibility of yaml definition

## Example with user inputs

```
# iserver set ocp metallb --cluster bm1 --mode adv


OpenShift Workflow - MetalLB Operator - Create bgp advertisement
================================================================

OpenShift Cluster: bm1
Operator metallb-operator found

+----+-------------------+------+
| ID | BGP Advertisement | Spec |
+----+-------------------+------+
+----+-------------------+------+

BGP advertisement crd name: adv1
IPAddressPool name: 
BGPPeer name: 
Community x:y value: 
Aggregation v4 length [0]: 
Aggregation v6 length [0]:

Create BGPAdvertisement
-----------------------
- namespace: metallb-system
- name: adv1

~~~
apiVersion: metallb.io/v1beta1
kind: BGPAdvertisement
metadata:
  name: adv1
  namespace: metallb-system
spec: {}

~~~
BGPAdvertisement [metallb-system/adv1] created
- wait for BGPAdvertisement metallb-system/adv1 [timeout:60s]

+----+-------------------+------------------------------+
| ID | BGP Advertisement | Spec                         |
+----+-------------------+------------------------------+
| 1  | metallb-system    | {                            | 
|    | adv1              |   "aggregationLength": 32,   | 
|    |                   |   "aggregationLengthV6": 128 | 
|    |                   | }                            | 
+----+-------------------+------------------------------+

Completed tasks
- MetalLB bgp advertisement defined
```

[[Back]](./README.md) [[Delete]](./delete_adv.md)