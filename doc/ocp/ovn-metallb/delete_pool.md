# MetalLB - Delete pool

[[Back]](./README.md) [[Create]](./create_pool.md)

Notes:
- `pool` value `__all__` selects all pools
- if `pool` parameter is not specified, the pool must be selected from the list using index

## Example by name

```
# iserver delete metallb --cluster bm1 --mode pool --pool pool1

OpenShift Workflow - MetalLB Operator - Delete ip address pool
==============================================================

OpenShift Cluster: bm1
Operator metallb-operator found

Delete IPAddressPool
--------------------
- namespace: metallb-system
- name: pool1
- deleted
- wait for no IPAddressPool metallb-system/pool1 [timeout:60s]

Completed tasks
- MetalLB ip address pool deleted
```

## Example with selection

```
# iserver delete ocp metallb --cluster bm1 --mode pool

OpenShift Workflow - MetalLB Operator - Delete ip address pool
==============================================================

OpenShift Cluster: bm1
Operator metallb-operator found

+----+-------------------+-------------------+-------------------------+
| ID | IP Address Pool   | Address           | Status                  |
+----+-------------------+-------------------+-------------------------+
| 1  | metallb-system    | 1.1.1.1-1.1.1.1   | {                       |
|    | pool-89b95d54eeab | 2.2.2.0/24        |   "assignedIPv4": 1,    |
|    |                   | 3.3.3.13-3.3.3.23 |   "assignedIPv6": 0,    |
|    |                   |                   |   "availableIPv4": 267, | 
|    |                   |                   |   "availableIPv6": 0    |
|    |                   |                   | }                       |
+----+-------------------+-------------------+-------------------------+
Select pool by index (0=all): 1

Delete IPAddressPool
--------------------
- namespace: metallb-system
- name: pool-89b95d54eeab
- deleted
- wait for no IPAddressPool metallb-system/pool-89b95d54eeab [timeout:60s]

+----+-----------------+---------+--------+
| ID | IP Address Pool | Address | Status |
+----+-----------------+---------+--------+
+----+-----------------+---------+--------+

Completed tasks
- MetalLB ip address pool deleted
```

[[Back]](./README.md) [[Create]](./create_pool.md)