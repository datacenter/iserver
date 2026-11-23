# MetalLB - Create pool

[[Back]](./README.md) [[Delete]](./delete_pool.md)

Notes:
- if `pool` parameter is not specified, pool name is generated with 'pool-' prefix
- refer [here](./kb/pool.md) for supported `addr` syntax

```
# iserver set metallb --cluster bm1 --mode pool --addr 1.1.1.1-1.1.1.1 --addr 2.2.2.0/24 --addr 3.3.3.13-3.3.3.23

OpenShift Workflow - MetalLB Operator - Create ip address pool
==============================================================

OpenShift Cluster: bm1
Operator metallb-operator found

Create IPAddressPool
--------------------
- namespace: metallb-system
- name: pool-9aed05f01a79

~~~
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: pool-9aed05f01a79
  namespace: metallb-system
spec:
  addresses:
  - 1.1.1.1-1.1.1.1
  - 2.2.2.0/24
  - 3.3.3.13-3.3.3.23

~~~
Continue [Y/N]? y
IPAddressPool [metallb-system/pool-9aed05f01a79] created
- wait for IPAddressPool metallb-system/pool-9aed05f01a79 [timeout:60s]

+----+-------------------+-------------------+-------------------------+
| ID | IP Address Pool   | Address           | Status                  |
+----+-------------------+-------------------+-------------------------+
| 1  | metallb-system    | 1.1.1.1-1.1.1.1   | {                       |
|    | pool-9aed05f01a79 | 2.2.2.0/24        |   "assignedIPv4": 1,    |
|    |                   | 3.3.3.13-3.3.3.23 |   "assignedIPv6": 0,    |
|    |                   |                   |   "availableIPv4": 267, |
|    |                   |                   |   "availableIPv6": 0    |
|    |                   |                   | }                       |
+----+-------------------+-------------------+-------------------------+

Completed tasks
- MetalLB ip address pool created
```

[[Back]](./README.md) [[Delete]](./delete_pool.md)