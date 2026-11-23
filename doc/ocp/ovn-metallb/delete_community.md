# MetalLB - Delete community

[[Back]](./README.md) [[Create]](./create_community.md)

Notes:
- delete [Community CRD](./kb/community.md) by name passed with `--community` parameter
- use `__all__` value to delete all communities
- if parameter is not defined, the selection is via cli

## Example

```
# iserver delete ocp metallb --cluster bm1 --mode community

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
| 2  | metallb-system | {                             | 
|    | community2     |   "communities": [            | 
|    |                |     {                         | 
|    |                |       "name": "my_comm",      | 
|    |                |       "value": "111:222"      | 
|    |                |     }                         | 
|    |                |   ]                           | 
|    |                | }                             | 
+----+----------------+-------------------------------+

Delete Community
----------------
- namespace: metallb-system
- name: community2
- deleted
- wait for no Community metallb-system/community2 [timeout:60s]

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

Completed tasks
- MetalLB community deleted
```

[[Back]](./README.md) [[Create]](./create_community.md)