# UDN w/L2 Topology - Task

[[Back]](../README.md) [[Prev]](../create/l2_crd.md) [[Next]](../get/l2.md)

## Workflow

- namespace must be udn-enabled
- no other primary udn may be defined in the namespace ref. [error example](./create_l2_primary_already_exists.md)
- maximum one IPv4 and one IPv6 CIDR can be defined

## Task Example 

```
[
    {
        "k8s": {
            "items": [
                {
                    "__type__": "ovn-udn",
                    "namespace": "island",
                    "name": "p1-l2",
                    "primary": true,
                    "topology": "l2",
                    "subnets": ["66.66.0.0/24"]
                }
            ]
        }
    }
]
```

## Expected Outcome

```
# iserver get k8s udn --cluster bm1

+----+----------------------+---+---+---+----------+--------------+--------------------------------------------+----------+
| ID | User Defined Network | C | A | P | Topology | Subnet       | Net Attach Def                             | Workload |
+----+----------------------+---+---+---+----------+--------------+--------------------------------------------+----------+
| 1  | island               | V | V | V | Layer2   | 66.66.0.0/24 | {                                          | ---      |
|    | p1-l2                |   |   |   |          |              |   "cniVersion": "1.0.0",                   |          |
|    |                      |   |   |   |          |              |   "joinSubnet": "100.65.0.0/16,fd99::/64", |          |
|    |                      |   |   |   |          |              |   "name": "island_p1-l2",                  |          |
|    |                      |   |   |   |          |              |   "netAttachDefName": "island/p1-l2",      |          |
|    |                      |   |   |   |          |              |   "role": "primary",                       |          |
|    |                      |   |   |   |          |              |   "subnets": "66.66.0.0/24",               |          |
|    |                      |   |   |   |          |              |   "topology": "layer2",                    |          |
|    |                      |   |   |   |          |              |   "transitSubnet": "100.88.0.0/16",        |          |
|    |                      |   |   |   |          |              |   "type": "ovn-k8s-cni-overlay"            |          |
|    |                      |   |   |   |          |              | }                                          |          |
+----+----------------------+---+---+---+----------+--------------+--------------------------------------------+----------+

Legend: (C)reated, (A)llocated, (P)rimary
```

## Task Outcome Example

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm
Cluster: bm1 (type: ocp)

Kubernetes Workflow - OVN User Defined Network - Create
=======================================================

OpenShift Cluster: bm1

Create UserDefinedNetwork
-------------------------
- namespace: island
- name: p1-l2

~~~
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: p1-l2
  namespace: island
spec:
  layer2:
    role: Primary
    subnets:
    - 66.66.0.0/24
  topology: Layer2

~~~

UserDefinedNetwork [island/p1-l2] created
- wait for UserDefinedNetwork island/p1-l2 [timeout:60s]
- wait for UserDefinedNetwork island/p1-l2 [timeout:60s] with {"created_status": "True"}
- wait for UserDefinedNetwork island/p1-l2 [timeout:60s] with {"allocated_status": "True"}

+----+----------------------+---+---+---+----------+--------------+--------------------------------------------+----------+
| ID | User Defined Network | C | A | P | Topology | Subnet       | Net Attach Def                             | Workload |
+----+----------------------+---+---+---+----------+--------------+--------------------------------------------+----------+
| 1  | island               | V | V | V | Layer2   | 66.66.0.0/24 | {                                          | ---      |
|    | p1-l2                |   |   |   |          |              |   "cniVersion": "1.0.0",                   |          |
|    |                      |   |   |   |          |              |   "joinSubnet": "100.65.0.0/16,fd99::/64", |          |
|    |                      |   |   |   |          |              |   "name": "island_p1-l2",                  |          |
|    |                      |   |   |   |          |              |   "netAttachDefName": "island/p1-l2",      |          |
|    |                      |   |   |   |          |              |   "role": "primary",                       |          | 
|    |                      |   |   |   |          |              |   "subnets": "66.66.0.0/24",               |          |
|    |                      |   |   |   |          |              |   "topology": "layer2",                    |          |
|    |                      |   |   |   |          |              |   "transitSubnet": "100.88.0.0/16",        |          |
|    |                      |   |   |   |          |              |   "type": "ovn-k8s-cni-overlay"            |          |
|    |                      |   |   |   |          |              | }                                          |          |
+----+----------------------+---+---+---+----------+--------------+--------------------------------------------+----------+

Completed tasks
- ovn user defined network created
```

[[Back]](../README.md) [[Prev]](../create/l2_crd.md) [[Next]](../get/l2.md)