# UDN w/L3 Topology - Task

[[Back]](../README.md) [[Prev]](../create/l3_crd.md) [[Next]](../get/l3.md)

## Workflow

- namespace must be udn-enabled
- no other primary udn may be defined in the namespace
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
                    "name": "p1-l3",
                    "primary": true,
                    "topology": "l3",
                    "subnets": [
                        {
                            "cidr": "66.66.0.0/24",
                            "host": 28
                        }
                    ]
                }
            ]
        }
    }
]
```

## Expected Outcome

```
# iserver get k8s udn --cluster bm1

+----+--------+---+---+---+----------+--------------+--------------------------------------------+----------+
| ID | UDN    | C | A | P | Topology | Subnet       | Net Attach Def                             | Workload |
+----+--------+---+---+---+----------+--------------+--------------------------------------------+----------+
| 1  | island | V | V | V | Layer3   | 66.66.0.0/24 | {                                          | ---      |
|    | p1-l3  |   |   |   |          | host /28     |   "cniVersion": "1.0.0",                   |          |
|    |        |   |   |   |          |              |   "joinSubnet": "100.65.0.0/16,fd99::/64", |          |
|    |        |   |   |   |          |              |   "name": "island_p1-l3",                  |          |
|    |        |   |   |   |          |              |   "netAttachDefName": "island/p1-l3",      |          |
|    |        |   |   |   |          |              |   "role": "primary",                       |          |
|    |        |   |   |   |          |              |   "subnets": "66.66.0.0/24/28",            |          |
|    |        |   |   |   |          |              |   "topology": "layer3",                    |          |
|    |        |   |   |   |          |              |   "type": "ovn-k8s-cni-overlay"            |          |
|    |        |   |   |   |          |              | }                                          |          |
+----+--------+---+---+---+----------+--------------+--------------------------------------------+----------+

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
- name: p1-l3

~~~
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: p1-l3
  namespace: island
spec:
  layer3:
    role: Primary
    subnets:
    - cidr: 66.66.0.0/24
      hostSubnet: 28
  topology: Layer3

~~~
UserDefinedNetwork [island/p1-l3] created
- wait for UserDefinedNetwork island/p1-l3 [timeout:60s]
- wait for UserDefinedNetwork island/p1-l3 [timeout:60s] with {"created_status": "True"}
- wait for UserDefinedNetwork island/p1-l3 [timeout:60s] with {"allocated_status": "True"}

+----+--------+---+---+---+----------+--------------+--------------------------------------------+----------+
| ID | UDN    | C | A | P | Topology | Subnet       | Net Attach Def                             | Workload |
+----+--------+---+---+---+----------+--------------+--------------------------------------------+----------+
| 1  | island | V | V | V | Layer3   | 66.66.0.0/24 | {                                          | ---      | 
|    | p1-l3  |   |   |   |          | host /28     |   "cniVersion": "1.0.0",                   |          | 
|    |        |   |   |   |          |              |   "joinSubnet": "100.65.0.0/16,fd99::/64", |          | 
|    |        |   |   |   |          |              |   "name": "island_p1-l3",                  |          | 
|    |        |   |   |   |          |              |   "netAttachDefName": "island/p1-l3",      |          | 
|    |        |   |   |   |          |              |   "role": "primary",                       |          | 
|    |        |   |   |   |          |              |   "subnets": "66.66.0.0/24/28",            |          | 
|    |        |   |   |   |          |              |   "topology": "layer3",                    |          | 
|    |        |   |   |   |          |              |   "type": "ovn-k8s-cni-overlay"            |          | 
|    |        |   |   |   |          |              | }                                          |          | 
+----+--------+---+---+---+----------+--------------+--------------------------------------------+----------+

Completed tasks
- ovn user defined network created
```

[[Back]](../README.md) [[Prev]](../create/l3_crd.md) [[Next]](../get/l3.md)