# MetalLB - Create community

[[Back]](./README.md) [[Delete]](./delete_community.md)

Notes:
- create [Community CRD](./kb/community.md)
- use `community` cli option to pass community name and value in name:x:y format
- otherwise community name and values are collected

## Example with parameter

```
# iserver set ocp metallb --cluster bm1 --mode community --community NO_ADVERTISE:65535:65282

OpenShift Workflow - MetalLB Operator - Create community
========================================================

OpenShift Cluster: bm1
Operator metallb-operator found

+----+-----------+------+
| ID | Community | Spec |
+----+-----------+------+
+----+-----------+------+


Create Community
----------------
- namespace: metallb-system
- name: community1

~~~
apiVersion: metallb.io/v1beta1
kind: Community
metadata:
  name: community1
  namespace: metallb-system
spec:
  communities:
  - name: NO_ADVERTISE
    value: 65535:65282

~~~
Community [metallb-system/community1] created
- wait for Community metallb-system/community1 [timeout:60s]

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
- MetalLB community defined
```

## Example with user inputs

```
# iserver set ocp metallb --cluster bm1 --mode community

OpenShift Workflow - MetalLB Operator - Create community
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


Create Community
----------------
- namespace: metallb-system
- name: community2

~~~
apiVersion: metallb.io/v1beta1
kind: Community
metadata:
  name: community2
  namespace: metallb-system
spec:
  communities:
  - name: my_comm
    value: 111:222

~~~
Community [metallb-system/community2] created
- wait for Community metallb-system/community2 [timeout:60s]

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

Completed tasks
- MetalLB community defined
```

[[Back]](./README.md) [[Delete]](./delete_community.md)