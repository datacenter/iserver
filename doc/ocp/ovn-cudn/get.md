# CUDN - Get State

[[Back]](./README.md)

```
# iserver get k8s cudn --cluster bm1
Cluster: bm1 (type: ocp)

+----+-------------+---+---+-----------+----------+--------------+---------------------------------------------------+-----------------------------------+
| ID | CUDN        | C | P | Namespace | Topology | Subnet       | Net Attach Def                                    | Workload                          |
+----+-------------+---+---+-----------+----------+--------------+---------------------------------------------------+-----------------------------------+
| 1  | msl2        | V |   | island-m1 | Layer2   | 66.66.1.0/24 | {                                                 | [VM] island-m1/c8kv1 (net1)       |
|    |             |   |   | island-m2 |          |              |   "cniVersion": "1.0.0",                          | [VM] island-m2/c8kv2 (net1)       |
|    |             |   |   |           |          |              |   "name": "cluster_udn_msl2",                     |                                   |
|    |             |   |   |           |          |              |   "netAttachDefName": "${NAMESPACE}/msl2",        |                                   |
|    |             |   |   |           |          |              |   "role": "secondary",                            |                                   | 
|    |             |   |   |           |          |              |   "subnets": "66.66.1.0/24",                      |                                   |
|    |             |   |   |           |          |              |   "topology": "layer2",                           |                                   |
|    |             |   |   |           |          |              |   "type": "ovn-k8s-cni-overlay"                   |                                   |
|    |             |   |   |           |          |              | }                                                 |                                   |
+----+-------------+---+---+-----------+----------+--------------+---------------------------------------------------+-----------------------------------+
| 2  | nsl3        | V |   | island-n1 | Layer3   | 66.66.1.0/24 | {                                                 | [VM] island-n1/c8kv1 (net1)       |
|    |             |   |   | island-n2 |          | host /28     |   "cniVersion": "1.0.0",                          | [VM] island-n2/c8kv2 (net1)       |
|    |             |   |   |           |          |              |   "name": "cluster_udn_nsl3",                     |                                   |
|    |             |   |   |           |          |              |   "netAttachDefName": "${NAMESPACE}/nsl3",        |                                   |
|    |             |   |   |           |          |              |   "role": "secondary",                            |                                   |
|    |             |   |   |           |          |              |   "subnets": "66.66.1.0/24/28",                   |                                   |
|    |             |   |   |           |          |              |   "topology": "layer3",                           |                                   |
|    |             |   |   |           |          |              |   "type": "ovn-k8s-cni-overlay"                   |                                   |
|    |             |   |   |           |          |              | }                                                 |                                   |
+----+-------------+---+---+-----------+----------+--------------+---------------------------------------------------+-----------------------------------+
| 3  | tenant-a    | V | V | island-a1 | Layer2   | 66.66.0.0/24 | {                                                 | [POD] island-a1/nginx3 (ovn-udn1) |
|    |             |   |   | island-a2 |          |              |   "cniVersion": "1.0.0",                          | [POD] island-a1/p1-1 (ovn-udn1)   |
|    |             |   |   |           |          |              |   "joinSubnet": "100.65.0.0/16,fd99::/64",        | [POD] island-a1/p1-2 (ovn-udn1)   |
|    |             |   |   |           |          |              |   "name": "cluster_udn_tenant-a",                 | [VM] island-a1/c8kv1 (default)    |
|    |             |   |   |           |          |              |   "netAttachDefName": "${NAMESPACE}/tenant-a",    | [VM] island-a1/c8kv2 (default)    |
|    |             |   |   |           |          |              |   "role": "primary",                              | [POD] island-a2/nginx3 (ovn-udn1) |
|    |             |   |   |           |          |              |   "subnets": "66.66.0.0/24",                      | [POD] island-a2/p1-1 (ovn-udn1)   |
|    |             |   |   |           |          |              |   "topology": "layer2",                           | [POD] island-a2/p1-2 (ovn-udn1)   | 
|    |             |   |   |           |          |              |   "transitSubnet": "100.88.0.0/16",               | [VM] island-a2/c8kv1 (default)    |
|    |             |   |   |           |          |              |   "type": "ovn-k8s-cni-overlay"                   | [VM] island-a2/c8kv2 (default)    |
|    |             |   |   |           |          |              | }                                                 |                                   |
+----+-------------+---+---+-----------+----------+--------------+---------------------------------------------------+-----------------------------------+

Legend: (C)reated, (P)rimary
Filter: name, topology
View:   state
```

[[Back]](./README.md)