# MetalLB - Delete bgp advertisement

[[Back]](./README.md) [[Create]](./create_adv.md)

Notes:
- `adv` value `__all__` selects all advertisements
- if `adv` parameter is not specified, the advertisement must be selected from the list using index

## Example with selection

```
# iserver delete ocp metallb --cluster bm1 --mode adv

OpenShift Workflow - MetalLB Operator - Delete bgp advertisement
================================================================

OpenShift Cluster: bm1
Operator metallb-operator found

+----+-------------------+------+
| ID | BGP Advertisement | Spec |
+----+-------------------+------+
| 1  | metallb-system    | {}   | 
|    | basic             |      | 
+----+-------------------+------+
Select advertisement by index (0=all): 1

Delete BGPAdvertisement
-----------------------
- namespace: metallb-system
- name: basic
- deleted
- wait for no BGPAdvertisement metallb-system/basic [timeout:60s]

+----+-------------------+------+
| ID | BGP Advertisement | Spec |
+----+-------------------+------+
+----+-------------------+------+

Completed tasks
- MetalLB bgp advertisement deleted
```

[[Back]](./README.md) [[Create]](./create_adv.md)